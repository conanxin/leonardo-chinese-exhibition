# v4.4 Item Import Evidence Table

> Scope of this document: per-candidate item-level evidence for the 6 v4.3 `selected-for-build-planning` candidates. v4.4 does **not** download any image — it records URL, identifier, rights statement, image/IIIF URL, proposed filename, credit-line basis, pre-import action. The 4 v4.4 statuses are `ready-for-asset-import` / `defer` / `blocked-from-import` / `replace-with-project-generated-diagram`. The status `approved` is **not used**.

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
| `image-placeholder-pro` count on live | 0 |
| v4.3 selected-for-build-planning count | 6 (C-01, C-03, C-06, C-08, C-09, C-10) |

---

## v4.4 status legend

| Status | Meaning |
|---|---|
| `ready-for-asset-import` | All 14 v4.4 fields complete. Item URL reachable. Rights statement locatable. Image/IIIF URL locatable. Credit-line basis composable. PD-subset / double-confirmation / per-item `licence` checks passed. |
| `defer` | At least one v4.4 field is missing. Held back to a future round. Follow-up action recorded. |
| `blocked-from-import` | Rights or compatibility issue makes import impossible. C-14 row and the C-03 CC BY-NC-SA subset. |
| `replace-with-project-generated-diagram` | A project-generated diagram replaces the real image. Not in the import set. |

---

## 6 rows

### Row C-01 — BHL page-level plate (Section 1 观察)

| Field | Value |
|---|---|
| 1. Official item URL | https://www.biodiversitylibrary.org/item/318921 |
| 2. Institution | Biodiversity Heritage Library (BHL) |
| 3. Title | Album of watercolors of Asian fruits and flowers |
| 4. Creator / maker | Unknown (watercolor artist) |
| 5. Date | between 1798 and 1850? |
| 6. Object / item identifier | BHL item **318921** |
| 7. Rights statement | Public domain, but **must filter per-page / per-item copyright status** (the item's `<Copyright Status>` field is documented per page / per volume) |
| 8. Rights / terms URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| 9. Image URL or IIIF URL | Item-level URL is reachable. The per-page image URL is reachable via the BHL page-viewer on the item page (URL recorded; **v4.4 does not download**) |
| 10. Proposed local filename | `bhl-318921-plate.jpg` |
| 11. Proposed alt text | "水彩绘亚洲水果与花卉图谱中的一页，画面为某一具体植物标本的手绘水彩插图。" |
| 12. Caption draft | "水彩绘亚洲水果与花卉图谱，1798—1850 年间绘制。BHL item 318921。该页用作第一展区《观察》的视觉标本——一帧早于摄影术、依赖肉眼与水彩转译的植物图像。" |
| 13. Source note draft | "页图像下载自 BHL item 318921，经 per-page `<Copyright Status>` 过滤为 `Public domain` 子集。CC BY-NC-SA 4.0 子集被排除在导入之外。" |
| 14. Credit line draft | "Source: Biodiversity Heritage Library, item 318921. Public domain (per-page copyright status filter applied)." |
| Proposed section | Section 1 (观察) |
| **v4.4 status** | **`ready-for-asset-import`** |
| Required pre-import action | Re-open BHL item 318921 on the day of import. Pick the per-page record. Run the per-page `<Copyright Status>` check. Filter to `Public domain` only. CC BY-NC-SA subset rejected. Capture the per-page image URL pattern. |

---

### Row C-03 — BHL title-level book record, PD subset only (Section 3 复制)

| Field | Value |
|---|---|
| 1. Official item URL | https://www.biodiversitylibrary.org/item/318921 |
| 2. Institution | Biodiversity Heritage Library (BHL) |
| 3. Title | Album of watercolors of Asian fruits and flowers |
| 4. Creator / maker | Unknown (watercolor artist) |
| 5. Date | between 1798 and 1850? |
| 6. Object / item identifier | BHL item **318921** (treated as the title-level book record for Section 3) |
| 7. Rights statement | Public domain (PD subset only). The CC BY-NC-SA 4.0 in-copyright subset is **`blocked-from-import`** at the per-page / per-volume level. |
| 8. Rights / terms URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| 9. Image URL or IIIF URL | Per-page image URL is reachable via the BHL page-viewer on the item page (URL recorded; **v4.4 does not download**) |
| 10. Proposed local filename | `bhl-318921-page.jpg` |
| 11. Proposed alt text | "水彩绘亚洲水果与花卉图谱的书页扫描，作为第三展区《复制》的实物载体。" |
| 12. Caption draft | "水彩绘亚洲水果与花卉图谱的书页，1798—1850 年间绘制。BHL item 318921。作为第三展区《复制》的视觉标本——纸本图像如何成为可被反复复制、流通、再制的载体。" |
| 13. Source note draft | "页图像下载自 BHL item 318921，经 per-page `<Copyright Status>` 过滤为 `Public domain` 子集。CC BY-NC-SA 4.0 子集被排除在导入之外。" |
| 14. Credit line draft | "Source: Biodiversity Heritage Library, item 318921. Public domain (per-page copyright status filter applied)." |
| Proposed section | Section 3 (复制) |
| **v4.4 status** | **`ready-for-asset-import` — PD subset only; CC BY-NC-SA subset blocked** |
| Required pre-import action | Same as C-01: re-open the item page, pick the per-page record, filter to `<Copyright Status> = Public domain`. **CC BY-NC-SA subset rejected.** |

---

### Row C-06 — Smithsonian NMNH herbarium sheet, CC0 (Section 2 分类)

| Field | Value |
|---|---|
| 1. Official item URL | https://collections.nmnh.si.edu/search/botany/ (NMNH Botany Department collections search entry — **not yet an item-level record**) |
| 2. Institution | Smithsonian National Museum of Natural History / NMNH Botany |
| 3. Title | (not selected — per-item title pending v4.4b) |
| 4. Creator / maker | (not selected — per-item collector pending v4.4b) |
| 5. Date | (not selected — per-item date pending v4.4b) |
| 6. Object / item identifier | (not selected — per-item accession number pending v4.4b) |
| 7. Rights statement | Smithsonian Open Access / **CC0 1.0** (to be confirmed per item) |
| 8. Rights / terms URL | https://www.si.edu/openaccess/faq |
| 9. Image URL or IIIF URL | Per-item image URL is locatable on the per-item record; **v4.4 records the entry URL only, not a per-item image** |
| 10. Proposed local filename | `nmnh-<accession_number>.jpg` (accession number pending v4.4b) |
| 11. Proposed alt text | (pending v4.4b — depends on selected specimen) |
| 12. Caption draft | (pending v4.4b) |
| 13. Source note draft | (pending v4.4b — basis: NMNH Botany CC0 1.0) |
| 14. Credit line draft | (pending v4.4b — template: "Source: Smithsonian National Museum of Natural History, NMNH Botany, accession <N>. CC0 1.0.") |
| Proposed section | Section 2 (分类) |
| **v4.4 status** | **`defer`** (per-item selection deferred to v4.4b) |
| Required pre-import action | Run NMNH Botany search in v4.4b. Pick a specific CC0-marked record with an image. Capture title, collector / maker, date, accession number, official record URL, media URL. Confirm CC0 1.0 on the per-item page. |

---

### Row C-08 — Met CC0 image, Section 3 alternate (Section 3 复制 alternate)

| Field | Value |
|---|---|
| 1. Official item URL | https://www.metmuseum.org/art/collection/search/285149 |
| 2. Institution | The Metropolitan Museum of Art |
| 3. Title | [Botanical Specimen: Fern] |
| 4. Creator / maker | Unknown |
| 5. Date | 1860s |
| 6. Object / item identifier | **285149 / 2003.562.3** |
| 7. Rights statement | Public domain (**double-confirmation still required**: Collection API `isPublicDomain: true` AND Open Access icon on the public object page) |
| 8. Rights / terms URL | https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources |
| 9. Image URL or IIIF URL | Met Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` → `primaryImage` / `primaryImageSmall` field. **URL recorded; do not download.** |
| 10. Proposed local filename | `met-285149.jpg` |
| 11. Proposed alt text | "大都会艺术博物馆所藏 19 世纪 60 年代蕨类植物标本银盐蛋白相片。" |
| 12. Caption draft | "大都会艺术博物馆藏品，[Botanical Specimen: Fern]，作者佚名，约 1860 年代，albumen silver print，馆藏编号 2003.562.3。作为第三展区《复制》的备选视觉标本——摄影术进入植物图像记录的早期形态。" |
| 13. Source note draft | "图像来源 The Metropolitan Museum of Art, object 285149 / accession 2003.562.3。Public domain 由 Collection API `isPublicDomain: true` 与公开页 Open Access 图标双重确认。" |
| 14. Credit line draft | "Source: The Metropolitan Museum of Art, object 285149 (accession 2003.562.3). Public domain (double-confirmation: API + public page)." |
| Proposed section | Section 3 (复制) — alternate |
| **v4.4 status** | **`defer`** (double-confirmation pending v4.4b) |
| Required pre-import action | Re-open Met object 285149 in v4.4b. Run double-confirmation: `isPublicDomain: true` in the Collection API **and** Open Access icon on the public object page. Capture the primary image URL. If either confirmation fails, C-08 is `blocked-from-import` and the Section 3 alternate slot is filled by a project-generated diagram. |

---

### Row C-09 — Rijksmuseum botanical print (Section 1 观察 primary / Section 2 分类 alternate)

| Field | Value |
|---|---|
| 1. Official item URL | https://www.rijksmuseum.nl/en/research/our-research/print-room (Rijksprentenkabinet entry — **not yet an item-level record**) |
| 2. Institution | Rijksmuseum / Rijksprentenkabinet |
| 3. Title | (not selected — per-item title pending v4.4b) |
| 4. Creator / maker | (not selected — per-item creator pending v4.4b) |
| 5. Date | (not selected — per-item date pending v4.4b) |
| 6. Object / item identifier | `objectNumber` + `id.rijksmuseum.nl/...` PID (pending v4.4b) |
| 7. Rights statement | Rijksmuseum two-tier policy: **`CC0 1.0`** (no longer in copyright) **or `CC BY 4.0`** (third-party grant). Per-item `licence` field recorded verbatim in v4.4b. |
| 8. Rights / terms URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| 9. Image URL or IIIF URL | Per-item Rijksstudio image URL or IIIF Image API URL. **v4.4 records the entry URL only, not a per-item image.** |
| 10. Proposed local filename | `rijksmuseum-<object_number>.jpg` (object number pending v4.4b) |
| 11. Proposed alt text | (pending v4.4b — depends on selected object) |
| 12. Caption draft | (pending v4.4b) |
| 13. Source note draft | (pending v4.4b — basis: Rijksmuseum per-item `licence` field) |
| 14. Credit line draft | (pending v4.4b — template: "Source: Rijksmuseum, object <object_number>. <licence field verbatim>.") |
| Proposed section | Section 1 (观察) primary / Section 2 (分类) alternate |
| **v4.4 status** | **`defer`** (per-item selection + per-item `licence` field deferred to v4.4b) |
| Required pre-import action | Pick a specific Rijksprentenkabinet object in v4.4b. Record the exact per-item `licence` field, `objectNumber`, `id.rijksmuseum.nl/...` PID, and image / IIIF URL. |

---

### Row C-10 — Rijksmuseum IIIF Presentation API manifest (Section 4 再组织)

| Field | Value |
|---|---|
| 1. Official item URL | https://www.rijksmuseum.nl/en/research/our-research/print-room (Rijksprentenkabinet entry — **not yet an item-level record**) |
| 2. Institution | Rijksmuseum / Rijksprentenkabinet |
| 3. Title | (not selected — per-item title pending v4.4b) |
| 4. Creator / maker | (not selected — per-item creator pending v4.4b) |
| 5. Date | (not selected — per-item date pending v4.4b) |
| 6. Object / item identifier | `objectNumber` + `id.rijksmuseum.nl/...` PID (pending v4.4b) |
| 7. Rights statement | Rijksmuseum two-tier policy: **`CC0 1.0`** or **`CC BY 4.0`**. Per-item `licence` field recorded verbatim in v4.4b. The IIIF Presentation API manifest's `license` field is the authoritative source. |
| 8. Rights / terms URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| 9. Image URL or IIIF URL | Rijksmuseum IIIF Presentation API manifest URL is on the per-item Catalogue record (URL pending v4.4b). |
| 10. Proposed local filename | (derives from C-09's per-item image; same Rijksmuseum object; pending v4.4b) |
| 11. Proposed alt text | (pending v4.4b) |
| 12. Caption draft | (pending v4.4b) |
| 13. Source note draft | (pending v4.4b — basis: IIIF Presentation API manifest `license` field) |
| 14. Credit line draft | (pending v4.4b — template: "Source: Rijksmuseum, IIIF manifest of object <object_number>. <licence field verbatim>.") |
| Proposed section | Section 4 (再组织) |
| **v4.4 status** | **`defer`** (per-item selection + per-item `licence` field deferred to v4.4b) |
| Required pre-import action | Same as C-09 — pick a specific Rijksprentenkabinet object in v4.4b. Capture the IIIF Presentation API manifest URL and the `license` field. |

---

## Selection totals (v4.4)

| Status | Count |
|---|---|
| `ready-for-asset-import` | **2** (C-01, C-03 — both anchored on BHL item 318921 with PD-subset enforcement) |
| `defer` | **4** (C-06, C-08, C-09, C-10 — per-item selection is a v4.4b step) |
| `blocked-from-import` | **0 row-level** (C-14 row is outside the v4.3 selected set; C-03 CC BY-NC-SA subset blocked at per-page level but does not create a separate row) |
| `replace-with-project-generated-diagram` | **0 row-level** (v4.1 carry-overs are fallback-only; they do not enter the v4.4 import-readiness table) |
| `approved` | **0** (not used) |
| Approved asset count | **0** (none in v4.4) |
| Downloaded image count | **0** (v4.4 records URLs only) |

**Threshold check.** `ready-for-asset-import` count = **2 < 4**. The next round is **v4.4b — Source Gap Fix**, not v4.5 — Asset Import.

---

## Round boundary

v4.4 ends with:

- All 5 v4.4 prep docs committed (`ASSET_IMPORT_PREP_v4.4.md`, `ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md`, `SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md`, `CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md`, `ASSET_FILENAME_MAP_v4.4.md`).
- `README.md` v4.4 block committed (and corrected: v4.4 does **not** download images).
- `docs/V4_ROADMAP.md` v4.4 section annotated (v4.4 is "Asset Import Prep", not "QA and Stable Freeze"; the freeze round is renumbered to a later phase).
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `scripts/template_quality_gate.py` is **empty**.
- Live byte size still **92,976 B**, v2.9 marker still present, `image-placeholder-pro` still **0**.
- `find` confirms no new image files.
- `ready-for-asset-import` count = 2 (recorded as < 4 → v4.4b is the next round).
- `approved` does not appear as a status value in any v4.4 doc.
- C-03's `CC BY-NC-SA subset blocked` is recorded.
- C-08's `double-confirmation` is recorded.
- C-09 / C-10's `licence field` is recorded.
- No new tag, no new GitHub Release.

The next round is **v4.4b — Source Gap Fix**.