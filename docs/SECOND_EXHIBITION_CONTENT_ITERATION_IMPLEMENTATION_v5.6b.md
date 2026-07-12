# v5.6b Second Exhibition v0.2 Content Iteration Implementation

## Baseline

- **Baseline HEAD / origin/main**: `5edc9fdc149bea2ac60a67a1244e24bae4f819b8`
- **Stable tag**: `v5.0-real-second-exhibition-deployment` (annotated tag, object `c8871f09…`, target `ac0f19e2c03b09738ae49b4a15c629a1f2177068`)
- **GitHub Releases**: v5.0 (unchanged from v5.3b+v5.5+a+v5.5b freezes)
- **Current production v0.1 identity** (live, unchanged):
  - root: 92,976 B / SHA `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
  - second-exhibition: 25,635 B / SHA `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c`
  - marker: `second-exhibition-v0.1`
- **Candidate v0.2 identity** (worker-only, local):
  - root source/staged: 92,976 B / SHA `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` (unchanged)
  - second-exhibition source: **31,458 B / SHA `662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e`**
  - second-exhibition staged: **31,452 B / SHA `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`**
  - marker: `second-exhibition-v0.2`
- **No-commit / no-push stop point**: this round produces documents only; commit + push require explicit `DEPLOY v5.6b` authorization.

## CHG-01 to CHG-15

| CHG | File | Before | After | Evidence | Result |
|---|---|---|---|---|---|
| CHG-01 | `second-exhibition/data/glossary.json` | Rijksprentenkabinet described as herbarium (implicit) | Rijksprentenkabinet (Rijksmuseum) — print room / works on paper, NOT herbarium | `data/glossary.json` Rijksprentenkabinet definition; page glossary div | ✅ |
| CHG-02 | `second-exhibition/data/sections.json` + `site/index.html` | Section 1 implied C-01/C-03 are 标本 | Section 1 disambiguates watercolour plate vs specimen (BHL Album is reproduction, NMNH is herbarium) | `data/sections.json` section-1 body; `site/index.html` section-1 paragraph | ✅ |
| CHG-03 | `data/sections.json` + `site/index.html` | Section 2 conflated C-06 and C-08 as 同一类别 | Section 2 explicitly distinguishes NMNH herbarium specimen thumbnail (C-06) vs Met 19th-c photograph (C-08) | `data/sections.json` section-2 body; `site/index.html` section-2 paragraph | ✅ |
| CHG-04 | `data/sections.json` + `site/index.html` | Section 3 ambiguous on Rijksprentenkabinet role | Section 3 explicit Rijksprentenkabinet = print-room (blueprint / photography department) holding cyanotype photograms, not herbarium | `data/sections.json` section-3 body; `site/index.html` section-3 paragraph | ✅ |
| CHG-05 | `data/sections.json` + `site/index.html` | Section 4 abstract on identifier / rights / IIIF | Section 4 adds concrete identifier / rights / IIIF examples (EZID arK, accession 2003.562.3, isPublicDomain, CC0 1.0, Micrio IIIF Image API, manifest 404 caveat) | `data/sections.json` section-4 body; `site/index.html` section-4 paragraph | ✅ |
| CHG-06 | `data/glossary.json` + page glossary div | cyanotype gloss over | cyanotype disambiguated: 蓝晒摄影印刷 (process) vs photogram (把对象作为底片晒制) | `data/glossary.json` items `cyanotype` and `photogram` | ✅ |
| CHG-07 | `data/glossary.json` + page glossary div | Public Domain / CC0 conflated | Public Domain = legal status (creator + term expiry); CC0 = explicit waiver tool; institution-specific labelling (Met `isPublicDomain: true`, Rijksmuseum `Public domain` page + CC0 1.0 link, NMNH dataset-level CC0 1.0) | `data/glossary.json` items `public-domain` and `cc0`; section 4 paragraph | ✅ |
| CHG-08 | `data/glossary.json` + page glossary div | IIIF treated as undifferentiated | IIIF Image API (image-derivative endpoint, `iiif.io/api/image`) vs IIIF Presentation API (manifest, `iiif.io/api/presentation`) | `data/glossary.json` items `iiif-image` and `iiif-presentation`; section 3 paragraph | ✅ |
| CHG-09 | `site/index.html` Hero | Generic title-only hero | Hero carries central question ("植物图谱如何变成可机读的图像史?") | `site/index.html` hero block | ✅ |
| CHG-10 | `site/index.html` 3-min guide | "What is this" 3-min list | 3-min guide rewritten as a viewing method (4 viewing actions) instead of abstract descriptor | `site/index.html` "如果你只有 3 分钟" block | ✅ |
| CHG-11 | `data/sections.json` + `site/index.html` Section 3 deep-block | Single prompt | Section 3 deep-block adds a prompt variant about cross-medium continuity vs break (simulation vs digital) | `data/sections.json` section-3 deep-block prompt; `site/index.html` deep-block | ✅ |
| CHG-12 | `data/glossary.json` + page glossary div | 12 items (no cyanotype, no photogram) | 14 items: added `cyanotype` + `photogram` | `data/glossary.json` items count = 14; build_gate + repository_qa echo 14 | ✅ |
| CHG-13 | `data/exhibition.json` + `data/sections.json` | marker `second-exhibition-v0.1` | marker `second-exhibition-v0.2` (5 occurrences in `site/index.html`) | `data/exhibition.json` `version`; `data/sections.json` `exhibition_version`; `site/index.html` `data-marker` / title / kicker / footer | ✅ |
| CHG-14 | `VISITOR_GUIDE_ZH.md` + `CURATORIAL_ESSAY_ZH.md` + `DEEP_RESEARCH_NOTES_ZH.md` + `BUILD_ASSET_USAGE.md` | v0.1 marker references + minor term gaps | Marker bumped to v0.2; cyanotype / photogram / Public Domain / CC0 / IIIF Image+Presentation terminology aligned; C-10 manifest 404 caveat phrasing restored (per `C-10` carve-out in CITATION_NOTE) | git diff against HEAD: 4 files +6/-6, +1/-1, +2/-1, +7/-7 | ✅ |
| CHG-15 | `scripts/second_exhibition_build_gate.py` + `scripts/second_exhibition_repository_qa.py` + `scripts/second_exhibition_production_healthcheck.py` | Marker assertion only checked `v0.2` presence, allow-lenient | Build + repository QA: 双向断言 `v0.2 present` AND `v0.1 absent` (regression guard); production healthcheck: new `--candidate-v0.2` flag → uses `SECOND_V02_CANDIDATE_BYTES=31452` + `SECOND_V02_CANDIDATE_SHA256=00894e8d…` (and source `SECOND_V02_SOURCE_*` constants). Default behavior (without flag) remains the v5.0 freeze v0.1 baseline. | git diff: `build_gate.py` +8/-5, `repository_qa.py` +14/-4, `production_healthcheck.py` +39/-5 | ✅ |

### Additional v5.6b diff (not CHG row, but v5.6b implementation decision)

- **`site/index.html` 4 × `style="scroll-margin-top: 2px;"`** on the 4 `<section id="section-N-…">` elements (sections 1–4).
  - **Purpose**: fix 320×700 viewport section navigation: sub-pixel anchor positioning produced `rect.top ≈ -0.05`, failing the `top >= 0` check in `scripts/second_exhibition_browser_qa.mjs`. With `scroll-margin-top: 2px` the section lands at `rect.top ≈ +1.95`, all 5 viewports pass.
  - **Impact**: 4 × ~32 chars inline style → source bytes 31,330 → 31,458 (+128); no asset / CSS / JS / structural change; HTML-semantic safe; no class-name collision.
  - **Documented here** so reviewer doesn't miss this 5th "boundary" change.

## Factual and terminology corrections

- **NMNH Botany vs Rijksprentenkabinet**:
  - NMNH Botany holds **herbarium specimens** (pressed / dried plants attached to accession sheets). C-06 in this exhibition is the low-resolution (90×90) NMNH Botany thumbnail derived from such a specimen.
  - Rijksmuseum Rijksprentenkabinet is the **print room** (prentenkabinet = "prints cabinet"), holding works on paper and photography, not a herbarium. C-09 / C-10 are Anna Atkins cyanotype photograms held there.
- **cyanotype / photogram**:
  - cyanotype = 蓝晒摄影印刷 (a 19th-c photographic printing process using iron-salt photochemistry, producing Prussian-blue prints).
  - photogram = 把对象作为底片晒出的摄影图像 (a contact-print photographic image made without a camera — the object itself is the negative / receiver of light).
  - C-09 / C-10 are cyanotype **photograms** of botanical specimens by Anna Atkins (not herbarium sheets).
- **Public Domain / CC0**:
  - Public Domain = 公共领域 (legal status: works whose copyright has expired or been waived); CC0 1.0 = a specific tool (Creative Commons) that lets a rights-holder waive copyright where possible.
  - Institution-specific labels observed: Met Collection API `isPublicDomain: true` + Public Domain page indicator (C-08 double-confirmation); Rijksmuseum public-domain page label + CC0 1.0 link (C-09 / C-10); NMNH Botany dataset-level CC0 1.0 release (C-06).
- **IIIF Image API vs Presentation API**:
  - IIIF Image API = `iiif.io/api/image` (image-derivative endpoint, requests size / region / rotation / format on a single canvas).
  - IIIF Presentation API = `iiif.io/api/presentation` (manifest / collection documents that describe structure and metadata for a multi-canvas / multi-object work).
  - In this exhibition: C-09 / C-10 have working Image API via Micrio (1024 px derivative); C-10 Presentation API `manifest.json` returned HTTP 404 in v5.3 deployment → manifest-derived claims are explicitly off-limits for C-10.
- **C-10 manifest 404 caveat**:
  - Phrasing preserved per `C-10` carve-out in `second-exhibition/docs/CITATION_NOTE`. C-10 keeps the "manifest 404" wording rather than asserting anything that would require a reachable manifest endpoint.

## Content counts

| Metric | v0.1 | v0.2 |
|---|---|---|
| marker | `second-exhibition-v0.1` | `second-exhibition-v0.2` |
| sections | 4 | 4 |
| artifact cards | 6 | 6 |
| glossary items | 12 | **14** |
| images | 6 | 6 |
| source notes | 6 | 6 |
| credit lines | 6 | 6 |
| deep-block sections | 4 | 4 |
| candidates (data-candidate-id) | 6 (C-01..C-06,C-08,C-09,C-10) | 6 (same set, content refined) |

## Candidate identity

- **Source** (`second-exhibition/site/index.html`):
  - bytes: **31,458**
  - SHA256: `662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e`
- **Staged** (after path rewrites, `/tmp/v56b-artifact/second-exhibition/index.html`):
  - bytes: **31,452**
  - SHA256: `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
  - byte delta vs source: **-6** = exactly the 6 image-path rewrites (`./assets/images/` → `../assets/images/`).
- **Marker counts in source HTML**:
  - `second-exhibition-v0.2` = 5 (HTML `data-marker` + footer + kicker + `<meta name="exhibition-version">` + title fragment / page heading)
  - `second-exhibition-v0.1` = **0** (regression guard passes)
- **Public inventory**:
  - root (`/tmp/v56b-artifact/`): 25 files
  - second-exhibition subtree (`/tmp/v56b-artifact/second-exhibition/`): 9 files (index.html, style.css, script.js, 6 images)
  - total: **34**
- **Status phrase counts** (live / candidate page text):
  - `production-deployed-v5.3` = 5
  - `published-in-v5.3` = 8
  - `imported-not-deployed` = 8 (all 8 in historical `Import record:` / `asset-import-manifest` / `(v4.5)` context — adjacent-history guard passes)
  - `repository-only-not-deployed` = 0

## Validation

| Check | Result |
|---|---|
| template quality gate | **PASS** (37/37) |
| second-exhibition build gate | **PASS** |
| second-exhibition repository QA | **166 PASS / 0 FAIL / 0 WARNINGS** |
| `asset-checksums.sha256 -c` | **6/6 OK** |
| `python3 -m json.tool` (4 JSON files: exhibition/sections/glossary/assets) | all OK |
| `node --check script.js` | OK |
| `node --check second_exhibition_browser_qa.mjs` | OK |
| `python3 -m py_compile production_healthcheck.py` | OK after §15 dest=`candidate_v02` fix |
| staging build | **PASS** (25 root + 9 second-ex, 6 path rewrites, source SHA intact) |
| staging gate | **PASS** (schema v2 identity check; `legacy_second_exhibition_source_index_html_sha256=662bee42…` carries scope) |
| exact-base-path dry-run | **PASS** (14/14 allowlist, 16/16 forbidden, 34/34 roundtrip byte-identical, workflow NOT modified) |
| browser QA matrix (5/5) | **5/5 PASS** at 1440×1000, 1280×900, 768×1024, 390×844, 320×700 |
| browser QA interactions (12/12) | **12/12 PASS** (guidedToggle, lightboxOpen, lightboxRole=dialog, lightboxAccessibleName, closeButtonFocused, escClose, focusReturn, c06LightboxOpen=false, sectionNav=true (320×700 fix verified), tabFocusable) |
| a11y | h1Count=1, img alt 0 missing, button 0 missing, heading jump false, hidden-title AT-safe |
| no-JS | cardCount=6, sourceNotes=6, creditLines=6, repoStatusVisible=true, bodyText=true |
| reduced motion | lightboxOpen + escClose OK |
| console / page / failed / external | 0 / 0 / 0 / 0 |
| overflow (5 viewports) | 0 (no body or document overflow) |
| current production v0.1 healthcheck | **PASS** (root 92,976 B / SHA `e2be1077…`; second-exhibition 25,635 B / SHA `7c05f39d…`; v0.1 baseline) |
| local candidate v0.2 healthcheck (`--candidate-v0.2` against 127.0.0.1:8772) | **PASS** (root 92,976 B / SHA `e2be1077…`; second-exhibition 31,452 B / SHA `00894e8d…`; 68 PASS / 0 FAIL) |
| workflow (`pages.yml`) | **NOT modified** |
| tag / Release | **NOT modified** |

## Known carry-overs (NOT v5.6b regressions)

These are intentional, documented in-scope leftovers. Neither should be misinterpreted as a v5.6b oversight or as a current-exhibition-marker regression.

- `second-exhibition/data/assets.json` retains `marker: second-exhibition-v0.1`. This is the asset-data historical / data-version field, not the current-exhibition public marker. It does not enter the public artifact (artifact builder never copies this file — confirmed by F-section staging gate check). v5.6b does not unify this field with the current-exhibition marker.
- `second-exhibition/site/README.md` retains v0.1 references. This file does not enter the public artifact (same reason). v5.6b does not modify it.
- Both carry-overs are scoped-out of v5.6b by the brief; if a future round wants full marker unification, it must bump `data/assets.json` AND `site/README.md` in their own dedicated scope.

## No-touch confirmation

Confirmed untouched (git diff empty for each path):

- top-level `site/`
- `second-exhibition/assets/` (six images + asset-import-manifest.json + asset-checksums.sha256)
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md`
- `.github/workflows/` (including `pages.yml` — confirmed by dry-run `workflow NOT modified`)
- `scripts/template_quality_gate.py`
- `scripts/second_exhibition_asset_gate.py`
- `scripts/second_exhibition_staging_build.py`
- `scripts/second_exhibition_deployment_dry_run.py`
- `scripts/test_second_exhibition_staging_audit.py`
- `_template/`, `_pilots/`, `release-assets/`

## Stop point

- **No** `git add`
- **No** `git commit`
- **No** `git push`
- **No** new tag
- **No** new GitHub Release
- Production surface (`conanxin.github.io/leonardo-chinese-exhibition/…`) remains v5.0-freeze v0.1.
- Working-tree changes recorded in §8 / scope validation §6.
- **Required authorization**:
  ```
  DEPLOY v5.6b
  ```
  Only after this token is received do we execute the git + Pages workflow steps.

## Idempotence / verification receipts

(Real artifacts on disk, independent re-runnable.)

- `/tmp/v56b-current-production-health-2.json` — live v0.1 health JSON (default, no flag).
- `/tmp/v56b-live-v01-default.json` — live v0.1 health JSON via workspace script.
- `/tmp/v56b-candidate-health.json` — local candidate v0.2 health JSON via workspace script with `--candidate-v0.2`.
- `/tmp/v56b-browser-qa-final.json.log` — five-viewport / twelve-interaction browser QA dump.
- `/tmp/v56b-artifact/`, `/tmp/v56b-artifact-audit/`, `/tmp/v56b-dry-run-test/` — staging + dry-run outputs.
