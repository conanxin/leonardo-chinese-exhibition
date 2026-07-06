---
title: "v1.8 real image integration report"
project: leonardo-chinese-exhibition
version: v1.8
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
---

# Leonardo Chinese Exhibition — v1.8 real image integration 报告

报告生成时间：2026-07-06
项目目录：/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
**构建基线**：v1.5b live hotfix + v1.7 exhibit image upgrade + v1.8 distribution pack（v1.6）+ v1.5c repo hygiene
**目标**：把展览从"图解驱动"升级为"真实手稿图像 + 原创图解双驱动"

---

## 0. STATUS

**STATUS: PASS**

本版本从 Wikimedia Commons 公共域下载 6 张真实手稿图像，集成到展品索引与三个展区（展区 2 / 展区 3），并保留 SVG 图解与 3 张"截图候选"占位卡：

- 4 张温莎皇家收藏（RCIN）真实手稿
- 2 张《大西洋手稿》代表页（f.719 / f.21）
- 3 张升级版"image-placeholder-pro"卡片（section 5 Watermarks / section 6 Recompositions / section 7 首页）

| 检查项 | 结果 |
|---|---|
| 真实图像下载并集成 | ✓ 6 张 |
| 仍为 screenshot-needed | ✓ 3 张（B1 / B4 / B5）+ 4 张外链候选（A5-A8）+ 3 张 Codex 候选（C3-C5）|
| 8 个展区图像覆盖 | ✓ 全部覆盖（真实图像 + 原创 SVG + 截图候选 三层混合）|
| source note 完整性 | ✓ 6 张真实图像全部含 credit-line |
| v1.5b marker 保留 | ✓ |
| v1.7 marker 保留 | ✓ |
| v1.8 marker 新增 | ✓ meta + comment + footer 三层 |
| 图片路径 404 数 | ✓ 0 |
| 临时占位文案（"实际使用时请替换为真实手稿影像"） | ✓ 已删除 |
| 是否修改 Hermes 生产配置 / posts/ | ✗ 否 |

---

## 1. 修改 / 新增文件列表

| 类型 | 路径 | 字节 | 说明 |
|---|---|---|---|
| 修改 | `site/index.html` | 33 0 91 → 40 151 | 加入 v1.8 meta + comment + footer；更新 4 张 index 卡片为 image-card；更新 4 张 section-3 画廊卡片为 image-card（含真实 RCIN）；section-2 增 2 张 Codex 图像卡（B-02 / B-03）；section-5/6/7 各加 1 张 `image-placeholder-pro` 截图候选卡 |
| 修改 | `site/style.css` | 9 503 → 12 401 | 新增 `.artifact-card.image-card` / `.artifact-image` / `.image-grid` / `.credit-line` / `.image-placeholder-pro` / `.placeholder-tag` / `.collection-label` / `.source-link` + mobile media query |
| 修改 | `reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md` | 文字计数修正 | 6 SVG → 7 SVG（修正 v1.7 报告里的小计数字 |
| 修改 | `README.md` | 文字计数修正 | 同上 |
| 修改 | `research/image-candidates.md` | 9 7 56 → 13 331 | 21 项候选细化为完整的字段 schema：id / name / source_url / type / final_use / asset_path / source_page / credit_line / download_status / integration_status |
| 新增 | `site/assets/images/README.md` | 4 303 | 图像资产说明（命名 / 版权 / 集成位置 / 后续替换） |
| 新增 | `site/assets/images/royal-collection/royal-horse-studies-rcin-912310.jpg` | 612 KB | 温莎 · 马的研究 · c.1490 |
| 新增 | `site/assets/images/royal-collection/royal-water-studies-rcin-912660.jpg` | 903 KB | 温莎 · 水的研究 · c.1510-12 |
| 新增 | `site/assets/images/royal-collection/royal-shoulder-arm-rcin-919003.jpg` | 716 KB | 温莎 · 肩臂肌肉（verso）· c.1510-11 |
| 新增 | `site/assets/images/royal-collection/royal-cats-lions-dragon-rcin-912363.jpg` | 882 KB | 温莎 · 猫、狮子与龙 · c.1517-18 |
| 新增 | `site/assets/images/codex-atlanticus/codex-atlanticus-f719-recto.jpg` | 208 KB | 大西洋手稿 · f.719 正面 |
| 新增 | `site/assets/images/codex-atlanticus/codex-atlanticus-f21-recto.jpg` | 238 KB | 大西洋手稿 · f.21 正面 |
| 新增 | `reports/leonardo_chinese_exhibition_v1_8_real_image_integration_report.md` | — | 本报告 |

**总计**：6 个真实图像文件 + 2 个目录 (royal-collection / codex-atlanticus / platform) + 1 个 README + 4 个文件修改 + 1 报告新增 = **14 个 Git 操作单元**。

---

## 2. 真实图像清单（v1.8 已下载 / 已集成）

### 2.1 Royal Collection Trust 温莎手稿（公共域 · Wikimedia Commons）

| RCIN | 名称 | 年份 | 字节 | 对应位置 |
|---|---|---|---|---|
| 912310 | Studies of a horse | c.1490 | 612 KB | index card C · section-3 画廊 C |
| 912660 | Studies of water | c.1510-12 | 903 KB | index card D · section-3 画廊 D |
| 919003 | Verso: The muscles of the shoulder | c.1510-11 | 716 KB | index card E · section-3 画廊 E |
| 912363 | Cats, lions, and a dragon | c.1517-18 | 882 KB | index card F · section-3 画廊 F |

> 备注：v1.8 同时修正了 v1.7 报告中不准确的 RCIN 值（912695/919023/912377 是早期 API 检索时猜的近似值，正式注册号分别为 912310 / 919003 / 912363）。

### 2.2 Veneranda Biblioteca Ambrosiana · Codex Atlanticus

| folio | 名称 | 字节 | 对应位置 |
|---|---|---|---|
| f.719 recto | 机械 / 飞行相关页 | 208 KB | section-2 展品柜 B-02 |
| f.21 recto | 早期混合主题页 | 238 KB | section-2 展品柜 B-03 |

### 2.3 仍在 screenshot-needed 状态

| 候选 | 状态 | 原因 |
|---|---|---|
| B1 首页截图 | screenshot-needed | 未下载（平台截图合规风险 + 频率约束） |
| B4 Watermarks 截图 | screenshot-needed | 同上 |
| B5 Recompositions 截图 | screenshot-needed | 同上 |
| B2 Foliations | screenshot-needed | 同上 |
| B3 Subject Indexes | screenshot-needed | 同上 |
| B6 Comparative Study | screenshot-needed | 同上 |
| B7 Advanced Search | screenshot-needed | 同上 |
| A5 Tuscany map | not-used · pending | Wikidata 已查得源 URL · v1.9 可下载 |
| A6 Star-of-Bethlehem | not-used · pending | 同上 |
| A7 Leda | not-used · pending | 同上 |
| A8 Gun-barrels | not-used · pending | 同上 |
| C3 Codex f.117 | not-used · pending | Wikimedia 公共域 · v1.9 可下载 |
| C4 Codex f.272 verso | not-used · pending | 同上 |
| C5 Codex f.455 recto | not-used · pending | 同上 |

---

## 3. 展区图像覆盖情况

| # | 展区 | 真实图像 | 原创 SVG | 截图候选卡 | figure 数 |
|---|---|---|---|---|---|
| 序厅 | 一座被拆散的思想博物馆 | — | manuscript-journey | — | 1 |
| 1 | 纸页的命运 | — | collection-split | — | 1 |
| 2 | 《大西洋手稿》 | **2 张（f.719 + f.21）+ 1 张文本柜（B-01）** | manuscript-journey | — | 1 |
| 3 | 温莎的绘图 | **4 张（horse / water / shoulder / cats）+ 索引卡 4 张共用** | — | — | 0 (画廊改为真图) |
| 4 | 同一张纸上的艺术与科学 | — | thinking-map + comparison-strip | — | 1 |
| 5 | 水印与纸张 | — | watermark-evidence-chain | **✓ screenshot-needed（B4）** | 1 |
| 6 | 复原拼合 | — | recomposition-triptych | **✓ screenshot-needed（B5）** | 1 |
| 7 | Leonardo//thek@ 工具 | — | platform-tool-wall | **✓ screenshot-needed（B1）** | 1 |
| 8 | 达·芬奇方法 | — | thinking-map + method-cards | — | 1 |

**总计**：6 个 `<figure>`（v1.7 是 9 个，section-3 已改为 image-card 画廊不计 figure），6 张本地 JPG，3 张 image-placeholder-pro 截图候选卡。

---

## 4. source note / credit-line 完整性

每张已下载的真实图像都满足：

1. ✓ `<img>` 标签含 `alt`（描述内容 + 来源 + 中文图注）
2. ✓ 容器 `<figure class="artifact-image">` 含边框、底色
3. ✓ 卡片底部 `<span class="credit-line">` 含：作者、馆藏、年代、来源（Wikimedia Commons · 公共域）+ 项目页面
4. ✓ 卡片仍含 `.exhibit-meta` 字段：RCIN / folio / 原题 / 图注 / 看点 / 外链
5. ✓ 整个 section 末尾的 `<p class="source-note">` 给出总结

每张截图候选卡的 credit-line 含：
1. ✓ `placeholder-tag` 明确"Screenshot-need / v1.8 标记"
2. ✓ 候选编号（B1 / B4 / B5 等）
3. ✓ 替代资源链接到 `codex.codex.ie / teche.museogalileo.it`
4. ✓ 等待到 v1.9 的明确路径

---

## 5. CSS 升级（v1.8 新增组件）

| 类 | 作用 |
|---|---|
| `.artifact-card.image-card` | 展品卡 + 图像容器组合，6 行 grid 排版 |
| `.artifact-image` | 图像框架：暖白底 + 暖线边框 + 内容占比 1:1.25（手稿友好）|
| `.artifact-image img` | `aspect-ratio: 1/1.25` + `object-fit: contain` |
| `.image-grid` | 画廊 / 展柜用 grid 容器 |
| `.credit-line` | 单独使用的版权行（与 .image-card 内部使用）|
| `.image-placeholder-pro` | 截图候选卡片：金虚线边框 + 暖沙色底 + 内含 h4、p、code 提示 |
| `.placeholder-tag` | "SCREENSHOT-NEEDED" 标签 |
| `.collection-label` · `.source-link` | 收集标识 / 来源链接的小型副本 |
| `@media (max-width:720px)` 扩展 | 移动端 image-card 单列 |

---

## 6. 本地预览

```bash
cd /home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
python3 -m http.server 8787 -d site
```

健康检查（v1.8 实测）：

```
HTTP:200 BYTES:40151    # /
css HTTP:200 BYTES:12401
royal-collection/royal-horse-studies-rcin-912310.jpg    HTTP:200 BYTES:612429
royal-collection/royal-water-studies-rcin-912660.jpg    HTTP:200 BYTES:903041
royal-collection/royal-shoulder-arm-rcin-919003.jpg     HTTP:200 BYTES:716214
royal-collection/royal-cats-lions-dragon-rcin-912363.jpg HTTP:200 BYTES:882279
codex-atlanticus/codex-atlanticus-f719-recto.jpg         HTTP:200 BYTES:208676
codex-atlanticus/codex-atlanticus-f21-recto.jpg          HTTP:200 BYTES:238583
watermark-evidence-chain    HTTP:200
recomposition-triptych      HTTP:200
platform-tool-wall          HTTP:200
```

全部 200，零 404。

---

## 7. live URL

- 线上：https://conanxin.github.io/leonardo-chinese-exhibition/
- v1.5b marker 保留（meta + comment 双层）
- v1.7 marker 保留（meta + comment 双层）
- v1.8 marker 新增（meta + comment + footer 三层）

## 8. git 操作摘要

### 8.1 单次 commit / push（step 11 / 12）

```bash
git add \
  site/index.html \
  site/style.css \
  site/assets/images/README.md \
  site/assets/images/royal-collection/royal-horse-studies-rcin-912310.jpg \
  site/assets/images/royal-collection/royal-water-studies-rcin-912660.jpg \
  site/assets/images/royal-collection/royal-shoulder-arm-rcin-919003.jpg \
  site/assets/images/royal-collection/royal-cats-lions-dragon-rcin-912363.jpg \
  site/assets/images/codex-atlanticus/codex-atlanticus-f719-recto.jpg \
  site/assets/images/codex-atlanticus/codex-atlanticus-f21-recto.jpg \
  research/image-candidates.md \
  README.md \
  reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md \
  reports/leonardo_chinese_exhibition_v1_8_real_image_integration_report.md
git commit -m "Integrate real manuscript image candidates"
git push origin main
```

**不**使用 `git add .`。**不** amend。**不** `--force-with-lease`。

### 8.2 不写空 commit

本次变更均有真实内容 diff（6 图像 + 2 文件重写 + 报告新增 + CSS 增量等），**不存在**仅权限修复的空 commit。

---

## 9. 不触动项（遵循约束）

✓ posts/ 传播包（v1.6）**未触动**。
✓ `.github/workflows/pages.yml` **未触动**。
✓ Hermes 生产配置**未触动**。
✓ `.git/` **未触动**。
✓ 7 个 SVG 文件（manuscript-journey / collection-split / watermark-evidence-chain / recomposition-triptych / platform-tool-wall / thinking-map / platform-structure）**保留**。
✓ favicon.svg · og-cover.svg **保留**。
✓ 未扫描无关目录。

---

## 10. 下一步建议（v1.9+）

### 10.1 短期（v1.9）

- 下载 A5-A8（4 张温莎外链候选 → Wikimedia 公共域）+ 补到展区 4 "同一页艺术与科学"画廊
- 下载 C3-C5（3 张 Codex 候选页） → 补到展区 2 展品柜
- 手动截图 B1 / B4 / B5（3 张平台截图）→ 替换 3 张 `.image-placeholder-pro`

### 10.2 中期（v2.0+）

- 给页面增加 /zh-tw / /en 多语版本
- 给每张真实图像增加放大查看（点击进入 lightbox / `figure-zoom.js`）
- 整合 DOI / source URL 内嵌层

### 10.3 不建议

- 不要触碰 production 部署 workflow
- 不要引入 analytics / tracking
- 不要重写展览叙事（8 节结构稳定后再演化）

---

## 11. 一句话总结

**v1.8 PASS。** 本版本从 Wikimedia Commons 公共域下载 6 张真实手稿图像（4 张温莎 RCIN + 2 张 Codex Atlanticus），集成到展品索引 + section-2 展品柜 + section-3 画廊；保留 7 个图解型 SVG 作为补充层；同时在 section-5/6/7 加 3 张 image-placeholder-pro 卡片，标记 B1 / B4 / B5 平台截图为 v1.9 待补。Footer / meta / comment 三层 marker 全部按规范增补；旧占位文案已彻底清理。
