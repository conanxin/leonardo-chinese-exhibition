# Second Exhibition Working Directory

- Working title: 《植物图谱与视觉分类：从自然史图像到知识秩序》
- Status: production-deployed-v5.3
- Deployment: production-deployed-v5.3 (publicly available through the controlled Pages artifact at https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/)
- Current stage: v5.3b production-state-reconciliation (post-deployment wording reconciliation)
- Imported assets (historical): 6 — each carries `import_status: imported-not-deployed` (v4.5, immutable)
- Per-asset current publication status: `published-in-v5.3`
- Live Leonardo exhibition: unchanged at root (`site/index.html` still 92,976 B, v2.9 marker still 1)

This directory holds the working copy of the second real exhibition. The public subtree (`second-exhibition/site/` + `second-exhibition/assets/images/` allowlisted files) is publicly available through the controlled Pages artifact since v5.3 controlled deployment (commits f84e53f + 83ab6d8). Internal-only artefacts — `second-exhibition/data/`, source/rights evidence, asset-import-manifest.json, asset-checksums.sha256 — remain non-public by design and are excluded from the Pages upload by the v5.3 staging builder allowlist.

## Asset inventory

See `assets/asset-import-manifest.json` (machine-readable, immutable v4.5 import record) and `assets/asset-checksums.sha256` (SHA-256 of every file in `assets/images/`). The human-readable inventory is `docs/IMPORTED_ASSET_INVENTORY_v4.5.md` (in `docs/IMPORTED_ASSET_INVENTORY_v4.5.md` of the project root).

## Source and rights evidence

See `docs/SOURCE_AUDIT_MANIFEST.md` and `docs/RIGHTS_AND_SOURCES.md` in this directory. These two files are immutable historical evidence and are excluded from the Pages upload. Public availability of the second exhibition is not a legal opinion.

## Deployment safety

The v5.3 GitHub Pages workflow runs the staging builder and staging gate before any `upload-pages-artifact` step. Only the allowlisted public artifact (root index + root assets + `second-exhibition/{index.html, style.css, script.js}` + `second-exhibition/assets/images/*.jpg,png,webp`) reaches Pages. `second-exhibition/data/`, `second-exhibition/docs/`, `second-exhibition/assets/asset-import-manifest.json`, `second-exhibition/assets/asset-checksums.sha256`, source/rights evidence, the second-exhibition staging-builder audit directory, the second-exhibition dry-run report, and the second-exhibition roundtrip directory are all excluded.

## Next round

The next round is `v4.6-second-exhibition-repository-build`, which has its own source/rights re-verification gate before any image is linked into a page.