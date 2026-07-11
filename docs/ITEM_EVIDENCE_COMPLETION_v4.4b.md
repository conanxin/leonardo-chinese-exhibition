# v4.4b Item Evidence Completion

> Scope: per-candidate per-item evidence for C-06, C-08, C-09, C-10 (all `defer` in v4.4, all `ready-for-asset-import` in v4.4b). The 2 v4.4 `ready-for-asset-import` rows (C-01, C-03) are unchanged and carried over from v4.4. v4.4b only records URLs and identifiers — **no image is downloaded in v4.4b**, and **no image file is created in v4.4b**. v4.4b status values: `ready-for-asset-import` or `defer` only. The status `approved` is **not used**.

> 收口时间：v4.4b source gap fix round 结束点。下一 round 是 **v4.5 asset import**。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `ad66d6db39622c19e8dc50238da1d9403defa7e9` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | **92,976 B** (preserved, v4.4b does not modify `site/`) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| Item-level / source-level sources checked in v4.4 | 6 |
| Item-level / source-level sources checked in v4.4b | 4 (C-06, C-08, C-09, C-10 — promoted from defer to per-item) |

---

## Item / source evidence table (6 rows, post-v4.4b)

| ID | Institution | Official item/source URL | Title | Creator / maker | Date | Identifier | Rights statement | Rights / terms URL | Image / IIIF URL known | v4.4b status |
|---|---|---|---|---|---|---|---|---|---|---|
| **C-01** | Biodiversity Heritage Library | https://www.biodiversitylibrary.org/item/318921 | Album of watercolors of Asian fruits and flowers | Unknown (watercolor artist) | between 1798 and 1850? | BHL item 318921 | Public domain (per-page / per-item `<Copyright Status>` filter; CC BY-NC-SA subset rejected at per-page / per-volume level) | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ | Yes — per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `ready-for-asset-import` |
| **C-03** | Biodiversity Heritage Library | https://www.biodiversitylibrary.org/item/318921 | Album of watercolors of Asian fruits and flowers | Unknown (watercolor artist) | between 1798 and 1850? | BHL item 318921 | Public domain (PD subset only); CC BY-NC-SA 4.0 in-copyright subset = `blocked-from-import` at per-page / per-volume level | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ | Yes — per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `ready-for-asset-import` (PD subset only) |
| **C-06** | Smithsonian National Museum of Natural History / NMNH Botany | https://collections.nmnh.si.edu/search/botany/?bc=00103617 (per-item URL); collection entry: https://collections.nmnh.si.edu/search/botany/ | Aconitum bulbilliferum Hand.-Mazz. (Ranunculaceae, Type fragment) | Handel-Mazzetti, H. R. (collector) | 17 Sep 1914 | US Catalog No. 1529703; Barcode 00103617; EZID `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920` | Dataset-level CC0 1.0 (verified on IPT page + GBIF dataset metadata). Per-item record is reachable on the day of audit. | https://www.si.edu/openaccess/faq; https://creativecommons.org/publicdomain/zero/1.0/legalcode (CC0 1.0) | Yes — `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes` (HEAD test returned HTTP/2 200, `Content-Type: image/png`; URL recorded, not downloaded) | `ready-for-asset-import` |
| **C-08** | The Metropolitan Museum of Art | https://www.metmuseum.org/art/collection/search/285149 | [Botanical Specimen: Fern] | Unknown (British) | 1855–60 | 285149 / 2003.562.3 | Public domain (double-confirmation: Collection API `isPublicDomain: true` AND "Public Domain" button on public object page) | https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources | Yes — `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` (URL recorded, not downloaded) | `ready-for-asset-import` |
| **C-09** | Rijksmuseum / Rijksprentenkabinet | https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da | Zeestreepvaren | Anna Atkins (photographer), England | c. 1854 | objectNumber `RP-F-F80152`; persistent URL `https://id.rijksmuseum.nl/200407820` | Public domain (per-item Copyright field on the public object page, with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`); Rijksmuseum two-tier policy `CC0 1.0` / `CC BY 4.0` confirmed via the data-policy page | https://data.rijksmuseum.nl/policy/information-and-data-policy; https://creativecommons.org/publicdomain/mark/1.0/deed.en | Yes — Micrio IIIF Image API: `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded) | `ready-for-asset-import` |
| **C-10** | Rijksmuseum / Rijksprentenkabinet | https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f | Wolfsklauw | Anna Atkins (photographer), England | c. 1854 | objectNumber `RP-F-F80313`; persistent URL `https://id.rijksmuseum.nl/200408260` | Public domain (per-item Copyright field on the public object page, with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`) | https://data.rijksmuseum.nl/policy/information-and-data-policy; https://creativecommons.org/publicdomain/mark/1.0/deed.en | Yes — Micrio IIIF Image API: `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded) | `ready-for-asset-import` |

---

## Source-level vs item-level clarification (post-v4.4b)

| ID | Source level in v4.4 | Source level in v4.4b |
|---|---|---|
| C-01 | item-level | item-level (unchanged) |
| C-03 | item-level | item-level (unchanged) |
| C-06 | **collection / search-level only** | **item-level** (US Catalog No. 1529703 picked in v4.4b) |
| C-08 | item-level | item-level (unchanged — Met object 285149 was already specific in v4.4) |
| C-09 | **collection / policy-level only** | **item-level** (RP-F-F80152 picked in v4.4b) |
| C-10 | **collection / policy-level only** | **item-level** (RP-F-F80313 picked in v4.4b — distinct per-item record from C-09) |

---

## Per-row v4.4b evidence details

### C-06 — NMNH Botany per-item record (picked in v4.4b)

- **Item URL**: `https://collections.nmnh.si.edu/search/botany/?bc=00103617` (per-item barcode querystring; per-item record is the search result for `bc=00103617`).
- **Per-item title (verbatim)**: `111-017 : Aconitum bulbilliferum Hand.-Mazz. : Ranunculaceae : Ranunculales : Dicotyledonae`.
- **Kind**: Pressed specimen.
- **Special Collections**: Type Register.
- **US Catalog Number**: 1529703.
- **Barcode**: 00103617.
- **Collector**: Handel-Mazzetti, H. R. (collection number 5202).
- **Date Collected**: 17 Sep 1914.
- **Country / State**: China / Sichuan (Biogeographic Region: 36 - China South-Central).
- **EZID (stable identifier)**: `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920`.
- **fiche number**: 0268/D09.
- **Rights basis**: NMNH Botany dataset-level CC0 1.0 (verified on `https://collections.nmnh.si.edu/ipt/resource?r=nmnh_botany` — "License: CC0 1.0", "publisher has waived all rights to these data and has dedicated them to the Public Domain (CC0 1.0). Users may copy, modify, distribute and use the work, including for commercial purposes, without restriction."). Cross-confirmed on `https://www.gbif.org/dataset/821cc27a-e3bb-4bc5-ac34-89ada245069d` — "Licence CC0 1.0".
- **Image URL pattern (template, not per-record IRN-resolved)**: `https://collections.nmnh.si.edu/media/?i={catalog_number}&ph=yes&thumb=yes`. Verified `?i=1529703` → HTTP/2 200, `Content-Type: image/png`. URL recorded only; do NOT download in v4.4b.
- **CC0 1.0 link**: https://creativecommons.org/publicdomain/zero/1.0/legalcode

### C-08 — Met object 285149 (double-confirmed in v4.4b)

- **Item URL**: `https://www.metmuseum.org/art/collection/search/285149`.
- **Collection API**: `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149`. API response (verified): `isPublicDomain: true`; `primaryImage: https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg`; `primaryImageSmall: https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg`; `title: [Botanical Specimen: Fern]`; `accessionNumber: 2003.562.3`; `objectDate: 1855–60`; `objectBeginDate: 1855`; `objectEndDate: 1860`; `medium: Albumen silver print from glass negative`; `department: Photographs`; `accessionYear: 2003`.
- **Public object page (verified)**: title `[Botanical Specimen: Fern]`; creator attribution `Unknown (British)` (note: this is the public-page wording; the API returns `culture: ""` and does not name a maker); date `1855–60`; "Not on view"; "Public Domain" button visible (Open Access icon); "Download Image" button visible; image dimensions 20.6 × 14.7 cm (8 1/8 × 5 13/16 in.); credit line `Gift of Simon Lowinsky, in memory of his uncle, Herbert Jonas, 2003`; accession `2003.562.3`.
- **Double-confirmation status**: PASS. (a) API `isPublicDomain: true` ✓. (b) Public-page "Public Domain" button + "Download Image" + "Enlarge Image" controls present ✓.
- **Image URL**: `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` (URL recorded only; do NOT download in v4.4b).

### C-09 — Rijksmuseum RP-F-F80152 (Zeestreepvaren, picked in v4.4b)

- **Item URL**: `https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da`.
- **Title (verbatim)**: `Zeestreepvaren`; title on object: `Asplenium marinum (title on object)`.
- **Maker (verbatim)**: `photographer: Anna Atkins, England`; maker role `photographer`.
- **Date**: `c. 1854`.
- **Material / technique**: `paper` + `cyanotype` (object type: `photogram`).
- **Dimensions**: height 247 mm × width 193 mm.
- **objectNumber**: `RP-F-F80152`.
- **Persistent URL (id.rijksmuseum.nl PID)**: `https://id.rijksmuseum.nl/200407820`.
- **Rijksstudio image URL pattern (Micrio IIIF Image API)**: `https://iiif.micr.io/{micrioId}/full/{max},/0/default.jpg`. For Zeestreepvaren, micrioId = `vGipU`. Verified `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` → HTTP/2 200, `Content-Type: image/jpeg`. URL recorded only; do NOT download in v4.4b.
- **Rights basis (per-item Copyright field on the public object page)**: `Public domain` (links to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`). Rijksmuseum's two-tier policy `CC0 1.0` / `CC BY 4.0` confirmed via the data-policy page (https://data.rijksmuseum.nl/policy/information-and-data-policy). The per-item Copyright field on the public object page is the authoritative source for the credit line.

### C-10 — Rijksmuseum RP-F-F80313 (Wolfsklauw, picked in v4.4b — distinct from C-09)

- **Item URL**: `https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f`.
- **Title (verbatim)**: `Wolfsklauw`.
- **Maker (verbatim)**: `photographer: Anna Atkins` (same photographer as C-09; distinct object, distinct objectNumber, distinct persistent URL, distinct IIIF Image API URL).
- **Date**: `c. 1854`.
- **objectNumber**: `RP-F-F80313`.
- **Persistent URL (id.rijksmuseum.nl PID)**: `https://id.rijksmuseum.nl/200408260`.
- **Rijksstudio image URL pattern (Micrio IIIF Image API)**: `https://iiif.micr.io/{micrioId}/full/{max},/0/default.jpg`. For Wolfsklauw, micrioId = `PrcdN`. Verified `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` → HTTP/2 200, `Content-Type: image/jpeg`. URL recorded only; do NOT download in v4.4b.
- **Rights basis (per-item Copyright field on the public object page)**: `Public domain` (links to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`).
- **IIIF Presentation API manifest note**: Rijksmuseum uses Micrio IIIF Image API; the manifest URL `https://iiif.micr.io/PrcdN/manifest.json` returned HTTP/2 404. The authoritative source for the credit line is therefore the per-item public object page's Copyright field, **not** a missing Presentation API manifest.

---

## Selection totals (post-v4.4b)

| Status | Count | IDs |
|---|---|---|
| `ready-for-asset-import` | **6** | C-01, C-03, C-06, C-08, C-09, C-10 |
| `defer` | **0** | (none) |
| `blocked-from-import` row-level | **0** | (C-14 + C-03 CC BY-NC-SA subset are policy-level entries) |
| `replace-with-project-generated-diagram` row-level | **0** | (none) |
| `approved` | **0** | (not used in v4.4b or any future round) |

**Threshold check.** `ready-for-asset-import` count = **6 ≥ 4**. The next round is **v4.5 — Asset Import** (unblocked).

---

## Round boundary

v4.4b ends with:

- All v4.4b docs committed (`SOURCE_GAP_FIX_v4.4b.md`, `ITEM_EVIDENCE_COMPLETION_v4.4b.md`, `READY_FOR_ASSET_IMPORT_SHORTLIST_v4.4b.md`, `ASSET_IMPORT_DECISION_LOG_v4.4b.md`, `ASSET_FILENAME_MAP_UPDATE_v4.4b.md`).
- `docs/V4_ROADMAP.md` v4.4b section committed.
- `README.md` v4.4b block committed.
- v4.4 report carries commit SHA + verified live byte + verified quality-gate three-piece evidence.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- No new image files.
- No new tag, no new GitHub Release.

The next round is **v4.5 — Asset Import**.