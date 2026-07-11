# v5.0 Second Exhibition Deployment Checklist

The checklist is split into five phases. Each phase has its own exit gate. Any failure exits the round and either fixes the issue or rolls back.

## Phase 1 — Pre-build

- [ ] `git status` is clean except for untracked `.firecrawl/` (which is not touched).
- [ ] Current HEAD matches `v4.8` evidence backfill commit `01bebd87c2d109b2e549430436fe91c8ff2d3720`.
- [ ] `python3 scripts/template_quality_gate.py` → **PASS, 37/37**.
- [ ] `python3 scripts/second_exhibition_build_gate.py` → **PASS**.
- [ ] `python3 scripts/second_exhibition_repository_qa.py` → **161 PASS / 0 FAIL / 0 WARNINGS** (exit 0).
- [ ] `node scripts/second_exhibition_browser_qa.mjs` → **PASS** (5/5 viewports, 0 external requests, 0 console errors, 0 failed requests, 0 page errors).
- [ ] `sha256sum -c second-exhibition/assets/asset-checksums.sha256` → **6/6 OK**.
- [ ] `node --check second-exhibition/site/script.js` → OK.
- [ ] `node --check scripts/second_exhibition_browser_qa.mjs` → OK.
- [ ] All JSON files valid (`asset-import-manifest.json`, `exhibition.json`, `sections.json`, `glossary.json`, `assets.json`).
- [ ] No High / Blocked risk open in `SECOND_EXHIBITION_DEPLOYMENT_RISK_REGISTER_v5.0.md`.
- [ ] Current live baseline captured: live byte = 92,976 B, v2.9 marker = 1, second exhibition title count = 0.
- [ ] `python3 scripts/second_exhibition_deployment_preflight.py` → **PASS**.

**Exit gate 1:** all pre-build items above checked. Proceed to Phase 2.

## Phase 2 — Artifact assembly

The staging directory is **outside the repository** (e.g., `/tmp/leonardo-pages-artifact/`). Nothing is committed during this phase.

- [ ] Staging directory created from scratch.
- [ ] Top-level site copied byte-identical: `cp -p site/index.html staging/`, `cp -p site/style.css staging/`, `cp -p site/script.js staging/`.
- [ ] Second-exhibition page files copied: `cp -p second-exhibition/site/index.html staging/second-exhibition/index.html`, `cp -p second-exhibition/site/style.css staging/second-exhibition/style.css`, `cp -p second-exhibition/site/script.js staging/second-exhibition/script.js`.
- [ ] Second-exhibition assets copied: 6 raster images under `staging/second-exhibition/assets/images/`.
- [ ] Path rewrite applied **only** to the staging copy of `second-exhibition/index.html`:
  - `../assets/images/` → `./assets/images/`
- [ ] `second-exhibition/data/`, `second-exhibition/docs/`, `second-exhibition/assets/asset-import-manifest.json`, `second-exhibition/assets/asset-checksums.sha256` are **NOT** in the staging tree.
- [ ] No `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `docs/`, `reports/`, `.git/`, `.firecrawl/` in the staging tree.
- [ ] File inventory generated and saved outside the repo.
- [ ] SHA-256 hash inventory generated for every file in the staging tree.
- [ ] Hash of top-level `staging/index.html` matches `sha256sum site/index.html` byte-identical.
- [ ] Hashes of all 6 staging raster images match `second-exhibition/assets/asset-checksums.sha256`.

**Exit gate 2:** staging inventory matches expectations. Proceed to Phase 3.

## Phase 3 — Staging QA

- [ ] Start a local HTTP server on a port that does not conflict with existing services: `python3 -m http.server <port> --directory /tmp/leonardo-pages-artifact`.
- [ ] Browser QA runner pointed at the staging root: `SECOND_EXHIBITION_QA_URL=http://127.0.0.1:<port>/ node scripts/second_exhibition_browser_qa.mjs` → **PASS**.
- [ ] Browser QA runner pointed at the staging second exhibition: `SECOND_EXHIBITION_QA_URL=http://127.0.0.1:<port>/second-exhibition/ node scripts/second_exhibition_browser_qa.mjs` → **PASS**.
- [ ] All 6 image URLs return HTTP 200.
- [ ] Direct probes for `/second-exhibition/data/`, `/second-exhibition/docs/`, `/second-exhibition/assets/asset-import-manifest.json` all return HTTP 404.
- [ ] `externalRequests` = 0.
- [ ] `consoleErrors` = 0.
- [ ] `failedRequests` = 0.
- [ ] `pageErrors` = 0.
- [ ] No horizontal overflow at any viewport.
- [ ] Accessibility: h1 count = 1, no missing alt on artifact-card images, no missing button names, no heading jumps, focus restoration works.
- [ ] No-JS rendering: all 6 cards visible, source notes and credit lines visible, repository status visible.
- [ ] Reduced-motion rendering: lightbox opens and closes on `Escape`.

**Exit gate 3:** all staging QA items checked. Stop the local HTTP server. Proceed to Phase 4.

## Phase 4 — Deployment

- [ ] `.github/workflows/pages.yml` change is exactly one commit and one push.
- [ ] The change switches `actions/upload-pages-artifact@v3` `path:` from `site` to the staging directory (assembled by a pre-step).
- [ ] No second Pages workflow is created.
- [ ] No CNAME is created.
- [ ] No repository-root upload (`path: .` or similar).
- [ ] Push to `main` and wait for GitHub Actions.
- [ ] GitHub Actions run is `success`.
- [ ] The deployment commit is recorded.
- [ ] **No tag is created in this round.** (Tags only after v5.4 verification passes.)
- [ ] **No Release is created in this round.**

**Exit gate 4:** GitHub Actions success and no tag / Release created. Proceed to Phase 5.

## Phase 5 — Post-deployment

- [ ] Live URL `https://conanxin.github.io/leonardo-chinese-exhibition/` → HTTP 200.
- [ ] Live byte still **92,976 B**.
- [ ] `v2.9-real-source-rights-audit` count still **1**.
- [ ] Top-level `script.js` HTTP 200.
- [ ] `/second-exhibition/` HTTP **200** (this is the new state).
- [ ] `/second-exhibition/index.html` HTTP 200.
- [ ] `/second-exhibition/style.css` HTTP 200.
- [ ] `/second-exhibition/script.js` HTTP 200.
- [ ] All 6 `/second-exhibition/assets/images/...` URLs HTTP 200.
- [ ] Direct probes on `/second-exhibition/data/`, `/second-exhibition/docs/`, `/second-exhibition/assets/asset-import-manifest.json`, `/second-exhibition/assets/asset-checksums.sha256` all HTTP 404.
- [ ] Direct probes on `/README.md`, `/_template`, `/_pilots`, `/posts`, `/case-study`, `/release-assets` all HTTP 404.
- [ ] Browser QA against public URL `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` → **PASS**.
- [ ] External requests from public URL = 0.
- [ ] Source / rights recheck: each of the 6 source URLs (BHL, Met, Rijksmuseum × 2, NMNH) opened fresh and compared against `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` and `RIGHTS_AND_SOURCES.md`.
- [ ] No High / Blocked risk open after deployment.
- [ ] Release notes drafted (separate round).

**Exit gate 5:** all post-deployment items checked. **Proceed to v5.4 stable freeze.** Tag + Release only after this gate.

## Rollback gate

If any of the following occurs at any phase, abort the round and execute `SECOND_EXHIBITION_ROLLBACK_PLAN_v5.0.md`:

- Top-level site regresses (live byte changes, v2.9 marker missing, top-level URL not 200).
- Internal files (README, _template, _pilots, posts, etc.) become reachable on Pages.
- Browser QA fails against public URL with no simple fix.
- External requests > 0 from the published second exhibition.
- Source / rights blocker.
- GitHub Actions deployment fails twice in a row.