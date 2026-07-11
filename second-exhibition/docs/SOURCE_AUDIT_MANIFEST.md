# Second Exhibition — Source Audit Manifest

Round: **v4.5-asset-import**
Deployment status: **repository-only-not-deployed**

This manifest records per-asset source evidence that was reviewed and accepted during v4.5. It is the **audit-side** counterpart to `assets/asset-import-manifest.json`. The current round is **not** a legal opinion; the source/rights evidence is recorded for repository housekeeping only.

---

## C-01 — BHL page 603998

| Field | Value |
|---|---|
| Candidate ID | C-01 |
| Local path | `second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` |
| Institution | Biodiversity Heritage Library |
| Official source URL | https://www.biodiversitylibrary.org/page/603998 |
| Exact media URL | https://www.biodiversitylibrary.org/pageimage/603998 |
| Identifier | BHL item 318921 / page 603998 |
| Source note | Album of watercolors of Asian fruits and flowers, page 603998 (Pistillaria plate) |
| SHA-256 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` |
| Import status | imported-not-deployed |
| Remaining caution | BHL serves page images as WebP from `/pageimage/<id>`. The c01/c03 page-id suffix is added in v4.5 for traceability. Re-verify per-page Copyright Status inside v4.6 build before linking into a page. |

## C-03 — BHL page 603962

| Field | Value |
|---|---|
| Candidate ID | C-03 |
| Local path | `second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` |
| Institution | Biodiversity Heritage Library |
| Official source URL | https://www.biodiversitylibrary.org/page/603962 |
| Exact media URL | https://www.biodiversitylibrary.org/pageimage/603962 |
| Identifier | BHL item 318921 / page 603962 |
| Source note | Album of watercolors of Asian fruits and flowers, page 603962 (Cycas revoluta plate). **PD subset only.** |
| SHA-256 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` |
| Import status | imported-not-deployed |
| Remaining caution | Distinct page from C-01 (SHA differs). CC BY-NC-SA subset pages of BHL item 318921 remain blocked-from-import. |

## C-06 — NMNH Botany catalog 1529703

| Field | Value |
|---|---|
| Candidate ID | C-06 |
| Local path | `second-exhibition/assets/images/smithsonian-nmnh-1529703.png` |
| Institution | Smithsonian National Museum of Natural History / NMNH Botany |
| Official source URL | https://collections.nmnh.si.edu/search/botany/?ark=ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920 |
| Exact media URL | https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes |
| Identifier | US Catalog No. 1529703; Barcode 00103617; EZID ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920 |
| Source note | *Aconitum bulbilliferum* Hand.-Mazz. (Ranunculaceae, Type fragment), Handel-Mazzetti H. R. 5202, 17 Sep 1914, China / Sichuan. EZID redirector resolves to the NMNH Botany record page; media URL serves a 90x90 PNG thumbnail via the `/media/?i=...` endpoint. |
| SHA-256 | `75f523b06cc1a62713de51b1ba3a51fc4d43c4ac19268c48478d30c9e2af73a1` |
| Import status | imported-not-deployed |
| Remaining caution | The /media/?i=... endpoint serves a 90x90 PNG thumbnail. The high-resolution derivative URL was not exposed by the NMNH Ke Emu API at import time. Re-check inside v4.6 build and request a higher-resolution derivative via the NMNH IPT API if needed. |

## C-08 — Met object 285149

| Field | Value |
|---|---|
| Candidate ID | C-08 |
| Local path | `second-exhibition/assets/images/met-285149.jpg` |
| Institution | The Metropolitan Museum of Art |
| Official source URL | https://www.metmuseum.org/art/collection/search/285149 |
| Collection API URL | https://collectionapi.metmuseum.org/public/collection/v1/objects/285149 |
| Exact media URL | https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg |
| Identifier | Met object 285149 / accession 2003.562.3 |
| Source note | [Botanical Specimen: Fern], 1855–60, Gift of Russell C. Vail, 2003. Double-confirmation: (a) Collection API `isPublicDomain: true`; (b) public object page Public Domain indicator. |
| SHA-256 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| Import status | imported-not-deployed |
| Remaining caution | Used web-large derivative (1024 px on long edge) instead of original (3000+ px) to limit bandwidth. Original URL `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` was re-confirmed live during v4.5. |

## C-09 — Rijksmuseum RP-F-F80152

| Field | Value |
|---|---|
| Candidate ID | C-09 |
| Local path | `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Official source URL | https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da |
| Exact media URL | https://iiif.micr.io/vGipU/full/1024,/0/default.jpg |
| Identifier | objectNumber RP-F-F80152; persistent URL https://id.rijksmuseum.nl/200407820; Micrio ID vGipU |
| Source note | *Zeestreepvaren*, Anna Atkins (photographer, England), c. 1854, cyanotype on paper. Per-item Copyright field on the public object page reads verbatim `Public domain` (CC0 1.0 link). |
| SHA-256 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| Import status | imported-not-deployed |
| Remaining caution | Object type is photogram (cyanotype), not traditional print. |

## C-10 — Rijksmuseum RP-F-F80313

| Field | Value |
|---|---|
| Candidate ID | C-10 |
| Local path | `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Official source URL | https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f |
| Exact media URL | https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg |
| Identifier | objectNumber RP-F-F80313; persistent URL https://id.rijksmuseum.nl/200408260; Micrio ID PrcdN |
| Source note | *Wolfsklauw*, Anna Atkins (photographer, England), c. 1854. Per-item Copyright field reads verbatim `Public domain` (CC0 1.0 link). **Manifest caveat**: Presentation API `/manifest.json` returned HTTP 404; manifest-based evidence was intentionally omitted from this round. |
| SHA-256 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |
| Import status | imported-not-deployed |
| Remaining caution | Object type is photogram (cyanotype), not traditional print. Manifest-based evidence intentionally omitted. |

---

## Round totals

| Metric | Value |
|---|---|
| ready-for-asset-import at v4.4b | 6 |
| imported in v4.5 | 6 |
| blocked-from-import in v4.5 | 0 |
| deployed | 0 |
| approved | 0 (status word intentionally not used) |
| downloaded image files | 6 |
| new tags | 0 |
| new releases | 0 |
| live site changes | 0 |