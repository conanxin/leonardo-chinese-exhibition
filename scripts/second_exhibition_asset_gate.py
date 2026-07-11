#!/usr/bin/env python3
"""Second-exhibition asset gate (v4.5).

Run from the repository root:

    python3 scripts/second_exhibition_asset_gate.py

Exit codes:
    0   PASS — every required check holds.
    1   FAIL — at least one required check failed.
    2   INFRASTRUCTURE — manifest or required path missing.

The gate performs no network calls. It only reads files under
``second-exhibition/`` and a small set of protected site paths.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SECOND_EX = REPO_ROOT / "second-exhibition"
IMAGES_DIR = SECOND_EX / "assets" / "images"
MANIFEST = SECOND_EX / "assets" / "asset-import-manifest.json"
CHECKSUMS = SECOND_EX / "assets" / "asset-checksums.sha256"
README_MD = SECOND_EX / "README.md"
SOURCE_AUDIT = SECOND_EX / "docs" / "SOURCE_AUDIT_MANIFEST.md"
RIGHTS_DOC = SECOND_EX / "docs" / "RIGHTS_AND_SOURCES.md"

REQUIRED_CANDIDATE_IDS = ["C-01", "C-03", "C-06", "C-08", "C-09", "C-10"]
EXPECTED_FILENAMES = {
    "C-01": "bhl-318921-page-603998-c01.webp",
    "C-03": "bhl-318921-page-603962-c03.webp",
    "C-06": "smithsonian-nmnh-1529703.png",
    "C-08": "met-285149.jpg",
    "C-09": "rijksmuseum-rp-f-f80152.jpg",
    "C-10": "rijksmuseum-rp-f-f80313.jpg",
}
FORBIDDEN_STATUS_TOKENS = {
    "approved",
    "deployed",
    "live",
    "safe for commercial use",
    "cleared for all uses",
}
PROTECTED_SITE_PATHS = [
    REPO_ROOT / "site" / "index.html",
    REPO_ROOT / "site" / "script.js",
    REPO_ROOT / "site" / "style.css",
]

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC_SOI = b"\xff\xd8"
JPEG_MAGIC_EOI = b"\xff\xd9"
RIFF_MAGIC = b"RIFF"
WEBP_MAGIC = b"WEBP"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _magic_mime(path: Path) -> str | None:
    head = path.read_bytes()[:16]
    if head.startswith(PNG_MAGIC):
        return "image/png"
    if head.startswith(JPEG_MAGIC_SOI) and head.endswith(JPEG_MAGIC_EOI[:1]):
        return "image/jpeg"
    if head.startswith(JPEG_MAGIC_SOI):
        return "image/jpeg"
    if head.startswith(RIFF_MAGIC) and b"WEBP" in path.read_bytes()[8:12]:
        return "image/webp"
    return None


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
    info: list[str] = []

    # --- A. Required structure ---
    for required in (MANIFEST, CHECKSUMS, README_MD, SOURCE_AUDIT, RIGHTS_DOC):
        if not required.is_file():
            failures.append(f"A.required-structure: missing {required.relative_to(REPO_ROOT)}")
    if not IMAGES_DIR.is_dir():
        failures.append(f"A.required-structure: missing directory {IMAGES_DIR.relative_to(REPO_ROOT)}")

    if (SECOND_EX / "site").exists():
        failures.append("E.deployment-safety: second-exhibition/site/ exists but must NOT exist (deployment-safety rule)")

    if not MANIFEST.is_file():
        print("INFRASTRUCTURE — manifest missing", file=sys.stderr)
        return 2

    # --- B. Manifest ---
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL — manifest JSON parse error: {exc}", file=sys.stderr)
        return 1

    if manifest.get("deployment_status") != "repository-only-not-deployed":
        failures.append(
            f"B.manifest: deployment_status must be 'repository-only-not-deployed', got {manifest.get('deployment_status')!r}"
        )
    if manifest.get("asset_count") != 6:
        failures.append(f"B.manifest: asset_count must be 6, got {manifest.get('asset_count')!r}")
    if manifest.get("import_round") != "v4.5-asset-import":
        failures.append(
            f"B.manifest: import_round must be 'v4.5-asset-import', got {manifest.get('import_round')!r}"
        )

    assets = manifest.get("assets")
    if not isinstance(assets, list) or len(assets) != 6:
        failures.append(f"B.manifest: assets[] must contain exactly 6 entries, got {len(assets) if isinstance(assets, list) else 'n/a'}")

    by_id: dict[str, dict] = {}
    filenames_seen: set[str] = set()
    for entry in assets or []:
        cid = entry.get("candidate_id")
        if cid in REQUIRED_CANDIDATE_IDS:
            by_id[cid] = entry
        fname = entry.get("filename")
        if fname is None:
            failures.append(f"B.manifest: asset with candidate_id={cid!r} has null filename")
            continue
        if fname in filenames_seen:
            failures.append(f"B.manifest: duplicate filename {fname}")
        filenames_seen.add(fname)
        # Path confinement.
        lp = entry.get("local_path", "")
        if not lp.startswith("second-exhibition/assets/images/"):
            failures.append(
                f"B.manifest: candidate {cid} local_path {lp!r} is not confined to second-exhibition/assets/images/"
            )
        # Status field.
        if entry.get("import_status") != "imported-not-deployed":
            failures.append(
                f"B.manifest: candidate {cid} import_status must be 'imported-not-deployed', got {entry.get('import_status')!r}"
            )
        if entry.get("import_status") in FORBIDDEN_STATUS_TOKENS:
            failures.append(
                f"B.manifest: candidate {cid} import_status uses forbidden token {entry.get('import_status')!r}"
            )
        # Required fields non-empty.
        for k in ("official_source_url", "media_url", "rights_url", "identifier"):
            v = entry.get(k)
            if not v or not isinstance(v, str):
                failures.append(f"B.manifest: candidate {cid} field {k!r} must be a non-empty string")
        # Filename matches expected.
        if EXPECTED_FILENAMES.get(cid) != fname:
            failures.append(
                f"B.manifest: candidate {cid} filename must be {EXPECTED_FILENAMES.get(cid)!r}, got {fname!r}"
            )

    missing_ids = [c for c in REQUIRED_CANDIDATE_IDS if c not in by_id]
    extra_ids = [c for c in by_id if c not in REQUIRED_CANDIDATE_IDS]
    for c in missing_ids:
        failures.append(f"B.manifest: missing candidate_id {c}")
    for c in extra_ids:
        failures.append(f"B.manifest: unexpected candidate_id {c}")

    # --- C. Local files ---
    if IMAGES_DIR.is_dir():
        on_disk = {p.name for p in IMAGES_DIR.iterdir() if p.is_file()}
    else:
        on_disk = set()
    expected_filenames = set(EXPECTED_FILENAMES.values())
    missing_files = expected_filenames - on_disk
    extra_files = on_disk - expected_filenames
    for m in sorted(missing_files):
        failures.append(f"C.local-files: expected file missing: {m}")
    for e in sorted(extra_files):
        failures.append(f"C.local-files: unexpected file in images/: {e}")

    # bytes / sha256 / mime / extension / dimensions
    shas: dict[str, str] = {}
    for cid, expected_fname in EXPECTED_FILENAMES.items():
        path = IMAGES_DIR / expected_fname
        if not path.is_file():
            continue  # already reported
        entry = by_id.get(cid, {})
        actual_sha = _sha256(path)
        actual_bytes = path.stat().st_size
        actual_mime = _magic_mime(path)
        shas[expected_fname] = actual_sha
        ext = path.suffix.lower()
        # bytes
        if entry.get("bytes") != actual_bytes:
            failures.append(
                f"C.local-files: {expected_fname}: bytes mismatch — manifest={entry.get('bytes')}, actual={actual_bytes}"
            )
        # sha256
        if entry.get("sha256") != actual_sha:
            failures.append(
                f"C.local-files: {expected_fname}: SHA-256 mismatch — manifest={entry.get('sha256')}, actual={actual_sha}"
            )
        # mime
        if entry.get("mime_type") and actual_mime and entry["mime_type"] != actual_mime:
            failures.append(
                f"C.local-files: {expected_fname}: mime_type mismatch — manifest={entry.get('mime_type')}, magic-bytes={actual_mime}"
            )
        if not actual_mime:
            failures.append(f"C.local-files: {expected_fname}: magic bytes do not look like a real image")
        # extension matches mime
        ext_to_mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}
        expected_mime_for_ext = ext_to_mime.get(ext)
        if actual_mime and expected_mime_for_ext and actual_mime != expected_mime_for_ext:
            failures.append(
                f"C.local-files: {expected_fname}: extension {ext} (implies {expected_mime_for_ext}) does not match actual mime {actual_mime}"
            )
        # dimensions
        w = entry.get("width")
        h = entry.get("height")
        if w is not None and isinstance(w, int) and w <= 0:
            failures.append(f"C.local-files: {expected_fname}: manifest width must be > 0")
        if h is not None and isinstance(h, int) and h <= 0:
            failures.append(f"C.local-files: {expected_fname}: manifest height must be > 0")

    # Six SHA256 values unique.
    if len(shas) != 6:
        failures.append(f"C.local-files: expected 6 distinct SHA-256, got {len(shas)}")
    else:
        if len(set(shas.values())) != 6:
            failures.append("C.local-files: six SHA-256 values must be unique")
    # C-01 / C-03 SHA distinct.
    c01_sha = shas.get(EXPECTED_FILENAMES["C-01"])
    c03_sha = shas.get(EXPECTED_FILENAMES["C-03"])
    if c01_sha and c03_sha and c01_sha == c03_sha:
        failures.append("C.local-files: C-01 and C-03 SHA-256 must differ")

    # --- D. Checksums file ---
    if CHECKSUMS.is_file():
        checksums = _read_checksums(CHECKSUMS)
        if len(checksums) != 6:
            failures.append(f"D.checksums: asset-checksums.sha256 must contain exactly 6 entries, got {len(checksums)}")
        for fname, sha in checksums.items():
            actual_sha = shas.get(Path(fname).name)
            if actual_sha and sha != actual_sha:
                failures.append(
                    f"D.checksums: {fname}: checksum file value {sha} does not match actual file SHA {actual_sha}"
                )
    # All six expected filenames must appear in the checksum file (with the repo-root prefix).
    if CHECKSUMS.is_file():
        text = CHECKSUMS.read_text(encoding="utf-8")
        for fname in EXPECTED_FILENAMES.values():
            expected_path = f"second-exhibition/assets/images/{fname}"
            if expected_path not in text:
                failures.append(f"D.checksums: checksum file missing entry for {expected_path}")

    # --- E. Deployment safety ---
    for site_path in PROTECTED_SITE_PATHS:
        if not site_path.is_file():
            continue
        try:
            content = site_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for fname in EXPECTED_FILENAMES.values():
            if fname in content:
                failures.append(
                    f"E.deployment-safety: {site_path.relative_to(REPO_ROOT)} references second-exhibition image {fname}"
                )

    if README_MD.is_file():
        text = README_MD.read_text(encoding="utf-8")
        if "repository-only" not in text.lower():
            failures.append("E.deployment-safety: second-exhibition/README.md must state repository-only status")
        if "not deployed" not in text.lower():
            failures.append("E.deployment-safety: second-exhibition/README.md must state not-deployed status")

    if failures:
        print("FAIL — second exhibition asset gate", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    info.append(f"asset_count = 6")
    info.append(f"deployment_status = repository-only-not-deployed")
    info.append(f"all six SHA-256 unique")
    info.append(f"C-01 and C-03 SHA-256 differ")
    info.append(f"all six files present in second-exhibition/assets/images/")
    info.append(f"asset-checksums.sha256 contains exactly 6 entries")
    info.append(f"no protected site path references any v4.5 image filename")
    info.append(f"second-exhibition/site/ does not exist")
    info.append(f"no manifest asset status equals a forbidden token")
    print("PASS — second exhibition asset gate")
    for line in info:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())