# Second Exhibition Deployment Dry Run — v5.2

**Round:** v5.2-deployment-dry-run
**Date:** 2026-07-11
**STATUS:** **PASS** — dry-run only, no production deploy

---

## Goal

Simulate the GitHub Pages project-site deployment of `v5.1` staging artifact under the
canonical project-site base path:

```
/leonardo-chinese-exhibition/
```

…without pushing to `main`, without modifying `.github/workflows/pages.yml`, without
creating a tag or Release.

Three simulations in one run:

1. **Base-path HTTP probe** — start a local base-path server, probe every allowlisted
   URL under the project-site base, and verify forbidden paths return 404.
2. **Pack + roundtrip** — pack the staging artifact into a tarball, unpack it to a
   fresh directory, verify per-file SHA256 identity.
3. **Rollback rehearsal** — confirm the current workflow has exactly one `path: site`
   line and document the one-line revert that would restore production state.

A fourth step — **base-path browser QA** — runs the existing browser QA runner against
the same base-path URL via a thin wrapper script.

---

## Inputs

| Input | Value | Source |
|-------|-------|--------|
| Staging artifact | `/tmp/leonardo-pages-artifact` (built by `scripts/second_exhibition_staging_build.py`) | v5.1 |
| Audit dir | `/tmp/leonardo-pages-artifact-audit` (sibling of artifact) | v5.1 |
| Project-site base path | `/leonardo-chinese-exhibition` | repo name |
| Local HTTP server | inline `BasePathHTTPRequestHandler` in `scripts/second_exhibition_deployment_dry_run.py` | this round |
| Browser QA wrapper | `scripts/second_exhibition_deployment_dry_run_browser.mjs` (delegates to `scripts/second_exhibition_browser_qa.mjs`) | this round |

The dry-run script also writes:

| Output | Purpose |
|--------|---------|
| `/tmp/leonardo-pages-dry-run/` | dry-run output dir |
| `/tmp/leonardo-pages-dry-run/report.json` | JSON summary of probes + roundtrip + rollback rehearsal |
| `/tmp/leonardo-pages-dry-run/browser-qa.json` | base-path browser QA summary |
| `/tmp/leonardo-pages-roundtrip/` | unpacked copy of the artifact tarball |
| `/tmp/leonardo-pages-artifact.tar.gz` | packed staging artifact (excludes audit dir) |

None of these paths are inside the repository.

---

## Section A — Base-path HTTP probe

Server: `python3 -c "BasePathHTTPRequestHandler(...)"` listening on a random free port,
translating `/leonardo-chinese-exhibition/<path>` → `<artifact>/<path>`.

**Allowlist probes (14/14 PASS):**

| URL | Expected | Actual | Bytes |
|-----|---------:|-------:|------:|
| `/leonardo-chinese-exhibition/` | 200 | 200 | 92,976 |
| `/leonardo-chinese-exhibition/index.html` | 200 | 200 | 92,976 |
| `/leonardo-chinese-exhibition/style.css` | 200 | 200 | 42,079 |
| `/leonardo-chinese-exhibition/script.js` | 200 | 200 | 14,594 |
| `/leonardo-chinese-exhibition/second-exhibition/` | 200 | 200 | 24,380 |
| `/leonardo-chinese-exhibition/second-exhibition/index.html` | 200 | 200 | 24,380 |
| `/leonardo-chinese-exhibition/second-exhibition/style.css` | 200 | 200 | 8,261 |
| `/leonardo-chinese-exhibition/second-exhibition/script.js` | 200 | 200 | 4,070 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` | 200 | 200 | 306,126 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` | 200 | 200 | 262,498 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/smithsonian-nmnh-1529703.png` | 200 | 200 | 3,550 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/met-285149.jpg` | 200 | 200 | 95,001 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` | 200 | 200 | 294,445 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` | 200 | 200 | 191,606 |

**Special assertions (PASS):**

- Root `index.html` byte count = **92,976** (matches production live)
- Root `index.html` contains `v2.9-real-source-rights-audit` marker
- `/second-exhibition/index.html` contains the Chinese title `植物图谱与视觉分类` (count = 2)
- Staged `/second-exhibition/index.html` has **0** `../assets/images/` references (path rewrite complete)
- Staged `/second-exhibition/index.html` has **6** `./assets/images/` references (image src + href)
- All 6 image links resolve under the project-site base path

**Forbidden probes (16/16 PASS, all 404):**

| Path | Status |
|------|-------:|
| `/leonardo-chinese-exhibition/second-exhibition/data/` | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/docs/` | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/data/exhibition.json` | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/data/sections.json` | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/docs/RIGHTS_AND_SOURCES.md` | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/asset-import-manifest.json` | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/asset-checksums.sha256` | 404 |
| `/leonardo-chinese-exhibition/_template/` | 404 |
| `/leonardo-chinese-exhibition/_pilots/` | 404 |
| `/leonardo-chinese-exhibition/reports/` | 404 |
| `/leonardo-chinese-exhibition/scripts/` | 404 |
| `/leonardo-chinese-exhibition/.firecrawl/` | 404 |
| `/leonardo-chinese-exhibition/README.md` | 404 |
| `/leonardo-chinese-exhibition/V4_ROADMAP.md` | 404 |
| `/leonardo-chinese-exhibition/V5_ROADMAP.md` | 404 |

**Out-of-base sanity:**

- `http://127.0.0.1:<port>/some-other-base/second-exhibition/` → **404** (correctly not served).

---

## Section B — Artifact pack + roundtrip

| Metric | Value |
|--------|------:|
| Files packed | 34 |
| Tar size | **5,802,670 bytes** |
| Tar path | `/tmp/leonardo-pages-artifact.tar.gz` |
| Roundtrip dir | `/tmp/leonardo-pages-roundtrip` |
| File count match (src vs roundtrip) | 34 / 34 |
| SHA256 identity | all 34 files byte-identical |
| Roundtrip `index.html` byte count | 92,976 |

The artifact packs cleanly into a tar.gz and unpacks to a directory tree that is
**byte-identical** to the source artifact (per-file SHA256 verified). This proves the
artifact is reproducible as a transport artifact (the same byte sequence arrives at
the deployer after pack/untar).

---

## Section C — Rollback rehearsal

| Item | Value |
|------|-------|
| Current workflow `path:` line | `          path: site` |
| Occurrences of `path: site` in workflow | exactly 1 |
| Proposed change | `          path: site` → `          path: __STAGING_ARTIFACT_DIR__` |
| Diff size | **1 line** |
| Rollback method | `git revert <deployment-commit>` produces a 1-line diff that restores `path: site` |
| Workflow modified by this round? | **No** (verified by re-reading the file after the dry-run) |

A 1-line revert restores production. The rollback rehearsal is purely textual — no
`git revert` was executed.

---

## Section D — Base-path browser QA

The wrapper `scripts/second_exhibition_deployment_dry_run_browser.mjs`:

1. Reads `/tmp/leonardo-pages-dry-run/report.json` for the captured port (or accepts
   `SECOND_EXHIBITION_BASEPATH_URL` env override).
2. Spawns the existing `scripts/second_exhibition_browser_qa.mjs` runner with
   `SECOND_EXHIBITION_QA_URL=http://127.0.0.1:8773/leonardo-chinese-exhibition/second-exhibition/`.
3. Parses the JSON summary emitted by the runner.
4. Adds a base-path assertion summary (URL starts with `/leonardo-chinese-exhibition/`,
   image src values resolve under base path, no external requests).

**Result: PASS, 5/5 viewports.**

| Viewport | Result |
|----------|:------:|
| 1440 × 1000 | PASS |
| 1280 × 900 | PASS |
| 768 × 1024 | PASS |
| 390 × 844 | PASS |
| 320 × 700 | PASS |

| Counter | Value |
|---------|------:|
| Console errors | 0 |
| Page errors | 0 |
| Failed requests | 0 |
| External requests | 0 |
| Horizontal overflow | 0 |
| Images loaded per viewport | 6 / 6 |

Interactions verified: guided-toggle, lightbox (role=dialog, aria-labelledby=lightbox-title),
ESC close, focus return, section-nav, tab traversal, C-06 stays closed on initial load.

Accessibility verified: 1 `<h1>`, 0 missing alt, 0 missing button names, visually-hidden
title correctly measured (1×1 px, `position: absolute`).

Reduced-motion: lightbox opens + ESC closes correctly under `prefers-reduced-motion`.

No-JS path: 6 cards / 6 source notes / 6 credit lines / repo-status banner visible /
body text content present.

The wrapper itself writes `/tmp/leonardo-pages-dry-run/browser-qa.json`.

---

## What was NOT done

- No push to `main` of any workflow change.
- No call to `actions/deploy-pages`.
- No change to GitHub Pages settings.
- No CNAME modification.
- No repository-root upload.
- No staging artifact committed to the repository.
- No `dist/`, `build/`, `staging/` directory inside the repository.
- No second-exhibition image downloaded or replaced.
- No `.firecrawl/` directory touched.
- No tag created.
- No GitHub Release created.

---

## Production state after v5.2

| Check | Result |
|-------|--------|
| `.github/workflows/pages.yml` modified? | **No** |
| Production live byte | **92,976 B** (unchanged) |
| Production v2.9 marker | **1** (unchanged) |
| `/second-exhibition/` Pages URL | **404** |
| All sub-URLs under `/second-exhibition/` | **404** |
| Tags | unchanged (12 tags v2.0–v4.8) |
| Releases | unchanged (no new Release) |

---

## Reproduce

```bash
# 1. Build staging artifact (v5.1)
python3 scripts/second_exhibition_staging_build.py \
  --output /tmp/leonardo-pages-artifact

# 2. Run dry-run (auto-finds a free port)
python3 scripts/second_exhibition_deployment_dry_run.py

# 3. Inspect outputs
cat /tmp/leonardo-pages-dry-run/report.json
ls -la /tmp/leonardo-pages-roundtrip/ /tmp/leonardo-pages-artifact.tar.gz

# 4. Run base-path browser QA (needs Playwright at /tmp/playwright-test/node_modules)
#    Server must still be running. The dry-run script's HTTP server shuts down
#    at end of run, so start a separate base-path server for the browser QA:
python3 -m http.server 8773 --directory /tmp/leonardo-pages-artifact &
# NOTE: this serves at /; for the project-site base path, use the inline
# BasePathHTTPRequestHandler logic from the dry-run script.

SECOND_EXHIBITION_BASEPATH_URL=http://127.0.0.1:8773/leonardo-chinese-exhibition/second-exhibition/ \
  node scripts/second_exhibition_deployment_dry_run_browser.mjs
```

---

## Next task

**v5.3-controlled-deployment** — actually push the workflow change to `main`, verify
that the existing live byte stays at 92,976 B, verify the new `/second-exhibition/`
URL returns 200, run browser QA against the public URL.

(Today's v5.2 round deliberately does NOT take that step.)