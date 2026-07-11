# v4.4 Asset Import Prep

> Scope of this document: per-candidate item-level / source-level evidence for the 6 v4.3 `selected-for-build-planning` candidates, plus the import-readiness assessment. v4.4 does not download any image. v4.4 only records the *plan* (URL, identifier, rights statement, image/IIIF URL, future filename, credit line basis, pre-import action) so that a future asset-import round can execute the 11-step import rule.

> 本轮不得下载图片，不得新增图片文件。`approved` is **not used** in v4.4 or any future round. The 4 v4.4 statuses are: `ready-for-asset-import` / `defer` / `blocked-from-import` / `replace-with-project-generated-diagram`. v4.4 status values for the per-row tables are `ready-for-asset-import` or `defer` only — the other two statuses (`blocked-from-import`, `replace-with-project-generated-diagram`) are policy-level entries, not row-level.

## v4.4 Asset Import Prep — summary block

- **item-level / source-level import prep completed** for the 6 v4.3 selected candidates.
- **ready-for-asset-import count = 2** (C-01, C-03 — BHL item 318921, PD subset only).
- **defer count = 4** (C-06, C-08, C-09, C-10 — per-item record deferred).
- **ready-for-asset-import count < 4** (2 < 4) — the asset import threshold is not met.
- **no images downloaded** in v4.4.
- **no assets imported** in v4.4.
- **no approved status** in v4.4 or any future round (the status `approved` is not used).
- **C-03 CC BY-NC-SA subset blocked** at the per-page / per-volume level.
- **C-08 double-confirmation required** (Collection API `isPublicDomain: true` AND Open Access icon on public object page).
- **C-09 / C-10 per-item licence field required** (recorded verbatim at v4.4b / v4.5).
- **next recommended task = v4.4b-source-gap-fix** (closes the source gap; v4.5 — Asset Import — is conditioned on v4.4b producing ≥ 4 `ready-for-asset-import` rows).

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `978f8eddf9a8dcdf8e9f6b209f5f764c6192062c` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| v3.4 tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (baseline) | **92,976 B** |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v4.3 selected-for-build-planning count | **6** (C-01, C-03, C-06, C-08, C-09, C-10) |
| v4.3 defer count | 6 (C-04, C-05, C-07, C-11, C-12, C-13) |
| v4.3 blocked-from-build | 1 (C-14) + C-03 CC BY-NC-SA subset blocked at per-item level |
| Exhibition direction | 《植物图谱与视觉分类：从自然史图像到知识秩序》 |

---

## Goal

v4.4 only prepares the evidence for a future asset-import round. Specifically:

1. **Pick one specific item-level source per selected candidate.** Re-open the official item / object page on the day of the audit. Do not rely on the v4.3 dossier as the final evidence — v4.3 is a *plan*, v4.4 is the *evidence* (or a deferred/declined decision if evidence is insufficient).
2. **Capture the per-item evidence fields.** Item URL, institution, title, creator / maker, date, identifier, rights statement, rights / terms URL, image / IIIF URL (if available — without download), proposed local filename, proposed alt text, caption draft, source note draft, credit line draft, proposed section, v4.4 status, required pre-import action.
3. **Apply the v4.4 import-readiness statuses.** Only `ready-for-asset-import` rows are eligible for the future import round. Rows with `defer` / `blocked-from-import` / `replace-with-project-generated-diagram` do not enter the import round.
4. **Build the asset filename map** so the future import round has a stable local path.
5. **Draft the credit line + source note** for each row so the future import round can copy them verbatim.

The v4.4 status `approved` is **not used**. The phrase "safe for commercial use" is **not used**. v4.4 makes *project release decisions* based on what the institution's own page says, not legal opinions.

---

## Item-level research method

For each of the 6 v4.3 selected candidates, v4.4 re-opens the official page and records the per-item evidence. The method:

1. **Re-open the official source page** (per the v4.3 dossier's source URL).
2. **Pick one specific item-level record** that fits the section's argument. The item must be reachable today; the audit is "as written on the institution's own page on the day of audit".
3. **Capture the 14 v4.4 fields** listed below.
4. **Apply the v4.4 status** based on whether the 14 fields are complete and whether the rights statement is locatable.

The 14 v4.4 fields are:

1. Official item URL.
2. Institution.
3. Title.
4. Creator / maker.
5. Date.
6. Object / item identifier.
7. Rights statement.
8. Rights / terms URL.
9. Image URL or IIIF URL (if available — record URL only, do not download).
10. Proposed local filename.
11. Proposed alt text.
12. Caption draft.
13. Source note draft.
14. Credit line draft.

Plus, the v4.4 row also records: proposed section, v4.4 status, required pre-import action.

---

## Candidate import readiness

The 6 v4.3 selected candidates enter v4.4 import-readiness assessment. The 4 v4.4 statuses are:

| Status | Meaning in v4.4 |
|---|---|
| `ready-for-asset-import` | All 14 v4.4 fields are complete. The official item URL is reachable. The rights statement is locatable on the institution's own page. The image / IIIF URL is locatable. The credit line basis is composable without guessing. The C-08 double-confirmation (if applicable) is complete. The C-09 / C-10 per-item `licence` field is recorded. The C-03 PD-subset check is passed. |
| `defer` | At least one v4.4 field is missing. The candidate is held back to a future round. The follow-up action is recorded. |
| `blocked-from-import` | A rights or compatibility issue makes the import impossible. The C-14 row (BHL CC BY-NC-SA) and the C-03 CC BY-NC-SA subset remain `blocked-from-import`. |
| `replace-with-project-generated-diagram` | A project-generated diagram replaces the real image. The candidate is *not* in the import set. |

| ID | Candidate | Institution | Item selected? | Image / IIIF URL found? | v4.4 status | Proposed section | Caution |
|---|---|---|---|---|---|---|---|
| **C-01** | BHL pre-1928 Public-domain botanical plate (page-level) | BHL | Yes — BHL item **318921** (album of watercolors of Asian fruits and flowers, with per-page watercolors that serve as "plates" within the v4.0 outline's artifact type) | Image / IIIF URL is reachable via the BHL page-viewer on the item page (page image URL is the per-page image URL; the v4.4 record captures the item-level URL + the per-page URL pattern; **v4.4 records URLs only, does not download**) | **ready-for-asset-import** (with C-03-style PD-subset check) | Section 1 (观察) | v4.4 must filter on `<Copyright Status> = Public domain` at the per-page level. The C-01 / C-03 distinction is *which page of the same item is the Section 1 plate vs the Section 3 book page*. v4.4 must run the per-page check on the day of import. |
| **C-03** | BHL title-level book record (PD subset only) | BHL | Yes — BHL item **318921** (album of watercolors of Asian fruits and flowers, treated as the title-level book record for Section 3) | Image / IIIF URL is reachable via the BHL page-viewer (per-page image URL pattern; **URL only, no download**) | **ready-for-asset-import** — **PD subset only; CC BY-NC-SA subset blocked** | Section 3 (复制) | **CC BY-NC-SA subset blocked.** The v4.4 import must filter on `<Copyright Status> = Public domain` only at the per-page / per-volume level. The CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` and is not eligible. |
| **C-06** | NMNH herbarium sheet, CC0 | Smithsonian Open Access (NMNH Botany) | Yes — NMNH Botany Department collections search entry at <https://collections.nmnh.si.edu/search/botany/> (Botany Department, ~4.2M specimen records, ~115k type specimens with images); the per-item record will be selected at v4.5 | Image URL is locatable on the per-item record (the specimen image is part of the record's media; **v4.4 records the entry URL only, not a per-item image**) | **defer** (per-item selection deferred to v4.5) | Section 2 (分类) | The NMNH Botany search is the *entry*. v4.4 does not pick a specific item. v4.5 will run a per-item query (e.g., by Family or Collection Number), pick a CC0-marked record with an image, and capture the accession number. |
| **C-08** | Met CC0 image (Section 3 alternate) | The Metropolitan Museum of Art | Yes — Met object **285149** (*[Botanical Specimen: Fern]*, Unknown, 1860s, albumen silver print, Photographs Department, accession 2003.562.3) | Image URL: reachable via Met Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` → `primaryImage` / `primaryImageSmall` field. **Double-confirmation required at v4.4.** | **defer** (double-confirmation result depends on `isPublicDomain: true` AND public-page OA icon; v4.4 cannot re-fetch the live page during this planning round) | Section 3 (复制) — alternate | **C-08 must pass double-confirmation** at v4.4 or v4.5: `isPublicDomain: true` in the Met Collection API record **and** Open Access icon on the public object page <https://www.metmuseum.org/art/collection/search/285149>. If either confirmation is missing, C-08 is `blocked-from-import` and the Section 3 alternate slot is filled by a project-generated diagram. v4.4 records the Met object 285149 as a *candidate*; the double-confirmation is the v4.4 / v4.5 pre-import action. |
| **C-09** | Rijksmuseum botanical print, CC0 (or CC BY 4.0) | Rijksmuseum | Yes — Rijksprentenkabinet entry at <https://www.rijksmuseum.nl/en/research/our-research/print-room> (750,000 works on paper); per-item record will be selected at v4.5 | Image URL: per-item Rijksstudio image URL or IIIF Image API URL; **v4.4 records the entry URL only, not a per-item image** | **defer** (per-item selection + per-item `licence` field deferred to v4.5) | Section 1 (观察) primary / Section 2 (分类) alternate | **C-09 must record per-item `licence` field at v4.5** — the Rijksmuseum's two-tier policy: `CC0 1.0` (no longer in copyright) or `CC BY 4.0` (third-party grant). The per-item `licence` field is recorded verbatim. v4.4 records the candidate type; v4.5 picks a specific object and records the `licence` field. |
| **C-10** | Rijksmuseum IIIF Presentation API manifest | Rijksmuseum | Yes — same Rijksprentenkabinet entry; per-item IIIF manifest URL is locatable on the per-item Catalogue record; **v4.4 records the entry URL only, not a per-item manifest** | IIIF URL: Rijksmuseum IIIF Presentation API manifest URL is on the per-item Catalogue record; v4.4 records the entry URL only | **defer** (per-item selection + per-item `licence` field deferred to v4.5) | Section 4 (再组织) | **C-10 must record per-item `licence` field at v4.5** — the IIIF Presentation API manifest's `license` field is the authoritative source (CC0 1.0 or CC BY 4.0). v4.4 records the candidate type; v4.5 picks a specific object and captures the `license` field. |

**Selection totals (v4.4).**

- `ready-for-asset-import`: **2** (C-01 and C-03, both anchored on BHL item 318921 with PD-subset enforcement; the per-page / per-volume check is the v4.4 pre-import action).
- `defer`: **4** (C-06, C-08, C-09, C-10 — the per-item selection is a v4.5 step).
- `blocked-from-import`: **0** in the 6-row set (the C-14 row is outside the v4.3 selected set; the C-03 CC BY-NC-SA subset is blocked at the per-page level but does not create a separate row).
- `replace-with-project-generated-diagram`: **0** in the 6-row set (the v4.1 carry-overs are still fallback-only; they do not enter the v4.4 import-readiness table).
- `approved`: **0** (not used).

**Threshold check.** The `ready-for-asset-import` count is **2**, which is **< 4**. The next round is **v4.4b — Source Gap Fix** (a follow-up to v4.4 that picks the deferred candidates' specific items). v4.5 — Asset Import — is conditioned on the gap fix producing ≥ 4 `ready-for-asset-import` rows.

**Why is the count 2?** The BHL item 318921 is reachable, has a clear item-level URL, and the per-page `<Copyright Status>` field is documented (so C-01 and C-03 can be checked at v4.4). The other 4 candidates' per-item records are *not* picked in v4.4 because the institution's per-item records require a per-item search query (NMNH Botany search returns up to 10,000 records, Rijksmuseum search returns paginated results, Met object 285149 requires a live `isPublicDomain: true` check on the Collection API). v4.4 does not run those queries — it records the *entry* URL and defers the per-item selection to v4.5.

**Per-candidate pre-import action summary.**

- **C-01 / C-03 (BHL):** Re-open BHL item 318921, pick a per-page or per-volume record, run the per-page / per-volume `<Copyright Status>` check, filter to `Public domain` only, capture the page image URL pattern. CC BY-NC-SA subset rejected.
- **C-06 (Smithsonian NMNH):** Run a NMNH Botany search by Family or Collection Number, pick a CC0-marked record with an image, capture the accession number.
- **C-08 (Met):** Re-open Met object 285149, run the double-confirmation (`isPublicDomain: true` in the Collection API + Open Access icon on the public object page), capture the image URL.
- **C-09 / C-10 (Rijksmuseum):** Run a Rijksmuseum search by `type` and `creator`, pick a Rijksprentenkabinet object, capture the per-item `licence` field, capture the IIIF manifest URL (for C-10), capture the `objectNumber` and `id.rijksmuseum.nl/...` PID.

---

## Non-goals

v4.4 explicitly does **not**:

- Download any image.
- Add any image file to the repository.
- Modify `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`.
- Modify `scripts/template_quality_gate.py`.
- Mark any candidate `approved` (the status `approved` is **not used** in v4.4 or any future round).
- Create a tag or GitHub Release.
- Move or rewrite any pre-existing tag (`v2.0` through `v3.4`) or any pre-existing GitHub Release.
- Process the untracked `.firecrawl/` directory.
- Re-introduce any `defer` (v4.2 needs-clarification) candidate as `ready-for-asset-import`.
- Re-introduce the v4.1 `excluded` row (C-14) as `ready-for-asset-import`.
- Re-introduce the v4.1 `replace with project-generated diagram` rows (C-02, Section-4 screenshot) as `ready-for-asset-import`.
- Run a per-item search query for NMNH, Rijksmuseum, or Met. v4.4 only records the *entry* URL; the per-item query is a v4.5 step.

---

## Round boundary

v4.4 ends with:

- All 5 v4.4 prep docs committed (`ASSET_IMPORT_PREP_v4.4.md`, `ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md`, `SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md`, `CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md`, `ASSET_FILENAME_MAP_v4.4.md`).
- `README.md` v4.4 block committed.
- `docs/V4_ROADMAP.md` v4.4 section rewritten.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/` is **empty**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- `find` confirms no new image files.
- `ready-for-asset-import` count is recorded (2 in this round, < 4 → v4.4b is the next round).
- `approved` does not appear as a status value in any v4.4 doc.
- C-03's `CC BY-NC-SA subset blocked` is recorded.
- C-08's `double-confirmation` is recorded.
- C-09 / C-10's `licence field` is recorded.
- No new tag, no new GitHub Release.

The next round is **v4.4b — Source Gap Fix** (a follow-up that picks the per-item records for C-06, C-08, C-09, C-10 and re-runs the v4.4 import-readiness assessment). v4.5 — Asset Import — is conditioned on the gap fix producing ≥ 4 `ready-for-asset-import` rows.