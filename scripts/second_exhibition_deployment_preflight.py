#!/usr/bin/env python3
"""v5.0 second exhibition deployment preflight.

Pure-stdlib, no network access, no file modification. Run from the repository
root. Exit code 0 = PASS, 1 = FAIL.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ALLOWED_V5_DOCS = [
    "docs/SECOND_EXHIBITION_DEPLOYMENT_OPTIONS_v5.0.md",
    "docs/SECOND_EXHIBITION_DEPLOYMENT_ARCHITECTURE_v5.0.md",
    "docs/SECOND_EXHIBITION_DEPLOYMENT_RISK_REGISTER_v5.0.md",
    "docs/SECOND_EXHIBITION_ROLLBACK_PLAN_v5.0.md",
    "docs/SECOND_EXHIBITION_DEPLOYMENT_CHECKLIST_v5.0.md",
    "docs/SECOND_EXHIBITION_URL_AND_PATH_PLAN_v5.0.md",
    "docs/V5_ROADMAP.md",
]

V4_8_RELEASE_FILES = [
    "docs/RELEASE_NOTES_v4.8_REAL_SECOND_EXHIBITION_REPOSITORY_HARDENING.md",
    "release-assets/v4.8-real-second-exhibition-repository-hardening-manifest.md",
    "reports/leonardo_chinese_exhibition_v4_8_real_stable_freeze_report.md",
]

SECOND_EXHIBITION_SITE_FILES = [
    "second-exhibition/site/index.html",
    "second-exhibition/site/style.css",
    "second-exhibition/site/script.js",
]

SECOND_EXHIBITION_DATA_FILES = [
    "second-exhibition/data/exhibition.json",
    "second-exhibition/data/sections.json",
    "second-exhibition/data/glossary.json",
    "second-exhibition/data/assets.json",
]

CHECKSUM_FILE = Path("second-exhibition/assets/asset-checksums.sha256")
ASSETS_DIR = Path("second-exhibition/assets/images")
WORKFLOW_FILE = Path(".github/workflows/pages.yml")

FORBIDDEN_DEPLOY_EXTS = {".md", ".json", ".sha256"}
FORBIDDEN_DEPLOY_PATH_PATTERNS = [
    re.compile(r"^_template/"),
    re.compile(r"^_pilots/"),
    re.compile(r"^posts/"),
    re.compile(r"^case-study/"),
    re.compile(r"^release-assets/"),
    re.compile(r"^docs/"),
    re.compile(r"^reports/"),
    re.compile(r"^scripts/"),
    re.compile(r"^\.git/"),
    re.compile(r"^\.firecrawl/"),
    re.compile(r"^second-exhibition/data/"),
    re.compile(r"^second-exhibition/docs/"),
    re.compile(r"^second-exhibition/assets/asset-import-manifest\.json$"),
    re.compile(r"^second-exhibition/assets/asset-checksums\.sha256$"),
]

ALLOWED_DEPLOY_PATTERNS = [
    re.compile(r"^site/(index\.html|style\.css|script\.js)$"),
    re.compile(r"^second-exhibition/(index\.html|style\.css|script\.js)$"),
    re.compile(r"^second-exhibition/assets/images/[A-Za-z0-9._-]+$"),
]

ALLOWED_DEPLOY_EXTS = {".html", ".css", ".js", ".webp", ".png", ".jpg", ".jpeg"}


def banner(title: str) -> None:
    print(f"\n=== {title} ===")


def ok(msg: str) -> None:
    print(f"  [PASS] {msg}")


def fail(msg: str) -> None:
    print(f"  [FAIL] {msg}")


def info(msg: str) -> None:
    print(f"  [info] {msg}")


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def section_a() -> bool:
    banner("A. Verified baseline")
    ok_flag = True
    for rel in V4_8_RELEASE_FILES:
        if (ROOT / rel).is_file():
            ok(rel)
        else:
            fail(f"missing: {rel}")
            ok_flag = False

    for rel in SECOND_EXHIBITION_SITE_FILES:
        if (ROOT / rel).is_file():
            ok(rel)
        else:
            fail(f"missing: {rel}")
            ok_flag = False

    for rel in SECOND_EXHIBITION_DATA_FILES:
        if (ROOT / rel).is_file():
            ok(rel)
        else:
            fail(f"missing: {rel}")
            ok_flag = False

    for script in [
        "scripts/template_quality_gate.py",
        "scripts/second_exhibition_build_gate.py",
        "scripts/second_exhibition_repository_qa.py",
        "scripts/second_exhibition_browser_qa.mjs",
    ]:
        if (ROOT / script).is_file():
            ok(script)
        else:
            fail(f"missing: {script}")
            ok_flag = False

    return ok_flag


def section_b() -> bool:
    banner("B. Source build")
    ok_flag = True

    # Parse asset checksums and verify presence.
    if not CHECKSUM_FILE.is_file():
        fail(f"missing: {CHECKSUM_FILE}")
        return False
    checksum_entries: list[tuple[str, str]] = []
    for line in CHECKSUM_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        digest, _, name = line.partition("  ")
        if not digest or not name:
            fail(f"malformed checksum line: {line!r}")
            ok_flag = False
            continue
        checksum_entries.append((digest, name))
    info(f"checksum entries: {len(checksum_entries)}")

    for digest, name in checksum_entries:
        target = Path(name)
        if target.is_absolute() or ".." in target.parts:
            fail(f"unsafe path in checksum file: {name!r}")
            ok_flag = False
            continue
        full_path = ROOT / target
        if not full_path.is_file():
            fail(f"missing asset: {full_path}")
            ok_flag = False
            continue
        actual = hash_file(full_path)
        if actual != digest:
            fail(f"checksum mismatch: {full_path} expected {digest}, got {actual}")
            ok_flag = False
        else:
            ok(f"checksum OK: {target.name}")

    return ok_flag


def section_c() -> bool:
    banner("C. Deployment planning")
    ok_flag = True
    for rel in ALLOWED_V5_DOCS:
        if (ROOT / rel).is_file():
            ok(rel)
        else:
            fail(f"missing: {rel}")
            ok_flag = False

    risk_register = ROOT / "docs/SECOND_EXHIBITION_DEPLOYMENT_RISK_REGISTER_v5.0.md"
    if risk_register.is_file():
        text = risk_register.read_text(encoding="utf-8").lower()
        if "release blocker" in text and "high" in text and "blocked" in text:
            ok("risk register mentions release blocker / High / Blocked")
        else:
            fail("risk register missing release blocker rule")
            ok_flag = False

    rollback = ROOT / "docs/SECOND_EXHIBITION_ROLLBACK_PLAN_v5.0.md"
    if rollback.is_file():
        ok("rollback plan present")

    checklist = ROOT / "docs/SECOND_EXHIBITION_DEPLOYMENT_CHECKLIST_v5.0.md"
    if checklist.is_file():
        ok("checklist present")

    return ok_flag


def section_d() -> bool:
    banner("D. Source path analysis")
    ok_flag = True
    page = ROOT / "second-exhibition/site/index.html"
    if not page.is_file():
        fail("missing second-exhibition/site/index.html")
        return False

    text = page.read_text(encoding="utf-8")

    # Count ../assets/images/ references
    count_dotdot = len(re.findall(r"\.\./assets/images/", text))
    info(f"'../assets/images/' references in page: {count_dotdot}")
    if count_dotdot == 0:
        fail("no '../assets/images/' references found; rewrite plan needs them")
        ok_flag = False
    elif count_dotdot > 8:
        fail(f"unexpectedly many '../assets/images/' references: {count_dotdot}")
        ok_flag = False
    else:
        ok(f"path rewrite plan covers {count_dotdot} references")

    # Forbidden patterns
    forbidden_in_page = {
        "external image http(s)": re.findall(r'<img[^>]+src="https?://', text),
        "file:// image": re.findall(r'<img[^>]+src="file://', text),
        "windows image path": re.findall(r'<img[^>]+src="[A-Za-z]:\\', text),
        "absolute /assets/ ref": re.findall(r'src="/assets/', text),
    }
    for label, hits in forbidden_in_page.items():
        if hits:
            fail(f"{label}: {len(hits)} occurrences")
            ok_flag = False
        else:
            ok(f"no {label}")

    # No external image URLs (per v5.0 plan)
    if re.search(r'https?://[^"\s]+\.(?:jpg|jpeg|png|webp|gif|tif|tiff)', text, re.IGNORECASE):
        fail("external image URL found in second-exhibition page")
        ok_flag = False
    else:
        ok("no external image URLs in second-exhibition page")

    return ok_flag


def section_e() -> bool:
    banner("E. Publish allowlist (staging tree)")
    ok_flag = True

    info("allowed file extensions in staging tree: " + ",".join(sorted(ALLOWED_DEPLOY_EXTS)))
    info("allowed patterns:")
    for pat in ALLOWED_DEPLOY_PATTERNS:
        info(f"  - {pat.pattern}")
    info("forbidden path patterns:")
    for pat in FORBIDDEN_DEPLOY_PATH_PATTERNS:
        info(f"  - {pat.pattern}")

    # Verify the staging tree would be a strict allowlist if it existed.
    # We do not actually stage anything here; we only verify the rules.
    ok("publish allowlist defined")
    return ok_flag


def section_f() -> bool:
    banner("F. Workflow safety")
    ok_flag = True
    if not WORKFLOW_FILE.is_file():
        fail("workflow file missing")
        return False
    workflow_text = WORKFLOW_FILE.read_text(encoding="utf-8")

    if "actions/upload-pages-artifact@v3" in workflow_text:
        ok("upload-pages-artifact step present")
    else:
        fail("upload-pages-artifact step missing")
        ok_flag = False

    if re.search(r"path:\s+site", workflow_text):
        ok("workflow currently uploads only 'site' (path: site)")
    else:
        fail("workflow does not pin to 'site' as artifact source")
        ok_flag = False

    if re.search(r"path:\s*\.", workflow_text):
        fail("workflow appears to upload repository root")
        ok_flag = False
    else:
        ok("workflow does not upload repository root")

    forbidden_in_workflow = ["second-exhibition", "_template", "_pilots"]
    for tok in forbidden_in_workflow:
        if tok in workflow_text:
            fail(f"workflow references {tok!r}")
            ok_flag = False
        else:
            ok(f"workflow does not reference {tok!r}")

    return ok_flag


def main() -> int:
    results = {
        "A.baseline": section_a(),
        "B.source_build": section_b(),
        "C.planning": section_c(),
        "D.path_analysis": section_d(),
        "E.allowlist": section_e(),
        "F.workflow": section_f(),
    }

    banner("Summary")
    for k, v in results.items():
        status = "PASS" if v else "FAIL"
        print(f"  [{status}] {k}")

    overall = all(results.values())
    print("\nFINAL STATUS: " + ("PASS" if overall else "FAIL"))
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())