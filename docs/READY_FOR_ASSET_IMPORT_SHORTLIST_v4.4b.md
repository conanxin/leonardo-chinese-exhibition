# v4.4b Ready for Asset Import Shortlist

> Meaning of `ready-for-asset-import` in v4.4b: this status **only** means the per-item evidence is complete enough that the future asset-import round (v4.5) is allowed to enter. It does **not** mean the image has been downloaded. It does **not** mean the asset has been imported. It does **not** mean the asset is on the live site. It is **not** a legal opinion. The status `approved` is **not used**; the phrase "safe for commercial use" is **not used**; the phrase "cleared for all uses" is **not used**.

> 收口时间：v4.4b source gap fix round 结束点。下一 round 由 threshold 决定（≥ 4 ready → v4.5 Asset Import；< 4 → v4.4c Source Gap Research）。

---

## Ready candidates (6 rows)

| ID | Institution | Concrete item | Identifier | Source URL | Rights basis | Image / IIIF URL recorded | Proposed filename | Remaining caution |
|---|---|---|---|---|---|---|---|---|
| C-01 | Biodiversity Heritage Library | Album of watercolors of Asian fruits and flowers — per-page plate | BHL item 318921 | https://www.biodiversitylibrary.org/item/318921 | Public domain (per-page `<Copyright Status>` filter; CC BY-NC-SA subset rejected at per-page / per-volume level) | per-page image URL via BHL page-viewer (URL pattern recorded, not downloaded) | `bhl-318921-plate.jpg` | Re-open item 318921 on the day of import; filter per-page `<Copyright Status>` to `Public domain` only; CC BY-NC-SA subset rejected. |
| C-03 | Biodiversity Heritage Library | Album of watercolors of Asian fruits and flowers — book-level page | BHL item 318921 | https://www.biodiversitylibrary.org/item/318921 | Public domain (PD subset only); CC BY-NC-SA 4.0 in-copyright subset = `blocked-from-import` at per-page / per-volume level | per-page image URL via BHL page-viewer (URL pattern recorded, not downloaded) | `bhl-318921-page.jpg` | CC BY-NC-SA subset blocked at per-page level. Do not promote CC BY-NC-SA pages to the import set. |
| C-06 | Smithsonian National Museum of Natural History / NMNH Botany | Aconitum bulbilliferum Hand.-Mazz. — pressed specimen, Type fragment (Ranunculaceae), China / Sichuan | US Catalog No. 1529703; Barcode 00103617; EZID `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920` | https://collections.nmnh.si.edu/search/botany/?bc=00103617 (collection entry: https://collections.nmnh.si.edu/search/botany/) | Dataset-level CC0 1.0 (verbatim from `https://collections.nmnh.si.edu/ipt/resource?r=nmnh_botany` — "License: CC0 1.0"; cross-confirmed on `https://www.gbif.org/dataset/821cc27a-e3bb-4bc5-ac34-89ada245069d` — "Licence CC0 1.0") | `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes` (HEAD test returned HTTP/2 200, `Content-Type: image/png`; URL recorded, not downloaded) | `nmnh-1529703.jpg` | Re-open `?bc=00103617` on the day of import. Confirm per-item EZID `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920`. Confirm dataset-level CC0 1.0 on the IPT page. |
| C-08 | The Metropolitan Museum of Art | [Botanical Specimen: Fern] — albumen silver print from glass negative | Met objectID 285149 / accession 2003.562.3 | https://www.metmuseum.org/art/collection/search/285149 | Public domain (double-confirmed: Collection API `isPublicDomain: true` AND "Public Domain" button on public object page) | `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` (URL recorded, not downloaded) | `met-285149.jpg` | Re-open Met object 285149 on the day of import. Re-confirm `isPublicDomain: true` in the Collection API. Re-confirm "Public Domain" button + "Download Image" controls on the public object page. If either confirmation fails, C-08 is `blocked-from-import` and the Section 3 alternate slot is filled by a project-generated diagram. |
| C-09 | Rijksmuseum / Rijksprentenkabinet | Zeestreepvaren — photogram (cyanotype on paper), height 247 mm × width 193 mm | objectNumber `RP-F-F80152`; persistent URL `https://id.rijksmuseum.nl/200407820` | https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da | Per-item Copyright field on the public object page reads verbatim `Public domain` (with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`); Rijksmuseum two-tier policy `CC0 1.0` / `CC BY 4.0` confirmed via the data-policy page | Micrio IIIF Image API: `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded) | `rijksmuseum-rp-f-f80152.jpg` | Re-open `https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da` on the day of import. Re-confirm the per-item Copyright field reads `Public domain` (with the CC0 1.0 hyperlink). |
| C-10 | Rijksmuseum / Rijksprentenkabinet | Wolfsklauw — botanical cyanotype (distinct per-item record from C-09) | objectNumber `RP-F-F80313`; persistent URL `https://id.rijksmuseum.nl/200408260` | https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f | Per-item Copyright field on the public object page reads verbatim `Public domain` (with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`) | Micrio IIIF Image API: `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded) | `rijksmuseum-rp-f-f80313.jpg` | Re-open the public object page on the day of import. Re-confirm the per-item Copyright field reads `Public domain`. The Rijksmuseum IIIF Presentation API manifest at `https://iiif.micr.io/PrcdN/manifest.json` returned HTTP/2 404 (Rijksmuseum uses Micrio IIIF Image API, not Presentation API); the per-item public object page's Copyright field is the authoritative source for the credit line. |

## Deferred or blocked candidates (0 rows)

| ID | Status | Missing evidence | Required next action |
|---|---|---|---|
| (none) | — | — | — |

All 6 v4.3 `selected-for-build-planning` candidates are now `ready-for-asset-import`.

---

## Import gate

- The future asset-import round (v4.5) requires **at least 4** `ready-for-asset-import` rows. The current count is **6 ≥ 4**, so v4.5 is unblocked.
- **C-03 is still restricted to the Public-domain subset only.** The CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at the per-page / per-volume level. v4.5 must re-run the per-page `<Copyright Status>` check on the day of import.
- **v4.5 must re-open every source / rights / IIIF URL on the day of import** and re-confirm the rights basis before each download. The rights statement from v4.4 / v4.4b is the *basis*, not a substitute for a re-check on the import day.
- **v4.5 must not bulk-import items that are not on this shortlist.** Each download in v4.5 corresponds to exactly one row in this shortlist.
- **v4.5 must not create `second-exhibition/assets/images/` as a side effect** beyond the per-item filenames listed here. The directory creation is a v4.5 step.
- **v4.5 must not promote any `defer` row to `ready-for-asset-import`.** Rows on this shortlist are the only eligible input.

---

## Forbidden phrases (used in v4.4b and any future round)

The following phrases must **not** appear in any v4.4b or later doc:
- `approved`
- `safe for commercial use`
- `cleared for all uses`

These phrases were searched in this round's docs and confirmed absent as a status value.