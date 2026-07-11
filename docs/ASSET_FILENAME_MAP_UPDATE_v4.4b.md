# v4.4b Asset Filename Map Update

> Scope: v4.4b update to the asset filename map. v4.4b records the proposed filenames and the future local paths under `second-exhibition/assets/images/`. v4.4b does **not** create the directory, does **not** download any image, and does **not** create any file under that path. The filenames below are what v4.5 (asset import) will use when the per-item image is actually downloaded. The future local path uses `second-exhibition/assets/images/` as a logical prefix; the directory is not created in v4.4b.

> 收口时间：v4.4b source gap fix round 结束点。下一 round 是 **v4.5 Asset Import**。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `ad66d6db39622c19e8dc50238da1d9403defa7e9` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | **92,976 B** (preserved, v4.4b does not modify `site/`) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| Future local path prefix | `second-exhibition/assets/images/` (**not created** in v4.4b) |

---

## Filename rules (unchanged from v4.4)

1. **Lowercase** — no uppercase characters anywhere in the filename.
2. **Institution prefix** — the first token is the institution's short code (`bhl`, `nmnh`, `met`, `rijksmuseum`).
3. **Stable short identifier** — after the institution prefix, the institution's per-item identifier (`318921`, `1529703`, `285149`, `rp-f-f80152`, `rp-f-f80313`) is appended with a hyphen.
4. **No spaces** — every separator is a single hyphen (`-`).
5. **Extension preserved from source** — `.jpg` for Rijksmuseum (Micrio IIIF Image API serves JPEG), `.jpg` for Met (Collection API serves JPEG), `.png` for NMNH (the media endpoint serves PNG thumbnails). The map below defaults to `.jpg` for BHL, NMNH, Met, Rijksmuseum (the source-format is documented per-row).
6. **Never overwrite existing files** — the import round must check the destination path first and refuse to overwrite. If a file already exists, the import round halts and reports.
7. **Future import only** — the filenames below are **proposed** for the future import round. v4.4b does not create the files, the directory, or the import-script call. The directory `second-exhibition/assets/images/` is not created in v4.4b.

---

## Filename map (6 rows)

| ID | Concrete item identifier | Proposed filename | Future local path | Image / IIIF URL | Status | Collision check |
|---|---|---|---|---|---|---|
| C-01 | BHL item 318921 | `bhl-318921-plate.jpg` | `second-exhibition/assets/images/bhl-318921-plate.jpg` | per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `ready-for-asset-import`, `not downloaded` | No collision (filename is new; not present in `release-assets/` or `site/` baseline). |
| C-03 | BHL item 318921 | `bhl-318921-page.jpg` | `second-exhibition/assets/images/bhl-318921-page.jpg` | per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `ready-for-asset-import` (PD subset only), `not downloaded` | No collision (filename is new; suffix `-page` distinguishes from C-01's `-plate`). |
| C-06 | NMNH Botany, US Catalog 1529703 (Barcode 00103617) | `nmnh-1529703.jpg` | `second-exhibition/assets/images/nmnh-1529703.jpg` | `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes` (HEAD test HTTP/2 200, `Content-Type: image/png`; URL recorded, not downloaded) | `ready-for-asset-import`, `not downloaded` | No collision (filename is new). |
| C-08 | Met objectID 285149 / accession 2003.562.3 | `met-285149.jpg` | `second-exhibition/assets/images/met-285149.jpg` | `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` (URL recorded, not downloaded) | `ready-for-asset-import`, `not downloaded` | No collision (filename is new). |
| C-09 | Rijksmuseum objectNumber `RP-F-F80152` (persistent URL `https://id.rijksmuseum.nl/200407820`) | `rijksmuseum-rp-f-f80152.jpg` | `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` | `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (HEAD test HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded) | `ready-for-asset-import`, `not downloaded` | No collision (filename is new; objectNumber `RP-F-F80152` is in the filename). |
| C-10 | Rijksmuseum objectNumber `RP-F-F80313` (persistent URL `https://id.rijksmuseum.nl/200408260`) | `rijksmuseum-rp-f-f80313.jpg` | `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` | `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (HEAD test HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded) | `ready-for-asset-import`, `not downloaded` | No collision (filename is new; objectNumber `RP-F-F80313` is in the filename; C-09 and C-10 objectNumbers are distinct). |

---

## Per-row derivation notes

### C-01 — `bhl-318921-plate.jpg`

- Basis: BHL item 318921 (the item-level identifier is in the filename).
- Suffix `-plate` distinguishes the **plate-level** use (Section 1 — observation / single-page visual specimen) from the **book-level** use (Section 3 — see C-03).
- The page number is **not** in the filename — v4.4b records the per-page image URL pattern, not a specific page. v4.5 picks the per-page record and copies the file to `bhl-318921-plate.jpg`.

### C-03 — `bhl-318921-page.jpg`

- Basis: BHL item 318921.
- Suffix `-page` distinguishes the **book-level** use (Section 3 — full-page scan) from the **plate-level** use (Section 1 — see C-01).
- The page number is **not** in the filename for the same reason as C-01.

### C-06 — `nmnh-1529703.jpg`

- Basis: NMNH Botany US Catalog Number 1529703 (the accession number is in the filename).
- The Barcode (00103617) and EZID (`http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920`) are recorded in the evidence table (`docs/ITEM_EVIDENCE_COMPLETION_v4.4b.md`) but not in the filename (the US Catalog Number is the public-facing identifier).
- v4.4b v4.4 mapping updated: the placeholder `<accession_number>` from v4.4 (`docs/ASSET_FILENAME_MAP_v4.4.md`) is replaced with the concrete value `1529703`.

### C-08 — `met-285149.jpg`

- Basis: Met objectNumber 285149 (the accession 2003.562.3 is *not* in the filename because the object number is the public-facing identifier on Met's own page).
- The filename is fixed; only the **download step** is gated by the double-confirmation in v4.5.

### C-09 — `rijksmuseum-rp-f-f80152.jpg`

- Basis: Rijksmuseum `objectNumber` (a stable alphanumeric identifier on Rijksmuseum's own page).
- The objectNumber is **fully embedded** in the filename in lowercase: `rp-f-f80152` (Rijksmuseum object numbers are conventionally lowercase). The full objectNumber is preserved so that the filename is unambiguously derivable from the institution's record.
- The persistent URL PID (`https://id.rijksmuseum.nl/200407820`) is recorded in the evidence table but not in the filename (the objectNumber is the public-facing identifier).

### C-10 — `rijksmuseum-rp-f-f80313.jpg`

- Basis: Rijksmuseum `objectNumber` `RP-F-F80313` (lowercase `rp-f-f80313` in the filename).
- **Distinct from C-09** — different objectNumber, different persistent URL PID, different micrioId, different IIIF Image API URL.
- C-09 and C-10 are two distinct per-item records. The filename reflects this: `rijksmuseum-rp-f-f80152.jpg` vs `rijksmuseum-rp-f-f80313.jpg`.

---

## Why this map is empty (no files exist in v4.4b)

A filename map is only `final` once the per-item image has been downloaded and saved under that name. In v4.4b, no image is downloaded — the map is therefore a **proposed** map, and v4.4b verifies by absence:

- `find . -path ./.git -prune -o -path ./.firecrawl -prune -o \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" -o -iname "*.tif" -o -iname "*.tiff" \) -print | sort` returns the **same set** as the v4.4 baseline (no new files in the staged set).
- `find . -name "bhl-318921-*" -o -name "nmnh-*" -o -name "met-285149*" -o -name "rijksmuseum-*"` returns **no hits** in v4.4b (the proposed names do not yet exist as files).
- `ls second-exhibition/` (if it exists) does not contain `assets/images/`. The directory is not created.

The map graduates to `final` in v4.5 when the actual download happens.

---

## Forbidden filename content

The following substrings must **not** appear in any v4.4b or later asset filename:

- `Leonardo` (case-insensitive)
- `codex-atlanticus` / `Codex-Atlanticus`
- `royal-collection-trust` / `Royal-Collection-Trust`
- `Leonardo//thek@`

These are scanned by `scripts/template_quality_gate.py` Section C — and they are *also* forbidden as filenames so the live site cannot accidentally surface them as image alt text or as a `<img src="...">` URL.

---

## Round boundary

The next round is **v4.5 — Asset Import**, which uses this map (and the v4.4b evidence table) to execute the actual download.