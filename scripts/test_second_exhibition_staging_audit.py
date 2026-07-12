#!/usr/bin/env python3
"""test_second_exhibition_staging_audit.py

Regression test for the staging audit schema (v5.5b). Verifies that
`second_exhibition_staging_build.py` and `second_exhibition_staging_gate.py`
share a clear, unambiguous v2 schema in `build-summary.json` and that
root and second-exhibition identities cannot be confused.

Runs entirely outside the repo under ``/tmp``. Stdlib only. PASS=0,
FAIL=1.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Tuple, List

# Expected canonical values (independent of any report file)
CANONICAL_ROOT_BYTES = 92976
CANONICAL_ROOT_SHA = "e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc"


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


class TestResult:
    def __init__(self) -> None:
        self.passes: List[str] = []
        self.fails: List[str] = []

    def check(self, label: str, cond: bool, detail: str = "") -> None:
        if cond:
            self.passes.append(label)
        else:
            self.fails.append(f"{label} ({detail})")


def run(cmd: List[str], cwd: Path | None = None) -> Tuple[int, str]:
    """Run a subprocess and return (rc, stdout_stderr_combined)."""
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=300)
    return res.returncode, (res.stdout or "") + (res.stderr or "")


def build_audit(repo_root: Path, audit_dir: Path, art_dir: Path) -> None:
    rc, out = run(
        ["python3", "scripts/second_exhibition_staging_build.py",
         "--output", str(art_dir),
         "--audit", str(audit_dir)],
        cwd=repo_root,
    )
    if rc != 0:
        raise RuntimeError(f"staging build failed (rc={rc}):\n{out}")


def run_gate(repo_root: Path, art_dir: Path, audit_dir: Path) -> Tuple[int, str]:
    rc, out = run(
        ["python3", "scripts/second_exhibition_staging_gate.py",
         "--artifact", str(art_dir),
         "--audit", str(audit_dir)],
        cwd=repo_root,
    )
    return rc, out


def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--repo-root", default=str(Path.cwd()),
        help="path to the repository root (default: current directory)",
    )
    p.add_argument(
        "--keep", action="store_true",
        help="keep the /tmp test directory for inspection after the run",
    )
    args = p.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    if not (repo_root / "scripts" / "second_exhibition_staging_build.py").is_file():
        print(f"WARN: repo-root does not look like the project ({repo_root}); exit 2", file=sys.stderr)
        return 2

    test_dir = Path(tempfile.mkdtemp(prefix="v55b-audit-test-"))
    audit_dir = test_dir / "audit"
    art_dir = test_dir / "artifact"
    audit_dir.mkdir(parents=True, exist_ok=True)
    art_dir.mkdir(parents=True, exist_ok=True)

    res = TestResult()

    # ---- 1. Build ----
    try:
        build_audit(repo_root, audit_dir, art_dir)
        res.check("staging build exit 0", True)
    except Exception as e:
        res.check("staging build exit 0", False, str(e))
        print("FAIL: " + "; ".join(res.fails))
        return 1

    # ---- 2. Read audit ----
    summary_path = audit_dir / "build-summary.json"
    res.check("build-summary.json exists", summary_path.is_file(),
              f"missing {summary_path}")
    if not summary_path.is_file():
        print("FAIL: " + "; ".join(res.fails))
        return 1
    try:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        res.check("build-summary.json is valid JSON", True)
    except Exception as e:
        res.check("build-summary.json is valid JSON", False, str(e))
        print("FAIL: " + "; ".join(res.fails))
        return 1

    # ---- 3. Schema v2 structural checks ----
    res.check("audit_schema_version == 2.0",
              summary.get("audit_schema_version") == "2.0",
              f"got {summary.get('audit_schema_version')!r}")
    res.check("summary has root_site block", isinstance(summary.get("root_site"), dict))
    res.check("summary has second_exhibition block", isinstance(summary.get("second_exhibition"), dict))

    root = summary.get("root_site") or {}
    se = summary.get("second_exhibition") or {}

    res.check("root_site.source_path == site/index.html",
              root.get("source_path") == "site/index.html",
              f"got {root.get('source_path')!r}")
    res.check("second_exhibition.source_path == second-exhibition/site/index.html",
              se.get("source_path") == "second-exhibition/site/index.html",
              f"got {se.get('source_path')!r}")
    res.check("second_exhibition.staged_path == second-exhibition/index.html",
              se.get("staged_path") == "second-exhibition/index.html",
              f"got {se.get('staged_path')!r}")

    # ---- 4. SHA values match the actual files (direct sha256sum) ----
    src_root_path = repo_root / "site" / "index.html"
    src_root_sha = sha256_file(src_root_path)
    res.check("root_site.source_sha256 matches sha256sum site/index.html",
              root.get("source_sha256") == src_root_sha,
              f"audit={root.get('source_sha256')} direct={src_root_sha}")

    staged_root_path = art_dir / "index.html"
    staged_root_sha = sha256_file(staged_root_path)
    res.check("root_site.staged_sha256 matches sha256sum staged root index.html",
              root.get("staged_sha256") == staged_root_sha,
              f"audit={root.get('staged_sha256')} direct={staged_root_sha}")

    # Source-side second-exhibition SHA from local second-exhibition/site/
    src_se_path = repo_root / "second-exhibition" / "site" / "index.html"
    src_se_sha = sha256_file(src_se_path)
    res.check("second_exhibition.source_sha256 matches sha256sum second-exhibition/site/index.html",
              se.get("source_sha256") == src_se_sha,
              f"audit={se.get('source_sha256')} direct={src_se_sha}")

    # Staged-side second-exhibition SHA from the freshly-built artifact
    staged_se_path = art_dir / "second-exhibition" / "index.html"
    staged_se_sha = sha256_file(staged_se_path)
    res.check("second_exhibition.staged_sha256 matches sha256sum staged second-exhibition/index.html",
              se.get("staged_sha256") == staged_se_sha,
              f"audit={se.get('staged_sha256')} direct={staged_se_sha}")

    # ---- 5. Equality flags ----
    res.check("root_site.source_equals_staged == True",
              root.get("source_equals_staged") is True,
              f"got {root.get('source_equals_staged')!r}")
    res.check("second_exhibition.source_equals_staged == False",
              se.get("source_equals_staged") is False,
              f"got {se.get('source_equals_staged')!r}")
    res.check("second_exhibition.path_rewrite_count == 6",
              se.get("path_rewrite_count") == 6,
              f"got {se.get('path_rewrite_count')!r}")
    res.check("second_exhibition.source_sha256 != staged_sha256",
              se.get("source_sha256") != se.get("staged_sha256"),
              f"unexpected equality: src={se.get('source_sha256')} staged={se.get('staged_sha256')}")

    # ---- 6. Root/second-exhibition SHA confusion guard ----
    res.check("root_site.source_sha256 != second_exhibition.source_sha256",
              root.get("source_sha256") != se.get("source_sha256"),
              f"audit conflated: root_src={root.get('source_sha256')} second_src={se.get('source_sha256')}")
    res.check("root_site.source_sha256 != second_exhibition.staged_sha256",
              root.get("source_sha256") != se.get("staged_sha256"),
              f"audit conflated: root_src={root.get('source_sha256')} second_staged={se.get('staged_sha256')}")

    # ---- 7. Deprecated-key labelling (forward-compat check) ----
    deprecated_key = summary.get("source_index_html_sha256")
    deprecated_scope = summary.get("source_index_html_sha256_scope")
    res.check("source_index_html_sha256_scope == second-exhibition/site/index.html",
              deprecated_scope == "second-exhibition/site/index.html",
              f"got {deprecated_scope!r}")
    res.check(
        "deprecated source_index_html_sha256 equals second-exhibition.source_sha256",
        deprecated_key == src_se_sha,
        f"deprecated={deprecated_key} src_se_sha={src_se_sha}",
    )
    # The deprecated key MUST NOT equal the root SHA under any normal build.
    res.check(
        "deprecated source_index_html_sha256 != canonical root SHA",
        deprecated_key != CANONICAL_ROOT_SHA,
        f"deprecated={deprecated_key} canonical_root={CANONICAL_ROOT_SHA}",
    )

    # ---- 8. Staged index bytes & path-rewrite residue checks ----
    res.check("staged root index.html size == 92976",
              staged_root_path.stat().st_size == CANONICAL_ROOT_BYTES,
              f"got {staged_root_path.stat().st_size}")
    src_se_text = src_se_path.read_text(encoding="utf-8")
    staged_se_text = staged_se_path.read_text(encoding="utf-8")

    # Use precise regex matching for ./ vs ../ (substring overlap of './'
    # in '../' would falsely count 6 ./ matches in the source).
    import re
    src_dotdot_count = len(re.findall(r"(?<!\.)\.\/assets\/images\/", src_se_text))
    src_dotdot_count += src_se_text.count("../assets/images/")
    # The 6 image src= attributes in source are exactly '../assets/images/...'.
    res.check("source second-exhibition/site/index.html has 6 ../assets/images/ refs",
              src_se_text.count("../assets/images/") == 6,
              f"got {src_se_text.count('../assets/images/')}")

    staged_dotdot_count = staged_se_text.count("../assets/images/")
    staged_dotdot_slash_count = len(re.findall(r"(?<!\.)\.\/assets\/images\/", staged_se_text))
    res.check("staged second-exhibition/index.html has 0 ../assets/images/ refs",
              staged_dotdot_count == 0,
              f"got {staged_dotdot_count}")
    res.check("staged second-exhibition/index.html has 6 ./assets/images/ refs (post-rewrite)",
              staged_dotdot_slash_count == 6,
              f"got {staged_dotdot_slash_count}")
    res.check("staged second-exhibition/index.html size = 25635",
              staged_se_path.stat().st_size == 25635,
              f"got {staged_se_path.stat().st_size}")

    # ---- 9. Gate ----
    rc, gate_out = run_gate(repo_root, art_dir, audit_dir)
    res.check("staging gate exit 0", rc == 0, f"exit {rc}\n{gate_out[-2000:]}")

    # ---- 10. Report ----
    print(f"Test directory: {test_dir}")
    print(f"Audit summary: {summary_path}")
    print(f"Schema version: {summary.get('audit_schema_version')}")
    print(f"Root source SHA: {root.get('source_sha256')}")
    print(f"Second-exhibition source SHA: {se.get('source_sha256')}")
    print(f"Second-exhibition staged SHA: {se.get('staged_sha256')}")
    print()
    print(f"Checks: pass={len(res.passes)} fail={len(res.fails)} total={len(res.passes) + len(res.fails)}")
    if res.fails:
        print("FAIL:")
        for f in res.fails:
            print(f"  - {f}")

    if not args.keep:
        shutil.rmtree(test_dir, ignore_errors=True)
    else:
        print(f"Test directory kept at: {test_dir}")

    return 0 if not res.fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
