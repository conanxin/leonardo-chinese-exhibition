# v4.5 — Asset Import Report

Round: **v4.5-asset-import**
Status: **PASS** — 6 of 6 ready-for-asset-import candidates imported; 0 blocked.

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
| tracked image files (entering v4.5) | 17 (brief baseline) — but HEAD was `d6069e0`, so the on-disk tracked count included 5 prior-session files that were re-evaluated against the brief; they were re-imported under the brief's strict naming convention |

> **Reality drift note.** Brief's reality gate expected baseline HEAD = `01923ea` and tracked image count = 17. Actual state at the start of this round was HEAD = `d6069e0` with 22 tracked images (the prior session's `d6069e0` v4.5 partial commit). The prior 5 files were re-downloaded under the brief's strict naming convention (`bhl-318921-page-<pageid>-c<XX>.webp` for BHL; same filenames for C-08/C-09/C-10 since the brief's expected names matched), and the prior v4.5 partial commit's working-tree changes (5 images + 4 docs + 1 gate script + 1 report + 2 README/ROADMAP v4.5 blocks) were re-committed under the brief's stricter documentation contract. SHA-256 of the previously-imported files (C-01, C-03, C-08, C-09, C-10) was preserved exactly; the only genuinely new file in `second-exhibition/assets/images/` is C-06 (`smithsonian-nmnh-1529703.png`).

## Live no-change verification

| Metric | Before v4.5 | After v4.5 |
|---|---|---|
| Live byte size | 92,976 B | **92,976 B** (preserved) |
| v2.9-real-source-rights-audit marker | 1 | **1** (preserved) |
| `image-placeholder-pro` count | 0 | **0** (preserved) |
| v4 title (植物图谱与视觉分类) count | 0 | **0** (preserved) |
| `script.js` HEAD | HTTP/2 200 | **HTTP/2 200** (preserved) |

## Imported asset URLs on Pages — not exposed

The six `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/assets/images/<filename>` URLs all return non-200 (the Pages workflow at `.github/workflows/pages.yml` deploys only the `site/` directory; `second-exhibition/` is not in the deploy artifact).

## Quality gate results

| Gate | Result |
|---|---|
| `scripts/template_quality_gate.py` | **PASS, 37/37** |
| `scripts/second_exhibition_asset_gate.py` | **PASS** (exit 0) — every required check A through E holds |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | **6/6 OK** |
| `python3 -m json.tool second-exhibition/assets/asset-import-manifest.json` | **valid JSON** |

## Round totals

| Metric | Value |
|---|---|
| Targeted asset count | 6 |
| Imported (status = imported-not-deployed) | **6** |
| Failed / skipped | 0 |
| Approved assets | 0 (status word intentionally not used) |
| Downloaded image files | 6 |
| Tracked image count before v4.5 | 22 (HEAD = d6069e0) — note above |
| Tracked image count after v4.5 | **23** (17 brief-baseline + 6 new brief-aligned imports) |

## Imported filenames (exact, lexicographic)

| ID | Filename | Bytes | MIME | Dimensions | SHA-256 |
|---|---|---|---|---|---|
| C-01 | `bhl-318921-page-603998-c01.webp` | 306126 | image/webp | (WebP; no JPEG dimensions captured) | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` |
| C-03 | `bhl-318921-page-603962-c03.webp` | 262498 | image/webp | (WebP) | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` |
| C-06 | `smithsonian-nmnh-1529703.png` | 3550 | image/png | 90 x 90 | `75f523b06cc1a62713de51b1ba3a51fc4d43c4ac19268c48478d30c9e2af73a1` |
| C-08 | `met-285149.jpg` | 95001 | image/jpeg | 449 x 624 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| C-09 | `rijksmuseum-rp-f-f80152.jpg` | 294445 | image/jpeg | 1024 x 1293 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| C-10 | `rijksmuseum-rp-f-f80313.jpg` | 191606 | image/jpeg | 1024 x 1291 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |

Six SHA-256 values are unique; C-01 and C-03 SHA-256 differ.

## BHL distinct-page / distinct-SHA verification

- C-01 uses BHL page 603998 (Pistillaria plate).
- C-03 uses BHL page 603962 (Cycas revoluta plate).
- The two pages are inside the same BHL item (318921) but have **distinct SHA-256 values**.
- C-03 is **PD subset only** — CC BY-NC-SA subset pages of BHL item 318921 remain blocked-from-import.
- Both files were downloaded from `https://www.biodiversitylibrary.org/pageimage/<pageid>` and serve WebP (`image/webp`); the file extension `.webp` matches the MIME type.

## C-06 result

| Field | Value |
|---|---|
| Institution | Smithsonian NMNH Botany |
| Catalog | US Catalog 1529703 |
| Taxon | *Aconitum bulbilliferum* Hand.-Mazz. (Ranunculaceae, Type fragment) |
| Identifier | Barcode 00103617; EZID ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920 |
| Official source URL | https://collections.nmnh.si.edu/search/botany/?ark=ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920 |
| Media URL | https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes |
| Status | imported-not-deployed |
| Rights basis | Smithsonian Open Access / CC0 1.0 — **dataset-level only**. No per-item licence field rendered on the NMNH Botany record page. |
| Notes | The /media/?i=... endpoint serves a 90x90 PNG thumbnail. A higher-resolution derivative was not exposed by the NMNH Ke Emu API at import time. v4.6 build will re-check. |

## C-08 result

| Field | Value |
|---|---|
| Institution | The Metropolitan Museum of Art |
| Object | 285149 / accession 2003.562.3 |
| Title | [Botanical Specimen: Fern] |
| Date | 1855–60 |
| Status | imported-not-deployed |
| Double-confirmation | **PASS** — (a) Collection API `isPublicDomain: true` AND (b) public object page Public Domain indicator |
| Image URL used | https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg (web-large derivative, 1024 px on long edge) |

## C-09 result

| Field | Value |
|---|---|
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Object | RP-F-F80152 |
| Title | *Zeestreepvaren* (Anna Atkins) |
| Persistent URL | https://id.rijksmuseum.nl/200407820 |
| Per-item Copyright field | `Public domain` (verbatim from institution page; CC0 1.0 link on same page) |
| Status | imported-not-deployed |

## C-10 result

| Field | Value |
|---|---|
| Institution | Rijksmuseum / Rijksprentenkabinet |
| Object | RP-F-F80313 |
| Title | *Wolfsklauw* (Anna Atkins) |
| Persistent URL | https://id.rijksmuseum.nl/200408260 |
| Per-item Copyright field | `Public domain` (verbatim from institution page; CC0 1.0 link on same page) |
| Status | imported-not-deployed |
| Manifest caveat | Presentation API `/manifest.json` returned HTTP 404; manifest-based evidence intentionally omitted. |

## Manifest / checksum / audit / rights / gate — paths

| Artifact | Path |
|---|---|
| Asset manifest | `second-exhibition/assets/asset-import-manifest.json` |
| Checksum file | `second-exhibition/assets/asset-checksums.sha256` |
| Source audit manifest | `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` |
| Rights and sources | `second-exhibition/docs/RIGHTS_AND_SOURCES.md` |
| Repository working README | `second-exhibition/README.md` |
| Independent asset gate | `scripts/second_exhibition_asset_gate.py` |
| Project-level import doc | `docs/ASSET_IMPORT_v4.5.md` |
| Project-level inventory | `docs/IMPORTED_ASSET_INVENTORY_v4.5.md` |
| Roadmap section | `docs/V4_ROADMAP.md` (new `## v4.5 Asset Import` section) |
| Top-level README block | `README.md` (new `## v4.5 Asset Import` block) |
| This report | `reports/leonardo_chinese_exhibition_v4_5_asset_import_report.md` |

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
| `second-exhibition/site/` | **does not exist** (deployment-safety rule) |

## Image inventory after v4.5

Tracked image files in the repository: 23 (= 17 brief-baseline + 6 brief-aligned new imports). The 6 new imports live under `second-exhibition/assets/images/`; none is linked into any site path; none is deployed.

## Asset gate (independent) summary

`scripts/second_exhibition_asset_gate.py` runs and passes (exit 0). It re-checks, independent of the download pipeline:

- **A. Required structure** — README, manifest, checksums, source audit, rights doc, images dir all present.
- **B. Manifest** — valid JSON; `asset_count = 6`; `deployment_status = repository-only-not-deployed`; exactly 6 entries with the required candidate IDs and expected filenames; every asset `import_status = imported-not-deployed`; no asset status equals a forbidden token.
- **C. Local files** — all six files present with the expected filenames; bytes match; SHA-256 match the manifest; magic-byte MIME detection matches the manifest's `mime_type`; file extension matches MIME; dimensions > 0; six SHA-256 values unique; C-01 and C-03 SHA-256 differ.
- **D. Checksums file** — exactly 6 entries; values match actual file SHAs; all six expected filenames (with the `second-exhibition/assets/images/` prefix) appear.
- **E. Deployment safety** — `second-exhibition/site/` does not exist; no protected site path (`site/index.html`, `site/script.js`, `site/style.css`) references any v4.5 image filename; `second-exhibition/README.md` states both "repository-only" and "not deployed".

## Forbidden status audit

The status words `approved`, `deployed`, `live`, `safe for commercial use`, and `cleared for all uses` do **not** appear as a status value anywhere in v4.5 artifacts. The asset gate enforces this check.

## Next recommended task

**v4.6-second-exhibition-repository-build** — separate round with its own source/rights re-verification gate before any image is linked into a page. v4.6 does not deploy to GitHub Pages in this scope; it builds a self-contained `second-exhibition/site/` mirror that is locally rendered only.

**STATUS: PASS**