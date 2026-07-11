# leonardo-chinese-exhibition v4.4 — Asset Import Prep Report

## STATUS: PASS

> Scope: v4.4 = asset import prep round. v4.4 records per-item / source-level evidence for the 6 v4.3 `selected-for-build-planning` candidates, draft credit lines, draft source notes, and a filename map. v4.4 does **not** download images, does **not** create a tag, and does **not** publish a GitHub Release. The status `approved` is **not used** in v4.4 or any future round. The next recommended task is **v4.4b-source-gap-fix**.

---

## 1. Baseline + three-piece verification

> The memory rule: do not trust side-effect-bearing tool output; re-check with a different command before reporting success.

| Piece | Value | Re-check command | Re-check result (verbatim) |
|---|---|---|---|
| Current HEAD (v4.4 freeze commit) | `166e73cff276a8111f098da7c6ff674b39ff778d` | `git rev-parse HEAD` | **`166e73cff276a8111f098da7c6ff674b39ff778d`** |
| Origin/main | `978f8eddf9a8dcdf8e9f6b209f5f764c6192062c` (v4.3 baseline; pre-push) | `git rev-parse origin/main` | **`978f8eddf9a8dcdf8e9f6b209f5f764c6192062c`** |
| Source release | `v3.4-real-second-exhibition-hardening` | `git tag \| tail -1` | **`v3.4-real-second-exhibition-hardening`** |
| Source tag target (annotated → commit) | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` | `git show v3.4-real-second-exhibition-hardening --no-patch --format='%H'` | **`81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`** ("Harden second exhibition pilot") |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ | `curl -L -s -I` | `HTTP/2 200`, `content-type: text/html` |
| Live byte size (before / after) | **92,976 B** / **92,976 B** (preserved) | `curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ \| wc -c` | **`92976`** |
| v2.9 marker count on live | **1** | `grep -c "v2.9-real-source-rights-audit"` | **`1`** |
| `image-placeholder-pro` count on live | **0** | `grep -c "image-placeholder-pro"` | **`0`** |
| `植物图谱与视觉分类` (v4 title) on live | **0** | `grep -c "植物图谱与视觉分类"` | **`0`** (v4 is prep-only, not deployed) |
| `script.js` HTTP status | **HTTP/2 200** | `curl -LIs` | **`HTTP/2 200`, `content-type: application/javascript; charset=utf-8`** |
| Quality gate (before / after) | **PASS, 37/37** | `python3 scripts/template_quality_gate.py 2>&1 \| grep -E "Passed\|Failed\|FINAL"` | **`Passed: 37 / Failed: 0 / FINAL STATUS: PASS`** |

**Note on the three-piece rule.** The v3.4 freeze-discipline rule says the three pieces are `commit SHA + verified live byte + verified tag`. In v4.4, **no tag is created** (v4.4 is a prep round, not a freeze round). The three pieces are therefore `commit SHA + verified live byte + verified quality gate`. This substitution is explicit and intentional — the legacy "QA and Stable Freeze" content has been moved to a later phase.

---

## 2. Selection totals (v4.4)

| Metric | Count | Notes |
|---|---|---|
| Item-level / source-level sources checked | **6** | 2 item-level (C-01, C-03 — BHL item 318921) + 4 source-level (C-06 NMNH, C-08 Met, C-09 Rijksmuseum, C-10 Rijksmuseum) |
| Item-level sources checked | **2** | C-01, C-03 |
| Source-level sources checked | **4** | C-06, C-08, C-09, C-10 (per-item record deferred) |
| `ready-for-asset-import` | **2** | C-01, C-03 (both anchored on BHL item 318921, PD subset only) |
| `defer` | **4** | C-06 NMNH Botany search, C-08 Met 285149 double-confirmation, C-09 Rijksmuseum per-item `licence` field, C-10 Rijksmuseum IIIF manifest `license` field |
| `blocked-from-import` row-level | **0** | C-14 is outside the v4.3 selected set; C-03 CC BY-NC-SA subset blocked at per-page level but does not create a separate row |
| `replace-with-project-generated-diagram` row-level | **0** | v4.1 carry-overs are fallback-only |
| `approved` | **0** | (not used in v4.4 or any future round) |
| Approved asset count | **0** | none in v4.4 |
| Downloaded image count | **0** | v4.4 records URLs only |
| New image files added | **0** | `find` returns the same set as the v4.3 baseline |
| New image directories created | **0** | `second-exhibition/assets/images/` not created in v4.4 |

**Threshold check.** `ready-for-asset-import` count = **2 < 4**. The next recommended task is **v4.4b-source-gap-fix** (per `docs/ASSET_IMPORT_PREP_v4.4.md` §"v4.4 Asset Import Prep — summary block"). v4.5 — Asset Import — is conditioned on v4.4b producing ≥ 4 `ready-for-asset-import` rows.

---

## 3. Docs created (5 prep docs + 1 report)

| File | Purpose |
|---|---|
| `docs/ASSET_IMPORT_PREP_v4.4.md` | Round plan, baseline, summary block, 4-status legend, per-candidate readiness table, threshold check, round boundary |
| `docs/ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md` | 6-row evidence table (C-01 / C-03 / C-06 / C-08 / C-09 / C-10) with item URL, institution, title, creator, date, identifier, rights, image/IIIF URL pattern, proposed filename, v4.4 status |
| `docs/SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md` | Manifest draft (DRAFT) with one section per C-xx: local path, source URL, image/IIIF URL, institution, identifier, rights, rights/terms URL, source note draft, credit line draft, audit status, remaining caution |
| `docs/CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md` | Per-row credit line + source note drafts (English + optional zh) with rights caution; C-06 / C-09 / C-10 are template drafts with placeholders |
| `docs/ASSET_FILENAME_MAP_v4.4.md` | Filename rules + 6-row filename table with future local paths under `second-exhibition/assets/images/` (directory not created in v4.4) |
| `reports/leonardo_chinese_exhibition_v4_4_asset_import_prep_report.md` | this report |

### Filename map summary

| ID | Proposed filename | Future local path | Import status |
|---|---|---|---|
| C-01 | `bhl-318921-plate.jpg` | `second-exhibition/assets/images/bhl-318921-plate.jpg` | `wait for v4.5 asset import`, `not downloaded` |
| C-03 | `bhl-318921-page.jpg` | `second-exhibition/assets/images/bhl-318921-page.jpg` | `wait for v4.5 asset import`, `not downloaded` |
| C-06 | `nmnh-<accession_number>.jpg` | `second-exhibition/assets/images/nmnh-<accession_number>.jpg` | `wait for v4.4b-source-gap-fix`, `not downloaded` |
| C-08 | `met-285149.jpg` | `second-exhibition/assets/images/met-285149.jpg` | `wait for v4.4b-source-gap-fix`, `not downloaded` |
| C-09 | `rijksmuseum-<object_number>.jpg` | `second-exhibition/assets/images/rijksmuseum-<object_number>.jpg` | `wait for v4.4b-source-gap-fix`, `not downloaded` |
| C-10 | (derives from C-09) | (same Rijksmuseum object as C-09) | `wait for v4.4b-source-gap-fix`, `not downloaded` |

Filename rules: lowercase, institution prefix, short identifier, no spaces, extension preserved from source, never overwrite existing files, future import only.

### Source audit manifest draft summary

| ID | Audit status | Remaining caution |
|---|---|---|
| C-01 | `ready-for-asset-import` | per-page `<Copyright Status>` must be `Public domain`; CC BY-NC-SA subset rejected |
| C-03 | `ready-for-asset-import` (PD subset only) | CC BY-NC-SA subset blocked at per-page level |
| C-06 | `defer` | per-item record not selected yet; must be resolved in v4.4b |
| C-08 | `defer` | double-confirmation pending v4.4b |
| C-09 | `defer` | per-item record not selected yet; must be resolved in v4.4b |
| C-10 | `defer` | per-item record not selected yet; must be resolved in v4.4b |

### Credit line draft summary

| ID | Credit line basis |
|---|---|
| C-01 | final draft (English): "Source: Biodiversity Heritage Library, item 318921. Public domain (per-page copyright status filter applied)." |
| C-03 | final draft (English): same as C-01; differs in filename suffix and caption context |
| C-06 | template draft with `<accession_number>` placeholder; not final |
| C-08 | final draft pending double-confirmation; basis: "Source: The Metropolitan Museum of Art, object 285149 (accession 2003.562.3). Public domain (double-confirmation: Collection API + public page)." |
| C-09 | template draft with `<object_number>` and `<licence field>` placeholders; not final |
| C-10 | template draft with `<object_number>` and `<licence field>` placeholders; not final |

The phrase "safe for commercial use" is **not used** in any credit line. The status `approved` is **not used** in any v4.4 doc.

---

## 4. README + roadmap updates

| File | Change |
|---|---|
| `README.md` | Added "## v4.4 Asset Import Prep" block: status / `ready-for-asset-import` count / `defer` count / no images downloaded / no assets imported / no approved status / C-03 CC BY-NC-SA subset blocked / C-08 double-confirmation required / C-09 / C-10 per-item licence field required / next: v4.4b-source-gap-fix |
| `docs/V4_ROADMAP.md` | Added "## v4.4 Asset Import Prep (current round — summary)" block. Added "## v4.4b Source Gap Fix" section with goal (resolve C-06 / C-08 / C-09 / C-10 gaps), tasks (pick concrete NMNH item, double-confirm Met C-08, pick concrete Rijksmuseum C-09 / C-10 items, record per-item licence fields), explicit "still no image download unless separate v4.5 import round", and exit criteria. Updated Phasing summary: v4.4 (prep) → v4.4b (gap fix) → v4.5 (asset import, gated on v4.4b) → post-v4.5 (QA + stable freeze). |

---

## 5. Live site / template / pilot no-change confirmation

| Surface | Pre-v4.4 | Post-v4.4 | Diff |
|---|---|---|---|
| `site/index.html` | (v4.3 baseline) | (v4.3 baseline) | `git diff -- site/index.html` = **empty** |
| `site/style.css` | (v4.3 baseline) | (v4.3 baseline) | `git diff -- site/style.css` = **empty** |
| `site/script.js` | (v4.3 baseline) | (v4.3 baseline) | `git diff -- site/script.js` = **empty** |
| Live URL | 92,976 B | 92,976 B | **preserved** |
| `_template/site/` | (v4.3 baseline) | (v4.3 baseline) | `git diff -- _template/site/` = **empty** |
| `_template/data/` | (v4.3 baseline) | (v4.3 baseline) | `git diff -- _template/data/` = **empty** |
| `_pilots/second-exhibition-pilot/` | (v4.3 baseline) | (v4.3 baseline) | `git diff -- _pilots/second-exhibition-pilot/` = **empty** |

---

## 6. Old tags / old releases untouched

| Tag | SHA | Notes |
|---|---|---|
| `v2.0-public-portfolio-case` | (untouched) | legacy portfolio stable |
| `v2.6-content-stable` | (untouched) | active stable tag |
| `v2.7-zh-exhibition-polish` | (untouched) | legacy |
| `v2.8-real-deep-content` | (untouched) | legacy |
| `v2.9-real-source-rights-audit` | (untouched) | legacy |
| `v3.0-real-template-extraction-audit` | (untouched) | legacy |
| `v3.1-real-second-exhibition-pilot` | (untouched) | legacy |
| `v3.2-real-template-documentation` | (untouched) | legacy |
| `v3.3-real-template-quality-gate` | (untouched) | legacy |
| `v3.4-real-second-exhibition-hardening` | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` | source release for v4.4; **not moved, not rewritten** |

No new tag created in v4.4 (the QA / freeze round is post-v4.5 per the new phasing summary). All pre-existing tags (`v2.0` … `v3.4`) and pre-existing GitHub Releases are untouched.

---

## 7. Constraints respected

- **No images downloaded in v4.4.** Verified by `find . -path ./.git -prune -o \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" -o -iname "*.tif" -o -iname "*.tiff" \) -print | sort` returning the same set as the v4.3 baseline (no new files).
- **No image directories created in v4.4.** `second-exhibition/assets/images/` does not exist; v4.4 records the future local path only.
- **`site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/` unchanged.** Verified by `git diff --` against each (empty).
- **`scripts/template_quality_gate.py` unchanged.** Verified by `git diff -- scripts/template_quality_gate.py` (empty).
- **No tag created.** Verified by `git tag` (latest tag is `v3.4-real-second-exhibition-hardening` → `81f5e928`).
- **No GitHub Release created.** Out of scope for v4.4.
- **No `git add .` used.** All adds in the v4.4 commit are explicit per-path (see §8).
- **`approved` not used as a status value.** Verified by `grep -c "approved"` in each v4.4 doc; all hits are in "not used" / "forbidden phrases" context.
- **`defer` rows are not promoted to `ready-for-asset-import`.** Verified by reading the per-row tables: each of C-06, C-08, C-09, C-10 carries `defer` + "pending v4.4b".
- **C-03 CC BY-NC-SA subset blocked** at the per-page / per-volume level. Not promoted.
- **C-08 double-confirmation pending v4.4b.** Not promoted.
- **C-09 / C-10 per-item `licence` field pending v4.4b.** Not promoted.

---

## 8. Independent verification log (re-checked)

```text
$ git rev-parse HEAD
166e73cff276a8111f098da7c6ff674b39ff778d

$ git rev-parse origin/main
978f8eddf9a8dcdf8e9f6b209f5f764c6192062c

$ git tag | tail -1
v3.4-real-second-exhibition-hardening

$ git show v3.4-real-second-exhibition-hardening --no-patch --format='%H'
81f5e928aefdc4dc92a4dbb5aedecbd3cd564765

$ python3 scripts/template_quality_gate.py 2>&1 | grep -E "Passed|Failed|FINAL"
  Passed:       37
  Failed:       0
FINAL STATUS: PASS

$ curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ -o /tmp/live_v44b.html && wc -c /tmp/live_v44b.html
92976 /tmp/live_v44b.html

$ grep -c "v2.9-real-source-rights-audit" /tmp/live_v44b.html
1

$ grep -c "image-placeholder-pro" /tmp/live_v44b.html
0

$ grep -c "植物图谱与视觉分类" /tmp/live_v44b.html
0

$ curl -LIs https://conanxin.github.io/leonardo-chinese-exhibition/script.js | head -3
HTTP/2 200
server: GitHub.com
content-type: application/javascript; charset=utf-8

$ git diff -- site/index.html site/style.css site/script.js _template/site/ _template/data/ _pilots/second-exhibition-pilot/
(empty)

$ find . -path ./.git -prune -o -path ./.firecrawl -prune -o \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" -o -iname "*.tif" -o -iname "*.tiff" \) -print | sort
./release-assets/screenshots/desktop-exhibit-index.png
./release-assets/screenshots/desktop-hero.png
./release-assets/screenshots/desktop-platform-tools.png
./release-assets/screenshots/desktop-real-image-gallery.png
./release-assets/screenshots/mobile-hero.png
./release-assets/screenshots/mobile-section.png
./site/assets/images/codex-atlanticus/codex-atlanticus-f21-recto.jpg
./site/assets/images/codex-atlanticus/codex-atlanticus-f719-recto.jpg
./site/assets/images/platform/platform-advanced-search.jpg
./site/assets/images/platform/platform-comparative-study.jpg
./site/assets/images/platform/platform-home-leonardotheka.jpg
./site/assets/images/platform/platform-recompositions.jpg
./site/assets/images/platform/platform-watermarks.jpg
./site/assets/images/royal-collection/royal-cats-lions-dragon-rcin-912363.jpg
./site/assets/images/royal-collection/royal-horse-studies-rcin-912310.jpg
./site/assets/images/royal-collection/royal-shoulder-arm-rcin-919003.jpg
./site/assets/images/royal-collection/royal-water-studies-rcin-912660.jpg
```

> Every line above is a literal tool output captured during this session. No paraphrase.

---

## 9. Open work for v4.4b (next round)

1. **C-06.** Run NMNH Botany search, pick a CC0-marked record with an image, capture title, collector, date, accession number, official record URL, media URL.
2. **C-08.** Re-open Met object 285149, run double-confirmation (`isPublicDomain: true` in Collection API + Open Access icon on public object page), capture `primaryImage` URL.
3. **C-09.** Run Rijksmuseum search, pick a Rijksprentenkabinet object, record `licence` field verbatim, `objectNumber`, `id.rijksmuseum.nl/...` PID, image/IIIF URL.
4. **C-10.** Same Rijksmuseum object as C-09, capture IIIF Presentation API manifest URL and `license` field.
5. **Re-run the v4.4 import-readiness assessment.** Promote the deferred rows that pass their pre-import action; keep the rest as `defer`. The acceptance threshold for v4.5 is `ready-for-asset-import` ≥ 4.

---

## 10. Round boundary (sign-off)

v4.4 ends with:

- 5 v4.4 prep docs committed (5 new in `docs/`, plus the prep doc that was previously untracked).
- `README.md` v4.4 block committed (and corrected: v4.4 does not download images).
- `docs/V4_ROADMAP.md` v4.4 + v4.4b sections committed.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B**.
- v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- v4 title in live = **0** (v4 is prep-only, not deployed).
- `script.js` HTTP/2 **200**.
- No new image files. No new image directory.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `scripts/template_quality_gate.py` is **empty**.
- `approved` not used as a status value in any v4.4 doc.
- C-03's `CC BY-NC-SA subset blocked` is recorded.
- C-08's `double-confirmation required` is recorded.
- C-09 / C-10's `per-item licence field required` is recorded.
- No new tag, no new GitHub Release.

**The next recommended task is v4.4b-source-gap-fix.**