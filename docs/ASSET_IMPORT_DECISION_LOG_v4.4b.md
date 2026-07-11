# v4.4b Asset Import Decision Log

> Per-row decision log for the 6 v4.3 `selected-for-build-planning` candidates. The Decision values are limited to `ready-for-asset-import` / `defer` / `blocked-from-import` / `replace-with-project-generated-diagram`. The status `approved` is **not used** in this decision log or any future round.

> 收口时间：v4.4b source gap fix round 结束点。下一 round 由 threshold 决定（≥ 4 ready → v4.5 Asset Import；< 4 → v4.4c Source Gap Research）。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `ad66d6db39622c19e8dc50238da1d9403defa7e9` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | **92,976 B** (preserved) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| Approved asset count | **0** |
| Downloaded image count | **0** |

---

## Decision table (6 rows)

| ID | Decision | Evidence summary | Why | Required v4.5 action |
|---|---|---|---|---|
| **C-01** | `ready-for-asset-import` | BHL item 318921 (Album of watercolors of Asian fruits and flowers, Unknown watercolor artist, between 1798 and 1850?); per-page `<Copyright Status>` filter mechanism documented on BHL's reuse page; per-page image URL reachable via BHL page-viewer | BHL is a Public-domain-style source. Per-page rights status is locatable. The CC BY-NC-SA subset is filtered out at per-page / per-volume level. | Re-open BHL item 318921 on the day of import. Filter per-page `<Copyright Status>` to `Public domain` only. CC BY-NC-SA subset rejected. Capture the per-page image URL. |
| **C-03** | `ready-for-asset-import` (PD subset only) | Same BHL item 318921, treated as the title-level book record. **CC BY-NC-SA subset remains blocked** at the per-page / per-volume level. | Same item as C-01, used for the Section 3 book-level image. The CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at the per-page level. The C-03 row as a whole is `ready-for-asset-import` for the Public-domain subset only. | Same as C-01. **CC BY-NC-SA subset remains blocked** — do not promote CC BY-NC-SA pages to the import set. |
| **C-06** | `ready-for-asset-import` | NMNH Botany, US Catalog 1529703, *Aconitum bulbilliferum* Hand.-Mazz., China / Sichuan, Handel-Mazzetti H. R. 5202, 17 Sep 1914; EZID `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920`; media URL template `https://collections.nmnh.si.edu/media/?i={catalog_number}&ph=yes&thumb=yes` (HEAD test returned HTTP/2 200, `Content-Type: image/png`); dataset-level CC0 1.0 verbatim from `https://collections.nmnh.si.edu/ipt/resource?r=nmnh_botany` ("License: CC0 1.0"; "publisher has waived all rights to these data and has dedicated them to the Public Domain (CC0 1.0). Users may copy, modify, distribute and use the work, including for commercial purposes, without restriction."); cross-confirmed on `https://www.gbif.org/dataset/821cc27a-e3bb-4bc5-ac34-89ada245069d` ("Licence CC0 1.0"); Smithsonian Open Access FAQ `https://www.si.edu/openaccess/faq`. | The dataset-level CC0 1.0 covers the per-item record. The per-item record is reachable via `https://collections.nmnh.si.edu/search/botany/?bc=00103617`. The media URL is reachable via the NMNH media endpoint. The image bytes are reachable (HEAD test) without persisting locally. | Re-open `https://collections.nmnh.si.edu/search/botany/?bc=00103617` on the day of import. Confirm the per-item EZID. Re-confirm dataset-level CC0 1.0 on the IPT page. Download via `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes`. |
| **C-08** | `ready-for-asset-import` | Met object 285149, *[Botanical Specimen: Fern]*, Unknown (British) per public page / Unknown per API, 1855–60, Albumen silver print from glass negative, Gift of Simon Lowinsky 2003, accession 2003.562.3, Department: Photographs. **Double-confirmation passed**: (a) Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` returns `isPublicDomain: true` AND `primaryImage: https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg`; (b) public object page `https://www.metmuseum.org/art/collection/search/285149` shows a "Public Domain" button + "Download Image" + "Enlarge Image" controls (Open Access icon present). objectID = 285149 matches the URL. Accession = 2003.562.3. Title = `[Botanical Specimen: Fern]`. | Both API and public-page confirm Public Domain. objectID, accession, and title match. primaryImage is non-empty. The institution's own page language ("Public Domain") is the basis of the credit line. **Double-confirmation result**: PASS. | Re-open Met object 285149 on the day of import. Re-confirm `isPublicDomain: true` in the Collection API. Re-confirm "Public Domain" button + "Download Image" controls on the public object page. Download via `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg`. If either confirmation fails, C-08 is `blocked-from-import` and the Section 3 alternate slot is filled by a project-generated diagram. |
| **C-09** | `ready-for-asset-import` | Rijksmuseum RP-F-F80152, *Zeestreepvaren*, Anna Atkins (photographer, England), c. 1854, photogram (cyanotype) on paper, height 247 mm × width 193 mm, persistent URL `https://id.rijksmuseum.nl/200407820`. **Exact per-item licence field** (verbatim from the public object page): `Copyright: Public domain` with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`. Rijksmuseum's two-tier policy `CC0 1.0` / `CC BY 4.0` confirmed via the data-policy page (the per-item Copyright field is the authoritative source, not the institution-level policy). Image / IIIF URL (Micrio IIIF Image API): `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`). | The per-item Copyright field is recorded verbatim, not inferred from institution policy. The Rijksstudio image URL is reachable via the Micrio IIIF Image API. The image bytes are reachable (HEAD test) without persisting locally. | Re-open the public object page on the day of import. Re-confirm the per-item Copyright field reads `Public domain` (with the CC0 1.0 hyperlink). Download via `https://iiif.micr.io/vGipU/full/{max},/0/default.jpg`. |
| **C-10** | `ready-for-asset-import` | Rijksmuseum RP-F-F80313, *Wolfsklauw*, Anna Atkins (photographer, England), c. 1854, persistent URL `https://id.rijksmuseum.nl/200408260`. **Exact per-item licence field** (verbatim from the public object page): `Copyright: Public domain` with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`. Image / IIIF URL (Micrio IIIF Image API): `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`). The Rijksmuseum IIIF Presentation API manifest at `https://iiif.micr.io/PrcdN/manifest.json` returned HTTP/2 404; Rijksmuseum uses Micrio IIIF Image API, not Presentation API. The per-item public object page's Copyright field is therefore the authoritative source for the credit line. **Distinct per-item record from C-09** — different objectNumber (`RP-F-F80313` vs `RP-F-F80152`), different persistent URL (`id.rijksmuseum.nl/200408260` vs `id.rijksmuseum.nl/200407820`), different micrioId (`PrcdN` vs `vGipU`). | The per-item Copyright field is recorded verbatim, not inferred from institution policy. The Rijksstudio image URL is reachable via the Micrio IIIF Image API. The image bytes are reachable (HEAD test) without persisting locally. C-09 and C-10 are two distinct per-item records. | Re-open the public object page on the day of import. Re-confirm the per-item Copyright field reads `Public domain`. Download via `https://iiif.micr.io/PrcdN/full/{max},/0/default.jpg`. |

---

## Decision totals

| Decision | Count | IDs |
|---|---|---|
| `ready-for-asset-import` | **6** | C-01, C-03, C-06, C-08, C-09, C-10 |
| `defer` | **0** | (none) |
| `blocked-from-import` (row-level) | **0** | (none — C-14 + C-03 CC BY-NC-SA subset are policy-level entries) |
| `replace-with-project-generated-diagram` (row-level) | **0** | (none) |
| `approved` | **0** | (not used) |
| Approved asset count | **0** | (none) |
| Downloaded image count | **0** | (none — v4.4b records URLs only) |

---

## Key constraints reaffirmed

- **C-03 CC BY-NC-SA subset remains blocked.** The CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at the per-page / per-volume level. v4.5 must filter `<Copyright Status> = Public domain` only. CC BY-NC-SA pages must not enter the import set.
- **C-08 double-confirmation result: PASS.** Both the Collection API (`isPublicDomain: true`) and the public object page ("Public Domain" button + Open Access icon) confirm Public Domain. v4.5 must re-run both confirmations on the day of import.
- **C-09 / C-10 exact per-item licence result: PASS.** The per-item Copyright field on each public object page reads verbatim `Public domain` (with the CC0 1.0 hyperlink). The per-item licence is recorded verbatim, not inferred from institution policy. v4.5 must re-read the per-item Copyright field on the day of import.

---

## Round boundary

The next round is determined by the threshold check in `docs/SOURCE_GAP_FIX_v4.4b.md`:
- `ready-for-asset-import` count = **6 ≥ 4** → the next round is **v4.5 — Asset Import**.
- The status `approved` does not appear as a decision value in this log.