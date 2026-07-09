# v4.0 Real Second Exhibition Plan — Report

> Round: **v4.0 Real Second Exhibition Plan**
> Date: 2026-07-09 (UTC)
> Working title: 《植物图谱与视觉分类：从自然史图像到知识秩序》
> **STATUS: PASS**

---

## 1. Round summary

| Field | Value |
|---|---|
| **STATUS** | **PASS** |
| Round | v4.0 — Real Second Exhibition Plan |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Source tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Baseline HEAD | `14444d06d84e341f16332585daa52001e9704ea5` |
| `origin/main` at round start | `14444d06d84e341f16332585daa52001e9704ea5` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (before) | 92,976 B |
| Live byte size (after) | 92,976 B |
| Live byte size delta | **0 B** |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v2.9 marker in live | `1` (unchanged) |
| `image-placeholder-pro` in live | `0` (unchanged) |
| `植物图谱与视觉分类` in live | `0` (unchanged — planning round, not deployed) |
| `script.js` HTTP status | `200` |
| Working tree | clean except for untracked `.firecrawl/` (left alone this round, per scope) |
| New tag | **none** (v4.0 is a planning round) |
| New GitHub Release | **none** |

---

## 2. Reality gate result (round start)

| Check | Expected | Actual | Result |
|---|---|---|---|
| HEAD = `origin/main` | `14444d0` | `14444d0` | PASS |
| v3.4 tag object | `2d186a89` | `2d186a89` | PASS |
| v3.4 tag target | `81f5e92` | `81f5e92` | PASS |
| Quality gate | 37/37 PASS | 37/37 PASS | PASS |
| Live byte size | 92,976 B | 92,976 B | PASS |
| v2.9 marker in live | 1 | 1 | PASS |
| `image-placeholder-pro` in live | 0 | 0 | PASS |
| Pilot title in live (`一件作品的旅程`) | 0 | 0 | PASS |
| `script.js` HTTP status | 200 | 200 | PASS |
| Working tree | clean (untracked `.firecrawl/` ok) | matches | PASS |

Reality gate **PASS**. Round proceeded.

---

## 3. Planning docs created

| File | Bytes | Purpose |
|---|---|---|
| `docs/SECOND_EXHIBITION_PLAN_v4.0.md` | ~10.4 KB | Theme + MVE + non-goals + planning baseline |
| `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md` | ~7.5 KB | Preferred source types + candidate institutions + required metadata per asset + source acceptance rule |
| `docs/SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md` | ~6.1 KB | Risk levels + known risk categories + register table + release blocker rule |
| `docs/SECOND_EXHIBITION_CONTENT_OUTLINE_v4.0.md` | ~9.6 KB | Working title + 4 sections + artifact types + 10 glossary candidates + writing tasks |
| `docs/V4_ROADMAP.md` | ~8.3 KB | v4.0 → v4.4 phased plan with explicit do-not-do entries |
| `README.md` | updated | New `v4.0 Real Second Exhibition Plan` block injected after v3.4 section |

Grep verification of acceptance phrases:

| Check | Count |
|---|---|
| `植物图谱与视觉分类` in `SECOND_EXHIBITION_PLAN_v4.0.md` | 3 |
| `High / Blocked` in `SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md` | 3 |
| `Biodiversity Heritage Library` in `SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md` | 2 |

All 5 v4.0 planning docs exist; the source-scope doc lists **6 candidate institutions** (BHL, Wellcome, Smithsonian Open Access, The Met Open Access, Rijksmuseum, Library of Congress); the rights-risk register defines **4 risk levels** and **8+ known risk categories** with a release-blocker rule that **High / Blocked assets cannot enter a stable release unless resolved or excluded**.

---

## 4. Recommended direction

**Working title:** 《植物图谱与视觉分类：从自然史图像到知识秩序》

**Core visitor question:** 一张植物图像如何从观察记录，变成分类、教学、收藏和公共知识的一部分？

**Why this direction (vs. the two deprioritized directions):**

1. Strong public-domain / open-access surface — natural-history illustrations and herbarium sheets are heavily represented in clearly-licensed open collections (BHL, Wellcome, Smithsonian Open Access, The Met Open Access, Rijksmuseum, LoC).
2. Thematic distance from Leonardo is large — clearly exercises the template's cross-topic portability.
3. Visual artifact types are clean — `botanical plate` / `herbarium sheet` / `digitized book page` / `collection record screenshot` / `project-generated comparison diagram` — five distinct, well-bounded shapes.
4. Source / rights audit boundary is easier to control — each candidate can be checked against a fixed list of institutions and a fixed rights taxonomy. No AI-generated or software-screenshot ambiguity required.
5. Pedagogical clarity — the narrative arc "observe → name → reproduce → recombine" maps cleanly onto the template's `deep_reading` / `visual_thinking` / `research_model` markers.

The two deprioritized directions (A: 手稿与机器想象 / B: 博物馆里的知识网络) are recorded in the plan doc with their respective rights-risk and content-difficulty reasons for *not* being chosen for v4.0.

---

## 5. Source scope summary

`docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md` fixes:

- **5 preferred source types** (open access museum collections, public domain botanical illustrations, digitized books with clear rights statements, institution-provided IIIF images if rights allow, project-generated diagrams).
- **6 candidate institutions** (BHL, Wellcome, Smithsonian Open Access, The Met Open Access, Rijksmuseum, Library of Congress). v4.0 only enumerates them; **no contact, no crawl, no download**.
- **14 required metadata fields per asset** (title, creator, date, institution, collection URL, image URL, rights statement, identifier, local file path, alt text, caption, source note, credit line, audit status).
- **5-point source acceptance rule** (URL reachable; rights statement locatable; credit line composable; source note reconstructable; not a search-result or memory import).

---

## 6. Rights risk register status

`docs/SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md` fixes:

- **4 risk levels:** Low / Medium / High / Blocked.
- **8+ known risk categories** (public-domain status unclear; institution terms restrict reuse; platform screenshot ambiguity; missing image URL; missing object identifier; derivative diagram not clearly labeled; AI-generated or edited image unclear; no credit line; no source note).
- **Register table schema** (ID / Asset / Risk category / Risk level / Evidence / Decision / Follow-up owner / Status). The table is *empty* in v4.0 — there are no candidate assets yet; v4.1 populates candidate rows, v4.2 promotes or downgrades them.
- **Release blocker rule:** *High / Blocked risk items cannot enter a stable release unless resolved or excluded.* Three escape paths: resolve / exclude / defer. No fourth path.

---

## 7. Content outline status

`docs/SECOND_EXHIBITION_CONTENT_OUTLINE_v4.0.md` fixes:

- **Working title** and **core visitor question** (above).
- **4 sections** with purpose / artifact types / visitor takeaway / source requirements / rights notes for each:
  1. 观察：图像如何抓住植物特征
  2. 分类：图像如何服务命名与秩序
  3. 复制：书籍、版画与数字化如何改变传播
  4. 再组织：数字馆藏如何让图像重新连接
- **5 artifact types** enumerated (no real images imported).
- **10 glossary candidates** (botanical illustration, taxonomy, herbarium, specimen, plate, engraving, digitization, metadata, collection record, public domain).
- **9 writing tasks** enumerated (hero, 3-minute guide, 4× section body, 4–6 artifact card captions, source notes, credit lines, glossary, curatorial essay, rights notes).

---

## 8. README update

`README.md` updated with a new `## v4.0 Real Second Exhibition Plan` block, placed immediately after the `## v3.4 Real Second Exhibition Hardening` section. The block records:

- Status: planning only
- Recommended direction: 《植物图谱与视觉分类》
- Source release / tag / baseline HEAD / live byte size
- "No live changes / No deployment / No images imported"
- Pilot remains repository-only
- Quality gate 37/37
- Old tags and old GitHub Releases untouched
- No new tag, no new GitHub Release
- Links to all 5 planning docs and the report
- Next recommended task: v4.1 — Source Candidate Research

No prior v2.x / v3.x section was modified.

---

## 9. Live site no-change confirmation

| Check | Before | After | Delta |
|---|---|---|---|
| Live byte size | 92,976 B | 92,976 B | 0 |
| v2.9 marker in live | 1 | 1 | 0 |
| `image-placeholder-pro` in live | 0 | 0 | 0 |
| `植物图谱与视觉分类` in live | 0 | 0 | 0 (planning round, not deployed) |
| `script.js` HTTP status | 200 | 200 | — |
| `git diff -- site/index.html site/style.css site/script.js` | — | empty | — |

Live site **unchanged**.

---

## 10. Template / pilot no-change confirmation

| Check | Result |
|---|---|
| `git diff -- _template/site/` | empty |
| `git diff -- _template/data/` | empty |
| `git diff -- _pilots/second-exhibition-pilot/` | empty |
| `scripts/template_quality_gate.py` | PASS 37/37 |

Template and pilot **unchanged**.

---

## 11. Old tags / old releases untouched

| Check | Result |
|---|---|
| `git tag --list` | v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1 / v3.2 / v3.3 / v3.4 — **all 10 unchanged** |
| `git ls-remote --tags origin` | matches local list — no remote-side movement |
| v3.4 tag object | `2d186a89` (unchanged) |
| v3.4 tag target | `81f5e92` (unchanged) |
| Old GitHub Releases | **none modified** (no `gh release edit` issued; only the v3.4 Release already exists from prior round) |
| `posts/` | not touched (not in this round's allowed-edit list) |
| `case-study/` | not touched (not in this round's allowed-edit list) |
| `release-assets/` | not touched (not in this round's allowed-edit list) |

No tag, no Release, no movement, no rewrite. Old history **untouched**.

---

## 12. Files changed in this round

Allowed-edit list (per round scope) — all changed files fall inside this list:

| File | Action |
|---|---|
| `docs/SECOND_EXHIBITION_PLAN_v4.0.md` | created |
| `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md` | created |
| `docs/SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md` | created |
| `docs/SECOND_EXHIBITION_CONTENT_OUTLINE_v4.0.md` | created |
| `docs/V4_ROADMAP.md` | created |
| `README.md` | modified (v4.0 block added) |
| `reports/leonardo_chinese_exhibition_v4_0_real_second_exhibition_plan_report.md` | created (this file) |

Untracked `.firecrawl/` directory was observed at round start and **left alone**, per round scope.

---

## 13. Next recommended task

**v4.1 — Source Candidate Research.**

Scope of v4.1:

- Research each of the 6 candidate institutions at the collection / search-page level (not the individual asset level).
- For each candidate institution: record overall rights posture, API or IIIF availability, per-item rights-metadata field, identifier persistence.
- Identify candidate assets (not yet downloaded): one per section, plus one alternate per section.
- For each candidate asset, record: title, creator, date, institution, collection URL, image URL (if reachable without download), rights statement (or "not exposed"), identifier, source note, audit status = `pending`.
- Update the risk register rows from `pending` to a level when enough evidence exists.

v4.1 **must not**:

- Download or import any image file into the working tree.
- Write into `site/`.
- Start the template instantiation.
- Create a tag or GitHub Release.
- Move or rewrite any pre-existing tag or GitHub Release.
- Modify `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/`.

v4.1 **must** keep the live byte size at 92,976 B and the v2.9 marker at 1.

---

## 14. Final status

**STATUS: PASS**

All reality-gate, planning-doc, source-scope, rights-register, content-outline, README, quality-gate, no-change, and old-history conditions met. v4.0 closes with five committed planning docs, one updated README, one committed report, an unchanged live site (92,976 B / v2.9 marker = 1 / placeholder = 0), an unchanged template and pilot, and ten untouched old tags plus their corresponding old GitHub Releases. No new tag, no new GitHub Release was created. The next round is v4.1 — Source Candidate Research.