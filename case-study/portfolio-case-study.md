---
title: "作品集案例 · 达·芬奇的纸上宇宙——中文数字策展"
project: leonardo-chinese-exhibition
version: v2.0 (public portfolio case)
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
github_url: https://github.com/conanxin/leonardo-chinese-exhibition
audience: 作品集 / 个人网站 / 求职 / 学术合作
---

# 达·芬奇的纸上宇宙——一个独立中文数字策展案例

**一句话简介**：把意大利 Museo Galileo 的 Leonardo//thek@ 学术平台转译为中文受众的 8 节数字展览，含 6 张温莎皇家收藏与大西洋手稿的真实公共域手稿图像，全程静态网页 GitHub Pages 上线。

**Live URL**：https://conanxin.github.io/leonardo-chinese-exhibition/

---

## 一 · 项目背景

### 1.1 达·芬奇身后的真实遗产

大多数人想到达·芬奇，会先想起《蒙娜丽莎》《最后的晚餐》《维特鲁威人》。

但他留下的真正遗产不是这些油画——是**七千多页纸页**。这些纸页上有飞行器草图、心脏解剖、水力工程、光学实验、几何、日常账本，也有涂抹和涂鸦。它们原本装在几十本笔记里，由达·芬奇最忠诚的弟子弗朗切斯科·梅尔齐整理。

16 世纪末，意大利雕塑家庞佩奥·莱奥尼（Pompeo Leoni）拿到了所有手稿。他用剪刀把数千张纸裁开、混装、订成两本大册——一本藏于米兰安布罗西安图书馆，今天叫《大西洋手稿》（Codex Atlanticus），另一本后来进入英国皇家收藏，藏于温莎。

**这一剪，把达·芬奇原本的思考方式切碎了**。一整本笔记本里关于"光与影"的连续推理，被拆散到两册不同的"图书"里；一张关于飞行器的纸可能被裁成两半，一页关于心脏的笔记被贴到另一本手稿里。

莱奥尼的剪刀，决定了 500 年来人们对达·芬奇的扁平印象：觉得"他什么都懂一点，但很杂"。**没人意识到**：那种"杂"不是达·芬奇原本的样子，是装订方式塑造的。

### 1.2 Leonardo//thek@ 与三道门槛

意大利 Museo Galileo 推出了一个数字平台 **Leonardo//thek@**（`teche.museogalileo.it/leonardo`），试图反向拆散：

- 图像比对识别同一张纸的裁切碎片
- 水印分析判断纸张年代与产地
- 页码重建还原原始笔记本结构
- 虚拟复原把被拆散的纸页重新拼回去

但对中文读者有三道门槛：

1. **语言门槛**——网站意语 / 英语为主
2. **叙事门槛**——没有针对中文受众的策展叙事
3. **完整度门槛**——没有把"拆散—复原"讲成一个完整故事

**这个展览做的就是这件事**：把学术工具转译成中文受众可读的展览。

---

## 二 · 原始问题

如果你做了一个数字展览，你会同时撞到三类问题：

1. **学术翻译**：外文学术内容怎么"不油腻"地落地中文？
2. **展览工程**：怎么从"一篇长文"进化为"真实展览"？
3. **作品化**：怎么让独立项目变成可以放作品集、可以传播、可以被人引用的案例？

具体到这个项目，落地的难点是：

- **怎么把"被拆散的手稿如何重新连接"做成展览主线？**
- **怎么在不做大型博物馆、不直接侵权使用达·芬奇手稿的前提下，仍然让展览可信？**
- **怎么用纯静态网页（无后端、无数据库、无 CMS）做出博物馆级策展体感？**
- **怎么让一张 8 分钟读完的网页，既适合公众号长读，又适合小红书缩屏读？**

---

## 三 · 我的目标

把《达·芬奇的纸上宇宙》做成一个**完整、可信、可引用的独立数字策展案例**——

- **完整**：从学术背景到版本演进，每一步都可追溯
- **可信**：每张图、每条数据都标注来源、馆藏、授权方式
- **可引用**：版本号、报告、commit 全部可回到 GitHub 仓库

最终交付的不是一张网页，而是一个**完整工作流的标本**：数字研究平台 → 中文策展 → 图文展览 → 真实图像集成 → GitHub Pages 上线 → 传播包 → 作品化案例。

---

## 四 · 方法路径

### 4.1 转译 vs 重写

不是"翻译英文成中文"，而是**学术转译**——把意 / 英语学术内容转译为中文受众的策展叙事：

- 英文论文风格：reconstruct · disperse · watermark · compared studies
- 中文展览风格："复原被拆散的纸页"、"水印是手稿的指纹"、"让两张图并置比较"

**转译 ≠ 重写**。学术专有词（Leonardo//thek@ / Codex Atlanticus / RCIN）保留原形，因为它们是研究者关心的标识符；叙事则全部中文化。

### 4.2 单一主线 + 模块化

放弃"按时间线"或"按作品"的常规叙事——选择**单一主线 + 模块化**：

> "500 年前一个雕塑家用剪刀把达·芬奇的手稿拆开了，今天数字工具怎么把它们接回去？"

这条主线串起 8 个展区：

| 区 | 主题 | 核心问题 |
|---|---|---|
| 序厅 | 一座被拆散的思想博物馆 | 留下的是完整著作还是宇宙碎片？ |
| 1 | 纸页的命运 | 是谁拆的？为什么？ |
| 2 | 《大西洋手稿》 | 最大的纸上宇宙到底装了什么？ |
| 3 | 温莎的绘图 | 温莎手稿和大西洋有什么不同？ |
| 4 | 同一张纸上的艺术与科学 | 达·芬奇怎么在同一页做两件事？ |
| 5 | 水印与纸张 | 复原到底靠什么判断？ |
| 6 | 复原拼合 | 怎么把被拆散的页面接回去？ |
| 7 | 平台如何工作 | 数字工具到底怎么用？ |
| 8 | 达·芬奇方法 | 这个方法今天还能不能用？ |

每节都套用统一的四件套结构：`section-content + figure + meta-cards + viewing-guide`，便于阅读、不易疲劳。

### 4.3 双重可读性

**公众号长读 + 小红书缩屏读**——同一页 HTML 同时承担两类读者：

- 桌面端：每节 600-800 字，配套 figure / gallery / 展品卡 / source note
- 移动端：自动切换为单列布局，figure 优先 above-fold，文字可折叠

CSS 中 `@media (max-width:720px)` 处理一切移动适配，不依赖 JS。

---

## 五 · 信息架构

```
├── hero            # 标题 + 副标题 + 短叙事 + manuscript-journey.svg
├── blockquote      # 核心金句
├── exhibit-index   # 8 张展品卡（A-H）——首次访问即有"展览感"
├── exhibition-map  # 导航地图
├── intro           # 序厅：被拆散的思想博物馆
├── section1-8      # 8 个展区
├── sources         # 资料来源与延伸阅读
└── footer          # 致谢 + 版本标记
```

**核心 IA 决策**：

1. **展品索引先于展览地图**——避免"长文感"
2. **导航不沉到 footer**——顶部 nav 直接给 9 个跳转
3. **每节都有 figure / 展品卡**——避免"段落堆"
4. **显式 source page 链接在每节末**——而不是隐式藏在脚注

---

## 六 · 视觉设计

### 6.1 OpenAI editorial 风（v1.7 主轴）

参考 OpenAI 官网的展览式视觉：

- **暖白底** `#fbfaf6`
- **深灰文字** `#2a2a2a`
- **古金强调** `#9a7b3b`
- **深绿点缀** `#1f3a2e`
- **不规则边框** — 暖沙色 `#cfc8b8`
- **不卡通、不花哨、不回到黑底卡片**

字体：**PingFang SC + Helvetica Neue**。排版上：

- 大字号主标题（44-48px）
- 章回式编号（01 / 02 / ...）
- 章节之间留白（5-6 rem）
- 图注 + source-note 双层小字

### 6.2 编辑思维 vs 设计思维

> "传统展览第一反应是'设计海报'。但数字展览第一反应应该是'编辑内容'。"

每一节都是先想清楚"观众应该带走什么核心问题"，再设计视觉。视觉服务于内容，不反过来。

---

## 七 · 图像与展品系统

经历了**三个版本才做出真正的展览感**：

### v1.5 之前

只有 3 个最简单的 SVG 框图 + 文字。**像一篇排版好的博客文章，不像展览**。

### v1.7（exhibit image upgrade）

- 增加 4 个全新原创 SVG（collection-split / watermark-evidence-chain / recomposition-triptych / platform-tool-wall）+ 1 个升级版 manuscript-journey + 2 个继承自 v0.3
- 增加"本展展品索引"section，8 张展品卡（A-H）
- 8 个展区都升级为展品模块
- 移动端单列布局
- 删除了"实际使用时请替换为真实手稿影像"等临时占位文案

### v1.8（real image integration）

最大的一次质变：从 Wikimedia Commons **公共域** 下载 6 张真实手稿像素——

| 类别 | RCIN / folio | 内容 |
|---|---|---|
| 温莎皇家收藏 | RCIN 912310 | Studies of a horse · c.1490 |
| 温莎皇家收藏 | RCIN 912660 | Studies of water · c.1510-12 |
| 温莎皇家收藏 | RCIN 919003 | Verso: The muscles of the shoulder · c.1510-11 |
| 温莎皇家收藏 | RCIN 912363 | Cats, lions and a dragon · c.1517-18 |
| 大西洋手稿 | f.719 recto | 机械 / 飞行相关 |
| 大西洋手稿 | f.21 recto | 早期混合主题 |

每张都满足：

- ✓ `<img alt>` 中英文双语描述
- ✓ `<figure>` 容器带边框
- ✓ `.credit-line` 给出"公共域 + 来源 + 馆藏"
- ✓ 外链直指原馆藏页
- ✓ 配套 `folio` / `RCIN` / `c.1490` / `Wikimedia` 标识符

然后在 section-5/6/7 用 3 张 `.image-placeholder-pro` 占位卡标记 B1 / B4 / B5 三个平台截图候选，留给 v1.9/v2.0 补。

### v1.9（final polish）

最后一轮收口：

- 资产引用审计：6/6 JPG + 6/7 SVG + 2/2 favicon + og-cover 全部正确链接
- 补齐 `<link rel="icon">` 与 `og:image` 元数据
- 修复 4 个温莎索引卡片的 `credit-line` 格式一致性
- 19/19 `<img>` 都有 alt · 9/9 SVG figure 都有 figcaption + source-note
- 0 broken image path · 0 placeholder copy 残留

---

## 八 · 技术实现

| 层 | 选型 | 理由 |
|---|---|---|
| HTML | 静态 HTML 5 | 无需后端、无依赖 |
| CSS | 单纯 CSS · system fonts | 不引入 Tailwind / Bootstrap，保持极简 |
| 字体 | PingFang SC + Helvetica Neue + system fallback | 不引外部字体，避免 FOIT |
| 图像 | SVG（原创）+ JPG（Wikimedia Commons 公共域） | 控制版权风险 |
| 部署 | GitHub Pages + Actions | upload-pages-artifact@v3 + deploy-pages@v4 |
| 工作流 | `.github/workflows/pages.yml` | push main → 自动部署 |
| 域名 | `conanxin.github.io` | 已建立的个人站子路径 |
| Asset 大小 | index.html 40 KB · style.css 12 KB · SVG 总 24 KB · JPG 总 3.4 MB | 单页 3.6 MB |
| 版本化 | 4 个 layered marker | meta + comment + footer 三层冗余，可被 `curl grep` 验证 |

**全部页面 0 张位图、0 个外部 JS、0 个外部 CSS**。换言之，"它可以被任何 CDN、任何浏览器、任何屏幕大小、任何时间点读到。"

---

## 九 · 版本演进

| 版本 | 关键变更 | commit 关键 SHA |
|---|---|---|
| v0.2 | 视觉评审报告 | ... |
| v0.3 | 发布前最后整理 | ... |
| v1.0 | 首次公开发布 | ... |
| v1.1 - v1.4 | 多轮部署与 visual publish 验证 | ... |
| v1.5 | redesign to OpenAI editorial 风格 | ... |
| v1.5b | live hotfix · marker 上线 | `d69f516` |
| v1.5c | repo hygiene · 30 文件 chmod 0600→0644 | `53c4032` |
| v1.6 | distribution pack · 公众号/X/小红书/视频脚本/作品集/标题库 | `75fd9f9` |
| v1.7 | exhibit image upgrade · 4 新 SVG + 14 展品卡 | `af07b15` |
| v1.8 | real image integration · 6 真实公共域手稿图像 | `4f6d126` |
| v1.9 | final polish · 资产审计 + head meta + credit-line 一致 | `97f1670` |
| **v2.0** | **public portfolio case · 7 个 case-study 文档** | **本版本** |

**共 14 个版本报告**（reports/leonardo_*_v*.md），每步都有可追溯记录。

---

## 十 · 最终成果

- **线上展览**：https://conanxin.github.io/leonardo-chinese-exhibition/
- **GitHub 仓库**：https://github.com/conanxin/leonardo-chinese-exhibition
- **GitHub Actions**：deploy-pages-v4 自动化部署，已运行 10+ 次，均 success
- **6 张真实手稿图像** + 7 张原创 SVG 图解 + 8 节叙事 + 8 张展品索引卡
- **6 个传播材料** + 36 条标题
- **14 份版本报告** · 9 份审计报告
- **0 张位图、0 个外部 JS、0 个外部 CSS**

---

## 十一 · 可复用经验

### 11.1 给数字策展项目的方法

1. **先做完一个能用的版本，再扩展。** v1.0 不必"做完"，但必须有"可见的最低可验证形态"。
2. **marker 三层冗余**（meta + comment + footer）让每个版本都可被外部 grep 验证。
3. **报告与代码同仓**：reports/ 与 site/ 同步演进，让独立项目变"可追溯案例"。
4. **公开域优先**：Wiki Commons、V&A、Met Museum 公共域条目是学术展品图像的可靠来源。
5. **展品卡不是装饰**：每张展品卡至少要含 `exhibit-no / exhibit-title / exhibit-kind / exhibit-meta × 3 / credit-line`。

### 11.2 给"独立项目作品化"

1. **README 不只是入口**：把 README 当 portfolio index，写"项目结构 + 重点 deliverable + live URL"。
2. **posts/ 与 case-study/ 分开**：前者是给读者的传播材料，后者是给作品集/雇主/合作方的展示材料。
3. **每个版本都写报告**：报告不是事后补，是工作流的一部分。

### 11.3 给静态网页做数字展览

1. **SVG > 截图**：原创 SVG 是版权零风险 + 视觉可控 + 永久可读。
2. **图像 grid + aspect-ratio** 比"max-width: 100%"更可靠。
3. **平台截图谨慎**：除非明确授权，优先用 SVG 替代。

---

## 十二 · 后续路线

### 12.1 v2.0+

- 6 张温莎外链候选（A5-A8）+ 3 张 Codex 候选（C3-C5）→ 本地化 / 多 9 张真实手稿
- 3 个 screenshot-needed 卡（B1 / B4 / B5）→ 补为真实截图
- 转 webp 缩略版（GitHub Pages 原生支持）

### 12.2 v3.0+

- 多语版本（zh-tw / en）
- lightbox / 全屏查看图像
- DOI / source URL 内嵌

### 12.3 不建议

- 不要引入后端 / AI 助手（破坏静态架构）
- 不要引入 analytics（破坏隐私 / 简洁感）
- 不要改 production 部署 workflow

---

## 关键词

`digital humanities` · `中文策展` · `editorial design` · `Leonardo da Vinci` · `Codex Atlanticus` · `Royal Collection Trust` · `reverse engineering of historical manuscripts` · `static site` · `GitHub Pages` · `OpenAI editorial visual system` · `Wikimedia Commons` · `public-domain manuscripts`

---

**项目位置**：https://github.com/conanxin/leonardo-chinese-exhibition
**Live URL**：https://conanxin.github.io/leonardo-chinese-exhibition/
**最后更新**：2026-07-06
