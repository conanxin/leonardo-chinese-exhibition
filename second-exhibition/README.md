# Second Exhibition — Repository Assets

This directory holds repository-only assets for the **second exhibition** of the Leonardo Chinese exhibition project.

## Status

**Round:** v4.5-asset-import

**Deployment status:** `imported-not-deployed`

The assets in `assets/images/` are stored in the repository only. They are **not** linked into any live site (`site/index.html`, `site/script.js`, `site/style.css`, or `second-exhibition/site/`), not deployed to GitHub Pages, and not associated with any git tag or GitHub Release.

## Asset inventory

| File | Bytes | SHA-256 |
|---|---|---|
| `assets/images/bhl-318921-page-603998.webp` | 306126 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` |
| `assets/images/bhl-318921-page-603962.webp` | 262498 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` |
| `assets/images/met-285149.jpg` | 95001 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| `assets/images/rijksmuseum-rp-f-f80152.jpg` | 294445 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| `assets/images/rijksmuseum-rp-f-f80313.jpg` | 191606 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |

Checksum file: `assets/asset-checksums.sha256`

Machine-readable manifest: `assets/asset-import-manifest.json`

## Forbidden status values

The following labels are intentionally **not** used anywhere in this round's assets or docs:

- `approved`
- `deployed`
- `live`
- `safe for commercial use`
- `cleared for all uses`

Every asset is recorded as `imported-not-deployed`.

## C-06 gap

`C-06` (Smithsonian NMNH Botany, catalog 1529703) is recorded in `assets/asset-import-manifest.json` as `blocked-from-import`. The candidate media URL paths did not return a real image during v4.5 download verification (see `docs/ASSET_IMPORT_v4.5.md` and `docs/IMPORTED_ASSET_INVENTORY_v4.5.md`). No unverified replacement image was substituted.

## Next round

- `v4.5b-source-gap-fix` — re-derive the correct per-item record for NMNH catalog 1529703 and obtain a stable per-item media URL.
- `v4.6-second-exhibition-site-build` — separate round; will require its own source/rights re-verification before any image is linked into a page.