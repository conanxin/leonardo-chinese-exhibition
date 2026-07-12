# v5.6 Second Exhibition Content Iteration Prep — Report

## STATUS

**PASS** — five planning documents produced (`content audit`,
`fact-check matrix`, `iteration plan`, `changeset draft`,
`acceptance criteria`); no production content, page, data, image,
asset-manifest, checksum, source-evidence, workflow, tag, or
Release was modified in this round. The post-push verification
confirms zero production drift against the v5.0 freeze at
`ac0f19e2…`. v0.2 implementation awaits an explicit
`IMPLEMENT v5.6b` directive.

## Baseline

| Field                                       | Value |
|---|---|
| baseline HEAD                               | `ce01f1d8e37478c27cce7c6eb81f1c77ceb3739c` |
| baseline origin/main                        | same |
| stable tag                                  | `v5.0-real-second-exhibition-deployment` |
| stable tag object                           | `c8871f09e4003675d5796c76058d589a08541f45` |
| stable tag target                           | `ac0f19e2c03b09738ae49b4a15c629a1f2177068` |
| Release v5.0                                | `isDraft:false`, `isPrerelease:false`, `publishedAt: 2026-07-12T00:29:43Z` |
| production root                             | `https://conanxin.github.io/leonardo-chinese-exhibition/` |
| production second-exhibition                | `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` |
| canonical root SHA-256 (freeze)             | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| canonical second-exhibition source SHA-256  | `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda` |
| canonical second-exhibition staged/live SHA | `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c` |
| staging audit schema                        | `2.0` (canonical), `audit_schema_version` (deprecated alias) |
| image checksums                             | 6/6 OK |
| template gate                               | PASS 37/37 |
| build gate                                  | PASS |
| repository QA                               | PASS 164/164 |
| production healthcheck                      | PASS 68/73 final_ok=True |
| browser QA live                             | 5/5 viewports PASS |

## Content snapshot (frozen at HEAD `ce01f1d…`)

| Metric                              | Value |
|---|---|
| Title                               | 《植物图谱与视觉分类：从自然史图像到知识秩序》 |
| Subtitle                            | 从自然史图像到知识秩序 |
| HTML source bytes                   | 25,641 |
| Stripped prose chars                | 8,755 |
| Hero region bytes                   | 1,331 |
| Section count                       | 4 (观察 / 分类 / 复制 / 再组织) |
| Deep blocks                         | 4 (visual-thinking / material-evidence × 2 / research-model) |
| Artifact cards                      | 6 (C-01, C-03, C-06, C-08, C-09, C-10) |
| Glossary entries                    | 12 |
| Public images                       | 6 |
| Status phrase counts (live)         | `production-deployed-v5.3` = 5 · `published-in-v5.3` = 8 · `imported-not-deployed` = 8 · `repository-only-not-deployed` = 0 |
| Asset publication status (current)  | `published-in-v5.3` |
| Asset import status (historical)    | `imported-not-deployed` |

## Issues by severity / type

| Severity | Count | IDs |
|---|---:|---|
| blocker | 0 | — |
| high     | **1** | I-01 |
| medium   | **9** | I-02, I-03, I-05, I-06, I-07, I-08, I-09, I-10, I-11 |
| low      | **4** | I-12, I-13, I-14, I-15 |
| **Total**|  **15** | |

Type breakdown (one finding can be more than one type; primary
type shown):

| Type                       | Count |
|---|---:|
| factual                    | 1 (I-01) |
| terminology                | 4 (I-02, I-03, I-07, I-08) |
| narrative                  | 3 (I-06, I-09, I-12) |
| source-boundary            | 2 (I-05, I-14) |
| visitor comprehension      | 1 (I-10) |
| accessibility              | 1 (I-11) |
| repetition                 | 1 (I-15) |
| metadata                   | 1 (I-13) |

## Factual findings

- **F-17 / I-01 (high)**: `glossary-herbarium` includes
  "Rijksprentenkabinet 都属于此类机构" — Rijksprentenkabinet is
  the Rijksmuseum's print room (works on paper), **not** a herbarium.
  Blocker for v0.2.
- **F-18 / I-02 (medium)**: `glossary-print` lumps cyanotype with
  non-photographic print media; cyanotype is a photographic photogram.
  Recommended v0.2 (via `glossary-cyanotype` + cross-link).
- **F-19 / I-05 (medium)**: `glossary-public-domain` doesn't
  distinguish the **legal status** "public domain" from the
  **license instrument** "CC0 1.0". Recommended v0.2.
- **F-15 / I-04 (medium)**: `glossary-iiif` does not surface the
  Image API vs. Presentation API distinction explicitly enough; the
  manifest-404 caveat is not scoped to C-10. Recommended v0.2.

## Terminology findings

- **I-03 (medium)**: missing `glossary-cyanotype` and
  `glossary-photogram` entries.
- **I-07 / F-27 (medium)**: Section 2 bundles "NMNH Botany 馆藏的
  Aconitum bulbilliferum 与 Botanical Specimen: Fern 为对照样本" —
  these are different institutional categories
  (herbarium specimen vs. object record).
- **I-08 / F-13 (medium)**: Section 3 doesn't cue "Rijksprentenkabinet
  = print room"; cyanotype described but not anchored as photogram.

## Narrative findings

- **I-06 (medium)**: Section 1 doesn't surface the gap between
  watercolour-on-paper (drawn) and herbarium specimen (preserved).
- **I-09 / F-26 (medium)**: Section 4 stays abstract — pair each
  noun with a concrete identifier / rights / IIIF example.
- **I-12 (low)**: "Asset Cards" block appears *after* all 4 sections;
  optional move.

## Proposed v0.2 scope

| Field | Value |
|---|---|
| Sections | 4 (unchanged) |
| Artifact cards | 6 (unchanged) |
| Public images | 6 (unchanged) |
| Glossary count | 12 → **14** (+ `glossary-cyanotype`, `glossary-photogram`) |
| URL | unchanged |
| Status model | unchanged |
| Source-evidence files (`SOURCE_AUDIT_MANIFEST.md`, `RIGHTS_AND_SOURCES.md`) | unchanged |
| Asset manifest + checksums | unchanged |
| Public inventory | unchanged |
| `marker` | bumped to `second-exhibition-v0.2` |

## Planned modified files (next round, pending `IMPLEMENT v5.6b`)

| Path | Type of edit |
|---|---|
| `second-exhibition/site/index.html` | CHG-09 (hero), CHG-10 (3-min guide) |
| `second-exhibition/data/exhibition.json` | CHG-13 (`version`, `marker`) |
| `second-exhibition/data/sections.json` | CHG-02 / 03 / 04 / 05 (body), CHG-11 (deep-block prompt) |
| `second-exhibition/data/glossary.json` | CHG-01 / 06 / 07 / 08 (definitions), CHG-12 (add cyanotype, photogram) |
| `second-exhibition/data/assets.json` | no required edits this round |
| `second-exhibition/docs/VISITOR_GUIDE_ZH.md` | CHG-14 |
| `second-exhibition/docs/CURATORIAL_ESSAY_ZH.md` | CHG-14 |
| `second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md` | CHG-14 |
| `second-exhibition/docs/BUILD_ASSET_USAGE.md` | CHG-14 |
| `docs/V5_ROADMAP.md`, `README.md`, `reports/...` | CHG-15 |

## Asset / checksum / source / workflow / production unchanged?

| Surface | Changed? |
|---|---|
| Six image files (`second-exhibition/assets/images/*`) | **NO** |
| `second-exhibition/assets/asset-import-manifest.json` | **NO** |
| `second-exhibition/assets/asset-checksums.sha256` | **NO** |
| `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` | **NO** |
| `second-exhibition/docs/RIGHTS_AND_SOURCES.md` | **NO** |
| `.github/workflows/` | **NO** |
| `scripts/` | **NO** |
| `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/` | **NO** |
| Old tags / old Releases | **NO** |
| Public production content | **NO** (post-push verified) |

## Modified files in this prep round

| Path | Status |
|---|---|
| `docs/SECOND_EXHIBITION_CONTENT_AUDIT_v5.6.md` | new |
| `docs/SECOND_EXHIBITION_FACT_CHECK_MATRIX_v5.6.md` | new |
| `docs/SECOND_EXHIBITION_CONTENT_ITERATION_PLAN_v5.6.md` | new |
| `docs/SECOND_EXHIBITION_CONTENT_CHANGESET_DRAFT_v5.6.md` | new |
| `docs/SECOND_EXHIBITION_CONTENT_ACCEPTANCE_CRITERIA_v5.6.md` | new |
| `docs/V5_ROADMAP.md` | modified (one new section + link trail) |
| `README.md` | modified (one new section + link trail) |
| `reports/leonardo_chinese_exhibition_v5_6_content_iteration_prep_report.md` | new (this file) |

## Post-push verification (post-push of this prep round)

- Live root SHA = `e2be1077…` (canonical, freeze holds)
- Live second-exhibition bytes = 25,635; SHA = `7c05f39d…`
  (canonical, freeze holds)
- Six image checksums: 6/6 OK
- Status-phrase counts:
  `production-deployed-v5.3 = 5`,
  `published-in-v5.3 = 8`,
  `imported-not-deployed = 8`,
  `repository-only-not-deployed = 0`
  (all four unchanged)
- Tag still pinned to `ac0f19e2…`
- Release v5.0 still `isDraft:false`, `isPrerelease:false`
- Healthcheck PASS 68/73, `final_ok=True`

## Next

The next round is gated. The operator must send an explicit
`IMPLEMENT v5.6b` directive before the v0.2 implementation can begin.
At that point the implementation must follow:

1. The exact CHG-01 … CHG-15 changeset rows from
   `docs/SECOND_EXHIBITION_CONTENT_CHANGESET_DRAFT_v5.6.md`.
2. The acceptance gate from
   `docs/SECOND_EXHIBITION_CONTENT_ACCEPTANCE_CRITERIA_v5.6.md`.

Without that authorization, no production content is touched.
