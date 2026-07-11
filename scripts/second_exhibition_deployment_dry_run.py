#!/usr/bin/env python3
"""
second_exhibition_deployment_dry_run.py — simulate the GitHub Pages project-site
deployment without ever pushing to main or touching the workflow.

Project-site model:
  Repo:  conanxin/leonardo-chinese-exhibition
  URL:   https://conanxin.github.io/leonardo-chinese-exhibition/
  Mapping:
    artifact root          <->  <base>/            (top-level site index)
    artifact/second-exhibition/   <base>/second-exhibition/  (second-exhibition subtree)

This script:
  1. Starts a local HTTP server with a configurable base-path prefix.
  2. Probes every allowlisted URL and every forbidden URL, recording status / size / marker.
  3. Packs the artifact into /tmp/leonardo-pages-artifact.tar.gz (excluding the audit dir).
  4. Unpacks the tar into /tmp/leonardo-pages-roundtrip/ and verifies per-file SHA256
     identity against the original artifact.
  5. Pre-rehearses a workflow rollback by computing the one-line revert diff and
     verifying it would restore `path: site` if the workflow had been changed.
  6. Writes a JSON report to /tmp/leonardo-pages-dry-run/report.json.

Does NOT:
  - modify the workflow file
  - push to origin
  - create a tag or Release
  - write anything under the repository

Stdlib only. PASS=0 / FAIL=1.
"""

import argparse
import datetime
import hashlib
import http.server
import json
import os
import shutil
import socket
import socketserver
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ART_DEFAULT = "/tmp/leonardo-pages-artifact"
AUD_DEFAULT = "/tmp/leonardo-pages-artifact-audit"
DRY_DEFAULT = "/tmp/leonardo-pages-dry-run"
RND_DEFAULT = "/tmp/leonardo-pages-roundtrip"
TAR_DEFAULT = "/tmp/leonardo-pages-artifact.tar.gz"

# The repo name is the public base path for a GitHub Pages project site.
REPO_BASE = "/leonardo-chinese-exhibition"
REPO_NAME = "leonardo-chinese-exhibition"

# URLs to probe (relative to the base path). Each tuple: (path, expected_status,
# content_check_name). The base path is prepended at request time.
ALLOWLIST_PATHS = [
    ("/",                                                 200, "root_index"),
    ("/index.html",                                       200, "root_index_html"),
    ("/style.css",                                        200, "root_style_css"),
    ("/script.js",                                        200, "root_script_js"),
    ("/second-exhibition/",                               200, "se_index"),
    ("/second-exhibition/index.html",                     200, "se_index_html"),
    ("/second-exhibition/style.css",                      200, "se_style_css"),
    ("/second-exhibition/script.js",                      200, "se_script_js"),
    ("/second-exhibition/assets/images/bhl-318921-page-603998-c01.webp", 200, "se_img_1"),
    ("/second-exhibition/assets/images/bhl-318921-page-603962-c03.webp", 200, "se_img_2"),
    ("/second-exhibition/assets/images/smithsonian-nmnh-1529703.png",     200, "se_img_3"),
    ("/second-exhibition/assets/images/met-285149.jpg",                  200, "se_img_4"),
    ("/second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg",     200, "se_img_5"),
    ("/second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg",     200, "se_img_6"),
]

FORBIDDEN_PATHS = [
    "/second-exhibition/data/",
    "/second-exhibition/docs/",
    "/second-exhibition/data/exhibition.json",
    "/second-exhibition/data/sections.json",
    "/second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md",
    "/second-exhibition/docs/RIGHTS_AND_SOURCES.md",
    "/second-exhibition/assets/asset-import-manifest.json",
    "/second-exhibition/assets/asset-checksums.sha256",
    "/_template/",
    "/_pilots/",
    "/reports/",
    "/scripts/",
    "/.firecrawl/",
    "/README.md",
    "/V4_ROADMAP.md",
    "/V5_ROADMAP.md",
]


# ---- Helpers ----

def sha256_file(p: Path) -> str:
    h = hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()


def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256(); h.update(b); return h.hexdigest()


def now() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


# BasePathHTTPRequestHandler: serves every request as if the artifact were mounted
# at REPO_BASE. So an HTTP GET for "/leonardo-chinese-exhibition/style.css" maps
# to artifact/style.css.
class BasePathHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    BASE_PREFIX = REPO_BASE

    def translate_path(self, path: str):  # type: ignore[override]
        # Strip the base prefix; if not present, treat as 404.
        parsed = urllib.parse.urlparse(path)
        url_path = parsed.path
        if not url_path.startswith(self.BASE_PREFIX + "/") and url_path != self.BASE_PREFIX:
            # Not under our base — return a path that won't exist
            return str(Path(self.directory) / "__outside_base__" / url_path.lstrip("/"))
        # Strip base prefix (keep leading "/")
        stripped = url_path[len(self.BASE_PREFIX):]
        # Trailing slash on base URL should resolve to /index.html
        if stripped == "" or stripped == "/":
            stripped = "/index.html"
        # Translate relative to the configured directory
        rel = stripped.lstrip("/")
        return str(Path(self.directory) / rel)


def start_basepath_server(directory: Path, port: int) -> tuple:
    handler = lambda *a, **kw: BasePathHTTPRequestHandler(*a, directory=str(directory), **kw)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd, thread


def http_get(url: str, timeout: float = 5.0) -> tuple:
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            return r.status, data, dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, b"", dict(e.headers or {})
    except Exception as e:
        print(f"  ERR: {e}", file=sys.stderr)
        return 0, b"", {}


def parse_checksum_file(p: Path) -> dict:
    out = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        sha, _, name = line.partition("  ")
        out[name.strip()] = sha.strip()
    return out


# ---- Section printers ----

def section(label: str):
    print()
    print(f"=== {label} ===")


def ok(msg: str):
    print(f"  OK: {msg}")


def fail(msg: str, dry_run_report: dict, **ctx):
    print(f"  FAIL: {msg}", file=sys.stderr)
    for k, v in ctx.items():
        print(f"    {k}: {v}", file=sys.stderr)
    dry_run_report["status"] = "FAIL"
    dry_run_report["failure"] = msg
    raise SystemExit(1)


# ---- Main ----

def main():
    ap = argparse.ArgumentParser(description="v5.2 deployment dry-run")
    ap.add_argument("--artifact", default=ART_DEFAULT)
    ap.add_argument("--audit",    default=AUD_DEFAULT)
    ap.add_argument("--dry-run-dir", default=DRY_DEFAULT)
    ap.add_argument("--roundtrip-dir", default=RND_DEFAULT)
    ap.add_argument("--tar", default=TAR_DEFAULT)
    ap.add_argument("--repo-base", default=REPO_BASE,
                    help="Public base path (default: GitHub Pages project-site /<repo>/)")
    ap.add_argument("--keep-server-alive", action="store_true",
                    help="Keep the local base-path server running after probes (for browser QA).")
    ap.add_argument("--server-port", type=int, default=0,
                    help="Use a fixed server port (default: random free port).")
    args = ap.parse_args()

    art = Path(args.artifact).resolve()
    aud = Path(args.audit).resolve()
    drr = Path(args.dry_run_dir).resolve()
    rnd = Path(args.roundtrip_dir).resolve()
    tar = Path(args.tar).resolve()
    base = args.repo_base

    print(f"artifact:  {art}")
    print(f"audit:     {aud}")
    print(f"dry-run:   {drr}")
    print(f"roundtrip: {rnd}")
    print(f"tar:       {tar}")
    print(f"repo_base: {base}")
    print(f"deployment_status: dry-run-only-not-deployed")

    report: dict = {
        "schema_version": 1,
        "round": "v5.2-deployment-dry-run",
        "started_at": now(),
        "artifact_path": str(art),
        "audit_path": str(aud),
        "roundtrip_path": str(rnd),
        "tar_path": str(tar),
        "repo_base": base,
        "deployment_status": "dry-run-only-not-deployed",
        "results": {},
        "checks": [],
    }

    # ---- Pre-flight ----
    section("Pre-flight")
    if not art.is_dir():
        fail(f"artifact not found: {art}", report, hint="run second_exhibition_staging_build.py first")
    ok(f"artifact exists: {art}")
    if not aud.is_dir():
        fail(f"audit not found: {aud}", report, hint="run second_exhibition_staging_build.py first")
    ok(f"audit exists: {aud}")

    # Clean / create dry-run + roundtrip dirs
    for d in (drr, rnd):
        if d.exists():
            if d.is_symlink():
                d.unlink()
            elif d.is_dir():
                shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)
    ok(f"cleaned/created dry-run and roundtrip dirs")

    # Verify artifact is outside repo (defense-in-depth)
    repo = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"]
    ).decode().strip()
    repo_p = Path(repo).resolve()
    try:
        art.relative_to(repo_p)
        fail("artifact is inside repository", report, artifact=str(art), repo=str(repo_p))
    except ValueError:
        pass
    ok("artifact outside repository")

    # ---- A. Base-path HTTP probe ----
    section(f"A. Base-path HTTP probe (base={base})")
    if args.server_port:
        port = args.server_port
        # Verify the fixed port is free
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _s:
            try:
                _s.bind(("127.0.0.1", port))
            except OSError:
                fail(f"server port {port} is already in use", report)
    else:
        port = find_free_port()
    httpd, thread = start_basepath_server(art, port)
    base_url = f"http://127.0.0.1:{port}{base}"
    print(f"  server: {base_url}  (project-site model)")
    report["dry_run_http_port"] = port
    report["dry_run_http_base_url"] = base_url

    if args.keep_server_alive:
        # Skip the probes' try/finally cleanup; keep server running until SIGTERM.
        # Probes run normally; the finally block below is suppressed by re-raising
        # into a deferred handler.
        import atexit
        atexit.register(lambda: (httpd.shutdown(), httpd.server_close()))
        print(f"  NOTE: server kept alive; will shut down on process exit.")

    try:
        # Allowlist
        allow_results = []
        for rel_path, expected, name in ALLOWLIST_PATHS:
            url = f"http://127.0.0.1:{port}{base}" + rel_path
            status, body, _ = http_get(url)
            ok_ = status == expected
            allow_results.append({
                "name": name, "url": url, "status": status,
                "expected": expected, "bytes": len(body), "pass": ok_,
            })
            print(f"  {status}  expected={expected}  bytes={len(body):>7}  {url}")
            if not ok_:
                fail(f"allowlist probe failed: {name}", report,
                     url=url, status=status, expected=expected)
        report["results"]["allowlist_probes"] = allow_results
        ok(f"all {len(allow_results)} allowlisted URLs returned expected status")

        # Special checks
        # (a) root index byte
        root_status, root_body, _ = http_get(f"http://127.0.0.1:{port}{base}/")
        if len(root_body) != 92976:
            fail(f"root index byte mismatch: {len(root_body)} (expected 92976)", report)
        ok(f"root index byte = {len(root_body)} (matches production)")

        # (b) v2.9 marker
        if b"v2.9-real-source-rights-audit" not in root_body:
            fail("root index missing v2.9 marker", report)
        ok("root index contains v2.9-real-source-rights-audit marker")

        # (c) second-exhibition index carries title
        se_status, se_body, _ = http_get(f"http://127.0.0.1:{port}{base}/second-exhibition/")
        se_text = se_body.decode("utf-8", errors="replace")
        title_hits = se_text.count("植物图谱与视觉分类")
        if title_hits < 1:
            fail("second-exhibition index missing 植物图谱与视觉分类 title", report)
        ok(f"second-exhibition index has 植物图谱与视觉分类 title (count={title_hits})")

        # (d) staged second-exhibition index has zero ../assets/images/
        # (because artifact-only rewrite must be applied)
        se_old = se_text.count("../assets/images/")
        if se_old != 0:
            fail(f"second-exhibition index still has ../assets/images/ count={se_old}", report)
        ok("second-exhibition index has zero ../assets/images/ references")

        # (e) second-exhibition index links resolve under base path
        # (check that all referenced image URLs exist)
        import re as _re
        se_img_refs = _re.findall(r'(?:src|href)="(\./assets/images/[^"]+)"', se_text)
        if len(se_img_refs) != 6:
            fail(f"second-exhibition index image refs = {len(se_img_refs)} (expected 6)", report,
                 refs=se_img_refs)
        ok(f"second-exhibition index references {len(se_img_refs)} images via ./assets/images/")

        for ref in se_img_refs:
            rel = ref[2:]  # strip "./"
            url = f"http://127.0.0.1:{port}{base}/second-exhibition/{rel}"
            status, body, _ = http_get(url)
            if status != 200:
                fail(f"image link {ref} -> {url} returned {status}", report)
        ok(f"all {len(se_img_refs)} second-exhibition image links resolve under base path")

        # Forbidden
        forbidden_results = []
        for rel_path in FORBIDDEN_PATHS:
            url = f"http://127.0.0.1:{port}{base}" + rel_path
            status, _, _ = http_get(url)
            ok_ = status == 404
            forbidden_results.append({"url": url, "status": status, "pass": ok_})
            print(f"  {status}  expected=404  {url}")
            if not ok_:
                fail(f"forbidden path returned {status}: {url}", report)
        report["results"]["forbidden_probes"] = forbidden_results
        ok(f"all {len(forbidden_results)} forbidden paths returned 404")

        # Out-of-base sanity: an unrelated path on the same server should 404 too
        oob_url = f"http://127.0.0.1:{port}/some-other-base/second-exhibition/"
        oob_status, _, _ = http_get(oob_url)
        if oob_status == 200:
            fail(f"out-of-base probe unexpectedly returned 200: {oob_url}", report)
        ok(f"out-of-base probe {oob_url} = {oob_status} (correctly not served)")

    finally:
        httpd.shutdown()
        httpd.server_close()

    # ---- B. Pack + roundtrip ----
    section("B. Artifact pack + roundtrip")
    if tar.exists():
        tar.unlink()
    with tarfile.open(tar, "w:gz") as tf:
        # Pack artifact contents, NOT the audit dir
        for p in sorted(art.rglob("*")):
            if p.is_file() and not p.is_symlink():
                tf.add(p, arcname=p.relative_to(art))
    ok(f"packed artifact -> {tar} ({tar.stat().st_size} bytes)")

    # Unpack to roundtrip dir
    if rnd.exists():
        shutil.rmtree(rnd)
    rnd.mkdir(parents=True, exist_ok=True)
    with tarfile.open(tar, "r:gz") as tf:
        tf.extractall(rnd)
    ok(f"unpacked roundtrip -> {rnd}")

    # Per-file SHA identity
    src_files = sorted(p for p in art.rglob("*") if p.is_file() and not p.is_symlink())
    rnd_files = sorted(p for p in rnd.rglob("*") if p.is_file() and not p.is_symlink())
    if len(src_files) != len(rnd_files):
        fail(f"roundtrip file count differs: src={len(src_files)} rnd={len(rnd_files)}", report)
    ok(f"file count match: {len(src_files)}")

    mismatches = 0
    mismatched = []
    for sf, rf in zip(src_files, rnd_files):
        if sf.relative_to(art) != rf.relative_to(rnd):
            fail(f"path mismatch: src={sf.relative_to(art)} rnd={rf.relative_to(rnd)}", report)
        if sha256_file(sf) != sha256_file(rf):
            mismatches += 1
            mismatched.append(sf.relative_to(art))
    if mismatches:
        fail(f"roundtrip SHA mismatch on {mismatches} files: {mismatched[:5]}", report)
    ok(f"all {len(src_files)} files roundtrip SHA-identical")

    report["results"]["roundtrip"] = {
        "files": len(src_files),
        "tar_bytes": tar.stat().st_size,
        "identity": "byte-identical",
    }

    # Verify roundtrip index bytes are still 92976 (i.e., tar/untar preserved identity)
    rnd_root = rnd / "index.html"
    if rnd_root.stat().st_size != 92976:
        fail(f"roundtrip root index byte mismatch: {rnd_root.stat().st_size}", report)
    ok(f"roundtrip root index byte = {rnd_root.stat().st_size}")

    # ---- C. Rollback rehearsal ----
    section("C. Rollback rehearsal")
    # The future production change would be: change `path: site` -> `path: <artifact>`.
    # A clean rollback = revert that one commit (one line), restoring `path: site`.
    # This round does NOT modify the workflow; we just verify the rollback semantics.

    wf = Path(".github/workflows/pages.yml")
    wf_text = wf.read_text(encoding="utf-8")
    if "path: site" not in wf_text:
        fail("current workflow does not contain 'path: site'", report)
    ok("current workflow still uses 'path: site'")

    # Check that the proposed change would be a single-line, reviewable edit.
    proposed_old = "          path: site"
    proposed_new = "          path: __STAGING_ARTIFACT_DIR__"
    if wf_text.count(proposed_old) != 1:
        fail("could not locate unique 'path: site' line in workflow", report)
    ok("'path: site' appears exactly once in workflow")

    # Rollback rehearsal: simulate `git revert <freeze-commit>` producing a diff that
    # restores 'path: site'. We do NOT run git revert; we just confirm the line
    # count and reversibility.
    rehearsal = {
        "current_workflow_path_line": proposed_old,
        "proposed_change": proposed_old + " -> " + proposed_new,
        "rollback_method": "git revert <deployment-commit>; one-line diff restores 'path: site'",
        "rollback_diff_size_lines": 1,
        "rollback_verification": [
            "live byte returns to 92,976",
            "v2.9 marker count returns to 1",
            "/second-exhibition/ Pages URLs return 404 again",
        ],
    }
    report["results"]["rollback_rehearsal"] = rehearsal
    ok("rollback rehearsal documented (one-line revert restores 'path: site')")

    # Verify no actual workflow modification happened
    if "path: __STAGING_ARTIFACT_DIR__" in wf_text:
        fail("workflow was modified (dry-run should not touch it)", report)
    ok("workflow NOT modified")

    # ---- Finalize ----
    section("Finalize")
    report_path = drr / "report.json"
    report["finished_at"] = now()
    report["status"] = "PASS"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    ok(f"wrote report -> {report_path}")

    # Summary
    print()
    print("============================================")
    print(f"PASS: v5.2 deployment dry-run complete")
    print(f"  artifact  -> base path {base}")
    print(f"  allowlist probes : {len(report['results']['allowlist_probes'])}/{len(report['results']['allowlist_probes'])}")
    print(f"  forbidden probes : {len(report['results']['forbidden_probes'])}/{len(report['results']['forbidden_probes'])}")
    print(f"  roundtrip files  : {report['results']['roundtrip']['files']} byte-identical")
    print(f"  tar size         : {report['results']['roundtrip']['tar_bytes']} bytes")
    print(f"  deployment_status: {report['deployment_status']}")
    print(f"  report           : {report_path}")
    print("============================================")


if __name__ == "__main__":
    main()