# v5.6 Second Exhibition Content Audit

> Scope: facts, terminology, narrative structure, and visitor comprehension of
> `second-exhibition/site/index.html` plus its `data/*.json` and `docs/*.md`
> companion artefacts, **as frozen at the v5.0 / v5.3 freeze**. No production
> content has been modified in this round; this document only records what was
> observed so that the v0.2 iteration plan can be built on real evidence.

## Baseline

| Field                                  | Value                                                                              |
|---|---|
| HEAD / origin/main                     | `ce01f1d8e37478c27cce7c6eb81f1c77ceb3739c`                                        |
| Stable tag (pinned)                    | `v5.0-real-second-exhibition-deployment`                                          |
| Stable tag object                      | `c8871f09e4003675d5796c76058d589a08541f45`                                        |
| Stable tag target                      | `ac0f19e2c03b09738ae49b4a15c629a1f2177068`                                        |
| Stable Release                         | not draft, not prerelease, published `2026-07-12T00:29:43Z`                       |
| Second-exhibition source HTML bytes    | `25,641`                                                                           |
| Second-exhibition source SHA-256       | `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda`               |
| Second-exhibition staged/live bytes    | `25,635`                                                                           |
| Second-exhibition staged/live SHA-256  | `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c`               |
| source→staged difference               | exactly 6 expected image-path rewrites (`../assets/images/` → `./assets/images/`) |
| Title                                  | 《植物图谱与视觉分类：从自然史图像到知识秩序》 (working title)                  |
| Subtitle                               | 从自然史图像到知识秩序                                                            |
| Stripped prose char count              | `8,755`                                                                            |
| Section count                          | `4` (观察 / 分类 / 复制 / 再组织)                                                 |
| Section deep blocks                    | `4` (one per section: visual-thinking, material-evidence × 2, research-model)     |
| Artifact card count                    | `6` (C-01, C-03, C-06, C-08, C-09, C-10)                                          |
| Glossary entries                       | `12`                                                                              |
| Public image count                     | `6` (no new images in this round)                                                 |
| Status phrase counts (live)            | `production-deployed-v5.3` = 5 · `published-in-v5.3` = 8 · `imported-not-deployed` = 8 · `repository-only-not-deployed` = 0 |
| Asset publication / import status      | current = `published-in-v5.3` · historical = `imported-not-deployed`              |
| Image checksum integrity               | `6/6 OK`                                                                          |
| Schema / gate / healthcheck            | schema 2.0 · template PASS · build PASS · repo-QA 164/164 · healthcheck PASS · browser QA 5/5 |
| `second-exhibition/site/index.html` modified in this round | NO (read-only audit)                                                  |

## No-change declaration

This document, its companion planning docs, and the v0.2 implementation
documents **do not modify** any of the following:

- `site/` (root)
- `second-exhibition/site/`
- `second-exhibition/data/`
- `second-exhibition/assets/`
- `second-exhibition/docs/` (only read for audit)
- `.github/workflows/`
- `scripts/`
- `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`
- The 6 image files (`bhl-318921-page-603998-c01.webp`,
  `bhl-318921-page-603962-c03.webp`,
  `smithsonian-nmnh-1529703.png`, `met-285149.jpg`,
  `rijksmuseum-rp-f-f80152.jpg`, `rijksmuseum-rp-f-f80313.jpg`)
- `second-exhibition/assets/asset-import-manifest.json` and
  `asset-checksums.sha256`
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` and
  `RIGHTS_AND_SOURCES.md`

## Strengths

These are the parts of the current v0.1 exhibition that v0.2 should
**preserve** rather than replace:

1. **Status phrase integrity.** Counts `5 / 8 / 8 / 0`
   (`production-deployed-v5.3` / `published-in-v5.3` /
   `imported-not-deployed` / `repository-only-not-deployed`) match the
   spec. All four counts are documented and tool-enforced by the
   build-gate and the production healthcheck.
2. **Candidate-ID consistency.** All six `C-NN` IDs are referenced in
   `site/index.html`, `data/assets.json`, `data/sections.json`,
   `docs/SOURCE_AUDIT_MANIFEST.md`, and `docs/RIGHTS_AND_SOURCES.md`.
   Section IDs (`section-1-observation` … `section-4-reorganization`)
   are mirrored between `data/sections.json` and the rendered HTML
   headings.
3. **Caveat calls.** The page (via `data/assets.json` and
   `docs/SOURCE_AUDIT_MANIFEST.md`) correctly flags:
   - **C-03** PD subset only — CC BY-NC-SA sibling pages of the same
     BHL item are blocked.
   - **C-06** NMNH 90×90 thumbnail, `low_resolution: true`,
     `lightbox_enabled: false`.
   - **C-08** Met double-confirmation (API `isPublicDomain: true` +
     public page Public Domain indicator).
   - **C-10** Rijksmuseum IIIF Presentation API manifest `/manifest.json`
     HTTP 404; manifest-based statements must not be made.
4. **Mixed Chinese + English strategy.** Titles use a Chinese primary
   and English secondary; identifiers and credit lines use the
   institution's native form. This protects bilingual visitors and
   the institution's archival convention.
5. **Section ordering.** Observation → Classification → Reproduction →
   Reorganization forms a real progression: from the act of seeing
   (selection judgment) → the institution's name-giving act →
   reproduction technology → digital reorganization. This sequence
   is the correct scaffolding for the thesis and must survive
   v0.2.
6. **Existing fact / interpretation labelling.** CURATORIAL_ESSAY_ZH
   distinguishes "事实", "策展假设", "可研究方向" — the data-model
   for source-boundary hygiene is already in place.
7. **One asset per section except Section 4.** Section 4 lists all
   six C-IDs to make the "reorganization" thesis legible without
   adding new images.

## Issues

Each row links to a position in the current rendering of the page or
data file. **Severity** is scoped to *content quality* and *factual
risk*, not to *build* or *deployment*: no row blocks CI today.

| ID      | File / section                          | Current text or issue                                                                 | Type                  | Severity | Evidence (path / line context)                                                                                       | Proposed direction                                                                                                                                              |
|---------|-----------------------------------------|----------------------------------------------------------------------------------------|-----------------------|----------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I-01    | `data/glossary.json` → `glossary-herbarium.definition` | "保存植物标本的机构及其空间…NMNH Botany 与 Rijksprentenkabinet **都属于此类机构**。" | factual               | **high** | `second-exhibition/data/glossary.json` `glossary-herbarium.definition`                                              | Rijksprentenkabinet is the Rijksmuseum's print room (works on paper), not a herbarium. Move it out of this entry; either split glossary, or note "NMNH belongs" only. |
| I-02    | `data/glossary.json` → `glossary-print` | Lumps "雕版、蚀刻、石印、蓝晒 cyanotype" together as the same print medium.            | terminology           | medium   | `data/glossary.json` `glossary-print.definition`                                                                    | Add explicit disambiguation: cyanotype = a photographic photogram process, **not** a hand-pulled print. Existing wording is defensible but loose.                |
| I-03    | `data/glossary.json` (missing entries)  | No glossary entry for "cyanotype" or "photogram".                                        | terminology           | medium   | entire `data/glossary.json`                                                                                        | Add `glossary-cyanotype` and `glossary-photogram` (proposed v0.2 glossary count: 12 → 14).                                                                          |
| I-04    | `data/glossary.json` → `glossary-iiif`  | "包含 Image API … 和 Presentation API … Presentation API manifest 在 C-10 上返回 404。" | technical statement   | low      | `data/glossary.json` `glossary-iiif.definition`                                                                     | Tighten wording: distinguish *Image API* (single image, sized/regioned tiles) from *Presentation API* (manifest describing works and canvases), and explicitly state that the 404 only applies to C-10. |
| I-05    | `data/glossary.json` → `glossary-public-domain` | "版权已过期或因机构主动放弃而进入公共使用的状态。CC0 1.0 是常见的公共领域贡献许可。…" | source-boundary       | medium   | `data/glossary.json` `glossary-public-domain.definition`                                                            | Call out that **Public Domain (PD) is a legal status; CC0 is a license instrument**, and an institution's per-item Public Domain label is *not* the same as a CC0 dedication. Use C-08 (Met, double-confirmed) and C-09/C-10 (Rijksmuseum, per-item Public domain + CC0 link) as anchor examples. |
| I-06    | `data/sections.json` → `section-1-observation.body` / `data/glossary.json` → `glossary-specimen` | Section 1 talks about 18—19 c. watercolours but the term "标本 / specimen" is only used in the glossary, not foregrounded in Section 1 where the visual contrast would benefit. | narrative             | medium   | `data/sections.json` `section-1-observation.body`; `data/glossary.json` `glossary-specimen`                         | Foreground in Section 1 that watercolour-on-paper is **not** a herbarium specimen and therefore the visual evidence (drawing) and the institutional specimen belong to *different* registers. |
| I-07    | `data/sections.json` → `section-2-classification.body` | "NMNH Botany 馆藏的 Aconitum bulbilliferum 与大都会博物馆的 Botanical Specimen: Fern 为对照样本" — bundles specimens under one label. | terminology           | medium   | `data/sections.json` `section-2-classification.body`                                                                | Disambiguate: NMNH C-06 is a herbarium specimen (image of specimen); Met C-08 is a curated object (photograph of a botanical specimen). The institutional categories are different. |
| I-08    | `data/sections.json` → `section-3-reproduction.body` | "Rijksmuseum Rijksprentenkabinet 收藏的 Anna Atkins 蓝晒 cyanotype" — used as anchor for cyanotype explanation, but Anna Atkins's photographed objects (ferns, mosses) are *not* herbarium specimens in the NMNH sense. | terminology / visitor comprehension | medium | `data/sections.json` `section-3-reproduction.body`                                                                  | Make explicit that Rijksprentenkabinet is a print room, the cyanotype is a photographic *photogram* (a contact print from the object itself), and the institutional register is "works on paper", not "herbarium". |
| I-09    | `data/sections.json` → `section-4-reorganization.body` | "稳定的 identifier、可校验的元数据、可机器读取的 rights 字段" — currently abstract.   | narrative / visitor comprehension | medium | `data/sections.json` `section-4-reorganization.body`                                                                | Anchor concretely: show how C-06's EZID arK resolves to the NMNH record, how C-09's `RP-F-F80152` + persistent URL resolves back to the public page, and how C-10's missing `/manifest.json` makes manifest-based claims unavailable. |
| I-10    | `site/index.html` Hero region           | Hero (1,331 B) carries 3 status strings + URL — competes with the lead question for the visitor's eye. | accessibility / visitor comprehension | medium | `site/index.html` (hero region before first h2)                                                                       | Move the status-block to footer / sidebar; hero should carry the core question only.                                                                                |
| I-11    | `site/index.html` Artifact cards        | Six cards each repeat "credit line + source note + identifier + institution".         | visitor comprehension | medium   | `site/index.html` artifact-card markup                                                                              | Aggregate credit/source into a single line under the image, or move into modal; keep viewing note as the primary lead.                                            |
| I-12    | `site/index.html` Section "资产卡片 / Artifact Cards" | Appears *after* all 4 sections; narrative arc reaches reorganization before images are summarized. | narrative             | low      | `site/index.html` ordering                                                                                          | Optional — keep current order, or move "Asset Cards" block into Section 4's vicinity.                                                                            |
| I-13    | `data/glossary.json` → `glossary-plate` | Defines "图版 / Plate" but lists `BHL C-01, C-03` as examples without explaining that a BHL "page" is one rendering layer of a single "item". | metadata             | low      | `data/glossary.json` `glossary-plate.definition`                                                                     | Note that BHL item 318921 contains many pages; C-01 and C-03 are two distinct pages of the same item.                                                              |
| I-14    | `data/exhibition.json` → `forbidden_statuses_not_used` | Field exists; gate enforces it.                                                        | source-boundary       | low      | `data/exhibition.json`                                                                                              | Strengthen the gate to also assert *positive* status counts (`production-deployed-v5.3 ≥ 1`, etc.), not only negative.                                            |
| I-15    | Site copy repetition                    | "再看一眼" / "观察"  appear in body of Section 1 and the deep-block prompt.            | repetition            | low      | `data/sections.json` `section-1-observation.body` + `deep_block_prompt`                                            | Vary the verbs in the deep-block prompt to avoid reading like a restatement.                                                                                       |

> Severity legend (content-only):
> - **blocker** — fact is wrong or violates source-boundary in a way that cannot coexist with the v5.3 caveat rules. (none currently.)
> - **high** — likely factual error exposed to visitors. (I-01.)
> - **medium** — terminology looseness / narrative overlap that
>   reduces visitor comprehension.
> - **low** — wording polish, no visitor risk.

## Section-by-section assessment

### Hero / 3-minute guide (HTML h1, h2 "3 分钟导览")

- **Hero text reads**: subtitle + 3 status phrases + URL + 6-status
  enumeration, packed into 1,331 B. This is structurally a *status
  block*, not a *lead question*. The thesis of the exhibition is
  stated in the surrounding copy, but the hero is dominated by
  machine-checked metadata.
- **3-minute guide** is a 5-stop "visitor action" list. It tells
  visitors *what to do* but not *what to look for*. Strong for
  accessibility, weak for shaping interpretation.

### Section 1 · 观察 / Observation (`section-1-observation`)

- **Assets**: C-01 (BHL watercolour, page 603998).
- **Strengths**: clearly differentiates watercolour-on-paper from
  digitisation outcome; uses "保留什么、舍弃什么" (selection
  judgment) as the rubric.
- **Issues**: section talks about specimens and watercolours but does
  not explicitly mark the gap between the two — watercolour-on-paper
  is a *drawn representation*, not a herbarium specimen. Glossary
  entry `glossary-specimen` makes the disambiguation but the body
  text does not surface it. (See I-06.)

### Section 2 · 分类 / Classification (`section-2-classification`)

- **Assets**: C-06 (NMNH Botany specimen), C-08 (Met botanical
  specimen photograph).
- **Strengths**: contrast between an institutional herbarium specimen
  (NMNH) and an institutional object record (Met) is the right axis.
- **Issues**: the section bundles them as "对照样本"; the
  institutional registers — *herbarium* vs. *object record* — should
  be named. C-06's `low_resolution: true` and the fact that the
  Asset is a 90×90 thumbnail should be foregrounded in the body, not
  only in the data file. (See I-07.)

### Section 3 · 复制 / Reproduction (`section-3-reproduction`)

- **Assets**: C-03 (BHL watercolour, page 603962 — PD-subset),
  C-09 (Rijksmuseum Zeestreepvaren cyanotype), C-10 (Rijksmuseum
  Wolfsklauw cyanotype with manifest 404 caveat).
- **Strengths**: third act is anchored by reproduction technology,
  which is exactly the right progression; the IIIF Image API →
  Presentation API distinction is implicitly invoked by the
  manifest-404 caveat.
- **Issues**: the glossary conflates "print" and "cyanotype" in a way
  the body text does not correct. The "Rijksprentenkabinet 收藏的
  Anna Atkins 蓝晒" wording in the body does not cue the visitor
  that *Rijksprentenkabinet is a print room, not an herbarium*. (See
  I-08.)

### Section 4 · 再组织 / Reorganization (`section-4-reorganization`)

- **Assets**: C-01, C-03, C-06, C-08, C-09, C-10 (all six).
- **Strengths**: deliberately returns to every asset to demonstrate
  the *network effect*; uses `viewer_action` to point at
  `BUILD_ASSET_USAGE.md`.
- **Issues**: the body is the most abstract of the four sections.
  Adding concrete examples — identifier resolution paths, what
  fields are *stable* across visits, what fields break (C-10's
  missing `/manifest.json`) — would make the section legible to a
  non-specialist. (See I-09.)

### Artifact cards (`site/index.html`, `data/assets.json`)

- Six cards, 1 per asset. Currently carries: `title` · `alt` ·
  `caption` · `viewing_note` · `credit_line` · `source_note` ·
  `identifier` · `institution`. The credit + source + identifier
  triplet accounts for 50–60 % of the card height. (See I-11.)

### Glossary (`data/glossary.json`)

- 12 entries; identification-vocabulary term → definition → section
  hint. Strong baseline. **Real issue**: I-01 (Rijksprentenkabinet
  in `glossary-herbarium`), I-02 (`glossary-print` lumping), and
  I-05 (PD vs. CC0 distinction) are content-quality defects. (See
  also I-03, I-04, I-13.)

### Deep blocks (`site/index.html` h3, four `deep_block_*` entries)

- Per-section: visual-thinking (S1), material-evidence (S2, S3),
  research-model (S4). The labelling is internally consistent
  (`deep_block_type` matches the rendered h3 string). Content
  quality is good but two of the prompts re-use "如果你只能" prefix
  (I-15).

### Source / rights entry (`site/index.html` h2 "来源与版权")

- Aggregated source-note / credit-line / status listing for all
  six assets. Maintains the v5.3 controlled-deployment status
  phrases. Strong institutional hygiene.

### Footer / status block (`site/index.html` footer region)

- 1,108 B block. Holds the deployment-status text. Status phrase
  counts are *correct*; this is currently where the status block
  belongs. The pressure the hero currently carries should be moved
  here.

## Recommendation

> **Recommendation: v0.2 may proceed**, with the following
> preconditions:

1. The single **high-severity** finding (I-01, Rijksprentenkabinet
   ≠ herbarium) **must be fixed in v0.2**.
2. The **medium-severity** findings (I-02 / I-03 / I-05 / I-06 /
   I-07 / I-08 / I-09 / I-10 / I-11) should be fixed in v0.2 if the
   implementation slot allows, otherwise split into v0.2a (factual /
   terminology blockers) and v0.2b (narrative / accessibility).
3. The **low-severity** findings (I-12 / I-13 / I-14 / I-15) are
   optional, queued for a future iteration; they do not block v0.2.
4. The **section structure, status model, asset roster, and image
   files must remain unchanged in v0.2.**
5. The **next action is v0.2 implementation, gated by the changeset
   draft and the acceptance criteria documents**.

A precise per-file / per-section proposed-change grid is in
[`docs/SECOND_EXHIBITION_CONTENT_CHANGESET_DRAFT_v5.6.md`](SECOND_EXHIBITION_CONTENT_CHANGESET_DRAFT_v5.6.md).
A fact-by-fact verification matrix is in
[`docs/SECOND_EXHIBITION_FACT_CHECK_MATRIX_v5.6.md`](SECOND_EXHIBITION_FACT_CHECK_MATRIX_v5.6.md).
