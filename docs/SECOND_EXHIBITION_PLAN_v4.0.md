# v4.0 Real Second Exhibition Plan

> Status: **Planning only — no deployment, no image import, no live change.**
> Scope of this document: decide the theme, source boundaries, rights posture, minimum viable content structure, and execution roadmap for the next real second exhibition (the one *after* the hardening of the pilot in v3.4).
> This document does **not** deploy a new exhibition, does **not** create a tag or GitHub Release, and does **not** modify `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, or `release-assets/`.

---

## Planning baseline

| Field | Value |
|---|---|
| Current HEAD | `14444d06d84e341f16332585daa52001e9704ea5` |
| `origin/main` | `14444d06d84e341f16332585daa52001e9704ea5` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| v3.4 tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| v3.4 tag target (hardening commit) | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | `https://conanxin.github.io/leonardo-chinese-exhibition/` |
| Live byte size (baseline) | **92,976 B** |
| Live v2.9 marker | `v2.9-real-source-rights-audit = 1` (must stay) |
| Live `image-placeholder-pro` count | `0` (must stay) |
| Live pilot title ("一件作品的旅程") count | `0` (must stay — pilot is repository-only) |
| `script.js` HTTP status | `200` |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37 checks** |
| Pilot path | `_pilots/second-exhibition-pilot/` (repository-only, not deployed) |

---

## Goal

The goal of v4.0 is **not** to ship a second exhibition. It is to decide, **before any download or page edit**, the following:

1. What is the next real exhibition's **theme**?
2. What is its **core visitor question**?
3. Which **source types** are eligible, and which are not?
4. Which **institutions** are plausible candidates (for research, not yet for download)?
5. What is the **minimum viable content** that satisfies the v3.4 hardening rules?
6. What is the **explicit non-goal** list for v4.0 itself?

A real second exhibition only becomes buildable after these six decisions are written down, accepted, and reflected in the source-scope, rights-risk-register, and content-outline planning docs that accompany this plan.

---

## Candidate exhibition directions

Three directions were considered. Each is scored on five axes: source availability, rights clarity, thematic distance from Leonardo, template reusability signal, and content difficulty.

### Direction A — 手稿与机器想象：从图解到自动化

- **Working title**: 《手稿与机器想象：从图解到自动化》
- **Core question**: How did the figure — drawn by hand, then traced by machine — change from a record of observation into a record of computation?
- **Why it suits this template**: Strong thematic continuity with Leonardo (manuscript page → plate analogy maps onto the existing `artifact_card` structure).
- **Likely source set**: Digitized codex pages, modern textbook figures, AI-lab blog figures, software screenshots.
- **Rights risk**: **High.** Codex scans often have unclear or restrictive terms; AI-generated or edited images frequently lack rights statements; software screenshots are platform-ambiguous.
- **Content difficulty**: **Medium–high.** Requires careful separation of "diagram" (own work, cite) from "page scan" (third-party, often restricted).
- **Recommendation**: **Deprioritize for v4.0** — rights surface is too large to lock down before a build is even started.

### Direction B — 博物馆里的知识网络：一件藏品如何连接人、机构与目录

- **Working title**: 《博物馆里的知识网络：一件藏品如何连接人、机构与目录》
- **Core question**: How does a single object become a node that links people, institutions, and catalog records across decades?
- **Why it suits this template**: Excellent fit for `deep_reading` / `research_model` / `material_evidence` markers — the pilot already proved these slots work.
- **Likely source set**: Museum collection records (object pages, IIIF manifests), curator essays, finding aids.
- **Rights risk**: **Medium–high.** Records themselves are usually public, but most object *images* are institution-controlled; some allow IIIF reuse, many do not.
- **Content difficulty**: **High.** Heavy reliance on a single object's chain of custody — risky if that object's image cannot be cleared.
- **Recommendation**: **Deprioritize for v4.0** — too object-dependent; rights are decided one object at a time, which fights the planning-first rule.

### Direction C — 植物图谱与视觉分类：从自然史图像到知识秩序

- **Working title**: 《植物图谱与视觉分类：从自然史图像到知识秩序》
- **Core question**: How does a plant image travel from observation to taxonomy, teaching, collection, and public knowledge?
- **Why it suits this template**: Visual-material driven, taxonomy-rich, plate-friendly. Maps cleanly onto `botanical plate` / `herbarium sheet` / `digitized book page` artifact types.
- **Likely source set**: Public-domain botanical illustration, open-access herbarium sheets, digitized natural-history books, institution-provided IIIF.
- **Rights risk**: **Low–medium.** Natural-history illustrations are heavily public-domain; open-access herbaria (BHL, Wellcome, Smithsonian Open Access, Met, Rijksmuseum, LoC) publish clear rights statements.
- **Content difficulty**: **Medium.** Topic is deep but well-documented; clear plate vs. sheet vs. book-page separation.
- **Recommendation**: **PRIMARY direction for v4.0.**

---

## Recommended direction

**《植物图谱与视觉分类：从自然史图像到知识秩序》**

Reasons (in priority order):

1. **Strong public-domain / open-access surface.** Natural-history illustrations and herbarium sheets are over-represented in clearly-licensed open collections. This makes the v3.4 source-and-rights hardening testable *and* survivable.
2. **Thematic distance from Leonardo is large.** A botanical / taxonomy theme visibly exercises the template's cross-topic portability — which is the whole point of having a template at all.
3. **Visual artifact types are clear.** `botanical plate`, `herbarium sheet`, `digitized book page`, `collection record screenshot`, `project-generated comparison diagram` — five distinct, well-bounded shapes.
4. **Source / rights audit boundary is easier to control.** Each candidate can be checked against a fixed list of six institutions and a fixed rights taxonomy. No AI-generated or software-screenshot ambiguity required.
5. **Pedagogical clarity.** The narrative arc "observe → name → reproduce → recombine" maps onto the template's `deep_reading` / `visual_thinking` / `research_model` markers without forcing them.

---

## Minimum viable exhibition (MVE)

A real second exhibition must contain, at minimum:

| Slot | Count | Notes |
|---|---|---|
| Sections | 4 | Observe / Classify / Reproduce / Reorganize |
| Artifact cards | 4–6 | One per section minimum; one or two sections may carry two |
| Glossary terms | 6–10 | At least 10 candidates are listed in the outline doc |
| Curatorial essay | 1 | Single long-form piece, written *after* source audit passes |
| Source audit manifest | 1 | One row per asset; see source-scope doc for required fields |
| Rights note | 1 | Aggregate rights posture + per-asset credit lines |
| Release report | 1 | Live byte + tag + commit SHA three-piece evidence |
| Local render QA | 1 run | `template_quality_gate.py` PASS required |
| Deployment gate | **not before** source audit | Source audit must clear High / Blocked items first |

The MVE is intentionally *narrow*. The goal is to prove the v3.4 hardening generalizes to a non-Leonardo topic without expanding the surface area past what the source-scope and rights-register docs can defend.

---

## Non-goals for v4.0

v4.0 explicitly does **not**:

- Deploy a new exhibition.
- Create or modify any live page (`site/index.html`, `site/style.css`, `site/script.js`).
- Modify `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/`.
- Modify `scripts/template_quality_gate.py`.
- Download, import, transcribe, or restyle any real collection image.
- Replace any image currently served by the live site.
- Process or remove the untracked `.firecrawl/` directory (left alone this round).
- Create a tag or GitHub Release for v4.0.
- Move, retag, rewrite, or delete any existing tag (`v2.0` through `v3.4`).
- Modify any existing GitHub Release.

v4.0 is a **planning round**. The first build round is v4.3, and even v4.3 is gated by v4.1 source-candidate research and v4.2 rights audit.

---

## Companion documents in v4.0

| File | Purpose |
|---|---|
| `docs/SECOND_EXHIBITION_PLAN_v4.0.md` | This file — theme + MVE + non-goals |
| `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md` | Preferred source types + candidate institutions + required metadata per asset |
| `docs/SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md` | Risk levels + known risk categories + register table + release blocker rule |
| `docs/SECOND_EXHIBITION_CONTENT_OUTLINE_v4.0.md` | Working title + sections + artifact types + glossary candidates + writing tasks |
| `docs/V4_ROADMAP.md` | v4.0 → v4.4 phased plan with explicit do-not-do entries |

---

## Source tag for this round

This round does **not** create a tag. The source release referenced above is `v3.4-real-second-exhibition-hardening` and is the most recent stable anchor.

---

## Acceptance criteria for v4.0 closure

v4.0 is considered closed when **all** of the following are true:

1. The five planning docs above exist and are committed.
2. `README.md` records the v4.0 plan block.
3. `python3 scripts/template_quality_gate.py` → **PASS, 37/37**.
4. `git diff` against `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/` is **empty** for this round.
5. Live byte size is **still 92,976 B**, v2.9 marker is **still 1**, `image-placeholder-pro` count is **still 0**, pilot title in live is **still 0**.
6. No new tag, no new GitHub Release, no movement of old tags, no edit of old releases.
7. `reports/leonardo_chinese_exhibition_v4_0_real_second_exhibition_plan_report.md` exists and is committed.