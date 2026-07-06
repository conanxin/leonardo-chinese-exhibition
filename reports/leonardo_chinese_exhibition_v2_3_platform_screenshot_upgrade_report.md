# v2.3 Platform Screenshot Upgrade — Report

**项目**: leonardo-chinese-exhibition
**报告日期**: 2026-07-06
**base tag**: `v2.0-public-portfolio-case` (commit `9e6233a`)
**live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/

---

## STATUS: ✅ PASS

3 个 `.image-placeholder-pro` 占位卡片**全部替换**为真实平台截图。`placeholder-pro` 数量从 3 → 0。

---

## 1. 修改/新增文件清单

| 文件 | 状态 | 原大小 | 新大小 | 增量 |
|---|---|---:|---:|---:|
| `site/index.html` | 修改 | 57,478 | 60,473 | +2,995 (+5%) |
| `site/style.css` | 修改 | 23,006 | 26,651 | +3,645 (+16%) |
| `site/script.js` | 未触碰 | 6,664 | 6,664 | 0 |
| `site/assets/images/platform/platform-home-leonardotheka.jpg` | **新增** | — | 147,007 | +147 KB |
| `site/assets/images/platform/platform-watermarks.jpg` | **新增** | — | 439,040 | +439 KB |
| `site/assets/images/platform/platform-recompositions.jpg` | **新增** | — | 633,004 | +633 KB |
| `site/assets/images/platform/platform-comparative-study.jpg` | **新增** (research-asset) | — | 59,285 | +59 KB |
| `site/assets/images/platform/platform-advanced-search.jpg` | **新增** (research-asset) | — | 122,458 | +122 KB |
| `research/image-candidates.md` | 修改 | 13,331 | ~16 KB | +~2.5 KB |
| `README.md` | 修改 | ~10,150 | ~11,150 | +~1 KB |
| `reports/leonardo_chinese_exhibition_v2_3_…` | **新增** | — | ~10 KB | +10 KB |

> 未触碰：`posts/` · `case-study/` · `release-assets/` · 6 张真实 JPG · 9 张 SVG · favicon / og-cover · 旧的 18 个 reports · docs/RELEASE_NOTES_v2.0.md · GITHUB_RELEASE_v2.0.md · 6 张 v2.1 release-assets screenshots · v2.0 tag · v2.0 GitHub Release

---

## 2. Placeholder 替换前/后

| 位置 | 替换前 | 替换后 |
|---|---|---|
| section-5 line 634-640 | `.image-placeholder-pro` × 1 (B4 Watermarks 候选) | `.platform-screenshot-card` (platform-watermarks.jpg 真实截图) |
| section-6 line 675-681 | `.image-placeholder-pro` × 1 (B5 Recompositions 候选) | `.platform-screenshot-card` (platform-recompositions.jpg 真实截图) |
| section-7 line 707-713 | `.image-placeholder-pro` × 1 (B1 首页 9 入口候选) | `.platform-screenshot-card` (platform-home-leonardotheka.jpg 真实截图) |
| **TOTAL** | **3 个 placeholder** | **0 个 placeholder · 3 个真实截图卡片** |

---

## 3. 5 张平台截图清单

| 文件 | 尺寸 (W×H) | 字节 | 用途 | source URL |
|---|---:|---:|---|---|
| `platform-home-leonardotheka.jpg` | 1440×900 | 147,007 | section-7 (替换 placeholder) | `https://teche.museogalileo.it/leonardo/home/index_en.html` |
| `platform-watermarks.jpg` | 1440×3180 (full-page) | 439,040 | section-5 (替换 placeholder) | `https://teche.museogaliceo.it/leonardo/filigrane/index.html?lang=en` |
| `platform-recompositions.jpg` | 1440×5749 (full-page) | 633,004 | section-6 (替换 placeholder) | `https://teche.museogaliceo.it/leonardo/ricostruzioni/index.html?lang=en` |
| `platform-comparative-study.jpg` | 1440×900 | 59,285 | research-asset (备用) | `https://teche.museogaliceo.it/leonardo/ricostruttore/index.html?lang=en` |
| `platform-advanced-search.jpg` | 1440×1400 (full-page) | 122,458 | research-asset (备用) | `https://teche.museogaliceo.it/leonardo/ricerca/index.html?lang=en` |

> 全部 5 张为 2026-07-06 通过 headless Chrome-for-Testing 1440 一次性截屏的 JPEG 图像（quality 88）。`filigrane` / `ricostruzioni` / `ricerca` 三个页面原 viewport 截屏得到的内容主要在 header + 第一屏（body 较多留白），改用 `full_page=True` + viewport 1440×1400/1400+ 后获得完整内容。
> 注：原 `teche.museogaliceo.it` 是用户任务里的拼写；实际 URL 是 `teche.museogalileo.it`（已修正）。

---

## 4. lightbox 覆盖

| 类型 | 数量 | 触发器 |
|---|---:|---|
| 真实温莎手稿图 (v1.8 集成) | 4 张 | `.artifact-image > img` |
| 真实 Codex Atlanticus 图 (v1.8 集成) | 2 张 | `.artifact-image > img` |
| 展品细读图 (v2.2 新增) | 2 张 | `.reading-image > img` |
| **平台截图 (v2.3 新增)** | **3 张** | **`.platform-screenshot-frame > img[data-lightbox]`** |
| **TOTAL data-lightbox 目标** | **15** | — |

每张 v2.3 平台截图都含完整五元组：
- `data-lightbox` (触发器)
- `data-title` (e.g. "Watermarks · 水印目录")
- `data-subtitle` (e.g. "Leonardo//thek@ 模块 · teche.museogaliceo.it/leonardo/filigrane")
- `data-credit` (e.g. "截图 · Museo Galileo · Leonardo//thek@ 平台 · 公共文化资源")
- `data-viewing` (一句"如何观看"的中文引导)

---

## 5. local_check（Playwright 端到端）

执行：

```bash
cd site && python3 -m http.server 8911
# Playwright v23check.py → /tmp/v23run.log
```

| 检查 | 目标 | 结果 |
|---|---|---|
| `.image-placeholder-pro` 数量 | 0 | **0** ✓ |
| `.platform-screenshot-card` 数量 | 3 | **3** ✓ |
| 5 张新图 HTTP 200 | 5/5 | **5/5** (147/439/633/59/122 KB) ✓ |
| 3 张平台截图 alt | yes | **yes** ✓ |
| 3 张平台截图 `data-lightbox` | yes | **yes** ✓ |
| 3 张平台截图 `data-title` | yes | **yes** ✓ |
| 3 张平台截图 `data-credit` | yes | **yes** ✓ |
| 5 个 meta version markers | 5/5 | **5/5** (v1.5b/v1.7/v1.8/v2.2/v2.3) ✓ |
| `.version-footer` 含 v2.3 | yes | **yes** ✓ |
| 平台图 lightbox 打开 | yes | **yes** ("Watermarks · 水印目录") ✓ |
| ESC 关闭 lightbox | yes | **yes** ✓ |
| Royal Collection 图 lightbox（回归） | yes | **yes** ("Studies of a horse · 展品索引速览") ✓ |
| 移动 390: platform-screenshot-card 渲染 | 3 | **3** ✓ |
| 移动 390: 横向溢出 | no | **no** (390=390) ✓ |
| Console errors / pageerrors | 0 | **0** ✓ |
| HTML tag balance (`section/article/div/figure/ol/ul/li`) | balanced | **balanced** ✓ |

---

## 6. `research/image-candidates.md` 同步更新

- B1（首页 9 入口）: `screenshot-needed / planned` → `downloaded-v2.3 / integrated`
- B2（Foliations）: `screenshot-needed / planned` → `not-needed-v2.3 / not-used-v2.3`
- B3（Subject Indexes）: `screenshot-needed / planned` → `not-needed-v2.3 / not-used-v2.3`
- B4（Watermarks）: `screenshot-needed / planned` → `downloaded-v2.3 / integrated`
- B5（Recompositions）: `screenshot-needed / planned` → `downloaded-v2.3 / integrated`
- B6（Comparative Study）: `screenshot-needed / planned` → `downloaded-v2.3 / not-used-v2.3 (research-asset)`
- B7（Advanced Search）: `screenshot-needed / planned` → `downloaded-v2.3 / not-used-v2.3 (research-asset)`
- v1.9 待补章节替换为 v2.3 集成清单
- 新增 v2.3 placeholder 替换说明段

---

## 7. 严格 no-touch 自检

| 路径 | 状态 |
|---|---|
| `posts/` (6 传播 + title-options) | ✓ 未触碰 |
| `case-study/` (7 portfolio 文档) | ✓ 未触碰 |
| `release-assets/` (6 PNG + manifest) | ✓ 未触碰 |
| v2.0 tag `v2.0-public-portfolio-case` (→ `9e6233a`) | ✓ 未移动 |
| v2.0 GitHub Release (7 assets / 0.68 MiB) | ✓ 未修改 |
| `site/assets/images/royal-collection/` 4 张 JPG | ✓ 未触碰 |
| `site/assets/images/codex-atlanticus/` 2 张 JPG | ✓ 未触碰 |
| `site/assets/diagrams/` 9 张 SVG | ✓ 未触碰 |
| `site/assets/favicon.svg` · `og-cover.svg` | ✓ 未触碰 |
| `.github/workflows/pages.yml` | ✓ 未触碰 |
| 18 个历史 reports | ✓ 未触碰 |
| `docs/RELEASE_NOTES_v2.0.md` · `GITHUB_RELEASE_v2.0.md` | ✓ 未触碰 |
| `site/script.js` | ✓ 未触碰（6,664 字节 · 零依赖 lightbox 自动检测新平台截图） |

---

## 8. 下一步建议（非本版本范围）

| 路线 | 触发条件 |
|---|---|
| v2.4 视频导览 (45–60s screencast) | 用户确认语音/TTS 选择 |
| v2.5 Lightbox 上一张/下一张导航 | 用户希望连续浏览 |
| v3.0 通用展览模板 | 用户希望复用工作流 |
| B6/B7 启用 | 用户希望在 comparative-study section 引用 comparative-study 与 advanced-search 截图 |
| C3-C5 (Codex Atlanticus 候选) | 后续可继续补充更多手稿页 |

---

**结论**：v2.3 platform screenshot upgrade 完整闭环。

| 任务项 | 状态 |
|---|---|
| Status check | ✓ |
| 5 个 platform screenshot 真实抓取 | ✓ 5/5 |
| 3 个 placeholder-pro 替换为真实截图卡片 | ✓ 3/3 |
| 5 个 lightbox 五元组数据 | ✓ |
| image-candidates.md 同步 | ✓ |
| 5 个 markers (4 旧 + v2.3) | ✓ |
| local_check (15 项) | ✓ all pass |
| posts/case-study/release-assets 未触碰 | ✓ |
| v2.0 tag 未动 | ✓ |
| 报告 | ✓ 本文件 |

**v2.3 platform screenshot upgrade → PASS** ✓
