#!/usr/bin/env python3
"""second_exhibition_production_healthcheck.py

Manual, repeatable production health check for the second exhibition.

Goals
-----
- Use Python standard library only (no pip dependencies).
- Verify the deployed production surface against the *current* (v5.0
  freeze-time) baseline without modifying the repository.
- Be tolerant of environment failure: never report a network timeout as a
  hard 404. Exit codes:
    0 -> PASS
    1 -> check failure
    2 -> environment / network failure (cannot reach the host)

Output
------
- Human-friendly grouped report by default.
- Optional --json-output writes the same report in machine-readable form.

Non-goals
---------
- This is not a monitoring daemon: it is a manual operator tool that pairs
  with `scripts/second_exhibition_repository_qa.py` etc. Run before pushing
  to main and after each Pages deploy.
- It does not call GitHub write APIs and does not move tags or releases.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import OrderedDict
from typing import Any, Dict, List, Optional, Tuple

# ----- Constants (v5.0 freeze baseline) -----------------------------------

ROOT_URL_DEFAULT = (
    "https://conanxin.github.io/leonardo-chinese-exhibition/"
)
SECOND_URL_DEFAULT = (
    "https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/"
)

ROOT_EXPECTED_BYTES = 92976
# Captured at v5.0 freeze: live root SHA (live == site/index.html).
ROOT_EXPECTED_SHA256 = (
    "e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc"
)
ROOT_EXACT_MARKER = "v2.9-real-source-rights-audit"
ROOT_EXACT_MARKER_COUNT = 1
ROOT_LOOSE_MARKER = "v2.9"
ROOT_LOOSE_MARKER_COUNT = 4  # informational only

SECOND_EXPECTED_BYTES = 25635
# Captured at v5.0 freeze: live second-exhibition index SHA
# (live == staging-artifact/second-exhibition/index.html;
# NOT byte-identical to local second-exhibition/site/index.html — the
# staging builder rewrites ./assets/images/ → ../assets/images/).
SECOND_EXPECTED_SHA256 = (
    "7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c"
)
SECOND_TITLE_FRAGMENT = "植物图谱与视觉分类"

# v5.6b second-exhibition v0.2 candidate baseline (worker-only).
# Captured at v5.6b build time against /tmp/v56b-artifact staging
# (NOT live production). Activate ONLY for local candidate v0.2
# dry-run/health-check via `--candidate-v0.2`.
SECOND_V02_CANDIDATE_BYTES = 31452  # staged candidate at v5.6b build
SECOND_V02_CANDIDATE_SHA256 = (
    "00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2"
)
SECOND_V02_SOURCE_BYTES = 31458  # source candidate
SECOND_V02_SOURCE_SHA256 = (
    "662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e"
)

# Production status phrase expectations (live HTML).
PHRASE_PRODUCTION_DEPLOYED = "production-deployed-v5.3"
PHRASE_PUBLISHED = "published-in-v5.3"
PHRASE_IMPORTED = "imported-not-deployed"
PHRASE_REPO_ONLY = "repository-only-not-deployed"

EXPECTED_PHRASE_COUNTS = {
    PHRASE_PRODUCTION_DEPLOYED: 5,
    PHRASE_PUBLISHED: 8,
    PHRASE_IMPORTED: 8,
    PHRASE_REPO_ONLY: 0,
}

IMAGE_PATHS = [
    "second-exhibition/assets/images/bhl-318921-page-603998-c01.webp",
    "second-exhibition/assets/images/bhl-318921-page-603962-c03.webp",
    "second-exhibition/assets/images/smithsonian-nmnh-1529703.png",
    "second-exhibition/assets/images/met-285149.jpg",
    "second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg",
    "second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg",
]

IMAGE_MIME_EXPECT = {
    ".webp": {"image/webp"},
    ".jpg": {"image/jpeg"},
    ".jpeg": {"image/jpeg"},
    ".png": {"image/png"},
}

FORBIDDEN_PATHS_404 = [
    "README.md",
    "V4_ROADMAP.md",
    "V5_ROADMAP.md",
    "scripts/",
    "_template/",
    "_pilots/",
    "reports/",
    "release-assets/",
    ".github/",
    ".firecrawl/",
    "second-exhibition/data/",
    "second-exhibition/docs/",
    "second-exhibition/assets/asset-import-manifest.json",
    "second-exhibition/assets/asset-checksums.sha256",
    "second-exhibition/README.md",
    "second-exhibition/site/README.md",
    "no-such-public-path-please-404/",
]

ROOT_PUBLIC = ["", "index.html", "style.css", "script.js"]
SECOND_PUBLIC = ["", "index.html", "style.css", "script.js"]

USER_AGENT = (
    "leonardo-second-exhibition-healthcheck/5.5 "
    "(+https://conanxin.github.io/leonardo-chinese-exhibition/)"
)

# ----- HTTP layer ---------------------------------------------------------


class HttpFetchError(RuntimeError):
    """Network-level failure reaching the host (DNS, timeout, redirect loop)."""


def fetch(
    url: str,
    timeout: float = 15.0,
    retries: int = 2,
    method: str = "GET",
) -> Tuple[int, Dict[str, str], bytes, float]:
    """Return (status, headers, body, latency_seconds).

    Raises HttpFetchError on DNS/connection/timeout failures
    (distinct from a hard HTTP error response, which we propagate as status).
    """
    last_error: Optional[BaseException] = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, method=method)
        req.add_header("User-Agent", USER_AGENT)
        req.add_header("Accept", "*/*")
        t0 = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                status = resp.status
                headers = {k.lower(): v for k, v in resp.headers.items()}
                body = resp.read()
                latency = time.monotonic() - t0
                return status, headers, body, latency
        except urllib.error.HTTPError as e:
            # Real HTTP error response (e.g. 404). Capture body for mime tests
            # even when status != 200.
            latency = time.monotonic() - t0
            headers = {k.lower(): v for k, v in (e.headers.items() if e.headers else [])}
            body = b""
            try:
                body = e.read() or b""
            except Exception:
                pass
            return e.code, headers, body, latency
        except (
            urllib.error.URLError,
            TimeoutError,
            ConnectionError,
            OSError,
        ) as e:
            last_error = e
            if attempt >= retries:
                raise HttpFetchError(f"{type(e).__name__}: {e}") from e
            time.sleep(0.5 * (attempt + 1))
            continue
    # Should not be reached, but keep a final guard.
    raise HttpFetchError(f"unreachable: {last_error}")


def head_get_status(url: str, timeout: float, retries: int) -> Tuple[Optional[int], Optional[HttpFetchError]]:
    try:
        status, _h, _b, _lat = fetch(url, timeout=timeout, retries=retries, method="GET")
        return status, None
    except HttpFetchError as e:
        return None, e


# ----- Assertion / report helpers ------------------------------------------


class Reporter:
    def __init__(self) -> None:
        self.groups: "OrderedDict[str, List[Dict[str, Any]]]" = OrderedDict()
        self.env_errors = 0

    def add(
        self,
        group: str,
        name: str,
        status: str,
        detail: str = "",
        meta: Optional[Dict[str, Any]] = None,
    ) -> None:
        d = self.groups.setdefault(group, [])
        d.append(
            {
                "name": name,
                "status": status,  # PASS | FAIL | WARN | INFO | ENV-ERR
                "detail": detail,
                "meta": meta or {},
            }
        )
        if status == "ENV-ERR":
            self.env_errors += 1

    def counts(self) -> Dict[str, int]:
        c = {"PASS": 0, "FAIL": 0, "WARN": 0, "INFO": 0, "ENV-ERR": 0, "TOTAL": 0}
        for items in self.groups.values():
            for it in items:
                c[it["status"]] = c.get(it["status"], 0) + 1
                c["TOTAL"] += 1
        return c


def expect(rep: Reporter, group: str, name: str, ok: bool, detail: str = "") -> bool:
    rep.add(group, name, "PASS" if ok else "FAIL", detail)
    return ok


def warn(rep: Reporter, group: str, name: str, detail: str) -> None:
    rep.add(group, name, "WARN", detail)


def info(rep: Reporter, group: str, name: str, detail: str) -> None:
    rep.add(group, name, "INFO", detail)


def env_err(rep: Reporter, group: str, name: str, detail: str) -> None:
    rep.add(group, name, "ENV-ERR", detail)


# ----- Section A: Root identity -------------------------------------------


def check_root(
    rep: Reporter, root_url: str, repo_root: str, timeout: float, retries: int
) -> Tuple[bool, Dict[str, int], Dict[str, float]]:
    latencies: Dict[str, float] = {}
    sizes: Dict[str, int] = {"root": 0, "second": 0}
    all_ok = True
    try:
        status, headers, body, latency = fetch(root_url, timeout=timeout, retries=retries)
    except HttpFetchError as e:
        env_err(rep, "A. Root production identity", "fetch root", str(e))
        return False, sizes, latencies
    latencies["root"] = latency
    text = body.decode("utf-8", errors="replace")
    sha = hashlib.sha256(body).hexdigest()
    sizes["root"] = len(body)

    if not expect(
        rep,
        "A. Root production identity",
        "HTTP 200 on root URL",
        status == 200,
        f"status={status}",
    ):
        all_ok = False

    if not expect(
        rep,
        "A. Root production identity",
        f"byte size = {ROOT_EXPECTED_BYTES}",
        len(body) == ROOT_EXPECTED_BYTES,
        f"actual={len(body)}",
    ):
        all_ok = False

    if not expect(
        rep,
        "A. Root production identity",
        "SHA256 matches freeze baseline",
        sha == ROOT_EXPECTED_SHA256,
        f"live={sha}",
    ):
        all_ok = False

    exact_count = text.count(ROOT_EXACT_MARKER)
    if not expect(
        rep,
        "A. Root production identity",
        f"exact marker '{ROOT_EXACT_MARKER}' count = {ROOT_EXACT_MARKER_COUNT}",
        exact_count == ROOT_EXACT_MARKER_COUNT,
        f"actual={exact_count}",
    ):
        all_ok = False

    loose_count = text.count(ROOT_LOOSE_MARKER)
    info(
        rep,
        "A. Root production identity",
        f"loose '{ROOT_LOOSE_MARKER}' count",
        f"actual={loose_count} (expected informational {ROOT_LOOSE_MARKER_COUNT})",
    )

    local_root = os.path.join(repo_root, "site", "index.html")
    if os.path.exists(local_root):
        try:
            with open(local_root, "rb") as f:
                local_bytes = f.read()
            local_sha = hashlib.sha256(local_bytes).hexdigest()
            identical = (local_sha == sha) and (len(local_bytes) == len(body))
            if not expect(
                rep,
                "A. Root production identity",
                "live root byte-identical to site/index.html",
                identical,
                f"local_sha={local_sha}",
            ):
                all_ok = False
        except OSError as e:
            warn(rep, "A. Root production identity", "read site/index.html", str(e))
    else:
        warn(
            rep,
            "A. Root production identity",
            "local site/index.html",
            "not found (run from repo root)",
        )

    return all_ok, sizes, latencies


# ----- Section B: Second exhibition identity ------------------------------


def count_adjacent_phrase_occurrences(text: str, phrase: str, context_markers: List[str]) -> int:
    """Count occurrences of `phrase` whose nearest context_marker
    (any of `context_markers`) is within a window of the phrase.

    Used to disambiguate `imported-not-deployed` (historical import
    record) from any current publication assertion. The live second-
    exhibition page only uses `imported-not-deployed` as a historical
    import record annotation, so its occurrences must fall inside one
    of the recognised historical-import contexts:

      * adjacent to "Import record:" — per-source note
      * followed by "(v4.5)" — version-history marker
      * adjacent to "asset-import-manifest" — manifest reference
        (used in the top and bottom page-level status paragraphs)
    """
    near = 0
    for m in re.finditer(re.escape(phrase), text):
        start = max(0, m.start() - 320)
        end = min(len(text), m.end() + 320)
        window = text[start:end]
        if any(cm in window for cm in context_markers):
            near += 1
    return near


def check_second(
    rep: Reporter,
    root_url: str,
    second_url: str,
    timeout: float,
    retries: int,
    candidate_v02: bool = False,
) -> Tuple[bool, Dict[str, int], Dict[str, float]]:
    all_ok = True
    sizes: Dict[str, int] = {}
    latencies: Dict[str, float] = {}
    try:
        status, headers, body, latency = fetch(second_url, timeout=timeout, retries=retries)
    except HttpFetchError as e:
        env_err(rep, "B. Second-exhibition identity", "fetch second URL", str(e))
        return False, sizes, latencies
    latencies["second"] = latency
    text = body.decode("utf-8", errors="replace")
    sizes["second"] = len(body)

    if candidate_v02:
        expected_bytes = SECOND_V02_CANDIDATE_BYTES
        expected_sha = SECOND_V02_CANDIDATE_SHA256
        byte_label = f"{SECOND_V02_CANDIDATE_BYTES} (v0.2 candidate staged)"
        sha_label = "SHA256 matches v0.2 candidate staged baseline (worker-only)"
    else:
        expected_bytes = SECOND_EXPECTED_BYTES
        expected_sha = SECOND_EXPECTED_SHA256
        byte_label = f"{SECOND_EXPECTED_BYTES}"
        sha_label = "SHA256 matches freeze baseline (live == staging artifact)"

    if not expect(
        rep,
        "B. Second-exhibition identity",
        "HTTP 200 on second-exhibition URL",
        status == 200,
        f"status={status}",
    ):
        all_ok = False

    if not expect(
        rep,
        "B. Second-exhibition identity",
        f"byte size = {byte_label}",
        len(body) == expected_bytes,
        f"actual={len(body)}",
    ):
        all_ok = False

    second_sha = hashlib.sha256(body).hexdigest()
    if not expect(
        rep,
        "B. Second-exhibition identity",
        sha_label,
        second_sha == expected_sha,
        f"live={second_sha}",
    ):
        all_ok = False

    if not expect(
        rep,
        "B. Second-exhibition identity",
        f"<title> contains '{SECOND_TITLE_FRAGMENT}'",
        SECOND_TITLE_FRAGMENT in text,
        "title fragment not found",
    ):
        all_ok = False

    for phrase, expected in EXPECTED_PHRASE_COUNTS.items():
        actual = text.count(phrase)
        if not expect(
            rep,
            "B. Second-exhibition identity",
            f"phrase '{phrase}' count = {expected}",
            actual == expected,
            f"actual={actual}",
        ):
            all_ok = False

    # Adjacent-history guard for imported-not-deployed: it must appear in
    # a recognised historical-import context, never as a current
    # publication assertion. Live page contexts:
    #   * per-source-note: "Import record: imported-not-deployed (v4.5)"
    #   * top/bottom page-level status: adjacent to "asset-import-manifest"
    imported_in_history = count_adjacent_phrase_occurrences(
        text,
        PHRASE_IMPORTED,
        ["Import record:", "(v4.5)", "asset-import-manifest"],
    )
    if not expect(
        rep,
        "B. Second-exhibition identity",
        "'imported-not-deployed' only appears in historical import context",
        imported_in_history == EXPECTED_PHRASE_COUNTS[PHRASE_IMPORTED],
        f"in historical context = {imported_in_history} (expected {EXPECTED_PHRASE_COUNTS[PHRASE_IMPORTED]})",
    ):
        all_ok = False

    forbidden_live_strs = ["未部署", "not deployed", "stale"]
    # These are checked as INFO only - wording can shift. The phrase-count
    # table above is the source of truth, not these substrings.
    for s in forbidden_live_strs:
        info(
            rep,
            "B. Second-exhibition identity",
            f"occurrences of '{s}'",
            f"count={text.count(s)}",
        )

    return all_ok, sizes, latencies


# ----- Section C + D: Public files & image integrity ----------------------


def check_public_files(
    rep: Reporter, root_url: str, timeout: float, retries: int
) -> bool:
    all_ok = True
    candidates = []
    for p in ROOT_PUBLIC:
        candidates.append(("root", root_url.rstrip("/") + "/" + p if p else root_url))
    for p in SECOND_PUBLIC:
        candidates.append(
            ("second", root_url.rstrip("/") + "/" + ("second-exhibition/" + p if p else "second-exhibition/"))
        )
    seen: Dict[str, Optional[int]] = {}
    for prefix, url in candidates:
        status, err = head_get_status(url, timeout=timeout, retries=retries)
        if err is not None:
            env_err(rep, "C. Public static files", f"{prefix} {url}", str(err))
            all_ok = False
            continue
        label = f"{prefix} {url.split('conanxin.github.io')[-1] or '/'}"
        if status != 200:
            # For trailing-slash variations, root listing may 404 but be ok
            # for index.html; allow if any of {prefix/, prefix/index.html} is 200.
            if not any(seen.get(f"{prefix}:{p}") == 200 for p in [c[1] for c in candidates if c[0] == prefix]):
                all_ok = False
        seen[f"{prefix}:{url}"] = status
        if not expect(
            rep,
            "C. Public static files",
            f"{label} HTTP 200",
            status == 200,
            f"status={status}",
        ):
            all_ok = False
    return all_ok


def sha256_of_url(url: str, timeout: float, retries: int) -> Tuple[Optional[int], Optional[str], Optional[str], Optional[HttpFetchError]]:
    try:
        status, headers, body, _lat = fetch(url, timeout=timeout, retries=retries)
    except HttpFetchError as e:
        return None, None, None, e
    return status, hashlib.sha256(body).hexdigest(), headers.get("content-type", ""), None


def load_checksum_file(repo_root: str) -> Dict[str, str]:
    path = os.path.join(repo_root, "second-exhibition", "assets", "asset-checksums.sha256")
    out: Dict[str, str] = {}
    if not os.path.exists(path):
        return out
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(None, 1)
            if len(parts) == 2:
                out[parts[1].strip()] = parts[0].strip()
    return out


def check_images(
    rep: Reporter, root_url: str, repo_root: str, timeout: float, retries: int
) -> bool:
    all_ok = True
    expected = load_checksum_file(repo_root)
    if not expected:
        warn(rep, "D. Image integrity", "checksum file", "not found locally; skipping identity test")
    for rel in IMAGE_PATHS:
        url = root_url.rstrip("/") + "/" + rel
        status, sha, ctype, err = sha256_of_url(url, timeout=timeout, retries=retries)
        if err is not None or status is None:
            env_err(rep, "D. Image integrity", rel, str(err) if err else "no status")
            all_ok = False
            continue
        ok_status = status == 200
        if not expect(
            rep,
            "D. Image integrity",
            f"{rel} HTTP 200",
            ok_status,
            f"status={status}",
        ):
            all_ok = False

        ext = os.path.splitext(rel)[1].lower()
        expected_mime = IMAGE_MIME_EXPECT.get(ext, set())
        if expected_mime:
            mime_ok = (ctype or "").lower() in {m.lower() for m in expected_mime}
            if not expect(
                rep,
                "D. Image integrity",
                f"{rel} content-type in {sorted(expected_mime)}",
                mime_ok,
                f"ctype={ctype}",
            ):
                all_ok = False

        want_sha = expected.get(os.path.join("second-exhibition", "assets", "images", os.path.basename(rel))) \
            or expected.get(rel)
        if want_sha and sha:
            if not expect(
                rep,
                "D. Image integrity",
                f"{rel} SHA256 match asset-checksums.sha256",
                sha == want_sha,
                f"want={want_sha[:12]}… live={(sha or '')[:12]}…",
            ):
                all_ok = False
        else:
            warn(rep, "D. Image integrity", rel, "no expected SHA in checksums file")
    return all_ok


# ----- Section E: Forbidden path boundary ---------------------------------


def check_forbidden(
    rep: Reporter, root_url: str, timeout: float, retries: int
) -> bool:
    all_ok = True
    for rel in FORBIDDEN_PATHS_404:
        if rel.startswith("second-exhibition/"):
            url = root_url.rstrip("/") + "/" + rel
        elif rel.startswith("."):
            url = root_url.rstrip("/") + "/" + rel
        else:
            url = root_url.rstrip("/") + "/" + rel
        status, err = head_get_status(url, timeout=timeout, retries=retries)
        label = rel
        if err is not None:
            env_err(rep, "E. Forbidden exposure boundary", label, str(err))
            all_ok = False
            continue
        # 404 is the desired outcome; 403 (GitHub Pages fallback) acceptable.
        ok = status in (404, 403)
        if not expect(
            rep,
            "E. Forbidden exposure boundary",
            f"{label} NOT 200",
            ok,
            f"status={status}",
        ):
            all_ok = False
    # Sanity: if every root-reachable forbidden request came back as a
    # network error, the environment is broken even if statuses look OK.
    return all_ok


# ----- Section F: Workflow static safety ----------------------------------


def check_workflow_safety(rep: Reporter, repo_root: str) -> bool:
    all_ok = True
    wf = os.path.join(repo_root, ".github", "workflows", "pages.yml")
    if not os.path.exists(wf):
        warn(rep, "F. Workflow static safety", ".github/workflows/pages.yml", "missing locally")
        return False
    with open(wf, "r", encoding="utf-8") as f:
        text = f.read()

    expectations = [
        ("staging_builder_step", "--output" in text and "--audit" in text, "builder step uses --output and --audit"),
        ("staging_gate_step", "second_exhibition_staging_gate" in text, "staging gate step present"),
        ("artifact_path", "leonardo-pages-artifact" in text, "artifact dir = leonardo-pages-artifact"),
        ("upload_pages_artifact", "actions/upload-pages-artifact" in text or "upload-pages-artifact" in text, "uses upload-pages-artifact"),
        ("configure_pages", "actions/configure-pages" in text, "configures Pages"),
        ("deploy_pages", "actions/deploy-pages" in text or "deploy" in text, "deploy step present"),
        ("no_repo_root_upload", "actions/upload-pages-artifact" in text and "." not in re.findall(r"path:\s*([^\n]+)", text)[-1:] or True, None),
    ]

    seen_builder = bool(re.search(r"second_exhibition_staging_build", text))
    seen_gate = bool(re.search(r"second_exhibition_staging_gate", text))
    if not expect(rep, "F. Workflow static safety", "staging builder step exists", seen_builder, ""):
        all_ok = False
    if not expect(rep, "F. Workflow static safety", "staging gate step exists", seen_gate, ""):
        all_ok = False
    if not expect(rep, "F. Workflow static safety", "builder invokes both --output and --audit", "--output" in text and "--audit" in text, ""):
        all_ok = False
    if not expect(rep, "F. Workflow static safety", "deploy uses leonardo-pages-artifact", "leonardo-pages-artifact" in text, ""):
        all_ok = False
    if not expect(rep, "F. Workflow static safety", "uses actions/configure-pages", "configure-pages" in text, ""):
        all_ok = False
    if not expect(rep, "F. Workflow static safety", "uses actions/deploy-pages", "deploy-pages" in text, ""):
        all_ok = False

    # Audit directory must not be uploaded. Look for any explicit
    # reference to it near a `path:` line.
    audit_uploaded = bool(re.search(r"path:\s*[^\n]*audit", text))
    if not expect(rep, "F. Workflow static safety", "audit dir not uploaded as artifact", not audit_uploaded, f"audit_uploaded={audit_uploaded}"):
        all_ok = False

    # No reference to repository root in the upload step.
    root_uploaded = bool(re.search(r"path:\s*\.\s*\n", text)) or bool(re.search(r"path:\s*\.\s*$", text, re.M))
    if not expect(rep, "F. Workflow static safety", "repository root not uploaded", not root_uploaded, f"root_uploaded={root_uploaded}"):
        all_ok = False

    return all_ok


# ----- Section G: Stable release identity (no GitHub API) -----------------


def check_release_identity(rep: Reporter, repo_root: str) -> bool:
    all_ok = True
    tag_name = "v5.0-real-second-exhibition-deployment"
    expected_target = "ac0f19e2c03b09738ae49b4a15c629a1f2177068"
    try:
        rev = subprocess.run(
            ["git", "rev-parse", tag_name],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        peeled = subprocess.run(
            ["git", "rev-parse", f"{tag_name}^{{}}"],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        cat_t = subprocess.run(
            ["git", "cat-file", "-t", tag_name],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
    except Exception as e:
        env_err(rep, "G. Stable release identity", "git invocation", str(e))
        return False

    tag_object = (rev.stdout or "").strip()
    target = (peeled.stdout or "").strip()
    cat_type = (cat_t.stdout or "").strip()
    head_sha = (head.stdout or "").strip()

    if not expect(
        rep,
        "G. Stable release identity",
        f"tag {tag_name} exists locally",
        bool(tag_object),
        f"object={tag_object}",
    ):
        all_ok = False
    if not expect(
        rep,
        "G. Stable release identity",
        "tag type is 'tag' (annotated)",
        cat_type == "tag",
        f"type={cat_type}",
    ):
        all_ok = False
    if not expect(
        rep,
        "G. Stable release identity",
        f"tag target = {expected_target[:12]}…",
        target == expected_target,
        f"target={target}",
    ):
        all_ok = False
    # HEAD may be at or past the tag target — both are acceptable.
    info(
        rep,
        "G. Stable release identity",
        "current HEAD",
        f"head={head_sha} (tag target {target} allowed behind HEAD)",
    )

    return all_ok


# ----- Main entry point ---------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Production health check for the second exhibition"
    )
    p.add_argument("--root-url", default=ROOT_URL_DEFAULT)
    p.add_argument("--second-url", default=SECOND_URL_DEFAULT)
    p.add_argument("--timeout", type=float, default=15.0)
    p.add_argument("--retries", type=int, default=2)
    p.add_argument("--json-output", default=None, help="optional JSON report path")
    p.add_argument(
        "--repo-root", default=os.getcwd(),
        help="path used to read site/index.html and asset checksums",
    )
    p.add_argument(
        "--candidate-v0.2", action="store_true", dest="candidate_v02",
        help="Compare second-exhibition bytes/SHA against v5.6b v0.2 candidate "
             "baseline (worker-only); must point --second-url at the candidate "
             "host (NOT live production). Does NOT affect root baseline.",
    )
    args = p.parse_args(argv)

    repo_root = os.path.abspath(args.repo_root)
    if not os.path.isdir(repo_root):
        print(f"WARN: repo-root {repo_root} not a directory; some checks will WARN", file=sys.stderr)

    rep = Reporter()

    ok_a, sizes_a, lat_a = check_root(rep, args.root_url, repo_root, args.timeout, args.retries)
    ok_b, sizes_b, lat_b = check_second(
        rep, args.root_url, args.second_url, args.timeout, args.retries,
        candidate_v02=args.candidate_v02,
    )
    ok_c = check_public_files(rep, args.root_url, args.timeout, args.retries)
    ok_d = check_images(rep, args.root_url, repo_root, args.timeout, args.retries)
    ok_e = check_forbidden(rep, args.root_url, args.timeout, args.retries)
    ok_f = check_workflow_safety(rep, repo_root)
    ok_g = check_release_identity(rep, repo_root)

    counts = rep.counts()
    final_ok = (
        ok_a and ok_b and ok_c and ok_d and ok_e and ok_f and ok_g
    )

    # Human-readable report ------------------------------------------------
    print("=" * 70)
    print(f"Production healthcheck @ {datetime.datetime.utcnow().isoformat()}Z")
    print(f"  root:  {args.root_url}")
    print(f"  second:{args.second_url}")
    print("=" * 70)
    for group, items in rep.groups.items():
        print(f"\n[{group}]")
        for it in items:
            line = f"  [{it['status']:<7}] {it['name']}"
            if it["detail"]:
                line += f"  ({it['detail']})"
            print(line)
    print("\n" + "-" * 70)
    print(f"checks: total={counts['TOTAL']} pass={counts['PASS']} fail={counts['FAIL']} "
          f"warn={counts['WARN']} info={counts['INFO']} env_err={counts['ENV-ERR']}")
    if lat_a:
        print(f"latency root: {lat_a.get('root', 0)*1000:.0f} ms")
    if lat_b:
        print(f"latency second: {lat_b.get('second', 0)*1000:.0f} ms")
    if sizes_a.get("root"):
        print(f"downloaded bytes root: {sizes_a['root']}")
    if sizes_b.get("second"):
        print(f"downloaded bytes second: {sizes_b['second']}")
    print("-" * 70)
    print(f"FINAL STATUS: {'PASS' if final_ok and rep.env_errors == 0 else 'FAIL' if final_ok is False or rep.env_errors == 0 else 'ENV-ERROR'}")
    print("=" * 70)

    # JSON output ---------------------------------------------------------
    if args.json_output:
        out = OrderedDict()
        out["timestamp_utc"] = datetime.datetime.utcnow().isoformat() + "Z"
        out["root_url"] = args.root_url
        out["second_url"] = args.second_url
        out["counts"] = counts
        out["latency_ms"] = {
            "root": round(lat_a.get("root", 0) * 1000, 1) if lat_a else 0,
            "second": round(lat_b.get("second", 0) * 1000, 1) if lat_b else 0,
        }
        out["downloaded_bytes"] = {
            "root": sizes_a.get("root", 0),
            "second": sizes_b.get("second", 0),
        }
        out["groups"] = OrderedDict()
        for group, items in rep.groups.items():
            out["groups"][group] = items
        out["final_ok"] = bool(final_ok and rep.env_errors == 0)
        try:
            with open(args.json_output, "w", encoding="utf-8") as f:
                json.dump(out, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"WARN: failed to write JSON output: {e}", file=sys.stderr)

    if rep.env_errors > 0:
        return 2
    if not final_ok:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
