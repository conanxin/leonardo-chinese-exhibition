# v2.4 Artifact Annotation Upgrade — Report

**项目**: leonardo-chinese-exhibition
**报告日期**: 2026-07-06
**base tag**: `v2.0-public-portfolio-case` (commit `9e6233a`)
**live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/

---

## STATUS: ✅ PASS

4 套新教育性内容（viewing primer · 4 注释层 · 5 界面说明 · 14 术语表）全部就绪。lightbox 增强验证通过。`image-placeholder-pro` 仍为 0。

---

## 1. 修改/新增文件清单

| 文件 | 状态 | 原大小 | 新大小 | 增量 |
|---|---|---:|---:|---:|
| `site/index.html` | 修改 | 60,473 | 77,045 | +16,572 (+27%) |
| `site/style.css` | 修改 | 26,651 | 33,517 | +6,866 (+26%) |
| `site/script.js` | 修改 | 6,664 | 6,670 | +6 (+0.1%) |
| `README.md` | 修改 | ~11,150 | ~12,200 | +~1 KB |
| `reports/leonardo_chinese_exhibition_v2_4_…` | **新增** | — | ~10 KB | +10 KB |

> 未触碰：`posts/` · `case-study/` · `release-assets/` · 6 张真实 JPG · 9 张 SVG · 5 张平台截图 · favicon / og-cover · 18 个历史 reports · v2.0 tag · v2.0 GitHub Release · `research/` · `exhibition/` · `.github/workflows/pages.yml`

---

## 2. viewing-primer 检查

| Step | 标题 | 内容要点 | 对应展区 | 对应工具 |
|---|---|---|---|---|
| 1 | 先看整体结构 | 图像 / 文字 / 空白 / 边缘 / 方向 | section2 · section3 | Photographic Plates · Lexicon |
| 2 | 再看运动线索 | 水流 / 肌肉 / 马 / 机械 | section3 · section4 | Subject Indexes |
| 3 | 再看材料证据 | 水印 / 纸张 / 裁切边 / 编号 / 馆藏 | section5 · section6 | Watermarks · Foliations |
| 4 | 最后看连接关系 | 与其他纸页 / 主题 / 平台工具的关系 | section6 · section7 | Recompositions · Comparative Study |

位置：展品索引（exhibit-index）之后、展览地图（exhibition-map）之前。

---

## 3. annotation panel 清单

| # | 关联展品 | 3 annotation bullets | 这说明什么 |
|---|---|---|---|
| A | Studies of water（RCIN 912660） | 障碍物周围的水流 · 下落水柱与气泡 · 波纹如何变成运动研究 | 达·芬奇用画图做"流体力学"；Subject Indexes 让跨页比较成为可能 |
| B | The muscles of the shoulder（RCIN 919003） | 肌肉层次 · 骨骼结构 · 身体作为机械系统 | 这是工程图不是艺术品；Lexicon 统一术语索引跨页检索 |
| C | Cats, lions and a dragon（RCIN 912363） | 连续姿态 · 生命观察 · 想象动物与真实动物的关系 | 晚年达·芬奇把动物当成"运动的几何形状"；Comparative Study 让跨馆藏并置 |
| D | Codex Atlanticus f.719 正面 | 文字 / 草图 / 工程结构共存 · 页面不是插图而是工作现场 · 同一张纸上多个主题并置 | 《大西洋手稿》不是一本书而是"被剪裁的纸页博物馆"；Watermarks + Recompositions 是反向拆散工具 |

每个 annotation-panel 的结构：

```html
<aside class="annotation-panel">
  <p class="annotation-tag">细读提示 · 展品 X</p>
  <h4 class="annotation-heading">...</h4>
  <ul class="annotation-list">
    <li><strong>...：</strong>...</li>  ← 3 bullets
  </ul>
  <p class="annotation-so-what">...这说明什么：...</p>  ← 自带"这说明什么"前缀
</aside>
```

---

## 4. 平台截图说明清单

| # | 类型 | 截图 | 4 字段 |
|---|---|---|---|
| 1 | in-page (section-5) | platform-watermarks.jpg | 这是什么 / 解决什么 / 看哪里 / 对应展区 → #section5 |
| 2 | in-page (section-6) | platform-recompositions.jpg | 这是什么 / 解决什么 / 看哪里 / 对应展区 → #section6 |
| 3 | in-page (section-7) | platform-home-leonardotheka.jpg | 这是什么 / 解决什么 / 看哪里 / 对应展区 → #section7 |
| 4 | research-asset | platform-comparative-study.jpg | 这是什么 / 解决什么 / 看哪里 / 对应展区 → #section4 |
| 5 | research-asset | platform-advanced-search.jpg | 这是什么 / 解决什么 / 看哪里 / 对应展区 → #section7 |

> research-asset (comparative-study, advanced-search) 的 interface-note 放在 home screenshot card 之后，因为 2 张图本身是 v2.3 标记的"备用"资源。interface-note 起到"研究档案"作用——告诉观众这些图存在、对应什么研究问题。

---

## 5. Glossary 术语（14 项）

| 术语 | 一句话定义 |
|---|---|
| Codex Atlanticus | 达·芬奇手稿最大合集，1119 页，藏米兰安布罗西安图书馆 |
| Royal Collection | 温莎城堡王室收藏，约 600 张达·芬奇手稿 |
| Leonardo//thek@ | Museo Galileo 运营的数字平台，本展览所有"平台截图"来源 |
| Foliations | 复原莱奥尼剪裁前的页码顺序 |
| Subject Indexes | 按主题（水/机械/解剖/几何）跨页检索 |
| Watermarks | 14–16 世纪造纸厂暗记，像纸的"指纹" |
| Recompositions | 平台最核心的"反向拆散"工具 |
| Comparative Study | 同一主题不同手稿左右并置 |
| Advanced Search | 按水印+纤维+时代+馆藏多字段检索 |
| Photographic Plates | 6000+ 像素宽的高分辨率扫描底图 |
| Lexicon | 解剖/植物/机械/几何词汇统一索引 |
| Bibliography | 达·芬奇研究文献库 |
| Pompeo Leoni | 16 世纪末"破坏性裁切与装订"实施者 |
| Francesco Melzi | 1519 年继承手稿的弟子 |

布局：desktop 1440 两列 grid / 移动 390 单列。

---

## 6. lightbox 增强

| 项 | 改动 |
|---|---|
| `.lightbox-viewing-label` 标签 | 新增 "观看提示" 棕色 uppercase label，border-top 与版权信息分隔 |
| `.lb-section-label` "如何观看" → `.lightbox-viewing-label` "观看提示" | 文案从"如何观看"改为"观看提示"，标签区分更清晰 |
| `data-viewing` 内容 | 5 段 v2.3 平台截图的 viewing 文字 + 4 段 v2.4 真实手稿 viewing 文字 — 全部经 `.lb-viewing` 显示 |
| ESC / × / backdrop 关闭 | 三种路径全部通过 Playwright 验证（无变更） |

---

## 7. local_check（Playwright 端到端）

执行：

```bash
cd site && python3 -m http.server 8911
# Playwright v24check.py → /tmp/v24run.log
```

| 检查 | 目标 | 结果 |
|---|---|---|
| `.image-placeholder-pro` | 0 | **0** ✓ |
| `.primer-card` | 4 | **4** ✓ |
| `.annotation-panel` | 4 | **4** ✓ |
| `.interface-note` | 5 | **5** ✓ |
| `.glossary-item` | ≥ 12 | **14** ✓ |
| `section.glossary` | 1 | **1** ✓ |
| 6 markers in body | 6/6 | **6/6** ✓ |
| `.version-footer` 含 v2.4 | yes | **yes** ✓ |
| Lightbox 平台图打开 | yes | **yes** (title="Watermarks · 水印目录") ✓ |
| **`.lightbox-viewing-label` 可见** | yes | **"观看提示"** ✓ |
| 增强 viewing 文本 | yes | "看第一列：每个水印..." ✓ |
| ESC 关闭 | yes | **yes** ✓ |
| × 按钮关闭 | yes | **yes** ✓ |
| backdrop 关闭 | yes | **yes** ✓ |
| Lightbox 真实手稿图（回归） | works | **works** ("Studies of a horse") ✓ |
| 移动 390: 4 primer cards | 4 | **4** ✓ |
| 移动 390: 14 glossary items | 14 | **14** ✓ |
| 移动 390: 4 annotation panels | 4 | **4** ✓ |
| 移动 390: 无横向溢出 | no | **no** (390=390) ✓ |
| Console errors / pageerrors | 0 | **0** ✓ |
| HTML tag balance | balanced | **balanced** (section 17/17, article 36/36, dl 5/5, dt 20/20, dd 20/20) ✓ |
| `node --check site/script.js` | OK | **OK** ✓ |

---

## 8. 严格 no-touch 自检

| 路径 | 状态 |
|---|---|
| `posts/` (6 传播 + title-options) | ✓ 未触碰 |
| `case-study/` (7 portfolio 文档) | ✓ 未触碰 |
| `release-assets/` (6 PNG + manifest) | ✓ 未触碰 |
| v2.0 tag `v2.0-public-portfolio-case` (→ `9e6233a`) | ✓ 未移动 |
| v2.0 GitHub Release (7 assets / 0.68 MiB) | ✓ 未修改 |
| `site/assets/images/royal-collection/` 4 张 JPG | ✓ 未触碰 |
| `site/assets/images/codex-atlanticus/` 2 张 JPG | ✓ 未触碰 |
| `site/assets/images/platform/` 5 张 JPG | ✓ 未触碰 |
| `site/assets/diagrams/` 9 张 SVG | ✓ 未触碰 |
| `site/assets/favicon.svg` · `og-cover.svg` | ✓ 未触碰 |
| `.github/workflows/pages.yml` | ✓ 未修改 |
| 19 个历史 reports | ✓ 未触碰 |
| `docs/RELEASE_NOTES_v2.0.md` · `GITHUB_RELEASE_v2.0.md` | ✓ 未触碰 |
| `research/image-candidates.md` | ✓ 未触碰（v2.3 已落地） |

---

## 9. 下一步建议（非本版本范围）

| 路线 | 触发条件 |
|---|---|
| v2.5 Lightbox 上一张/下一张导航 | 用户希望连续浏览 |
| v2.5 视频导览 (45–60s screencast) | 用户确认语音/TTS 选择 |
| v3.0 通用展览模板 | 用户希望复用工作流 |
| Annotation hotspots（坐标级热点） | 用户希望从"文字注释"升级到"图上点击" |

---

**结论**：v2.4 artifact annotation upgrade 完整闭环。

| 任务项 | 状态 |
|---|---|
| Status check | ✓ |
| v2.4 marker (3 layers) | ✓ |
| viewing primer (4 cards) | ✓ |
| annotation panels (4) | ✓ |
| interface notes (5) | ✓ |
| glossary (14 terms) | ✓ |
| lightbox viewing-label | ✓ |
| local_check (21 项) | ✓ all pass |
| posts/case-study/release-assets 未触碰 | ✓ |
| v2.0 tag 未动 | ✓ |

**v2.4 artifact annotation upgrade → PASS** ✓
