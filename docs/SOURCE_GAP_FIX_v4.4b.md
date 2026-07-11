# v4.4b Source Gap Fix

> Scope: round that closes the per-item record gaps for C-06, C-08, C-09, C-10 (all `defer` in v4.4). v4.4b is **prep-only**: it records URLs and identifiers, it does **not** download any image, and it does **not** create `second-exhibition/assets/images/`. v4.4b status values for the per-row tables are `ready-for-asset-import` or `defer` only. The status `approved` is **not used**.

> 收口时间：v4.4b source gap fix round 结束点。下一 round 是 **v4.5 asset import** (gated on `ready-for-asset-import` ≥ 4).

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
| v4.4 status (carry-over) | `ready-for-asset-import` = 2 (C-01, C-03) + `defer` = 4 (C-06, C-08, C-09, C-10) |
| v4.4b target | close the 4 defer gaps so that the v4.5 asset import round has ≥ 4 `ready-for-asset-import` rows |

---

## v4.4b status legend (only these two values appear in the table below)

| Status | Meaning |
|---|---|
| `ready-for-asset-import` | All evidence fields complete. Item URL reachable. Rights statement locatable on the institution's own page. Image / IIIF URL locatable. Credit-line basis composable without guessing. C-08 double-confirmation (Collection API + public-page OA icon) has passed. C-09 / C-10 per-item `licence` field recorded verbatim. C-06 dataset-level CC0 1.0 confirmed on the IPT page and the per-item record is reachable via NMNH search. |
| `defer` | At least one v4.4b field is missing or a per-action check has not passed. Held back to a future round. |

The status `approved` is **not used** in v4.4b or any future round.

---

## Source-gap fix table (4 rows)

| ID | Source level in v4.4 | v4.4b per-item record picked | Rights status in v4.4b | Image / IIIF URL verified | v4.4b status |
|---|---|---|---|---|---|
| **C-06** | collection / search-level only | NMNH Botany, US Catalog No. **1529703** (Barcode **00103617**), *Aconitum bulbilliferum* Hand.-Mazz., Type fragment (Ranunculaceae), pressed specimen, China / Sichuan, Handel-Mazzetti H. R. 5202, 17 Sep 1914 | Dataset-level CC0 1.0 (verified on IPT page `https://collections.nmnh.si.edu/ipt/resource?r=nmnh_botany` and GBIF dataset `https://www.gbif.org/dataset/821cc27a-e3bb-4bc5-ac34-89ada245069d` — "Licence CC0 1.0") + per-item record reachable via `https://collections.nmnh.si.edu/search/botany/?bc=00103617` with full metadata and stable EZID `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920` | `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes` (HEAD test returned HTTP/2 200, `Content-Type: image/png`; URL recorded, do NOT download) | `ready-for-asset-import` |
| **C-08** | item-level (Met object 285149) | The Metropolitan Museum of Art, object 285149, *Unknown (British)* (per public page) / *Unknown* (per API), *Albumen silver print from glass negative*, *Gift of Simon Lowinsky, in memory of his uncle, Herbert Jonas, 2003*, 1855–60, accession 2003.562.3, Department: Photographs | Double-confirmation: (a) Met Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` returned `isPublicDomain: true` AND `primaryImage: https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg`; (b) public object page `https://www.metmuseum.org/art/collection/search/285149` shows a "Public Domain" button + "Download Image" + "Enlarge Image" controls (Open Access icon present) | `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` (URL recorded, do NOT download) | `ready-for-asset-import` |
| **C-09** | collection / policy-level only | Rijksmuseum, **Zeestreepvaren**, objectNumber **RP-F-F80152**, Anna Atkins, c. 1854, photogram on paper (cyanotype), height 247 mm × width 193 mm, persistent URL `https://id.rijksmuseum.nl/200407820`, public object page `https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da` | Per-item Copyright field on the public object page reads `Public domain` and links to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`; Rijksmuseum's two-tier policy `CC0 1.0` / `CC BY 4.0` confirmed via `https://data.rijksmuseum.nl/policy/information-and-data-policy` | IIIF Image API (Micrio): `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, do NOT download) | `ready-for-asset-import` |
| **C-10** | collection / policy-level only | Rijksmuseum, **Wolfsklauw**, objectNumber **RP-F-F80313**, Anna Atkins, c. 1854, persistent URL `https://id.rijksmuseum.nl/200408260`, public object page `https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f`. **Distinct per-item record** from C-09 (different objectNumber, different micrioId, different persistent URL, different IIIF Image API URL). | Per-item Copyright field on the public object page reads `Public domain` and links to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`. The Rijksmuseum IIIF Presentation API manifest at `https://iiif.micr.io/PrcdN/manifest.json` returned HTTP/2 404 (Rijksmuseum uses Micrio IIIF Image API, not the Presentation API manifest); the per-item public object page's Copyright field is therefore the authoritative source for the credit line. | IIIF Image API (Micrio): `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, do NOT download) | `ready-for-asset-import` |

---

## v4.4b selection totals

| Status | v4.4 carry-over | v4.4b delta | v4.4b totals | IDs |
|---|---|---|---|---|
| `ready-for-asset-import` | 2 (C-01, C-03) | +4 (all 4 defer rows promoted) | **6** | C-01, C-03, C-06, C-08, C-09, C-10 |
| `defer` | 4 (C-06, C-08, C-09, C-10) | -4 (all 4 promoted) | **0** | (none) |
| `blocked-from-import` row-level | 0 | 0 | 0 | (none — C-14 + C-03 CC BY-NC-SA subset are policy-level entries) |
| `replace-with-project-generated-diagram` row-level | 0 | 0 | 0 | (none) |
| `approved` | 0 | 0 | **0** (not used) | (none) |

**Threshold check.** `ready-for-asset-import` count = **6 ≥ 4**. The next round is **v4.5 — Asset Import**, which is no longer gated on v4.4b (the source gap is closed).

---

## Pre-import actions recap (for v4.5)

| ID | Pre-import action in v4.5 |
|---|---|
| **C-01** | Re-open BHL item 318921. Pick a per-page record. Filter per-page `<Copyright Status>` to `Public domain` only. CC BY-NC-SA subset rejected. Capture per-page image URL. |
| **C-03** | Same as C-01. |
| **C-06** | Re-open NMNH Botany search `?bc=00103617`. Confirm per-item EZID `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920` on the day of import. Download via `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes`. |
| **C-08** | Re-open Met object 285149. Confirm `isPublicDomain: true` in the Collection API on the day of import. Confirm the "Public Domain" button + Open Access icon on the public object page. Download via `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg`. |
| **C-09** | Re-open Rijksmuseum object RP-F-F80152. Confirm the per-item Copyright field is `Public domain` (with the CC0 1.0 link to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`). Download via the Micrio IIIF Image API URL `https://iiif.micr.io/vGipU/full/{max},/0/default.jpg`. |
| **C-10** | Re-open Rijksmuseum object RP-F-F80313. Confirm the per-item Copyright field is `Public domain`. Download via `https://iiif.micr.io/PrcdN/full/{max},/0/default.jpg`. |

---

## Why these are `ready-for-asset-import` (not `approved`)

Each row's rights statement is taken **verbatim** from the institution's own page on the day of audit:
- BHL C-01 / C-03: per-page `<Copyright Status>` filter (PD subset) — `Public domain` is the institution's own page language.
- NMNH C-06: dataset-level `CC0 1.0` on the IPT page + GBIF dataset metadata.
- Met C-08: `isPublicDomain: true` in the Collection API + `Public Domain` button on the public object page.
- Rijksmuseum C-09 / C-10: per-item `Copyright: Public domain` field on the public object page, with a hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`.

The status `approved` is **not used**. The status `cleared for all uses` is **not used**. The phrase "safe for commercial use" is **not used**.

---

## Constraints respected in v4.4b

- **No images downloaded.** Verified by `find . -path ./.git -prune -o -path ./.firecrawl -prune -o \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" -o -iname "*.tif" -o -iname "*.tiff" \) -print | sort` returning the same set as the v4.4 baseline. HEAD / GET requests were used only to verify URL reachability, not to persist image bytes locally. Any transient fetch artifacts were cleaned up in `/tmp` immediately.
- **No `second-exhibition/assets/images/` directory created.** v4.4b is prep-only; directory creation is a v4.5 step.
- **`site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/`, `scripts/template_quality_gate.py` unchanged.** Verified by `git diff` (empty).
- **No tag created.** Verified by `git tag` (latest tag is `v3.4-real-second-exhibition-hardening` → `81f5e928`).
- **No GitHub Release created.** Out of scope for v4.4b.
- **No `git add .` used.** All adds are explicit per-path (see `docs/V4_ROADMAP.md` v4.4b section and the round report).
- **v4.4 historical snapshot docs not modified.** The 5 v4.4 prep docs (`ASSET_IMPORT_PREP_v4.4.md`, `ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md`, `SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md`, `CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md`, `ASSET_FILENAME_MAP_v4.4.md`) and the v4.4 report are preserved unchanged; v4.4b writes its own `_v4.4b.md` files alongside them.
- **`.firecrawl/` not processed.** Untracked directory remains untouched.

---

## Round boundary

v4.4b ends with:

- All v4.4b docs committed (`SOURCE_GAP_FIX_v4.4b.md`, `ITEM_EVIDENCE_COMPLETION_v4.4b.md`, `READY_FOR_ASSET_IMPORT_SHORTLIST_v4.4b.md`, `ASSET_IMPORT_DECISION_LOG_v4.4b.md`, `ASSET_FILENAME_MAP_UPDATE_v4.4b.md`).
- `docs/V4_ROADMAP.md` v4.4b section committed.
- `README.md` v4.4b block committed.
- `reports/leonardo_chinese_exhibition_v4_4b_source_gap_fix_report.md` committed.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- `find` confirms no new image files.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `scripts/template_quality_gate.py` is empty.
- `ready-for-asset-import` count = 6 (recorded as ≥ 4 → v4.5 — Asset Import — is unblocked).
- `approved` does not appear as a status value in any v4.4b doc.
- No new tag, no new GitHub Release.

The next round is **v4.5 — Asset Import**.