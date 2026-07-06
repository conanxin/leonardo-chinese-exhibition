# v2.2 Exhibition Experience Upgrade — Report

**项目**: leonardo-chinese-exhibition
**报告日期**: 2026-07-06
**base tag**: `v2.0-public-portfolio-case` (commit `9e6233a`)
**live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/

---

## STATUS: ✅ PASS

7 个新体验模块 + 原生 JS lightbox 全部就绪；v2.0 tag 未动；posts/ case-study/ GitHub Release 均未触碰。

---

## 1. 修改/新增文件清单

| 文件 | 状态 | 原大小 | 新大小 | 增量 |
|---|---|---:|---:|---:|
| `site/index.html` | 修改 | 40,516 | 57,478 | +16,962 (+41%) |
| `site/style.css` | 修改 | 12,401 | 23,006 | +10,605 (+85%) |
| `site/script.js` | **新增** | — | 6,664 | +6,664 |
| `README.md` | 修改 | ~9,170 | ~10,150 | ~+980 |
| `reports/leonardo_chinese_exhibition_v2_2_…` | **新增** | — | ~7 KB | +7 KB |

> Git 仓库其他文件全部未触碰，包括 `site/assets/images/*`（6 张 JPG）· `site/assets/diagrams/*`（9 张 SVG）· `site/assets/favicon.svg` · `site/assets/og-cover.svg` · `posts/*` · `case-study/*` · 旧的 17 个 reports · docs/GITHUB_RELEASE_v2.0.md · release-assets/* · v2.0 tag · v2.0 GitHub Release。

---

## 2. 新增体验模块（7 项）

### 2.1 「选择你的参观路线」模块

- **位置**: 展览地图（`<section class="exhibition-map">`）之后、序厅（`<!-- 序厅 -->`）之前
- **HTML**: `<section class="visit-routes" id="visit-routes">`
- **CSS**: `.visit-routes` · `.route-grid` (grid 3 列) · `.route-card` · `.route-name` · `.route-time` (chip 风格) · `.route-for` · `.route-stops` · `.route-cta`
- **3 张 route cards**:
  - **A · 5 分钟快速路线** — 展品索引 · 温莎绘图 · 复原拼合 · 达·芬奇方法 — CTA `#exhibit-index`
  - **B · 15 分钟深度路线** — 8 个展区完整阅读 — CTA `#intro-detail`
  - **C · 研究者路线** — 水印证据链 · 复原拼合 · 比较研究 · 平台工具 — CTA `#section5`

### 2.2 「一张纸页的五百年旅程」时间线

- **位置**: 展区 1 `<section id="section1">` 内、meta-cards 之后、`</section>` 之前
- **HTML**: `<ol class="timeline" id="timeline">` 内嵌 7 个 `<li class="timeline-item">`
- **CSS**: `.timeline` (vertical line via `::before`) · `.timeline-item` (年号徽章) · 圆点 via `::before`
- **7 节点**: 1519 梅尔齐继承 → 约 1580–1590 莱奥尼剪裁 → 17–18 世纪分藏 → 现代两大馆藏 → 2023 Leonardo//thek@ 1.0 → 2026 2.0 扩展整合温莎 → 今天中文展览
- **移动端**: `.timeline::before` 缩到 `left: 0.3rem`，节点圆点缩到 `1rem`

### 2.3 「展品细读」模块

- **位置**: 展区 3 `<section id="section3">` 内、`source-note` 之后
- **HTML**: `<h3 id="close-reading">如何细读一张达·芬奇手稿？</h3>` + `<div class="reading-cards">` 内 2 张 `<article class="reading-card">`
- **CSS**: `.reading-cards` (grid 2 列) · `.reading-card` · `.reading-image` · `.reading-image img` · `.reading-title` · `.reading-meta` · `ol.reading-steps` · `.reading-method`
- **2 张细读卡**:
  - **A · Studies of water (RCIN 912660)** — 先看涡旋头位置 → 再看重复绘制 → 最后理解"稳定图案"
  - **B · The muscles of the shoulder (RCIN 919003)** — 先看肩胛骨隆起 → 再看肌肉分配 → 最后理解"身体作为机器"
- 每张含「先看哪里 / 再看什么 / 最后理解什么」三步 + 「与达·芬奇方法的关系」总结

### 2.4 「强化展区 7 研究工作台」

- **位置**: 展区 7 工具墙（`.tool-wall`）之后、meta-cards 之后（保留原有 9 宫格）
- **HTML**: `<h3 id="research-scenarios">研究者如何使用 Leonardo//thek@？</h3>` + `<div class="research-scenarios">` 内 4 个 `<article class="scenario-card">`
- **CSS**: `.research-scenarios` (grid 2 列) · `.scenario-card` · `.scenario-q::before "问："` · `.scenario-tool::before` · `.scenario-out::before "得到："` · `.scenario-why::before "为什么："` (中文 chip prefix)
- **4 个 research scenarios**:
  1. 我想知道一张纸的原始编号 → Foliations
  2. 我想按主题进入手稿 → Subject Indexes
  3. 我想判断两张纸是否原本相连 → Watermarks + Recompositions
  4. 我想并排比较米兰与温莎的材料 → Comparative Study
- 平台 9 大工具完整保留在原 tool-wall，并新增提示语指向上述 4 场景

### 2.5 「展后总结」模块

- **位置**: 展区 8 `<section id="section8">` 之后、`<section class="sources">` 之前
- **HTML**: `<section class="postscript" id="postscript">` + lede + `<ul class="postscript-points">` 4 条要点
- **CSS**: `.postscript` (左侧棕色 accent border) · `.postscript-lede` · `ul.postscript-points` · 关键词加粗
- **4 条要点**:
  - 知识如何在纸上生成
  - 图像如何成为思考工具
  - 被拆散的材料如何被数字平台重新连接
  - 今天的知识库和 AI 工具如何借鉴这种连接方式
- 正文字数 ~310 字（符合 250–400 字要求）

### 2.6 Lightbox（展品细看）

- **原生 JS**: `site/script.js` — 零外部依赖
- **DOM 自动构建**: `<div class="lightbox">` 一次性创建并 append 到 `<body>`
- **触发器** (按优先级):
  1. `<img data-lightbox>`
  2. `.artifact-image > img`（6 张真实手稿图）
  3. `.reading-image > img`（2 张细读图）
- **关闭方式 (3 种,全部测试通过)**:
  - **ESC 键** — `document.addEventListener('keydown')`
  - **× 按钮** — `.close-lightbox` 的 click 监听
  - **点击背景** — `.lightbox` 自身 click 监听（区分 panel 与 backdrop）
- **附加**: `tabindex=0` `role=button` `aria-label` 键盘可达；`body.lb-open` 锁滚动；`.lightbox-panel` 桌面 2 列 / 移动 1 列

### 2.7 v2.2 markers（三层）

| 层 | 内容 |
|---|---|
| `meta name="version"` | `v2.2-exhibition-experience-upgrade`（追加到 v1.5b/v1.7/v1.8 之后） |
| HTML 注释 | `<!-- leonardo-chinese-exhibition v2.2 exhibition experience upgrade -->` |
| footer 文本 | `版本：v1.7 exhibit image upgrade / v1.8 real image integration / v2.2 exhibition experience upgrade` |

---

## 3. JS 实现

- **新增文件**: `site/script.js` (6,664 字节)
- **零外部依赖** — `node --check site/script.js` ✓
- **行为**:
  - `DOMContentLoaded` 触发 `wireLightbox()`
  - 自动收集所有 lightbox targets（去重 by `Set`）
  - 对每个 `<img>` 设置 `tabindex=0` / `role=button` / `aria-label`
  - click → 弹出 lightbox
  - Enter / Space 键 → 弹出 lightbox
  - 焦点移至关闭按钮（无障碍）
  - ESC → 关闭
  - backdrop click → 关闭（panel 内 click 不关闭）

---

## 4. local_check 报告（关键验证）

执行:

```bash
cd site && python3 -m http.server 8911
# Playwright v22check.py → /tmp/v22run.log
```

| 检查 | 结果 |
|---|---|
| 3 张 `.route-card` | ✓ count=3 |
| 7 个 `.timeline-item` (1519→今天) | ✓ count=7 |
| 2 张 `.reading-card` (water + shoulder) | ✓ count=2 |
| 4 张 `.scenario-card` | ✓ count=4 |
| 1 个 `.postscript` | ✓ count=1 |
| `<div class="lightbox">` 初始化 | ✓ |
| `p.version-footer` 包含 v2.2 | ✓ |
| **点击展览索引马图** → lightbox 打开 | ✓ aria-hidden='false' |
| lightbox title 正确（"Studies of a horse · 展品索引速览"） | ✓ |
| lightbox subtitle / credit / viewing 全部正确填充 | ✓ |
| **ESC 键** 关闭 lightbox | ✓ |
| **点击背景** 关闭 lightbox | ✓ |
| 点击 reading-card 图也能打开 lightbox（"Studies of water（水的涡旋）"） | ✓ |
| 移动 390 宽: route-grid 折叠为单列（`358px`） | ✓ |
| 移动 390 宽: timeline `::before` 左移到 `4.8px` | ✓ |
| Console errors | ✓ none |
| HTTP 200 on `/index.html` / `script.js` / `style.css` | ✓ |
| 19 张 `<img>` 全部 HTTP 200（含 6 张真实 JPG 612-903 KB） | ✓ |
| HTML tag balance：`section/article/div/figure/ol/ul/li` | ✓ 全 balanced |

---

## 5. live URL check (提交后)

提交后会等待 Pages workflow run 触发（v2.0 freeze 时已经确认 workflows 走 Actions 不是 legacy），再 curl 验证 v2.2 marker 上线。

预期结果:
```bash
curl -L https://conanxin.github.io/leonardo-chinese-exhibition/ | grep v2.2-exhibition-experience-upgrade
# → <meta name="version" content="v2.2-exhibition-experience-upgrade">
```

---

## 6. 严格 no-touch 自检

| 路径 | 状态 |
|---|---|
| `posts/` 全套 (6 传播 + title-options) | ✓ 未触碰 |
| `case-study/` 全套 (7 portfolio 文档) | ✓ 未触碰 |
| v2.0 tag `v2.0-public-portfolio-case` (指向 `9e6233a`) | ✓ 未移动 |
| v2.0 GitHub Release (7 assets) | ✓ 未修改 |
| `release-assets/` (6 PNG + manifest) | ✓ 未修改 |
| `site/assets/images/` 6 张真实 JPG | ✓ 未修改 |
| `site/assets/diagrams/` 9 张 SVG | ✓ 未修改 |
| `site/assets/favicon.svg` · `og-cover.svg` | ✓ 未修改 |
| `.github/workflows/pages.yml` | ✓ 未修改 |
| 历史 17 个 reports | ✓ 未修改 |
| `docs/RELEASE_NOTES_v2.0.md` · `GITHUB_RELEASE_v2.0.md` | ✓ 未修改 |
| `README.md` (v2.2 节段追加) | ✓ 仅 + 增量 |

---

## 7. 下一步建议（非本版本范围）

| 路线 | 触发条件 |
|---|---|
| v2.3 视频导览 (45–60s screencast) | 用户确认语音/TTS 选择 |
| v2.4 国际化 (英文版 lightbox metadata) | 用户确认双语策略 |
| v3.0 通用展览模板 | 用户希望复用工作流 |
| Lightbox 增强 (上一张/下一张导航) | 用户希望连续浏览 |

---

**结论**：v2.2 exhibition experience upgrade 完整闭环。

| 任务项 | 状态 |
|---|---|
| Status check | ✓ |
| v2.2 marker (三层) | ✓ |
| 5 大新模块 | ✓ |
| lightbox native JS | ✓ |
| 6 真实图 lightbox metadata | ✓ |
| 9 个 tool 完全保留 | ✓ |
| posts/case-study untouched | ✓ |
| local_check 全绿 | ✓ |
| README 更新 | ✓ |
| 报告 | ✓ 本文件 |

**v2.2 exhibition experience upgrade → PASS** ✓
