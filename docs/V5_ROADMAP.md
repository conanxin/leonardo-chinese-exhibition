# V5 Roadmap — Second Exhibition Deployment

> Scope of this document: deployment of the second exhibition to GitHub Pages. Companion to `docs/SECOND_EXHIBITION_DEPLOYMENT_OPTIONS_v5.0.md`, `docs/SECOND_EXHIBITION_DEPLOYMENT_ARCHITECTURE_v5.0.md`, `docs/SECOND_EXHIBITION_URL_AND_PATH_PLAN_v5.0.md`, `docs/SECOND_EXHIBITION_DEPLOYMENT_RISK_REGISTER_v5.0.md`, `docs/SECOND_EXHIBITION_ROLLBACK_PLAN_v5.0.md`, and `docs/SECOND_EXHIBITION_DEPLOYMENT_CHECKLIST_v5.0.md`.

---

## v5.0 — Second Exhibition Deployment Planning (this round)

**Goal.** Compare deployment options; select the architecture; define the URL / path plan; define the risk register; define the rollback plan; define the deployment checklist; add a deployment preflight script.

**Deliverables.**

- `docs/SECOND_EXHIBITION_DEPLOYMENT_OPTIONS_v5.0.md` — options A / B / C compared
- `docs/SECOND_EXHIBITION_DEPLOYMENT_ARCHITECTURE_v5.0.md` — selected architecture and artifact layout
- `docs/SECOND_EXHIBITION_URL_AND_PATH_PLAN_v5.0.md` — canonical public URL and allowed / forbidden paths
- `docs/SECOND_EXHIBITION_DEPLOYMENT_RISK_REGISTER_v5.0.md` — 15 named risks with mitigation / rollback
- `docs/SECOND_EXHIBITION_ROLLBACK_PLAN_v5.0.md` — rollback baseline, triggers, method, verification
- `docs/SECOND_EXHIBITION_DEPLOYMENT_CHECKLIST_v5.0.md` — five phases, exit gates
- `scripts/second_exhibition_deployment_preflight.py` — pre-deploy gate
- `docs/V5_ROADMAP.md` — this file
- `README.md` — updated with v5.0 block
- `reports/leonardo_chinese_exhibition_v5_0_second_exhibition_deployment_planning_report.md`

**Do NOT do in v5.0.**

- Do not deploy the second exhibition.
- Do not modify the Pages workflow.
- Do not create a CNAME.
- Do not create a second Pages workflow.
- Do not upload the repository root.
- Do not modify tracked `second-exhibition/site/`, `second-exhibition/data/`, `second-exhibition/assets/`, or source / rights evidence files.
- Do not create a tag or GitHub Release.
- Do not process the untracked `.firecrawl/` directory.

**Exit criteria for v5.0.**

- All 6 v5.0 docs committed.
- `scripts/second_exhibition_deployment_preflight.py` committed; preflight **PASS**.
- `python3 scripts/template_quality_gate.py` → **PASS, 37/37**.
- `python3 scripts/second_exhibition_build_gate.py` → **PASS**.
- `python3 scripts/second_exhibition_repository_qa.py` → **161 PASS / 0 FAIL / 0 WARNINGS** (exit 0).
- `node scripts/second_exhibition_browser_qa.mjs` → **PASS** (5/5 viewports, 0 external requests).
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256` → **6/6 OK**.
- `git diff` against `site/`, `second-exhibition/site/`, `second-exhibition/data/`, `second-exhibition/assets/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `.github/workflows/`, `scripts/template_quality_gate.py`, `scripts/second_exhibition_asset_gate.py`, `scripts/second_exhibition_build_gate.py`, `scripts/second_exhibition_repository_qa.py`, `scripts/second_exhibition_browser_qa.mjs` is **empty**.
- Live byte still **92,976 B**.
- v2.9 marker still **1**.
- All `second-exhibition/` Pages URLs still HTTP 404.
- Existing tags (`v2.0` through `v4.8`) and Releases untouched.

---

## v5.1 — Staging Artifact Build

**Goal.** Build a temporary staging artifact from `site/` + `second-exhibition/site/` (path-rewritten) + `second-exhibition/assets/images/`. Do **not** deploy. Run the existing browser QA against the staging tree.

**Tasks.**

- Create the staging directory outside the repository (e.g., `/tmp/leonardo-pages-artifact/`).
- Copy `site/` to the staging root.
- Copy `second-exhibition/site/` to `staging/second-exhibition/`, applying the path rewrite (`../assets/images/` → `./assets/images/`) to the staging copy of `index.html` only.
- Copy the 6 raster images under `staging/second-exhibition/assets/images/`.
- Generate the file inventory and the SHA-256 hash inventory. Save them outside the repo.
- Run `python3 scripts/second_exhibition_deployment_preflight.py` against the staging tree (or against the source tree as a regression test).
- Serve the staging tree locally with `python3 -m http.server <port> --directory /tmp/leonardo-pages-artifact`.
- Run `node scripts/second_exhibition_browser_qa.mjs` against both `/` and `/second-exhibition/` of the staging server.

**Do NOT do in v5.1.**

- Do not modify the Pages workflow.
- Do not push to `main` from this round's working tree.
- Do not commit the staging tree.
- Do not create a tag or Release.

**Exit criteria for v5.1.**

- Staging artifact has exactly the allowlisted files.
- Hash inventory matches `second-exhibition/assets/asset-checksums.sha256`.
- Browser QA PASS on both `/` and `/second-exhibition/`.
- No external requests.
- No High / Blocked risks open.

**v5.1 actual result — PASS** (commit SHA to be filled by round run)

- Staging artifact assembled at `/tmp/leonardo-pages-artifact` (outside repo).
- Audit summary at `/tmp/leonardo-pages-artifact-audit/` (outside repo, sibling dir).
- Main site: 25 files copied byte-identical (SHA verified); staging `index.html` = 92,976 B; v2.9 marker = 1.
- Second exhibition subtree: exactly 9 public files (3 site files + 6 raster images), allowlist extensions only.
- Path rewrite: 6 `../assets/images/` → `./assets/images/` in staged `index.html` only. Source `second-exhibition/site/index.html` SHA unchanged.
- Forbidden exposure: none (no `data/`, `docs/`, manifest, checksums, MD/JSON/SHA256 files, `_template/`, `_pilots/`, `reports/`, `scripts/`).
- Staging gate `python3 scripts/second_exhibition_staging_gate.py` → **PASS, exit 0** (8 sections A–H all green).
- Local HTTP QA: root 200 / 92,976 B / v2.9 marker 1; `/second-exhibition/` 200 / title present; 6 images 200; all internal paths 404.
- Browser QA `SECOND_EXHIBITION_QA_URL=http://127.0.0.1:8771/second-exhibition/ node scripts/second_exhibition_browser_qa.mjs` → **PASS, 5/5 viewports**, 0 console/page/failed/external requests, 0 overflow, 6 images loaded per viewport.
- Production Pages untouched: live byte still 92,976 B, v2.9 marker still 1, all `/second-exhibition/` Pages paths still 404.
- Workflow unchanged: still `path: site` (top-level only).
- Tags / Releases unchanged.
- Next: **v5.2 deployment dry run**.

---

## v5.2 — Deployment Dry Run

**Goal.** Inspect what a deployment would do, without actually publishing.

**Tasks.**

- Re-read `.github/workflows/pages.yml`. Plan the one-line change that will switch the artifact source from `site` to the staging directory.
- Confirm that the workflow change is local and reviewable.
- Confirm the rollback path (one revert commit).

**Do NOT do in v5.2.**

- Do not push to `main`.
- Do not create a tag or Release.

**Exit criteria for v5.2.**

- A documented one-line workflow change proposal exists in `reports/`.
- Rollback plan is confirmed against the proposed change.

**v5.2 actual result — PASS** (commit SHA to be filled by round run)

- Project-site base path verified: `/leonardo-chinese-exhibition/`.
- Base-path HTTP probe: **14/14 allowlist URLs returned 200** (root 92,976 B, v2.9 marker 1, second-exhibition 24,380 B with title, all 6 images with correct byte counts).
- Base-path HTTP probe: **16/16 forbidden paths returned 404** (data/, docs/, manifest, checksums, _template/, _pilots/, reports/, scripts/, .firecrawl/, README.md, V4/V5_ROADMAP.md).
- Out-of-base sanity probe `/some-other-base/second-exhibition/` → 404.
- Artifact pack: 34 files → `/tmp/leonardo-pages-artifact.tar.gz` (5,802,670 bytes); unpack → `/tmp/leonardo-pages-roundtrip`; **all 34 files SHA-identical**.
- Rollback rehearsal: workflow `path: site` appears exactly once; proposed change is 1 line (`path: site` → `path: __STAGING_ARTIFACT_DIR__`); revert is 1 line; workflow NOT modified.
- Base-path browser QA: 5/5 viewports PASS, 0 console/page/failed/external errors, 6 images loaded per viewport, all interactions and a11y OK.
- Production Pages untouched: live byte still 92,976 B, v2.9 marker still 1, all `/second-exhibition/` Pages paths still 404.
- Workflow unchanged.
- Tags / Releases unchanged.
- Next: **v5.3 controlled deployment**.

---

## v5.3 — Controlled Deployment (executed)

**Goal.** Publish the second exhibition to Pages. Verify the existing top-level site remains intact. Verify the new route.

**Tasks.**

- Push the workflow change to `main`.
- Wait for GitHub Actions success.
- Probe `https://conanxin.github.io/leonardo-chinese-exhibition/` — must remain at 92,976 B.
- Probe `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` — must be HTTP 200.
- Run `node scripts/second_exhibition_browser_qa.mjs` against the public URL.
- Re-verify all source / rights pages.

**Do NOT do in v5.3.**

- Do not create a tag or Release yet (those are v5.4).

**Exit criteria for v5.3.**

- Live byte unchanged at 92,976 B.
- v2.9 marker still 1.
- `/second-exhibition/` returns 200.
- All 6 image URLs return 200.
- Forbidden paths under `/second-exhibition/` return 404.
- Browser QA against the public URL PASS.
- External requests = 0.
- Source / rights recheck: no changes.

**Actual outcome (commits on `main`).**

- `f84e53f` — wire staging builder + gate + upload path `${{ runner.temp }}/leonardo-pages-artifact`
- `83ab6d8` — pass `--audit "${{ runner.temp }}/leonardo-pages-artifact-audit"` to the builder (fix mismatch that aborted first run 29154310813)
- GitHub Actions run `29154365778` succeeded in 18s.
- Live root 92,976 B / v2.9 = 1 unchanged; `/second-exhibition/` and all 6 images return HTTP 200; all forbidden paths 404.

---

## v5.3b — Production State Reconciliation (prepared, awaiting authorization)

**Goal.** Reconcile visible on-page wording with the new production state established by v5.3, without rewriting historical v4.5 import evidence. Page-level status text and current publication metadata must reflect the v5.3 reality; immutable v4.5 import records remain in place.

**Problem observed after v5.3 deploy.**

- The deployed page still displayed `repository-only-not-deployed` and the asset cards exposed only `imported-not-deployed` (historical import status). This is a factual status mismatch between the visible page and the actual deployed state — not a deployment failure.

**Status layering (introduced in v5.3b).**

| Layer | Field | Value | Source |
|---|---|---|---|
| Historical import (per asset, immutable) | `import_status` | `imported-not-deployed` | `second-exhibition/assets/asset-import-manifest.json` (v4.5) |
| Current publication (per asset) | `publication_status` | `published-in-v5.3` | added to `second-exhibition/data/assets.json` |
| Current exhibition publication (top-level) | `status` / `publication_status` / `deployment_status` | `production-deployed-v5.3` | `second-exhibition/data/exhibition.json` |
| Public URL | `deployment_url` | `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` | `second-exhibition/data/exhibition.json` |
| Deployment round | `deployment_round` | `v5.3-controlled-deployment` | `second-exhibition/data/exhibition.json` |
| Build-time audit marker | (in `build-summary.json`) | `staging-only-not-deployed` | preserved as build-pipeline marker, not page text |

**Files modified in v5.3b prep.**

- `second-exhibition/site/index.html` — meta description, kicker, header badge + sentence, 6× artifact-meta lines (split `Status: imported-not-deployed` into `Import record: imported-not-deployed (v4.5) · Publication status: published-in-v5.3`), footer badge + status block.
- `second-exhibition/data/exhibition.json` — top-level `status` / `deployment_status` → `production-deployed-v5.3`; added `publication_status`, `deployment_url`, `deployment_round`, `historical_import_round`; replaced `forbidden_statuses_not_used` overclaim list.
- `second-exhibition/data/assets.json` — top-level `status` → `production-deployed-v5.3`, added `publication_status: published-in-v5.3`; each of 6 assets gained `publication_status: published-in-v5.3` while `import_status: imported-not-deployed` preserved.
- `second-exhibition/site/README.md` — header description + status block + forbidden-status list updated to v5.3 reality.
- `second-exhibition/README.md` — status section rewritten; deployment-safety section describes the v5.3 Pages workflow allowlist.
- `scripts/second_exhibition_build_gate.py` — JSON checks require `production-deployed-v5.3` for `status` / `publication_status` / `deployment_status` + matching `deployment_url`; per-asset dual-status check (preserve `import_status`, add `publication_status`); page-text check requires current status + per-asset status + preserved historical record; forbids stale badge/prose.
- `scripts/second_exhibition_repository_qa.py` — status field check now requires `production-deployed-v5.3`; status-text check requires `production-deployed-v5.3` AND `published-in-v5.3` on page; explicit preservation check for `imported-not-deployed`.
- `scripts/second_exhibition_staging_gate.py` — Group H rewritten: requires current status + per-asset status + preserved historical record + no stale phrasing.
- `scripts/second_exhibition_browser_qa.mjs` — per-viewport page-text check requires `production-deployed-v5.3` + `published-in-v5.3` + preserved `imported-not-deployed` + no stale prose; aggregation requires all 5 viewports to see current status.
- `scripts/second_exhibition_deployment_dry_run.py` — Section C updated to verify v5.3 workflow semantics (`${{ runner.temp }}/leonardo-pages-artifact` upload path + matching `--audit` flag), instead of the obsolete `path: site` check. Rollback rehearsal now references reverting `f84e53f` + `83ab6d8` to restore prior `pages.yml`.
- `README.md` — added v5.3 (executed) and v5.3b (prepared) blocks; preserved all historical v3.x / v4.x / v5.0–v5.2 sections.
- `docs/V5_ROADMAP.md` — added this v5.3b section.

**Files preserved (v4.5 immutable evidence).**

- `second-exhibition/assets/asset-import-manifest.json` (historical import record, untouched)
- `second-exhibition/assets/asset-checksums.sha256` (untouched)
- All six image bytes under `second-exhibition/assets/images/` (untouched; `sha256sum -c` 6/6 OK)
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` (untouched)
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md` (untouched)
- All `release-assets/`, `reports/`, `docs/RELEASE_NOTES_*`, `_template/`, `_pilots/`, `posts/`, `case-study/` content (untouched)
- `site/index.html`, `site/script.js`, `site/style.css` (untouched; root byte 92,976 B preserved)
- `.github/workflows/pages.yml` (untouched in v5.3b prep; v5.3 wiring already in place)

**Validation gates (all PASS before push).**

- `python3 scripts/template_quality_gate.py` → PASS 37/37
- `python3 scripts/second_exhibition_build_gate.py` → PASS
- `python3 scripts/second_exhibition_repository_qa.py` → PASS 164/164
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256` → 6/6 OK
- `node --check second-exhibition/site/script.js` → clean
- `node --check scripts/second_exhibition_browser_qa.mjs` → clean
- Staging build + staging gate → PASS (root 92,976 B, 34 public files, 6 image SHA identical, 0 forbidden leakage)
- Deployment dry-run with v5.3-aware Section C → PASS exit 0
- Browser QA 5/5 viewports → PASS (current status visible, no stale phrasing, 0 console/page/failed/external, 6 images per viewport, all interactions OK)

**Do NOT do in v5.3b.**

- Do not commit / push / trigger Actions without explicit `DEPLOY v5.3b` from the user.
- Do not move or create any tag.
- Do not overwrite any existing Release.
- Do not modify any of the v4.5 immutable evidence files listed above.
- Do not modify `.github/workflows/pages.yml` again — v5.3 wiring is correct.

**Exit criteria for v5.3b.**

- All listed gates and validations PASS.
- Working tree contains only the 11 modified files listed above plus the untracked `.firecrawl/`.
- No tracked file under `second-exhibition/assets/`, `second-exhibition/docs/`, top-level `site/`, `_template/`, `_pilots/`, `release-assets/`, `reports/`, `.github/`, or workflow area is modified.
| `git reflog` shows no new commits this round. |
| Live production still at root 92,976 B / v2.9 = 1 / `/second-exhibition/` 200 / 6 images 200 / forbidden paths 404 / page text still reflects v5.3b-prep-old wording (until push). |

**Required authorization to commit + push + deploy.**

```
DEPLOY v5.3b
```

Only after receiving this exact string will commit + push + deploy be executed.

---

## v5.3c — Live Production Browser QA (executed)

**Goal.** Verify the v5.3b-published second exhibition against the live public URL from a real Chromium browser across five representative viewports, four environment variants (default, interaction, no-JS, reduced-motion), and verify the v5.3b status wording is intact, that all six candidate images load byte-identical to the local asset-checksums, and that the live root has not regressed.

**Result (this round).**

- Public URL `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` reached from Chromium headless shell `148.0.7778.96` (Chrome for Testing).
- Five-viewport matrix (1440x1000, 1280x900, 768x1024, 390x844, 320x700) -- all five pass.
- Per-viewport counts: `<section class="deep-block"> = 4`, artifact cards `[data-candidate-id] = 6` (C-01 / C-03 / C-06 / C-08 / C-09 / C-10), glossary items `.glossary-item = 12`, source notes `.source-note = 6`, credit lines `.credit-line = 6`, six images loaded (naturalWidth > 0).
- Per-viewport text: `production-deployed-v5.3` OK, `published-in-v5.3` OK, `imported-not-deployed` OK (only inside the `Import record: imported-not-deployed (v4.5)` annotation), `repository-only-not-deployed` ABSENT, stale `未部署` / `not deployed` phrase ABSENT.
- Per-viewport runtime: external requests = 0, failed requests = 0, console errors = 0, page errors = 0, horizontal overflow = 0.
- Interactions (1440x1000): guided toggle `aria-pressed` switches false -> true, C-01 lightbox opens with `role=dialog` + `aria-modal=true` + accessible name `图片查看器` (via `#lightbox-title`), close button receives focus, ESC closes, focus returns to the C-01 trigger; C-06 click is blocked (low-resolution warning); section navigation links (6) and 6 primary buttons are tab-reachable.
- no-JS render (JS disabled, 1440x1000): title, body text including all three status phrases, six artifact cards, source notes, credit lines, and `.repository-status` element all remain visible.
- reduced-motion (1440x1000, `prefers-reduced-motion: reduce`): `matchMedia` reports true; lightbox opens and ESC closes cleanly.
- Live root byte = 92,976 / v2.9 marker = 4 occurrences in body / `https://conanxin.github.io/leonardo-chinese-exhibition/` HTTP 200 (unchanged from v5.3).
- Live second-exhibition byte = 25,635 / HTTP 200 (unchanged from v5.3).
- Live six image SHA-256: byte-identical to `second-exhibition/assets/asset-checksums.sha256` (6/6 OK).
- Forbidden public paths: 16/16 -> HTTP 404.
- `git status -sb`: 0 modified, only `.firecrawl/` + the two v5.3b prep files untracked. No commit / push / Actions / Pages re-deploy / tag / Release this round.

**Files created in v5.3c (not yet committed; awaiting DEPLOY v5.3c).**

- `docs/SECOND_EXHIBITION_LIVE_PRODUCTION_QA_v5.3c.md` -- full QA baseline doc with 5-viewport matrix, interaction, a11y, no-JS, reduced-motion, asset SHA, forbidden paths, rollback method.
- `reports/leonardo_chinese_exhibition_v5_3c_live_production_browser_qa_report.md` -- round report with STATUS, totals, image SHA comparison, protected-path confirmation, tags/Releases unchanged, next = v5.4-real-stable-freeze.

**Files updated in v5.3c (not yet committed; awaiting DEPLOY v5.3c).**

- `docs/V5_ROADMAP.md` -- this section.
- `README.md` -- v5.3c block added alongside v5.3b block.

**Files preserved (v5.3c must NOT modify).**

- `site/`, `second-exhibition/site/`, `second-exhibition/data/`, `second-exhibition/assets/` (incl. all six image bytes), `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`, `second-exhibition/docs/RIGHTS_AND_SOURCES.md`, `_template/`, `_pilots/`, `release-assets/`, existing `reports/` files, `.github/workflows/pages.yml`, and every script under `scripts/`. The browser QA runner used this round lives at `/tmp/qa/` (not in the repo).

**Exit criteria for v5.3c (all met).**

- Live root byte unchanged at 92,976 B.
- v2.9 marker still present.
- `/second-exhibition/` HTTP 200.
- All six candidate images HTTP 200 with byte-identical SHA.
- Forbidden public paths 16/16 -> HTTP 404.
- 5/5 viewports see the current publication status; 0/5 see any stale phrasing.
- 0 external requests, 0 failed requests, 0 console errors, 0 page errors.
- C-01 lightbox open + ESC close + focus return; C-06 click blocked.
- no-JS render preserves status text, cards, source notes, credit lines.
- reduced-motion: lightbox open + ESC close under `prefers-reduced-motion: reduce`.

**Required authorization.**

```
DEPLOY v5.3c
```

Only after receiving this exact string will commit + push of the two new docs and the README/ROADMAP update be executed.

**Next.** **v5.4 — Public Stable Freeze** (annotated tag, Release, release notes, manifest, freeze report).

---

## v5.4 — Public Stable Freeze

**Goal.** Final QA, public source / rights recheck, release notes, annotated tag, GitHub Release.

**Tasks.**

- Draft `docs/RELEASE_NOTES_v5_0_REAL_SECOND_EXHIBITION_DEPLOYMENT.md`.
- Draft `release-assets/v5.0-real-second-exhibition-deployment-manifest.md`.
- Draft `reports/leonardo_chinese_exhibition_v5_4_public_stable_freeze_report.md`.
- Run all gates one final time.
- Create annotated tag `v5.0-real-second-exhibition-deployment`.
- Push the tag to origin.
- Create the GitHub Release.
- (Optional) backfill the freeze report with the tag object SHA, tag target SHA, Release URL, `createdAt`, and GitHub Actions run ID.

**Result (this round).**

- Public deployment verified -- live root `GET /` HTTP 200, byte-count **92,976** (unchanged from v5.3); v2.9 exact-marker (`v2.9-real-source-rights-audit`) = 1; v2.9 loose-marker = 4; second-exhibition `GET /second-exhibition/` HTTP 200, byte-count **25,635**.
- Production-state reconciliation verified -- `cmp -s site/index.html live-root` IDENTICAL; staged vs live for second-exhibition `index.html` / `style.css` / `script.js` IDENTICAL; six image SHA-256 byte-identical across source / staged / live.
- Live browser QA 5 / 5 PASS -- using local Playwright + Chromium headless shell `148.0.7778.96` against the live URL `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`. Viewports 1440x1000, 1280x900, 768x1024, 390x844, 320x700 all PASS for status wording, deep-block sections = 4, artifact cards = 6, glossary items = 12, source notes = 6, credit lines = 6, six images loaded, horizontal overflow = 0, console / page / failed / external errors = 0.
- Root and second-exhibition artifact identity PASS -- staging builder + staging gate exit 0; 25 main-site + 9 second-exhibition files (34 total); 0 forbidden leakage.
- Public inventory and forbidden-path boundary verified -- 25 main-site + 9 second-exhibition public files; 18 / 18 forbidden public paths (root and second-exhibition) return HTTP 404.
- Annotated tag and GitHub Release created -- `v5.0-real-second-exhibition-deployment` (annotated, points at the freeze doc commit); GitHub Release published with notes from `docs/RELEASE_NOTES_v5_0_REAL_SECOND_EXHIBITION_DEPLOYMENT.md`. Backfill commit (child of freeze) fills the freeze report with the tag object SHA / tag target SHA / Release URL / `publishedAt` / Actions run ID.
- Existing tags + Releases unchanged -- 12 pre-existing tags (`v2.0-public-portfolio-case` through `v4.8-real-second-exhibition-repository-hardening`) remain pinned to their original commits; no pre-existing GitHub Release was modified.

**Do NOT do in v5.4.**

- Do not move any existing tag.
- Do not overwrite any existing Release.

**Exit criteria for v5.4.**

- Tag points at the freeze commit.
- Release is published.
- Existing tags and Releases are unchanged.
- Live URL still 92,976 B.
- Second exhibition URL is live.

---

## Phasing summary

| Phase | Theme | Deploy? | Tag? | Release? |
|-------|-------|---------|------|----------|
| v5.0 | Deployment planning | No | No | No |
| v5.1 | Staging artifact build | No (staging only) | No | No |
| v5.2 | Deployment dry run | No (workflow review only) | No | No |
| v5.3 | Controlled deployment | Yes (first public deploy) | No | No |
| v5.4 | Public stable freeze | Yes | Yes | Yes |
| v5.5 | Public deployment maintenance | Redeploys (no content change) | No | No |
| v5.5a | Production hash baseline reconciliation | No | No | No |
| v5.5b | Staging audit schema reconciliation | No (tooling/docs only) | No | No |
| post-v5.5 | Future content updates / continued maintenance | Yes | per round | per round |

---

## v5.5 — Public Deployment Maintenance

**Goal.** Stabilise the v5.0 deployed surface with a repeatable manual
health-check, a frozen baseline, an operations runbook, and an
incident-response / rollback reference — without changing the live
content or Pages workflow.

**Tasks.**

- Add `scripts/second_exhibition_production_healthcheck.py`
  (Python stdlib only, optional JSON output, distinct exit codes 0/1/2).
- Freeze the production identity in
  `docs/PRODUCTION_HEALTH_BASELINE_v5.5.md` (URLs, byte sizes,
  SHA-256 values, status phrase counts, image checksums).
- Add `docs/PUBLIC_DEPLOYMENT_MAINTENANCE_RUNBOOK_v5.5.md` (daily check,
  full verification flow, allowed vs blocked maintenance actions).
- Add `docs/INCIDENT_RESPONSE_AND_ROLLBACK_v5.5.md` (severity levels,
  immediate checks, rollback principles, deploy-wiring revert chain,
  freeze-commit revert, post-rollback verification, evidence capture).
- Document the historical semantics of
  `production-deployed-v5.3` / `published-in-v5.3` /
  `imported-not-deployed` / `repository-only-not-deployed` so future
  rounds do not strip them mechanically.
- Run the new health check end-to-end against the live surface, exit 0.
- Run the public browser QA over the live URL, 5 / 5 viewports PASS.
- Push the documentation-only / script-only commit, wait for Actions
  success, re-verify the live surface is byte-identical.

**Do NOT do in v5.5.**

- Do not edit any file under `site/`, `second-exhibition/site/`,
  `second-exhibition/data/`, `second-exhibition/assets/`,
  `second-exhibition/docs/`, `second-exhibition/site/README.md`, or
  `.github/workflows/`.
- Do not modify the six public images or the asset manifest / checksums
  file.
- Do not create a new tag or Release.
- Do not modify the freeze tag (`v5.0-real-second-exhibition-deployment`)
  or its GitHub Release.
- Do not add a cron job or scheduled workflow — this round is a manual
  operator tool only.

**Exit criteria for v5.5.**

- `python3 scripts/second_exhibition_production_healthcheck.py` exits 0
  against `https://conanxin.github.io/leonardo-chinese-exhibition/`
  and `…/second-exhibition/`.
- The seven new / updated files are the only diff in this round.
- Stable tag still annotated on freeze commit `ac0f19e2…`.
- Live URL still 92,976 B; second-exhibition URL still 25,635 B.
- Six image SHA-256 still byte-identical to `asset-checksums.sha256`.
- Existing tags and Releases unchanged.

**Next.** v5.6 second-exhibition content iteration or continued
maintenance, depending on the next content round.

---

## v5.5a — Production Hash Baseline Reconciliation

**Goal.** Read-only reconciliation of the root site SHA-256 baseline
that diverged across the v5.0 → v5.5 trail. Establish one canonical
root SHA, document the source of the conflicting hash, and add the
reconciliation procedure to the v5.5 baseline doc — without touching
any production content or the staging builder.

**Tasks.**

- Generate five files with explicit binary-safe tools (`cp`,
  `git show`, `python3 scripts/second_exhibition_staging_build.py`,
  `curl -H 'Accept-Encoding: identity'`).
- Record `wc -c` and `sha256sum` for every file.
- Run `cmp -s` on all ten unordered pairs.
- Identify the canonical root SHA only when all five sources agree on
  bytes and on SHA-256 and all ten `cmp -s` pairs exit 0.
- Audit recursive grep of both candidate hashes across
  `README.md docs reports release-assets scripts`.
- Produce
  `docs/PRODUCTION_HASH_BASELINE_RECONCILIATION_v5.5a.md` with the
  five-source table, the attribution diagnosis, and the procedure.
- Append a minimal correction note + canonical-command block to
  `docs/PRODUCTION_HEALTH_BASELINE_v5.5.md`.
- Produce
  `reports/leonardo_chinese_exhibition_v5_5a_production_hash_baseline_reconciliation_report.md`.

**Do NOT do in v5.5a.**

- Do not modify any file under `site/`, `second-exhibition/site/`,
  `second-exhibition/data/`, `second-exhibition/assets/`,
  `second-exhibition/docs/`, or `.github/workflows/`.
- Do not modify the staging builder
  (`scripts/second_exhibition_staging_build.py`), the staging gate,
  the production health-check script, or any other in-repo script.
- Do not edit the existing release manifest line that contains the
  misattributed hash (the historical error is preserved unmodified
  for the audit trail).
- Do not create or move a tag or Release.
- Do not deploy new content.
- Do not modify the freeze tag or its GitHub Release.

**Exit criteria for v5.5a.**

- Five-source binary comparison PASS; canonical SHA equals
  `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`.
- All twelve protected paths (per "Modification scope" above) have
  empty `git diff` against `9bd8107`.
- Stable tag still annotated on freeze commit `ac0f19e2…`; Release
  v5.0 unchanged.
- Live root still 92,976 B / SHA `e2be1077…` after the v5.5a push
  (Pages workflow rebuilds without content change).
- Healthcheck re-run after the v5.5a push still PASS.

**Next.** v5.6-second-exhibition-content-iteration-prep.

---

## v5.5b — Staging Audit Schema Reconciliation

**Goal.** Replace the ambiguous audit key `source_index_html_sha256`
in the staging builder's `build-summary.json` schema with explicit
per-source / per-staged identity blocks, add a regression test that
prevents the root site SHA and the second-exhibition source SHA
from being conflated again, and document the schema as the canonical
reference going forward.

**Tasks.**

- Bump the audit schema to `audit_schema_version: "2.0"`.
- Add explicit `root_site` block
  (`source_path`, `source_bytes`, `source_sha256`,
  `staged_path`, `staged_bytes`, `staged_sha256`,
  `source_equals_staged`).
- Add explicit `second_exhibition` block with `path_rewrite_count`,
  and `source_equals_staged = false` (rewrites change staged bytes).
- Retain the deprecated `source_index_html_sha256` only with an
  explicit `_scope` annotation
  (`source_index_html_sha256_scope = "second-exhibition/site/index.html"`).
- Update `scripts/second_exhibition_staging_gate.py` to read the new
  schema, enforce `root_site.source_equals_staged = true`, and
  enforce `second_exhibition.source_equals_staged = false`
  (with `path_rewrite_count = 6`).
- Add a `B'. Schema v2 identity from audit` section to
  `scripts/second_exhibition_deployment_dry_run.py` that
  cross-checks the audit summary against the live repo files.
- Add a regression test
  `scripts/test_second_exhibition_staging_audit.py` (stdlib only,
  runs in `/tmp`, 28 assertions, exit 0 on PASS).
- Create `docs/STAGING_AUDIT_SCHEMA_v5.5b.md` as the canonical
  reference for the schema.
- Append forward-reference / link the schema doc from the v5.5a
  reconciliation and v5.5 baseline documents.
- Do not modify production content, assets, manifest, checksums,
  workflow, stable tag, or Release.

**Do NOT do in v5.5b.**

- Do not edit any file under `site/`, `second-exhibition/site/`,
  `second-exhibition/data/`, `second-exhibition/assets/`,
  `second-exhibition/docs/`, or `.github/workflows/`.
- Do not modify the six images or any check-gate output bytes.
- Do not create or move a tag or Release.
- Do not modify the v5.0 freeze tag or its GitHub Release.
- Do not rewrite the v5.0 release manifest line 61 (historical
  error preserved unchanged).

**Exit criteria for v5.5b.**

- `scripts/second_exhibition_staging_build.py` produces a
  `build-summary.json` whose `audit_schema_version` is `"2.0"`.
- `scripts/second_exhibition_staging_gate.py` exits 0 against a
  fresh artifact, and emits the new schema v2 PASS lines.
- `scripts/test_second_exhibition_staging_audit.py` exits 0.
- All eight pre-existing scripts (template, build, repository QA,
  asset gate, browser QA, dry-run, dry-run browser, preflight)
  remain unchanged at `git diff --stat` level.
- Live surface byte-identical to the v5.5 freeze after the v5.5b
  push (rebuilt by the unchanged Pages workflow).
- Stable tag still annotated on freeze commit `ac0f19e2…`; Release
  v5.0 unchanged.

---

## v5.5b Staging Audit Key Semantics Fix

**Goal.** Tighten the v5.5b schema-version contract: canonicalise the
schema-version field name (`schema_version`, deprecated alias
`audit_schema_version`), use the `*_index_*` infix on every
per-source / per-staged identity field, and rename the carry-over
v1 key to `legacy_second_exhibition_source_index_html_sha256` with
its scope baked into the field name. Gate must fail-loud if a bare
v1 key (`source_index_html_sha256` or `source_index_html_sha256_scope`)
is re-emitted.

**Tasks.**

- Rename `audit_schema_version` → `schema_version` (canonical) in
  `scripts/second_exhibition_staging_build.py`; retain
  `audit_schema_version` as a deprecated alias for one round.
- Add `*_index_*` infix to all six identity fields inside each
  nested block:
  `source_index_path`, `source_index_bytes`, `source_index_sha256`,
  `staged_index_path`, `staged_index_bytes`, `staged_index_sha256`.
- Rename deprecated carry-over key
  `source_index_html_sha256` →
  `legacy_second_exhibition_source_index_html_sha256`. Remove the
  now-redundant `_scope` companion key.
- Update `scripts/second_exhibition_staging_gate.py` to read the
  canonical `schema_version` + `*_index_*` fields, and reject any
  audit that emits bare v1 keys (`source_index_html_sha256`,
  `source_index_html_sha256_scope`) as fail-loud.
- Update `scripts/second_exhibition_deployment_dry_run.py` §B'
  Schema v2 identity from audit with the same contract.
- Update `scripts/test_second_exhibition_staging_audit.py` to
  assert the canonical field names + bare-v1-key absence +
  renamed legacy-field presence. (Total assertions: 30.)
- Rewrite `docs/STAGING_AUDIT_SCHEMA_v5.5b.md` to document the
  new canonical contract.
- Capture a `/tmp/v55b-before-artifact` baseline build against
  `92f14e9` (the v5.5a-baseline) using
  `git show 92f14e9:scripts/second_exhibition_staging_build.py`,
  then prove the new `/tmp/v55b-after-artifact` is **34/34
  byte-identical** (public artifact, 0 drift).
- Write
  `reports/leonardo_chinese_exhibition_v5_5b_staging_audit_key_semantics_fix_report.md`.

**Do NOT do in v5.5b-key-semantics-fix.**

- Do not edit any file under `site/`, `second-exhibition/site/`,
  `second-exhibition/data/`, `second-exhibition/assets/`,
  `second-exhibition/docs/`, or `.github/workflows/`.
- Do not modify the six images or any check-gate output bytes.
- Do not create or move a tag or Release.
- Do not modify the v5.0 freeze tag or its GitHub Release.
- Do not rewrite the v5.0 release manifest line 61 (historical
  error preserved unchanged).
- Do not modify
  `scripts/second_exhibition_production_healthcheck.py`
  (it does not consume the staging audit schema).
- Do not modify any other in-repo script outside the allowlist
  (template quality gate, build gate, repository QA, asset gate,
  browser QA, dry-run browser, preflight all stay untouched).

**Exit criteria for v5.5b Staging Audit Key Semantics Fix.**

- `git status` shows exactly the files staged: 3 modified scripts
  in scope + 1 modified regression test + 1 modified schema doc +
  1 modified V5_ROADMAP + 1 modified README + 1 new report.
- `scripts/second_exhibition_staging_build.py` emits a
  `build-summary.json` with:
  - `schema_version: "2.0"` (canonical)
  - `audit_schema_version: "2.0"` (deprecated alias)
  - bare `source_index_html_sha256` ABSENT
  - bare `source_index_html_sha256_scope` ABSENT
  - `legacy_second_exhibition_source_index_html_sha256` PRESENT,
    value `f31ddcba…`
  - `root_site.source_index_sha256`, `source_index_bytes`,
    `source_index_path`, `staged_index_*` populated
  - `second_exhibition.source_index_sha256`, etc., populated with
    `source_equals_staged = false`, `path_rewrite_count = 6`
- Artifact built this round is **34/34 byte-identical** to the
  v5.5a-baseline build (proves 0 public drift).
- `scripts/second_exhibition_staging_gate.py` exits 0 against the
  new artifact; same gate exits 1 against a synthetic stale v1
  audit (fail-loud policy).
- `scripts/test_second_exhibition_staging_audit.py` exits 0 with
  all 30 assertions passing.
- `scripts/second_exhibition_deployment_dry_run.py` §B' Schema
  v2 identity exits 0 with the new audit.
- `python3 scripts/template_quality_gate.py` PASS.
- `python3 scripts/second_exhibition_build_gate.py` PASS.
- `python3 scripts/second_exhibition_repository_qa.py` PASS 164/164.
- `python3 scripts/second_exhibition_production_healthcheck.py`
  PASS (post-push, 0 production drift).
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256` 6/6 OK.
- Workflow `.github/workflows/` empty diff.
- Tag still annotated on freeze commit `ac0f19e2…`; Release v5.0
  unchanged.

**Next.** `v5.6-second-exhibition-content-iteration-prep`.

---

## v5.6 Second Exhibition Content Iteration Prep

**Goal.** Plan the first content iteration of the second exhibition
(`second-exhibition-v0.1 → second-exhibition-v0.2`) without modifying
any production content. Produce five planning documents: an audit,
a fact-check matrix, an iteration plan, a changeset draft, and an
acceptance criteria document. Next round awaits explicit
`IMPLEMENT v5.6b` authorization.

**Tasks.**

- Capture a frozen snapshot of the second exhibition content as
  recorded at HEAD `ce01f1d…` (source / staged / live identity,
  section / artifact / glossary counts, hero region, status-phrase
  counts, image roster, data JSON shapes).
- Audit current content across five dimensions: factual accuracy,
  narrative structure, visitor comprehension, content depth,
  source / curation boundary.
- Tag each finding with a severity (`blocker / high / medium / low`)
  and a type (`factual / terminology / narrative / repetition /
  accessibility / visitor comprehension / source-boundary / metadata`).
- Produce a fact-check matrix that classifies every candidate claim
  as `verified / wording-needs-precision / unsupported /
  interpretation-only / research-needed` and traces each
  `verified` row to either `docs/SOURCE_AUDIT_MANIFEST.md` or the
  institutional source URL.
- Define v0.2 scope: still 4 sections, still 6 artifact cards, still
  6 images, glossary 12 → 14; URL / status model / source-evidence
  files unchanged.
- Draft a 15-row changeset (CHG-01 … CHG-15), each row naming its
  target file, JSON path or HTML section, current state, proposed
  state, reason, evidence, risk, and impact on page byte, source
  SHA, staged/live SHA, browser QA, gate QA, and asset checksums.
- Define the v0.2 acceptance criteria (Content / Data consistency /
  Assets / Tooling / Page-render / Deployment / Source & rights /
  Authority).
- Do **not** modify any production file; the allowlist for this
  round is exactly the eight documents named below.

**Deliverables.**

- `docs/SECOND_EXHIBITION_CONTENT_AUDIT_v5.6.md` (audit)
- `docs/SECOND_EXHIBITION_FACT_CHECK_MATRIX_v5.6.md` (matrix)
- `docs/SECOND_EXHIBITION_CONTENT_ITERATION_PLAN_v5.6.md` (plan)
- `docs/SECOND_EXHIBITION_CONTENT_CHANGESET_DRAFT_v5.6.md` (changeset)
- `docs/SECOND_EXHIBITION_CONTENT_ACCEPTANCE_CRITERIA_v5.6.md` (gate)
- `docs/V5_ROADMAP.md` (this round's section)
- `README.md` (one new section)
- `reports/leonardo_chinese_exhibition_v5_6_content_iteration_prep_report.md`

**Do NOT do in v5.6-prep.**

- Do not edit any file under `site/`, `second-exhibition/site/`,
  `second-exhibition/data/`, `second-exhibition/assets/`,
  `second-exhibition/docs/`, or `.github/workflows/`.
- Do not modify the six image files, the asset manifest, the
  checksums, or the source / rights evidence files.
- Do not create a new tag or Release.
- Do not modify the v5.0 freeze tag.
- Do not bypass the planning gate by editing `second-exhibition/`
  in this round.
- Do not process the untracked `.firecrawl/` directory.

**Exit criteria for v5.6-prep.**

- All 8 allowlisted files committed.
- `git status` shows exactly those 8 files modified or added; other
  paths empty.
- Reality gate (§1 of the brief) PASS.
- Push triggers the Pages workflow; post-push verification shows
  **0 production drift** (root SHA, second-exhibition SHA, six image
  checksums, status-phrase counts, and the browser QA 5/5 result
  all unchanged).
- Stable tag still annotated on freeze commit `ac0f19e2…`; Release
  v5.0 still `isDraft=false`, `isPrerelease=false`.

**Next.** `v5.6b-content-iteration-implementation-prep`.

**Required authorization before v5.6b starts:**
`IMPLEMENT v5.6b`.
## v5.6b Second Exhibition v0.2 Implementation — Prepared

This round is content-iteration execution on top of v5.6 prep's
audit + fact-check + plan + changeset draft + acceptance criteria.

- **CHG-01 through CHG-15 implemented** (factual corrections,
  terminology, hero / 3-min-guide rewrites, sections 1–4, glossary
  12 → 14, marker v0.1 → v0.2, build_gate + repository_qa + production
  healthcheck sync).
- **Candidate marker**: `second-exhibition-v0.2` (5 HTML occurrences in
  `site/index.html`; `v0.1` count = 0; both build_gate + repository_qa
  enforce the bidirectional regression guard).
- **Sections**: 4 (`section-1-observation`, `section-2-classification`,
  `section-3-reproduction`, `section-4-reorganization`).
- **Artifacts**: 6 (C-01, C-03, C-06, C-08, C-09, C-10).
- **Glossary**: **14** items (was 12; added `cyanotype` + `photogram`).
- **Images**: **unchanged** — 6 SHA match `asset-checksums.sha256`.
- **Source / rights evidence**: **unchanged** — `SOURCE_AUDIT_MANIFEST.md`
  and `RIGHTS_AND_SOURCES.md` untouched.
- **Candidate root identity**: 92,976 B / SHA `e2be1077…` (unchanged).
- **Candidate second-exhibition source identity**:
  31,458 B / SHA `662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e`.
- **Candidate second-exhibition staged identity**:
  31,452 B / SHA `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
  (= source − 6 bytes from exactly 6 image-path rewrites).
- **Inline-only adjustment**: 4 × `style="scroll-margin-top: 2px;"` on
  the 4 `<section id="section-N-…">` elements — fixes the 320×700
  viewport section-nav sub-pixel anchor positioning; no semantic / CSS
  / asset impact.
- **Candidate gates**:
  - template_quality_gate: **PASS**
  - second_exhibition_build_gate: **PASS**
  - second_exhibition_repository_qa: **166 PASS / 0 FAIL / 0 WARNINGS**
  - 4 × JSON: OK
  - 6 × image checksum: OK
- **Staging / dry-run**:
  - `second_exhibition_staging_build`: PASS (6 path rewrites, schema v2 audit)
  - `second_exhibition_staging_gate`: PASS (34 entries, identity verified)
  - `second_exhibition_deployment_dry_run`: PASS (14/14 allowlist,
    16/16 forbidden, 34/34 roundtrip byte-identical, workflow NOT modified)
- **Five-viewport browser QA**: **PASS** at
  1440×1000, 1280×900, 768×1024, 390×844, 320×700.
  - consoleErrors: 0, pageErrors: 0, failedRequests: 0, externalRequests: 0
  - 12/12 interactions PASS (incl. section navigation True post-fix)
- **Healthcheck dual-track**:
  - current production v0.1: PASS (68/68; root 92,976 B; second 25,635 B)
  - local candidate v0.2 (`--candidate-v0.2`): PASS (68/68; root 92,976 B;
    second 31,452 B / SHA `00894e8d…`)
- **Workflow**: NOT modified.
- **Tags / Releases**: NOT modified.
- **Working tree**: 11 modified + 4 new files; 0 staged, 0 commit, 0 push.
- **Current production**: still `second-exhibition-v0.1` (live, unchanged).

### Known carry-overs (NOT v5.6b regressions)

- `second-exhibition/data/assets.json` `marker: second-exhibition-v0.1`
  (asset-data historical field, NOT current-exhibition public marker;
  not copied into public artifact).
- `second-exhibition/site/README.md` `second-exhibition-v0.1`
  (NOT copied into public artifact).

Both carry-overs are scope-bounded by brief §15 and are explicitly
documented in `docs/SECOND_EXHIBITION_CONTENT_ITERATION_IMPLEMENTATION_v5.6b.md`
under "Known carry-overs".

### Stop point

- **No** `git add`, **no** `git commit`, **no** `git push`, **no** new
  tag, **no** new Release.
- Local background http servers stopped; staging directories cleaned
  to scope-managed temp paths.
- **Required authorization**: `DEPLOY v5.6b`.

Without this token, the production surface remains v5.0-frozen
v0.1 (`ac0f19e2…`). With the token, the commit(s) produced from this
working tree go through the Pages workflow, post-push reality
verification confirms `0 production drift` on every identity
checkbox, and `v0.2` becomes the live surface.

## v5.6c — Post-deploy Verification & Baseline Promotion

Round after v5.6b deployment (commit `6b7ee06`).

- `second-exhibition-v0.2` publicly verified on https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/
- Default production healthcheck promoted from v0.1 → v0.2:
  - `SECOND_EXPECTED_BYTES = 31452`
  - `SECOND_EXPECTED_SHA256 = 00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
  - `SECOND_EXACT_MARKER = "second-exhibition-v0.2"` (count = 3)
  - `SECOND_STALE_MARKER = "second-exhibition-v0.1"` (count = 0; regression guard)
- `--candidate-v0.2` retained as a deprecated alias (one migration round), emits stderr `DEPRECATION NOTICE`
- `--legacy-v0.1` retained only for explicit historical-fixture checks
- Default healthcheck: 70 PASS / 0 FAIL on live production
- Public 5-viewport browser QA: 5/5 PASS (1440×1000, 1280×900, 768×1024, 390×844, 320×700)
  - 0 console errors, 0 page errors, 0 failed requests, 0 external requests
  - 0 overflow across all 5 viewports
  - All 8 interactions PASS (guided toggle, lightbox, dialog name, ESC, focus return, C-06 exclusion, section nav)
  - no-JS: 6 cards / 14 glossary / 6 source notes / 6 credit lines / body text / repo status — PASS
  - reduced-motion: lightbox + ESC — PASS
- Image checksums: 6/6 unchanged
- No page / data / asset / workflow changes (docs + 1 script only)
- Stable v5.0 tag `v5.0-real-second-exhibition-deployment` remains initial-deployment anchor (unchanged)

### Next

- v5.6-real-stable-freeze

## v5.6d — Live Browser QA Reproducibility

Promote v5.6c's `/tmp/v56c-live-browser-qa.mjs` fixes into the official
runner `scripts/second_exhibition_browser_qa.mjs` so that public QA is
reproducible from repository content alone (no `/tmp` scripts, no
user-specific paths, no `/home/conanxin/...` hardcoding).

### Changes (additive; v4.8 design preserved)

- `checkServer()` now uses `https.request` for `https://` URLs (was
  `http.get` only — failed against public Pages).
- `trackRequests()` is now **origin-aware**: same-origin subresource
  fetches (whether `http://127.0.0.1:8770/site/...` or
  `https://conanxin.github.io/.../second-exhibition/...`) are first-party,
  never counted as "external".
- `main()` error message adapts to whether the target is local
  (suggests `python3 -m http.server 8770`) or remote (neutral).
- Docstring updated to document both invocation patterns
  (local server, public URL).

### What did NOT change

- `loadPlaywright()` — unchanged. `PLAYWRIGHT_NODE_PATH` env var
  remains the canonical override. No `~/.local/...` lookup in the
  script.
- Selectors, viewport matrix, interaction / a11y / no-JS /
  reduced-motion checks — all byte-identical to v4.8.
- Lazy-image handling — unchanged (still scroll + 800 ms).
- Exit codes, JSON summary shape, default URL — unchanged.

### Verification (this round, official runner only)

- Local 5-viewport QA: 5/5 PASS, 0 errors of any kind.
- Public 5-viewport QA (against
  `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`):
  5/5 PASS, 0 errors of any kind.
- Default production healthcheck: 70/70 PASS, root 92,976 B / second
  31,452 B — unchanged.
- Public artifact (root + second) byte-identical to v5.6c.
- Scope guard: only `scripts/second_exhibition_browser_qa.mjs`
  modified. All protected paths (`site/`, `second-exhibition/`,
  `.github/workflows/`, `_template/`, `_pilots/`, `posts/`,
  `case-study/`, `release-assets/`, other `scripts/*.py`,
  `__pycache__`) empty.

### Next

- v5.6-real-stable-freeze
