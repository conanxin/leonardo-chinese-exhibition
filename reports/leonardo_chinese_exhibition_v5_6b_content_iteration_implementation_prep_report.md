---
schema_version: v5.6b
report_type: prep
round: leonardo-chinese-exhibition / v5.6b / second-exhibition v0.2 content iteration implementation prep
---

# v5.6b Second Exhibition v0.2 Content Iteration Implementation — Prep Report

## STATUS

**READY_FOR_MANUAL_DEPLOY_APPROVAL**

> Production is unchanged. Working tree holds CHG-01…15 + 4 scroll-margin-top inline styles + this round's documentation only. No commit, no push, no tag, no Release. Authorization required: `DEPLOY v5.6b`.

## Baseline

| Field | Value |
|---|---|
| Baseline HEAD | `5edc9fdc149bea2ac60a67a1244e24bae4f819b8` |
| baseline origin/main | `5edc9fdc149bea2ac60a67a1244e24bae4f819b8` |
| Stable tag | `v5.0-real-second-exhibition-deployment` (annotated, object `c8871f09…`, target `ac0f19e2c03b09738ae49b4a15c629a1f2177068`) |
| Stable Release | v5.0 GitHub Release (unchanged) |
| Current production | second-exhibition **v0.1** (live) |
| Live root identity | 92,976 B / SHA `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| Live second-exhibition identity | 25,635 B / SHA `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c` |

## Exact modified files

| File | additions | deletions |
|---|---|---|
| scripts/second_exhibition_build_gate.py | 8 | 5 |
| scripts/second_exhibition_production_healthcheck.py | 39 | 5 |
| scripts/second_exhibition_repository_qa.py | 14 | 4 |
| second-exhibition/data/exhibition.json | 10 | 5 |
| second-exhibition/data/glossary.json | 66 | 18 |
| second-exhibition/data/sections.json | 27 | 11 |
| second-exhibition/docs/BUILD_ASSET_USAGE.md | 6 | 6 |
| second-exhibition/docs/CURATORIAL_ESSAY_ZH.md | 1 | 1 |
| second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md | 2 | 1 |
| second-exhibition/docs/VISITOR_GUIDE_ZH.md | 7 | 7 |
| second-exhibition/site/index.html | 37 | 25 |
| docs/SECOND_EXHIBITION_CONTENT_ITERATION_IMPLEMENTATION_v5.6b.md | new | — |
| reports/leonardo_chinese_exhibition_v5_6b_content_iteration_implementation_prep_report.md | new | — |
| docs/V5_ROADMAP.md | (incremental add) | — |
| README.md | (incremental add) | — |
| **Total changes** | **217 + new docs** | **88** |

Total tracked modifications = **11 modified + 4 new** = 15 files, all in-scope per brief §11.

`scripts/second_exhibition_staging_gate.py` and `scripts/second_exhibition_browser_qa.mjs` were NOT modified (verified by `git diff --name-status` — neither listed). This is consistent with v5.5b+v5.6a design: staging gate only checks SHA identity (marker-agnostic), browser QA only requires HTML invariants (no marker constants).

## CHG-01 to CHG-15 completion

- CHG-01 — Rijksprentenkabinet / herbarium disambiguation: **DONE** (data + page).
- CHG-02 — Section 1 watercolour vs specimen disambiguation: **DONE**.
- CHG-03 — Section 2 NMNH herbarium vs Met institutional record: **DONE**.
- CHG-04 — Section 3 print-room + 4-medium + cyanotype photogram: **DONE**.
- CHG-05 — Section 4 identifier / rights / IIIF concrete examples: **DONE**.
- CHG-06 — cyanotype (blueprint process) gloss: **DONE** (glossary + page div).
- CHG-07 — Public Domain vs CC0: **DONE** (glossary + page div + section 4).
- CHG-08 — IIIF Image API vs Presentation API: **DONE** (glossary + page div + section 3).
- CHG-09 — Hero core question rewrite: **DONE**.
- CHG-10 — 3-minute guide as viewing method: **DONE**.
- CHG-11 — Section 3 deep-block prompt variant: **DONE**.
- CHG-12 — glossary 12 → 14 (+ cyanotype + photogram): **DONE**.
- CHG-13 — marker v0.1 → v0.2 (5 HTML occurrences + exhibition.json + sections.json): **DONE**.
- CHG-14 — 4 content Markdown files sync (visitor guide, curatorial essay, deep-research notes, build-asset usage): **DONE**.
- CHG-15 — gates + production healthcheck sync (build + repo QA bidirectional v0.2 / v0.1 assertion; healthcheck `--candidate-v0.2` flag): **DONE**.

Additional v5.6b inline-only adjustment (documented in implementation doc, not a CHG row):
- 4 × `style="scroll-margin-top: 2px;"` on `<section id="section-N-…">` (320×700 sub-pixel section-nav fix; 128 source bytes added; verified by 5/5 browser QA after re-build).

## Factual blockers

**0.**

- Rijksprentenkabinet — herbarium confusion: corrected and validated against institution documentation + reproducible in `data/glossary.json`.
- NMNH vs Met institutional distinction: corrected.
- IIIF Image vs Presentation API: corrected and scoped per `C-10` carve-out (manifest 404 caveat preserved, no manifest-derived claims).

## Terminology blockers

**0.**

- cyanotype / photogram added (12 → 14).
- Public Domain / CC0 separated.
- IIIF Image API / Presentation API separated.
- C-10 manifest 404 wording preserved per `CITATION_NOTE`.

## Marker before / after

| | v0.1 | v0.2 candidate |
|---|---|---|
| Public marker (HTML) | `second-exhibition-v0.1` | `second-exhibition-v0.2` (5 occurrences) |
| `data/exhibition.json.version` | `second-exhibition-v0.1` | `second-exhibition-v0.2` |
| `data/sections.json.exhibition_version` | (legacy name) | `second-exhibition-v0.2` |

Stale `second-exhibition-v0.1` count in candidate `site/index.html` = **0** (regression guard passes).

## Glossary before / after

12 → **14** (+cyanotype, +photogram). Both new entries are wired into `data/glossary.json` items and into the page glossary `<div id="glossary-list">` rendering. The `image_src` / `image_alt` / `term_zh` / `term_en` / `body_zh` fields follow the existing item schema (verified by build_gate + repository QA).

## Candidate source identity

- bytes: **31,458**
- SHA256: `662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e`

## Candidate staged identity

- bytes: **31,452**
- SHA256: `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
- delta vs source: **-6 bytes** from exactly 6 path rewrites (`./assets/images/` → `../assets/images/`)

## Root identity (unchanged)

- 92,976 B / SHA `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` (source == staged, byte + SHA identical).

## Public inventory

- root: 25 files
- second-exhibition subtree: 9 files (index.html, style.css, script.js, 6 images)
- **total: 34**

## Asset / checksums

- 6/6 images SHA256 unchanged (verified by `sha256sum -c second-exhibition/assets/asset-checksums.sha256`).
- `asset-import-manifest.json` and `asset-checksums.sha256` themselves are untouched (git diff empty for both).

## Source / rights preservation

- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`: NOT modified.
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md`: NOT modified.
- All citation chains preserved (C-01..C-10 identifiers, source URLs, rights URLs unchanged).

## Gate results

| Gate | Result |
|---|---|
| `template_quality_gate` | PASS (37/37) |
| `second_exhibition_build_gate` | PASS (marker bidirectional assertion passes) |
| `second_exhibition_repository_qa` | **166 PASS / 0 FAIL / 0 WARNINGS** |
| `asset-checksums.sha256 -c` | 6/6 OK |
| 4 × `python3 -m json.tool` | OK (exhibition/sections/glossary/assets) |
| `node --check site/script.js` | OK |
| `node --check scripts/second_exhibition_browser_qa.mjs` | OK |
| `py_compile scripts/second_exhibition_production_healthcheck.py` | OK after `--candidate-v0.2` `dest="candidate_v02"` fix |

## Staging result

- `python3 scripts/second_exhibition_staging_build.py --output /tmp/v56b-artifact --audit /tmp/v56b-artifact-audit`: **PASS** (25 root + 9 second-ex, 6 path rewrites, source SHA preserved)
- `python3 scripts/second_exhibition_staging_gate.py --artifact /tmp/v56b-artifact --audit /tmp/v56b-artifact-audit`: **PASS** (schema v2; `legacy_second_exhibition_source_index_html_sha256=662bee42…` carries scope; artifact-files.txt + artifact-sha256.txt each 34 entries)

## Dry-run result

- `python3 scripts/second_exhibition_deployment_dry_run.py`: **PASS** (14/14 allowlist, 16/16 forbidden, 34/34 roundtrip byte-identical, tar 5,804,984 B, schema v2, workflow NOT modified, rollback-rehearsal semantics preserved).

## Browser viewport matrix

| Viewport | pass | overflow | page errors |
|---|---|---|---|
| 1440 × 1000 | ✅ | 0 | 0 |
| 1280 × 900 | ✅ | 0 | 0 |
| 768 × 1024 | ✅ | 0 | 0 |
| 390 × 844 | ✅ | 0 | 0 |
| 320 × 700 | ✅ | 0 | 0 |

## Console / page / request / external errors

- consoleErrors: **0**
- pageErrors: **0**
- failedRequests: **0**
- externalRequests: **0**

## Overflow

- horizontal overflow across all 5 viewports: **0**
- document overflow: 0 across all 5 viewports

## No-JS

- cardCount: 6, sourceNotes: 6, creditLines: 6, repoStatusVisible: true, bodyText present — all pass.

## Reduced motion

- lightboxOpen: true, escClose: true under `prefers-reduced-motion: reduce`.

## Current production v0.1 healthcheck

Worker: `/tmp/v56b-current-production-healthcheck.py` (saved at v5.6b start, identical to v5.5 freeze baseline):

- 73 checks / 68 PASS / 0 FAIL / 0 WARN / 5 INFO / 0 ENV-ERR — **PASS**
- Live root: 92,976 B (matches baseline)
- Live second-exhibition: 25,635 B (matches v5.0 freeze baseline)
- Forbidden paths: 17/17 = 404
- Tag `v5.0-real-second-exhibition-deployment` exists annotated, points at `ac0f19e2…`

Re-run on workspace script (no flag): **PASS, same numbers.**

JSON saved: `/tmp/v56b-live-v01-default.json`, `/tmp/v56b-current-production-health-2.json`.

## Candidate v0.2 local healthcheck

Worker: workspace `scripts/second_exhibition_production_healthcheck.py --candidate-v0.2 --root-url http://127.0.0.1:8772/leonardo-chinese-exhibition/ --second-url http://127.0.0.1:8772/leonardo-chinese-exhibition/second-exhibition/`:

- 73 checks / 68 PASS / 0 FAIL / 0 WARN / 5 INFO / 0 ENV-ERR — **PASS**
- Local root: 92,976 B (matches ROOT_EXPECTED_BYTES + ROOT_EXPECTED_SHA256)
- Local second-exhibition: **31,452 B / SHA `00894e8d…` (matches `SECOND_V02_CANDIDATE_BYTES/SHA256`)**
- root baseline unchanged; only second-exhibition baseline swapped via `--candidate-v0.2`

JSON saved: `/tmp/v56b-candidate-health.json`.

## Workflow unchanged

`git diff .github/workflows/` returns empty. Dry-run "workflow NOT modified" check passes.

## Tags / Releases unchanged

`git tag -l` shows `v5.0-real-second-exhibition-deployment` unchanged; no new tag created; no GitHub Release touched.

## Known carry-overs

- `second-exhibition/data/assets.json` keeps `marker: second-exhibition-v0.1` (asset-data historical field, NOT current-exhibition public marker; not copied into public artifact).
- `second-exhibition/site/README.md` keeps v0.1 references (NOT copied into public artifact).

Both are scope-bounded by brief §15; neither is a v5.6b regression.

## Rollback plan

If `DEPLOY v5.6b` triggers Pages workflow failure, rollback is two-stage:

1. **Workflow failure (build/gate)**: revert the working-tree commit(s) only on `main` — produced-against-HEAD = `5edc9fdc`. The deployment will fail closed (Pages does not promote a failed artifact).
2. **Production drift detected post-deploy**: revert the deployment commit and re-tag `v5.0-real-second-exhibition-deployment` per v5.3b+v5.5 runbook. v5.3b already documents the explicit revert pair for v5.3 wording; the symmetric revert to restore v5.3 production surface from v5.6b is described in `docs/INCIDENT_RESPONSE_AND_ROLLBACK_v5.5.md` (left untouched).

**Headroom for emergency live rollback**:
- Live v0.1 staging artifact is reproducible from any pre-v5.6b commit via `scripts/second_exhibition_staging_build.py` against the v5.0 freeze source bytes (`f31ddcba…`); no schema v0.2 data is needed for v0.1 reproduction.

## Working tree state

- HEAD / origin/main = `5edc9fdc…` (unchanged)
- tracked working tree modified files: **15** (11 modified + 4 new docs in this round)
- untracked: `.firecrawl/`
- 0 staged, 0 commits made this round, 0 pushes
- `git diff --check`: clean (no conflict markers)
- background http server (port 8772): **stopped** (proc `35571` killed; proc `proc_ebb679b88ad3` exited cleanly per system notice)

## Required authorization

```
DEPLOY v5.6b
```

Only this token moves the project past the stop point.
