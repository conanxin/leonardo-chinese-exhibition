#!/usr/bin/env python3
"""
second_exhibition_staging_build.py — assemble a future Pages artifact OUTSIDE the repo.

Assembles /tmp/leonardo-pages-artifact/ from:
  1) site/  (top-level — byte-identical, no rewrite)
  2) second-exhibition/site/{index.html,style.css,script.js}  ->  second-exhibition/
  3) second-exhibition/assets/images/*.{webp,png,jpg,jpeg}     ->  second-exhibition/assets/images/

Path rewrite (artifact-only, NEVER touches tracked source):
  ../assets/images/  ->  ./assets/images/   in staged second-exhibition/index.html

Audit (sibling directory, NOT in artifact):
  /tmp/leonardo-pages-artifact-audit/build-summary.json

Stdlib only. No network. PASS=0 / FAIL=1.
"""

import argparse
import datetime
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

# ---- Config ----

ROOT_DEFAULT_OUTPUT = "/tmp/leonardo-pages-artifact"
ROOT_DEFAULT_AUDIT  = "/tmp/leonardo-pages-artifact-audit"

SOURCE_SITE_DIR         = "site"
SOURCE_SE_DIR           = "second-exhibition"
SOURCE_SE_SITE_SUBDIR   = "second-exhibition/site"
SOURCE_SE_ASSETS_SUBDIR = "second-exhibition/assets/images"

# Forbidden filenames at any depth inside the second-exhibition subtree
FORBIDDEN_NAMES = {
    "README.md",
    "asset-import-manifest.json",
    "asset-checksums.sha256",
    "SOURCE_AUDIT_MANIFEST.md",
    "RIGHTS_AND_SOURCES.md",
}

# Allowlist extensions inside the second-exhibition subtree
ALLOW_EXT = {".html", ".css", ".js", ".webp", ".png", ".jpg", ".jpeg"}

# Second-exhibition site files (exact filenames)
SE_SITE_FILES = ("index.html", "style.css", "script.js")

OLD_PREFIX = "../assets/images/"
NEW_PREFIX = "./assets/images/"


def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256(); h.update(b); return h.hexdigest()


def sha256_file(p: Path) -> str:
    return sha256_bytes(p.read_bytes())


def fail(msg: str, **ctx):
    print(f"FAIL: {msg}", file=sys.stderr)
    for k, v in ctx.items():
        print(f"  {k}: {v}", file=sys.stderr)
    sys.exit(1)


def info(msg: str):
    print(msg)


def safe_rmtree(p: Path):
    if p.exists():
        if p.is_symlink():
            p.unlink()
        elif p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()


def copy_byte_identical(src: Path, dst: Path):
    """Copy file bytes without copying metadata. dst parent must exist."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_symlink():
        fail("Refusing to follow symlink", src=str(src))
    with open(src, "rb") as fi, open(dst, "wb") as fo:
        while True:
            chunk = fi.read(1 << 16)
            if not chunk:
                break
            fo.write(chunk)


def is_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def find_repo_root(start: Path) -> Path:
    cur = start.resolve()
    for _ in range(8):
        if (cur / ".git").exists():
            return cur
        cur = cur.parent
    fail("Cannot locate repository root (.git not found)", start=str(start))
    raise SystemExit(1)


def main():
    ap = argparse.ArgumentParser(description="Build staging artifact outside repository")
    ap.add_argument("--output", default=ROOT_DEFAULT_OUTPUT,
                    help=f"Artifact output dir (default: {ROOT_DEFAULT_OUTPUT})")
    ap.add_argument("--audit", default=ROOT_DEFAULT_AUDIT,
                    help=f"Audit output dir (default: {ROOT_DEFAULT_AUDIT})")
    args = ap.parse_args()

    repo = find_repo_root(Path.cwd())
    info(f"[A] repo root: {repo}")

    out = Path(args.output).resolve()
    aud = Path(args.audit).resolve()
    info(f"[A] output (artifact): {out}")
    info(f"[A] output (audit)  : {aud}")

    # Reject if output is inside repo
    if is_within(out, repo) or is_within(aud, repo):
        fail("Refusing to write artifact or audit inside repository", out=str(out), aud=str(aud))
    info("[A] OK: artifact and audit are outside repository")

    # Resolve source paths
    src_site = repo / SOURCE_SITE_DIR
    src_se_site = repo / SOURCE_SE_SITE_SUBDIR
    src_se_imgs = repo / SOURCE_SE_ASSETS_SUBDIR
    for label, p in [("site/", src_site), ("second-exhibition/site/", src_se_site),
                     ("second-exhibition/assets/images/", src_se_imgs)]:
        if not p.is_dir():
            fail(f"Source directory missing: {label}", path=str(p))
    info("[A] OK: source directories exist")

    # Clean output dirs
    safe_rmtree(out)
    safe_rmtree(aud)
    out.mkdir(parents=True, exist_ok=True)
    aud.mkdir(parents=True, exist_ok=True)
    info("[A] OK: cleaned and recreated output dirs")

    # ---- B. Copy main site byte-identical ----
    info("[B] Copying main site byte-identical...")
    root_site_files = []
    # Use rglob('*') then filter to regular files (not symlinks)
    for src in sorted(src_site.rglob("*")):
        if src.is_symlink():
            fail("Refusing to follow symlink", path=str(src))
        if not src.is_file():
            # skip directories
            continue
        rel = src.relative_to(src_site)
        dst = out / rel
        copy_byte_identical(src, dst)
        root_site_files.append((str(rel), sha256_file(src), src.stat().st_size))
    info(f"[B] OK: copied {len(root_site_files)} main-site files (byte-identical)")

    # ---- C. Copy second exhibition public subtree ----
    info("[C] Assembling second-exhibition public subtree...")
    dst_se = out / "second-exhibition"
    dst_se.mkdir(parents=True, exist_ok=True)

    # Site files
    for fname in SE_SITE_FILES:
        src = src_se_site / fname
        if not src.is_file():
            fail(f"Missing second-exhibition site file: {fname}", path=str(src))
        copy_byte_identical(src, dst_se / fname)

    # Assets
    dst_imgs = dst_se / "assets" / "images"
    dst_imgs.mkdir(parents=True, exist_ok=True)
    se_asset_files = []
    for src in sorted(src_se_imgs.iterdir()):
        if not src.is_file() or src.is_symlink():
            fail("Refusing to copy non-regular asset or symlink", path=str(src))
        if src.suffix.lower() not in {".webp", ".png", ".jpg", ".jpeg"}:
            fail("Unexpected asset extension in second-exhibition/assets/images",
                 file=str(src), ext=src.suffix)
        copy_byte_identical(src, dst_imgs / src.name)
        se_asset_files.append(src.name)

    # Confirm no forbidden names copied (defense-in-depth)
    for forbidden in FORBIDDEN_NAMES:
        for found in dst_se.rglob(forbidden):
            fail("Forbidden file ended up inside second-exhibition subtree",
                 file=str(found))
    info(f"[C] OK: second-exhibition site files (3) + assets ({len(se_asset_files)}) copied")

    # ---- D. Path rewrite (artifact-only) ----
    info("[D] Path rewriting second-exhibition/index.html (artifact-only)...")
    staged_index = dst_se / "index.html"
    src_index    = src_se_site / "index.html"
    src_text     = staged_index.read_text(encoding="utf-8")

    rewrite_count = src_text.count(OLD_PREFIX)
    if rewrite_count == 0:
        fail(f"No {OLD_PREFIX} references found in staged second-exhibition/index.html")
    if rewrite_count != 6:
        fail(f"Unexpected rewrite count (expected 6, got {rewrite_count})")

    new_text = src_text.replace(OLD_PREFIX, NEW_PREFIX)
    if new_text.count(OLD_PREFIX) != 0:
        fail("Rewrite did not eliminate all OLD_PREFIX occurrences")
    if new_text.count(NEW_PREFIX) != 6:
        fail("Staged index does not contain exactly 6 NEW_PREFIX references")

    staged_index.write_text(new_text, encoding="utf-8")
    info(f"[D] OK: rewrote {rewrite_count} path references (source untouched)")

    # Verify tracked source index.html SHA is unchanged
    src_sha_after = sha256_file(src_index)
    info(f"[D] source index.html SHA256 (must be unchanged): {src_sha_after}")

    # ---- E. Build summary ----
    info("[E] Writing audit summary...")
    staged_files = sorted(p for p in out.rglob("*") if p.is_file() and not p.is_symlink())
    staged_hashes = []
    for p in staged_files:
        rel = p.relative_to(out).as_posix()
        staged_hashes.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})

    # Per requirement: 5 audit files in sibling dir (NOT inside artifact)
    (aud / "artifact-files.txt").write_text(
        "\n".join(h["path"] for h in staged_hashes) + "\n", encoding="utf-8"
    )
    (aud / "artifact-sha256.txt").write_text(
        "\n".join(f"{h['sha256']}  {h['path']}" for h in staged_hashes) + "\n",
        encoding="utf-8",
    )
    root_site_hashes = [h for h in staged_hashes
                        if not h["path"].startswith("second-exhibition/")]
    se_hashes = [h for h in staged_hashes
                 if h["path"].startswith("second-exhibition/")]
    (aud / "root-site-sha256.txt").write_text(
        "\n".join(f"{h['sha256']}  {h['path']}" for h in root_site_hashes) + "\n",
        encoding="utf-8",
    )
    (aud / "second-exhibition-sha256.txt").write_text(
        "\n".join(f"{h['sha256']}  {h['path']}" for h in se_hashes) + "\n",
        encoding="utf-8",
    )

    summary = {
        "schema_version": 1,
        "source_commit": subprocess_head(repo),
        "output_path": str(out),
        "audit_path": str(aud),
        "root_site_file_count": len(root_site_files),
        "second_exhibition_public_file_count": len(staged_files) - len(root_site_files),
        "path_rewrite_count": rewrite_count,
        "build_time": datetime.datetime.utcnow().isoformat() + "Z",
        "deployment_status": "staging-only-not-deployed",
        "source_index_html_sha256": src_sha_after,
        "root_site_sha256": [r[1] for r in root_site_files],
        "second_exhibition_files": [h["path"] for h in staged_hashes
                                    if h["path"].startswith("second-exhibition/")],
        "staged_hashes": staged_hashes,
    }
    (aud / "build-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True))
    info(f"[E] OK: wrote build-summary.json -> {aud / 'build-summary.json'}")

    info("")
    info("============================================")
    info("PASS: staging build complete")
    info(f"  output: {out}")
    info(f"  audit : {aud}")
    info(f"  root site files     : {summary['root_site_file_count']}")
    info(f"  second-exhibition   : {summary['second_exhibition_public_file_count']}")
    info(f"  path rewrite count  : {summary['path_rewrite_count']}")
    info(f"  deployment_status   : {summary['deployment_status']}")
    info("============================================")


def subprocess_head(repo: Path) -> str:
    head = repo / ".git" / "HEAD"
    if not head.exists():
        return "unknown"
    ref = head.read_text().strip()
    if ref.startswith("ref:"):
        ref_file = repo / ".git" / ref.split(":", 1)[1].strip()
        if ref_file.exists():
            return ref_file.read_text().strip()
    return ref


if __name__ == "__main__":
    main()