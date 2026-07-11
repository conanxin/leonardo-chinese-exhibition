# v4.5 — Imported Asset Inventory

This document is the **human-readable inventory** of the v4.5 second-exhibition asset set. The machine-readable counterpart is `second-exhibition/assets/asset-import-manifest.json`.

Round: **v4.5-asset-import** (partial: 5 of 6 ready candidates imported)
Status semantics: **imported-not-deployed**

---

## Imported (5)

### C-01 — Biodiversity Heritage Library, page 603998

| Field | Value |
|---|---|
| ID | C-01 |
| Institution | Biodiversity Heritage Library |
| Parent item | Album of watercolors of Asian fruits and flowers (BHL item 318921) |
| Selected page | BHL page 603998 (Pistillaria plate) |
| Page URL | https://www.biodiversitylibrary.org/page/603998 |
| Image URL | https://www.biodiversitylibrary.org/pageimage/603998 |
| Rights | Public domain per BHL per-page status |
| Rights URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| Filename | `second-exhibition/assets/images/bhl-318921-page-603998.webp` |
| Media type | image/webp |
| Bytes | 306126 |
| SHA-256 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` |
| Status | imported-not-deployed |
| Proposed section | Section 1 — botanical plate |

### C-03 — Biodiversity Heritage Library, page 603962

| Field | Value |
|---|---|
| ID | C-03 |
| Institution | Biodiversity Heritage Library |
| Parent item | Album of watercolors of Asian fruits and flowers (BHL item 318921) |
| Selected page | BHL page 603962 (Cycas revoluta plate) |
| Page URL | https://www.biodiversitylibrary.org/page/603962 |
| Image URL | https://www.biodiversitylibrary.org/pageimage/603962 |
| Rights | Public domain per BHL per-page status |
| Rights URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| Filename | `second-exhibition/assets/images/bhl-318921-page-603962.webp` |
| Media type | image/webp |
| Bytes | 262498 |
| SHA-256 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` |
| Status | imported-not-deployed |
| Proposed section | Section 3 — book/page example |
| Note | Distinct page from C-01 (SHA differs). CC BY-NC-SA subset pages of this item remain blocked. |

### C-08 — The Metropolitan Museum of Art, object 285149

| Field | Value |
|---|---|
| ID | C-08 |
| Institution | The Metropolitan Museum of Art |
| Title | [Botanical Specimen: Fern] |
| Creator | Unknown |
| Date | 1860s |
| Object ID | 285149 |
| Accession number | 2003.562.3 |
| Object URL | https://www.metmuseum.org/art/collection/search/285149 |
| Collection API URL | https://collectionapi.metmuseum.org/public/collection/v1/objects/285149 |
| Image URL used | https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg |
| Rights | The Met Open Access — public domain |
| Rights URL | https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources |
| Double-confirmation | API `isPublicDomain=true` AND public-page Public Domain indicator |
| Filename | `second-exhibition/assets/images/met-285149.jpg` |
| Media type | image/jpeg |
| Bytes | 95001 |
| SHA-256 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| Status | imported-not-deployed |
| Proposed section | Section 2 — institutional specimen comparison |

### C-09 — Rijksmuseum, object RP-F-F80152

| Field | Value |
|---|---|
| ID | C-09 |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Title | Zeestreepvaren |
| Creator | Anna Atkins |
| Date | c. 1854 |
| Object number | RP-F-F80152 |
| Persistent URL | https://id.rijksmuseum.nl/200408261 |
| Micrio ID | vGipU |
| Object URL | https://www.rijksmuseum.nl/en/collection/RP-F-F80152 |
| Image URL used (Micrio IIIF) | https://iiif.micr.io/vGipU/full/1024,/0/default.jpg |
| Per-item rights field | `Public domain` (verbatim from institution page) |
| Rights | Public domain / CC0 1.0 — **per-item**, not policy-level |
| Rights URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| Filename | `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` |
| Media type | image/jpeg |
| Bytes | 294445 |
| SHA-256 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| Status | imported-not-deployed |
| Proposed section | Section 3 — printed botanical reproduction |

### C-10 — Rijksmuseum, object RP-F-F80313

| Field | Value |
|---|---|
| ID | C-10 |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Title | Wolfsklauw |
| Creator | Anna Atkins |
| Date | c. 1854 |
| Object number | RP-F-F80313 |
| Persistent URL | https://id.rijksmuseum.nl/200408260 |
| Micrio ID | PrcdN |
| Object URL | https://www.rijksmuseum.nl/en/collection/RP-F-F80313 |
| Image URL used (Micrio IIIF) | https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg |
| Per-item rights field | `Public domain` (verbatim from institution page) |
| Rights | Public domain / CC0 1.0 — **per-item**, not policy-level |
| Rights URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| Filename | `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` |
| Media type | image/jpeg |
| Bytes | 191606 |
| SHA-256 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |
| Status | imported-not-deployed |
| Proposed section | Section 3 — printed botanical reproduction (companion to C-09) |
| Note | Presentation API `/manifest.json` returned HTTP 404; manifest-based evidence intentionally omitted. |

---

## Blocked-from-import (1)

### C-06 — Smithsonian NMNH Botany, catalog 1529703

| Field | Value |
|---|---|
| ID | C-06 |
| Institution | Smithsonian National Museum of Natural History / NMNH Botany |
| Catalog number | 1529703 |
| Expected taxon | Aconitum bulbilliferum (per v4.4b evidence; not re-verified in v4.5) |
| Record URL attempted | https://collections.nmnh.si.edu/search/botany/?irn=2793935 |
| Image URL attempted | (multiple — see `docs/ASSET_IMPORT_v4.5.md` C-06 section; all returned 404) |
| Rights | Smithsonian Open Access / CC0 1.0 — dataset-level only |
| Rights URL | https://www.si.edu/openaccess/faq |
| Filename | (none — no file imported) |
| Status | **blocked-from-import** |
| Blocked reason | Per brief: do not substitute search thumbnails, cached images, or third-party mirrors when source/rights verification fails. The candidate media URLs returned HTTP 404 and the catalog-number → irnstamp relationship could not be confirmed during v4.5. |
| Next round | `v4.5b-source-gap-fix` must (a) re-derive correct irnstamp for catalog 1529703, (b) confirm on-page taxon, (c) obtain a stable per-item media URL, (d) re-record CC0 1.0 basis from live si.edu Terms page. |

---

## Round totals

| Metric | Value |
|---|---|
| ready-for-asset-import at v4.4b | 6 |
| imported (status = imported-not-deployed) | 5 |
| blocked-from-import | 1 |
| deployed | 0 |
| approved | 0 (status word intentionally not used) |
| downloaded image files | 5 |
| new tags | 0 |
| new releases | 0 |
| live site changes | 0 |