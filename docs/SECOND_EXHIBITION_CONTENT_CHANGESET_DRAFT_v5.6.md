# v5.6 Second Exhibition Content Changeset Draft

> Per-file, per-section, per-field draft of every proposed v0.2 edit.
> "Current state" is byte-locked to HEAD `ce01f1d…` (the v0.1
> freeze). "Proposed state" is *what will land in v0.2 subject to
> operator `IMPLEMENT v5.6b` directive*. Each row also names the
> effect on Page / Source SHA / Staged-Live SHA / Browser QA / Gate
> QA / Asset checksums.

> **Field convention**: every `"Impact"` sub-row answers
> `Does this change affect …` with **YES** (will change) or **NO**
> (unchanged).

## Files allowed for modification in v0.2

| Path                                                          | In allowlist? |
|---|:---:|
| `second-exhibition/site/index.html`                           | YES (named rows only) |
| `second-exhibition/data/exhibition.json`                      | YES (single field) |
| `second-exhibition/data/sections.json`                        | YES (named fields only) |
| `second-exhibition/data/glossary.json`                        | YES (named fields only) |
| `second-exhibition/data/assets.json`                          | YES (named fields only) |
| `second-exhibition/docs/VISITOR_GUIDE_ZH.md`                  | YES (light edits) |
| `second-exhibition/docs/CURATORIAL_ESSAY_ZH.md`               | YES (light edits) |
| `second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md`            | YES (no new sections; minor wording) |
| `second-exhibition/docs/BUILD_ASSET_USAGE.md`                 | YES (caveat refresh only) |
| `README.md`                                                   | YES (one new section) |
| `docs/V5_ROADMAP.md`                                          | YES (one new section) |
| `reports/leonardo_chinese_exhibition_v5_6_…_report.md`        | YES (new file) |
| `second-exhibition/assets/images/*` (6 images)                | **NO** |
| `second-exhibition/assets/asset-import-manifest.json`         | **NO** |
| `second-exhibition/assets/asset-checksums.sha256`             | **NO** |
| `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`             | **NO** |
| `second-exhibition/docs/RIGHTS_AND_SOURCES.md`                | **NO** |
| `site/` (root site)                                           | **NO** |
| `.github/workflows/`                                          | **NO** |
| `scripts/`                                                    | **NO** |
| `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/` | **NO** |
| Old tags / old Releases                                       | **NO** |

## CHG-01 — `data/glossary.json` `glossary-herbarium` definition

> **Blocker. Required by F-17 / I-01.**

| Field          | Value |
|---|---|
| File           | `second-exhibition/data/glossary.json` |
| JSON path      | `items[?id=='glossary-herbarium'].definition` |
| Section        | (no `section_hint` change; remain `section-2-classification`) |
| **Current**    | "保存植物标本的机构及其空间，通常隶属于自然史博物馆或大学。NMNH Botany 与 Rijksprentenkabinet 都属于此类机构。" |
| **Proposed**   | "保存植物标本的机构及其空间，通常隶属于自然史博物馆或大学。本展览中，NMNH Botany（C-06）属于此类机构；Rijksprentenkabinet（C-09 / C-10）是 Rijksmuseum 的版画／素描／摄影作品部门（print room），不保存植物标本。" |
| Reason         | F-17 / I-01: Rijksprentenkabinet is a print room, not a herbarium. Misattribution is high-severity factual error. |
| Evidence       | Rijksmuseum public collection page structure (department attribution on `RP-F-F80152`, `RP-F-F80313`); F-30 in fact-check matrix. |
| Risk           | Low — wording only; data-file only. |

**Impact:**

- Page byte: NO (data file; rendered JSON file path `data/glossary.json` is loaded by JS — same byte count possible if length similar, but JSON IS fetched as `second-exhibition/data/glossary.json` and a longer string will change its byte count. Public artifact file count: NO; per-file byte: **YES**, by ~30 B.)
- Source SHA: NO (`second-exhibition/site/index.html` not touched in this row).
- Staged/Live SHA: NO (staging builder does not rewrite `data/*.json`).
- Browser QA expectation: NO (JSON content not asserted; only HTML titles, headings, and IDs are).
- Gate expectation: NO (no schema field changes).
- Asset checksums: NO (6 images, 2 manifest files unchanged).
- Source/rights evidence principle: NO (`SOURCE_AUDIT_MANIFEST.md` and `RIGHTS_AND_SOURCES.md` unchanged).

## CHG-02 — Section 1 body disambiguation

> **Recommended. Word / phrase level only.**

| Field        | Value |
|---|---|
| File         | `second-exhibition/data/sections.json` |
| JSON path    | `sections[?id=='section-1-observation'].body` |
| Section      | section-1-observation |
| **Current**  | "观察是植物图谱的起点。当画家、博物学家或摄影师面对一株活体或一份标本，他们需要做出选择：哪些特征值得记录？哪些细节会因为印刷或数字化而丢失？本节以两份 BHL《Album of watercolors of Asian fruits and flowers》中的页面为引子，观察 18—19 世纪的水彩如何把花的轮廓、叶的脉络、果的质感固定为可被反复观看的图像。" |
| **Proposed** | "观察是植物图谱的起点。当画家、博物学家或摄影师面对一株活体或一份标本，他们需要做出选择：哪些特征值得记录？哪些细节会因为印刷或数字化而丢失？本节以 BHL《Album of watercolors of Asian fruits and flowers》的两份水彩图版（C-01 / C-03）为引子。需要说明的是：水彩图版是对真实标本的视觉再现，本身并不是标本；而 Rijksprentenkabinet 收藏的 Anna Atkins 蓝晒作品（C-09 / C-10）属于把植物本身作为底片晒出的摄影印刷（photogram），与水彩图版在媒介上也有区别。" |
| Reason       | I-06 / F-22: foreground the gap between watercolour-on-paper (drawn) and specimen (preserved physical); Section 1 currently elides the distinction. |
| Evidence     | F-13, F-22. |
| Risk         | Low — phrase-level only. |

**Impact:** identical to CHG-01 (data file byte changes; no HTML/source/asset change).

## CHG-03 — Section 2 body disambiguation

> **Recommended.**

| Field        | Value |
|---|---|
| File         | `second-exhibition/data/sections.json` |
| JSON path    | `sections[?id=='section-2-classification'].body` |
| **Current**  | "分类让图像有了位置。每一份植物标本背后都对应一个学名、一段采集信息和一份机构记录。本节以 Smithsonian NMNH Botany 馆藏的 Aconitum bulbilliferum 与大都会博物馆的 Botanical Specimen: Fern 为对照样本，观察图像如何从被观察的对象变成被命名的对象。NMNH 提供的低分辨率缩略图与 Met 提供的相对完整的 JPEG 也在提醒我们：…" |
| **Proposed** | "分类让图像有了位置。每一份植物标本背后都对应一个学名、一段采集信息和一份机构记录。本节以 Smithsonian NMNH Botany 馆藏的 Aconitum bulbilliferum 标本记录（C-06）与大都会博物馆的 Botanical Specimen: Fern 馆藏条目（C-08）为对照样本。两者都属于机构性植物记录，但并不属于同一类别：C-06 是压制并保存的真实植物标本（herbarium specimen）的低分辨率缩略图；C-08 是对一份 1855–60 年的植物标本照片（已为机构收藏对象）的更完整数字派生。换言之，前者让我们看到"什么样的植物对应一个学名"，后者让我们看到"机构如何让一份 19 世纪的标本照片获得数字身份"。NMNH 提供的 90×90 缩略图与 Met 提供的相对完整的 JPEG 也在提醒我们：…" |
| Reason       | I-07 / F-27: NMNH C-06 = herbarium specimen (image of specimen); Met C-08 = institutional object record of a botanical specimen photograph. Different institutional categories. |
| Evidence     | F-06, F-09, F-27. |
| Risk         | Low. |

**Impact:** data-file only; identical to CHG-01.

## CHG-04 — Section 3 body disambiguation

> **Recommended.**

| Field        | Value |
|---|---|
| File         | `second-exhibition/data/sections.json` |
| JSON path    | `sections[?id=='section-3-reproduction'].body` |
| **Current**  | "从手稿到印刷，从印刷到扫描，从扫描到 IIIF，复制技术决定了图像能否走出书房、走出博物馆、走出图书馆。本节以 Rijksmuseum Rijksprentenkabinet 收藏的 Anna Atkins 蓝晒 cyanotype 图像为引子，讨论 19 世纪的摄影/蓝晒印刷与今天的 IIIF Image API 在复制语义上的连续性与断裂。两件 Rijksmuseum 作品分别通过 Micri…" |
| **Proposed** | "从手稿到印刷，从印刷到扫描，从扫描到 IIIF，复制技术决定了图像能否走出书房、走出博物馆、走出图书馆。本节展示四种复制媒介之间的关系：本展览中 C-01 / C-03 是手工绘制的水彩图版，C-08 是机构对 19 世纪标本照片的更完整数字派生，C-09 / C-10 是 Rijksmuseum Rijksprentenkabinet（版画／素描／摄影部门，区别于植物标本馆）馆藏的 Anna Atkins 蓝晒摄影印刷（cyanotype photogram），二者均通过 Micrio IIIF Image API 在 1024px 上派生后下载；C-10 的 IIIF Presentation API /manifest.json 在本轮 v5.3 deployment 中返回 HTTP 404，因此 *不* 基于 manifest 撰写任何陈述。19 世纪的接触印相与今天的 IIIF Image API 之间既有复制语义上的连续性（都是分层、区域可取的图像派生），也有根本性断裂（前者是模拟光化学反应，后者是数字端点）。" |
| Reason       | I-08 / F-13: distinguish Rijksprentenkabinet (print room) from herbarium; cyanotype as photogram. |
| Evidence     | F-13, F-15, F-24. |
| Risk         | Low. |

**Impact:** data-file only.

## CHG-05 — Section 4 body concrete examples

> **Recommended.**

| Field        | Value |
|---|---|
| File         | `second-exhibition/data/sections.json` |
| JSON path    | `sections[?id=='section-4-reorganization'].body` |
| **Current**  | "再组织是本展览的尾声，也是数字馆藏时代最大的可能：当图像有了稳定的 identifier、可校验的元数据、可机器读取的 rights 字段，它们就不再是孤立的艺术品，而可以与其它图像重新连接。本节不展示新图像，而是把前 3 节出现的 6 件资产放回一张使用图谱，让观者看见：哪些字段是稳定的（identifier、source URL、rights URL），哪些字段是脆弱的（90×90 的缩略图、…）" |
| **Proposed** | "再组织是本展览的尾声，也是数字馆藏时代最大的可能：当图像有了稳定的 identifier、可校验的元数据、可机器读取的 rights 字段，它们就不再是孤立的艺术品，而可以与其它图像重新连接。本节不展示新图像，而是把前 3 节出现的 6 件资产放回一张使用图谱，让观者看见：identifier 让我们能回头找到原页面（C-06 的 EZID arK、C-08 的 accession 2003.562.3、C-09 / C-10 的 objectNumber）；rights 字段让我们能在不同的使用场景下复用（C-08 通过 Met Collection API `isPublicDomain: true` 与公共页面 Public Domain 指示做了双重确认；C-09 / C-10 的每件 Rijksmuseum 公开页面都标注为 Public domain 并附带 CC0 1.0 链接）；IIIF 让机器可以按尺寸、按区域、按格式请求图像派生（C-09 / C-10 通过 Micrio IIIF Image API 在 1024px 上派生后下载，C-10 的 Presentation API /manifest.json 在 v5.3 deployment 中返回 HTTP 404——这就让"基于 manifest 的证据"变成不可使用）。哪些字段是稳定的（identifier、source URL、rights URL），哪些字段是脆弱的（90×90 的缩略图、media 端点是否仍然 200、manifest 是否可达），必须被诚实地标注，不能被静默使用。" |
| Reason       | I-09 / F-26: pair each abstract noun with a concrete example; the section is the most abstract of the four. |
| Evidence     | F-09, F-10, F-11, F-12, F-14, F-16, F-26. |
| Risk         | Low. |

**Impact:** data-file only.

## CHG-06 — `data/glossary.json` `glossary-print` definition

> **Recommended. Cross-references CHG-01.**

| Field         | Value |
|---|---|
| File          | `second-exhibition/data/glossary.json` |
| JSON path     | `items[?id=='glossary-print'].definition` |
| **Current**   | "通过雕版、蚀刻、石印、蓝晒 cyanotype 等复制工艺制作的图像。Anna Atkins 的 Rijksmuseum 作品属于此类。" |
| **Proposed**  | "通过雕版、蚀刻、石印等非摄影复制工艺制作的图像。Anna Atkins 的 Rijksmuseum 蓝晒作品（C-09 / C-10）属于 cyanotype（请见 `glossary-cyanotype`）——一种以植物本身为底片的摄影接触印相，与传统手雕版画在媒介上不同；它在"复制"维度上仍属于本条目的扩展含义，但应在术语上单独标注。" |
| Reason        | F-18 / I-02: cyanotype is a photographic photogram; the prose now points visitors to the new `glossary-cyanotype` entry (see CHG-12). |
| Evidence      | F-13, F-18. |
| Risk          | Low — wording only. |

**Impact:** data-file only.

## CHG-07 — `data/glossary.json` `glossary-public-domain` definition

> **Recommended.**

| Field         | Value |
|---|---|
| File          | `second-exhibition/data/glossary.json` |
| JSON path     | `items[?id=='glossary-public-domain'].definition` |
| **Current**   | "版权已过期或因机构主动放弃而进入公共使用的状态。CC0 1.0 是常见的公共领域贡献许可。本展览的 6 件资产都基于公共领域或 CC0 1.0。" |
| **Proposed**  | "**公共领域 (Public Domain, PD) 是一种法律状态**：版权已过期，或机构在司法允许的范围内主动放弃对其作品的专有使用权。**CC0 1.0 是一种法律工具**：由机构通过 Creative Commons 主动以"不保留权利"的方式贡献作品。两者并不完全等价——一件被机构标为 Public Domain 的对象可能并没有正式的 CC0 文件，反之亦然。本展览的实例：C-08 通过 Met Collection API `isPublicDomain: true` 与公共页面 Public Domain 指示做了**双重确认**；C-09 / C-10 的 Rijksmuseum 公开页面上每件作品都标注为 Public domain 并附带 CC0 1.0 链接；C-06 的 NMNH Botany 记录以数据集级 CC0 1.0 发布。" |
| Reason        | F-19 / I-05: distinguish PD as legal status from CC0 as license instrument; anchor each version with a concrete example. |
| Evidence      | F-08, F-10, F-12, F-16. |
| Risk          | Low. |

**Impact:** data-file only.

## CHG-08 — `data/glossary.json` `glossary-iiif` definition

> **Recommended.**

| Field         | Value |
|---|---|
| File          | `second-exhibition/data/glossary.json` |
| JSON path     | `items[?id=='glossary-iiif'].definition` |
| **Current**   | "International Image Interoperability Framework。包含 Image API（按尺寸/区域派生图像）和 Presentation API（提供 manifest，描述图像的结构化元数据）。本展览使用 IIIF Image API 下载图像；Presentation API manifest 在 C-10 上返回 404。" |
| **Proposed**  | "International Image Interoperability Framework。三个常用 API：**(a) Image API**——按尺寸、区域、旋转、格式派生单张图像的位图（如 C-09 / C-10 通过 Micrio IIIF Image API 在 1024px 上派生下载）；**(b) Presentation API**——以 manifest（JSON / JSON-LD）描述一个作品、一个清单或一组图像的结构化元数据（轮次、画布、标签、归属）；**(c) Authentication API**——用于受控访问，本展览不使用。本展览仅依赖 Image API；C-10 的 Presentation API manifest /manifest.json 在 v5.3 deployment 中返回 HTTP 404，因此本展览不基于 Presentation API manifest 撰写任何陈述。" |
| Reason        | I-04 / F-20 / F-21: surface the API distinction explicitly; scope the 404 caveat to C-10 only. |
| Evidence      | F-15, F-20, F-21. |
| Risk          | Low. |

**Impact:** data-file only.

## CHG-09 — Hero status-block relocation

> **Recommended.**

| Field      | Value |
|---|---|
| File       | `second-exhibition/site/index.html` |
| Section    | Hero region (between h1 and first h2 "3 分钟导览"), plus a new home for the status phrases inside the existing footer/source-block region. |
| **Current**| Hero region (1,331 B) carries: subtitle, three status phrases, deployment URL, and the v5.3 controlled-deployment enumeration. |
| **Proposed**| Hero region carries: subtitle + the v0.2 thesis framing sentence (~1 sentence). Three status phrases + URL are relocated to the page footer / source-block, retaining their exact byte content but no longer in the hero. |
| Reason     | I-10: hero should carry the core question, not status boilerplate. |
| Evidence   | Hero-region audit in `SECOND_EXHIBITION_CONTENT_AUDIT_v5.6.md`. |
| Risk       | Medium — touches the page directly. Must verify that the four status-phrase counts (5 / 8 / 8 / 0) do not change. |

**Impact:**

- Page byte: **YES** (one paragraph moves; total page byte may shrink by 200–400 B).
- Source SHA: **YES** (page byte changes).
- Staged / Live SHA: **YES** (staging builder does not rewrite `site/index.html` byte-identically here, but the staged root index is byte-identical to the source root — and the second-exhibition staged / live depends on the actual `site/index.html` content vs. `second-exhibition/site/index.html` content separately. This row only affects `site/index.html`, so it changes the staged root SHA. **This is THE only changeset row that affects the production freeze hash. Any v0.2 commit MUST be reviewed against the production-drift gate.**)
- Browser QA expectation: NO (no candidate-id or shape assertion changes; only hero layout).
- Gate expectation: NO (source HTML byte changes; gate reads source vs. staged, both still byte-identical for the root).
- Asset checksums: NO.
- Source/rights: NO.
- Workflow: NO.

## CHG-10 — 3-minute guide viewing-method framing

> **Recommended.**

| Field       | Value |
|---|---|
| File        | `second-exhibition/site/index.html` |
| Section     | the h2 block labelled `3 分钟导览`. |
| **Current** | 5-step "visitor action" list. |
| **Proposed**| Reframe lead sentence from "what to do" to "what to look for". Keep the 5 steps, anchor each to a viewing method (水彩 vs. 标本 vs. 蓝晒 vs. 馆藏条目 vs. 元数据网络). |
| Reason      | I-10 follow-on: align the 3-min guide with the new hero framing. |
| Evidence    | I-10, I-15. |
| Risk        | Low — wording only. |

**Impact:**

- Page byte: YES (sentence-level edit).
- Source SHA: YES.
- Staged / Live SHA: YES.
- Browser QA expectation: NO (5-step count preserved).
- Gate expectation: NO.
- Asset checksums: NO.

## CHG-11 — `data/sections.json` deep-block prompt variation (optional)

> **Optional. If no design budget, defer to v0.3.**

| Field         | Value |
|---|---|
| File          | `second-exhibition/data/sections.json` |
| JSON path     | `sections[?id in ('section-1-observation','section-3-reproduction')].deep_block_prompt` |
| **Current**   | Section 1 prompt begins "如果你只能…"; Section 3 prompt begins "如果你只能…". |
| **Proposed**  | Re-phrase one of the two so they no longer share a leading phrase. (E.g. Section 3 prompt becomes "在 C-01 / C-03 / C-08 / C-09 / C-10 之间，你最舍不得丢失的是哪一类复制？— 手工绘制、机构拍照、cyanotype 接触印相，还是 IIIF 派生？") |
| Reason        | I-15. |
| Evidence      | Section block taxonomy. |
| Risk          | Low. |

**Impact:** data-file only.

## CHG-12 — `data/glossary.json` add `glossary-cyanotype` + `glossary-photogram`

> **Recommended (glossary count 12 → 14).**

| Field         | Value |
|---|---|
| File          | `second-exhibition/data/glossary.json` |
| JSON path     | `items[?id in ('glossary-cyanotype','glossary-photogram')]` (currently absent) |
| **Current**   | (entries do not exist) |
| **Proposed**  | **glossary-cyanotype** term: "蓝晒 / Cyanotype"; alias_zh: ["蓝晒法"]; definition: "一种 19 世纪的摄影复制工艺：将物体直接放在涂有感光药剂的纸上曝光，被涂面随光照发生蓝色化学反应而形成图像。Anna Atkins 的蕨类植物图谱（C-09 / C-10）即属于 cyanotype。cyanotype 与雕版／石印等印刷的最大区别在于它本质是接触印相的摄影结果。" section_hint: `section-3-reproduction`. **glossary-photogram** term: "接触印相 / Photogram"; alias_zh: ["物影成像"]; definition: "将物体本身作为底片直接放在感光材料上曝光所得的摄影图像——不需要相机。蓝晒 cyanotype（C-09 / C-10）即一种典型的 photogram。" section_hint: `section-3-reproduction`. |
| Reason        | I-03: cyanotype and photogram are missing from the glossary; both belong in Section 3. |
| Evidence      | F-13, F-24. |
| Risk          | Low — additive, doesn't conflict with existing entries. |

**Impact:** data-file only (adds 2 entries; data file byte grows).

## CHG-13 — `data/exhibition.json` version marker bump

> **Required (marker only).**

| Field         | Value |
|---|---|
| File          | `second-exhibition/data/exhibition.json` |
| JSON path     | `version`, `marker` |
| **Current**   | both `second-exhibition-v0.1` |
| **Proposed**  | both `second-exhibition-v0.2` |
| Reason        | version bump marker |
| Evidence      | existing convention |
| Risk          | Low |

**Impact:** data-file only.

## CHG-14 — `second-exhibition/docs/*.md` wording refresh

> **Recommended. Only the four narrative docs.**

| File                               | Section title | What changes |
|---|---|---|
| `VISITOR_GUIDE_ZH.md`              | 第二步 / 第三步 | sentence-level reframing of "what to do" → "what to look for"; align with the new 3-min guide |
| `CURATORIAL_ESSAY_ZH.md`           | 第二节 / 第三节 | tighten the "specimen / watercolour / photogram" wording to match CHG-02 / CHG-04 |
| `DEEP_RESEARCH_NOTES_ZH.md`        | (no new sections) | append one sentence on IIIF Presentation API manifest caveat re-verification cadence |
| `BUILD_ASSET_USAGE.md`             | 关键 caveat 汇总 | refresh caveat phrases to match CHG-09 / CHG-10 wording |

**Impact:**

- Page byte: NO (`docs/` is loaded only by the footer / source-block link list in `data/assets.json`'s `source_note` strings — but only as referenced URLs, never embedded; the user downloads them as separate Markdown files). Verify via `data/assets.json` URLs only.
- Source SHA: NO.
- Staged / Live SHA: NO.
- Browser QA: NO.
- Gate QA: NO.
- Asset checksums: NO.

## CHG-15 — README / V5_ROADMAP updates

> **Required (release documentation).**

| File                    | Change |
|---|---|
| `README.md`             | Add `## v5.6 Second Exhibition Content Iteration Prep` section analogous to `## v5.5b Staging Audit Key Semantics Fix`. |
| `docs/V5_ROADMAP.md`    | Append `## v5.6 Second Exhibition Content Iteration Prep` section. |
| `reports/…v5_6…report.md` | New file written by the v5.6 round itself. |

**Impact:**

- Page byte: NO (root `README.md` is not under `site/`).
- Source SHA: NO.
- Staged / Live SHA: NO.
- Browser QA: NO.
- Gate QA: NO.
- Asset checksums: NO.

## Cross-impact summary

If the **only** rows implemented in v0.2 are the *blocker* (CHG-01)
plus *recommended* (CHG-02 … CHG-10 + CHG-13), the production-affecting
rows are limited to two:

- **CHG-09 / CHG-10** (HTML edits) — these change `site/index.html`
  and `second-exhibition/site/index.html` byte counts, which **does**
  affect the canonical root SHA `e2be1077…` and the second-exhibition
  source SHA `f31ddcba…`.
- **CHG-01, CHG-02, CHG-03, CHG-04, CHG-05, CHG-06, CHG-07, CHG-08,
  CHG-11, CHG-12, CHG-13** — JSON edits only; **do not** affect
  `site/index.html` or `second-exhibition/site/index.html`; **do**
  affect the bytes of the `data/*.json` files which are loaded by
  JavaScript at page-render time but are not currently in the 34-file
  Pages artifact (they are served separately under the
  `second-exhibition/data/` URL). Staging builder does not rewrite
  `data/*.json`. Staged root index SHA does not change.

> **Important caveat**: the 34-file public artifact is built from
> `site/` and `second-exhibition/` only (no `data/*.json`).
> Therefore if v0.2 only touches `data/*.json` and the named HTML
> paragraphs, the *staged artifact* can stay byte-identical to v0.1
> for the root surface and only differ on `second-exhibition/`
> bytes where Section bodies or glossary callouts render into
> `second-exhibition/site/index.html`. The exact diff delta is
> captured by the staging builder audit (`root_site` and
> `second_exhibition` blocks).

## Authority gate

This Changeset Draft is planning-stage. v0.2 implementation is
permitted only after:

- An explicit `IMPLEMENT v5.6b` directive from the operator.
- An exact diff review against the freeze at HEAD `ce01f1d…` /
  tag `ac0f19e2…` is recorded.
- The acceptance criteria document is read in full.

See
[`docs/SECOND_EXHIBITION_CONTENT_ACCEPTANCE_CRITERIA_v5.6.md`](SECOND_EXHIBITION_CONTENT_ACCEPTANCE_CRITERIA_v5.6.md)
for the gate that the v0.2 implementation round must pass.
