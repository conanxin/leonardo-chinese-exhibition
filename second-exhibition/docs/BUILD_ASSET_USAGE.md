# 资产使用图谱 / Build Asset Usage

> 本表把 v4.5 阶段导入的 6 件资产放回本展览（v4.6 阶段）的页面使用上下文：每个 asset 在哪一节出现、扮演什么角色、显示多大尺寸、是否启用 lightbox、caveat 是什么。本表是元数据层（v4.5 manifest / source audit / rights docs）与页面层（v4.6 index.html）之间的桥梁。
>
> 本表与 `second-exhibition/data/assets.json` 一一对应；本表是它的可读版本（适合 markdown 阅读），`assets.json` 是它的机器可读版本（适合 gate / script / future-round validator）。
>
> 核对时间：2026-07-11。

## 6 件资产在页面中的角色

| ID | Filename | Section | Page role | Display size | Lightbox | Source note present | Credit line present | Caveat |
|---|---|---|---|---|---|---|---|---|
| **C-01** | `bhl-318921-page-603998-c01.webp` | 01 · 观察 | primary botanical illustration | large (max-width 720px on desktop) | enabled | yes | yes | BHL `/pageimage/` 端点返回 WebP。Distinct page from C-03。 |
| **C-03** | `bhl-318921-page-603962-c03.webp` | 03 · 复制 | publication / page example | large (max-width 720px on desktop) | enabled | yes | yes | **PD subset only**；BHL 同 item 的 CC BY-NC-SA 子集仍被 blocked-from-import。Distinct page from C-01。 |
| **C-06** | `smithsonian-nmnh-1529703.png` | 02 · 分类 | compact specimen / catalogue thumbnail | small (max-width 180px, natural size 90×90) | **disabled** | yes | yes | **90×90 low-resolution source media**；不放大，不作为 Hero，不启用 lightbox。 |
| **C-08** | `met-285149.jpg` | 02 · 分类 | institutional specimen comparison | medium-large (max-width 480px on desktop) | enabled | yes | yes | **Double-confirmation PASS**：API `isPublicDomain=true` + public-page Public Domain indicator。Credit line "Gift of Russell C. Vail, 2003" 待 v4.7 repository QA 复核。 |
| **C-09** | `rijksmuseum-rp-f-f80152.jpg` | 03 · 复制 | printed reproduction (cyanotype) | large (max-width 480px on desktop) | enabled | yes | yes | **Per-item licence**：Rijksmuseum 公开页面逐项标注版权为 Public domain（CC0 1.0）。对象类型为 photogram（cyanotype），不是传统版画。 |
| **C-10** | `rijksmuseum-rp-f-f80313.jpg` | 03 · 复制 | printed reproduction (cyanotype), companion to C-09 | large (max-width 480px on desktop) | enabled | yes | yes | **Per-item licence**：Public domain（CC0 1.0）。**Manifest 404 caveat**：Rijksmuseum IIIF Presentation API manifest `/manifest.json` 在 v4.5 阶段返回 HTTP 404；本展览不基于 IIIF Presentation API manifest 撰写任何陈述。 |

## 章节分布（与 `second-exhibition/data/sections.json` 一致）

- **01 · 观察**：[C-01]
- **02 · 分类**：[C-06, C-08]
- **03 · 复制**：[C-03, C-09, C-10]
- **04 · 再组织**：[C-01, C-03, C-06, C-08, C-09, C-10]（"使用图谱"汇总视图，不展示新图像）

## 与元数据层的一一对应

每件 asset 在 `assets.json` 中的字段都对应到上表中的某一列：

- `candidate_id` ↔ ID
- `filename` / `local_path` ↔ Filename
- `section_id` ↔ Section
- `low_resolution` ↔ Display size（小尺寸 + Caveat 列）
- `lightbox_enabled` ↔ Lightbox
- `source_note` ↔ Source note present
- `credit_line` ↔ Credit line present
- `viewing_note` ↔ Caveat

`import_status` 字段对所有 6 件资产都是 `imported-not-deployed`（在 `assets.json` 与本表中都成立）。

## 与 v4.5 阶段证据的一一对应

每件 asset 的 identifier、institution、rights basis、source URL、media URL、官方 source URL 都来自 v4.5 阶段产出的 `second-exhibition/assets/asset-import-manifest.json` 与 `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` / `RIGHTS_AND_SOURCES.md`。本展览没有引入任何新的 source / rights 字段；如果未来 round 需要新增字段，必须重新打开对应官方页面核对。

## 关键 caveat 汇总

- **C-01 / C-03**：BHL 同 item 不同 page；SHA-256 互不相同；C-03 仅 PD 子集。
- **C-06**：低分辨率（90×90）缩略图；页面不得作为大幅展示；不启用 lightbox；image-rendering 使用浏览器默认值（不像素化、不模糊扩展）。
- **C-08**：double-confirmation PASS（API + public-page）。
- **C-09 / C-10**：per-item Public domain / CC0 1.0；对象类型 cyanotype（不是传统版画）。
- **C-10**：IIIF Presentation API manifest `/manifest.json` 返回 404，本展览不基于 manifest 撰写任何陈述。

## 引用规则

任何后续出版物引用本展览中的 6 件资产，必须：

1. 重新打开对应 source URL 与 rights URL 核对现状；
2. 在 credit line 中标注 institution 与 per-item 或 dataset-level 的 rights basis；
3. 在 source note 中标注 source URL 与获取日期；
4. 对低分辨率资产（C-06）必须显式说明"低分辨率缩略图"；
5. 对 404 caveat（C-10 IIIF Presentation API manifest）必须显式说明"本轮 manifest 不可用"。

不允许：把 6 件资产描述为 `approved` / `deployed` / `live` / `safe for commercial use` / `cleared for all uses` 中的任何一种。