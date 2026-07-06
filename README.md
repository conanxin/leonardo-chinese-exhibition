# 达·芬奇的纸上宇宙：被拆散的手稿与重新连接的思想

基于 Leonardo//thek@ 平台的中文数字展览项目。

## Live Demo
https://conanxin.github.io/leonardo-chinese-exhibition/

## 当前版本

- **Latest stable tag**: `v2.0-public-portfolio-case`（v2.0 portfolio 稳定版）
- **Active stable tag**: `v2.6-content-stable`（v2.6 内容稳定版，修正历史误报后的真实版本线）
- **Live URL**:

> https://conanxin.github.io/leonardo-chinese-exhibition/

## Stable release

Current active stable release:

- **v2.6-content-stable**（v2.6 Content Stable）
- Tag target: `01cdaa2dc1487a5f7877c8702720d0df8dbb17ce`
- Live: https://conanxin.github.io/leonardo-chinese-exhibition/
- GitHub Release: *(回填于 Step 9 — 见下方 "GitHub Release" 小节)*

**说明**：当前稳定版是修正历史误报后形成的真实版本线，包含 v2.5-real guided accessibility recovery 与 v2.6 content copy polish。详见 [`docs/RELEASE_NOTES_v2.6_CONTENT_STABLE.md`](docs/RELEASE_NOTES_v2.6_CONTENT_STABLE.md) 与 [`release-assets/v2.6-content-stable-manifest.md`](release-assets/v2.6-content-stable-manifest.md)。

## v2.5 real guided accessibility（从真实 v2.4 状态出发的导览 + 无障碍恢复）

**重要诚实声明**：此前被报告为"已完成并上线"的 v2.5 guided tour mode 与 v2.6 interaction accessibility polish，**实际上从未进入 git 仓库**（`git reflog` 确认无对应 commit，且 live 一度仍为 v2.4）。v2.7 content copy polish（commit `31e5126`）是直接在 v2.4 之上做的，跳过了 v2.5 / v2.6。

本轮 v2.5-real **从真实 v2.4 / v2.7 当前状态** 重新实现并真实部署导览模式、运行时展区导航、Lightbox 无障碍、引导模式、图像延迟加载、prefers-reduced-motion 与 focus-visible。每一项都通过 Playwright 在本地 server 跑通。

| 新增模块 | 实现方式 |
|---|---|
| **运行时展区导览 section-nav** | `site/script.js` 的 `getTourSections()` / `createSectionNav()`，不手工插入；JS 启动时按页面 DOM 自动收集 `#intro` / `#section1`-`#section8` / `#exhibit-index` / `#visit-routes`，按位置给每个 section 追加 上一站 / 返回展览地图 / 下一站 三组链接 |
| **导览进度条 tour-progress** | 页面顶部 sticky bar，按 IntersectionObserver 实时更新当前展区 label + 短横条百分比 + jump-list；jump-link 当前项 `aria-current="true"`；进度条本身 `aria-hidden="true"`（纯视觉） |
| **9 个 section-takeaway 摘要卡** | 每个主要 section 顶部插入 `<aside class="section-takeaway">`："本区带走" + 1–2 句话 |
| **5 分钟导览模式** | 参观路线模块新加按钮；body 加 `guided-mode` class；4 个核心展区（exhibit-index / section3 温莎 / section4 艺术与科学 / section7 平台）打 `guided-highlight`；其余降级并显示"可跳过"标签；banner 用 `role="status" aria-live="polite"`；退出按钮在 banner 内 |
| **Lightbox 无障碍硬化** | `role="dialog" aria-modal="true"`、close button `aria-label="关闭展品大图"`、Tab 键焦点 trap、ESC / backdrop / × 关闭、关闭后焦点回到原触发元素 |
| **图像延迟加载 belt-and-suspenders** | 23 张非首屏 `<img>` 加 `loading="lazy" decoding="async"`；hero 图刻意不加（首屏不延迟） |
| **`@media (prefers-reduced-motion: reduce)`** | 全站动画与过渡降到 0.01ms，`scroll-behavior: auto` |
| **`:focus-visible`** | 全局焦点环（2px brand-color，2px offset） |
| **Mobile 390px** | tour progress / section-nav / section-takeaway / guided-mode-banner 在窄屏下不溢出 |

**真实基线（commit `0d58fdc`，v2.7 backfill）**：

```
HEAD = origin/main = 0d58fdc (v2.7)
live = 77,474 字节, v2.7 markers (含 v2.5-real 之前的全部 v2.4 + v2.7)
v2.0 tag = v2.0-public-portfolio-case @ 9e6233a (未触碰)
```

**实现**：
- 修改 `site/index.html` (77,474 → 82,611 字节 · +6.6%)
- 修改 `site/style.css` (33,517 → 39,518 字节 · +17.9%)
- 重写 `site/script.js` (6,670 → 14,594 字节 · +118.8% · 加 7 个新函数：getTourSections / getSectionLabel / createSectionNav / buildTourProgress / applyGuidedMode / wireGuidedMode / ensureLazyImages)
- 显式 add（无 `git add .`）

**v2.5-real 报告**：`reports/leonardo_chinese_exhibition_v2_5_real_guided_accessibility_report.md`

**Playwright 验证（36/36 PASS）**：
- section-nav ≥ 9 ✓
- section-takeaway == 9 ✓
- image-placeholder-pro == 0 ✓
- glossary items ≥ 12 ✓
- annotation panels ≥ 4 ✓
- platform interface notes ≥ 5 ✓
- tour progress 存在 + 9 jump links ✓
- 5-min 按钮 + aria-pressed 切换 ✓
- guided-mode body class + banner role=status + aria-live=polite ✓
- 4 guided-highlight + guided-skip-note ✓
- Lightbox role=dialog + ESC + focus trap ✓
- 23 imgs loading=lazy + 23 imgs decoding=async ✓
- 8 个旧 markers 全部保留 + v2.5-real 新 marker ✓
- mobile 390 无横向溢出 ✓
- 0 console errors ✓

**section-nav 实际数量（已统一口径）**：
- v2.5-real 报告里曾用 "9+" / "10 generated" / "9+ in DOM" 三种说法（不准确）
- v2.6 通过 Playwright `document.querySelectorAll('.section-nav').length` 实地确认
- **真实数量 = 11**：#intro + #exhibit-index + #section1-#section8 + #visit-routes
- 这 11 个 section 每个都通过 `getTourSections()` 自动获得 nav，无重复
- 11 比 v2.5-real 报告的 "9+" 多 2 个：exhibit-index 与 visit-routes 之前被算到边界外

## v2.6 content copy polish（第三轮内容打磨）

v2.6 是在 v2.7 (commit `31e5126`) 与 v2.5-real (commit `c512dbd`) 之上的**第三轮内容打磨**。本轮**只改文案、不改功能**，目标是让页面读起来更像正式博物馆数字展览。

**主要修改**：

| 项 | 调整 |
|---|---|
| **v2.6 marker** | meta / HTML 注释 / footer 三层 |
| **Hero 导语** | 把"借助 Leonardo//thek@ 平台" / "反向连接" 改为更展览入口式的语气（"沿着手稿的命运走一遍——看清它如何被拆散，又如何被数字工具重新组织为可读的研究对象"） |
| **策展前言** | 同上语气；减少"反向连接"与"重新连接"的重复，让策展主旨更突出 |
| **《大西洋手稿》展区** | 修"与内容是否与大西洋无关"为"与内容是否涉及大西洋无关"（消除歧义） |
| **展品 B-01** | 修 typo "1 1 19 张纸页 · 40 余册大小" → "1119 张纸页 · 装订为多册"（未引用未确认的具体册数） |
| **CONTENT_STYLE_GUIDE** | 移除文末 emoji（"🔮"违反"不出现 emoji 装饰"规则）；更新到 v2.6 修订 |
| **section-nav 口径** | 用 Playwright 实地确认 = **11**（非 "9+"），v2.5-real 报告"9+ / 10 generated / 9+ in DOM"三种说法不统一，本轮统一 |
| **image loading/decoding 口径** | 静态 HTML = 24 imgs / 23 lazy / 23 decoding async；live DOM 因 lightbox `<img>` 注入多 1，= 25 / 24 / 24 |

**没有修改**：
- 任何 JS 逻辑（脚本只动了 aria / label 文案，不动行为）
- 任何 image 文件
- 任何 posts/ / case-study/ / release-assets/ 文件
- v2.0 tag
- 旧 8 个 markers 全部保留
- section-nav 数量 = 11（runtime 真实值）
- glossary 14 项
- annotation panels 4 个
- platform interface notes 5 个
- section-takeaway 9 个
- image-placeholder-pro 0
- lightbox a11y、guided mode、tour progress 行为

**Playwright 验证（25/25 PASS）**：
- section-nav == 11 ✓
- section-takeaway == 9 ✓
- image-placeholder-pro == 0 ✓
- glossary == 14 ✓
- annotation panels ≥ 4 ✓
- platform interface notes ≥ 5 ✓
- v2.6 marker 存在 + 7 个旧 marker 保留 ✓
- 8 个 v2.6 footer 项全部显示 ✓
- Lightbox role=dialog + aria-modal=true + close aria-label="关闭展品大图" + ESC ✓
- Guided mode aria-pressed + body.guided-mode + exit ✓
- mobile 390 无横向溢出 + section-nav 仍 11 ✓
- 0 console errors ✓

**v2.6 报告**：`reports/leonardo_chinese_exhibition_v2_6_content_copy_polish_report.md`

## v2.6 Content Stable

v2.6 content stable 是当前**真实稳定封版**。

- **Stable commit**: `d71b0e8`
- **Stable tag**: `v2.6-content-stable`（本轮新增）
- **Live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/
- **Live byte size**: 82,787 B
- **Live Playwright 验证**: 14/14 PASS

本轮在 v2.6 content copy polish 之上完成：

- 真实版本链整理：v2.4 → v2.5-real → v2.6 → **v2.6 stable**
- 清理了上一轮残留的 stale `v2.7-content-copy-polish` marker
- 新增 `v2.6-content-stable` marker（三层：meta / HTML 注释 / footer）
- 撰写 `docs/RELEASE_NOTES_v2.6_CONTENT_STABLE.md` 与 `reports/leonardo_chinese_exhibition_v2_6_content_stable_audit_report.md`
- section-nav 口径统一为 **11**（早前报告 "9+ / 10 generated / 9+ in DOM" 三种说法已澄清）
- no-touch 严格遵守：v2.0 tag / 旧 GitHub Release / `posts/` / `case-study/` / `release-assets/` / Hermes 生产配置 **均未触碰**

**Release notes**: [`docs/RELEASE_NOTES_v2.6_CONTENT_STABLE.md`](docs/RELEASE_NOTES_v2.6_CONTENT_STABLE.md)
**Audit report**: [`reports/leonardo_chinese_exhibition_v2_6_content_stable_audit_report.md`](reports/leonardo_chinese_exhibition_v2_6_content_stable_audit_report.md)

## v2.7 content copy polish

v2.7 是 v2.0 freeze 后的内容打磨轮。不动展览结构、不动交互逻辑，只做：

- **内容审校**与中文文案打磨（Hero、策展前言、8 个展区、9 段总结、图注、source note、credit-line、annotation panel、glossary、postscript、footer）
- **术语统一**：达·芬奇 / 《大西洋手稿》 / Royal Collection / 安布罗西安图书馆 / 弗朗切斯科·梅尔齐 / 庞佩奥·莱奥尼 / 11 个平台模块中英文
- **图注与 source note 格式统一**（图名 / 年代 / 馆藏 + 它展示了什么 + 为什么重要）
- **glossary 14 个术语** 打磨为 1–2 句简明解释
- **decoding="async" 补充**：对非首屏 19 张真实图片补充，不改首屏装饰图
- **事实边界**保持：1519 年达·芬奇去世 / 《大西洋手稿》1119 页 / 温莎约 600 张 / 名称与装订尺寸有关

详见 [`reports/leonardo_chinese_exhibition_v2_7_content_copy_polish_report.md`](reports/leonardo_chinese_exhibition_v2_7_content_copy_polish_report.md) 与 [`docs/CONTENT_STYLE_GUIDE.md`](docs/CONTENT_STYLE_GUIDE.md)。

## v2.0 stable release

本仓库的 v2.0 是稳定冻结版本。

- 展览本体 `site/` 在 v1.8 / v1.9 已成熟，v2.0 不再修改
- 7 件作品化文档全部在 `case-study/` 下发布
- Git tag `v2.0-public-portfolio-case` 已创建，可通过 `git checkout v2.0-public-portfolio-case` 切到稳定快照

**Release notes**: [`docs/RELEASE_NOTES_v2.0.md`](docs/RELEASE_NOTES_v2.0.md)
**v2.0 freeze 报告**: `reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md`

## v2.2 exhibition experience upgrade（可参观的数字展览）

v2.2 是展览本体升级版。在不动展览正文的前提下，把"图文展览页"升级成**更像可参观的数字展览**的页面：

| 新增模块 | 位置 | 内容 |
|---|---|---|
| **选择你的参观路线** | 展览地图之后、序厅之前 | 3 张 route cards：5 分钟快速 / 15 分钟深度 / 研究者路线，每张含路线名、时长、适合谁、重点看、CTA 按钮 |
| **一张纸页的五百年旅程** | 展区 1 末尾 | 7 节点垂直时间线：1519 梅尔齐继承 → 莱奥尼剪裁 → 米兰/温莎分藏 → Leonardo//thek@ 1.0 → 2.0 → 本中文展览 |
| **展品细读** | 展区 3 末尾 | 2 张温莎皇家收藏图（水的涡旋 + 肩臂肌肉）的"先看哪里 / 再看什么 / 最后理解什么"细读卡 |
| **强化展区 7 研究工作台** | 展区 7 工具墙之后 | 4 个研究场景卡：原始编号 / 主题进入 / 判断相连 / 跨馆对比 — 对应 Foliations · Subject Indexes · Watermarks+Recompositions · Comparative Study |
| **展后总结** | 展区 8 之后、资料来源之前 | "这不是一场关于天才的展览" 短文 + 4 条要点（知识如何在纸上生成 / 图像如何成为思考工具 / 被拆散的材料如何被数字平台重新连接 / 今天的知识库和 AI 工具如何借鉴） |
| **Lightbox（展品细看）** | 全站 | 点击任意真实手稿图（含 reading-card）打开沉浸式 lightbox：大图 + title + subtitle + credit + "如何观看"说明，支持 ESC、点击背景、× 按钮三种关闭方式，无外部依赖（原生 JS `site/script.js`） |

**实现**：

- 仅修改 `site/index.html`（40,516 → 57,478 字节 · +41%）+ `site/style.css`（12,401 → 23,006 字节 · +85%）
- 新增 `site/script.js`（6,664 字节 · 原生 JS · 零依赖） — lightbox 自动绑定 `.artifact-image img` 和 `.reading-image img`、显式声明的 `img[data-lightbox]`
- 所有 6 张真实手稿图（含 4 张展品索引速览 + 2 张展区 2/3 主图 + 2 张展区 3 细读）都加齐 `data-lightbox` / `data-title` / `data-subtitle` / `data-credit` / `data-viewing`
- 三个旧 markers 完整保留 + 新增 `v2.2-exhibition-experience-upgrade`（meta 标签 + HTML 注释 + footer 文本三层）
- 桌面 1440 / 移动 390 双断点验证通过：路线 3 → 1 列、轻 timeline 等所有模块不溢出

**v2.2 报告**：`reports/leonardo_chinese_exhibition_v2_2_exhibition_experience_upgrade_report.md`

## v2.3 platform screenshot upgrade（消灭 placeholder）

v2.3 是展览本体补图版。把 v1.8 / v1.9 阶段残留的 3 个 `.image-placeholder-pro` 占位卡片**全部替换为真实平台截图**。

| 替换位置 | 原 placeholder | 现截图 | asset_path |
|---|---|---|---|
| 展区 5 · Watermarks | "Watermarks 界面截图" | Leonardo//thek@ 真实 filigrane 模块截图（full-page 1440×3180） | `assets/images/platform/platform-watermarks.jpg` (439 KB) |
| 展区 6 · Recompositions | "Recompositions 界面截图" | 真实 ricostruzioni 模块截图（full-page 1440×5749） | `assets/images/platform/platform-recompositions.jpg` (633 KB) |
| 展区 7 · 首页 | "首页 9 功能入口截图" | 真实 home 1440×900 截图 | `assets/images/platform/platform-home-leonardotheka.jpg` (147 KB) |

**额外下载 2 张备用平台截图**（不直接入 page，存入研究材料库）：

- `platform-comparative-study.jpg` (ricostruttore · 59 KB) — research-asset
- `platform-advanced-search.jpg` (ricerca · 122 KB) — research-asset

**实现方式**：

- 全部由 headless Chrome-for-Testing 1440 截屏工具链在 2026-07-06 一次性完成
- 截图目标：`teche.museogaliceo.it/leonardo/{home,filigrane,ricostruzioni,ricostruttore,ricerca}/index.html?lang=en`
- 全部 5 张截图都有完整 lightbox 元数据（`data-lightbox` / `data-title` / `data-subtitle` / `data-credit` / `data-viewing`）——和 v2.2 真实手稿图共用同一套 lightbox 机制
- 新增 CSS 块 `.platform-screenshot-card` / `.platform-screenshot-frame` / `.screenshot-frame` / `.source-entry-card`（fallback），与 v2.2 编辑式视觉风格一致
- 仅修改 `site/index.html` (57,478 → 60,473 字节 · +5%) + `site/style.css` (23,006 → 26,651 字节 · +16%) + 新增 5 张截图文件
- `research/image-candidates.md` 同步更新 B1-B7 状态：3 张 integrated、4 张 downloaded（2 张 research-asset + 2 张 not-needed-v2.3）

**核心数字**：

- placeholder-pro 卡片：**3 → 0**
- 新增本地图像：**5 张**（总 11 张 v1.8 + 5 张 v2.3 = 16 张本地资源）
- `data-lightbox` 目标数：**12 → 15**

**v2.3 报告**：`reports/leonardo_chinese_exhibition_v2_3_platform_screenshot_upgrade_report.md`

## v2.4 artifact annotation upgrade（看图导览 + 注释层）

v2.4 是"观众如何看展品"能力升级版。在不动展览主体（site/ 的 11 张图、5 张平台截图、9 个 SVG）的前提下，给展览加上 4 套教育性内容：

| 新增模块 | 位置 | 内容 |
|---|---|---|
| **如何看一张达·芬奇手稿？** | 展品索引后 · 展览地图前 | 4 步导览卡：先看整体结构 → 再看运动线索 → 再看材料证据 → 最后看连接关系。每张卡含标题 / 说明 / 对应展区 / 对应工具 |
| **展品注释层** | 4 个真实展品后 | 4 个 `.annotation-panel` 细读提示：Studies of water（A）· The muscles of the shoulder（B）· Cats, lions and a dragon（C）· Codex Atlanticus f.719（D）。每条含 3 个 annotation bullets + 「这说明什么」结语 |
| **平台界面说明** | 3 个 platform-screenshot-card 内 + 2 个研究界面档案 | 5 个 `.interface-note`：Watermarks · Recompositions · 首页（in-page）+ Comparative Study · Advanced Search（research-asset 档案）。每个含"这是什么 / 解决什么 / 看哪里 / 对应展区"4 字段 |
| **术语表 Glossary** | 资料来源前 | 14 个术语，2 列网格，desktop 1440 显示、移动 390 单列。覆盖 Codex Atlanticus · Royal Collection · Leonardo//thek@ · Foliations · Subject Indexes · Watermarks · Recompositions · Comparative Study · Advanced Search · Photographic Plates · Lexicon · Bibliography · Pompeo Leoni · Francesco Melzi |
| **Lightbox 观看提示增强** | lightbox-meta 内部 | 新增 `.lightbox-viewing-label` 标签（"观看提示"），把 data-viewing 内容用视觉上更明显的分隔线（border-top）与版权信息分开——让观众一眼看到"如何看" |

**实现细节**：

- 仅修改 `site/index.html` (60,473 → 77,045 字节 · +27%) + `site/style.css` (26,651 → 33,517 字节 · +26%) + `site/script.js` (6,664 → 6,670 字节 · viewing-label 标签替换)
- 新增 CSS 块：`.viewing-primer` / `.primer-card` / `.annotation-panel` / `.annotation-list` / `.interface-note` / `.glossary` / `.glossary-grid` / `.glossary-item` / `.lightbox-viewing-label`
- 移动 390 三组布局（primer / glossary / interface-rows）全部转单列，无横向溢出
- Lightbox 自动绑定新平台截图（JS 未改逻辑，只改了显示模板）

**核心数字**：

- 4 套新内容：viewing primer + 4 annotation panels + 5 interface notes + 14 glossary terms
- 6 markers (4 旧 + v2.2 + v2.3 + v2.4) — 全部保留
- `image-placeholder-pro` 仍 0
- data-lightbox 目标数：15（未变）
- Lightbox 关闭路径：ESC / × 按钮 / 点击背景 — 全部通过

**v2.4 报告**：`reports/leonardo_chinese_exhibition_v2_4_artifact_annotation_upgrade_report.md`

## GitHub Release

**v2.0 已在 GitHub Releases 发布**：<https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.0-public-portfolio-case>

附带了 6 张 Playwright 真实截图 + 1 份 asset manifest，全部为已上传状态。

**Release body 文件**：[`docs/GITHUB_RELEASE_v2.0.md`](docs/GITHUB_RELEASE_v2.0.md)（可作为 GitHub Release 页面文案复用）

**v2.6 Content Stable 已在 GitHub Releases 发布**：<https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.6-content-stable>

**Release body 文件**：[`docs/GITHUB_RELEASE_v2.6_CONTENT_STABLE.md`](docs/GITHUB_RELEASE_v2.6_CONTENT_STABLE.md)
**Release manifest**：[`release-assets/v2.6-content-stable-manifest.md`](release-assets/v2.6-content-stable-manifest.md)

## v2.1 release publishing kit

v2.1 是「发布收口」版本：在不改动展览本体和 case-study/ 的前提下，把 v2.0 整理成可在 GitHub Release / X / 作品集 / 个人站点直接复用的发布材料。

| 资产 | 用途 |
|---|---|
| `release-assets/screenshots/desktop-hero.png` | 1440×900 hero 主图，可作 GitHub Release top 缩图 + README 顶图 |
| `release-assets/screenshots/desktop-exhibit-index.png` | 1440×900 展品索引页截图 |
| `release-assets/screenshots/desktop-real-image-gallery.png` | 1440×900 真实手稿图像展区 |
| `release-assets/screenshots/desktop-platform-tools.png` | 1440×900 平台工具页截图 |
| `release-assets/screenshots/mobile-hero.png` | 390×844 mobile hero |
| `release-assets/screenshots/mobile-section.png` | 390×844 mobile section 截图 |
| `release-assets/manifest.md` | 全部截图用途 + 复用建议（README / Release / X / 作品集） |

**截图规格**：

- 全部 6 张由 Playwright + Chrome-for-Testing 149 通过 `headless=true` 从 live URL 抓取
- 桌面 1440×900 / 移动 390×844，与 README 设计网格一致
- 全部锚定到 `#hash` (`/`, `/` `#exhibit-index`, `/` `#section2`, `/` `#section7`) 确保取到正确 section
- 重新生成方法：`/tmp/pwtool/capture6.py`（约 30 秒）

**完整发布报告**：`reports/leonardo_chinese_exhibition_v2_1_release_publishing_kit_report.md`

### 关键里程碑

- v1.5b（`d69f516`）· live hotfix · marker 上线
- v1.5c（`53c4032`）· repo hygiene
- v1.6（`75fd9f9`）· distribution pack
- v1.7（`af07b15`）· exhibit image upgrade
- v1.8（`4f6d126`）· real image integration
- v1.9（`97f1670`）· final polish
- **v2.0（`ae946b3`）· public portfolio case → tag `v2.0-public-portfolio-case`**
- **v2.1（`9e6233a`-based）· release publishing kit + GitHub Release + 6 截图**
- **v2.2（`056125e`+）· exhibition experience upgrade: 参观路线 + 时间线 + lightbox + 展品细读 + 研究场景 + 展后总结**
- **v2.3（`e1ca01f`+）· platform screenshot upgrade: 5 张真实平台截图 + 3 placeholder-pro 归零**
- **v2.4（`988ebb9`+）· artifact annotation upgrade: viewing primer + 4 注释层 + 5 界面说明 + 14 术语表**

## v2.0 作品化（public portfolio case）

v2.0 是一个收口版本：把整个 v1.5 → v1.9 的工作流整理成可直接复用到个人作品集、个人主页、求职简历的 7 件文档。

| 文档 | 用途 |
|---|---|
| `case-study/portfolio-case-study.md` | 中文长篇案例（14 节 · 含背景 / 问题 / 方法 / IA / 视觉 / 图像系统 / 技术 / 版本演进 / 复用经验 / 后续路线） |
| `case-study/project-onepager.md` | 一页式项目说明（项目类型 / 关键词 / 解决问题 / 产出 / 技术栈 / 链接 / 亮点 5 条） |
| `case-study/portfolio-case-en.md` | 英文版短案例（适合国际作品集） |
| `case-study/readme-showcase-section.md` | README 顶部展示段（可直接拷贝） |
| `case-study/launch-x-post.md` | X 14 条中文长帖（发布用） |
| `case-study/project-retrospective.md` | 项目复盘（做对了什么 / 踩的坑 / v1.7-1.8 解决路径 / 对未来的启发） |
| `case-study/README.md` | case-study 目录导览 |

完整 v2.0 报告：`reports/leonardo_chinese_exhibition_v2_0_public_portfolio_case_report.md`

## 推荐阅读路径

如果你只有 5 秒：`case-study/project-onepager.md`

如果你只有 30 秒：`case-study/portfolio-case-en.md`（英文）或`case-study/readme-showcase-section.md`（中文 top-level）

如果你有 5 分钟：`case-study/portfolio-case-study.md`

如果你想看项目内幕：`case-study/project-retrospective.md`

## case-study/ 目录说明

`case-study/` 目录下所有文件均为**作品集展示**类内容，独立于展览本体（site/）。每份文档都自含目标读者、用途、可以如何引用。**与 posts/ 不同**：posts/ 是给读者的传播材料，case-study/ 是给雇主 / 合作方 / 学术同行 的展示材料。

## v1.9 最终展览 polish 与资产审计（final exhibition polish & asset reference audit）

v1.9 是真实图像集成后的收口版本。本版本聚焦"小修小补"，不重写任何内容。

完成的核心工作：

- 资产引用审计：6 张 JPG + 7 张 SVG + 2 张 favicon/og-cover 全部确认已在页面正确路径使用（除一张 `platform-structure.svg` 为 v0.3 保留资产，未被引用）；
- 补齐 `<link rel="icon">` 与 `og:image` 元数据，让 `assets/favicon.svg` 与 `assets/og-cover.svg` 这两个之前未挂载的资源上线；
- 修复 4 个温莎索引卡片的 `credit-line` 格式（从 `公共域 · Wikimedia Commons` 升级为 `公共域 · Wikimedia Commons · Leonardo da Vinci, Royal Collection Trust`），与展区 3 画廊卡片一致；
- 全 19/19 `<img>` 标签都有 alt text（0 missing）；
- 全 10/10 真实图像有统一格式的 credit-line（公共域 + 来源 + 馆藏）；
- 9 张 SVG figure 全部有 figcaption + source-note；
- 移动端 image-grid 单列布局已就绪；
- v1.5b / v1.7 / v1.8 三层 marker 完整保留。

完整 v1.9 报告：`reports/leonardo_chinese_exhibition_v1_9_final_exhibition_polish_report.md`

## v1.8 真实手稿图像集成（real image integration）

v1.8 解决了 v1.7 仍然只用原创 SVG 图解、缺乏真实手稿像素的问题。本版本：

- 从 Wikimedia Commons 公共域下载 6 张真实手稿图像：4 张温莎皇家收藏（RCIN 912310 / 912660 / 919003 / 912363）+ 2 张《大西洋手稿》（f.719 / f.21）
- 展品索引 4 张卡片（马 / 水 / 肩臂 / 猫龙）升级为 image-card，直接展示 RCIN 真实手稿像素
- 展区 2 增 2 张 Codex Atlanticus 代表页
- 展区 3 画廊完全真实化（4 张温莎手稿）
- section-5 / 6 / 7 各加 1 张 `.image-placeholder-pro` 截图候选卡（v1.9 待补）
- 修正 v1.7 报告中 SVG 数字计数不一致
- 修正 v1.7 报告里 3 个不准确的 RCIN 编号（912695→912310，919023→919003，912377→912363）
- 临时占位文案（"实际使用时请替换为真实手稿影像"）已彻底删除

完整 v1.8 报告：`reports/leonardo_chinese_exhibition_v1_8_real_image_integration_report.md`
图像资产说明：`site/assets/images/README.md`

## v1.7 展览图像升级（exhibit image upgrade）

v1.7 解决了"页面底部原来写着图片使用占位"的问题。本版本：

- 增加 4 个全新原创 SVG（collection-split / watermark-evidence-chain / recomposition-triptych / platform-tool-wall）+ 1 个升级版（manuscript-journey，从 ~1 KB 升级到 4 KB 的 editorial 风格）+ 2 个继承自 v0.3 的（thinking-map / platform-structure）。平台内容承担在 v1.7 之后由 `platform-tool-wall` 接替，page 不再引用 `platform-structure`。
- 增加"本展展品索引"section，8 张展品卡（A-H），进入页面即有"展览感"
- 8 个展区都升级为展品模块：每节必有 `figure` / `gallery` / 展品柜
- 温莎绘图以"展品卡 + RCIN 编号 + 外链"形式陈列，不直接嵌入第三方像素
- 平台 9 功能以"原创工具墙 + HTML 9 宫格"双层呈现
- 配色更克制：暖白 + 黑灰 + 古金 + 深绿；不再用黑底金字的视觉惯式

完整 v1.7 提交报告：`reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md`

## v1.6 传播包（distribution pack）

基于已上线的中文数字展览，一套可用于公众号、小红书、X、短视频和作品集展示的传播材料。

| 文件 | 用途 |
|---|---|
| `posts/wechat-longform.md` | 公众号长文（带章节、副标题、CTA） |
| `posts/x-thread.md` | X 14 条 thread |
| `posts/xiaohongshu.md` | 小红书图文稿（10 个标题 + 7 张图文卡片 + 互动钩子） |
| `posts/video-script-3min.md` | 3 分钟短视频口播稿（hook / 中段 / 结尾 CTA + 剪辑建议） |
| `posts/portfolio-case.md` | 作品集案例说明（项目背景 / 问题 / 方法 / 产出 / 技术 / 设计 / 反思） |
| `posts/title-options.md` | 标题库（公众号 10 + 小红书 10 + X 10 + 作品集 6 = 36 条） |

完整 v1.6 提交报告：`reports/leonardo_chinese_exhibition_v1_6_distribution_pack_report.md`

## posts/ 目录说明

`posts/` 目录下所有文件均为**散文 / 脚本 / 标题 / 卡片文案**类传播内容，不是展览本体。`site/index.html` 与 `site/style.css` 仍是线上展览页面的唯一来源。

发布时不要把 `posts/` 推到 GitHub Pages 的根（它属于仓库文档层，不会被 GitHub Pages 工作流加载）。

## 项目结构

```
.
├── site/                   # GitHub Pages 部署根（仅这一层被部署）
│   ├── index.html          # 中文展览主页（v1.5b-live-hotfix + v1.7-exhibit-image-upgrade marker）
│   ├── style.css
│   └── assets/
│       ├── diagrams/       # 6 个原创 SVG 图解（v1.7 升级与新增）
│       └── favicon.svg · og-cover.svg
├── posts/                  # v1.6 传播材料（公众号 / X / 小红书 / 视频 / 作品集 / 标题）
├── research/               # 学术背景资料 + image-candidates.md（v1.7 候选清单）
├── reports/                # 版本报告（v0.2 → v1.5c → v1.6 → v1.7）
├── docs/                   # DEPLOYMENT / GITHUB_PAGES / CLOUDFLARE / RELEASE_NOTES
├── exhibition/             # 策展脚本与计划
├── README.md
└── .github/workflows/pages.yml
```

## 本地预览命令
```bash
python3 -m http.server 8787 -d site
```

## 发布目录
site/

## 项目状态
v1.7 把页面从"文字型说明页"升级为"图文革新型数字展览"——8 个展区都有 figure / gallery / 图注 / source note / 展品卡。已不再用占位图的临时提示，外部展品用展品卡 + 外链的形式给出。移动端已专门适配（单列布局）。

v1.5b live hotfix marker 保留（meta + comment 两层）。
v1.6 distribution pack 6 个传播材料 + 36 标题保留。