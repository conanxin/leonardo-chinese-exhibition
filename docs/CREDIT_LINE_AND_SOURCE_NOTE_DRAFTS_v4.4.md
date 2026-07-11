# v4.4 Credit Line and Source Note Drafts

> Scope of this document: per-row drafts of the credit line and the source note for the 6 v4.3 `selected-for-build-planning` candidates. v4.4 only writes the drafts — no row is finalised until v4.4b (for the deferred rows) or v4.5 (for the actual import). The 4 v4.4 statuses are `ready-for-asset-import` / `defer` / `blocked-from-import` / `replace-with-project-generated-diagram`. The status `approved` is **not used**.

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

---

## Drafting rules

1. The credit line and the source note are written in **English**, with optional zh context where useful.
2. The credit line is the **short attribution** that appears in the asset caption / alt text.
3. The source note is the **longer explanation** that appears in the project's source-audit notes (and is the basis for the future manifest's `source_note` field).
4. The credit line must reference the institution's **own page language** (e.g., "Public domain" vs "CC0 1.0" vs "CC BY 4.0" vs "no longer in copyright"), not a project-invented phrase. The phrase "safe for commercial use" is **not used**.
5. The credit line must reference the institution's per-item identifier, not the project-local filename.
6. For BHL, the per-page `<Copyright Status>` filter is recorded explicitly in the source note (so the CC BY-NC-SA subset is excluded from the import set on the record).

---

## Per-row drafts

### Row C-01 — BHL page-level plate (Section 1 观察)

| Field | Value |
|---|---|
| Candidate ID | C-01 |
| Section | Section 1 (观察) |
| v4.4 status | `ready-for-asset-import` |
| Local filename | `bhl-318921-plate.jpg` |

**Credit line (English).**

> Source: Biodiversity Heritage Library, item 318921. Public domain (per-page copyright status filter applied).

**Source note (English).**

> Page-level image downloaded from BHL item 318921, *Album of watercolors of Asian fruits and flowers*, watercolor artist unknown, between 1798 and 1850. The per-page `<Copyright Status>` field is filtered to `Public domain` only; the CC BY-NC-SA 4.0 in-copyright subset is rejected and not part of the import set. BHL's reuse terms (https://about.biodiversitylibrary.org/help/copyright-and-reuse/) apply; the institution's own page language ("Public domain") is the basis of the credit line.

**Source note (中文).**

> 页图像下载自 BHL item 318921（《水彩绘亚洲水果与花卉图谱》，作者佚名，1798—1850 年间）。下载时按页的 `<Copyright Status>` 字段过滤为 `Public domain` 子集；CC BY-NC-SA 4.0 在版权期内子集被排除，不进入导入集合。Reuse 条款参见 BHL 官方页面（https://about.biodiversitylibrary.org/help/copyright-and-reuse/）。

---

### Row C-03 — BHL title-level book record, PD subset only (Section 3 复制)

| Field | Value |
|---|---|
| Candidate ID | C-03 |
| Section | Section 3 (复制) |
| v4.4 status | `ready-for-asset-import` — PD subset only; CC BY-NC-SA subset blocked |
| Local filename | `bhl-318921-page.jpg` |

**Credit line (English).**

> Source: Biodiversity Heritage Library, item 318921. Public domain (per-page copyright status filter applied).

**Source note (English).**

> Title-level book record: BHL item 318921, *Album of watercolors of Asian fruits and flowers*, watercolor artist unknown, between 1798 and 1850. The image is downloaded at the per-page level; the per-page `<Copyright Status>` is filtered to `Public domain` only. The CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at the per-page level and is not part of the import set. BHL's reuse terms (https://about.biodiversitylibrary.org/help/copyright-and-reuse/) apply.

**Source note (中文).**

> 书级条目（BHL item 318921）。下载时按页过滤为 `Public domain` 子集；CC BY-NC-SA 4.0 在版权期内子集被排除。Reuse 条款参见 BHL 官方页面。

---

### Row C-06 — Smithsonian NMNH herbarium sheet, CC0 (Section 2 分类)

| Field | Value |
|---|---|
| Candidate ID | C-06 |
| Section | Section 2 (分类) |
| v4.4 status | `defer` (per-item selection deferred to v4.4b) |
| Local filename | `nmnh-<accession_number>.jpg` (pending v4.4b) |

**Credit line template (English) — fill at v4.4b.**

> Source: Smithsonian National Museum of Natural History, NMNH Botany, accession <accession_number>. CC0 1.0.

**Source note template (English) — fill at v4.4b.**

> Specimen image downloaded from the Smithsonian NMNH Botany collections search (https://collections.nmnh.si.edu/search/botany/). The per-item accession number, collector, date, and media URL are recorded on the day of import. Rights basis: Smithsonian Open Access / CC0 1.0, confirmed on the per-item page (https://www.si.edu/openaccess/faq).

**Source note template (中文) — v4.4b 填写.**

> 标本图像下载自 Smithsonian NMNH Botany 检索页（https://collections.nmnh.si.edu/search/botany/）。下载当日记录入藏号、采集者、日期、图像 URL。权利基础：Smithsonian Open Access / CC0 1.0，以当日 per-item 页为准（https://www.si.edu/openaccess/faq）。

---

### Row C-08 — Met CC0 image, Section 3 alternate

| Field | Value |
|---|---|
| Candidate ID | C-08 |
| Section | Section 3 (复制) — alternate |
| v4.4 status | `defer` (double-confirmation pending v4.4b) |
| Local filename | `met-285149.jpg` |

**Credit line (English) — finalised at v4.4b after double-confirmation.**

> Source: The Metropolitan Museum of Art, object 285149 (accession 2003.562.3). Public domain (double-confirmation: Collection API `isPublicDomain: true` and public-page Open Access icon).

**Source note (English) — finalised at v4.4b after double-confirmation.**

> Image downloaded from The Metropolitan Museum of Art, object 285149, *[Botanical Specimen: Fern]*, creator unknown, 1860s, accession 2003.562.3. Rights basis: Public domain, double-confirmed by (a) Collection API record `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` showing `isPublicDomain: true`, and (b) Open Access icon on the public object page `https://www.metmuseum.org/art/collection/search/285149`. Met's image-resources terms (https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources) apply. If either confirmation fails, C-08 is `blocked-from-import` and the Section 3 alternate slot is filled by a project-generated diagram.

**Source note (中文).**

> 图像下载自 The Metropolitan Museum of Art, object 285149（[Botanical Specimen: Fern]，作者佚名，1860 年代，馆藏 2003.562.3）。权利基础：Public domain，双重确认依据（a）Collection API 记录的 `isPublicDomain: true` 与（b）公开页 Open Access 图标。条款参见 Met image-resources 页（https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources）。任一确认失败则 C-08 改为 `blocked-from-import`，Section 3 alternate 由项目自绘示意图填充。

---

### Row C-09 — Rijksmuseum botanical print (Section 1 观察 primary / Section 2 分类 alternate)

| Field | Value |
|---|---|
| Candidate ID | C-09 |
| Section | Section 1 (观察) primary / Section 2 (分类) alternate |
| v4.4 status | `defer` (per-item selection + per-item `licence` field deferred to v4.4b) |
| Local filename | `rijksmuseum-<object_number>.jpg` |

**Credit line template (English) — fill at v4.4b with the per-item `licence` field.**

> Source: Rijksmuseum, object <object_number>. <licence field verbatim, e.g., "CC0 1.0" or "CC BY 4.0">.

**Source note template (English) — fill at v4.4b.**

> Print image downloaded from the Rijksmuseum Rijksprentenkabinet (https://www.rijksmuseum.nl/en/research/our-research/print-room). Per-item record: `objectNumber` + `id.rijksmuseum.nl/...` PID. Rights basis: per-item `licence` field recorded verbatim. Rijksmuseum's data-policy (https://data.rijksmuseum.nl/policy/information-and-data-policy) applies.

**Source note template (中文) — v4.4b 填写.**

> 图像下载自 Rijksmuseum Rijksprentenkabinet（https://www.rijksmuseum.nl/en/research/our-research/print-room）。Per-item 记录含 `objectNumber` 与 `id.rijksmuseum.nl/...` PID。权利基础：逐字记录 per-item `licence` 字段。条款参见 Rijksmuseum data-policy 页（https://data.rijksmuseum.nl/policy/information-and-data-policy）。

---

### Row C-10 — Rijksmuseum IIIF Presentation API manifest (Section 4 再组织)

| Field | Value |
|---|---|
| Candidate ID | C-10 |
| Section | Section 4 (再组织) |
| v4.4 status | `defer` (per-item selection + per-item `license` field deferred to v4.4b) |
| Local filename | derived from C-09's per-item image (same Rijksmuseum object) |

**Credit line template (English) — fill at v4.4b.**

> Source: Rijksmuseum, IIIF manifest of object <object_number>. <licence field verbatim, e.g., "CC0 1.0" or "CC BY 4.0">.

**Source note template (English) — fill at v4.4b.**

> The IIIF Presentation API manifest URL is on the per-item Catalogue record of the Rijksmuseum. The manifest's `license` field is the authoritative source for the credit line. The image bytes are downloaded from the per-item Rijksstudio image URL or IIIF Image API URL (same `objectNumber` as C-09).

**Source note template (中文) — v4.4b 填写.**

> IIIF Presentation API manifest URL 位于 Rijksmuseum per-item Catalogue record。manifest 的 `license` 字段为 credit line 的权威来源。图像字节下载自 per-item Rijksstudio image URL 或 IIIF Image API URL（与 C-09 同一 `objectNumber`）。

---

## Why these are drafts

A credit line / source note is only `final` once:

1. The per-item image has been downloaded and the proposed filename is verified.
2. The per-item rights statement has been re-read on the institution's page on the day of download.
3. For BHL: the per-page `<Copyright Status>` has been verified to be `Public domain` (not CC BY-NC-SA).
4. For Met: the double-confirmation has passed.
5. For Rijksmuseum: the per-item `licence` field has been recorded verbatim.

In v4.4, none of those conditions hold (v4.4 records URLs only, downloads nothing). The credit lines and source notes above are therefore `DRAFT` and will graduate to `final` in v4.4b (for the rows that flip from `defer` to `ready-for-asset-import`) or v4.5 (after the actual download).

---

## Forbidden phrases

The following phrases must **not** appear in any v4.4 or later credit line or source note:

- "safe for commercial use"
- "approved" (used as a project status)
- "no attribution required" (project-invented; the institution's own page language is the basis)

---

## Round boundary

The next round is **v4.4b — Source Gap Fix**, which closes the gap by picking the deferred candidates' specific items and finalising the credit-line / source-note drafts.