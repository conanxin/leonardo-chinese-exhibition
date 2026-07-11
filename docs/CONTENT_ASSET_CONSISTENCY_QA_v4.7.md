# Content and Asset Consistency QA v4.7

## Baseline

- Asset import manifest: `second-exhibition/assets/asset-import-manifest.json`
- Asset data: `second-exhibition/data/assets.json`
- Site page: `second-exhibition/site/index.html`
- Source audit: `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`
- Rights and sources: `second-exhibition/docs/RIGHTS_AND_SOURCES.md`
- Build usage: `second-exhibition/docs/BUILD_ASSET_USAGE.md`

## Candidate ID matrix

| ID | Filename | Identifier | Institution | Section | Rights basis | Import status |
|---|---|---|---|---|---|---|
| C-01 | `bhl-318921-page-603998-c01.webp` | BHL item 318921 / page 603998 | Biodiversity Heritage Library | section-1-observation | Public-domain page subset | imported-not-deployed |
| C-03 | `bhl-318921-page-603962-c03.webp` | BHL item 318921 / page 603962 | Biodiversity Heritage Library | section-3-copy | Public-domain page subset only | imported-not-deployed |
| C-06 | `smithsonian-nmnh-1529703.png` | USNM Catalog 1529703 | Smithsonian National Museum of Natural History / NMNH Botany | section-2-classification | Smithsonian Open Access / CC0 1.0 (dataset-level) | imported-not-deployed |
| C-08 | `met-285149.jpg` | The Met 285149 / accession 2003.562.3 | The Metropolitan Museum of Art | section-4-reorganization | Public Domain (API isPublicDomain=true + public-page confirmation) | imported-not-deployed |
| C-09 | `rijksmuseum-rp-f-f80152.jpg` | RP-F-F80152 | Rijksmuseum / Rijksprentenkabinet | section-4-reorganization | per-item Public domain / CC0 1.0 | imported-not-deployed |
| C-10 | `rijksmuseum-rp-f-f80313.jpg` | RP-F-F80313 | Rijksmuseum / Rijksprentenkabinet | section-4-reorganization | per-item Public domain / CC0 1.0 | imported-not-deployed |

## Consistency checks

- Candidate IDs in the import manifest, `assets.json`, and `index.html` are identical: `C-01, C-03, C-06, C-08, C-09, C-10`.
- Filenames in the manifest, checksum file, and `assets.json` match the files on disk.
- Each asset's `local_path` points to `../assets/images/<filename>`.
- SHA-256 values match across the import manifest, the checksum file, and the actual files.
- All six SHA-256 values are unique.
- C-01 and C-03 SHA-256 values are different.

## Source notes and credit lines

- Every asset in `assets.json` has a non-empty `source_note` and a non-empty `credit_line`.
- The site page renders these as `.source-note` and `.credit-line` blocks.
- Source notes point to the original institutional object or page URLs.
- Credit lines include the institution and rights statement.

## C-03 caution

- C-03 is explicitly labeled as a Public-domain page subset only.
- The CC BY-NC-SA subset of the same BHL item is not imported and is not referenced as a usable asset.
- This caution appears in the asset data, the build usage document, and the site page.

## C-06 low-resolution handling

- `low_resolution = true`.
- `lightbox_enabled = false`.
- Display size is small, not hero.
- A visible note explains the 90 × 90 px limitation and the dataset-level rights basis.

## C-08 double-confirmation

- The asset data records both API `isPublicDomain=true` and the public page Public Domain indicator.
- The rights document references the Met Collection API and the public object page.

## C-10 caveat

- The Rijksmuseum Presentation API manifest returned HTTP 404 during v4.4b / v4.5 investigation.
- The asset rights basis is therefore based on the per-item `Copyright` field, not on a manifest.
- This caveat is recorded in the build usage document and the rights document.

## Result

- All content/asset consistency checks in `scripts/second_exhibition_repository_qa.py` PASS.

<!-- v4.7-partial-finding -->
## Relationship to the blocking finding

The v4.7 blocker is an ARIA reference defect in the lightbox dialog. It is not a content, candidate-ID, filename, checksum, source-note, credit-line, or asset-integrity conflict. The six imported assets and their repository evidence remain unchanged.
