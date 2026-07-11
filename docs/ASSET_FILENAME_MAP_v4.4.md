# v4.4 Asset Filename Map

> Scope: a stable filename map for the 6 v4.3 `selected-for-build-planning` candidates. v4.4 records the proposed filenames only — **no file is created in v4.4**, and **no image is downloaded in v4.4**. The future local path uses `second-exhibition/assets/images/` as a logical prefix, but **this directory is not created in v4.4** (the directory creation is a v4.5 step).

> 收口时间：v4.4 asset import prep round 结束点。下一 round 是 **v4.4b-source-gap-fix**，不是 v4.5。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `166e73cff276a8111f098da7c6ff674b39ff778d` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | **92,976 B** (preserved) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |

---

## Filename rules

1. **Lowercase** — no uppercase characters anywhere in the filename.
2. **Institution prefix** — the first token is the institution's short code (`bhl`, `nmnh`, `met`, `rijksmuseum`). This makes the source of each asset visually obvious in a directory listing.
3. **Short identifier** — after the institution prefix, the institution's per-item identifier (`318921`, `<accession_number>`, `285149`, `<object_number>`) is appended with a hyphen. The identifier is short enough to read in a URL or in a manifest row.
4. **No spaces** — every separator is a single hyphen (`-`). No underscores, no dots, no spaces.
5. **Extension preserved from source** — if the source institution serves the image as `.jpg`, the local filename ends in `.jpg`. If the source serves `.png` / `.webp` / `.tif`, the extension follows. The v4.4 map defaults to `.jpg` because every institution in this set serves JPEG as the default image format; v4.5 may revise per item.
6. **Never overwrite existing files** — the import round must check the destination path first and refuse to overwrite. If a file already exists, the import round halts and reports.
7. **Future import only** — the filenames below are **proposed** for the future import round. v4.4 does not create the files, the directory, or the import-script call. The directory `second-exhibition/assets/images/` is not created in v4.4.

---

## Filename map (6 rows)

| ID | Proposed filename | Future local path | Source URL | Image / IIIF URL | Import status | Notes |
|---|---|---|---|---|---|---|
| C-01 | `bhl-318921-plate.jpg` | `second-exhibition/assets/images/bhl-318921-plate.jpg` | https://www.biodiversitylibrary.org/item/318921 | per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `wait for v4.5 asset import`, `not downloaded` | Per-page `<Copyright Status>` must be `Public domain` at the time of download. CC BY-NC-SA subset rejected. |
| C-03 | `bhl-318921-page.jpg` | `second-exhibition/assets/images/bhl-318921-page.jpg` | https://www.biodiversitylibrary.org/item/318921 | per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `wait for v4.5 asset import`, `not downloaded` | Per-page `<Copyright Status>` must be `Public domain`. CC BY-NC-SA subset blocked at per-page level. |
| C-06 | `nmnh-<accession_number>.jpg` | `second-exhibition/assets/images/nmnh-<accession_number>.jpg` | https://collections.nmnh.si.edu/search/botany/ | per-item image URL on the per-item record (not yet selected in v4.4) | `wait for v4.4b-source-gap-fix`, `not downloaded` | Per-item accession number pending v4.4b. Per-item CC0 1.0 must be confirmed. |
| C-08 | `met-285149.jpg` | `second-exhibition/assets/images/met-285149.jpg` | https://www.metmuseum.org/art/collection/search/285149 | Met Collection API `primaryImage` field on object 285149 (URL recorded, not downloaded) | `wait for v4.4b-source-gap-fix`, `not downloaded` | Double-confirmation (Collection API `isPublicDomain: true` + public-page Open Access icon) pending v4.4b. |
| C-09 | `rijksmuseum-<object_number>.jpg` | `second-exhibition/assets/images/rijksmuseum-<object_number>.jpg` | https://www.rijksmuseum.nl/en/research/our-research/print-room | per-item Rijksstudio image URL or IIIF Image API URL (not yet selected in v4.4) | `wait for v4.4b-source-gap-fix`, `not downloaded` | Per-item `objectNumber` and `licence` field pending v4.4b. |
| C-10 | (derives from C-09's per-item image; same Rijksmuseum object) | `second-exhibition/assets/images/rijksmuseum-<object_number>.jpg` | https://www.rijksmuseum.nl/en/research/our-research/print-room | per-item IIIF Presentation API manifest URL (not yet selected in v4.4) | `wait for v4.4b-source-gap-fix`, `not downloaded` | Same Rijksmuseum object as C-09; per-item `license` field on the IIIF manifest pending v4.4b. |

---

## Import status values (only these four appear in the table above)

| Import status | Meaning |
|---|---|
| `not downloaded` | The per-item image has not been downloaded in v4.4 (and is not downloaded at all yet). This tag applies to every row in v4.4. |
| `wait for v4.5 asset import` | The row is `ready-for-asset-import` in v4.4; the future import round (v4.5) executes the download. |
| `wait for v4.4b-source-gap-fix` | The row is `defer` in v4.4; v4.4b picks the per-item record, then v4.5 executes the download. |
| `blocked-from-import` | The row's rights status makes import impossible. (Not used as a row-level import status in v4.4 — C-14 and the C-03 CC BY-NC-SA subset are policy-level entries.) |

The phrase "approved" is **not used** as an import status. The status `wait for v4.4b-source-gap-fix` is the deferred status for C-06 / C-08 / C-09 / C-10.

---

## Per-row derivation notes

### C-01 — `bhl-318921-plate.jpg`

- Basis: BHL item 318921.
- Suffix `-plate` distinguishes the **plate-level** use (Section 1 — observation / single-page visual specimen) from the **book-level** use (Section 3 — see C-03).
- The page number is **not** in the filename — v4.4 records the per-page image URL pattern, not a specific page. v4.5 picks the per-page record and copies the file to `bhl-318921-plate.jpg`.

### C-03 — `bhl-318921-page.jpg`

- Basis: BHL item 318921.
- Suffix `-page` distinguishes the **book-level** use (Section 3 — full-page scan) from the **plate-level** use (Section 1 — see C-01).
- The page number is **not** in the filename for the same reason as C-01.

### C-06 — `nmnh-<accession_number>.jpg`

- Basis: NMNH Botany accession number.
- The accession number is **not yet known** — v4.4 records the entry URL (https://collections.nmnh.si.edu/search/botany/) only. v4.4b picks a specific CC0-marked record and captures the accession number.
- When v4.4b writes the row, the filename becomes `nmnh-<N>.jpg` where `<N>` is the accession number.

### C-08 — `met-285149.jpg`

- Basis: Met object number **285149** (the accession 2003.562.3 is *not* in the filename because the object number is the public-facing identifier on Met's own page).
- The filename is fixed; only the **download step** is gated by the double-confirmation in v4.4b.

### C-09 / C-10 — `rijksmuseum-<object_number>.jpg`

- Basis: Rijksmuseum `objectNumber` (a stable alphanumeric identifier on Rijksmuseum's own page).
- C-09 and C-10 are **the same physical object** — C-10 is the IIIF Presentation API manifest of the object whose per-item image is downloaded for C-09. C-10 does not get its own filename; the image bytes flow from C-09.
- The `objectNumber` is **not yet known** — v4.4 records the entry URL (https://www.rijksmuseum.nl/en/research/our-research/print-room) only. v4.4b picks a specific Rijksprentenkabinet object.

---

## Why this map is empty (no files exist in v4.4)

A filename map is only `final` once the per-item image has been downloaded and saved under that name. In v4.4, no image is downloaded — the map is therefore a **proposed** map, and v4.4 verifies by absence:

- `find . -path ./.git -prune -o -name "*.jpg" -print -o -name "*.jpeg" -print -o -name "*.png" -print -o -name "*.webp" -print -o -name "*.tif" -print -o -name "*.tiff" -print` returns the **same set** as the v4.3 baseline.
- `find . -name "bhl-318921-*" -o -name "nmnh-*" -o -name "met-285149*" -o -name "rijksmuseum-*" -o -path "*second-exhibition/assets/images*"` returns **no hits** in v4.4 (the proposed names do not yet exist as files, and the directory `second-exhibition/assets/images/` does not yet exist).

The map graduates to `final` in v4.4b (when per-item selection closes the source gap) or v4.5 (when the actual download happens).

---

## Forbidden filename content

The following substrings must **not** appear in any v4.4 or later asset filename:

- `Leonardo` (case-insensitive)
- `codex-atlanticus` / `Codex-Atlanticus`
- `royal-collection-trust` / `Royal-Collection-Trust`
- `Leonardo//thek@`

These are scanned by `scripts/template_quality_gate.py` Section C — and they are *also* forbidden as filenames so the live site cannot accidentally surface them as image alt text or as a `<img src="...">` URL.

---

## Round boundary

The next round is **v4.4b-source-gap-fix**, which picks the deferred candidates' specific items and replaces the `<accession_number>` / `<object_number>` placeholders in this map. v4.5 — Asset Import — uses this map (and the v4.4b updates) to execute the actual download.