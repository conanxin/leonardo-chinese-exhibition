# v2.8 Real Deep Content

> 2026-07-07 · 真实稳定封版 (real stable freeze)
>
> 本 release 把 v2.8 真实深度内容扩展正式独立 tag + release，作为下一 round（v2.9+）的真实起点。

## Release identity

- **Live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/
- **Tag**: `v2.8-real-deep-content`
- **Source tag**: `v2.7-zh-exhibition-polish` @ `f58f6b4`
- **Verified live byte size**: **92,507 B**
- **Content commit**: `18b551b2e7c832bb5e34d2cf904b8ce90b887978` — *Rebuild v2.8 deep content from verified baseline*
- **Backfill commit**: `dfecf202d07b430e7df2e50676c3613464b4c03c` (报告数字回填)
- **Freeze commit**: 留空（freeze round 提交后回填）
- **Status**: verified real deep content

## What changed (相对于 v2.7-zh-exhibition-polish)

v2.8 Real Deep Content 是**从真实 v2.7 tag 出发重建**的深度内容扩展版。它**不**引用 phantom v2.8 / v2.9 / v3.x 历史，不做双语、不做教育版、不做模板化。

### 内容层面

- 新增「被装订改变的思想」深度模块（`.deep-reading-block`，位于 section1 之后、section2 之前）
  - 解释手稿命运不是单纯保存史，而是知识结构被重新排序的历史
  - 三个层次：达·芬奇留下工作纸页 / 梅尔齐继承仍在生成中的工作现场 / 莱奥尼裁切装订保存材料也改变关系
- 新增「纸页也在说话」深度模块（`.material-evidence-block`，位于 section4 之后、section5 之前）
  - 4 个 evidence chips：水印 / 裁切边缘 / 编号 / 空白与方向
  - 把纸张证据从辅助信息提升为第一手证据
- 新增「图像如何成为思考工具」深度模块（`.visual-thinking-block`，位于 section3 之后、section4 之前）
  - 4 个 thought cards：水:运动 / 肌肉:结构 / 动物:姿态 / 机械:推演
  - 深化「达·芬奇不是画插图，而是用图像思考」
- 新增「从看图到建模：Leonardo//thek@ 的研究逻辑」深度模块（`.research-model-block`，位于 section7 之后、section8 之前）
  - 9 个 method rows：Foliations / Subject Indexes / Photographic Plates / Lexicon / Watermarks / Recompositions / Bibliography / Advanced Search / Comparative Study
  - 把平台九大工具从列表提升为「从图像到证据、到关系、到论证」的工作流
- 深化 postscript（从「不是天才崇拜」4 点短句，深化为「关于知识如何生成 / 材料如何打断 / 数字平台如何重新连接 / 今天我们能学到什么」4 段，约 480 字）
- 新增 [`docs/CURATORIAL_ESSAY_ZH.md`](../docs/CURATORIAL_ESSAY_ZH.md) — 中文策展长文（5 节，约 2,600 字）
- 新增 [`docs/DEEP_RESEARCH_NOTES_ZH.md`](../docs/DEEP_RESEARCH_NOTES_ZH.md) — 研究深化笔记（13 个可深挖问题 / 6 个待查证事实 / 8 个后续轮方向）

### 元数据层面

- v2.8 footer marker `v2.8 real deep content`（strong）
- v2.7 / v2.6 / v2.5-real / v1.5b 历史 marker 全部保留（三层：meta / comment / footer）
- 4 个深度模块用 `<aside>` 而非新 `<section data-section>` —— 不进入 `getTourSections()` 的 section registry，保持 v2.5-real runtime section-nav 与 guided mode 完全兼容

### Issue 状态

- GitHub Issues #1 / #2 / #3 / #4 全部保持 OPEN（与本 round 内容无直接关联）。Issue #1 标题「v2.7 Bilingual Edition」与实际做的「Chinese Exhibition Polish」不一致 —— 这是历史遗留命名差异，本 round **不**强行关闭 / 重命名，留给后续 round 单独处理。

## Verification (live 实测 2026-07-07)

| 项 | 命令 | 结果 |
|---|---|---|
| Live HTTP | `curl -LIs` | 200 |
| Live byte size | `wc -c` on `curl -L -s` | **92,507 B** |
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | 1 |
| v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| deep-reading-block | `grep -c` | 1 |
| material-evidence-block | `grep -c` | 1 |
| visual-thinking-block | `grep -c` | 1 |
| research-model-block | `grep -c` | 1 |
| quick-guide-zh | `grep -c` | 1 |
| viewer-action | `grep -c` | 4 |
| image-placeholder-pro | `grep -c` | 0 |
| section-takeaway | `grep -c` | 18 (≥ 9) |
| script.js | `curl -LIs` | HTTP 200 |
| `node --check site/script.js` | syntax check | PASS |

### Playwright 运行时检查（python3.12 + Playwright 1.58.0）

| 项 | 结果 |
|---|---|
| section-nav runtime links | 31 (与 v2.5-real 基线一致) |
| 4 deep blocks | 1 / 1 / 1 / 1 |
| guided-mode toggle | **OK** (body class 切换 `guided-mode`) |
| lightbox open | **OK** (role=dialog 出现 1 次) |
| mobile 390 overflow | **0 px** ✓ |
| console errors | **[]** ✓ |

## No-touch confirmation (freeze round)

| 类别 | 状态 |
|---|---|
| v2.0 tag (`v2.0-public-portfolio-case`) | untouched (基线 9e6233a) |
| v2.6 tag (`v2.6-content-stable`) | untouched (基线 033b65e / 01cdaa2) |
| v2.7 tag (`v2.7-zh-exhibition-polish`) | untouched (基线 a0fee10 / f58f6b4^{}) |
| Old GitHub Releases (v2.0 / v2.6 / v2.7) | untouched |
| `site/index.html` | 不修改 (freeze round 仅文档) |
| `site/style.css` | 不修改 |
| `site/script.js` | 不修改 (v2.8 content round 已不动) |
| `posts/` | 不修改 |
| `case-study/` | 不修改 |
| `release-assets/` 既有文件 | 不修改（仅新增 v2.8 manifest） |
| `_template/` | 不创建（按约束） |
| `_pilots/` | 不创建（按约束） |
| Untracked `.firecrawl/` | 不处理 |
| `git add .` | 不用 |

## Known note

Earlier phantom v2.8 / v2.9 / v3.x task histories were recorded as **phantom / unverified** in [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md). 本 v2.8 是从 verified `v2.7-zh-exhibition-polish` tag 真实重建，**不**复用任何 phantom 阶段叙述。下一 round 起点为本 tag。

## Files in this release

| 文件 | 角色 |
|---|---|
| `docs/RELEASE_NOTES_v2.8_REAL_DEEP_CONTENT.md` | 本文件 |
| `release-assets/v2.8-real-deep-content-manifest.md` | release manifest |
| `reports/leonardo_chinese_exhibition_v2_8_real_stable_freeze_report.md` | freeze round 报告 |
| `README.md` | v2.8 Real Deep Content 小节更新 |

---

*v2.8-real-deep-content 是真实 deep content 的第一次正式 freeze。下一个 round（v2.9+）从本 tag 出发。*