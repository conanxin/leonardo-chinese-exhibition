# v5.6d (round 2) Live Browser QA Reproducibility Report

- **Round**: v5.6d (round 2) — Live browser QA reproducibility, real-bug fix
- **Date**: 2026-07-12
- **Trigger**: v5.6d round 1 (commit `96bef6a`) promoted v5.6c's
  temporary-runner fixes into the official runner, but the
  reproduction-target spec (`images loaded = 6`) is non-deterministic
  on the public URL's cold cache — `setTimeout(800)` tail wait + 3 s
  per-image timeout is sometimes not enough for BHL's 2 lazy `webp`
  images to complete fetch + decode.
- **Status**: PASS

## 1. Baseline

- Pre-v5.6d-r2 HEAD: `96bef6a4c16745dc420630a6df081c663c440929`
- Pre-v5.6d-r2 origin/main: `96bef6a4c16745dc420630a6df081c663c440929`
- Stable v5.0 tag: `v5.0-real-second-exhibition-deployment` →
  `ac0f19e2c03b09738ae49b4a15c629a1f2177068` (unchanged)
- Stable Release: published, unchanged

## 2. Reality gate (this round)

| Check | Result |
|---|---|
| HEAD == origin/main | PASS |
| tracked tree clean before edits | PASS (only `__pycache__` removed) |
| `.firecrawl/` ignored as expected | PASS |
| `__pycache__` cleanup | PASS (none present) |
| `template_quality_gate` | PASS |
| `second_exhibition_build_gate` | PASS |
| `second_exhibition_repository_qa` | 166/0/0 |
| `second_exhibition_production_healthcheck` | 70/0 (default mode) |
| 6/6 asset checksums | OK |

## 3. Initial official runner result (this round, BEFORE the fix)

`SECOND_EXHIBITION_QA_URL=https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/ \
 PLAYWRIGHT_NODE_PATH=… node scripts/second_exhibition_browser_qa.mjs`

- Run 1: **FAIL** — exit 1, 4/5 viewports pass, 1440×1000 failed
  (`images loaded = 5`, expected 6)
- Run 2 (immediate retry, hot cache): **PASS** — exit 0, 5/5 viewports,
  imgsLoaded `[6, 6, 6, 6, 6]`

Conclusion: the official runner (as of `96bef6a`) is
**non-deterministic** on the public URL's cold cache. Brief §4 C
requires that the 6 images must actually load — the fix is required.

## 4. v5.6c temporary runner comparison (this round)

`diff -u scripts/second_exhibition_browser_qa.mjs /tmp/v56c-live-browser-qa.mjs`

Differences categorized per brief §3:

| Category | v5.6c temporary | v5.6d official (after edits) |
|---|---|---|
| Playwright module resolution | hardcoded `~/.local/...` + `/tmp/playwright-test/...` | env `PLAYWRIGHT_NODE_PATH` + `require("playwright")` + `require("playwright-core")` |
| HTTPS pre-flight | implicit (no pre-flight) | explicit `https.request` |
| Origin-aware tracking | `url.startsWith(TARGET_URL.split("/s")[0])` | `url.startsWith(ORIGIN)` helper |
| Lazy image scroll | `scrollIntoView()` per-image + 1500 ms hydration | scroll-to-bottom + 1500 ms tail wait |
| Per-image load timeout | 3000 ms (in `checkPage`) | 5000 ms |
| Selectors | identical | identical |
| Interactions | identical | identical |
| Result serialization | `JSON.stringify` | `JSON.stringify` |
| Default URL | hardcoded public URL | preserves `http://127.0.0.1:8770/site/` (v4.8 compat) |
| Exit codes | none explicit | 0/1/2 (v4.8) |

**Items explicitly NOT ported** (per brief §3 forbidden list):

- absolute user paths (`/home/conanxin/...`, `~/.local/...`)
- ad-hoc `/tmp/playwright-test/...` location
- machine-specific Chromium executable path
- unbounded `setTimeout` waits
- silent `try/catch` around failures
- "FAIL → WARN" downgrades

## 5. Runner modifications (this round)

`scripts/second_exhibition_browser_qa.mjs` — only file changed:

1. `runViewport()` lazy-load tail wait: `setTimeout(800)` →
   `setTimeout(1500)` after the scroll-to-bottom step, with an
   inline comment explaining the cold-cache rationale.
2. Per-image `setTimeout` cap in the load poll: `3000` → `5000`, with
   an inline comment explaining the bound (a slow cold-cache 404
   should still surface as not-loaded rather than hanging the whole
   viewport).

Net diff: `1 file changed, 12 insertions(+), 2 deletions(-)`. Both
numbers are bounded waits; no unbounded waits introduced.

## 6. Playwright resolution (post-fix)

`loadPlaywright()` is unchanged since v4.8. It accepts the
`PLAYWRIGHT_NODE_PATH` env var and falls back to `require("playwright")`
then `require("playwright-core")`. No hardcoded user home, no
hardcoded `/tmp` path, no machine-specific Chromium executable path.
The runtime result is reported under `RESULTS.browser.source` — the
runner tells the caller which path it picked.

## 7. Local exact-base-path 5-viewport matrix (this round, post-fix)

Server: `python3 -m http.server 8772` over `/tmp/v56d-artifact` (the
v5.6d staging artifact), base path `/leonardo-chinese-exhibition`.

URL: `http://127.0.0.1:8772/leonardo-chinese-exhibition/second-exhibition/`

| Run | Status | viewports | imgsLoaded per vp | err (ext/fail/con/page) |
|---|---|---|---|---|
| 1 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 2 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 3 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |

Per-run detail (any of the 3):

- interactions: guidedToggle / lightboxOpen / lightboxRole=dialog /
  lightboxAccessibleName=`lightbox-title` / closeButtonFocused /
  escClose / focusReturn / c06LightboxOpen=false / sectionNav /
  tabFocusable — all true
- a11y: h1=1, imgMissingAlt=0, buttonMissingName=0, headingJump=false
- no-JS: 6 cards / 6 source notes / 6 credit lines / repo status
  visible / body text
- reduced-motion: lightboxOpen + escClose

## 8. Production 5-viewport matrix (this round, post-fix)

URL: `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`

| Run | Status | viewports | imgsLoaded per vp | err (ext/fail/con/page) |
|---|---|---|---|---|
| 1 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 2 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 3 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |

Per-run detail: identical interactions / a11y / no-JS / reduced-motion
to local. Browser: chromium 148.0.7778.96 (via
`PLAYWRIGHT_NODE_PATH`).

## 9. Staging dry-run (this round)

```text
python3 scripts/second_exhibition_staging_build.py \
  --output /tmp/v56d-artifact --audit /tmp/v56d-audit
# PASS: staging build complete
#   output: /tmp/v56d-artifact
#   audit : /tmp/v56d-audit
#   root site files     : 25
#   second-exhibition   : 9
#   path rewrite count  : 6
#   deployment_status   : staging-only-not-deployed

python3 scripts/second_exhibition_staging_gate.py \
  --artifact /tmp/v56d-artifact --audit /tmp/v56d-audit
# PASS: staging gate — 25 main-site + 9 second-exhibition files verified
# source SHA 662bee… → staged SHA 00894e8d… (6 path rewrites, expected)
# schema 2.0

python3 scripts/second_exhibition_deployment_dry_run.py \
  --artifact /tmp/v56d-artifact --audit /tmp/v56d-audit \
  --dry-run-dir /tmp/v56d-dry-run --roundtrip-dir /tmp/v56d-roundtrip \
  --tar /tmp/v56d-artifact.tar.gz \
  --repo-base /leonardo-chinese-exhibition --server-port 8772
# PASS: v5.2+v5.3-aware deployment dry-run complete
#   allowlist probes : 14/14
#   forbidden probes : 16/16
#   roundtrip files  : 34 byte-identical
#   tar size         : 5804964 bytes
#   deployment_status: dry-run-only-not-deployed
```

## 10. Public artifact identity (this round)

| Identity | Pre-v5.6d-r2 | Post-v5.6d-r2 (live probe) | Same? |
|---|---|---|---|
| root bytes | 92,976 | 92,976 | yes |
| root SHA256 | `e2be1077…` | `e2be1077…` | yes |
| second bytes | 31,452 | 31,452 | yes |
| second SHA256 | `00894e8d…` | `00894e8d…` | yes |
| `second-exhibition-v0.2` marker count | 3 | 3 | yes |
| stale `second-exhibition-v0.1` count | 0 | 0 | yes |
| 6 image checksums | OK | OK | yes |
| Default healthcheck | 70/0 | 70/0 | yes |
| Forbidden paths (`_template/`, `_pilots/`, `scripts/`, `posts/`, `case-study/`, `release-assets/`) | 404 | 404 | yes |

## 11. Scope guard (this round)

Modified files (working tree, this round):

- `scripts/second_exhibition_browser_qa.mjs` (additive only — see §5)
- `docs/SECOND_EXHIBITION_LIVE_BROWSER_QA_REPRODUCIBILITY_v5.6d.md`
  (round-2 version, replaces / extends the `96bef6a` version)
- `docs/V5_ROADMAP.md` (round-2 section appended)
- `README.md` (round-2 section appended)
- `reports/leonardo_chinese_exhibition_v5_6d_live_browser_qa_reproducibility_report.md`
  (this file, new)

Protected paths (all empty diffs):

- `site/`
- `second-exhibition/site/`, `second-exhibition/data/`,
  `second-exhibition/assets/`, `second-exhibition/docs/`
- `.github/workflows/`
- `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`
- All other `scripts/*.py`
- No `__pycache__` in working tree
- No `.gitignore` change
- No new tag, no new Release

## 12. No-touch confirmation

- Public production surface — **unchanged** ✓
- 6 image files — **unchanged** (same SHA) ✓
- Source / rights evidence — **unchanged** ✓
- Workflow — **unchanged** ✓
- Stable v5.0 tag `v5.0-real-second-exhibition-deployment` →
  `ac0f19e2c03b…` — **unchanged** ✓
- Stable Release — **unchanged** ✓

## 13. Files modified (final)

1. `scripts/second_exhibition_browser_qa.mjs` — 12+ / 2- (lazy-load tail + per-image cap)
2. `docs/SECOND_EXHIBITION_LIVE_BROWSER_QA_REPRODUCIBILITY_v5.6d.md` (new / round-2)
3. `docs/V5_ROADMAP.md` (round-2 section appended)
4. `README.md` (round-2 section appended)
5. `reports/leonardo_chinese_exhibition_v5_6d_live_browser_qa_reproducibility_report.md` (this file, new)

## 14. Next recommended task

- **v5.6-real-stable-freeze**
