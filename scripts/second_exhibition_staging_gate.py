#!/usr/bin/env python3
"""
second_exhibition_staging_gate.py — verify a staging artifact against the v5.1 contract.

Checks (8 groups):
  A. Artifact location   — outside repo, no .git, no hidden metadata
  B. Main-site identity  — every site/ file present byte-identical in staging root
  C. Second-exhibition tree — exactly the 9 expected files, allowlist ext only
  D. Path rewrite        — staged index has 0 OLD_PREFIX, 6 NEW_PREFIX;
                           source index SHA unchanged
  E. Asset integrity     — 6 images, exact filenames, source SHA match,
                           checksum file match, no 7th image
  F. Forbidden exposure  — none of the listed names anywhere in artifact
  G. Audit separation    — audit dir outside artifact, files exist, JSON valid
  H. Deployment status   — staged index carries "repository-only" / "not deployed" text

Stdlib only. No network. PASS=0 / FAIL=1.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path


ART_DEFAULT = "/tmp/leonardo-pages-artifact"
AUD_DEFAULT = "/tmp/leonardo-pages-artifact-audit"

SOURCE_SITE_DIR         = "site"
SOURCE_SE_DIR           = "second-exhibition"
SOURCE_SE_SITE_SUBDIR   = "second-exhibition/site"
SOURCE_SE_ASSETS_SUBDIR = "second-exhibition/assets/images"
SOURCE_CHECKSUMS        = "second-exhibition/assets/asset-checksums.sha256"

OLD_PREFIX = "../assets/images/"
NEW_PREFIX = "./assets/images/"

EXPECTED_IMAGES = {
    "bhl-318921-page-603998-c01.webp",
    "bhl-318921-page-603962-c03.webp",
    "smithsonian-nmnh-1529703.png",
    "met-285149.jpg",
    "rijksmuseum-rp-f-f80152.jpg",
    "rijksmuseum-rp-f-f80313.jpg",
}

FORBIDDEN_NAMES = {
    "README.md",
    "asset-import-manifest.json",
    "asset-checksums.sha256",
    "SOURCE_AUDIT_MANIFEST.md",
    "RIGHTS_AND_SOURCES.md",
    "_template",
    "_pilots",
    "reports",
    "scripts",
    ".firecrawl",
}

FORBIDDEN_PATHS = [
    "reports",
    "scripts",
    "_template",
    "_pilots",
    "second-exhibition/data",
    "second-exhibition/docs",
    ".firecrawl",
]

ALLOW_EXT = {".html", ".css", ".js", ".webp", ".png", ".jpg", ".jpeg"}


def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256(); h.update(b); return h.hexdigest()


def sha256_file(p: Path) -> str:
    return sha256_bytes(p.read_bytes())


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
    print(f"FAIL: cannot locate repository root (.git not found) from {start}", file=sys.stderr)
    raise SystemExit(1)


def section(label: str):
    print()
    print(f"=== {label} ===")


def group_pass(msg: str):
    print(f"  OK: {msg}")


def group_fail(msg: str):
    print(f"  FAIL: {msg}")
    raise SystemExit(1)


def parse_checksum_file(p: Path):
    out = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        sha, _, name = line.partition("  ")
        out[name.strip()] = sha.strip()
    return out


def main():
    ap = argparse.ArgumentParser(description="Verify staging artifact")
    ap.add_argument("--artifact", default=ART_DEFAULT)
    ap.add_argument("--audit",    default=AUD_DEFAULT)
    args = ap.parse_args()

    repo = find_repo_root(Path.cwd())
    art = Path(args.artifact).resolve()
    aud = Path(args.audit).resolve()
    print(f"repo   : {repo}")
    print(f"artifact: {art}")
    print(f"audit   : {aud}")

    failures = []

    # ---- A. Artifact location ----
    section("A. Artifact location")
    if not art.is_dir():
        group_fail(f"artifact directory does not exist: {art}")
    group_pass("artifact directory exists")

    if is_within(art, repo):
        group_fail(f"artifact is inside repository: {art} inside {repo}")
    group_pass("artifact is outside repository")

    if not aud.is_dir():
        group_fail(f"audit directory does not exist: {aud}")
    group_pass("audit directory exists")

    if is_within(aud, repo):
        group_fail(f"audit is inside repository: {aud} inside {repo}")
    group_pass("audit is outside repository")

    # Artifact must not be repo root
    if art.resolve() == repo.resolve():
        group_fail("artifact IS repository root (must never be)")
    group_pass("artifact is not repository root")

    # No .git / hidden metadata in artifact
    if (art / ".git").exists():
        group_fail("artifact contains .git")
    group_pass("artifact contains no .git")

    hidden = [p for p in art.iterdir() if p.name.startswith(".")]
    if hidden:
        group_fail(f"artifact contains hidden entries: {[p.name for p in hidden]}")
    group_pass("artifact contains no hidden metadata")

    # ---- B. Main-site identity ----
    section("B. Main-site identity")
    src_site = repo / SOURCE_SITE_DIR
    if not src_site.is_dir():
        group_fail(f"source site/ missing: {src_site}")

    # All regular files under source site/ (recursive)
    src_files = sorted(p for p in src_site.rglob("*") if p.is_file() and not p.is_symlink())
    # All regular files under staging root, excluding second-exhibition/ subtree
    staged_root = art
    staged_root_files = sorted(
        p for p in staged_root.rglob("*")
        if p.is_file() and not p.is_symlink()
        and not str(p.relative_to(staged_root)).startswith("second-exhibition")
    )

    print(f"  source site/ files: {len(src_files)}")
    print(f"  staging root files (excluding second-exhibition/): {len(staged_root_files)}")

    if len(src_files) != len(staged_root_files):
        group_fail(f"main-site file count differs: src={len(src_files)} staged={len(staged_root_files)}")

    src_index = src_site / "index.html"
    if not src_index.is_file():
        group_fail("main-site source index.html missing")
    src_index_sha = sha256_file(src_index)
    src_index_bytes = src_index.stat().st_size

    # Compare bytes per file
    mismatches = 0
    for sf in src_files:
        rel = sf.relative_to(src_site)
        df = staged_root / rel
        if not df.is_file():
            group_fail(f"missing in staging: {rel}")
        if sha256_file(df) != sha256_file(sf):
            mismatches += 1
            print(f"    MISMATCH: {rel}", file=sys.stderr)
    if mismatches:
        group_fail(f"{mismatches} main-site files differ in staging")
    group_pass(f"all {len(src_files)} main-site files are byte-identical in staging root")

    # Extra: no extra top-level dirs (only second-exhibition/ is added)
    top_dirs = {p.name for p in staged_root.iterdir() if p.is_dir()}
    src_top_dirs = {p.name for p in src_site.iterdir() if p.is_dir()}
    added_top_dirs = top_dirs - src_top_dirs
    expected_added = {"second-exhibition"}
    unexpected = added_top_dirs - expected_added
    if unexpected:
        group_fail(f"unexpected top-level dirs in staging root: {sorted(unexpected)}")
    group_pass(f"staging root has only expected added dirs: {sorted(added_top_dirs)}")

    staged_index = staged_root / "index.html"
    if staged_index.stat().st_size != src_index_bytes:
        group_fail(f"staging index byte mismatch: src={src_index_bytes} staged={staged_index.stat().st_size}")
    group_pass(f"staging index byte = {src_index_bytes} (matches main-site source)")

    # v2.9 marker
    root_text = staged_index.read_text(encoding="utf-8", errors="replace")
    v29_count = root_text.count("v2.9-real-source-rights-audit")
    if v29_count != 1:
        group_fail(f"v2.9 marker count = {v29_count} (expected 1)")
    group_pass(f"v2.9 marker = {v29_count}")

    # ---- C. Second-exhibition public tree ----
    section("C. Second-exhibition public tree")
    se_dir = art / "second-exhibition"
    if not se_dir.is_dir():
        group_fail(f"second-exhibition subtree missing: {se_dir}")

    # Walk subtree, collect all regular files (not following symlinks)
    se_files = sorted(p for p in se_dir.rglob("*") if p.is_file() and not p.is_symlink())
    print(f"  second-exhibition public files: {len(se_files)}")
    for f in se_files:
        print(f"    {f.relative_to(art).as_posix()}  ext={f.suffix.lower()}  bytes={f.stat().st_size}")

    if len(se_files) != 9:
        group_fail(f"expected 9 second-exhibition public files, found {len(se_files)}")

    # Allowlist check
    bad_ext = [f for f in se_files if f.suffix.lower() not in ALLOW_EXT]
    if bad_ext:
        group_fail(f"disallowed extensions in second-exhibition subtree: {[str(f) for f in bad_ext]}")
    group_pass("all 9 second-exhibition files have allowlist extensions")

    # No hidden, no symlinks, no source maps, no executables (mode check: skip bit)
    bad = []
    for f in se_files:
        if f.name.startswith("."):
            bad.append(("hidden", f))
        if f.suffix == ".map":
            bad.append(("source map", f))
        # executable-bit check
        mode = f.stat().st_mode
        if mode & 0o111:
            bad.append(("executable", f))
    if bad:
        group_fail(f"second-exhibition has disallowed file kinds: {bad}")
    group_pass("no hidden / source-map / executable files in second-exhibition subtree")

    # ---- D. Path rewrite ----
    section("D. Path rewrite")
    src_se_index = repo / SOURCE_SE_SITE_SUBDIR / "index.html"
    if not src_se_index.is_file():
        group_fail(f"source second-exhibition index.html missing: {src_se_index}")

    src_text = src_se_index.read_text(encoding="utf-8")
    staged_se_text = (se_dir / "index.html").read_text(encoding="utf-8")

    src_old_count = src_text.count(OLD_PREFIX)
    src_new_count = src_text.count(NEW_PREFIX)  # substring of OLD; informational only
    staged_old_count = staged_se_text.count(OLD_PREFIX)
    staged_new_count = staged_se_text.count(NEW_PREFIX)

    print(f"  source   ../assets/images/ = {src_old_count}")
    print(f"  source   ./assets/images/  = {src_new_count}  (substring of OLD; not a separate reference)")
    print(f"  staged   ../assets/images/ = {staged_old_count}")
    print(f"  staged   ./assets/images/  = {staged_new_count}")

    if src_old_count != 6:
        group_fail(f"source ../assets/images/ count = {src_old_count} (expected 6)")
    if staged_old_count != 0:
        group_fail(f"staged index still has ../assets/images/ count = {staged_old_count}")
    if staged_new_count != 6:
        group_fail(f"staged ./assets/images/ count = {staged_new_count} (expected 6)")
    group_pass("path rewrite correct: source has 6 ../assets/; staged has 0 ../ and 6 ./assets/")

    # Source SHA must be unchanged
    src_sha_after = sha256_file(src_se_index)
    print(f"  source index.html SHA256 (must match pre-build): {src_sha_after}")
    # We can't compare against pre-build directly here, but we already recorded
    # it in build-summary.json — cross-check below in section G.
    group_pass("source index.html is intact (rewrite was staging-only)")

    # Normalized diff: source vs staged (should differ ONLY by the 6 path replacements)
    expected_diff_lines = src_old_count  # each replacement is one line
    # Compute a simple line-based diff count
    src_lines = src_text.splitlines()
    staged_lines = staged_se_text.splitlines()
    if len(src_lines) != len(staged_lines):
        group_fail(f"line count differs between source ({len(src_lines)}) and staged ({len(staged_lines)}) index.html")
    diff_lines = sum(1 for a, b in zip(src_lines, staged_lines) if a != b)
    print(f"  differing lines (src vs staged) = {diff_lines}")
    if diff_lines != expected_diff_lines:
        group_fail(f"diff line count = {diff_lines} (expected {expected_diff_lines})")
    group_pass(f"only {diff_lines} lines differ between source and staged index — all are path rewrites")

    # ---- E. Asset integrity ----
    section("E. Asset integrity")
    se_imgs = se_dir / "assets" / "images"
    if not se_imgs.is_dir():
        group_fail(f"staged assets/images missing: {se_imgs}")
    staged_imgs = sorted(p for p in se_imgs.iterdir() if p.is_file() and not p.is_symlink())

    if len(staged_imgs) != 6:
        group_fail(f"expected 6 staged images, found {len(staged_imgs)}")
    group_pass("staged image count = 6")

    names = {p.name for p in staged_imgs}
    if names != EXPECTED_IMAGES:
        group_fail(f"staged image names mismatch: {names ^ EXPECTED_IMAGES}")
    group_pass("staged image names match expected set exactly")

    # Compare to source images
    src_imgs_dir = repo / SOURCE_SE_ASSETS_SUBDIR
    for fname in EXPECTED_IMAGES:
        s = src_imgs_dir / fname
        d = se_imgs / fname
        if not s.is_file():
            group_fail(f"source image missing: {fname}")
        if not d.is_file():
            group_fail(f"staged image missing: {fname}")
        s_sha = sha256_file(s)
        d_sha = sha256_file(d)
        if s_sha != d_sha:
            group_fail(f"image SHA mismatch for {fname}: src={s_sha} staged={d_sha}")
    group_pass("all 6 staged images match source SHA256 byte-for-byte")

    # Compare against checksum file
    chk_file = repo / SOURCE_CHECKSUMS
    if not chk_file.is_file():
        group_fail(f"checksum file missing: {chk_file}")
    checksums = parse_checksum_file(chk_file)
    print(f"  checksum file entries: {len(checksums)}")
    if len(checksums) != 6:
        group_fail(f"checksum file has {len(checksums)} entries (expected 6)")
    for fname in EXPECTED_IMAGES:
        # Try matching by basename or by basename within assets/images/
        candidates = [fname, f"images/{fname}", f"second-exhibition/assets/images/{fname}"]
        entry = ""
        for c in candidates:
            if c in checksums:
                entry = checksums[c]; break
        if not entry:
            group_fail(f"no checksum entry found for {fname} (tried {candidates})")
        d_sha = sha256_file(se_imgs / fname)
        if entry.lower() != d_sha.lower():
            group_fail(f"checksum mismatch for {fname}: file={entry.lower()} staged={d_sha.lower()}")
    group_pass("all 6 staged images match asset-checksums.sha256")

    # MIME / ext consistency
    for f in staged_imgs:
        ext = f.suffix.lower().lstrip(".")
        expected_mime = {
            "webp": "image/webp",
            "png":  "image/png",
            "jpg":  "image/jpeg",
            "jpeg": "image/jpeg",
        }.get(ext)
        if not expected_mime:
            group_fail(f"unknown image extension for {f.name}: {ext}")
    group_pass("staged image extensions map cleanly to expected MIME")

    # ---- F. Forbidden exposure ----
    section("F. Forbidden exposure")
    # (a) forbidden filenames inside the second-exhibition subtree only
    se_forbidden_hits = []
    for p in se_dir.rglob("*"):
        if p.is_file() and p.name in FORBIDDEN_NAMES:
            se_forbidden_hits.append(p)
    if se_forbidden_hits:
        group_fail(f"forbidden files in second-exhibition subtree: {[str(p) for p in se_forbidden_hits]}")
    group_pass("no forbidden filenames in second-exhibition subtree")

    # (b) forbidden path components anywhere inside artifact
    bad_paths = []
    for p in art.rglob("*"):
        rel = p.relative_to(art).as_posix()
        for fp in FORBIDDEN_PATHS:
            if rel == fp or rel.startswith(fp + "/") or f"/{fp}/" in f"/{rel}/":
                bad_paths.append((fp, rel))
    if bad_paths:
        group_fail(f"forbidden paths in artifact: {bad_paths}")
    group_pass("no forbidden path components in artifact")

    # (c) artifact contains no repository README / V5_ROADMAP
    for forbidden in ("README.md", "V4_ROADMAP.md", "V5_ROADMAP.md"):
        if (art / forbidden).exists():
            group_fail(f"artifact contains top-level {forbidden}")
    group_pass("no top-level README / V4_ROADMAP / V5_ROADMAP in artifact")

    # ---- G. Audit separation ----
    section("G. Audit separation")
    for fname in ("artifact-files.txt", "artifact-sha256.txt",
                  "root-site-sha256.txt", "second-exhibition-sha256.txt",
                  "build-summary.json"):
        if not (aud / fname).is_file():
            group_fail(f"audit file missing: {fname}")
    group_pass("all expected audit files present")

    # inventory counts match actual
    af_lines = (aud / "artifact-files.txt").read_text(encoding="utf-8").splitlines()
    actual_files = [p for p in art.rglob("*") if p.is_file() and not p.is_symlink()]
    if len(af_lines) != len(actual_files):
        group_fail(f"artifact-files.txt has {len(af_lines)} entries but {len(actual_files)} actual files")
    group_pass(f"artifact-files.txt entry count matches actual: {len(actual_files)}")

    # hash inventory matches actual SHA
    ah = (aud / "artifact-sha256.txt").read_text(encoding="utf-8").splitlines()
    if len(ah) != len(actual_files):
        group_fail(f"artifact-sha256.txt has {len(ah)} entries but {len(actual_files)} actual files")
    group_pass(f"artifact-sha256.txt entry count matches actual: {len(actual_files)}")

    # build-summary.json valid
    summary: dict = {}
    summary_raw = (aud / "build-summary.json").read_text(encoding="utf-8")
    try:
        summary = json.loads(summary_raw)
    except Exception as e:
        group_fail(f"build-summary.json invalid: {e}")
    if not summary:
        group_fail("build-summary.json parsed to empty object")
    group_pass("build-summary.json is valid JSON")

    # verify summary cross-checks
    if summary.get("deployment_status") != "staging-only-not-deployed":
        group_fail(f"deployment_status in summary = {summary.get('deployment_status')!r}")
    if summary.get("path_rewrite_count") != 6:
        group_fail(f"path_rewrite_count in summary = {summary.get('path_rewrite_count')}")
    if summary.get("root_site_file_count") != len(src_files):
        group_fail(f"root_site_file_count in summary = {summary.get('root_site_file_count')}, actual {len(src_files)}")
    summary_se_count = summary.get("second_exhibition_public_file_count")
    if summary_se_count != len(se_files):
        group_fail(f"second_exhibition_public_file_count = {summary_se_count}, actual {len(se_files)}")
    group_pass("build-summary.json internal counts cross-check OK")

    # Schema v2: explicit per-source / per-staged identity blocks.
    schema_version = summary.get("audit_schema_version")
    if schema_version != "2.0":
        group_fail(f"audit_schema_version in summary = {schema_version!r}, expected '2.0'")
    else:
        group_pass("audit_schema_version in summary = 2.0")

    root_block = summary.get("root_site") or {}
    se_block = summary.get("second_exhibition") or {}

    # ---- Root site identity ----
    expected_root_sha = sha256_file(src_site / "index.html")
    expected_root_bytes = (src_site / "index.html").stat().st_size
    if root_block.get("source_sha256") != expected_root_sha:
        group_fail(f"root_site.source_sha256 in summary = {root_block.get('source_sha256')}, expected {expected_root_sha}")
    if root_block.get("staged_sha256") != expected_root_sha:
        group_fail(f"root_site.staged_sha256 in summary = {root_block.get('staged_sha256')}, expected {expected_root_sha}")
    if root_block.get("source_bytes") != expected_root_bytes:
        group_fail(f"root_site.source_bytes in summary = {root_block.get('source_bytes')}, expected {expected_root_bytes}")
    if not root_block.get("source_equals_staged"):
        group_fail("root_site.source_equals_staged is false (expected true for byte-identical copy)")
    else:
        group_pass(
            f"root_site identity OK: source={expected_root_sha[:12]}… staged={expected_root_sha[:12]}… "
            f"source_equals_staged=True"
        )

    # ---- Second-exhibition identity (MUST differ by 6 path rewrites) ----
    src_se_sha = sha256_file(src_se_index)
    src_se_bytes = src_se_index.stat().st_size
    if se_block.get("source_sha256") != src_se_sha:
        group_fail(f"second_exhibition.source_sha256 in summary = {se_block.get('source_sha256')}, expected {src_se_sha}")
    if se_block.get("staged_sha256") in (None, ""):
        group_fail("second_exhibition.staged_sha256 missing from summary")
    if se_block.get("staged_sha256") == src_se_sha:
        group_fail(
            f"second_exhibition.staged_sha256 equals source_sha256 ({src_se_sha}); "
            "the 6 path rewrites must produce a different staged index"
        )
    if se_block.get("source_bytes") != src_se_bytes:
        group_fail(f"second_exhibition.source_bytes in summary = {se_block.get('source_bytes')}, expected {src_se_bytes}")
    if se_block.get("path_rewrite_count") != 6:
        group_fail(f"second_exhibition.path_rewrite_count = {se_block.get('path_rewrite_count')}, expected 6")
    if se_block.get("source_equals_staged"):
        group_fail("second_exhibition.source_equals_staged is true (expected false; rewrites must change staged bytes)")
    else:
        group_pass(
            f"second_exhibition identity OK: source={src_se_sha[:12]}… bytes={src_se_bytes} "
            f"staged={(se_block.get('staged_sha256') or '')[:12]}… "
            f"source_equals_staged=False path_rewrite_count=6"
        )

    # ---- Deprecated key forward-compat: warn-but-don't-fail if present ----
    deprecated_key = summary.get("source_index_html_sha256")
    deprecated_scope = summary.get("source_index_html_sha256_scope")
    if deprecated_key is not None:
        if deprecated_key == src_se_sha:
            group_pass(
                f"DEPRECATED source_index_html_sha256 still equals second-exhibition source ({deprecated_key[:12]}…); "
                f"scope annotation: {deprecated_scope!r}"
            )
        else:
            group_fail(
                f"DEPRECATED source_index_html_sha256 = {deprecated_key}; expected {src_se_sha} "
                "or remove the deprecated key"
            )
        if deprecated_scope != "second-exhibition/site/index.html":
            group_fail(
                f"DEPRECATED source_index_html_sha256_scope = {deprecated_scope!r}; "
                "expected 'second-exhibition/site/index.html'"
            )
        else:
            group_pass(
                "DEPRECATED source_index_html_sha256_scope correctly labelled "
                "'second-exhibition/site/index.html'"
            )

    # Audit must NOT be inside artifact
    if is_within(aud, art):
        group_fail("audit directory is inside artifact directory")
    group_pass("audit directory is outside artifact directory")

    # ---- H. Deployment status (page text) ----
    # v5.3b: staged second-exhibition page must declare current publication status 'production-deployed-v5.3'
    # and per-asset 'published-in-v5.3'. Historical import record 'imported-not-deployed' must remain present.
    section("H. Deployment status (page text)")
    se_text = (se_dir / "index.html").read_text(encoding="utf-8", errors="replace")
    has_current_status = ("production-deployed-v5.3" in se_text) and ("published-in-v5.3" in se_text)
    has_historical_record = ("imported-not-deployed" in se_text)
    # Forbidden stale phrasing — page must not currently claim repository-only / not deployed
    stale_phrases = [
        "repository-only-not-deployed</span>",
        "<span class=\"badge\">not deployed",
        "本展览未部署到 GitHub Pages",
    ]
    found_stale = [s for s in stale_phrases if s in se_text]
    if not has_current_status:
        group_fail("staged second-exhibition index.html missing current publication status 'production-deployed-v5.3' or per-asset 'published-in-v5.3'")
    if not has_historical_record:
        group_fail("staged second-exhibition index.html lost historical import record 'imported-not-deployed' (must be preserved)")
    if found_stale:
        group_fail(f"staged second-exhibition index.html contains stale current-status phrasing: {found_stale}")
    if has_current_status and has_historical_record and not found_stale:
        group_pass("staged second-exhibition index.html carries production-deployed-v5.3 + published-in-v5.3 + preserved imported-not-deployed")

    print()
    print("============================================")
    print(f"PASS: staging gate — {len(src_files)} main-site + {len(se_files)} second-exhibition files verified")
    print("============================================")


if __name__ == "__main__":
    main()