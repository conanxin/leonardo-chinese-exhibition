#!/usr/bin/env python3
"""
template_quality_gate.py — leonardo-chinese-exhibition v3.3

Reusable quality gate for the Chinese digital exhibition template and pilot.

Usage:
    python3 scripts/template_quality_gate.py

Exit codes:
    0  — PASS (all checks satisfied)
    1  — FAIL (one or more checks failed)

Checks covered:
    A. Required paths        — directories + key manual files + roadmap
    B. JSON validation       — template 5 files + pilot 4 files
    C. Forbidden terms       — default template content must NOT mention
                               project-specific source names
    D. Pilot structure       — marker / artifacts / glossary / deep blocks
    E. Release workflow rule — reality recovery rule + forbidden phrases
    F. No accidental deploy  — live site files must NOT contain pilot
                               markers or pilot titles
    G. Summary               — print final STATUS

This script is intentionally dependency-free (Python standard library only)
and idempotent. It can be run from repo root.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# Resolve repo root from script location: <repo>/scripts/template_quality_gate.py
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REQUIRED_DIRS = [
    REPO_ROOT / "_template",
    REPO_ROOT / "_template" / "site",
    REPO_ROOT / "_template" / "data",
    REPO_ROOT / "_pilots" / "second-exhibition-pilot",
]

REQUIRED_FILES = [
    REPO_ROOT / "docs" / "V3_TEMPLATE_ROADMAP.md",
    REPO_ROOT / "_template" / "USAGE_GUIDE_ZH.md",
    REPO_ROOT / "_template" / "CONTENT_AUTHORING_GUIDE_ZH.md",
    REPO_ROOT / "_template" / "SOURCE_RIGHTS_CHECKLIST_ZH.md",
    REPO_ROOT / "_template" / "PILOT_WORKFLOW_ZH.md",
    REPO_ROOT / "_template" / "RELEASE_WORKFLOW_ZH.md",
]

TEMPLATE_JSON_FILES = [
    REPO_ROOT / "_template" / "content.schema.json",
    REPO_ROOT / "_template" / "data" / "exhibition.example.json",
    REPO_ROOT / "_template" / "data" / "sections.example.json",
    REPO_ROOT / "_template" / "data" / "glossary.example.json",
    REPO_ROOT / "_template" / "data" / "assets.example.json",
]

PILOT_JSON_FILES = [
    REPO_ROOT / "_pilots" / "second-exhibition-pilot" / "data" / "exhibition.json",
    REPO_ROOT / "_pilots" / "second-exhibition-pilot" / "data" / "sections.json",
    REPO_ROOT / "_pilots" / "second-exhibition-pilot" / "data" / "glossary.json",
    REPO_ROOT / "_pilots" / "second-exhibition-pilot" / "data" / "assets.json",
]

# Default-content files scanned for forbidden terms.
# README and MANIFEST may mention the source case ("文档说明文件可以提到 source case") and are excluded.
FORBIDDEN_TERM_SCAN_FILES = [
    REPO_ROOT / "_template" / "data" / "exhibition.example.json",
    REPO_ROOT / "_template" / "data" / "sections.example.json",
    REPO_ROOT / "_template" / "data" / "glossary.example.json",
    REPO_ROOT / "_template" / "data" / "assets.example.json",
    REPO_ROOT / "_template" / "site" / "index.template.html",
    REPO_ROOT / "_template" / "site" / "script.template.js",
    REPO_ROOT / "_template" / "site" / "style.template.css",
]

FORBIDDEN_TERMS = [
    "Leonardo",
    "Codex Atlanticus",
    "Royal Collection Trust",
    "Leonardo//thek@",
]

PILOT_HTML = REPO_ROOT / "_pilots" / "second-exhibition-pilot" / "site" / "index.html"

PILOT_STRUCTURE_THRESHOLDS = {
    "pilot_marker": 1,        # pilot-v0.1 marker occurrences
    "artifact_card": 4,       # template-artifact-card occurrences
    "glossary_term": 6,       # <dt> terms in glossary
    "deep_reading": 1,        # deep-reading class occurrences
    "material_evidence": 1,   # material-evidence class occurrences
    "visual_thinking": 1,     # visual-thinking class occurrences
    "research_model": 1,      # research-model class occurrences
}

RELEASE_WORKFLOW = REPO_ROOT / "_template" / "RELEASE_WORKFLOW_ZH.md"
RELEASE_WORKFLOW_REQUIRED_PHRASES = [
    "commit SHA + verified live byte + verified tag",
    "git add .",
    "不移动旧 tag",
    "不覆盖旧 release",
]

LIVE_SITE_FILES = [
    REPO_ROOT / "site" / "index.html",
    REPO_ROOT / "site" / "script.js",
    REPO_ROOT / "site" / "style.css",
]

LIVE_SITE_FORBIDDEN = [
    "一件作品的旅程",
    "pilot-v0.1",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class GateReport:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failures: list[str] = []

    def check(self, label: str, ok: bool, detail: str = "") -> bool:
        marker = "PASS" if ok else "FAIL"
        line = f"  [{marker}] {label}"
        if detail:
            line += f" — {detail}"
        print(line)
        if ok:
            self.passed += 1
        else:
            self.failed += 1
            self.failures.append(label)
        return ok

    def group(self, title: str) -> None:
        print()
        print(f"=== {title} ===")


def _is_js_comment_line(line: str) -> bool:
    """True if the line is purely a JS/JS-doc comment line."""
    stripped = line.strip()
    if not stripped:
        return False
    # Line comment
    if stripped.startswith("//"):
        return True
    # Block comment continuation lines (JSDoc / * ... */)
    if stripped.startswith("*"):
        return True
    # Block comment start — strip the leading /* and check the remainder is comment-like
    if stripped.startswith("/*"):
        # Either a single-line block or the first line of a multi-line block
        # If the line ends with */ it's still a comment line; treat as comment
        return True
    return False


def _is_css_comment_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("/*"):
        return True
    if stripped.startswith("*"):
        return True
    return False


def _scan_forbidden(file_path: Path, term: str) -> int:
    """Count occurrences of `term` in `file_path`, ignoring comment lines
    for JS / CSS / HTML files."""
    if not file_path.exists():
        return 0
    suffix = file_path.suffix.lower()
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return 0
    count = 0
    for raw_line in content.splitlines():
        line = raw_line
        if suffix == ".js" and _is_js_comment_line(line):
            continue
        if suffix == ".css" and _is_css_comment_line(line):
            continue
        if suffix in (".html", ".htm"):
            # Strip HTML comments <!-- ... --> on a single line, but ignore
            # lines that ARE only comments.
            stripped = line.strip()
            if stripped.startswith("<!--") and stripped.endswith("-->"):
                continue
            # Mid-line comments (rare in this template) — leave for naive match
        count += line.count(term)
    return count


def _grep(path: Path, pattern: str) -> int:
    if not path.exists():
        return 0
    content = path.read_text(encoding="utf-8", errors="replace")
    return content.count(pattern)


# ---------------------------------------------------------------------------
# Check sections
# ---------------------------------------------------------------------------

def check_required_paths(report: GateReport) -> bool:
    report.group("A. Required paths")
    all_ok = True
    for d in REQUIRED_DIRS:
        ok = d.is_dir()
        report.check(f"dir: {d.relative_to(REPO_ROOT)}", ok)
        all_ok = all_ok and ok
    for f in REQUIRED_FILES:
        ok = f.is_file()
        report.check(f"file: {f.relative_to(REPO_ROOT)}", ok)
        all_ok = all_ok and ok
    return all_ok


def check_json_validation(report: GateReport) -> bool:
    report.group("B. JSON validation")
    all_ok = True
    for jf in TEMPLATE_JSON_FILES:
        ok = False
        try:
            json.loads(jf.read_text(encoding="utf-8"))
            ok = True
        except Exception as e:
            report.failures.append(f"{jf.name}: {e}")
        report.check(f"template: {jf.relative_to(REPO_ROOT)}", ok)
        all_ok = all_ok and ok
    for jf in PILOT_JSON_FILES:
        ok = False
        try:
            json.loads(jf.read_text(encoding="utf-8"))
            ok = True
        except Exception as e:
            report.failures.append(f"{jf.name}: {e}")
        report.check(f"pilot: {jf.relative_to(REPO_ROOT)}", ok)
        all_ok = all_ok and ok
    return all_ok


def check_forbidden_terms(report: GateReport) -> bool:
    report.group("C. Forbidden terms in default template content")
    all_ok = True
    for term in FORBIDDEN_TERMS:
        total = 0
        hits = []
        for fp in FORBIDDEN_TERM_SCAN_FILES:
            n = _scan_forbidden(fp, term)
            if n > 0:
                hits.append((fp.relative_to(REPO_ROOT), n))
                total += n
        ok = total == 0
        if hits:
            detail = "; ".join(f"{p}={n}" for p, n in hits)
        else:
            detail = "0 hits"
        report.check(f"forbidden '{term}'", ok, detail)
        all_ok = all_ok and ok
    return all_ok


def check_pilot_structure(report: GateReport) -> bool:
    report.group("D. Pilot structural checks")
    if not PILOT_HTML.exists():
        report.check(f"file: {PILOT_HTML.relative_to(REPO_ROOT)}", False)
        return False
    counts = {
        "pilot_marker": _grep(PILOT_HTML, "pilot-v0.1"),
        "artifact_card": _grep(PILOT_HTML, "template-artifact-card"),
        "glossary_term": len(re.findall(r"<dt[\s>]", PILOT_HTML.read_text(encoding="utf-8"))),
        "deep_reading": _grep(PILOT_HTML, "deep-reading"),
        "material_evidence": _grep(PILOT_HTML, "material-evidence"),
        "visual_thinking": _grep(PILOT_HTML, "visual-thinking"),
        "research_model": _grep(PILOT_HTML, "research-model"),
    }
    all_ok = True
    for key, threshold in PILOT_STRUCTURE_THRESHOLDS.items():
        actual = counts[key]
        ok = actual >= threshold
        report.check(f"{key} >= {threshold}", ok, f"actual={actual}")
        all_ok = all_ok and ok
    return all_ok


def check_release_workflow(report: GateReport) -> bool:
    report.group("E. Release workflow rule")
    if not RELEASE_WORKFLOW.exists():
        report.check(f"file: {RELEASE_WORKFLOW.relative_to(REPO_ROOT)}", False)
        return False
    content = RELEASE_WORKFLOW.read_text(encoding="utf-8")
    all_ok = True
    for phrase in RELEASE_WORKFLOW_REQUIRED_PHRASES:
        ok = phrase in content
        report.check(f"contains '{phrase}'", ok)
        all_ok = all_ok and ok
    return all_ok


def check_no_accidental_deploy(report: GateReport) -> bool:
    report.group("F. No accidental deployment signal (local site/)")
    all_ok = True
    for fp in LIVE_SITE_FILES:
        if not fp.exists():
            report.check(f"file: {fp.relative_to(REPO_ROOT)}", False)
            all_ok = False
            continue
        content = fp.read_text(encoding="utf-8", errors="replace")
        hits = []
        for term in LIVE_SITE_FORBIDDEN:
            n = content.count(term)
            if n > 0:
                hits.append(f"{term}={n}")
        ok = len(hits) == 0
        detail = "; ".join(hits) if hits else "clean"
        report.check(f"{fp.relative_to(REPO_ROOT)}", ok, detail)
        all_ok = all_ok and ok
    return all_ok


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    if not REPO_ROOT.is_dir():
        print(f"FATAL: repo root not found at {REPO_ROOT}", file=sys.stderr)
        return 1

    print(f"Repo root: {REPO_ROOT}")
    print(f"Gate: template_quality_gate.py")

    report = GateReport()

    results = {
        "A. Required paths": check_required_paths(report),
        "B. JSON validation": check_json_validation(report),
        "C. Forbidden terms": check_forbidden_terms(report),
        "D. Pilot structure": check_pilot_structure(report),
        "E. Release workflow rule": check_release_workflow(report),
        "F. No accidental deployment signal": check_no_accidental_deploy(report),
    }

    # Summary
    report.group("G. Summary")
    print(f"  Total checks: {report.passed + report.failed}")
    print(f"  Passed:       {report.passed}")
    print(f"  Failed:       {report.failed}")
    print()
    print("  Section results:")
    for section, ok in results.items():
        marker = "PASS" if ok else "FAIL"
        print(f"    [{marker}] {section}")
    print()
    if report.failures:
        print("  Failures:")
        for f in report.failures:
            print(f"    - {f}")

    final_status = "PASS" if report.failed == 0 else "FAIL"
    print()
    print(f"FINAL STATUS: {final_status}")
    return 0 if final_status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())