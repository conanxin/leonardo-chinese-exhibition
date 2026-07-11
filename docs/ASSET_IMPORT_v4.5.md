# v4.5 — Asset Import

Round: **v4.5-asset-import**
Round status: **PASS** — 6 of 6 ready-for-asset-import candidates imported into the repository.
Baseline commit: `01923ea9689f509d3547c64339680e8c571952de`
Source tag: `v3.4-real-second-exhibition-hardening` → `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`

---

## Import goal

Import the 6 v4.4b `ready-for-asset-import` candidates as **repository-only assets** under `second-exhibition/assets/images/`, with a machine-readable manifest, a SHA-256 checksum file, per-asset source/rights evidence, and an independent asset gate. This round does **not** deploy, does **not** modify any live site, and does **not** create a tag or GitHub Release.

## Six imported candidate IDs (all 6 PASS)

| ID | Institution | Filename | Bytes | SHA-256 |
|---|---|---|---|---|
| C-01 | Biodiversity Heritage Library | `bhl-318921-page-603998-c01.webp` | 306126 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` |
| C-03 | Biodiversity Heritage Library | `bhl-318921-page-603962-c03.webp` | 262498 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` |
| C-06 | Smithsonian NMNH Botany | `smithsonian-nmnh-1529703.png` | 3550 | `75f523b06cc1a62713de51b1ba3a51fc4d43c4ac19268c48478d30c9e2af73a1` |
| C-08 | The Metropolitan Museum of Art | `met-285149.jpg` | 95001 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| C-09 | Rijksmuseum | `rijksmuseum-rp-f-f80152.jpg` | 294445 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| C-10 | Rijksmuseum | `rijksmuseum-rp-f-f80313.jpg` | 191606 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |

All six are recorded as `imported-not-deployed`. None is linked into `site/index.html`, `site/script.js`, `site/style.css`, or `second-exhibition/site/`. None is deployed to GitHub Pages. None is associated with a tag or Release.

## Preflight evidence summary

URLs were re-validated with HEAD probes inside this round:

| ID | Media URL | HEAD result |
|---|---|---|
| C-01 | https://www.biodiversitylibrary.org/pageimage/603998 | HTTP/2 200, `image/webp`, 306126 B |
| C-03 | https://www.biodiversitylibrary.org/pageimage/603962 | HTTP/2 200, `image/webp`, 262498 B |
| C-06 | https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes | HTTP/2 200, `image/png`, 3550 B |
| C-08 | https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg | HTTP/2 200, `image/jpeg`, 95001 B |
| C-09 | https://iiif.micr.io/vGipU/full/1024,/0/default.jpg | HTTP/2 200, `image/jpeg`, 294445 B |
| C-10 | https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg | HTTP/2 200, `image/jpeg`, 191606 B |

## BHL page-level selection

- **C-01** uses BHL page 603998 (Pistillaria plate).
- **C-03** uses BHL page 603962 (Cycas revoluta plate).

Both pages are inside BHL item 318921. The two pages have distinct SHA-256 values. C-03 is **PD subset only** — the CC BY-NC-SA subset of BHL item 318921 remains blocked.

The v4.5 final filenames add the page-id and a `c01` / `c03` suffix (`bhl-318921-page-<pageid>-c<XX>.webp`) for traceability. BHL's `/pageimage/<id>` endpoint serves WebP, so the file extension is `.webp` (matches MIME type `image/webp`).

## C-08 double-confirmation

Both indicators were re-confirmed inside v4.5:

1. Met Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` returns `isPublicDomain: true`.
2. The public object page `https://www.metmuseum.org/art/collection/search/285149` displays the Public Domain indicator.

The web-large derivative was used for download (`https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg`, 449x624, 95001 B). The original URL `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` was also re-confirmed live during v4.5.

## C-09 / C-10 per-item rights evidence

Both Rijksmuseum objects were re-confirmed on the day of import. The public object pages carry a per-item Copyright field that reads verbatim `Public domain` with a hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en` (CC0 1.0). This is **per-item evidence**, not a derivation from the institution-wide policy.

- **C-09**: objectNumber `RP-F-F80152`, persistent URL `https://id.rijksmuseum.nl/200407820`, Micrio ID `vGipU`.
- **C-10**: objectNumber `RP-F-F80313`, persistent URL `https://id.rijksmuseum.nl/200408260`, Micrio ID `PrcdN`.

The two objects are distinct (different objectNumbers, different persistent URLs, different Micrio IDs, different titles — *Zeestreepvaren* vs *Wolfsklauw*).

## C-10 manifest caveat

The Rijksmuseum IIIF Presentation API manifest at `https://iiif.micr.io/PrcdN/manifest.json` returned HTTP 404 during v4.5 verification. Manifest-based evidence was intentionally **omitted** from this round. The per-item public object page Copyright field (`Public domain` / CC0 1.0) is the authoritative licence source for the credit line.

## C-06 dataset-level rights wording

The Smithsonian's Open Access release is **dataset-level CC0 1.0**. No per-item licence field is rendered on the NMNH Botany record page. The dataset-level CC0 1.0 statement (verified on `https://www.si.edu/openaccess/faq`) is the licence basis for C-06; the credit line uses the **dataset-level CC0 1.0** wording verbatim. Do not invent a per-item licence field that does not exist on the institution's own page.

The `/media/?i=...` endpoint serves a 90x90 PNG thumbnail (3550 B). A higher-resolution derivative URL was not exposed by the NMNH Ke Emu API at import time and was not substituted from a third-party mirror. v4.6 build will re-check and request a higher-resolution derivative via the NMNH IPT API if needed.

## Live no-change confirmation

Live byte size, markers, and `script.js` HTTP status were re-verified after import:

| Metric | Value |
|---|---|
| Live byte size of `https://conanxin.github.io/leonardo-chinese-exhibition/` | 92,976 B (preserved) |
| v2.9-real-source-rights-audit marker | 1 (preserved) |
| `image-placeholder-pro` count | 0 (preserved) |
| v4 title (植物图谱与视觉分类) count | 0 (preserved; v4.5 is repository-only) |
| `script.js` HEAD | HTTP/2 200 (preserved) |

In addition, none of the six `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/assets/images/<filename>` URLs are exposed on GitHub Pages — the Pages workflow deploys only the `site/` directory, so `second-exhibition/` is not in the deploy artifact.

## Forbidden status words

The status words `approved`, `deployed`, `live`, `safe for commercial use`, and `cleared for all uses` are intentionally **not used** anywhere in v4.5. Every imported asset carries the status `imported-not-deployed`.

## Next round

The next round is **v4.6-second-exhibition-repository-build**, which has its own source/rights re-verification gate before any image is linked into a page. v4.6 does not deploy to GitHub Pages in this scope; it builds a self-contained `second-exhibition/` site that mirrors the v4.6 draft structure.