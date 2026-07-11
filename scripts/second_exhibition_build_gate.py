#!/usr/bin/env python3
"""Second-exhibition build gate (v4.6).

Run from the repository root:

    python3 scripts/second_exhibition_build_gate.py

Exit codes:
    0   PASS — every required check holds.
    1   FAIL — at least one required check failed.
    2   INFRASTRUCTURE — a required file is missing.

The gate performs no network calls. It only reads files under
``second-exhibition/`` and a small set of protected paths.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SECOND_EX = REPO_ROOT / "second-exhibition"
SITE_DIR = SECOND_EX / "site"
DATA_DIR = SECOND_EX / "data"
DOCS_DIR = SECOND_EX / "docs"
ASSETS_DIR = SECOND_EX / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
MANIFEST = ASSETS_DIR / "asset-import-manifest.json"
CHECKSUMS = ASSETS_DIR / "asset-checksums.sha256"
SOURCE_AUDIT = DOCS_DIR / "SOURCE_AUDIT_MANIFEST.md"
RIGHTS_DOC = DOCS_DIR / "RIGHTS_AND_SOURCES.md"
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"

REQUIRED_CANDIDATE_IDS = ["C-01", "C-03", "C-06", "C-08", "C-09", "C-10"]

REQUIRED_SITE_FILES = [
    SITE_DIR / "index.html",
    SITE_DIR / "style.css",
    SITE_DIR / "script.js",
    SITE_DIR / "README.md",
]

REQUIRED_DATA_FILES = [
    DATA_DIR / "exhibition.json",
    DATA_DIR / "sections.json",
    DATA_DIR / "glossary.json",
    DATA_DIR / "assets.json",
]

REQUIRED_CONTENT_DOCS = [
    DOCS_DIR / "VISITOR_GUIDE_ZH.md",
    DOCS_DIR / "CURATORIAL_ESSAY_ZH.md",
    DOCS_DIR / "DEEP_RESEARCH_NOTES_ZH.md",
    DOCS_DIR / "BUILD_ASSET_USAGE.md",
]

REQUIRED_ASSET_DOCS = [MANIFEST, CHECKSUMS, SOURCE_AUDIT, RIGHTS_DOC]

REQUIRED_DEEP_BLOCK_CLASSES = [
    "deep-reading-block",
    "material-evidence-block",
    "visual-thinking-block",
    "research-model-block",
]

PROTECTED_SITE_PATHS = [
    REPO_ROOT / "site" / "index.html",
    REPO_ROOT / "site" / "script.js",
    REPO_ROOT / "site" / "style.css",
]


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


def _count_html_occurrences(html: str, *needles: str) -> int:
    return sum(html.count(n) for n in needles)


def main() -> int:
    failures: list[str] = []
    info: list[str] = []

    # --- A. Required structure ---
    for required in REQUIRED_SITE_FILES + REQUIRED_DATA_FILES + REQUIRED_CONTENT_DOCS + REQUIRED_ASSET_DOCS:
        if not required.is_file():
            failures.append(f"A.required-structure: missing {required.relative_to(REPO_ROOT)}")

    if not failures:
        info.append("A.required-structure: all 15 required files present")
    else:
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        print("INFRASTRUCTURE — required files missing", file=sys.stderr)
        return 2

    # --- B. JSON validation ---
    data: dict[str, dict] = {}
    for path in REQUIRED_DATA_FILES:
        try:
            data[path.name] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"B.json: {path.name} is not valid JSON: {exc}")

    if "exhibition.json" in data:
        ex = data["exhibition.json"]
        if ex.get("status") != "repository-only-not-deployed":
            failures.append(
                f"B.json: exhibition.status must be 'repository-only-not-deployed', got {ex.get('status')!r}"
            )
        if ex.get("deployment_status") != "repository-only-not-deployed":
            failures.append(
                f"B.json: exhibition.deployment_status must be 'repository-only-not-deployed', got {ex.get('deployment_status')!r}"
            )
        if ex.get("section_count") != 4:
            failures.append(
                f"B.json: exhibition.section_count must be 4, got {ex.get('section_count')!r}"
            )
        if ex.get("artifact_count") != 6:
            failures.append(
                f"B.json: exhibition.artifact_count must be 6, got {ex.get('artifact_count')!r}"
            )
        if not isinstance(ex.get("glossary_count_target"), int) or ex["glossary_count_target"] < 10:
            failures.append(
                f"B.json: exhibition.glossary_count_target must be >= 10, got {ex.get('glossary_count_target')!r}"
            )

    if "sections.json" in data:
        sec = data["sections.json"]
        sections = sec.get("sections")
        if not isinstance(sections, list) or len(sections) != 4:
            failures.append(f"B.json: sections.sections[] must contain exactly 4 entries, got {len(sections) if isinstance(sections, list) else 'n/a'}")

    if "glossary.json" in data:
        gl = data["glossary.json"]
        items = gl.get("items")
        if not isinstance(items, list) or len(items) < 10:
            failures.append(f"B.json: glossary.items[] must contain >= 10 entries, got {len(items) if isinstance(items, list) else 'n/a'}")

    if "assets.json" in data:
        as_ = data["assets.json"]
        assets = as_.get("assets")
        if not isinstance(assets, list) or len(assets) != 6:
            failures.append(f"B.json: assets.assets[] must contain exactly 6 entries, got {len(assets) if isinstance(assets, list) else 'n/a'}")
        ids_in_assets = [a.get("candidate_id") for a in assets] if isinstance(assets, list) else []
        for cid in REQUIRED_CANDIDATE_IDS:
            if cid not in ids_in_assets:
                failures.append(f"B.json: assets.json missing candidate_id {cid}")

    # --- C. Asset integrity ---
    if MANIFEST.is_file():
        try:
            manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"C.assets: manifest JSON parse error: {exc}")
            manifest = {}
        m_assets = manifest.get("assets", []) if isinstance(manifest, dict) else []
        if not isinstance(m_assets, list) or len(m_assets) != 6:
            failures.append(f"C.assets: manifest.assets[] must contain exactly 6 entries, got {len(m_assets) if isinstance(m_assets, list) else 'n/a'}")

    # All 6 image files exist.
    if IMAGES_DIR.is_dir():
        on_disk = {p.name for p in IMAGES_DIR.iterdir() if p.is_file()}
    else:
        on_disk = set()
    expected_filenames = {
        "bhl-318921-page-603998-c01.webp",
        "bhl-318921-page-603962-c03.webp",
        "smithsonian-nmnh-1529703.png",
        "met-285149.jpg",
        "rijksmuseum-rp-f-f80152.jpg",
        "rijksmuseum-rp-f-f80313.jpg",
    }
    missing = expected_filenames - on_disk
    for m in sorted(missing):
        failures.append(f"C.assets: expected file missing: {m}")

    # Page-referenced images all exist.
    index_html = (SITE_DIR / "index.html").read_text(encoding="utf-8") if (SITE_DIR / "index.html").is_file() else ""
    img_srcs = re.findall(r'<img\s+[^>]*src="([^"]+)"', index_html)
    referenced_local_imgs = [s for s in img_srcs if s.startswith("../assets/images/")]
    referenced_names = {Path(s).name for s in referenced_local_imgs}
    for name in referenced_names:
        if name not in expected_filenames:
            failures.append(f"C.assets: page references unknown image: {name}")
    for name in expected_filenames:
        if name not in referenced_names:
            failures.append(f"C.assets: page does not reference expected image: {name}")

    # No external image URLs in <img src>.
    external_imgs = [s for s in img_srcs if s.startswith(("http://", "https://", "//"))]
    if external_imgs:
        failures.append(f"C.assets: page contains {len(external_imgs)} external <img src> URL(s); only local ../assets/images/ allowed")

    # Checksums match.
    if CHECKSUMS.is_file():
        checksums = _read_checksums(CHECKSUMS)
        for fname in expected_filenames:
            rel_path = f"second-exhibition/assets/images/{fname}"
            sha_expected = checksums.get(rel_path)
            path = IMAGES_DIR / fname
            if not path.is_file():
                continue
            sha_actual = _sha256(path)
            if sha_expected is None:
                failures.append(f"C.assets: checksum file missing entry for {rel_path}")
            elif sha_expected != sha_actual:
                failures.append(f"C.assets: {rel_path}: checksum mismatch (file={sha_expected}, actual={sha_actual})")

    # --- D. Page structure (in index.html) ---
    if not index_html:
        failures.append("D.page-structure: index.html missing or empty")
    else:
        # marker
        marker_count = _count_html_occurrences(index_html, "second-exhibition-v0.1")
        if marker_count < 1:
            failures.append("D.page-structure: marker 'second-exhibition-v0.1' not found in index.html")

        # artifact-card count
        artifact_card_count = index_html.count('class="artifact-card"')
        if artifact_card_count != 6:
            failures.append(f"D.page-structure: expected 6 .artifact-card, got {artifact_card_count}")

        # glossary-item count
        glossary_item_count = index_html.count('class="glossary-item"')
        if glossary_item_count < 10:
            failures.append(f"D.page-structure: expected >= 10 .glossary-item, got {glossary_item_count}")

        # source-note count
        source_note_count = index_html.count('class="source-note"')
        if source_note_count < 6:
            failures.append(f"D.page-structure: expected >= 6 .source-note, got {source_note_count}")

        # credit-line count
        credit_line_count = index_html.count('class="credit-line"')
        if credit_line_count < 6:
            failures.append(f"D.page-structure: expected >= 6 .credit-line, got {credit_line_count}")

        # 4 deep block classes each >= 1
        for cls in REQUIRED_DEEP_BLOCK_CLASSES:
            # Match either exact class="X" or class="X ..." prefix.
            pat = re.compile(rf'class="{cls}(?:\s|")')
            if not pat.search(index_html):
                failures.append(f"D.page-structure: deep block class .{cls} not found in index.html")

        # repository-status >= 1
        repo_status_count = index_html.count('class="repository-status"')
        if repo_status_count < 1:
            failures.append("D.page-structure: .repository-status not found in index.html")

        # 4 sections each present
        for sid in ("section-1-observation", "section-2-classification", "section-3-reproduction", "section-4-reorganization"):
            if f'id="{sid}"' not in index_html:
                failures.append(f"D.page-structure: section id #{sid} missing")

        # forbidden status words must not appear as status in page
        # (allow them only in "forbidden/not used" prose context)
        # We do a conservative check: look for the literal phrase "Status: approved" / "Status: deployed" / "Status: live"
        for tok in ("Status: approved", "Status: deployed", "Status: live", "status: approved", "status: deployed", "status: live"):
            if tok in index_html:
                failures.append(f"D.page-structure: forbidden status phrase {tok!r} appears in page")

    # --- E. Candidate rules ---
    if index_html:
        candidate_ids_in_page = re.findall(r'data-candidate-id="([^"]+)"', index_html)
        if sorted(candidate_ids_in_page) != sorted(REQUIRED_CANDIDATE_IDS):
            failures.append(
                f"E.candidates: page data-candidate-id set {sorted(candidate_ids_in_page)} != required {sorted(REQUIRED_CANDIDATE_IDS)}"
            )
        # Each candidate id must appear at most once per attribute context — uniqueness check
        if len(candidate_ids_in_page) != len(set(candidate_ids_in_page)):
            from collections import Counter
            counts = Counter(candidate_ids_in_page)
            dups = [c for c, n in counts.items() if n > 1]
            failures.append(f"E.candidates: duplicate data-candidate-id in page: {dups}")

        # C-06 lightbox disabled
        c06_match = re.search(r'<article[^>]*data-candidate-id="C-06"[^>]*>', index_html)
        if c06_match is None:
            failures.append("E.candidates: C-06 artifact card not found")
        else:
            c06_tag = c06_match.group(0)
            if 'data-lightbox-enabled="false"' not in c06_tag:
                failures.append("E.candidates: C-06 must have data-lightbox-enabled='false'")
            if 'data-low-resolution="true"' not in c06_tag:
                failures.append("E.candidates: C-06 must have data-low-resolution='true'")

        # C-06 low-resolution warning present in page text
        c06_card_block = index_html[c06_match.start():c06_match.start() + 4000]
        if "90×90" not in c06_card_block and "90x90" not in c06_card_block:
            failures.append("E.candidates: C-06 low-resolution warning ('90×90' or '90x90') not found in C-06 card block")

        # C-03 PD subset caution present (anywhere in page)
        if "PD subset" not in index_html:
            failures.append("E.candidates: 'PD subset' caution for C-03 not found in page")

        # C-08 double-confirmation note present
        if "double-confirmation" not in index_html.lower():
            failures.append("E.candidates: 'double-confirmation' note for C-08 not found in page")

        # C-10 manifest 404 caveat present
        if "manifest" not in index_html.lower() or "404" not in index_html:
            failures.append("E.candidates: C-10 IIIF Presentation API manifest 404 caveat not found in page")

    # Check content docs for the candidate-rule prose too
    for fname in ("BUILD_ASSET_USAGE.md",):
        path = DOCS_DIR / fname
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for required in (
                ("PD subset", "C-03 PD subset caution"),
                ("low-resolution", "C-06 low-resolution caveat"),
                ("double-confirmation", "C-08 double-confirmation note"),
                ("manifest", "C-10 manifest caveat"),
            ):
                if required[0].lower() not in text.lower():
                    failures.append(f"E.candidates: docs/{fname} missing '{required[0]}' ({required[1]})")

    # --- F. Deployment safety ---
    # No protected top-level site path contains "second-exhibition" marker.
    for site_path in PROTECTED_SITE_PATHS:
        if not site_path.is_file():
            continue
        try:
            content = site_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "second-exhibition" in content.lower():
            failures.append(
                f"F.deployment-safety: {site_path.relative_to(REPO_ROOT)} mentions 'second-exhibition' — top-level live must not reference the second exhibition"
            )

    # Workflows must not include second-exhibition as a deployment path.
    if WORKFLOWS_DIR.is_dir():
        for wf in sorted(WORKFLOWS_DIR.glob("*.y*ml")):
            try:
                text = wf.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "second-exhibition" in text:
                failures.append(
                    f"F.deployment-safety: workflow {wf.relative_to(REPO_ROOT)} mentions 'second-exhibition' — Pages workflow must not target it"
                )

    # Page does not use forbidden status words as status
    if index_html:
        for tok in ("deployed", "live"):
            # Look for "Status: live" / "Status: deployed" patterns only — these tokens appear legitimately in many contexts.
            for pat in (f"Status: {tok}", f"status: {tok}", f"Status:{tok}"):
                if pat in index_html:
                    failures.append(f"F.deployment-safety: forbidden status phrase {pat!r} in index.html")

    # --- Final output ---
    if failures:
        print("FAIL — second exhibition build gate", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    info.append(f"B.json: 4 data JSON files valid")
    info.append(f"C.assets: 6 expected image filenames present, all referenced in page")
    info.append(f"C.assets: checksum file matches all 6 local files")
    info.append(f"D.page-structure: marker 'second-exhibition-v0.1' present")
    info.append(f"D.page-structure: 6 artifact cards, {glossary_item_count} glossary items, {source_note_count} source notes, {credit_line_count} credit lines")
    info.append(f"D.page-structure: 4 deep block classes present")
    info.append(f"D.page-structure: .repository-status present")
    info.append(f"D.page-structure: 4 sections present")
    info.append(f"E.candidates: 6 data-candidate-id present and unique")
    info.append(f"E.candidates: C-06 lightbox disabled, low-resolution warning present")
    info.append(f"E.candidates: C-03 PD subset caution, C-08 double-confirmation, C-10 manifest 404 caveat present")
    info.append(f"F.deployment-safety: top-level site paths and Pages workflows do not reference second-exhibition")
    print("PASS — second exhibition build gate")
    for line in info:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())