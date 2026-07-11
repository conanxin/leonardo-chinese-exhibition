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

---

## v5.3 — Controlled Deployment

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