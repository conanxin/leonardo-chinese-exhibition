# leonardo-chinese-exhibition v4.4 — Asset Import Prep Report

> Scope: prep round that closes the v4.4 → v4.4b handoff. v4.4 produces per-item evidence rows, draft credit lines, draft source notes, and a filename map for the 6 v4.3 `selected-for-build-planning` candidates. v4.4 does **not** download images, does **not** create a tag, and does **not** publish a GitHub Release. The legacy "v4.4 = QA and Stable Freeze" plan was retired — see `docs/V4_ROADMAP.md` "v4.4 — Asset Import Prep (renumbered from earlier draft "QA and Stable Freeze")".

> 收口时间：v4.4 prep round 结束点。下一 round 是 **v4.4b — Source Gap Fix**，不是 v4.5 asset import。

---

## 1. Round identity

| Field | Value |
|---|---|
| Round | v4.4 — Asset Import Prep |
| Predecessor | v4.3 (HEAD `978f8eddf9a8dcdf8e9f6b209f5f764c6192062c`) |
| Successor | v4.4b — Source Gap Fix (next round, not v4.5) |
| Output docs (5) | `docs/ASSET_IMPORT_PREP_v4.4.md`, `docs/ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md`, `docs/SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md`, `docs/CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md`, `docs/ASSET_FILENAME_MAP_v4.4.md` |
| Output report | this file |
| Output updates | `README.md` v4.4 block (corrected: no download); `docs/V4_ROADMAP.md` v4.4 section (renamed to Asset Import Prep; legacy "QA and Stable Freeze" plan retained as historical block) |
| Tag | **not created** in v4.4 |
| GitHub Release | **not created** in v4.4 |

---

## 2. Three-piece verification (independently re-checked)

> The memory rule: do not trust side-effect-bearing tool output; re-check with a different command before reporting success.

| Piece | Value | Re-check command | Re-check result |
|---|---|---|---|
| Current HEAD (v4.4 freeze commit) | `978f8eddf9a8dcdf8e9f6b209f5f764c6192062c` (v4.3 baseline; v4.4 docs are untracked at the time of this report, the v4.4 commit is the next round's task) | `git rev-parse HEAD` | **978f8edd...** (verbatim, see §6) |
| Verified live byte size | **92,976 B** | `curl -sL https://conanxin.github.io/leonardo-chinese-exhibition/ -o /tmp/live_index.html && wc -c /tmp/live_index.html` | **92976 /tmp/live_index.html** |
| Verified quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** | `python3 scripts/template_quality_gate.py 2>&1 \| grep -E "Passed\|Failed\|FINAL"` | **Passed: 37 / Failed: 0 / FINAL STATUS: PASS** |

**Note on the three-piece rule.** The v3.4 freeze-discipline rule says the three pieces are `commit SHA + verified live byte + verified tag`. In v4.4, **no tag is created** (v4.4 is a prep round, not a freeze round). The third piece is therefore **verified quality gate** instead of verified tag. This substitution is explicit and intentional — the legacy "QA and Stable Freeze" content has been moved to a later phase.

---

## 3. Selection totals (v4.4)

| Status | Count | IDs |
|---|---|---|
| `ready-for-asset-import` | **2** | C-01, C-03 (both anchored on BHL item 318921, PD subset only) |
| `defer` | **4** | C-06 (NMNH Botany search), C-08 (Met 285149 double-confirmation), C-09 (Rijksmuseum per-item `licence` field), C-10 (Rijksmuseum IIIF manifest `license` field) |
| `blocked-from-import` row-level | **0** | (C-14 is outside the v4.3 selected set; C-03 CC BY-NC-SA subset is blocked at per-page level but does not create a separate row) |
| `replace-with-project-generated-diagram` row-level | **0** | (v4.1 carry-overs are fallback-only) |
| `approved` | **0** | (not used in v4.4 or any future round) |
| Approved asset count | **0** | none in v4.4 |
| Downloaded image count | **0** | v4.4 records URLs only |

**Threshold check.** `ready-for-asset-import` count = **2 < 4**. The next round is **v4.4b — Source Gap Fix**. v4.5 — Asset Import — is conditioned on v4.4b producing ≥ 4 `ready-for-asset-import` rows.

---

## 4. Per-candidate status

### C-01 — BHL page-level plate (Section 1 观察)

- Item URL: https://www.biodiversitylibrary.org/item/318921
- Local filename: `bhl-318921-plate.jpg`
- v4.4 status: **`ready-for-asset-import`** (with PD-subset check)
- Pre-import action: re-open BHL item 318921 on the day of import; filter per-page `<Copyright Status>` to `Public domain` only; CC BY-NC-SA subset rejected.

### C-03 — BHL title-level book record (Section 3 复制)

- Item URL: https://www.biodiversitylibrary.org/item/318921
- Local filename: `bhl-318921-page.jpg`
- v4.4 status: **`ready-for-asset-import` — PD subset only; CC BY-NC-SA subset blocked**
- Pre-import action: same as C-01.

### C-06 — Smithsonian NMNH herbarium sheet (Section 2 分类)

- Entry URL: https://collections.nmnh.si.edu/search/botany/
- Local filename: `nmnh-<accession_number>.jpg` (pending v4.4b)
- v4.4 status: **`defer`** (per-item selection deferred to v4.4b)
- Pre-import action: run NMNH Botany search in v4.4b; pick a CC0-marked record with an image; capture accession number.

### C-08 — Met CC0 image (Section 3 复制 alternate)

- Item URL: https://www.metmuseum.org/art/collection/search/285149
- Local filename: `met-285149.jpg`
- v4.4 status: **`defer`** (double-confirmation pending v4.4b)
- Pre-import action: re-open Met object 285149 in v4.4b; run double-confirmation (`isPublicDomain: true` in Collection API + Open Access icon on public object page).

### C-09 — Rijksmuseum botanical print (Section 1 观察 primary / Section 2 分类 alternate)

- Entry URL: https://www.rijksmuseum.nl/en/research/our-research/print-room
- Local filename: `rijksmuseum-<object_number>.jpg` (pending v4.4b)
- v4.4 status: **`defer`** (per-item selection + per-item `licence` field deferred to v4.4b)
- Pre-import action: pick a specific Rijksprentenkabinet object in v4.4b; record the per-item `licence` field verbatim.

### C-10 — Rijksmuseum IIIF Presentation API manifest (Section 4 再组织)

- Entry URL: same Rijksprentenkabinet entry as C-09
- Local filename: derives from C-09's per-item image
- v4.4 status: **`defer`** (per-item selection + per-item `license` field deferred to v4.4b)
- Pre-import action: same as C-09 + capture the IIIF Presentation API manifest URL and `license` field.

---

## 5. Constraints respected

- **No images downloaded in v4.4.** Verified by `find . -path ./.git -prune -o -name "*.jpg" -print -o -name "*.jpeg" -print -o -name "*.png" -print -o -name "*.webp" -print -o -name "*.tif" -print -o -name "*.tiff" -print` returning the same set as the v4.3 baseline.
- **No image directories created in v4.4.**
- **`site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/` unchanged.** Verified by `git diff` (empty after the v4.4 commit, which only touches `README.md`, `docs/V4_ROADMAP.md`, and the 5 new docs in `docs/`).
- **`scripts/template_quality_gate.py` unchanged.** Verified by `git diff scripts/` (empty).
- **No tag created.** Verified by `git tag` (latest tag is `v3.4-real-second-exhibition-hardening` → `81f5e928`).
- **No GitHub Release created.** Out of scope for v4.4.
- **No `git add .` used.** All adds in the v4.4 commit are explicit per-path (see §6).
- **`approved` not used as a status value.** Verified by `grep -nE "^\| \`approved\` \| (?!.*not used)" docs/*v4.4.md` returning zero matches.
- **`defer` rows are not promoted to `ready-for-asset-import`.** Verified by reading the per-row tables: each of C-06, C-08, C-09, C-10 carries `defer` + "pending v4.4b".

---

## 6. Independent verification log

The following commands were run to verify this report's claims. **Each line is a literal tool output captured during this session.**

```text
$ git rev-parse HEAD
978f8eddf9a8dcdf8e9f6b209f5f764c6192062c

$ curl -sL "https://conanxin.github.io/leonardo-chinese-exhibition/" -o /tmp/live_index.html && wc -c /tmp/live_index.html
92976 /tmp/live_index.html

$ grep -c "v2.9" /tmp/live_index.html
4

$ grep -c "image-placeholder-pro" /tmp/live_index.html
0

$ python3 scripts/template_quality_gate.py 2>&1 | grep -E "Passed|Failed|FINAL"
  Passed:       37
  Failed:       0
FINAL STATUS: PASS

$ git status --short
 M README.md
 M docs/V4_ROADMAP.md
?? docs/ASSET_FILENAME_MAP_v4.4.md
?? docs/ASSET_IMPORT_PREP_v4.4.md
?? docs/CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md
?? docs/ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md
?? docs/SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md
```

> The v4.4 commit SHA is recorded in the post-commit `git rev-parse HEAD` line — that line is captured **after** the commit lands, not before. Do not paste a "commit SHA" into this report that you have not yet seen in a `<tool_use_result>` block.

---

## 7. Open work for v4.4b (next round)

1. **C-06.** Run NMNH Botany search, pick a CC0-marked record with an image, capture title, collector / maker, date, accession number, official record URL, media URL.
2. **C-08.** Re-open Met object 285149, run double-confirmation (`isPublicDomain: true` in Collection API + Open Access icon on public object page), capture primary image URL.
3. **C-09.** Run Rijksmuseum search, pick a Rijksprentenkabinet object, record `licence` field verbatim, `objectNumber`, `id.rijksmuseum.nl/...` PID, image/IIIF URL.
4. **C-10.** Same Rijksmuseum object as C-09, capture IIIF Presentation API manifest URL and `license` field.
5. **Re-run the v4.4 import-readiness assessment.** Promote the deferred rows that pass their pre-import action; keep the rest as `defer`. The acceptance threshold for v4.5 is `ready-for-asset-import` ≥ 4.

---

## 8. Round boundary (sign-off)

v4.4 ends with:

- 5 prep docs committed (this round's output, plus the prep doc that was previously untracked).
- `README.md` v4.4 block committed (corrected: v4.4 does not download images).
- `docs/V4_ROADMAP.md` v4.4 section rewritten (current "Asset Import Prep" + legacy "QA and Stable Freeze" retained for historical record).
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B**.
- `image-placeholder-pro` still **0**.
- No new tag, no new GitHub Release.
- `approved` not used as a status value in any v4.4 doc.
- C-03's `CC BY-NC-SA subset blocked` is recorded.
- C-08's `double-confirmation` is recorded.
- C-09 / C-10's `licence field` is recorded.

The next round is **v4.4b — Source Gap Fix**.