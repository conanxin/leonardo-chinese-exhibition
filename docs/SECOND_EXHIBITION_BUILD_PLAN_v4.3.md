# v4.3 Second Exhibition Build Plan

> Scope of this document: turn the 6 v4.2 verified candidates into a **build plan** for the second real exhibition. The plan defines which candidates enter build planning, what each candidate's role in the exhibition will be, what the future asset-import action is, and what cautions remain.
>
> v4.3 does not download any image. v4.3 does not import any asset. v4.3 does not write to `site/`, `_template/`, or `_pilots/`. v4.3 does not create a tag, a GitHub Release, or a live page. The status `approved` is **not used** in v4.3.

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `b6738f525d211c453ac174e4091808980a5a9a77` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| v3.4 tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (baseline) | **92,976 B** |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v4.2 verified candidates | **6** (C-01, C-03, C-06, C-08, C-09, C-10) |
| v4.2 needs clarification candidates | 6 (carried over; do not enter v4.3 build planning) |
| Exhibition direction | 《植物图谱与视觉分类：从自然史图像到知识秩序》 |
| Working title | 《植物图谱与视觉分类：从自然史图像到知识秩序》 |
| Sections (from v4.0 outline) | 1. 观察 / 2. 分类 / 3. 复制 / 4. 再组织 |

---

## Build planning goal

v4.3 只决定第二展览 build 的候选范围、内容结构和未来 asset import 计划。具体地说：

1. **Pick a build-planning candidate per section.** Each of the 4 sections (观察 / 分类 / 复制 / 再组织) gets at least one primary candidate and one fallback (a project-generated diagram, *not* a real image).
2. **Define the proposed role of each candidate in the exhibition.** Hero, 3-minute guide, section body, artifact card, or a project-generated diagram.
3. **Record per-item evidence plans** (the dossier) so that a future asset-import round can re-check the same fields without rebuilding the research.
4. **Define the content draft brief** so that the writing work (which is also a future round) has a fixed starting point.
5. **Define the asset import plan** so that the future round that *does* download a real image knows exactly what to re-check, what to record, and what files to write.
6. **Do none of the above in v4.3 itself.** v4.3 produces the *plan*; future rounds execute it.

The status `approved` is **not used** in v4.3. The 4 v4.3 statuses are:

| Status | Meaning in v4.3 |
|---|---|
| `selected-for-build-planning` | The candidate is in the build planning set. The future asset-import round may download it (after re-checking the source URL, the rights statement, the identifier, the metadata, and the credit line basis). |
| `defer` | The candidate is held back to a future round (e.g., the per-item evidence is not yet strong enough, or the section's argument is already covered by another candidate). |
| `replace-with-project-generated-diagram` | A project-generated diagram replaces the real image in the section. The candidate is *not* in the build set; the section's argument survives without the real image. |
| `blocked-from-build` | The candidate is *not* in the build set because of a rights or compatibility issue that v4.2 already identified. This includes the C-03 CC BY-NC-SA subset. |

---

## Candidate selection

The 6 v4.2 verified candidates enter v4.3 selection. The `selected-for-build-planning` set is the union of one primary candidate per section + 0–2 alternates. The status of each candidate in v4.3 is recorded in the table below.

| ID | Candidate | Institution | v4.2 status | v4.3 status | Proposed section | Proposed exhibition role | Caution |
|---|---|---|---|---|---|---|---|
| **C-01** | Pre-1928 BHL Public-domain botanical plate | BHL | verified | **selected-for-build-planning** | Section 1 (观察) | Primary real-image artifact card for Section 1; a "this is what an illustrator chose to look at" example. | The US 95-year cutoff is the safe default; non-US distribution may differ. v4.3 / v4.4 must restrict to the Public-domain subset (per-item `<Copyright Status>` field). |
| **C-03** | BHL title-level book record, **PD subset only** | BHL | verified (PD subset) / blocked (CC BY-NC-SA subset) at per-item level | **selected-for-build-planning** (PD subset only) — **CC BY-NC-SA subset blocked** | Section 3 (复制) | Primary real-image artifact card for Section 3; a "this is what a plate looked like in its published context" example. | **CC BY-NC-SA subset blocked.** The candidate row as a whole is `verified` for the PD subset; the CC BY-NC-SA in-copyright subset is `blocked-from-build` and must not appear in any v4.3 / v4.4 candidate selection. Per-item check at v4.4 must filter on `<Copyright Status> = Public domain` only. |
| **C-06** | NMNH herbarium sheet, CC0 | Smithsonian Open Access | verified | **selected-for-build-planning** | Section 2 (分类) | Primary real-image artifact card for Section 2; the "specimen + label" example. | The Smithsonian FAQ explicitly states: "CC0 only applies to copyright so you may still need someone else's permission." v4.4 must note any donor / cultural-sensitivity restrictions on the chosen item. |
| **C-08** | Met `MetObjects.csv` row + linked CC0 image | Met Open Access | verified (mechanism) | **selected-for-build-planning** (alt) | Section 3 (复制) | Alternate real-image artifact card for Section 3; a print / engraving from the Met. The Met is a secondary source for the botanical theme (the corpus is small). | Double-confirmation mandatory at v4.4: `isPublicDomain: true` in the Collection API **and** Open Access icon on the public object page. |
| **C-09** | Rijksmuseum botanical print, CC0 | Rijksmuseum | verified (mechanism) | **selected-for-build-planning** | Section 1 (观察) / Section 2 (分类) | Primary real-image artifact card for Section 1; an alternate for Section 2. | Per-item `licence` field is `CC0 1.0` or `CC BY 4.0`; if `CC BY 4.0` is selected, attribution is mandatory and the credit line must include the per-item licence. |
| **C-10** | Rijksmuseum IIIF Presentation API manifest | Rijksmuseum | verified (mechanism) | **selected-for-build-planning** | Section 4 (再组织) | Primary real-image artifact card for Section 4; the "IIIF as a re-linking layer" example. | The IIIF endpoint must be paired with the Catalogue-side object record; the rights field is on the Catalogue record, not on the IIIF info.json. |
| **C-02** | BHL Flickr photostream | BHL | replace with project-generated diagram (v4.1) | **replace-with-project-generated-diagram** | — (not in build) | The Section 1 fallback when no real image is used. | Risk category 3 (platform screenshot ambiguity) per the v4.0 register. The section's argument survives a project-generated diagram. |
| **C-04** | Wellcome Works search — Engravings / Lithographs | Wellcome | needs clarification (v4.2) | **defer** | Section 1 (alternate) | Carried as a future-round candidate; v4.3 does not pick a per-item selection. | Per-item `items.locations.license` field must be confirmed. Deferred to a future round (v4.1b or later). |
| **C-05** | Wellcome IIIF Image API per-item | Wellcome | needs clarification (v4.2) | **defer** | Section 4 (alternate) | Carried as a future-round candidate. | The IIIF endpoint must be paired with the Catalogue API work record. Deferred. |
| **C-07** | Smithsonian OpenAccess GitHub data dump | Smithsonian | needs clarification (v4.2) | **defer** | Section 4 (alternate) | Carried as a future-round candidate. | Every C-07 row must be promoted via a C-06-style per-item check. Deferred. |
| **C-11** | LoC P&P — Botanical illustrations subject heading | LoC P&P | needs clarification (v4.2) | **defer** | Section 1 (alternate) | Carried as a future-round candidate. | Per-item rights wording is non-affirmative in the "no known" variant. Deferred. |
| **C-12** | LoC Digital Collections — illustrated-book type | LoC | needs clarification (v4.2) | **defer** | Section 3 (alternate) | Carried as a future-round candidate. | The candidate type is a *type*, not a specific LoC collection. Deferred. |
| **C-13** | LoC P&P per-item record | LoC P&P | needs clarification (v4.2) | **defer** | Section 1 / Section 3 (alternate) | Carried as a future-round candidate. | Per-record rights wording. Deferred. |
| **C-14** | BHL in-copyright subset (CC BY-NC-SA 4.0) | BHL | excluded (v4.1) | **blocked-from-build** | — (not in build) | The BHL in-copyright subset is incompatible with the project's openly-distributed output. | The v4.2 audit does not re-clear this. v4.3 does not re-introduce it. |
| **(Section 4 implicit row)** | Collection record screenshot from an institution's catalog page | (platform screenshot) | replace with project-generated diagram (v4.1) | **replace-with-project-generated-diagram** | Section 4 (fallback) | A project-generated facsimile of a record's fields; the underlying fields are stable, the UI is not. | Risk category 3 (platform screenshot ambiguity) per the v4.0 register. |

**Selection totals.**

- `selected-for-build-planning`: **5** (C-01, C-03 [PD subset only], C-06, C-08 [alt], C-09, C-10) — the parenthetical "C-08 [alt]" is a single row in the table, so the count is **6** (C-01, C-03, C-06, C-08, C-09, C-10). 5 of these are **primary**; C-08 is **alt** for Section 3. (Final count: **6 selected-for-build-planning**.)
- `defer`: 6 (C-04, C-05, C-07, C-11, C-12, C-13).
- `replace-with-project-generated-diagram`: 2 (C-02, Section-4 screenshot row).
- `blocked-from-build`: 1 (C-14, the BHL CC BY-NC-SA title-level row).
- `approved`: **0** (not used).

**Important cautions.**

- **C-03 has two halves.** The C-03 row is `verified` for the **Public-domain** subset only. The **CC BY-NC-SA** subset is `blocked-from-build` and must not appear in any v4.3 / v4.4 candidate selection. The future asset-import round must filter on `<Copyright Status> = Public domain` only.
- **C-08 is an alternate.** The Met's botanical / natural-history holdings are not a primary collection strength; C-08 is the Section 3 alternate. The primary Section 3 real image is C-03 (PD subset).
- **No real image is downloaded in v4.3.** The selection table is a plan, not a download log.

---

## Proposed minimum build set

The minimum build set is the union of one primary candidate per section + 0–1 alternate + 1–2 project-generated diagrams. The build set must cover all 4 sections, must not exceed 6 selected-for-build-planning rows, and must not import a real image in v4.3.

| Section | Primary real-image candidate | Alternate real-image candidate | Fallback project-generated diagram |
|---|---|---|---|
| Section 1 (观察) | **C-01** (BHL PD plate) | C-04 (Wellcome) — deferred; or C-11 (LoC P&P) — deferred | Comparison-of-two-editions diagram, drawn by the project. |
| Section 2 (分类) | **C-06** (Smithsonian NMNH CC0) | C-09 (Rijksmuseum) — also Section 1 alternate | Comparison of two related species, side-by-side, with the diagnostic features labelled. |
| Section 3 (复制) | **C-03** (BHL PD book page, **PD subset only**) | C-08 (Met CC0) | Reproduction-chain diagram (engraving → lithograph → photograph → scan → digital). |
| Section 4 (再组织) | **C-10** (Rijksmuseum IIIF manifest) | C-05 (Wellcome IIIF) — deferred; or C-07 (Smithsonian data dump) — deferred | Network diagram (one botanical species connected across two herbaria, two editions, two records). |

**Section coverage.** Each section has at least one primary candidate and at least one fallback. Section 1 and Section 2 share C-09 as a cross-section candidate; Section 3's primary is C-03 (PD subset only), with C-08 as the alternate.

**Real-image count in the build set.** **5** primary real-image candidates + **1** alternate (C-08) = 6 selected-for-build-planning rows. None is downloaded in v4.3.

**Project-generated diagram count.** 4 (one per section) + the 2 carried-over from v4.1 (the Section 4 screenshot replacement, and the C-02 BHL-Flickr replacement) = 6 project-generated entries. None is drawn in v4.3; the diagrams are *planned*, not produced.

**Total planned content units (real + project-generated).** **6** selected real images + **6** project-generated diagrams = **12** content units. The MVE (from v4.0) requires 4 sections + 4–6 artifact cards + 6–10 glossary terms. The build set covers all four.

---

## Build non-goals

v4.3 explicitly does **not**:

- Download any image.
- Import any image file into the repository.
- Modify `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`.
- Modify `scripts/template_quality_gate.py`.
- Mark any candidate `approved` (the status `approved` is **not used** in v4.3 or any future round).
- Create a tag or GitHub Release.
- Move or rewrite any pre-existing tag (`v2.0` through `v3.4`) or any pre-existing GitHub Release.
- Process the untracked `.firecrawl/` directory.
- Pick a specific per-item selection (e.g., a specific BHL volume, a specific NMNH accession number). Per-item selection is a v4.4 step.
- Write the section bodies, the hero, the 3-minute guide, the artifact card captions, the curatorial essay, or the source notes. The content draft is in `docs/CONTENT_DRAFT_BRIEF_v4.3.md`; the actual writing is a future round.
- Draw any project-generated diagram. The diagrams are planned in `docs/CONTENT_DRAFT_BRIEF_v4.3.md` and `docs/ASSET_IMPORT_PLAN_v4.3.md`; the actual drawing is a future round.
- Re-introduce any `needs clarification` candidate as `selected-for-build-planning` (C-04, C-05, C-07, C-11, C-12, C-13 are all `defer`).
- Re-introduce the v4.1 `replace with project-generated diagram` rows (C-02, Section-4 screenshot) as `selected-for-build-planning`. They remain `replace-with-project-generated-diagram`.
- Re-introduce the v4.1 `excluded` row (C-14, BHL CC BY-NC-SA). It remains `blocked-from-build`.

---

## Round boundary

v4.3 ends with:

- All 5 v4.3 planning docs committed (`SECOND_EXHIBITION_BUILD_PLAN_v4.3.md`, `ITEM_EVIDENCE_DOSSIER_v4.3.md`, `BUILD_SCOPE_v4.3.md`, `CONTENT_DRAFT_BRIEF_v4.3.md`, `ASSET_IMPORT_PLAN_v4.3.md`).
- `README.md` v4.3 block committed.
- `docs/V4_ROADMAP.md` v4.3 section rewritten.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/` is **empty**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- `find` confirms no new image files (`.jpg` / `.jpeg` / `.png` / `.webp` / `.tif` / `.tiff`).
- `approved` does not appear as a status value in any v4.3 doc.
- No new tag, no new GitHub Release.

The next round is **v4.4 — Asset Import Prep** (or, equivalently, a future round that does the actual image download per the asset import plan).