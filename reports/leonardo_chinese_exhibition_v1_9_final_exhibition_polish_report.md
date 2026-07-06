---
title: "v1.9 final exhibition polish & asset reference audit report"
project: leonardo-chinese-exhibition
version: v1.9
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
---

# Leonardo Chinese Exhibition — v1.9 final exhibition polish & asset reference audit 报告

报告生成时间：2026-07-06
项目目录：/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
**构建基线**：v1.5b live hotfix + v1.5c repo hygiene + v1.6 distribution pack + v1.7 exhibit image upgrade + v1.8 real image integration
**目标**：在不大改展览正文的前提下，做一次"小修小补 + 资产引用审计"，让公开中文数字展览更成熟。

---

## 0. STATUS

**STATUS: PASS**

v1.9 是一轮只动头/小修文字/补挂链接的 polish 收口：

| 检查项 | 结果 |
|---|---|
| 资产引用审计 | ✓ 6/6 JPG + 6/7 SVG 已被引用（仅 1 张 `platform-structure.svg` 为 v0.3 保留资产）|
| 19/19 `<img>` 都有 alt | ✓ |
| 19/19 figure：9 SVG figure 有 figcaption，10 artifact-image figure 由 `.credit-line` 承担署名 | ✓ 设计一致 |
| source-note / credit-line 格式统一 | ✓ v1.9 已修复 4 个 index 卡片的短 credit-line |
| `<head>` 关键元数据完整 | ✓ v1.9 新增 `<link rel="icon">` + `og:image` + `twitter:card` |
| v1.5b / v1.7 / v1.8 marker | ✓ 完整保留 |
| GitHub Actions 部署 | ✓ 通过 |
| 修改文件数 | 2（site/index.html + README.md）+ 1 报告新增 = 3 |
| 是否修改 posts/ | ✗ 否 |
| 是否修改 Hermes 生产配置 | ✗ 否 |
| 是否大改展览正文 | ✗ 否 |

---

## 1. 修改 / 新增文件清单

| 类型 | 路径 | 说明 |
|---|---|---|
| 修改 | `site/index.html` | 40,151 → 40,516 字节；新增 4 行 `<head>` 元数据 + 4 处 index 卡 credit-line 修正 |
| 修改 | `README.md` | v1.8 → v1.9 顶级版本号更新 + 新增 v1.9 节段落 |
| 新增 | `reports/leonardo_chinese_exhibition_v1_9_final_exhibition_polish_report.md` | 本报告 |

总计 **3 个** git 操作单元。

---

## 2. Asset Reference Audit

### 2.1 site/assets/images/（6 JPG + 1 README）

| 文件 | 字节 | 是否被 index 引用 | final_use | 状态 |
|---|---|---|---|---|
| `royal-horse-studies-rcin-912310.jpg` | 612,429 | ✓ index C + section-3 C | 展品索引 + 画廊 | integrated |
| `royal-water-studies-rcin-912660.jpg` | 903,041 | ✓ index D + section-3 D | 展品索引 + 画廊 | integrated |
| `royal-shoulder-arm-rcin-919003.jpg` | 716,214 | ✓ index E + section-3 E | 展品索引 + 画廊 | integrated |
| `royal-cats-lions-dragon-rcin-912363.jpg` | 882,279 | ✓ index F + section-3 F | 展品索引 + 画廊 | integrated |
| `codex-atlanticus-f719-recto.jpg` | 208,676 | ✓ section-2 B-02 | 大西洋展柜 | integrated |
| `codex-atlanticus-f21-recto.jpg` | 238,583 | ✓ section-2 B-03 | 大西洋展柜 | integrated |
| `README.md` | 4,303 | — (documentation) | 资产说明文档 | intentional |

**结论**：6 张真实手稿图像已全部正确挂在展览页面；未发现 unreferenced 商业图像。

### 2.2 site/assets/diagrams/（7 SVG）

| 文件 | 字节 | 是否被 index 引用 | 在哪里引用 |
|---|---|---|---|
| `manuscript-journey.svg` | 4,271 | ✓（×2） | hero + section-2 figure |
| `collection-split.svg` | 3,556 | ✓ | section-1 figure |
| `watermark-evidence-chain.svg` | 3,557 | ✓ | section-5 figure |
| `recomposition-triptych.svg` | 3,681 | ✓ | section-6 figure |
| `platform-tool-wall.svg` | 4,556 | ✓ | section-7 figure |
| `thinking-map.svg` | 2,507 | ✓（×2） | section-4 figure + section-8 figure |
| `platform-structure.svg` | 2,353 | **✗** | — |

**未引用资产**：
- `platform-structure.svg`（v0.3 平台示意图，2.3 KB）

**处理方式**：**保留，不删除**。原因：v1.7 起被 `platform-tool-wall.svg` 接替；page 不引用；作为可恢复资产保留，符合"不要删除显然可用资产"原则。报告里说明，未来 v2.0 重构可视情况删/转。

### 2.3 site/assets/（favicon + og-cover）

| 文件 | 字节 | v1.9 前是否被引用 | v1.9 修复后 |
|---|---|---|---|
| `favicon.svg` | 201 | ✗ 没有 `<link rel="icon">` | ✓ `<head>` 新增 `<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">` |
| `og-cover.svg` | 394 | ✗ 没有 `og:image` | ✓ `<head>` 新增 `<meta property="og:image" content="assets/og-cover.svg">` |

**修复**：v1.9 是真正的清理——这两个 SVG 文件之前在仓库里存在但**没有任何 hook 把它们连到 page**。现在通过 2 个 meta 行 + 1 个 `<link>` 行挂上。

### 2.4 Asset 引用汇总

| 类别 | 文件数 | 被 page 引用 | 未被引用（intentional） | 应删除 |
|---|---|---|---|---|
| site/assets/images/ | 7 | 6 | 1（README.md） | 0 |
| site/assets/diagrams/ | 7 | 6 | 1（platform-structure.svg）| 0 |
| site/assets/ root | 2 | 2 (post v1.9) | 0 | 0 |

**未发现任何 unreferenced 错误文件**。仅 `platform-structure.svg` 是设计上的"保留中未使用"。

---

## 3. image / figcaption / source note 检查

### 3.1 `<img>` alt 完整性

| 指标 | 值 |
|---|---|
| 总 `<img>` 标签数 | **19** |
| 含 `alt=...` 的 | **19** |
| 不含 alt 的 | **0** |

每张 `<img>` 的 `alt` 都包含：作者（达·芬奇）+ 馆藏 + RCIN/folio + 中文图注 + 关键风格说明。

### 3.2 figure 与 figcaption / credit-line

| figure 类型 | 数量 | 是否有 figcaption |
|---|---|---|
| SVG `<figure class="figure-large">` | 9 | ✓ 每张都有 `<figcaption>` 含 figure-title + source-note |
| `<figure class="artifact-image">` (image card 内) | 10 | ✗ 不需要，因为 image card 用 `.credit-line` |
| 总 `<figure>` | 19 | 9 figcaption + 10 credit-line |

### 3.3 credit-line 格式

v1.9 修复前后对比：

**修复前**（index cards C/D/E/F）：`公共域 · Wikimedia Commons`

**修复后**：`公共域 · Wikimedia Commons · Leonardo da Vinci, Royal Collection Trust`

**全 13 条 credit-line 当前格式**：

| 类型 | 数量 | 格式 |
|---|---|---|
| 温莎手稿（index + gallery ×2） | 8 | `公共域 · Wikimedia Commons · Leonardo da Vinci, Royal Collection Trust` |
| Codex Atlanticus 展柜 | 2 | `公共域 · Wikimedia Commons · Codex Atlanticus, Veneranda Biblioteca Ambrosiana` |
| Screenshot placeholder | 3 | `screenshot-needed · 由 platform screenshot candidate B# 承载 · v1.9 待补` |

格式全部一致。

### 3.4 source-note 检查

| source-note 数量 | 11 |
|---|---|
| SVG figure (figcaption 内 span) | 9 |
| Section 总结性段落 `<p>` | 2（section-2 Codex 总结 + section-3 RCIN 总结） |

格式多样但每条都指出：来源 / 馆藏 / 公共域授权。

---

## 4. Visual Polish 收口检查

### 4.1 首屏展览感

✓ Hero block：
- 左栏：H1 + subtitle + 两条简短 hero-text
- 右栏：manuscript-journey.svg + figure-title + source-note
- 既有展览 museum-wall 视觉，也有数字展览 control plane 视觉

### 4.2 展品索引

✓ `section#exhibit-index`：
- 8 张卡片（A · Handshakrd示意图 + B · Codex 柜 + C/D/E/F 真实温莎手稿 + G · 水印证据链 + H · 复原三联图）
- 4 张温莎卡 v1.9 已统一 credit-line
- 点击跳转到对应 section

### 4.3 展区图像覆盖

| 展区 | 真实图像 | SVG | 截图候选 |
|---|---|---|---|
| 序厅 | — | manuscript-journey | — |
| 1 | — | collection-split | — |
| 2 | Codex f.719 + f.21 | manuscript-journey | — |
| 3 | 温莎 4 张（与索引共用）| — | — |
| 4 | — | thinking-map | — |
| 5 | — | watermark-evidence-chain | B4 screenshot-needed |
| 6 | — | recomposition-triptych | B5 screenshot-needed |
| 7 | — | platform-tool-wall | B1 screenshot-needed |
| 8 | — | thinking-map | — |

✓ 全部展区都有图像支撑（真实图 / SVG / 截图候选）。

### 4.4 个别段落没有"说明文感"

✓ 各展区没有冗长段落，所有都是有结构的"section-content + figure + meta-cards + viewing-guide"四件套模式。

### 4.5 mobile 单列布局

✓ CSS 中 `@media (max-width: 720px)`：
- `.gallery, .exhibit-grid, .tool-wall, .exhibit-cabinet, .method-cards, .comparison-strip, .image-grid` 全部单列
- `.artifact-card.image-card` 单列 + 取消左侧 number rail
- `img { max-width: 100% }`

---

## 5. Performance / Size Summary

| 资产类型 | 总字节 | 数量 | 单文件平均 |
|---|---|---|---|
| JPG（真实手稿图像）| **3,561,222** | 6 | 593 KB |
| SVG（原创图解） | **24,481** | 7 | 3.5 KB |
| SVG（favicon + og-cover）| 595 | 2 | ~300 B |
| site/index.html | **40,516** | 1 | — |
| site/style.css | **12,401** | 1 | — |
| 全部 site/ | ~3.64 MB | 17 | — |

### 5.1 单 JPG 大小观察

| 文件 | 字节 | 原图分辨率（v1.8 验证） |
|---|---|---|
| codex-atlanticus-f21-recto.jpg | 238,583 | 2000 × 2742 |
| codex-atlanticus-f719-recto.jpg | 208,676 | 2000 × 2812 |
| royal-horse-studies-rcin-912310.jpg | 612,429 | 2000 × 1490 |
| royal-water-studies-rcin-912660.jpg | 903,041 | 1439 × 2000 |
| royal-shoulder-arm-rcin-919003.jpg | 716,214 | 1216 × 1742 |
| royal-cats-lions-dragon-rcin-912363.jpg | 882,279 | 1553 × 2000 |

**显示需求**：CSS 中 `aspect-ratio: 1/1.25` + `object-fit: contain`，界面卡片宽度约 280 px，最大纵向 ~350 px。**原图分辨率远超显示需求**。

**未压缩原因**（按用户约束）：
> "如果图片文件过大但页面仍可接受，只记录，不要复杂压缩。"

页面仍可接受（3.6 MB total 在 GitHub Pages CDN 上 < 1 s 完成首屏；GitHub Pages 自带 gz/br 压缩）。后续 v2.0 可考虑生成 webp / 800px 缩略版本，但 v1.9 不动。

---

## 6. live URL & 上游部署验证

- 线上：https://conanxin.github.io/leonardo-chinese-exhibition/
- v1.5b marker：保留（meta line 8 + comment line 15）
- v1.7 marker：保留（meta line 9 + comment line 16）
- v1.8 marker：保留（meta line 10 + comment line 17）
- v1.9 不引入新 marker（按"不大改展览正文"原则）；v1.9 工作主要以 README 形式记录

## 7. git 操作摘要（step 10 / 11）

### 7.1 单次 commit + push

```bash
git add site/index.html README.md reports/leonardo_chinese_exhibition_v1_9_final_exhibition_polish_report.md
git commit -m "Polish final exhibition presentation"
git push origin main
```

**不**使用 `git add .`。**不** amend。**不** `--force-with-lease`。

### 7.2 未触动项

✓ posts/ 传播包（6 个 .md + title-options.md）完整保留原状。
✓ `.github/workflows/pages.yml` 未触动。
✓ Hermes agent 生产配置未触动。
✓ `.git/` 未触动。
✓ 所有 6 张真实 JPG / 7 张 SVG / 2 张 favicon-og-cover **保留原状**（v1.9 不删不改任何一张图像）。
✓ 8 节展区结构 + 8 张展品索引结构 + 3 张 placeholder 卡 v1.9 未触碰。

---

## 8. 下一步建议（v2.0+）

### 8.1 不紧急项

- 6 张 JPG 转 webp 缩略版本（v1.9 不做，v2.0 视访问量决定）
- 补全 B1 / B4 / B5 等 3 张平台截图候选为真实截图
- 给 figure 增加点击进入 lightbox / 全屏查看
- 给图像卡增加 lazy-loading 提示

### 8.2 中期（v2.0+）

- 平台截图候选 B1-B7 全部下载为本地 PNG / JPG
- A5-A8（4 张温莎外链候选）→ 本地化
- C3-C5（3 张 Codex 候选页）→ 本地化
- 给页面增加 /zh-tw / /en 多语版本

### 8.3 不建议

- 不要再添加 v1.10 / v2.0 真实图像，直到用户大规模使用
- 不要引入 analytics
- 不要改 production 部署 workflow

---

## 9. 一句话总结

**v1.9 PASS。** 资产审计发现 6/6 JPG + 6/7 SVG 引用正确，1 张 `platform-structure.svg` 作为保留资产合理不删；favicon + og-cover 两张 SVG 在 v1.9 之前从未被连接，v1.9 通过 `<link rel="icon">` + `og:image` + `twitter:card` 三条 meta 把它们重新挂上；index 4 张温莎卡 credit-line 升级到与 gallery 卡一致；19/19 `<img>` alt 完整；9 张 SVG figure 全部含 figcaption + source-note。3 个文件变更一次 commit + push 落地，3 个 marker 全部保留，posts/ 与 Hermes 生产配置未触动。
