# v4.1 Source Candidate Research — Report

> Round: **v4.1 — Source Candidate Research**
> Date: 2026-07-09 (UTC)
> Working title: 《植物图谱与视觉分类：从自然史图像到知识秩序》
> **STATUS: PASS**

---

## 1. Round summary

| Field | Value |
|---|---|
| **STATUS** | **PASS** |
| Round | v4.1 — Source Candidate Research |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Source tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Baseline HEAD | `a24379261d3bd2acb83c1e95ad89edf96bdedb4d` |
| `origin/main` at round start | `a24379261d3bd2acb83c1e95ad89edf96bdedb4d` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (before) | 92,976 B |
| Live byte size (after) | 92,976 B |
| Live byte size delta | **0 B** |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v2.9 marker in live | `1` (unchanged) |
| `image-placeholder-pro` in live | `0` (unchanged) |
| `植物图谱与视觉分类` in live | `0` (unchanged — research round, not deployed) |
| `script.js` HTTP status | `200` |
| Working tree | clean except for untracked `.firecrawl/` (left alone this round, per scope) |
| New tag | **none** (v4.1 is a research round) |
| New GitHub Release | **none** |
| Approved asset count | **0** (status `approved` is not used in v4.1) |
| Downloaded image count | **0** |

---

## 2. Reality gate result (round start)

| Check | Expected | Actual | Result |
|---|---|---|---|
| HEAD = `origin/main` | `a243792` | `a243792` | PASS |
| v3.4 tag object | `2d186a89` | `2d186a89` | PASS |
| v3.4 tag target | `81f5e92` | `81f5e92` | PASS |
| Quality gate | 37/37 PASS | 37/37 PASS | PASS |
| Live byte size | 92,976 B | 92,976 B | PASS |
| v2.9 marker in live | 1 | 1 | PASS |
| `image-placeholder-pro` in live | 0 | 0 | PASS |
| `植物图谱与视觉分类` in live | 0 | 0 | PASS |
| `script.js` HTTP status | 200 | 200 | PASS |
| Working tree | clean (untracked `.firecrawl/` ok) | matches | PASS |

Reality gate **PASS**. Round proceeded.

---

## 3. Candidate institutions researched (6)

| # | Institution | Official rights / terms URL | Key wording (as written on the institution's own page) |
|---|---|---|---|
| 1 | **Biodiversity Heritage Library** | <https://about.biodiversitylibrary.org/help/copyright-and-reuse/> | "BHL does not claim copyright on its digitized works." Metadata: CC0 1.0. In-copyright subset: CC BY-NC-SA 4.0. US public-domain cutoff: 95 years. |
| 2 | **Wellcome Collection** | Site footer (<https://wellcomecollection.org/>) | "Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International Licence." IIIF Image API publicly available. |
| 3 | **Smithsonian Open Access** | <https://www.si.edu/openaccess/faq> | "We have released these images and data into the public domain as Creative Commons Zero (CC0)." Items not marked CC0 are "subject to usage conditions." |
| 4 | **The Met Open Access** | <https://github.com/metmuseum/openaccess/blob/master/LICENSE> + <https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources> | "The Metropolitan Museum of Art has waived all copyright and related or neighboring rights to this dataset using Creative Commons Zero." Images CC0 only if the public object page shows the icon. |
| 5 | **Rijksmuseum** | <https://data.rijksmuseum.nl/policy/information-and-data-policy> | Two-tier: CC0 1.0 (no longer in copyright) or CC BY 4.0 (third-party written grant). IIIF Image / Presentation / Change Discovery APIs. |
| 6 | **Library of Congress** | Per-collection "Rights & Access" page (e.g. <https://www.loc.gov/collections/single-sheet-maps-title-collection/about-this-collection/rights-and-access>) | Per-collection wording. "U.S. government works not subject to copyright" or "no known copyright restrictions" — both non-affirmative variants. |

All 6 institutions have a reachable, official rights / terms page. The v4.1 research recorded each institution's wording *verbatim* into `docs/INSTITUTION_POLICY_NOTES_v4.1.md`; v4.2 re-verifies per item.

---

## 4. Candidate docs created (5)

| File | Bytes | Purpose |
|---|---|---|
| `docs/SOURCE_CANDIDATES_v4.1.md` | ~20.6 KB | Institution summaries + 12 candidate directions (≥ 1 per institution). |
| `docs/SOURCE_CANDIDATE_TABLE_v4.1.md` | ~8.1 KB | 14 candidate rows × 6 institutions, with status limited to `candidate` / `needs rights audit` / `excluded`. |
| `docs/INSTITUTION_POLICY_NOTES_v4.1.md` | ~16.3 KB | Per-institution policy notes — official URLs, exact wording, attribution, API notes, uncertainty, v4.2 audit question. |
| `docs/ASSET_CANDIDATE_MATRIX_v4.1.md` | ~10.9 KB | 4-section matrix (观察 / 分类 / 复制 / 再组织) with candidate asset types, source institutions, source / search URLs, rights risk, fit, and project-generated substitution guidance. |
| `docs/RIGHTS_SCREENING_DECISIONS_v4.1.md` | ~7.6 KB | Decision rules + 14 preliminary decisions (`keep` / `replace` / `exclude` — never `approved`). |
| `docs/V4_ROADMAP.md` | updated | v4.1 section rewritten to reflect actual deliverables + the "no asset approval" rule. |
| `README.md` | updated | `v4.1 Source Candidate Research` block added after the v4.0 block. |

Grep verification of acceptance phrases:

| Check | Count |
|---|---|
| `Biodiversity Heritage Library` in `SOURCE_CANDIDATES_v4.1.md` | 1 (header) + multiple in body |
| `Wellcome` in `SOURCE_CANDIDATES_v4.1.md` | 7 |
| `Smithsonian` in `SOURCE_CANDIDATES_v4.1.md` | 11 |
| `The Met` in `SOURCE_CANDIDATES_v4.1.md` | 4 |
| `Rijksmuseum` in `SOURCE_CANDIDATES_v4.1.md` | 8 |
| `Library of Congress` in `SOURCE_CANDIDATES_v4.1.md` | 5 |
| `v4.1 不批准任何资产` in `RIGHTS_SCREENING_DECISIONS_v4.1.md` | 1 |

---

## 5. Candidate count and disposition

| Status (table) | Count | Description |
|---|---|---|
| `candidate` | 5 | Row is a plausible v4.3 input; v4.2 must re-verify per item. |
| `needs rights audit` | 8 | Evidence is partial or depends on a per-item check. Enters v4.2 with the check listed. |
| `excluded` | 1 | BHL in-copyright subset under CC BY-NC-SA 4.0 (NC clause mismatch with openly-distributed output). |
| **`approved`** | **0** | **Status `approved` is not used in v4.1.** |

| Decision (screening) | Count | Description |
|---|---|---|
| `keep for v4.2 audit` | 12 | C-01, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13. |
| `replace with project-generated diagram` | 2 | C-02 (BHL Flickr — platform-screenshot ambiguity) and the implicit Section-4 collection-record-screenshot row. |
| `exclude` | 1 | C-14 (BHL in-copyright subset, CC BY-NC-SA 4.0, NC clause). |
| **`approved`** | **0** | **Decision `approved` is not used in v4.1.** |

| Downloaded image count | **0** |
| New image file in repo | **0** (`find` of `.jpg` / `.jpeg` / `.png` / `.webp` / `.tif` / `.tiff` shows only the 17 pre-existing files in `site/assets/images/` and `release-assets/screenshots/`). |

---

## 6. Recommended shortlist (entering v4.2)

The 12 rows entering v4.2 audit are, by section:

- **Section 1 (观察).** C-01 (BHL public-domain plate), C-03 (BHL title-level book), C-04 (Wellcome engraving / lithograph).
- **Section 2 (分类).** C-06 (Smithsonian NMNH herbarium sheet), C-09 (Rijksmuseum botanical print), C-11 (LoC P&P botanical illustration).
- **Section 3 (复制).** C-12 (LoC illustrated-book collection), C-13 (LoC P&P per-record).
- **Section 4 (再组织).** C-05 (Wellcome IIIF manifest), C-07 (Smithsonian OpenAccess data dump), C-08 (Met `MetObjects.csv` row), C-10 (Rijksmuseum IIIF Presentation API).

Plus the project-generated diagrams: 4 diagrams (one per section) and the 2 replacements for the excluded/screenshot rows = 6 project-generated entries that do not require external rights.

---

## 7. Rights risk summary

- **Low** initial risk (4 rows): C-01 (BHL public-domain), C-06 (Smithsonian NMNH CC0), C-08 (Met CC0 with double-confirmation), C-09 (Rijksmuseum CC0).
- **Low–Medium** (4 rows): C-05 (Wellcome IIIF per item), C-07 (Smithsonian data dump), C-10 (Rijksmuseum IIIF per item), C-11 (LoC P&P).
- **Medium** (3 rows): C-02 (BHL Flickr — replaced), C-03 (BHL in-copyright title — per item), C-12 (LoC illustrated book — per collection).
- **Medium / per record** (1 row): C-13 (LoC P&P per record).
- **Excluded at v4.1** (1 row): C-14 (BHL CC BY-NC-SA 4.0 — NC clause).
- **Replaced at v4.1** (2 rows): C-02 (BHL Flickr), plus the Section-4 collection-record-screenshot.

The mix is consistent with the v4.0 rights-risk register's expectations: pre-1928 botanical plates + open-access herbarium sheets are the lowest-risk sources; in-copyright subsets + platform screenshots are the highest-risk sources and are either queued for v4.2 with a per-item check or replaced with project-generated diagrams.

---

## 8. README / roadmap update

- `README.md` now carries a `## v4.1 Source Candidate Research` block immediately after the v4.0 block, recording: status (research only), no live change, no images downloaded, no assets approved, the 6 institutions, the 5 candidate docs, the keep / replace / exclude counts, and the next task (v4.2).
- `docs/V4_ROADMAP.md` v4.1 section rewritten to reflect actual deliverables + the "no asset approval" rule. The old v4.1 placeholder text (one task, "no download yet", "exit criteria = candidate source table populated with one row per candidate asset") is replaced with the more accurate deliverable list and the harder no-approval rule.

No prior v2.x / v3.x / v4.0 section was modified.

---

## 9. Live site no-change confirmation

| Check | Before | After | Delta |
|---|---|---|---|
| Live byte size | 92,976 B | 92,976 B | 0 |
| v2.9 marker in live | 1 | 1 | 0 |
| `image-placeholder-pro` in live | 0 | 0 | 0 |
| `植物图谱与视觉分类` in live | 0 | 0 | 0 (research round, not deployed) |
| `script.js` HTTP status | 200 | 200 | — |
| `git diff -- site/index.html site/style.css site/script.js` | — | empty | — |

Live site **unchanged**.

---

## 10. Template / pilot no-change confirmation

| Check | Result |
|---|---|
| `git diff -- _template/site/` | empty |
| `git diff -- _template/data/` | empty |
| `git diff -- _pilots/second-exhibition-pilot/` | empty |
| `scripts/template_quality_gate.py` | PASS 37/37 |

Template and pilot **unchanged**.

---

## 11. Old tags / old releases untouched

| Check | Result |
|---|---|
| `git tag --list` | v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1 / v3.2 / v3.3 / v3.4 — **all 10 unchanged** |
| `git ls-remote --tags origin` | matches local list — no remote-side movement |
| v3.4 tag object | `2d186a89` (unchanged) |
| v3.4 tag target | `81f5e92` (unchanged) |
| Old GitHub Releases | **none modified** (no `gh release edit` issued; only the v3.4 Release already exists from prior round) |
| `posts/` | not touched (not in this round's allowed-edit list) |
| `case-study/` | not touched (not in this round's allowed-edit list) |
| `release-assets/` | not touched (not in this round's allowed-edit list) |

No tag, no Release, no movement, no rewrite. Old history **untouched**.

---

## 12. Files changed in this round

Allowed-edit list (per round scope) — all changed files fall inside this list:

| File | Action |
|---|---|
| `docs/SOURCE_CANDIDATES_v4.1.md` | created |
| `docs/SOURCE_CANDIDATE_TABLE_v4.1.md` | created |
| `docs/INSTITUTION_POLICY_NOTES_v4.1.md` | created |
| `docs/ASSET_CANDIDATE_MATRIX_v4.1.md` | created |
| `docs/RIGHTS_SCREENING_DECISIONS_v4.1.md` | created |
| `docs/V4_ROADMAP.md` | modified (v4.1 section rewritten) |
| `README.md` | modified (v4.1 block added) |
| `reports/leonardo_chinese_exhibition_v4_1_source_candidate_research_report.md` | created (this file) |

Untracked `.firecrawl/` directory was observed at round start and **left alone**, per round scope.

---

## 13. Next recommended task

**v4.2 — Rights Audit.**

Scope of v4.2:

- For each of the 12 `keep for v4.2 audit` rows, perform the **per-item check** specified in `INSTITUTION_POLICY_NOTES_v4.1.md` and `RIGHTS_SCREENING_DECISIONS_v4.1.md`.
- Re-fetch the source URL on the day of audit; do not rely on a copy-paste from v4.1.
- Confirm the per-item rights statement, identifier, and credit-line composition.
- For items with `Is Public Domain = True` *and* a public-page CC0 icon (Met), confirm both.
- For LoC items, fetch the **collection's** Rights & Access page (not just the item page).
- For Wellcome items, confirm the per-item licence (do not trust the site-wide default).
- Promote a row to `verified` only if all 5 source-acceptance checks pass + the per-item rights statement is locatable.
- Downgrade a row to `blocked` or `excluded` if any check fails.
- Produce a single source-audit manifest, ordered by section.

v4.2 **must not**:

- Mark any row `approved` *before* all 14 metadata fields are filled (per the v4.0 source-scope rule).
- "Soft-include" any High / Blocked row by uncrediting or unfootnoting it.
- Start the build.
- Create a tag or GitHub Release.
- Move or rewrite any pre-existing tag or GitHub Release.

v4.2 **must** keep the live byte size at 92,976 B and the v2.9 marker at 1.

---

## 14. Final status

**STATUS: PASS**

All reality-gate, candidate-research, source-table, institution-policy, asset-matrix, screening-decision, README / roadmap, quality-gate, no-change, no-new-image, and old-history conditions met. v4.1 closes with five committed candidate docs, two updated existing docs, an unchanged live site (92,976 B / v2.9 marker = 1 / placeholder = 0), an unchanged template and pilot, no new image files in the repository, 12 rows entering v4.2 audit, 2 rows replaced with project-generated diagrams, 1 row excluded at v4.1, and ten untouched old tags plus their corresponding old GitHub Releases. No new tag, no new GitHub Release, no asset was approved. The next round is v4.2 — Rights Audit.