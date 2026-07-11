# v4.4 Asset Filename Map

> Scope of this document: a stable filename map for the 6 v4.3 `selected-for-build-planning` candidates. v4.4 records the proposed filenames only — **no file is created in v4.4**, and **no image is downloaded in v4.4**. The filenames below are what v4.5 (or v4.4b + v4.5) will use when the per-item image is actually downloaded.

> 收口时间：v4.4 prep round 结束点。下一 round 是 **v4.4b — Source Gap Fix**，不是 v4.5 asset import。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `978f8eddf9a8dcdf8e9f6b209f5f764c6192062c` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | **92,976 B** (baseline preserved) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |

---

## Naming rules

1. The filename is the **project-local name** of the per-item image. It is not the BHL / NMNH / Met / Rijksmuseum identifier, but it must be **deterministically derivable** from that identifier (so a reader can re-derive it from the manifest row).
2. The filename ends in `.jpg` (the per-item image is a JPEG in every institution's policy). WebP / PNG / TIFF are not used unless the institution's per-item media is in that format — v4.4 does not pick a per-item image, so the format is fixed at `.jpg`.
3. The filename uses **lowercase, ASCII, hyphens** (no spaces, no underscores, no non-ASCII characters).
4. The filename is **unique per row**. Two rows from the same institution must not share a filename. (BHL C-01 vs C-03 is resolved by suffix `-plate` vs `-page` — they are different visual uses of the same item.)
5. The filename must not contain any of the forbidden project words: `Leonardo`, `Codex Atlanticus`, `Royal Collection Trust`, `Leonardo//thek@`. (These are scanned by `scripts/template_quality_gate.py` Section C.)

---

## Filename map (6 rows)

| ID | Institution | Item identifier (basis) | Proposed filename | Section | v4.4 status |
|---|---|---|---|---|---|
| C-01 | BHL | BHL item 318921 | `bhl-318921-plate.jpg` | Section 1 (观察) | `ready-for-asset-import` |
| C-03 | BHL | BHL item 318921 | `bhl-318921-page.jpg` | Section 3 (复制) | `ready-for-asset-import` — PD subset only |
| C-06 | NMNH Botany | accession number (pending v4.4b) | `nmnh-<accession_number>.jpg` | Section 2 (分类) | `defer` |
| C-08 | The Met | object 285149 / accession 2003.562.3 | `met-285149.jpg` | Section 3 (复制) — alternate | `defer` (double-confirmation pending v4.4b) |
| C-09 | Rijksmuseum | `objectNumber` (pending v4.4b) | `rijksmuseum-<object_number>.jpg` | Section 1 (观察) primary / Section 2 (分类) alternate | `defer` |
| C-10 | Rijksmuseum | `objectNumber` (pending v4.4b, same as C-09) | (derives from C-09's filename) | Section 4 (再组织) | `defer` |

---

## Per-row derivation notes

### C-01 — `bhl-318921-plate.jpg`

- Basis: BHL item 318921 (the item-level identifier is in the filename).
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
- `find . -name "bhl-318921-*" -o -name "nmnh-*" -o -name "met-285149*" -o -name "rijksmuseum-*"` returns **no hits** in v4.4 (the proposed names do not yet exist as files).

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

The next round is **v4.4b — Source Gap Fix**, which picks the deferred candidates' specific items and replaces the `pending v4.4b` placeholders in this map. v4.5 — Asset Import — uses this map (and the v4.4b updates) to execute the actual download.