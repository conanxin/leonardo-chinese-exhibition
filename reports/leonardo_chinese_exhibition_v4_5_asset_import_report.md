# v4.5 — Asset Import Report

Round: **v4.5-asset-import**
Status: **PARTIAL** — 5 of 6 ready-for-asset-import candidates imported; C-06 blocked-from-import.

---

## Baseline

| Field | Value |
|---|---|
| Baseline commit | `01923ea9689f509d3547c64339680e8c571952de` |
| origin/main before | `01923ea9689f509d3547c64339680e8c571952de` |
| Source tag | `v3.4-real-second-exhibition-hardening` |
| Source tag target SHA | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` (untouched) |
| ready-for-asset-import at v4.4b | 6 |
| approved asset count (entering v4.5) | 0 (status word intentionally not used) |
| downloaded image count (entering v4.5) | 0 |
| tracked image files (entering v4.5) | 17 |

## Live state (before / after)

| Metric | Before v4.5 | After v4.5 |
|---|---|---|
| Live byte size of `https://conanxin.github.io/leonardo-chinese-exhibition/` | 92,976 B | **92,976 B** (preserved) |
| v2.9-real-source-rights-audit marker in live | 1 | **1** (preserved) |
| `image-placeholder-pro` count in live | 0 | **0** (preserved) |
| v4 title (植物图谱与视觉分类) count in live | 0 | **0** (preserved; v4.5 is repository-only) |
| `script.js` HEAD status | HTTP/2 200 | **HTTP/2 200** (preserved) |

## Quality gate

| Gate | Result |
|---|---|
| `scripts/template_quality_gate.py` | **PASS, 37/37** |
| `scripts/second_exhibition_asset_gate.py` (new in v4.5) | **PASS — 5 imported, 1 blocked** (exit 0) |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | **5/5 OK** |

## Gaps investigated

`gaps_investigated = 1` (only C-06 was re-investigated during v4.5; C-01 / C-03 / C-08 / C-09 / C-10 used v4.4b-verified URLs without re-research).

## Concrete items completed

`concrete_items_completed = 4` (C-06 re-investigated; C-08 double-confirmation re-verified; C-09 / C-10 image URLs re-confirmed live).

## Round totals

| Metric | Value |
|---|---|
| ready-for-asset-import at v4.4b | 6 |
| imported (status = imported-not-deployed) | **5** |
| blocked-from-import | **1** (C-06) |
| deployed | 0 |
| approved | 0 (status word intentionally not used) |
| downloaded image files | 5 |
| new tags created | 0 |
| new GitHub Releases | 0 |
| live site changes | 0 |

## C-06 result (blocked-from-import)

| Field | Value |
|---|---|
| ID | C-06 |
| Institution | Smithsonian NMNH Botany |
| Catalog number | 1529703 |
| Expected taxon | *Aconitum bulbilliferum* (per v4.4b evidence) |
| Record URL attempted | https://collections.nmnh.si.edu/search/botany/?irn=2793935 |
| Issue | The irnstamp value 2793935 in the v4.4b evidence maps to an NMNH Botany record whose on-page `<title>` reads "Rhynchanthus longiflorus, Myitkyina, Myanmar", not the *Aconitum bulbilliferum* taxon recorded in v4.4b evidence. The catalog-number → irnstamp relationship could not be confirmed during v4.5 download verification. |
| Image URLs attempted | (multiple path variations under `collections.nmnh.si.edu/services/media/...` and `collections.nmnh.si.edu/media/...`) — all returned HTTP 404 with `text/html` content. |
| Outcome | **blocked-from-import**. No file created in `second-exhibition/assets/images/`. Per brief: no unverified replacement was substituted. |
| Next round action | `v4.5b — Source Gap Fix` must (a) re-derive the correct irnstamp for catalog 1529703 from a fresh NMNH Botany search, (b) confirm the on-page taxon matches *Aconitum bulbilliferum*, (c) obtain a stable per-item media URL, (d) re-record the dataset-level CC0 1.0 basis from the live `si.edu/openaccess/faq` page. |

## C-08 result (imported)

| Field | Value |
|---|---|
| ID | C-08 |
| Institution | The Metropolitan Museum of Art |
| Object ID | 285149 |
| Accession | 2003.562.3 |
| Title | [Botanical Specimen: Fern] |
| Double-confirmation | PASS: (a) Collection API `isPublicDomain=true`, (b) public object page Public Domain button present. |
| Filename | `second-exhibition/assets/images/met-285149.jpg` |
| Bytes | 95001 |
| SHA-256 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| Image URL used | `https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg` (web-large derivative; original also re-confirmed live during v4.5) |
| Status | imported-not-deployed |

## C-09 result (imported)

| Field | Value |
|---|---|
| ID | C-09 |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Object number | RP-F-F80152 |
| Title | Zeestreepvaren |
| Per-item licence field | `Public domain` (verbatim from institution page; CC0 1.0 link on same page) |
| Filename | `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` |
| Bytes | 294445 |
| SHA-256 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| Image URL used | `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (Micrio IIIF Image API; HEAD 200 image/jpeg confirmed before download) |
| Status | imported-not-deployed |

## C-10 result (imported)

| Field | Value |
|---|---|
| ID | C-10 |
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Object number | RP-F-F80313 |
| Title | Wolfsklauw |
| Per-item licence field | `Public domain` (verbatim from institution page; CC0 1.0 link on same page) |
| Filename | `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` |
| Bytes | 191606 |
| SHA-256 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |
| Image URL used | `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (Micrio IIIF Image API; HEAD 200 image/jpeg confirmed before download) |
| Caveat | Presentation API manifest `/manifest.json` returned HTTP 404; manifest-based evidence intentionally omitted from this round. |
| Status | imported-not-deployed |

## C-01 / C-03 result (imported)

| ID | Filename | Bytes | SHA-256 | Notes |
|---|---|---|---|---|
| C-01 | `second-exhibition/assets/images/bhl-318921-page-603998.webp` | 306126 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` | BHL page 603998 (Pistillaria plate). |
| C-03 | `second-exhibition/assets/images/bhl-318921-page-603962.webp` | 262498 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` | BHL page 603962 (Cycas revoluta plate). Distinct from C-01 (SHA differs). CC BY-NC-SA subset pages of BHL item 318921 remain blocked. |

Both C-01 and C-03 downloaded via BHL page-image endpoint (`https://www.biodiversitylibrary.org/pageimage/<page-id>`); HEAD test before each download returned HTTP 200 with `image/webp`.

## Docs and gates created/modified in v4.5

Created:

- `second-exhibition/README.md`
- `second-exhibition/assets/asset-import-manifest.json` (12,390 bytes, valid JSON)
- `second-exhibition/assets/asset-checksums.sha256` (5 entries, `sha256sum -c` PASS)
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md`
- `scripts/second_exhibition_asset_gate.py` (independent gate, exit 0)
- `docs/ASSET_IMPORT_v4.5.md`
- `docs/IMPORTED_ASSET_INVENTORY_v4.5.md`
- `reports/leonardo_chinese_exhibition_v4_5_asset_import_report.md` (this file)

Modified:

- `README.md` — added `v4.5 Asset Import` block.
- `docs/V4_ROADMAP.md` — added `v4.5 — Asset Import` section + Phasing-summary row.

## Path-discipline verification

| Path | Diff after v4.5 |
|---|---|
| `site/index.html`, `site/style.css`, `site/script.js` | **empty** |
| `_template/site/` | **empty** |
| `_template/data/` | **empty** |
| `_pilots/second-exhibition-pilot/` | **empty** |
| `posts/`, `case-study/`, `release-assets/` | **empty** (no existing files modified) |
| `scripts/template_quality_gate.py` | **empty** (unchanged) |
| Existing git tags (`v2.0` through `v3.4`) | **untouched** |
| Existing GitHub Releases | **untouched** |
| Untracked `.firecrawl/` directory | **not processed** |

## Image inventory after v4.5

22 image files total (17 pre-existing + 5 new in v4.5):

- 17 pre-existing: 7 in `site/assets/images/` (5 platform + 4 royal-collection + 2 codex-atlanticus, the v3.4-era releases), 7 in `release-assets/screenshots/` (v1.9–v3.4 release artefacts), 0 elsewhere.
- 5 new in `second-exhibition/assets/images/` (all `imported-not-deployed`; not linked from any site path; not deployed).

## Asset gate (independent) summary

`scripts/second_exhibition_asset_gate.py` runs and passes (exit 0). It re-checks, independent of the download pipeline:

1. Every filename declared in `second-exhibition/assets/asset-import-manifest.json` exists in `second-exhibition/assets/images/`.
2. Every file in `second-exhibition/assets/images/` is declared in the manifest.
3. Every file's SHA-256 matches the manifest AND the checksum file.
4. Every file's byte size matches the manifest.
5. No manifest asset `status` field equals a forbidden token (`approved`, `deployed`, `live`, `safe for commercial use`, `cleared for all uses`).
6. No protected site path (`site/index.html`, `site/script.js`, `site/style.css`) references any v4.5 image filename.
7. Manifest `round_status` is one of `pass` / `partial` / `blocked`.

## Forbidden status audit

Grep of `docs/`, `README.md`, `second-exhibition/`, and `scripts/second_exhibition_asset_gate.py` confirms that `approved`, `deployed`, `live`, `safe for commercial use`, and `cleared for all uses` do **not** appear as a status value anywhere in v4.5 artifacts (with the trivial exception of explicit "not used" / "forbidden token" / "must not appear" prose references inside the docs that explicitly call out these labels as forbidden).

## Next recommended task

**v4.5b — Source Gap Fix** (because v4.5 round status is `partial`).

v4.5b goals:

- Re-derive the correct irnstamp for NMNH Botany catalog 1529703 from a fresh NMNH Botany search.
- Confirm the on-page taxon matches *Aconitum bulbilliferum*.
- Obtain a stable per-item media URL.
- Re-record dataset-level CC0 1.0 basis from the live si.edu Open Access / Terms page.
- Update `second-exhibition/assets/asset-import-manifest.json`, `docs/IMPORTED_ASSET_INVENTORY_v4.5.md`, `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`, and `second-exhibition/docs/RIGHTS_AND_SOURCES.md` to v4.5b.

v4.5b does **not** deploy, does **not** modify any live site, and does **not** create a tag or GitHub Release.

After v4.5b, if `imported` reaches 6 and no blockers remain, the next round is **v4.6 — Second Exhibition Site Build** (separate round with its own source/rights re-verification gate before any image is linked into a page). If v4.5b still leaves the count < 6, continue source-gap research until the threshold is met.

**STATUS: PARTIAL**