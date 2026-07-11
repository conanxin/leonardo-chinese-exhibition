# v4.4 Source Audit Manifest (DRAFT)

> Scope of this document: a draft of the future source-audit manifest, written now (v4.4) so that the v4.4b / v4.5 import rounds can copy the rows verbatim. v4.4 records URLs and identifiers only — **no image is downloaded in v4.4**, and **no image file is created in v4.4**. The manifest rows below are evidence rows; the actual `docs/SOURCE_AUDIT_MANIFEST.md` only graduates to `final` when v4.5 actually downloads a per-item image. In v4.4, this file is marked `DRAFT`.

> 收口时间：v4.4 prep round 结束点。下一 round 是 **v4.4b — Source Gap Fix**，不是 v4.5 asset import。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `978f8eddf9a8dcdf8e9f6b209f5f764c6192062c` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | **92,976 B** (baseline preserved) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v4.4 doc set | `ASSET_IMPORT_PREP_v4.4.md` + `ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md` + `SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md` (this file) + `CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md` + `ASSET_FILENAME_MAP_v4.4.md` |

---

## Manifest rows (DRAFT)

Each row below is a v4.4 evidence row. Rows are `ready-for-asset-import` (eligible for v4.5 once v4.4b closes the source gap) or `defer` (held back to v4.4b). The status `approved` is **not used**. The status `blocked-from-import` does not appear at the row level for the 6-row set (C-14 and the C-03 CC BY-NC-SA subset are policy-level entries — see the "Policy-level entries" section below).

### Row C-01 — BHL page-level plate (Section 1 观察)

| Field | Value |
|---|---|
| Candidate ID | C-01 |
| Title (short) | BHL pre-1928 Public-domain botanical plate (page-level) |
| Institution | Biodiversity Heritage Library (BHL) |
| Official item URL | https://www.biodiversitylibrary.org/item/318921 |
| Item title | Album of watercolors of Asian fruits and flowers |
| Creator / maker | Unknown (watercolor artist) |
| Date | between 1798 and 1850? |
| Identifier | BHL item 318921 |
| Rights statement | Public domain (per-page / per-item `<Copyright Status>` filter) |
| Rights / terms URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| Image / IIIF URL pattern | per-page image URL via BHL page-viewer (item-level URL is reachable; per-page URL recorded but not downloaded in v4.4) |
| Proposed local filename | `bhl-318921-plate.jpg` |
| Proposed section | Section 1 (观察) |
| v4.4 status | `ready-for-asset-import` |
| Pre-import action | Re-open BHL item 318921 on the day of import. Filter per-page `<Copyright Status>` to `Public domain` only. CC BY-NC-SA subset rejected. Capture per-page image URL. |
| Local path status | not yet downloaded; v4.4 records the proposed filename only |

### Row C-03 — BHL title-level book record, PD subset only (Section 3 复制)

| Field | Value |
|---|---|
| Candidate ID | C-03 |
| Title (short) | BHL title-level book record (PD subset only) |
| Institution | Biodiversity Heritage Library (BHL) |
| Official item URL | https://www.biodiversitylibrary.org/item/318921 |
| Item title | Album of watercolors of Asian fruits and flowers |
| Creator / maker | Unknown (watercolor artist) |
| Date | between 1798 and 1850? |
| Identifier | BHL item 318921 |
| Rights statement | Public domain (PD subset only). CC BY-NC-SA 4.0 subset = **`blocked-from-import`** at per-page / per-volume level. |
| Rights / terms URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| Image / IIIF URL pattern | per-page image URL via BHL page-viewer |
| Proposed local filename | `bhl-318921-page.jpg` |
| Proposed section | Section 3 (复制) |
| v4.4 status | `ready-for-asset-import` — PD subset only; CC BY-NC-SA subset blocked |
| Pre-import action | Same as C-01. Re-open item 318921. Filter to PD subset. |
| Local path status | not yet downloaded; v4.4 records the proposed filename only |

### Row C-06 — Smithsonian NMNH herbarium sheet, CC0 (Section 2 分类)

| Field | Value |
|---|---|
| Candidate ID | C-06 |
| Title (short) | NMNH herbarium sheet, CC0 |
| Institution | Smithsonian National Museum of Natural History / NMNH Botany |
| Official item URL | https://collections.nmnh.si.edu/search/botany/ (entry URL; **not yet an item-level record**) |
| Item title | pending v4.4b |
| Creator / maker | pending v4.4b |
| Date | pending v4.4b |
| Identifier | pending v4.4b (per-item accession number) |
| Rights statement | Smithsonian Open Access / **CC0 1.0** (to be confirmed per item in v4.4b) |
| Rights / terms URL | https://www.si.edu/openaccess/faq |
| Image / IIIF URL pattern | per-item image URL is locatable on the per-item record; v4.4 records the entry URL only |
| Proposed local filename | `nmnh-<accession_number>.jpg` (accession number pending v4.4b) |
| Proposed section | Section 2 (分类) |
| v4.4 status | `defer` (per-item selection deferred to v4.4b) |
| Pre-import action | Run NMNH Botany search in v4.4b. Pick a CC0-marked record with an image. Capture title, collector, date, accession number, official record URL, media URL. |
| Local path status | not yet downloaded; per-item accession number pending |

### Row C-08 — Met CC0 image, Section 3 alternate

| Field | Value |
|---|---|
| Candidate ID | C-08 |
| Title (short) | Met CC0 image (Section 3 alternate) |
| Institution | The Metropolitan Museum of Art |
| Official item URL | https://www.metmuseum.org/art/collection/search/285149 |
| Item title | [Botanical Specimen: Fern] |
| Creator / maker | Unknown |
| Date | 1860s |
| Identifier | 285149 / 2003.562.3 |
| Rights statement | Public domain (**double-confirmation still required**: Collection API `isPublicDomain: true` AND Open Access icon on the public object page) |
| Rights / terms URL | https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources |
| Image / IIIF URL pattern | Met Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` → `primaryImage` / `primaryImageSmall` field |
| Proposed local filename | `met-285149.jpg` |
| Proposed section | Section 3 (复制) — alternate |
| v4.4 status | `defer` (double-confirmation pending v4.4b) |
| Pre-import action | Re-open Met object 285149 in v4.4b. Run double-confirmation (API + public page OA icon). Capture primary image URL. |
| Local path status | not yet downloaded; double-confirmation pending |

### Row C-09 — Rijksmuseum botanical print

| Field | Value |
|---|---|
| Candidate ID | C-09 |
| Title (short) | Rijksmuseum botanical print (CC0 1.0 or CC BY 4.0) |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Official item URL | https://www.rijksmuseum.nl/en/research/our-research/print-room (entry URL; **not yet an item-level record**) |
| Item title | pending v4.4b |
| Creator / maker | pending v4.4b |
| Date | pending v4.4b |
| Identifier | pending v4.4b (`objectNumber` + `id.rijksmuseum.nl/...` PID) |
| Rights statement | Rijksmuseum two-tier policy: **`CC0 1.0`** or **`CC BY 4.0`**. Per-item `licence` field recorded verbatim in v4.4b. |
| Rights / terms URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| Image / IIIF URL pattern | per-item Rijksstudio image URL or IIIF Image API URL (pending v4.4b) |
| Proposed local filename | `rijksmuseum-<object_number>.jpg` |
| Proposed section | Section 1 (观察) primary / Section 2 (分类) alternate |
| v4.4 status | `defer` (per-item selection + per-item `licence` field deferred to v4.4b) |
| Pre-import action | Pick a specific Rijksprentenkabinet object in v4.4b. Record `licence` field verbatim, `objectNumber`, `id.rijksmuseum.nl/...` PID, image/IIIF URL. |
| Local path status | not yet downloaded; per-item `objectNumber` and `licence` field pending |

### Row C-10 — Rijksmuseum IIIF Presentation API manifest

| Field | Value |
|---|---|
| Candidate ID | C-10 |
| Title (short) | Rijksmuseum IIIF Presentation API manifest |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Official item URL | https://www.rijksmuseum.nl/en/research/our-research/print-room (entry URL; **not yet an item-level record**) |
| Item title | pending v4.4b (same Rijksmuseum object as C-09) |
| Creator / maker | pending v4.4b |
| Date | pending v4.4b |
| Identifier | pending v4.4b (`objectNumber` + `id.rijksmuseum.nl/...` PID) |
| Rights statement | Rijksmuseum two-tier policy: **`CC0 1.0`** or **`CC BY 4.0`**. The IIIF Presentation API manifest's `license` field is the authoritative source. |
| Rights / terms URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| Image / IIIF URL pattern | Rijksmuseum IIIF Presentation API manifest URL is on the per-item Catalogue record |
| Proposed local filename | derived from C-09's per-item image |
| Proposed section | Section 4 (再组织) |
| v4.4 status | `defer` (per-item selection + per-item `license` field deferred to v4.4b) |
| Pre-import action | Same as C-09 — pick a specific Rijksprentenkabinet object in v4.4b. Capture the IIIF Presentation API manifest URL and the `license` field. |
| Local path status | not yet downloaded |

---

## Policy-level entries

These are not rows in the 6-row set, but they are policy-level entries that the future import round must respect. They live in the manifest's preamble, not in the per-item table.

| Policy entry | Status | Notes |
|---|---|---|
| C-14 (BHL CC BY-NC-SA — row-level block) | `blocked-from-import` | C-14 was `excluded` in v4.1; it must not be re-introduced as `ready-for-asset-import` in any future round. |
| C-03 CC BY-NC-SA 4.0 in-copyright subset (page-level block) | `blocked-from-import` | C-03 itself is `ready-for-asset-import` for the Public-domain subset only. The CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at the per-page / per-volume level. |

---

## Manifest totals (DRAFT)

| Bucket | Count |
|---|---|
| `ready-for-asset-import` | 2 (C-01, C-03) |
| `defer` | 4 (C-06, C-08, C-09, C-10) |
| `blocked-from-import` row-level | 0 |
| `replace-with-project-generated-diagram` row-level | 0 |
| `approved` | 0 (not used) |
| Total rows | 6 |

---

## Why this file is marked DRAFT

A manifest is only `final` once:

1. The per-item image has been downloaded into the repository under the proposed filename.
2. The image bytes have been re-checked (sha256 / file size).
3. The license field on the institution's page has been re-read on the day of download.

In v4.4, none of those three conditions hold (v4.4 records URLs only, downloads nothing). So this manifest is a `DRAFT` and the `final` version of `docs/SOURCE_AUDIT_MANIFEST.md` will be written in v4.4b or v4.5 once the source gap is closed.

---

## Non-goals for v4.4

- Do **not** download any image in v4.4. The image bytes are recorded as URLs only.
- Do **not** create any image file (`*.jpg` / `*.jpeg` / `*.png` / `*.webp` / `*.tif` / `*.tiff`) in v4.4.
- Do **not** move the existing `docs/SOURCE_AUDIT_MANIFEST.md` (it carries the v4.3 manifest; v4.4 produces a *new* file `docs/SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md` alongside it).
- Do **not** create a tag or GitHub Release in v4.4.

---

## Round boundary

The next round is **v4.4b — Source Gap Fix**, which closes the gap by picking the deferred candidates' specific items and re-running the v4.4 import-readiness assessment. v4.5 — Asset Import — is conditioned on v4.4b producing ≥ 4 `ready-for-asset-import` rows.