# leonardo-chinese-exhibition v4.4b — Source Gap Fix Report

## STATUS: PASS

> Scope: prep-only round that closes the per-item evidence gaps for the 4 v4.4 `defer` rows (C-06, C-08, C-09, C-10). v4.4b records per-item / per-licence evidence, records image / IIIF URLs without downloading any image, and produces 5 v4.4b docs + this report. v4.4b does **not** download images, does **not** create `second-exhibition/assets/images/`, does **not** modify `site/` / `_template/` / `_pilots/` / `posts/` / `case-study/` / `release-assets/` / `scripts/template_quality_gate.py`, does **not** create a tag, and does **not** publish a GitHub Release. The status `approved` is **not used**.

---

## 1. Three-piece verification (independently re-checked at round close)

| Piece | Value | Re-check command | Re-check result (verbatim) |
|---|---|---|---|
| Current HEAD (before commit) | `ad66d6db39622c19e8dc50238da1d9403defa7e9` | `git rev-parse HEAD` | **`ad66d6db39622c19e8dc50238da1d9403defa7e9`** |
| Origin/main (before push) | `ad66d6db39622c19e8dc50238da1d9403defa7e9` | `git rev-parse origin/main` | **`ad66d6db39622c19e8dc50238da1d9403defa7e9`** (HEAD == origin/main at round start) |
| Source release | `v3.4-real-second-exhibition-hardening` | `git tag \| tail -1` | **`v3.4-real-second-exhibition-hardening`** |
| Source tag target (annotated → commit) | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` | `git show v3.4-real-second-exhibition-hardening --no-patch --format='%H'` | **`81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`** |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ | `curl -L -s -I` | `HTTP/2 200`, `content-type: text/html` |
| Live byte size (before / after) | **92,976 B** / **92,976 B** (preserved) | `curl -L -s ... \| wc -c` | **`92976`** |
| v2.9 marker count on live | **1** | `grep -c "v2.9-real-source-rights-audit"` | **`1`** |
| `image-placeholder-pro` count on live | **0** | `grep -c "image-placeholder-pro"` | **`0`** |
| `植物图谱与视觉分类` (v4 title) on live | **0** | `grep -c "植物图谱与视觉分类"` | **`0`** (v4 is prep-only, not deployed) |
| `script.js` HTTP status | **HTTP/2 200** | `curl -LIs` | **`HTTP/2 200`, `content-type: application/javascript; charset=utf-8`** |
| Quality gate (before / after) | **PASS, 37/37** | `python3 scripts/template_quality_gate.py` | **`Passed: 37 / Failed: 0 / FINAL STATUS: PASS`** |

---

## 2. Gaps investigated + concrete items completed

| Metric | Count |
|---|---|
| Gaps investigated (v4.4 `defer` rows) | **4** (C-06, C-08, C-09, C-10) |
| Concrete items completed in v4.4b | **4** (C-06, C-08, C-09, C-10 — all promoted from `defer` to `ready-for-asset-import`) |
| Total `ready-for-asset-import` after v4.4b | **6** (C-01, C-03, C-06, C-08, C-09, C-10) |
| `defer` after v4.4b | **0** |
| `blocked-from-import` (row-level) | **0** |
| `replace-with-project-generated-diagram` (row-level) | **0** |
| `approved` | **0** (not used) |
| Approved asset count | **0** |
| Downloaded image count | **0** (v4.4b records URLs only; HEAD test only; transient `/tmp` artifacts cleaned up) |

---

## 3. Per-gap result

### C-06 result

- **Concrete item picked**: NMNH Botany, US Catalog No. **1529703**, Barcode **00103617**, *Aconitum bulbilliferum* Hand.-Mazz. (Ranunculaceae, Type fragment), pressed specimen, China / Sichuan, Handel-Mazzetti H. R. 5202, 17 Sep 1914. EZID `http://n2t.net/ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920`.
- **Item URL**: `https://collections.nmnh.si.edu/search/botany/?bc=00103617`.
- **Rights basis**: dataset-level **CC0 1.0** verbatim from `https://collections.nmnh.si.edu/ipt/resource?r=nmnh_botany` ("License: CC0 1.0"; "publisher has waived all rights to these data and has dedicated them to the Public Domain (CC0 1.0). Users may copy, modify, distribute and use the work, including for commercial purposes, without restriction."). Cross-confirmed on `https://www.gbif.org/dataset/821cc27a-e3bb-4bc5-ac34-89ada245069d` ("Licence CC0 1.0"). Smithsonian Open Access FAQ: `https://www.si.edu/openaccess/faq`.
- **Image URL**: `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes` (HEAD test returned HTTP/2 200, `Content-Type: image/png`; URL recorded, not downloaded).
- **v4.4b status**: `ready-for-asset-import`.

### C-08 double-confirmation result

- **Concrete item**: Met objectID **285149**, *[Botanical Specimen: Fern]*, Unknown (British) per public page / Unknown per API, 1855–60, Albumen silver print from glass negative, Gift of Simon Lowinsky 2003, accession **2003.562.3**, Department: Photographs.
- **Item URL**: `https://www.metmuseum.org/art/collection/search/285149`.
- **Collection API**: `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149`. API response (verified): `isPublicDomain: true`; `primaryImage: https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg`; `accessionNumber: 2003.562.3`; `title: [Botanical Specimen: Fern]`.
- **Public object page (verified)**: title `[Botanical Specimen: Fern]`; "Not on view"; "Public Domain" button visible (Open Access icon); "Download Image" button visible; "Enlarge Image" button visible. objectID 285149 matches the URL. Accession 2003.562.3 matches the API.
- **Double-confirmation result**: **PASS**. (a) API `isPublicDomain: true` ✓. (b) Public-page "Public Domain" button + "Download Image" + "Enlarge Image" controls present ✓.
- **Image URL**: `https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg` (URL recorded, not downloaded).
- **v4.4b status**: `ready-for-asset-import`.

### C-09 per-item licence result

- **Concrete item**: Rijksmuseum objectNumber **RP-F-F80152**, *Zeestreepvaren*, Anna Atkins (photographer, England), c. 1854, photogram (cyanotype) on paper, height 247 mm × width 193 mm.
- **Item URL**: `https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da`.
- **Persistent URL (id.rijksmuseum.nl PID)**: `https://id.rijksmuseum.nl/200407820`.
- **Exact per-item licence field (verbatim from the public object page)**: `Copyright: Public domain` with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`. The per-item Copyright field is recorded verbatim, not inferred from institution policy.
- **Rights / policy URL**: `https://data.rijksmuseum.nl/policy/information-and-data-policy` (Rijksmuseum two-tier policy `CC0 1.0` / `CC BY 4.0`).
- **Image / IIIF URL (Micrio IIIF Image API)**: `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded).
- **v4.4b status**: `ready-for-asset-import`.

### C-10 per-item licence result

- **Concrete item**: Rijksmuseum objectNumber **RP-F-F80313**, *Wolfsklauw*, Anna Atkins (photographer, England), c. 1854. **Distinct per-item record from C-09** (different objectNumber, different persistent URL PID, different micrioId).
- **Item URL**: `https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f`.
- **Persistent URL (id.rijksmuseum.nl PID)**: `https://id.rijksmuseum.nl/200408260`.
- **Exact per-item licence field (verbatim from the public object page)**: `Copyright: Public domain` with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`. The per-item Copyright field is recorded verbatim, not inferred from institution policy.
- **Rights / policy URL**: `https://data.rijksmuseum.nl/policy/information-and-data-policy`.
- **Image / IIIF URL (Micrio IIIF Image API)**: `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (HEAD test returned HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded).
- **IIIF Presentation API manifest note**: `https://iiif.micr.io/PrcdN/manifest.json` returned HTTP/2 404. Rijksmuseum uses Micrio IIIF Image API, not the Presentation API. The per-item public object page's Copyright field is the authoritative source for the credit line.
- **v4.4b status**: `ready-for-asset-import`.

---

## 4. Docs created

| File | Purpose |
|---|---|
| `docs/SOURCE_GAP_FIX_v4.4b.md` | Round plan + baseline + gap resolution table + updated totals + threshold decision |
| `docs/ITEM_EVIDENCE_COMPLETION_v4.4b.md` | Per-item evidence for the 6 rows (v4.4 + v4.4b), with per-row v4.4b evidence details |
| `docs/READY_FOR_ASSET_IMPORT_SHORTLIST_v4.4b.md` | Ready candidates (6 rows) + deferred or blocked candidates (0 rows) + import gate |
| `docs/ASSET_IMPORT_DECISION_LOG_v4.4b.md` | Per-row decision (6 rows) + decision totals + key constraints reaffirmed |
| `docs/ASSET_FILENAME_MAP_UPDATE_v4.4b.md` | Filename map (6 rows) with concrete identifiers + collision check |

---

## 5. Live / template / pilot no-change confirmation

| Surface | v4.4b before | v4.4b after | Diff |
|---|---|---|---|
| `site/index.html` / `site/style.css` / `site/script.js` | (v4.4 baseline) | (v4.4 baseline) | `git diff` = **empty** |
| `_template/site/` | (v4.3 baseline) | (v4.3 baseline) | `git diff` = **empty** |
| `_template/data/` | (v4.3 baseline) | (v4.3 baseline) | `git diff` = **empty** |
| `_pilots/second-exhibition-pilot/` | (v4.3 baseline) | (v4.3 baseline) | `git diff` = **empty** |
| `posts/` | (v3.4 baseline) | (v3.4 baseline) | `git diff` = **empty** |
| `case-study/` | (v3.4 baseline) | (v3.4 baseline) | `git diff` = **empty** |
| `release-assets/` | (v3.4 baseline) | (v3.4 baseline) | `git diff` = **empty** |
| `scripts/template_quality_gate.py` | (v3.4 baseline) | (v3.4 baseline) | `git diff` = **empty** |
| Live URL | 92,976 B | 92,976 B | **preserved** |
| `second-exhibition/assets/images/` | (does not exist) | (does not exist) | **not created** |

---

## 6. Tags / releases untouched

| Tag | Status |
|---|---|
| `v2.0-public-portfolio-case` | untouched |
| `v2.6-content-stable` | untouched (active stable tag) |
| `v2.7-zh-exhibition-polish` | untouched |
| `v2.8-real-deep-content` | untouched |
| `v2.9-real-source-rights-audit` | untouched |
| `v3.0-real-template-extraction-audit` | untouched |
| `v3.1-real-second-exhibition-pilot` | untouched |
| `v3.2-real-template-documentation` | untouched |
| `v3.3-real-template-quality-gate` | untouched |
| `v3.4-real-second-exhibition-hardening` | untouched (source release for v4.4 / v4.4b) |

No new tag created in v4.4b. No new GitHub Release created in v4.4b. All pre-existing tags and Releases are untouched.

---

## 7. Forbidden phrases

The following phrases were searched in every v4.4b doc and confirmed absent as a status value or decision value:

- `approved` (used as a project status) — **not used** (only appears in "not used" context)
- `safe for commercial use` — **not used**
- `cleared for all uses` — **not used**

---

## 8. Round boundary (sign-off)

v4.4b ends with:

- 5 v4.4b docs committed.
- `docs/V4_ROADMAP.md` v4.4b section committed.
- `README.md` v4.4b block committed.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- No new image files. No new image directory.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `scripts/template_quality_gate.py` is **empty**.
- `approved` not used as a status value in any v4.4b doc.
- C-03's `CC BY-NC-SA subset remains blocked`.
- C-08's `double-confirmation` result: **PASS**.
- C-09 / C-10's per-item `licence field` result: **PASS** (recorded verbatim from each public object page's Copyright field).
- No new tag, no new GitHub Release.

**Threshold decision.** `ready-for-asset-import` count = **6 ≥ 4** → the next round is **v4.5 — Asset Import** (unblocked).