# v5.3b Production State Reconciliation — Prep Report

## STATUS

`READY_FOR_MANUAL_DEPLOY_APPROVAL` — awaiting `DEPLOY v5.3b` from user.

## Baseline

| Field | Value |
|---|---|
| HEAD | `83ab6d8bc8a3f278d53c72516cf72d1a747e13bd` |
| origin/main | `83ab6d8bc8a3f278d53c72516cf72d1a747e13bd` (identical) |
| Local ≡ Remote | identical (no commit/push this round) |
| `git reflog` | unchanged at HEAD (no new commits) |
| Working tree | 12 modified tracked files + 1 new untracked file + `.firecrawl/` (pre-existing untracked) |
| v5.3 deployment commits | `f84e53f7f1c5fa20fc8fc40e747bbf934cdfdf92` (wire) + `83ab6d8bc8a3f278d53c72516cf72d1a747e13bd` (audit-path fix) |
| Successful Actions run | `29154365778` (18s) |
| Source tag (untouched) | `v4.8-real-second-exhibition-repository-hardening` at `a70c8430` |
| Other tags / Releases | unchanged |

## Production status before push

| Probe | Expected | Observed |
|---|---|---|
| Root `https://conanxin.github.io/leonardo-chinese-exhibition/` | HTTP 200, 92,976 B, v2.9 = 1 | HTTP 200, 92,976 B, v2.9 = 1 ✅ |
| `/second-exhibition/` | HTTP 200 | HTTP 200 ✅ |
| `/second-exhibition/index.html` | HTTP 200 | HTTP 200 ✅ |
| Six image assets | HTTP 200 | HTTP 200 ✅ |
| Forbidden public paths (README.md, V4_ROADMAP, V5_ROADMAP, scripts/, _template/, _pilots/, second-exhibition/data/, second-exhibition/assets/{asset-checksums,asset-import-manifest,SOURCE_AUDIT,RIGHTS}) | HTTP 404 | HTTP 404 ✅ |
| Live page text on `/second-exhibition/` | still reflects v5.3 wording (`repository-only-not-deployed` × 3 occurrences) — no v5.3b push yet | confirmed ✅ |

## Stale visible strings corrected

12 hits in `second-exhibition/site/index.html` were split/replaced:

- meta description (line 6): `repository-only 页面 ... repository-only-not-deployed` → `当前发布状态：production-deployed-v5.3 · 公开 URL：...`
- kicker (line 15): `second-exhibition · v0.1 · repository-only` → `second-exhibition · v0.1 · production-deployed-v5.3`
- header `<span class="badge">` (line 19): `repository-only-not-deployed` → `production-deployed-v5.3`
- header status sentence (line 20): "v4.6 阶段产物，只用于 repository QA ... 未部署到 GitHub Pages" → "v5.3 controlled deployment 产物，通过 GitHub Pages 公开：[URL]。6 件资产的当前发布状态为 published-in-v5.3；历史导入记录 imported-not-deployed 保留在 ...asset-import-manifest.json 中，作为 v4.5 阶段的可审计证据"
- 6 × artifact-meta lines (lines 119, 132, 145, 158, 171, 184): `Status: imported-not-deployed` → `Import record: imported-not-deployed (v4.5) · Publication status: published-in-v5.3`
- footer badge (line 271): `repository-only-not-deployed` → `production-deployed-v5.3`
- footer status block (lines 273-275): rewritten to enumerate current status + public URL + asset publication status + preserved historical import record + workflow allowlist

## Historical import strings preserved

`imported-not-deployed` is preserved in **explicit "Import record" contexts only**:
- 6 × artifact-meta lines in index.html (each followed by `Publication status: published-in-v5.3`)
- 1 × header status sentence (explaining the v4.5 manifest is preserved as audit evidence)
- 1 × footer status sentence (explaining the v4.5 manifest is preserved as audit evidence)
- All 6 × `import_status: imported-not-deployed` per-asset entries in `second-exhibition/data/assets.json`
- `second-exhibition/assets/asset-import-manifest.json` (v4.5 immutable)
- All historical round reports / release notes / source-rights documents

## Status model

| Layer | Field | Value | Where |
|---|---|---|---|
| Historical import (per asset, immutable) | `import_status` | `imported-not-deployed` | `second-exhibition/assets/asset-import-manifest.json` (v4.5) + per-asset in `second-exhibition/data/assets.json` |
| Current publication (per asset) | `publication_status` | `published-in-v5.3` | per-asset in `second-exhibition/data/assets.json` |
| Current exhibition publication (top-level) | `status` / `publication_status` / `deployment_status` | `production-deployed-v5.3` | `second-exhibition/data/exhibition.json` |
| Public URL | `deployment_url` | `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` | `second-exhibition/data/exhibition.json` |
| Deployment round | `deployment_round` | `v5.3-controlled-deployment` | `second-exhibition/data/exhibition.json` |
| Build-time audit marker | (in `build-summary.json`) | `staging-only-not-deployed` | preserved as build-pipeline marker (not page text) |
| Dry-run-only audit marker | (in dry-run report) | `dry-run-only-not-deployed` | preserved as dry-run pipeline marker (not page text) |

## Exact files modified

12 tracked files + 1 new untracked file:

| File | Lines | Change |
|---|---|---|
| `README.md` | +29 / -0 | Added `## v5.3 Second Exhibition Controlled Deployment — Executed` and `## v5.3b Production State Reconciliation — Prepared` blocks (both before `## 当前版本`); preserved all historical sections verbatim |
| `docs/V5_ROADMAP.md` | +90 / -3 | Renamed v5.3 to "Controlled Deployment (executed)" with new "Actual outcome" sub-block; inserted full `## v5.3b — Production State Reconciliation (prepared, awaiting authorization)` section between v5.3 and v5.4 |
| `docs/SECOND_EXHIBITION_PRODUCTION_STATE_RECONCILIATION_v5.3b.md` | (new, untracked) | 15,765 bytes — full reconciliation spec / status layering / files-modified / files-preserved / validation / production state / working tree / rollback / authorization |
| `scripts/second_exhibition_build_gate.py` | +49 / -11 | JSON checks: require `production-deployed-v5.3` for `status`/`publication_status`/`deployment_status` + matching `deployment_url`; per-asset dual-status check (preserve `import_status`, add `publication_status`); page-text check requires current status + per-asset status + preserved historical record; forbids stale phrases |
| `scripts/second_exhibition_repository_qa.py` | +18 / -7 | Status field check requires `production-deployed-v5.3` for three fields; status-text check requires `production-deployed-v5.3` AND `published-in-v5.3` on page; explicit preservation check for `imported-not-deployed`; allowed-phrase list updated to recognize v5.3 sanctioned wording |
| `scripts/second_exhibition_staging_gate.py` | +21 / -4 | Group H rewritten: requires current status + per-asset status + preserved historical record + no stale phrasing |
| `scripts/second_exhibition_browser_qa.mjs` | +12 / -1 | Per-viewport `bodyText` and `repoStatusText` metrics; per-viewport checks require current status + per-asset status + preserved historical record + no stale prose; aggregation check uses `viewportMatrix` and requires all 5 viewports to see current status |
| `scripts/second_exhibition_deployment_dry_run.py` | +94 / -25 | Added `import re`; Section C rewritten to verify v5.3 workflow semantics (builder/gate with `--output`/`--audit`/`--artifact` to runner-temp, upload path to runner-temp, configure/upload/deploy ordering, no pre-v5.3 `path: site` line); rollback rehearsal references reverting `f84e53f` + `83ab6d8` to restore prior `pages.yml`; summary line updated to "v5.2+v5.3-aware deployment dry-run complete" |
| `second-exhibition/site/index.html` | +19 / -7 | 12 hit updates: meta description, kicker, header badge, header status sentence, 6 × artifact-meta (split into Import record + Publication status), footer badge, footer status block |
| `second-exhibition/site/README.md` | +12 / -7 | Header description + status block + forbidden-status list updated to v5.3 reality; new prohibitions added (preserve historical import record; don't skip staging builder/gate) |
| `second-exhibition/README.md` | +14 / -6 | Status section rewritten: production-deployed-v5.3 + immutable v4.5 import records + Pages workflow allowlist description |
| `second-exhibition/data/exhibition.json` | +9 / -3 | Added `publication_status`, `deployment_url`, `deployment_round`, `historical_import_round`; top-level `status` and `deployment_status` → `production-deployed-v5.3`; replaced `forbidden_statuses_not_used` overclaim list |
| `second-exhibition/data/assets.json` | +7 / -4 | Top-level `status` → `production-deployed-v5.3`, added `publication_status: published-in-v5.3`; each of 6 assets gained `publication_status: published-in-v5.3` while `import_status: imported-not-deployed` preserved verbatim |

**Total:** 12 modified files (366 insertions, 83 deletions across all) + 1 new untracked file (15,765 bytes).

## Gate results (all PASS)

| Gate | Result |
|---|---|
| `python3 scripts/template_quality_gate.py` | PASS 37/37 |
| `python3 scripts/second_exhibition_build_gate.py` | PASS |
| `python3 scripts/second_exhibition_repository_qa.py` | PASS 164/164 |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | 6/6 OK |
| `node --check second-exhibition/site/script.js` | clean |
| `node --check scripts/second_exhibition_browser_qa.mjs` | clean |

## Staging result

```
PASS: staging build complete
  output: /tmp/leonardo-pages-artifact
  audit : /tmp/leonardo-pages-artifact-audit
  root site files     : 25
  second-exhibition   : 9
  path rewrite count  : 6
  deployment_status   : staging-only-not-deployed

PASS: staging gate — 25 main-site + 9 second-exhibition files verified
  OK: staged second-exhibition index.html carries production-deployed-v5.3 + published-in-v5.3 + preserved imported-not-deployed
```

| Metric | Value |
|---|---|
| Root index byte | 92,976 |
| Total public files | 34 (25 main + 9 second-exhibition) |
| v2.9 marker | 1 |
| Six image SHA-256 | 6/6 OK |
| Forbidden leakage | 0 |
| Staged page text | 5× `production-deployed-v5.3` + 8× `published-in-v5.3` + 8× `imported-not-deployed` (in Import record context) |

## Deployment dry-run result

```
PASS: v5.2+v5.3-aware deployment dry-run complete
  artifact  -> base path /leonardo-chinese-exhibition
  allowlist probes : 14/14
  forbidden probes : 16/16
  roundtrip files  : 34 byte-identical
  tar size         : 5802945 bytes
  deployment_status: dry-run-only-not-deployed
  report           : /tmp/leonardo-pages-dry-run/report.json
```

| Section | Result |
|---|---|
| Pre-flight | OK (artifact + audit exist, both outside repo, dry-run + roundtrip dirs cleaned) |
| A. Base-path HTTP probe (base=`/leonardo-chinese-exhibition/`) | 14/14 allowlist 200; 16/16 forbidden 404; out-of-base 404; root byte 92,976; v2.9 marker 1; second-exhibition title present; zero `../assets/` references; 6 images via `./assets/` |
| B. Artifact pack + roundtrip | 34/34 byte-identical; roundtrip root index byte 92,976 |
| C. Rollback rehearsal (v5.3-aware) | workflow invokes staging builder with `--output` and `--audit` at runner-temp; workflow invokes staging gate with `--artifact` and `--audit` at runner-temp; `upload-pages-artifact` path = `${{ runner.temp }}/leonardo-pages-artifact`; step order correct (checkout → builder → gate → configure-pages → upload → deploy); no pre-v5.3 `path: site` line; rollback rehearsal documented (revert `f84e53f` + `83ab6d8` restores pre-v5.3; revert v5.3b restores v5.3 wording); workflow NOT modified |
| Exit code | 0 |

## Browser QA matrix result

| Viewport | Status | Sections | Cards | Images loaded | Body overflow | Current status visible |
|---|---|---|---|---|---|---|
| 1440×1000 | PASS | 4 | 6 | 6 | none | yes |
| 1280×900 | PASS | 4 | 6 | 6 | none | yes |
| 768×1024 | PASS | 4 | 6 | 6 | none | yes |
| 390×844 | PASS | 4 | 6 | 6 | none | yes |
| 320×700 | PASS | 4 | 6 | 6 | none | yes |

**5/5 viewports PASS**, exit 0.

| Interaction | Result |
|---|---|
| guidedToggle | true |
| lightboxOpen | true |
| lightbox accessible name | lightbox-title |
| close button focus | true |
| ESC close | true |
| focus return | true |
| C-06 lightbox open (should be false) | false ✅ |
| section nav | true |
| tab focus | true |

| a11y | Result |
|---|---|
| h1Count | 1 |
| imgMissingAlt | 0 |
| buttonMissingName | 0 |
| headingJump | none |
| lightbox title hidden | none |

| Error metrics | Count |
|---|---|
| console errors | 0 |
| page errors | 0 |
| failed requests | 0 |
| external requests | 0 |

| No-JS / reduced-motion | Result |
|---|---|
| no-JS body text | PASS |
| no-JS card count | ≥ 6 |
| no-JS repo status | visible |
| reduced motion lightbox open | PASS |
| reduced motion ESC close | PASS |

## Assets / checksums unchanged

| Check | Result |
|---|---|
| `git diff -- second-exhibition/assets/images/` | CLEAN |
| `git diff -- second-exhibition/assets/asset-import-manifest.json` | CLEAN |
| `git diff -- second-exhibition/assets/asset-checksums.sha256` | CLEAN |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | 6/6 OK |
| Live vs source image SHA-256 (round 1 of dry-run) | not re-verified in this round; staging builder/gate verified SHA identity between source and staged |

## Source / rights evidence unchanged

| Check | Result |
|---|---|
| `git diff -- second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` | CLEAN |
| `git diff -- second-exhibition/docs/RIGHTS_AND_SOURCES.md` | CLEAN |

## Workflow unchanged

| Check | Result |
|---|---|
| `git diff -- .github/workflows/` | CLEAN |
| Live Pages workflow | unchanged (v5.3 wiring in place) |
| Workflow NOT modified by dry-run | confirmed |

## Tags / Releases unchanged

| Tag | Status |
|---|---|
| `v4.8-real-second-exhibition-repository-hardening` at `a70c8430` | unchanged |
| `v4.7-real-second-exhibition-repository-qa` at `2153d2e` | unchanged |
| All other tags | unchanged |
| All Releases | unchanged |

## Working tree state

| Field | Value |
|---|---|
| `git status -sb` | 12 modified + 1 untracked (`docs/SECOND_EXHIBITION_PRODUCTION_STATE_RECONCILIATION_v5.3b.md`) + pre-existing `.firecrawl/` |
| `git diff --check` | clean (exit 0) |
| `git diff --stat` | 12 files changed, 366 insertions(+), 83 deletions(-) |
| `git diff --name-status` | 12 × `M` (modified) + 1 × `??` (untracked) |
| `git reflog` | unchanged at HEAD `83ab6d8` (no new commits) |
| No `git add` | confirmed |
| No `git commit` | confirmed |
| No `git push` | confirmed |
| No GitHub Actions triggered | confirmed |
| No real Pages deploy | confirmed |
| No tag / Release created | confirmed |
| Production | unchanged at root 92,976 B / v2.9 = 1 / `/second-exhibition/` 200 (with v5.3 wording) / 6 images 200 / forbidden paths 404 |

## Rollback method

If v5.3b push is followed by a production regression, rollback is by a single `git revert` of the v5.3b commit (not yet created):

```
git revert <v5.3b-commit-sha>
git push origin main
```

After revert, all v5.3b-modified files are restored to v5.3 deployed state (`83ab6d8`); v5.3 Pages workflow remains intact; the live page reverts to v5.3 wording. No tag, Release, or v4.5 evidence file is touched by the revert.

If a deeper rollback to pre-v5.3 is needed (revert all of v5.3 + v5.3b), the procedure is `git revert <v5.3b-commit> 83ab6d8 f84e53f` (in reverse chronological order), restoring the pre-v5.3 workflow that only deploys `site/`.

## Required authorization

```
DEPLOY v5.3b
```

Only after receiving this exact string will commit + push + Pages deploy be executed.