# Second Exhibition Working Directory

- Working title: 《植物图谱与视觉分类：从自然史图像到知识秩序》
- Status: repository-only
- Deployment: not deployed
- Current stage: v4.5 asset import
- Imported assets: 6
- Live Leonardo exhibition: unchanged
- Future site build: separate v4.6 round

This directory holds the **repository-only** working copy of the second real exhibition. Nothing in `second-exhibition/` is linked into the live site (`site/index.html`, `site/script.js`, `site/style.css`), nothing is deployed to GitHub Pages, and nothing is associated with a git tag or GitHub Release.

## Asset inventory

See `assets/asset-import-manifest.json` (machine-readable) and `assets/asset-checksums.sha256` (SHA-256 of every file in `assets/images/`). The human-readable inventory is `docs/IMPORTED_ASSET_INVENTORY_v4.5.md` (in `docs/IMPORTED_ASSET_INVENTORY_v4.5.md` of the project root).

## Source and rights evidence

See `docs/SOURCE_AUDIT_MANIFEST.md` and `docs/RIGHTS_AND_SOURCES.md` in this directory. The current round is repository-only and does not constitute a legal opinion.

## Deployment safety

`second-exhibition/site/` does **not** exist. No file in `second-exhibition/` is referenced from `site/`. Do not treat this directory as a deployed exhibition. Do not push `second-exhibition/site/` even in a future round without first re-running the full source-and-rights audit.

## Next round

The next round is `v4.6-second-exhibition-repository-build`, which has its own source/rights re-verification gate before any image is linked into a page.