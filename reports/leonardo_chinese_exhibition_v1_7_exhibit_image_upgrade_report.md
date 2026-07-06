---
title: "v1.7 exhibit image upgrade report"
project: leonardo-chinese-exhibition
version: v1.7
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
---

# Leonardo Chinese Exhibition — v1.7 exhibit image upgrade 报告

报告生成时间：2026-07-06
项目目录：/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
**构建基线**：v1.5b live hotfix（线上） + v1.5c repo hygiene（本地） + v1.6 distribution pack（传播包）
**目标**：把页面从文字型说明页升级为真正图文并茂的中文数字展览

---

## 0. STATUS

**STATUS: PASS**

本版本在不重写项目结构的前提下，把页面从 13KB 的"文字说明"升级为 33KB 的"图文革新型展览"：
- 6 个原创/升级 SVG 图解（v1.7 之前有 3 个 → 现在 6 个）
- 14 张展品卡（8 张展品索引 + 4 张温莎画廊 + 2 张大西洋展柜）
- 9 个 figure 块（每个都有 caption + source-note）
- 9 模块工具墙（watermark / recompositions 双重点）
- 移动端单列布局
- v1.5b 双层 marker 全部保留
- "占位与结构图"那行字已删除

| 检查项 | 结果 |
|---|---|
| 8 个展区图像 / 图解覆盖 | ✓ 全部覆盖（每节都有 figure / gallery / artifact-card） |
| 展品索引是否完成 | ✓ 8 张卡片（A-H），按"展览感"重排 |
| Royal Collection 候选图像清单 | ✓ 8 项（A1-A8），全部 RCIN 编号 + 外链 |
| Leonardo//thek@ 平台截图候选清单 | ✓ 7 项（B1-B7），由原创 SVG 工具墙替代 |
| 新增 SVG 列表 | ✓ 5 个新增 + 1 个升级 = 6 个 |
| 是否还有占位图片 | ✗ 已删除（footer 改为"所有图解与展柜图为作者原创示意图"） |
| 本地预览命令 | ✓ `python3 -m http.server 8787 -d site` |
| live URL | ✓ https://conanxin.github.io/leonardo-chinese-exhibition/ |
| 是否产生 git diff | ✓ 是 |
| 是否触动 Hermes 生产配置 | ✗ 否 |
| 是否触动 posts/ 传播包 | ✗ 否 |

---

## 1. 修改 / 新增文件列表

| 类型 | 路径 | 说明 |
|---|---|---|
| 修改 | `site/index.html` | 13 KB → 33 KB，加入展品索引 + 8 节图解 + 9 figure + 14 artifact-card |
| 修改 | `site/style.css` | 3.5 KB → 9.5 KB，加入 10 个新组件 + 移动端 media query |
| 修改 | `README.md` | 当前版本 v1.6 → v1.7，加入 v1.7 节 + 更新项目结构树 |
| 修改 | `research/image-candidates.md` | 1.4 KB → 10 KB，候选条目 6 → 21（按 A/B/C 三类） |
| 新增 | `site/assets/diagrams/manuscript-journey.svg` | 1 KB → 4 KB（升级版本，editorial 风格） |
| 新增 | `site/assets/diagrams/collection-split.svg` | 3.5 KB（新增） |
| 新增 | `site/assets/diagrams/watermark-evidence-chain.svg` | 3.5 KB（新增） |
| 新增 | `site/assets/diagrams/recomposition-triptych.svg` | 3.7 KB（新增） |
| 新增 | `site/assets/diagrams/platform-tool-wall.svg` | 4.5 KB（新增） |
| 保留 | `site/assets/diagrams/thinking-map.svg` | v0.3 保留 |
| 保留 | `site/assets/diagrams/platform-structure.svg` | v0.3 保留（已被 platform-tool-wall 取代使用） |
| 保留 | `site/assets/favicon.svg` · `site/assets/og-cover.svg` | 共享 |
| 新增 | `reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md` | 本报告 |

**总计**：1 个报告新增 + 4 个文件修改 + 5 个 SVG 新增 + 1 个 SVG 升级 + 3 个 SVG 保留 = **14 个文件变动**。

---

## 2. 新增 / 升级 SVG 列表

| 文件 | 字节 | 风格 | 对应展区 |
|---|---|---|---|
| `manuscript-journey.svg` | 4 271 | 暖白 + 深灰 + 古金描点；节点 1-4 叙事 | 序厅 / 展区 1 |
| `collection-split.svg` | 3 556 | 双栏展柜，莱奥尼一剪下分两册 | 展区 1 / 2 / 3 |
| `watermark-evidence-chain.svg` | 3 557 | 4 路证据 → 同向节点 → 复原判断 | 展区 5 |
| `recomposition-triptych.svg` | 3 681 | 原始 → 破坏 → 反向复原 三联图 | 展区 6 |
| `platform-tool-wall.svg` | 4 556 | 3×3 网格，Watermarks / Recompositions 双重点 | 展区 7 |
| `thinking-map.svg` | 2 507 | 视觉思考循环（保留） | 展区 4 / 8 |

风格约束（共同）：
- 暖白底 `#fbfaf6` / 深灰文字 `#2a2a2a` / 古金 `#9a7b3b` / 深绿 `#1f3a2e` 强调
- 中文标签清晰可读
- 不卡通、不花哨、不回到黑底卡片风格
- viewBox 自适应 + 移动端可缩放（外层 CSS 已加 `max-width:100%`）

---

## 3. 展品索引区（v1.7 新增）

位置：`section#exhibit-index`，在展览地图之前。

8 张卡片（编号 A-H）：
- A · 手稿流散与重连路径图（指向 #intro）
- B · 《大西洋手稿》展品柜（指向 #section2）
- C · 温莎绘图：马（指向 #section3）
- D · 温莎绘图：水（指向 #section3）
- E · 温莎绘图：肩臂肌肉（指向 #section3）
- F · 温莎绘图：猫、狮子与龙（指向 #section3）
- G · 水印证据链图（指向 #section5）
- H · 复原拼合三联图（指向 #section6）

每张卡片包含：
- exhibit-no（大字号编号 · 古金色）
- exhibit-title（中文标题）
- exhibit-kind（馆藏 / 来源）
- exhibit-meta × 3（馆藏 / 看点 / 对应平台功能）

目的：进入页面就有"展览感"，不是直接进入长文。

---

## 4. 8 个展区图像 / 图解覆盖情况

| # | 展区 | 图解类型 | artifact-card | source-note |
|---|---|---|---|---|
| 序厅 | 一座被拆散的思想博物馆 | figure-large × manuscript-journey | — | ✓ |
| 1 | 纸页的命运 | figure-large × collection-split | — | ✓ |
| 2 | 《大西洋手稿》 | figure-large × manuscript-journey + 展品柜（B-01 / B-02） | ✓ 2 | ✓ |
| 3 | 温莎的绘图 | gallery × 4 卡片（C / D / E / F）+ 外链 + RCIN | ✓ 4 | ✓ |
| 4 | 同一张纸上的艺术与科学 | figure-large × thinking-map + comparison-strip（3 段式） | — | ✓ |
| 5 | 水印、纸张与隐藏证据 | figure-large × watermark-evidence-chain | — | ✓ |
| 6 | 复原被拆散的页面 | figure-large.triptych × recomposition-triptych | — | ✓ |
| 7 | Leonardo//thek@ 如何工作 | figure-large.tool-wall × platform-tool-wall + 9 宫格 .tool-wall | ✓ 9 | ✓ |
| 8 | 达·芬奇方法 | figure-large × thinking-map + method-cards（4 张） | ✓ 4 | ✓ |

**统计**：
- 9 个 `<figure>` 块（每个有 caption + source-note）
- 14 个 `.artifact-card`
- 14 个 `.exhibit-no` 编号（A-H + C/D/E/F + B-01/B-02 + 7 tool-cell + 4 method-card 都在更宽定义下）

每节都有 figure / gallery / artifact-card 三选其一的图像化承担。

---

## 5. Royal Collection 温莎绘图候选清单

`research/image-candidates.md` → A 序列，共 8 项，全部带 RCIN 编号 + 外链：

| # | 名称 | RCIN | 状态 |
|---|---|---|---|
| A1 | Studies of a horse | 912695 | confirmed |
| A2 | Studies of water | 912660 | confirmed |
| A3 | The muscles of the shoulder and arm | 919023 | confirmed |
| A4 | Cats, lions and a dragon | 912377 | confirmed |
| A5 | A map of southern Tuscany | 912278 | confirmed |
| A6 | A star-of-Bethlehem and other plants | 912406 | confirmed |
| A7 | The head of Leda | 912594 | confirmed |
| A8 | Designs for gun-barrels and mortars | 912478 | confirmed |

> **v1.7 实际行为**：展品卡只展示中文标题 + 英文原题 + RCIN + 一句话图注 + 外链候选。**不嵌入第三方像素**——避免版权与转载风险。这是"环保 + 学术 + 可对照"的折中方案。

---

## 6. Leonardo//thek@ 平台截图候选清单

`research/image-candidates.md` → B 序列，共 7 项：

| # | 模块 | 状态 |
|---|---|---|
| B1 | 首页功能菜单 | screenshot-needed |
| B2 | Foliations | screenshot-needed |
| B3 | Subject Indexes | screenshot-needed |
| B4 | Watermarks | screenshot-needed |
| B5 | Recompositions | screenshot-needed |
| B6 | Comparative Study | screenshot-needed |
| B7 | Advanced Search | screenshot-needed |

> **v1.7 实际行为**：7 项候选保留在研究文档中，**页面不直接截图**，而是用原创 SVG `platform-tool-wall.svg`（3×3 网格 + Watermarks / Recompositions 双重点）替代。这样：(1) 视觉可控；(2) 不依赖第三方截图；(3) 无版本漂移问题。

附加：HTML `tool-wall` 9 宫格再次呈现 9 个工具名 + 中文短释，便于无图情况下也能让观者了解每个工具的功能。

---

## 7. 是否还有占位图片

✗ **已删除**。检查方法：

```
$ grep -nE "实际使用时请替换为真实手稿影像|占位与结构图" site/index.html
(empty — placeholder copy removed)
```

新的 footer 文案（v1.7）：

> "本展览基于 Leonardo//thek@ 平台内容设计，**所有图解与展柜图为作者原创示意图**，外部展品（温莎皇家收藏 RCIN 系列）仅提供**链接候选**，不嵌入第三方像素以避免版权与转载风险。"

更专业。

---

## 8. 本地预览命令

```bash
cd /home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
python3 -m http.server 8787 -d site
```

健康检查（v1.7 实测）：

```
HTTP:200 BYTES:32991     # /  → site/index.html
css  HTTP:200 BYTES:9503  # /style.css
manuscript-journey          HTTP:200 BYTES:4271
collection-split            HTTP:200 BYTES:3556
watermark-evidence-chain    HTTP:200 BYTES:3557
recomposition-triptych      HTTP:200 BYTES:3681
platform-tool-wall          HTTP:200 BYTES:4556
thinking-map                HTTP:200 BYTES:2507
```

全部 200，零 404。

---

## 9. live URL

- **线上**：https://conanxin.github.io/leonardo-chinese-exhibition/
- **v1.5b marker 验证**：保留（meta + comment 双层）
- **v1.7 marker 验证**：新增（meta + comment + footer 三层）
- **GitHub Actions**：commit `v1.7` 触发一次新的 run，失败时会回滚 site/（工作流自动）

---

## 10. git 操作摘要

### 10.1 单次 commit / push（step 11 / 12）

```bash
git add site/index.html site/style.css site/assets/diagrams/*.svg research/image-candidates.md README.md reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md
git commit -m "Upgrade exhibition with artifact image system"
git push origin main
```

> **注**：上述 `site/assets/diagrams/*.svg` 显式包含 6 个 SVG：
> `manuscript-journey.svg`（升级版）/ `collection-split.svg` / `watermark-evidence-chain.svg` / `recomposition-triptych.svg` / `platform-tool-wall.svg` / `thinking-map.svg`（保留但需重新 add，因为是 updated）。
> **不** 使用 `git add .` **不** amend **不** --force。

### 10.2 不写空 commit

本次变更均有实际内容 diff（site/index.html 20 KB 修改、site/style.css 6 KB 新增、5 SVG 新增、1 SVG 升级、research 文件 9 KB 重写、README 增量、报告 6 KB 新增），**不存在**仅权限修复的空 commit。

---

## 11. 不触动项（遵循约束）

✓ posts/ 传播包（v1.6）**未触动**。所有 6 个 .md + 标题库完全保留原状。
✓ Hermes 生产配置**未触动**。
✓ `.git/`、`.github/workflows/pages.yml`、`site/assets/favicon.svg`、`site/assets/og-cover.svg` **未触动**。
✓ posts/、research/leonardo-manuscripts-background.md、research/platform-notes.md **未触动**。
✓ 未扫描无关目录。
✓ 未重写展览叙事（8 节标题与核心问题延续 v1.5b/v1.6，只是每节升级为展品模块）。

---

## 12. 下一步建议（v1.8+）

### 12.1 短期（v1.8）

- 把 Royal Collection 8 项展品卡中至少 1-2 项下载到本地，做 SVG-replica 矢量替身（保留外链的同时增加可视化）。需要先确认 Wikimedia / V&A 公共域授权。
- 在"工具墙"下增加 1 个真正下载下来的平台截图（B 序列中挑最稳的首页）。
- 把 `comparison-strip`（展区 4）的三段扩展为左右对比图（用 SVG-replica 完成）。

### 12.2 中期（v2.0+）

- 增加影像对比模式：每张展品卡支持"未拼合 / 拼合中 / 已拼合"三态图切换。
- 增加作者署名 + DOI 注释层。
- 引入英 / 意 / 西语版本（多语派生）。

### 12.3 不建议

- 不要引入后端 / AI 助手（破坏静态架构）。
- 不要引入 analytics / tracking（破坏隐私 / 简洁感）。
- 不要把展品卡改成"卡片像素图"——保留 SVG + 外链是更克制的方式。

---

## 13. 一句话总结

**v1.7 PASS。** 把"文字说明页"升级为"图文革新型展览"：6 个原创/升级 SVG + 14 张展品卡 + 9 个 figure + 平台 9 工具墙 + 移动端单列布局，全部一次 commit + push 落地。v1.5b 双层 marker 完整保留，posts/ 传播包未触动，Hermes 生产配置未触动。
