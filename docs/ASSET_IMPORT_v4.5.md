# v4.5 — Asset Import

Round: **v4.5-asset-import**
Round status: **partial** (5 of 6 ready-for-asset-import candidates imported)
Source tag: **v3.4-real-second-exhibition-hardening** (`81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`)
Baseline commit: `01923ea9689f509d3547c64339680e8c571952de`

---

## Goal of this round

Import the six `ready-for-asset-import` candidates from v4.4b as **repository-only assets** under `second-exhibition/assets/images/`, with a machine-readable manifest, a SHA-256 checksum file, per-asset source/rights evidence, and an independent asset gate. **This round does not deploy, does not modify any live site, and does not create any tag or GitHub Release.**

## What changed

| Action | Result |
|---|---|
| `second-exhibition/assets/images/` created | yes (new directory, holds 5 images) |
| Files imported | 5 (C-01, C-03, C-08, C-09, C-10) |
| Files blocked-from-import | 1 (C-06) |
| `second-exhibition/assets/asset-import-manifest.json` created | yes (machine-readable, 12,390 bytes) |
| `second-exhibition/assets/asset-checksums.sha256` created | yes (5 entries) |
| `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` created | yes (per-asset audit evidence) |
| `second-exhibition/docs/RIGHTS_AND_SOURCES.md` created | yes (per-asset rights summary) |
| `second-exhibition/README.md` created | yes (directory orientation) |
| `scripts/second_exhibition_asset_gate.py` created | yes (independent gate, exit 0) |
| Live site modified | **no** |
| New tag created | **no** |
| New GitHub Release | **no** |

## What did NOT change

- `site/index.html`, `site/style.css`, `site/script.js` — unchanged.
- `_template/site/`, `_template/data/` — unchanged.
- `_pilots/second-exhibition-pilot/` — unchanged.
- `scripts/template_quality_gate.py` — unchanged.
- `posts/`, `case-study/`, `release-assets/` — unchanged.
- Existing git tags (`v3.2-*`, `v3.3-*`, `v3.4-*`) — unchanged.
- Existing GitHub Releases — unchanged.

## C-06 gap (NMNH Botany catalog 1529703)

The candidate media URLs for NMNH Botany catalog 1529703 returned HTTP 404 (NMNH Ke Emu collection system does not expose a stable per-item media URL for that catalog number). Per brief, no unverified replacement image was substituted.

A secondary inconsistency was observed: the irnstamp value `2793935` recorded in v4.4b evidence maps to an NMNH Botany record whose on-page `<title>` reads **"Rhynchanthus longiflorus, Myitkyina, Myanmar"** — not the *Aconitum bulbilliferum* taxon recorded in v4.4b evidence. The catalog-number → irnstamp relationship could not be confirmed during v4.5 download verification.

**Resolution:** C-06 is recorded as `blocked-from-import` in the manifest and inventory. The next round (`v4.5b-source-gap-fix`) must:
1. Re-derive the correct irnstamp for catalog 1529703 from a fresh NMNH Botany search.
2. Confirm the on-page taxon matches *Aconitum bulbilliferum*.
3. Obtain a stable per-item media URL.
4. Re-record dataset-level CC0 1.0 basis from the live si.edu Terms page.

## Asset status semantics

Every imported asset is recorded as `imported-not-deployed`. This means:

- The file lives in `second-exhibition/assets/images/`.
- It is **not** linked into `site/index.html`, `site/script.js`, `site/style.css`, or `second-exhibition/site/`.
- It is **not** deployed to GitHub Pages.
- It is **not** associated with any git tag or GitHub Release.
- The asset gate enforces that no protected site path references any v4.5 image filename.

The forbidden labels — `approved`, `deployed`, `live`, `safe for commercial use`, `cleared for all uses` — are intentionally not used anywhere in this round.

## Validation

- `scripts/second_exhibition_asset_gate.py` — **PASS**, 5 imported, 1 blocked.
- `scripts/template_quality_gate.py` — **PASS**, 37/37 (re-run after all writes; expected unchanged).
- Live byte size of https://conanxin.github.io/leonardo-chinese-exhibition/ — **unchanged**.

## Next round

- **If** v4.5b resolves C-06 and the ready count remains ≥ 4: `v4.6-second-exhibition-site-build` is the next legitimate step. That round will have its own source/rights re-verification gate before any image is linked into a page.
- **If** v4.5b still leaves ready count < 4: continue source-gap research. **Do not enter site build.**