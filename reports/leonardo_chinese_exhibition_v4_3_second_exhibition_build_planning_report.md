# v4.3 Second Exhibition Build Planning — Report

> Round: **v4.3 — Second Exhibition Build Planning**
> Date: 2026-07-09 (UTC)
> Working title: 《植物图谱与视觉分类：从自然史图像到知识秩序》
> **STATUS: PASS**

---

## 1. Round summary

| Field | Value |
|---|---|
| **STATUS** | **PASS** |
| Round | v4.3 — Second Exhibition Build Planning |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Source tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Baseline HEAD | `b6738f525d211c453ac174e4091808980a5a9a77` |
| `origin/main` at round start | `b6738f525d211c453ac174e4091808980a5a9a77` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (before) | 92,976 B |
| Live byte size (after) | 92,976 B |
| Live byte size delta | **0 B** |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v2.9 marker in live | `1` (unchanged) |
| `image-placeholder-pro` in live | `0` (unchanged) |
| `植物图谱与视觉分类` in live | `0` (unchanged — planning round, not deployed) |
| `script.js` HTTP status | `200` |
| Working tree | clean except for untracked `.firecrawl/` (left alone this round, per scope) |
| New tag | **none** (v4.3 is a planning round) |
| New GitHub Release | **none** |
| Approved asset count | **0** (status `approved` is not used in v4.3) |
| Downloaded image count | **0** |

---

## 2. Reality gate result (round start)

| Check | Expected | Actual | Result |
|---|---|---|---|
| HEAD = `origin/main` | `b6738f5` | `b6738f5` | PASS |
| v3.4 tag object | `2d186a89` | `2d186a89` | PASS |
| v3.4 tag target | `81f5e92` | `81f5e92` | PASS |
| Quality gate | 37/37 PASS | 37/37 PASS | PASS |
| 5 v4.2 docs exist | all 5 | all 5 | PASS |
| Live byte size | 92,976 B | 92,976 B | PASS |
| v2.9 marker in live | 1 | 1 | PASS |
| `image-placeholder-pro` in live | 0 | 0 | PASS |
| `植物图谱与视觉分类` in live | 0 | 0 | PASS |
| `script.js` HTTP status | 200 | 200 | PASS |
| Working tree | clean (untracked `.firecrawl/` ok) | matches | PASS |

Reality gate **PASS**. Round proceeded.

---

## 3. v4.2 source count

| v4.2 status | Count | IDs |
|---|---|---|
| `verified` | 6 | C-01, C-03, C-06, C-08, C-09, C-10 |
| `needs clarification` | 6 | C-04, C-05, C-07, C-11, C-12, C-13 |
| `blocked` (at row level) | 0 | — |
| `excluded` (at row level) | 0 in the 12-row shortlist | — |

The build planning threshold (verified ≥ 4) is met: 6 ≥ 4. v4.3 may proceed.

---

## 4. v4.3 candidate selection

The 6 v4.2 verified candidates enter v4.3 selection. The v4.3 status counts are:

| v4.3 status | Count | IDs |
|---|---|---|
| `selected-for-build-planning` | **6** | C-01, C-03 (PD subset only), C-06, C-08 (alt), C-09, C-10 |
| `defer` | **6** | C-04, C-05, C-07, C-11, C-12, C-13 |
| `replace-with-project-generated-diagram` | **2** | C-02 (BHL Flickr), Section-4 screenshot row |
| `blocked-from-build` | **1** | C-14 (BHL in-copyright CC BY-NC-SA), **and the C-03 CC BY-NC-SA subset is blocked at the per-item level** |
| `approved` | **0** | Status `approved` is not used in v4.3 or any future round. |

**Selected-for-build-planning count: 6** (≥ 4 threshold). Approved asset count: 0. Downloaded image count: 0.

---

## 5. v4.3 docs created (5)

| File | Bytes | Purpose |
|---|---|---|
| `docs/SECOND_EXHIBITION_BUILD_PLAN_v4.3.md` | ~15.0 KB | Candidate selection + minimum build set + section coverage + non-goals. |
| `docs/ITEM_EVIDENCE_DOSSIER_v4.3.md` | ~18.7 KB | 6 per-candidate evidence plans (one per `selected-for-build-planning` row): institution, source URL, rights URL / statement, identifier, title / creator / date, proposed section / use, credit line basis, source note draft, rights note draft, remaining caution, future asset import status (not downloaded). |
| `docs/BUILD_SCOPE_v4.3.md` | ~10.2 KB | Section scope (4 sections, each with purpose, primary candidate, fallback diagram, evidence status, rights caution, writing tasks) + page structure. |
| `docs/CONTENT_DRAFT_BRIEF_v4.3.md` | ~11.4 KB | Tone + hero draft (186 Chinese characters) + 3-minute guide draft (5 points) + section briefs + artifact card writing brief (6 cards, one per selected candidate). |
| `docs/ASSET_IMPORT_PLAN_v4.3.md` | ~12.1 KB | 11-step import rule + planned asset import table (6 rows) + file naming convention + pre-import action summary. |
| `docs/V4_ROADMAP.md` | updated | v4.3 section added (Second Exhibition Build Planning) before the existing v4.3 Second Exhibition Build placeholder. |
| `README.md` | updated | `v4.3 Second Exhibition Build Planning` block added after the v4.2 block. |

Grep verification of acceptance phrases:

| Check | Count |
|---|---|
| `selected-for-build-planning` in `SECOND_EXHIBITION_BUILD_PLAN_v4.3.md` | 13 |
| `not downloaded` in `ITEM_EVIDENCE_DOSSIER_v4.3.md` | 8 |
| `本轮不下载图片` in `ASSET_IMPORT_PLAN_v4.3.md` | 1 |
| `CC BY-NC-SA subset blocked` in `SECOND_EXHIBITION_BUILD_PLAN_v4.3.md` | 1 |
| `approved` as a v4.3 status value in the build plan | **0** |

---

## 6. Build scope summary

| Section | Primary candidate | Alternate candidate | Fallback diagram |
|---|---|---|---|
| Section 1 (观察) | C-01 (BHL PD plate) | C-09 (Rijksmuseum) | Comparison-of-two-editions diagram |
| Section 2 (分类) | C-06 (Smithsonian NMNH CC0) | C-09 (Rijksmuseum) | Comparison of two related species, side-by-side |
| Section 3 (复制) | C-03 (BHL PD book page, PD subset only) | C-08 (Met CC0) | Reproduction-chain diagram |
| Section 4 (再组织) | C-10 (Rijksmuseum IIIF manifest) | — | Network diagram (one species connected across records) |

**Section coverage.** Each section has at least one primary candidate and at least one fallback. C-09 is a cross-section alternate (Section 1 + Section 2). C-08 is a Section 3 alternate.

**Real-image count in build set.** 4 primary + 2 alternates (C-08 alt, C-09 cross-section) = 6 selected-for-build-planning rows. None downloaded in v4.3.

**Project-generated diagram count.** 4 (one per section) + 2 v4.1 carry-overs (C-02 BHL Flickr, Section-4 screenshot row) = 6 project-generated entries. None drawn in v4.3.

**Total planned content units.** 6 selected real images + 6 project-generated diagrams = **12** content units. The v4.0 MVE requires 4 sections + 4–6 artifact cards + 6–10 glossary terms; the build set covers all four.

---

## 7. Item evidence dossier summary

The dossier has 6 entries, one per `selected-for-build-planning` candidate. Each entry has:

- Institution
- Source URL
- Rights URL / statement (verbatim)
- Identifier type (per-item ID captured at v4.4)
- Title / Creator / Date (TBD at v4.4)
- Proposed section
- Proposed use
- Credit line basis
- Source note draft
- Rights note draft
- Remaining caution
- **Future asset import status: not downloaded.**

The status `approved` does not appear. The phrase "safe for commercial use" does not appear. Per-item selection is a v4.4 step.

---

## 8. Asset import plan summary

The asset import plan records the 11-step import rule, the planned asset import table (6 rows), the file naming convention, and the pre-import action summary.

**The 11-step import rule** (must be executed in order at v4.4): re-open source URL → re-check rights statement → record identifier → record source URL → record image URL / IIIF URL → write credit line → write source note → save local file path → update source audit manifest → run quality gate → confirm no live change unless deployment round.

**Planned asset import table** (6 rows, all `not downloaded`):

- C-01 → `bhl-<title_id>-<item_id>-plate.jpg` · CC BY-NC-SA subset blocked.
- C-03 → `bhl-<title_id>-<page_id>-page.jpg` · **PD subset only**.
- C-06 → `smithsonian-nmnh-<accession_number>.jpg` · CC0 (mandatory accession number in credit line).
- C-08 → `met-<object_id>.jpg` · CC0 with double-confirmation.
- C-09 → `rijksmuseum-<object_number>.jpg` · CC0 (or CC BY 4.0 with attribution).
- C-10 → `rijksmuseum-<object_number>-iiif.json` · CC0 (or CC BY 4.0 with attribution); the manifest is JSON, the image is a separate download.

**File naming convention.** lowercase · institution prefix · short identifier · no spaces · extension preserved.

**Import status counts.**

- `not downloaded`: **6** (all 6 v4.3 `selected-for-build-planning` rows).
- `wait for v4.4 asset import`: **6** (same rows; v4.3 records the *plan*; v4.4 executes it).
- `replace with project-generated diagram`: **0** in the build set (the fallbacks are *fallback*, not import).
- `approved`: **0** (not used).

---

## 9. README / roadmap update

- `README.md` now carries a `## v4.3 Second Exhibition Build Planning` block immediately after the v4.2 block, recording: status (build planning only), 6 verified candidates used, no live change, no images downloaded, no assets approved, the v4.3 status counts (6 selected-for-build-planning / 6 defer / 2 replace-with-project-generated-diagram / 1 blocked-from-build), the C-03 CC BY-NC-SA subset blocked caution, the section coverage, the 5 v4.3 docs, the quality gate result, and the next task (v4.4 — Asset Import Prep).
- `docs/V4_ROADMAP.md` v4.3 section added (Second Exhibition Build Planning) before the existing v4.3 Second Exhibition Build placeholder, with the full goal / tasks / deliverables / do-not-do / exit-criteria / next-round text. The existing v4.3 Second Exhibition Build placeholder is preserved (it is a future round; the v4.3 Build Planning is the *current* round).

No prior v2.x / v3.x / v4.0 / v4.1 / v4.2 section was modified.

---

## 10. Live site no-change confirmation

| Check | Before | After | Delta |
|---|---|---|---|
| Live byte size | 92,976 B | 92,976 B | 0 |
| v2.9 marker in live | 1 | 1 | 0 |
| `image-placeholder-pro` in live | 0 | 0 | 0 |
| `植物图谱与视觉分类` in live | 0 | 0 | 0 (planning round, not deployed) |
| `script.js` HTTP status | 200 | 200 | — |
| `git diff -- site/index.html site/style.css site/script.js` | — | empty | — |

Live site **unchanged**.

---

## 11. Template / pilot no-change confirmation

| Check | Result |
|---|---|
| `git diff -- _template/site/` | empty |
| `git diff -- _template/data/` | empty |
| `git diff -- _pilots/second-exhibition-pilot/` | empty |
| `scripts/template_quality_gate.py` | PASS 37/37 |

Template and pilot **unchanged**.

---

## 12. Old tags / old releases untouched

| Check | Result |
|---|---|
| `git tag --list` | v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1 / v3.2 / v3.3 / v3.4 — **all 10 unchanged** |
| `git ls-remote --tags origin` | matches local list — no remote-side movement |
| v3.4 tag object | `2d186a89` (unchanged) |
| v3.4 tag target | `81f5e92` (unchanged) |
| Old GitHub Releases | **none modified** (no `gh release edit` issued) |
| `posts/` | not touched (not in this round's allowed-edit list) |
| `case-study/` | not touched (not in this round's allowed-edit list) |
| `release-assets/` | not touched (not in this round's allowed-edit list) |

No tag, no Release, no movement, no rewrite. Old history **untouched**.

---

## 13. Files changed in this round

Allowed-edit list (per round scope) — all changed files fall inside this list:

| File | Action |
|---|---|
| `docs/SECOND_EXHIBITION_BUILD_PLAN_v4.3.md` | created |
| `docs/ITEM_EVIDENCE_DOSSIER_v4.3.md` | created |
| `docs/BUILD_SCOPE_v4.3.md` | created |
| `docs/CONTENT_DRAFT_BRIEF_v4.3.md` | created |
| `docs/ASSET_IMPORT_PLAN_v4.3.md` | created |
| `docs/V4_ROADMAP.md` | modified (v4.3 Build Planning section added) |
| `README.md` | modified (v4.3 block added) |
| `reports/leonardo_chinese_exhibition_v4_3_second_exhibition_build_planning_report.md` | created (this file) |

Untracked `.firecrawl/` directory was observed at round start and **left alone**, per round scope.

---

## 14. Next recommended task

**v4.4 — Asset Import Prep.**

Scope of v4.4:

- For each of the 6 `selected-for-build-planning` rows, pick one specific item that passes the 5 source-acceptance checks.
- For C-01 / C-03 (BHL): filter on `<Copyright Status> = Public domain` only. The CC BY-NC-SA subset is rejected at the per-item check.
- For C-06 (Smithsonian NMNH): confirm the CC0 icon; capture the accession number; capture the image URL.
- For C-08 (Met): run the double-confirmation (`isPublicDomain: true` in the Collection API + Open Access icon on the public object page). If either is missing, the row is rejected and the Section 3 alternate slot is filled by a project-generated diagram.
- For C-09 / C-10 (Rijksmuseum): capture the per-item `licence` field exactly.
- Re-open the source URL on the day of import. The previous visit may be days or weeks old.
- Record all 11 import-rule fields per the asset import plan.
- Write the local file with the v4.3 file naming convention.
- Update the source audit manifest.
- Run `template_quality_gate.py`.
- Confirm no live change unless deployment round.

v4.4 **must not**:

- Mark any candidate `approved`.
- Re-introduce any `needs clarification` candidate as `selected-for-build-planning`.
- Re-introduce the v4.1 `excluded` row (C-14) as `selected-for-build-planning`.
- Modify `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`.
- Create a tag or GitHub Release.
- Move or rewrite any pre-existing tag or GitHub Release.
- Process the untracked `.firecrawl/` directory.

v4.4 **must** keep the live byte size at 92,976 B and the v2.9 marker at 1.

---

## 15. Final status

**STATUS: PASS**

All reality-gate, candidate-selection, evidence-dossier, build-scope, content-draft-brief, asset-import-plan, README / roadmap, quality-gate, no-change, no-new-image, and old-history conditions met. v4.3 closes with five committed planning docs, two updated existing docs, an unchanged live site (92,976 B / v2.9 marker = 1 / placeholder = 0), an unchanged template and pilot, no new image files in the repository, 6 `selected-for-build-planning` rows (≥ 4 threshold), 6 `defer` rows, 2 `replace-with-project-generated-diagram` rows, 1 `blocked-from-build` row (plus the C-03 CC BY-NC-SA subset blocked at the per-item level), 0 approved, 0 downloaded, and ten untouched old tags plus their corresponding old GitHub Releases. No new tag, no new GitHub Release. The next round is **v4.4 — Asset Import Prep**.