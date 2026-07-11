# v5.3b Second Exhibition Production State Reconciliation

> Companion to `docs/SECOND_EXHIBITION_DEPLOYMENT_CHECKLIST_v5.0.md`, `docs/SECOND_EXHIBITION_ROLLBACK_PLAN_v5.0.md`, `docs/V5_ROADMAP.md`, and `reports/leonardo_chinese_exhibition_v5_3b_production_state_reconciliation_prep_report.md`.

## Baseline

| Field | Value |
|---|---|
| HEAD / origin/main | `83ab6d8bc8a3f278d53c72516cf72d1a747e13bd` |
| v5.3 deployment commits | `f84e53f7f1c5fa20fc8fc40e747bbf934cdfdf92` (wire workflow), `83ab6d8bc8a3f278d53c72516cf72d1a747e13bd` (audit-path fix) |
| Successful Actions run | `29154365778` (18s, all 9 steps green) |
| Public URL | https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/ |
| Root production byte | 92,976 B |
| Root v2.9 marker | 1 |
| Six public images | HTTP 200, byte-identical to `second-exhibition/assets/asset-checksums.sha256` |
| Forbidden public paths | HTTP 404 |

## Problem

After v5.3 controlled deployment, the public page at `/second-exhibition/` was live and serving all assets, but the visible status text and per-asset meta still reflected the v4.6 repository-only source content:

- Header badge: `repository-only-not-deployed`
- Header sentence: "本展览未部署到 GitHub Pages"
- 6 artifact-meta lines: `Status: imported-not-deployed` (with no current publication status)
- Footer badge: `repository-only-not-deployed`
- Footer sentence: "资产状态：imported-not-deployed × 6 · 部署状态：not deployed"
- Top-level `exhibition.json` and `assets.json` `status: repository-only-not-deployed`
- `exhibition.json` `forbidden_statuses_not_used` list included `deployed` and `live` (now legitimate publication-status terms)

This is a **factual status mismatch between the visible page and the actual deployed state**, not a deployment failure. The deploy itself was correct; the wording authored in v4.6 was no longer accurate. Fixing this without rewriting historical v4.5 import evidence is the goal of v5.3b.

## Status layering

The fix introduces an explicit separation between **historical import status** (immutable v4.5 evidence) and **current publication status** (current public-facing state):

| Layer | Field | Value | Where it lives |
|---|---|---|---|
| Historical import (per asset, immutable) | `import_status` | `imported-not-deployed` | `second-exhibition/assets/asset-import-manifest.json` (v4.5) and `second-exhibition/data/assets.json` per-asset |
| Current publication (per asset) | `publication_status` | `published-in-v5.3` | `second-exhibition/data/assets.json` per-asset |
| Current exhibition publication (top-level) | `status` / `publication_status` / `deployment_status` | `production-deployed-v5.3` | `second-exhibition/data/exhibition.json` |
| Public URL | `deployment_url` | `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` | `second-exhibition/data/exhibition.json` |
| Deployment round | `deployment_round` | `v5.3-controlled-deployment` | `second-exhibition/data/exhibition.json` |
| Build-time audit marker | (in `build-summary.json`) | `staging-only-not-deployed` | preserved as build-pipeline marker, not page text |
| Dry-run-only audit marker | (in dry-run report) | `dry-run-only-not-deployed` | preserved as dry-run pipeline marker, not page text |

The page-visible wording now distinguishes these:

- **Current badge / kicker / footer**: `production-deployed-v5.3`
- **Per-asset artifact-meta**: `Import record: imported-not-deployed (v4.5) · Publication status: published-in-v5.3`
- **Footer status sentence**: explains that current status is `production-deployed-v5.3`, asset status is `published-in-v5.3`, and historical import record `imported-not-deployed` remains in `second-exhibition/assets/asset-import-manifest.json` as v4.5 evidence

The `imported-not-deployed` phrase still appears on the page — but only inside the explicit "Import record: imported-not-deployed (v4.5)" annotation, never as a current-status claim.

## Files modified

### Page content

- **`second-exhibition/site/index.html`** — meta description rewritten to declare current status + public URL; kicker updated to `production-deployed-v5.3`; header `<span class="badge">` updated; header `<p class="repository-status">` sentence rewritten to describe v5.3 deployment + public URL + asset publication status + preserved historical import record; 6 artifact-meta lines (one per candidate C-01 / C-03 / C-06 / C-08 / C-09 / C-10) updated to split the historical `Status: imported-not-deployed` into `Import record: imported-not-deployed (v4.5) · Publication status: published-in-v5.3`; footer badge updated to `production-deployed-v5.3`; footer status sentence rewritten to enumerate current status + public URL + asset status + preserved historical record; footer caveat sentence rewritten to describe the v5.3 Pages workflow allowlist (instead of "not coupled to workflow").

### Data files

- **`second-exhibition/data/exhibition.json`** — top-level `status: production-deployed-v5.3`, `deployment_status: production-deployed-v5.3`; added `publication_status: production-deployed-v5.3`, `deployment_url: https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`, `deployment_round: v5.3-controlled-deployment`, `historical_import_round: v4.5-asset-import`; `serving_contract` rationale extended to mention v5.3 production deployment uses GitHub Pages project-site base path; `forbidden_statuses_not_used` list updated (removed `deployed` and `live` which are now legitimate publication-status terms; replaced with overclaim guards like `watermark-free originals`).
- **`second-exhibition/data/assets.json`** — top-level `status: production-deployed-v5.3`, added `publication_status: published-in-v5.3`; manifest_source comment extended to note v4.5 historical import_status records are preserved; each of 6 assets gained `publication_status: published-in-v5.3` while `import_status: imported-not-deployed` preserved verbatim.

### Per-directory documentation

- **`second-exhibition/site/README.md`** — header description updated to declare v5.3 deployment + public URL; per-file list updated to enumerate new dual status (current + historical); `## 状态与版本` block replaced with current status / publication_status / historical_import_status + three gate references (asset / build / staging) all PASS; `## 不允许` block updated: removed `deployed` / `live` from overclaim list, added `watermark-free originals`; added two new prohibitions: do not erase `imported-not-deployed` or `import_status`, and do not skip staging builder/gate.
- **`second-exhibition/README.md`** — top-level status bullets replaced with current v5.3 state; main paragraph rewritten to describe v5.3 public subtree + internal-only artefacts; asset-inventory paragraph notes the manifest is immutable v4.5 record; source-and-rights paragraph notes those two files are immutable historical evidence and excluded from Pages upload; deployment-safety paragraph describes the v5.3 Pages workflow allowlist.

### Gates

- **`scripts/second_exhibition_build_gate.py`** — exhibition JSON check now requires `status == production-deployed-v5.3` AND `publication_status == production-deployed-v5.3` AND `deployment_status == production-deployed-v5.3` AND `deployment_url == "https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/"`. Assets JSON check now requires top-level `status == production-deployed-v5.3` AND top-level `publication_status == published-in-v5.3`; for each of 6 assets, `import_status == imported-not-deployed` (preserved) AND `publication_status == published-in-v5.3` (new). Page-text check now requires the page to contain `production-deployed-v5.3` AND `published-in-v5.3`; explicit preservation check requires `imported-not-deployed` to remain; explicit forbiddance of stale phrases (`repository-only-not-deployed</span>`, `<span class="badge">not deployed`, `本展览未部署到 GitHub Pages`, `Status: repository-only`, `Status: not deployed`).
- **`scripts/second_exhibition_repository_qa.py`** — exhibition field check now requires `status == production-deployed-v5.3` AND `publication_status == production-deployed-v5.3` AND `deployment_status == production-deployed-v5.3`. Status-text check on the page now requires `production-deployed-v5.3` AND `published-in-v5.3`; explicit preservation check requires `imported-not-deployed` to remain.
- **`scripts/second_exhibition_staging_gate.py`** — Group H rewritten: requires the staged page to contain `production-deployed-v5.3` AND `published-in-v5.3` AND `imported-not-deployed` (preserved) AND forbids stale phrases (`repository-only-not-deployed</span>`, `<span class="badge">not deployed`, `本展览未部署到 GitHub Pages`).
- **`scripts/second_exhibition_browser_qa.mjs`** — per-viewport metrics now include `repoStatusText` and `bodyText`; per-viewport checks now require `production-deployed-v5.3` AND `published-in-v5.3` in body text, plus preservation of `imported-not-deployed`, plus non-occurrence of `本展览未部署到 GitHub Pages`; aggregation check requires all 5 viewports to see the current status.

### Deployment dry-run

- **`scripts/second_exhibition_deployment_dry_run.py`** — Section C rewritten to verify v5.3 workflow semantics: the workflow must contain a `Build combined staging artifact` step that invokes `scripts/second_exhibition_staging_build.py` with `--output "${{ runner.temp }}/leonardo-pages-artifact"` AND `--audit "${{ runner.temp }}/leonardo-pages-artifact-audit"`; the workflow must contain a `Run staging gate` step that invokes `scripts/second_exhibition_staging_gate.py` with `--artifact "${{ runner.temp }}/leonardo-pages-artifact"` AND `--audit "${{ runner.temp }}/leonardo-pages-artifact-audit"`; the workflow's `upload-pages-artifact` step must have `path: ${{ runner.temp }}/leonardo-pages-artifact`; the workflow must contain `configure-pages`, `deploy-pages`, and the page-yaml ordering must be `checkout → builder → gate → configure-pages → upload → deploy`; rollback rehearsal now references reverting `f84e53f` + `83ab6d8` to restore the prior `pages.yml`; the script no longer fails on the obsolete `path: site` line. The script does NOT modify the workflow and does NOT execute a revert.

### Top-level documentation

- **`README.md`** — added `## v5.3 Second Exhibition Controlled Deployment — Executed` block (recording commits `f84e53f` + `83ab6d8`, Actions run `29154365778`, public URL, root byte, v2.9 marker, six images, forbidden paths, workflow changes, tags unchanged) and `## v5.3b Production State Reconciliation — Prepared` block (recording baseline HEAD, current exhibition publication status, current per-asset publication status, preserved historical import status, root byte unchanged, six public images unchanged, v4.5 immutable evidence untouched, workflow untouched, working tree state, no commit / push / Actions triggered, required authorization `DEPLOY v5.3b`). All historical v3.x / v4.x / v5.0–v5.2 sections preserved verbatim.
- **`docs/V5_ROADMAP.md`** — added `## v5.3b — Production State Reconciliation (prepared, awaiting authorization)` section between v5.3 and v5.4, with full status-layering table, files-modified list, files-preserved list, validation gates, prohibitions, exit criteria, and required authorization. The existing v5.3 section title is updated to "Controlled Deployment (executed)" with a new "Actual outcome" sub-block recording the two commits and Actions run `29154365778`.

## Files preserved

The following files were deliberately **not touched** in v5.3b prep:

- `second-exhibition/assets/asset-import-manifest.json` — historical v4.5 import manifest; immutable
- `second-exhibition/assets/asset-checksums.sha256` — image checksum file; immutable
- All 6 image bytes under `second-exhibition/assets/images/` — `sha256sum -c` 6/6 OK
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` — v4.5 source audit; immutable
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md` — v4.5 rights evidence; immutable
- All `release-assets/` content (historical round manifests)
- All `reports/` content (historical round reports)
- All `docs/RELEASE_NOTES_*` (historical release notes)
- All `_template/`, `_pilots/`, `posts/`, `case-study/` content
- Top-level `site/index.html`, `site/script.js`, `site/style.css` — root production byte 92,976 B / v2.9 = 1 preserved
- `.github/workflows/pages.yml` — v5.3 wiring already in place; v5.3b does not modify it again
- All `tags/` and `Release/` content — untouched; `v4.8-real-second-exhibition-repository-hardening` tag remains the most recent source freeze anchor

## Validation (all PASS in this prep round, no real push yet)

| Check | Result |
|---|---|
| `python3 scripts/template_quality_gate.py` | PASS 37/37 |
| `python3 scripts/second_exhibition_build_gate.py` | PASS |
| `python3 scripts/second_exhibition_repository_qa.py` | PASS 164/164 |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | 6/6 OK |
| `node --check second-exhibition/site/script.js` | clean |
| `node --check scripts/second_exhibition_browser_qa.mjs` | clean |
| Staging build | PASS (root 92,976 B, 34 public files, 25 main + 9 second-exhibition, 6 image SHA identical, 0 forbidden leakage) |
| Staging gate | PASS (Group H now requires `production-deployed-v5.3` + `published-in-v5.3` + preserved `imported-not-deployed`) |
| Deployment dry-run (v5.3-aware) | PASS exit 0 (Section A 14/14 allowlist 200, 16/16 forbidden 404; Section B 34/34 roundtrip byte-identical; Section C v5.3 workflow semantics verified; rollback rehearsal references reverting `f84e53f` + `83ab6d8`) |
| Browser QA 5/5 viewports | PASS (current status visible in all 5 viewports, no stale phrasing, 0 console/page/failed/external, 6 images per viewport, all interactions OK) |

## Production state before push

| Probe | Expected (unchanged) | Observed |
|---|---|---|
| Root `https://conanxin.github.io/leonardo-chinese-exhibition/` | HTTP 200 | HTTP 200 |
| Root byte | 92,976 | 92,976 |
| Root v2.9 marker | 1 | 1 |
| `/second-exhibition/` | HTTP 200 | HTTP 200 |
| Six image assets | HTTP 200 | HTTP 200 |
| Forbidden public paths | HTTP 404 | HTTP 404 |
| Page text on `/second-exhibition/` | still reflects v5.3b-prep-OLD wording (no push yet) | confirmed: `repository-only-not-deployed` badge, `imported-not-deployed` artifact-meta, etc. |

## Working tree state

| Field | Value |
|---|---|
| `git status -sb` | 11 modified files + 1 untracked (`.firecrawl/`) |
| `git diff --check` | clean |
| `git reflog` | unchanged at HEAD `83ab6d8` (no new commits this round) |
| No `git add` | confirmed |
| No `git commit` | confirmed |
| No `git push` | confirmed |
| No GitHub Actions triggered | confirmed |
| No real Pages deploy | confirmed |
| No tag / Release created | confirmed |
| Production | unchanged |

## Rollback method

If v5.3b push is followed by a production regression, rollback is by a single `git revert` of the v5.3b commit (not yet created):

```
git revert <v5.3b-commit-sha>
git push origin main
```

After revert, the v5.3b-modified files are restored to the v5.3 deployed state (commit `83ab6d8`); v5.3's Pages workflow remains intact; the live page reverts to the v5.3 text. No tag, Release, or v4.5 evidence file is touched by the revert.

If a deeper rollback to pre-v5.3 is needed (revert all of v5.3), the procedure is `git revert 83ab6d8 f84e53f`, restoring the pre-v5.3 workflow that only deploys `site/`. v5.3b commit (if already pushed) must be reverted first; then v5.3 commits in reverse order.

## Required authorization

```
DEPLOY v5.3b
```

Only after receiving this exact string will commit + push + Pages deploy be executed.