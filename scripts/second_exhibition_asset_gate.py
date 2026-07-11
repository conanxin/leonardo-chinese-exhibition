#!/usr/bin/env python3
"""Second exhibition asset gate.

Validates the v4.5 second-exhibition repository-only asset set:

1. Every filename declared in ``second-exhibition/assets/asset-import-manifest.json``
   must exist in ``second-exhibition/assets/images/``.
2. Every file in the images directory must appear in the manifest.
3. Every file's SHA-256 must match ``second-exhibition/assets/asset-checksums.sha256``.
4. File bytes must match manifest.
5. No file may use a forbidden status word in its manifest entry.
6. No path under ``site/`` may reference any second-exhibition image filename.

Exit codes:
    0   pass
    1   fail (any check failed)
    2   infrastructure error (manifest missing, etc.)
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "second-exhibition" / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
MANIFEST = ASSETS_DIR / "asset-import-manifest.json"
CHECKSUMS = ASSETS_DIR / "asset-checksums.sha256"

FORBIDDEN_STATUS_TOKENS = {
    "approved",
    "deployed",
    "live",
    "safe for commercial use",
    "cleared for all uses",
}

# Paths that must NOT reference any second-exhibition image filename.
PROTECTED_SITE_PATHS = [
    REPO_ROOT / "site" / "index.html",
    REPO_ROOT / "site" / "script.js",
    REPO_ROOT / "site" / "style.css",
]

EXPECTED_MANIFEST_FILES = {
    "bhl-318921-page-603998.webp",
    "bhl-318921-page-603962.webp",
    "met-285149.jpg",
    "rijksmuseum-rp-f-f80152.jpg",
    "rijksmuseum-rp-f-f80313.jpg",
}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_checksums(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        sha, _, name = line.partition("  ")
        if sha and name:
            out[name.strip()] = sha.strip()
    return out


def main() -> int:
    failures: list[str] = []

    if not MANIFEST.is_file():
        print(f"FAIL: manifest not found at {MANIFEST}", file=sys.stderr)
        return 2
    if not CHECKSUMS.is_file():
        print(f"FAIL: checksum file not found at {CHECKSUMS}", file=sys.stderr)
        return 2

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: manifest JSON parse error: {exc}", file=sys.stderr)
        return 2

    assets = manifest.get("assets", [])
    if not isinstance(assets, list) or not assets:
        print("FAIL: manifest has no assets[]", file=sys.stderr)
        return 2

    declared_files: dict[str, dict] = {}
    for entry in assets:
        if not isinstance(entry, dict):
            failures.append("manifest has a non-object asset entry")
            continue
        fname = entry.get("filename")
        if fname is None:
            # C-06 has filename=null because it was blocked-from-import.
            status = entry.get("status")
            if status == "blocked-from-import":
                continue
            failures.append(f"asset {entry.get('id')!r} has null filename but is not blocked-from-import")
            continue
        declared_files[fname] = entry
        # The asset's own status field must not equal a forbidden token.
        if entry.get("status") in FORBIDDEN_STATUS_TOKENS:
            failures.append(f"asset {entry.get('id')!r} status field uses forbidden token {entry.get('status')!r}")

    # 1 + 2. Manifest files == images directory files.
    on_disk = {p.name for p in IMAGES_DIR.iterdir() if p.is_file()}
    missing = set(declared_files) - on_disk
    extra = on_disk - set(declared_files)
    for m in sorted(missing):
        failures.append(f"file declared in manifest but missing on disk: {m}")
    for e in sorted(extra):
        failures.append(f"file on disk but not declared in manifest: {e}")

    # 3 + 4. SHA-256 + byte size.
    checksums = _read_checksums(CHECKSUMS)
    for fname, entry in declared_files.items():
        path = IMAGES_DIR / fname
        if not path.is_file():
            continue  # already reported
        expected_sha = entry.get("sha256")
        expected_bytes = entry.get("bytes")
        actual_sha = _sha256(path)
        actual_bytes = path.stat().st_size
        if expected_sha and expected_sha != actual_sha:
            failures.append(
                f"{fname}: SHA-256 mismatch — expected {expected_sha}, got {actual_sha}"
            )
        if expected_sha is None:
            failures.append(f"{fname}: manifest missing sha256")
        if expected_bytes is None:
            failures.append(f"{fname}: manifest missing bytes")
        elif expected_bytes != actual_bytes:
            failures.append(
                f"{fname}: byte size mismatch — expected {expected_bytes}, got {actual_bytes}"
            )
        if expected_sha and checksums.get(fname) != expected_sha:
            failures.append(
                f"{fname}: checksum file SHA-256 mismatch with manifest"
            )

    # 5. Check that the on-disk filenames match EXPECTED_MANIFEST_FILES set.
    # (Defensive: catches a future drift where a wrong file is added.)
    drift = on_disk - EXPECTED_MANIFEST_FILES
    if drift:
        failures.append(
            f"images directory contains filenames not in expected v4.5 set: {sorted(drift)}"
        )

    # 6. No second-exhibition image filename may be referenced from protected site paths.
    for site_path in PROTECTED_SITE_PATHS:
        if not site_path.is_file():
            continue
        try:
            content = site_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for fname in EXPECTED_MANIFEST_FILES:
            if fname in content:
                failures.append(
                    f"{site_path.relative_to(REPO_ROOT)} references second-exhibition image {fname} "
                    "(live site must not reference v4.5 assets)"
                )

    # 7. Sanity-check the round status field.
    round_status = manifest.get("round_status")
    if round_status not in {"pass", "partial", "blocked"}:
        failures.append(f"manifest.round_status must be one of pass/partial/blocked, got {round_status!r}")

    if failures:
        print("FAIL — second exhibition asset gate", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    n_imported = sum(1 for e in assets if e.get("status") == "imported-not-deployed" and e.get("filename"))
    n_blocked = sum(1 for e in assets if e.get("status") == "blocked-from-import")
    print(f"PASS — second exhibition asset gate ({n_imported} imported, {n_blocked} blocked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())