# v4.4 Source Audit Manifest (DRAFT)

> Scope: per-candidate source-audit manifest draft for the 6 v4.3 `selected-for-build-planning` candidates. v4.4 only records evidence — **no image is downloaded in v4.4**, and **no image file is created in v4.4**. This manifest is marked `DRAFT`; the `final` version is written in v4.4b / v4.5 once the per-item image is actually downloaded and the rights statement is re-read on the day of import.

> 收口时间：v4.4 asset import prep round 结束点。下一 round 是 **v4.4b-source-gap-fix**，不是 v4.5。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `166e73cff276a8111f098da7c6ff674b39ff778d` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | **92,976 B** (preserved) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| Item-level sources checked | 2 (C-01, C-03) |
| Source-level sources checked | 4 (C-06, C-08, C-09, C-10) |

---

## Manifest rows

### C-01 — BHL pre-1928 Public-domain botanical plate (page-level) — Section 1 (观察)

- **Local path**: not downloaded (proposed: `second-exhibition/assets/images/bhl-318921-plate.jpg` — directory not yet created)
- **Official source URL**: https://www.biodiversitylibrary.org/item/318921
- **Image / IIIF URL**: per-page image URL reachable via BHL page-viewer (URL recorded; v4.4 does not download)
- **Institution**: Biodiversity Heritage Library (BHL)
- **Identifier**: BHL item 318921
- **Rights statement**: Public domain, but must filter per-page / per-item `<Copyright Status>` (CC BY-NC-SA subset rejected)
- **Rights / terms URL**: https://about.biodiversitylibrary.org/help/copyright-and-reuse/
- **Source note draft**: Page-level image downloaded from BHL item 318921, *Album of watercolors of Asian fruits and flowers*, watercolor artist unknown, between 1798 and 1850. Per-page `<Copyright Status>` filtered to `Public domain` only; CC BY-NC-SA 4.0 in-copyright subset rejected.
- **Credit line draft**: "Source: Biodiversity Heritage Library, item 318921. Public domain (per-page copyright status filter applied)."
- **Audit status**: `ready-for-asset-import`
- **Remaining caution**: Per-page `<Copyright Status>` must be `Public domain` at the time of download; CC BY-NC-SA 4.0 in-copyright subset is rejected.

### C-03 — BHL title-level book record (PD subset only) — Section 3 (复制)

- **Local path**: not downloaded (proposed: `second-exhibition/assets/images/bhl-318921-page.jpg` — directory not yet created)
- **Official source URL**: https://www.biodiversitylibrary.org/item/318921
- **Image / IIIF URL**: per-page image URL reachable via BHL page-viewer (URL recorded; v4.4 does not download)
- **Institution**: Biodiversity Heritage Library (BHL)
- **Identifier**: BHL item 318921
- **Rights statement**: Public domain (PD subset only); CC BY-NC-SA 4.0 in-copyright subset = `blocked-from-import` at per-page / per-volume level
- **Rights / terms URL**: https://about.biodiversitylibrary.org/help/copyright-and-reuse/
- **Source note draft**: Title-level book record: BHL item 318921, *Album of watercolors of Asian fruits and flowers*, watercolor artist unknown, between 1798 and 1850. Image downloaded at the per-page level; per-page `<Copyright Status>` filtered to `Public domain` only. CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at the per-page level.
- **Credit line draft**: "Source: Biodiversity Heritage Library, item 318921. Public domain (per-page copyright status filter applied)."
- **Audit status**: `ready-for-asset-import` (PD subset only)
- **Remaining caution**: CC BY-NC-SA subset blocked at the per-page level; do not promote CC BY-NC-SA pages to the import set.

### C-06 — NMNH herbarium sheet, CC0 — Section 2 (分类)

- **Local path**: not downloaded (proposed: `second-exhibition/assets/images/nmnh-<accession_number>.jpg` — directory not yet created; accession number pending v4.4b)
- **Official source URL**: https://collections.nmnh.si.edu/search/botany/
- **Image / IIIF URL**: per-item image URL is locatable on the per-item record (not yet selected in v4.4; v4.4 records the entry URL only)
- **Institution**: Smithsonian National Museum of Natural History / NMNH Botany
- **Identifier**: pending v4.4b (per-item accession number)
- **Rights statement**: Smithsonian Open Access / CC0 1.0 (to be confirmed per item in v4.4b)
- **Rights / terms URL**: https://www.si.edu/openaccess/faq
- **Source note draft (template)**: Specimen image downloaded from the Smithsonian NMNH Botany collections search (https://collections.nmnh.si.edu/search/botany/). Per-item accession number, collector, date, and media URL recorded on the day of import. Rights basis: Smithsonian Open Access / CC0 1.0, confirmed on the per-item page.
- **Credit line draft (template)**: "Source: Smithsonian National Museum of Natural History, NMNH Botany, accession <accession_number>. CC0 1.0."
- **Audit status**: `defer`
- **Remaining caution**: per-item record not selected yet; must be resolved in v4.4b.

### C-08 — Met CC0 image, Section 3 alternate — Section 3 (复制)

- **Local path**: not downloaded (proposed: `second-exhibition/assets/images/met-285149.jpg` — directory not yet created)
- **Official source URL**: https://www.metmuseum.org/art/collection/search/285149
- **Image / IIIF URL**: Met Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` → `primaryImage` / `primaryImageSmall` field (URL recorded; v4.4 does not download)
- **Institution**: The Metropolitan Museum of Art
- **Identifier**: 285149 / 2003.562.3
- **Rights statement**: Public domain, but **double-confirmation required** at v4.4b: Collection API `isPublicDomain: true` AND Open Access icon on the public object page
- **Rights / terms URL**: https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources
- **Source note draft**: Image downloaded from The Metropolitan Museum of Art, object 285149, *[Botanical Specimen: Fern]*, creator unknown, 1860s, accession 2003.562.3. Rights basis: Public domain, double-confirmed by (a) Collection API record `isPublicDomain: true` and (b) Open Access icon on the public object page.
- **Credit line draft**: "Source: The Metropolitan Museum of Art, object 285149 (accession 2003.562.3). Public domain (double-confirmation: Collection API + public page)."
- **Audit status**: `defer`
- **Remaining caution**: Double-confirmation pending. If either confirmation fails, C-08 is `blocked-from-import` and the Section 3 alternate slot is filled by a project-generated diagram.

### C-09 — Rijksmuseum botanical print (CC0 1.0 or CC BY 4.0) — Section 1 (观察) primary / Section 2 (分类) alternate

- **Local path**: not downloaded (proposed: `second-exhibition/assets/images/rijksmuseum-<object_number>.jpg` — directory not yet created; `objectNumber` pending v4.4b)
- **Official source URL**: https://www.rijksmuseum.nl/en/research/our-research/print-room (collection / policy-level entry; per-item record not yet selected)
- **Image / IIIF URL**: per-item Rijksstudio image URL or IIIF Image API URL (not yet selected in v4.4; v4.4 records the entry URL only)
- **Institution**: Rijksmuseum / Rijksprentenkabinet
- **Identifier**: pending v4.4b (`objectNumber` + `id.rijksmuseum.nl/...` PID)
- **Rights statement**: Rijksmuseum two-tier policy: `CC0 1.0` (no longer in copyright) or `CC BY 4.0` (third-party grant). Per-item `licence` field to be recorded verbatim in v4.4b.
- **Rights / terms URL**: https://data.rijksmuseum.nl/policy/information-and-data-policy
- **Source note draft (template)**: Print image downloaded from the Rijksmuseum Rijksprentenkabinet. Per-item record: `objectNumber` + `id.rijksmuseum.nl/...` PID. Rights basis: per-item `licence` field recorded verbatim.
- **Credit line draft (template)**: "Source: Rijksmuseum, object <object_number>. <licence field verbatim, e.g., "CC0 1.0" or "CC BY 4.0">."
- **Audit status**: `defer`
- **Remaining caution**: per-item record not selected yet; must be resolved in v4.4b. The per-item `licence` field must be recorded verbatim.

### C-10 — Rijksmuseum IIIF Presentation API manifest — Section 4 (再组织)

- **Local path**: not downloaded (derives from C-09's per-item image; same Rijksmuseum object)
- **Official source URL**: https://www.rijksmuseum.nl/en/research/our-research/print-room (collection / policy-level entry; per-item IIIF manifest not yet selected)
- **Image / IIIF URL**: Rijksmuseum IIIF Presentation API manifest URL is on the per-item Catalogue record (not yet selected in v4.4)
- **Institution**: Rijksmuseum / Rijksprentenkabinet
- **Identifier**: pending v4.4b (`objectNumber` + `id.rijksmuseum.nl/...` PID, same as C-09)
- **Rights statement**: Rijksmuseum two-tier policy: `CC0 1.0` or `CC BY 4.0`. The IIIF Presentation API manifest's `license` field is the authoritative source.
- **Rights / terms URL**: https://data.rijksmuseum.nl/policy/information-and-data-policy
- **Source note draft (template)**: The IIIF Presentation API manifest URL is on the per-item Catalogue record of the Rijksmuseum. The manifest's `license` field is the authoritative source for the credit line. Image bytes are downloaded from the per-item Rijksstudio image URL or IIIF Image API URL (same `objectNumber` as C-09).
- **Credit line draft (template)**: "Source: Rijksmuseum, IIIF manifest of object <object_number>. <licence field verbatim>."
- **Audit status**: `defer`
- **Remaining caution**: per-item record not selected yet; must be resolved in v4.4b. The IIIF Presentation API manifest `license` field must be recorded verbatim.

---

## Policy-level entries

These are not rows in the 6-row table, but they are policy-level entries that the future import round must respect.

| Policy entry | Status | Notes |
|---|---|---|
| C-14 (BHL CC BY-NC-SA — row-level block) | `blocked-from-import` | C-14 was `excluded` in v4.1; it must not be re-introduced as `ready-for-asset-import` in any future round. |
| C-03 CC BY-NC-SA 4.0 in-copyright subset (page-level block) | `blocked-from-import` | C-03 itself is `ready-for-asset-import` for the Public-domain subset only. The CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at the per-page / per-volume level. |

---

## Manifest totals (DRAFT)

| Bucket | Count |
|---|---|
| `ready-for-asset-import` | **2** (C-01, C-03) |
| `defer` | **4** (C-06, C-08, C-09, C-10) |
| `blocked-from-import` row-level | **0** |
| `replace-with-project-generated-diagram` row-level | **0** |
| `approved` | **0** (not used) |
| Total rows | 6 |

---

## Why this manifest is DRAFT

A manifest is only `final` once:

1. The per-item image has been downloaded into the repository under the proposed filename.
2. The image bytes have been re-checked (sha256 / file size).
3. The license field on the institution's page has been re-read on the day of download.

In v4.4, none of those three conditions hold (v4.4 records URLs only, downloads nothing). So this manifest is a `DRAFT` and the `final` version will be written in v4.4b or v4.5 once the source gap is closed.

---

## Round boundary

The next round is **v4.4b-source-gap-fix**, which closes the gap by picking the deferred candidates' specific items and re-running the v4.4 import-readiness assessment. v4.5 — Asset Import — is conditioned on v4.4b producing ≥ 4 `ready-for-asset-import` rows.