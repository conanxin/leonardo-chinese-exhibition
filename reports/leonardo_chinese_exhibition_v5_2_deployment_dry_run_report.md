# Leonardo Chinese Exhibition — v5.2 Deployment Dry Run Report

**Round:** v5.2-deployment-dry-run
**Date:** 2026-07-11
**STATUS:** **PASS** — dry-run only, no production deploy

---

## Baseline

| Item | Value |
|------|-------|
| Baseline HEAD | `0bc9c9959d5c382b4f6c40757220f3d0dab4fd7c` |
| Origin/main | `0bc9c9959d5c382b4f6c40757220f3d0dab4fd7c` (matches) |
| Source tag | `v4.8-real-second-exhibition-repository-hardening` |
| Source tag object | `1c868b054424c348f273be4148a6a3f184e374ba` (annotated) |
| Source tag target | `a70c8430a8e3d01153153e54f055d9907340d6b7` |
| Existing live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Existing live byte | **92,976 B** (unchanged) |
| Production v2.9 marker | **1** (unchanged) |
| Production Pages workflow | `path: site` only (unchanged) |
| `/second-exhibition/` Pages paths | all **404** (unchanged) |

---

## Pre-flight quality gates

| Gate | Result |
|------|--------|
| Template quality gate | PASS 37/37 |
| Second-exhibition build gate | PASS |
| Repository QA | 161 PASS / 0 FAIL / 0 WARNINGS |
| v5.1 staging build | PASS (exit 0) — 25 main-site + 9 second-exhibition files |
| v5.1 staging gate | PASS (exit 0) — 8 sections A–H green |

---

## Dry-run summary

| Item | Value |
|------|-------|
| Dry-run script | `scripts/second_exhibition_deployment_dry_run.py` |
| Browser QA wrapper | `scripts/second_exhibition_deployment_dry_run_browser.mjs` |
| Project-site base path | `/leonardo-chinese-exhibition` |
| Dry-run output dir | `/tmp/leonardo-pages-dry-run` |
| Dry-run report | `/tmp/leonardo-pages-dry-run/report.json` |
| Browser QA output | `/tmp/leonardo-pages-dry-run/browser-qa.json` |
| Pack output | `/tmp/leonardo-pages-artifact.tar.gz` |
| Roundtrip output | `/tmp/leonardo-pages-roundtrip` |
| `deployment_status` | `dry-run-only-not-deployed` |
| Final exit code | **0 (PASS)** |

---

## Section A — Base-path HTTP probe

| Probe group | Result |
|-------------|--------|
| Allowlist probes | **14/14** returned expected status |
| Forbidden probes | **16/16** returned 404 |
| Out-of-base sanity | 1/1 returned 404 |
| Root index byte | **92,976** (matches production) |
| v2.9 marker count | **1** |
| Second-exhibition title present | **yes** (`植物图谱与视觉分类` × 2) |
| Staged `../assets/images/` count | **0** (path rewrite complete) |
| Staged `./assets/images/` count | **6** |
| Image links resolve under base path | **6/6** |

Sample probes (full list in
`docs/SECOND_EXHIBITION_BASE_PATH_QA_v5.2.md`):

| URL pattern under base | HTTP | Bytes |
|------------------------|-----:|------:|
| `/leonardo-chinese-exhibition/` | 200 | 92,976 |
| `/leonardo-chinese-exhibition/style.css` | 200 | 42,079 |
| `/leonardo-chinese-exhibition/script.js` | 200 | 14,594 |
| `/leonardo-chinese-exhibition/second-exhibition/` | 200 | 24,380 |
| `/leonardo-chinese-exhibition/second-exhibition/style.css` | 200 | 8,261 |
| `/leonardo-chinese-exhibition/second-exhibition/script.js` | 200 | 4,070 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` | 200 | 306,126 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/smithsonian-nmnh-1529703.png` | 200 | 3,550 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/images/met-285149.jpg` | 200 | 95,001 |

---

## Section B — Artifact pack + roundtrip

| Metric | Value |
|--------|------:|
| Files packed | 34 |
| Tar size | **5,802,670 bytes** |
| Tar path | `/tmp/leonardo-pages-artifact.tar.gz` |
| Roundtrip dir | `/tmp/leonardo-pages-roundtrip` |
| File count match | 34 / 34 |
| Per-file SHA256 identity | all 34 byte-identical |
| Roundtrip `index.html` byte count | 92,976 |

---

## Section C — Rollback rehearsal

| Item | Value |
|------|-------|
| Current `path:` line in workflow | `          path: site` (occurs exactly once) |
| Proposed change | `          path: site` → `          path: __STAGING_ARTIFACT_DIR__` |
| Diff size | **1 line** |
| Rollback method | `git revert <deployment-commit>` produces a 1-line diff that restores `path: site` |
| Workflow modified by v5.2? | **No** |

---

## Section D — Base-path browser QA

| Item | Value |
|------|-------|
| Target URL | `http://127.0.0.1:8773/leonardo-chinese-exhibition/second-exhibition/` |
| Viewports passed | **5 / 5** (1440×1000, 1280×900, 768×1024, 390×844, 320×700) |
| Console errors | 0 |
| Page errors | 0 |
| Failed requests | 0 |
| External requests | 0 |
| Horizontal overflow | 0 |
| Images loaded per viewport | 6 / 6 |
| Interactions verified | guided-toggle, lightbox (role=dialog), ESC, focus return, section-nav, tab traversal, C-06 stays closed |
| a11y | 1 h1, 0 missing alt, 0 missing button names, visually-hidden title 1×1 px |
| no-JS | 6 cards / 6 source notes / 6 credit lines / repo-status banner visible / body text |
| Reduced motion | lightbox opens + ESC closes correctly |

---

## What was NOT done (and was required not to do)

- No push to `main` of any workflow change.
- No call to `actions/deploy-pages`.
- No change to GitHub Pages settings.
- No CNAME modification.
- No staging artifact committed to the repository.
- No `dist/`, `build/`, `staging/` directory inside the repository.
- No second-exhibition image downloaded or replaced.
- No `.firecrawl/` directory touched.
- No tag created.
- No GitHub Release created.
- No `git add .` used.

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
| Releases | unchanged |
| Repository contains staging artifact? | **No** (in `/tmp` only) |
| Repository contains dry-run report? | **No** (in `/tmp` only) |

---

## Files added/modified in v5.2

- `scripts/second_exhibition_deployment_dry_run.py` (new)
- `scripts/second_exhibition_deployment_dry_run_browser.mjs` (new)
- `docs/SECOND_EXHIBITION_DEPLOYMENT_DRY_RUN_v5.2.md` (new)
- `docs/SECOND_EXHIBITION_BASE_PATH_QA_v5.2.md` (new)
- `docs/SECOND_EXHIBITION_ROLLBACK_PLAN_v5.2.md` (new)
- `docs/V5_ROADMAP.md` (updated — v5.2 actual result section added)
- `README.md` (updated — v5.2 block added)
- `reports/leonardo_chinese_exhibition_v5_2_deployment_dry_run_report.md` (this file)

No protected path was modified. No workflow change. No tag. No Release.

---

## Next recommended task

**v5.3-controlled-deployment** — push the one-line workflow change to `main`,
verify that the existing live byte stays at 92,976 B, verify the new
`/second-exhibition/` URL returns 200, run browser QA against the public URL.