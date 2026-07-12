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
| post-v5.4 | Public QA, future updates | Yes | per round | per round |