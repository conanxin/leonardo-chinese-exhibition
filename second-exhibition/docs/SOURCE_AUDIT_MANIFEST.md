# Second Exhibition Source Audit Manifest

This manifest records the per-asset source evidence reviewed and accepted during v4.5-asset-import. It is the **audit-side** counterpart to `assets/asset-import-manifest.json`.

Round: **v4.5-asset-import**
Round status: **partial** (5 of 6 ready candidates imported; C-06 blocked-from-import)
Source tag: **v3.4-real-second-exhibition-hardening** (`81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`)

---

## C-01 — BHL page 603998

| Field | Value |
|---|---|
| Institution | Biodiversity Heritage Library |
| Parent item | Album of watercolors of Asian fruits and flowers (BHL item 318921) |
| Parent item URL | https://www.biodiversitylibrary.org/item/318921 |
| Selected page | BHL page 603998 (Pistillaria plate) |
| Page URL | https://www.biodiversitylibrary.org/page/603998 |
| Page image URL | https://www.biodiversitylibrary.org/pageimage/603998 |
| Rights basis | Public domain per BHL per-page status |
| Rights URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| Source URL | https://www.biodiversitylibrary.org/page/603998 |
| Identifier | BHL page 603998 |
| Creator | Unknown (watercolor artist) |
| Date | between 1798 and 1850? |
| Filename | `assets/images/bhl-318921-page-603998.webp` |
| Media type | image/webp |
| Bytes | 306126 |
| SHA-256 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` |
| Credit line draft | Album of watercolors of Asian fruits and flowers (page 603998) / Biodiversity Heritage Library / Public domain |
| Source note draft | BHL item 318921, page 603998. Source: https://www.biodiversitylibrary.org/page/603998 |
| Proposed section | Section 1 — botanical plate |
| Status | imported-not-deployed |
| Remaining caution | BHL per-page copyright status must be re-verified inside v4.5 build. CC BY-NC-SA subset pages of this item remain blocked. |

## C-03 — BHL page 603962

| Field | Value |
|---|---|
| Institution | Biodiversity Heritage Library |
| Parent item | Album of watercolors of Asian fruits and flowers (BHL item 318921) |
| Parent item URL | https://www.biodiversitylibrary.org/item/318921 |
| Selected page | BHL page 603962 (Cycas revoluta plate) |
| Page URL | https://www.biodiversitylibrary.org/page/603962 |
| Page image URL | https://www.biodiversitylibrary.org/pageimage/603962 |
| Rights basis | Public domain per BHL per-page status |
| Rights URL | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ |
| Source URL | https://www.biodiversitylibrary.org/page/603962 |
| Identifier | BHL page 603962 |
| Creator | Unknown (watercolor artist) |
| Date | between 1798 and 1850? |
| Filename | `assets/images/bhl-318921-page-603962.webp` |
| Media type | image/webp |
| Bytes | 262498 |
| SHA-256 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` |
| Credit line draft | Album of watercolors of Asian fruits and flowers (page 603962) / Biodiversity Heritage Library / Public domain |
| Source note draft | BHL item 318921, page 603962. Source: https://www.biodiversitylibrary.org/page/603962 |
| Proposed section | Section 3 — book/page example |
| Status | imported-not-deployed |
| Remaining caution | CC BY-NC-SA subset pages of this item remain blocked. Distinct page from C-01 (SHA differs). |

## C-06 — NMNH Botany catalog 1529703

| Field | Value |
|---|---|
| Institution | Smithsonian National Museum of Natural History / NMNH Botany |
| Catalog number | 1529703 |
| Expected taxon | Aconitum bulbilliferum (per v4.4b evidence; not independently re-verified in v4.5 round) |
| Record URL attempted | https://collections.nmnh.si.edu/search/botany/?irn=2793935 |
| Rights basis | Smithsonian Open Access / CC0 1.0 — dataset-level only. No per-item evidence confirmed in v4.5. |
| Rights URL | https://www.si.edu/openaccess/faq |
| Status | **blocked-from-import** |
| Blocked reason | NMNH candidate media URL paths returned HTTP 404 (NMNH Ke Emu system does not expose a stable per-item media URL for catalog 1529703). Per brief: no unverified replacement was substituted. |
| Inconsistency found | The irn value 2793935 in the v4.4b evidence maps to an NMNH Botany record whose page <title> reads "Rhynchanthus longiflorus, Myitkyina, Myanmar" — not the Aconitum bulbilliferum taxon recorded in v4.4b evidence. Relationship between catalog 1529703 and irn 2793935 could not be confirmed. |
| Remaining caution | v4.5b must (a) re-derive the correct irnstamp for catalog 1529703 from a fresh NMNH Botany search, (b) confirm on-page taxon, (c) obtain a stable per-item media URL, (d) re-record CC0 1.0 basis from the live si.edu Terms page. |

## C-08 — Met object 285149

| Field | Value |
|---|---|
| Institution | The Metropolitan Museum of Art |
| Object URL | https://www.metmuseum.org/art/collection/search/285149 |
| Collection API URL | https://collectionapi.metmuseum.org/public/collection/v1/objects/285149 |
| Title | [Botanical Specimen: Fern] |
| Creator | Unknown |
| Date | 1860s |
| Object ID | 285149 |
| Accession number | 2003.562.3 |
| Rights basis | The Met Open Access — public domain designation confirmed via Collection API `isPublicDomain=true` and public-page Public Domain indicator. |
| Rights URL | https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources |
| Source URL | https://www.metmuseum.org/art/collection/search/285149 |
| Identifier | Met object 285149 / accession 2003.562.3 |
| Double-confirmation | API `isPublicDomain=true` AND public-page Public Domain button observed during v4.5 verification. |
| Image URL recorded | https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg |
| Image URL (original) | https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg |
| Filename | `assets/images/met-285149.jpg` |
| Media type | image/jpeg |
| Bytes | 95001 |
| SHA-256 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| Credit line draft | [Botanical Specimen: Fern], 1860s / The Metropolitan Museum of Art, Gift of Russell C. Vail, 2003 / Public domain |
| Source note draft | The Metropolitan Museum of Art, object 285149 (accession 2003.562.3). Source: https://www.metmuseum.org/art/collection/search/285149 |
| Proposed section | Section 2 — institutional specimen comparison |
| Status | imported-not-deployed |
| Remaining caution | Credit line "Gift of Russell C. Vail, 2003" was recorded in v4.4b evidence; not re-confirmed inside v4.5 download. Page build must verify before publishing. |

## C-09 — Rijksmuseum object RP-F-F80152

| Field | Value |
|---|---|
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Object URL | https://www.rijksmuseum.nl/en/collection/RP-F-F80152 |
| Persistent URL | https://id.rijksmuseum.nl/200408261 |
| Micrio ID | vGipU |
| Title | Zeestreepvaren |
| Creator | Anna Atkins |
| Date | c. 1854 |
| Object number | RP-F-F80152 |
| Per-item Copyright field | Public domain (verbatim from institution object page) |
| Rights basis | Per-item Rijksmuseum Copyright field: Public domain (CC0 1.0). |
| Rights URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| Source URL | https://www.rijksmuseum.nl/en/collection/RP-F-F80152 |
| Identifier | RP-F-F80152 |
| Image URL recorded (Micrio IIIF) | https://iiif.micr.io/vGipU/full/1024,/0/default.jpg |
| og:image URL | https://iiif.micr.io/vGipU/full/1000,/0/default.jpg |
| Filename | `assets/images/rijksmuseum-rp-f-f80152.jpg` |
| Media type | image/jpeg |
| Bytes | 294445 |
| SHA-256 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| Credit line draft | Zeestreepvaren, Anna Atkins, c. 1854 / Rijksmuseum, object RP-F-F80152 / Public domain (CC0 1.0) |
| Source note draft | Rijksmuseum, object RP-F-F80152 (persistent URL https://id.rijksmuseum.nl/200408261). Source: https://www.rijksmuseum.nl/en/collection/RP-F-F80152 |
| Proposed section | Section 3 — printed botanical reproduction |
| Status | imported-not-deployed |
| Remaining caution | Object type is photogram (cyanotype), not traditional print. Page build must label accordingly. |

## C-10 — Rijksmuseum object RP-F-F80313

| Field | Value |
|---|---|
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Object URL | https://www.rijksmuseum.nl/en/collection/RP-F-F80313 |
| Persistent URL | https://id.rijksmuseum.nl/200408260 |
| Micrio ID | PrcdN |
| Title | Wolfsklauw |
| Creator | Anna Atkins |
| Date | c. 1854 |
| Object number | RP-F-F80313 |
| Per-item Copyright field | Public domain (verbatim from institution object page) |
| Rights basis | Per-item Rijksmuseum Copyright field: Public domain (CC0 1.0). |
| Rights URL | https://data.rijksmuseum.nl/policy/information-and-data-policy |
| Source URL | https://www.rijksmuseum.nl/en/collection/RP-F-F80313 |
| Identifier | RP-F-F80313 |
| Image URL recorded (Micrio IIIF) | https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg |
| og:image URL | https://iiif.micr.io/PrcdN/full/1000,/0/default.jpg |
| Presentation manifest | /manifest.json returned HTTP 404 — manifest evidence intentionally omitted. |
| Filename | `assets/images/rijksmuseum-rp-f-f80313.jpg` |
| Media type | image/jpeg |
| Bytes | 191606 |
| SHA-256 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |
| Credit line draft | Wolfsklauw, Anna Atkins, c. 1854 / Rijksmuseum, object RP-F-F80313 / Public domain (CC0 1.0) |
| Source note draft | Rijksmuseum, object RP-F-F80313 (persistent URL https://id.rijksmuseum.nl/200408260). Source: https://www.rijksmuseum.nl/en/collection/RP-F-F80313 |
| Proposed section | Section 3 — printed botanical reproduction (companion to C-09) |
| Status | imported-not-deployed |
| Remaining caution | Object type is photogram (cyanotype), not traditional print. Presentation manifest /manifest.json returned 404; manifest-based evidence intentionally omitted. |

---

## Round totals

| Metric | Value |
|---|---|
| ready-for-asset-import at v4.4b | 6 |
| imported in v4.5 | 5 |
| blocked-from-import in v4.5 | 1 (C-06) |
| deployed assets | 0 |
| approved assets | 0 (status word intentionally not used) |
| downloaded image files | 5 |
| new tags | 0 |
| new releases | 0 |
| live site changes | 0 |