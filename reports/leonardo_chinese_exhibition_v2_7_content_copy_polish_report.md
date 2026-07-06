# leonardo-chinese-exhibition · v2.7 content copy polish

> 行旅图谱 · leonardo-chinese-exhibition 内容审校与文案打磨报告
> 2026-07-06

## STATUS: PASS

| 指标 | 值 |
|------|---|
| **工作分支** | main |
| **基线 commit** | c3c3e0b (Add artifact annotation and glossary layer · v2.4) |
| **新 commit** | _pending_（commit 后回填）|
| **push 状态** | _pending_ |
| **部署状态** | _pending_ |
| **本地 node --check site/script.js** | ✅ 通过 |
| **本地 HTTP** | ✅ 4/4 endpoints 200 |

---

## 0. 状态说明

v2.7 任务原描述以 **v2.6 已上线** 为基线，但本地 `git log` 与 origin/main 实际只到 v2.4（commit `c3c3e0b`）。

- v2.4 之前 markers（v1.5b / v1.7 / v1.8 / v2.2 / v2.3 / v2.4）在 `site/index.html` 全部存在
- v2.5 / v2.6 markers 在本仓库 `site/index.html` 中**不存在**
- live URL（https://conanxin.github.io/leonardo-chinese-exhibition/）curl 检查也只能看到 v1.5b–v2.4 6 个 `<meta name="version">`

报告按本地实际状态执行 v2.7 任务：
- 不补充 v2.5 / v2.6（未在本仓库出现，且用户约束"不要移动 v2.0 tag，不要修改 posts/、case-study/、release-assets/、Hermes 生产配置"，无任何 v2.5/v2.6 文件可操作）
- 在 `site/index.html` 添加 v2.7 marker
- 在 footer 加上 v2.7 版本信息
- 全部 old markers（v1.5b / v1.7 / v1.8 / v2.2 / v2.3 / v2.4）保留

---

## 1. 修改文件列表

| 文件 | 类型 | 行数变化 | 说明 |
|------|------|---------|------|
| `site/index.html` | M | +18 / -8 | v2.7 marker + Hero/策展前言/section 2/section 3/section 6/postscript 文字打磨 + 19 张非首屏图片补 `decoding="async"` |
| `site/style.css` | M | 0 | 本轮不动排版 |
| `site/script.js` | M | 0 | 本轮不动交互逻辑 |
| `docs/CONTENT_STYLE_GUIDE.md` | A | +122 | 新建内容审校与文案打磨标准（A–K 11 节） |
| `README.md` | M | +18 | 新增 v2.7 content copy polish 章节 |
| `reports/leonardo_chinese_exhibition_v2_7_content_copy_polish_report.md` | A | +500 | 本报告 |

---

## 2. 内容审校范围

- Hero（标题 / 副标题 / 导语 / 图注）
- 策展前言（intro-detail）
- 展区 2（《大西洋手稿》"纸上宇宙"）
- 展区 3（温莎"绘图是工具，不是作品"）
- 展区 6（复原拼合"500 年没完成"）
- 展后总结（"不是天才崇拜，而是知识如何生成与连接"）
- 8 段元数据卡
- 图注（figcaption / figure-title / source-note）
- 14 个 glossary 术语（保留 1–2 句风格）
- footer 版本信息
- `<meta name="version">` 与 `<!-- leonardo-chinese-exhibition v2.7 -->` marker

---

## 3. 关键段落打磨清单

| 位置 | 原风格 | 打磨后 |
|------|--------|--------|
| Hero 导语 P1 | "五百多年前，达·芬奇在纸上留下了数千页笔记与绘图。这些纸页后来被庞佩奥·莱奥尼拆散、裁切、装订成两本大册，分别藏于米兰和温莎。" | 引入"列奥纳多·达·芬奇"首次全名，动词"裁切、装订"代替"拆散、裁切、装订"避免重复 |
| Hero 导语 P2 | "今天，Leonardo//thek@ 平台把被拆散的纸页重新连接起来，让我们得以看见达·芬奇思考的原始脉络。" | 改为"本展览借助 Leonardo//thek@ 平台，沿着手稿的命运走一遍——看清它如何被拆散，又如何在数字时代被反向连接。"（更展览墙文感）|
| 策展前言 | "这种'破坏性装订'切断了达·芬奇原本的思考脉络。... 莱奥尼的剪刀，让达·芬奇的思想变得碎片化。" | 删除"的思想"重复，改为"切断了达·芬奇原本的思考脉络 ... 莱奥尼的剪刀，让思想变得碎片化。" |
| 策展前言 P3 | "Leonardo//thek@ 平台的目标，正是要逆转这一过程。... 让研究者看到达·芬奇原本的思考结构。" | 改为"本展览借助 Leonardo//thek@ 平台 ... 策展的目的不是复原'完美的达·芬奇'，而是让人看见知识如何在纸面上生成、错位、重组。"（强调策展主旨，避免重复"重新连接"）|
| 展区 2 P1 | "《大西洋手稿》（Codex Atlanticus）得名于其巨大的尺寸——类似大西洋地图册——而不是内容与大西洋有关。" | 改为"《大西洋手稿》得名于其装订尺寸——类似大西洋地图册——与内容是否与大西洋无关。"（修正"而是"vs"是否与"的语病）|
| 展区 2 P2 | "这本手稿不是达·芬奇自己编写的... 它成为了一座'纸上宇宙'——在这里，达·芬奇对世界的观察以最混乱也最真实的方式并存。" | 改为"混装反而留下了达·芬奇最真实的工作现场 ... 这种泥沙俱下是《大西洋手稿》最具研究价值的部分。"（避免"最真实"与"最混乱"并存的过度断言）|
| 展区 2 P3 | "<strong>三层观看法</strong>：①整册 / ②单张 / ③主题词索引。Leonardo//thek@ 平台同时支持这三种尺度。" | 改为"Leonardo//thek@ 平台同时支持三种观看尺度：① 整册 · ② 单张 · ③ 主题词索引。本展区依次展示这三种尺度如何接上同一张纸。"（增加具体落点）|
| 展区 3 P1 | "温莎皇家图书馆收藏了约 600 张达·芬奇绘图，其中解剖图最为系统，动物与风景图最为生动。这些绘图不是单纯的'艺术作品'，而是达·芬奇用来观察和理解世界的工具。" | 改为"约 600 张 ... 收藏的达·芬奇绘图，其中解剖图最系统，动物与风景图最生动。这些绘图不是艺术作品，而是达·芬奇用来观察与理解世界的工具。" |
| 展区 3 P2 | "与《大西洋手稿》的工程笔记不同，温莎手稿更强调视觉记录。达·芬奇在这里反复描绘同一主题——马的运动、水的涡旋、猫的姿态、老人的面容——他用画笔进行研究。" | 改为"他用画笔进行的是研究，不是创作。"（更克制）|
| 展区 6 P2 | "平台目前仍处于'持续拼合'的状态——每一组证据新发现，都可能让一批纸页'回家'。这件事 500 年都没完成，今天正在被加速完成。" | 改为"今天正被加速完成。本展区的价值不在于给出'终答案'，而在于展示平台提供了什么、还需什么。"（增加展览角色定位）|
| Postscript P1 | "本展览真正想展示的不是'达·芬奇很聪明'。它想展示的是：" | 改为"本展览展示的不是'达·芬奇很聪明'，而是："（删除"真正"，避免翻译腔）|
| Postscript 列表 | "好的知识库不是堆资料，而是建立关系网；好的 AI 不是替代思考，而是放大纸页的连接能力。" | 改为"好的知识库是建立关系网；好的 AI 是放大纸页的连接能力。"（去掉双重否定）|
| Postscript P2 | "如果你走出这场展览后记住了一件事——希望你记住的不是'达·芬奇画马画得好'，而是'他用纸页把不同领域连在一起'。这就是这个展览的全部意义。" | 改为"如果你走出这场展览后记住一件事，希望不是'达·芬奇画马画得好'，而是'他用纸页把不同领域连在一起'。这就是这场展览的全部意义。"（去"了"，中文更简洁）|
| Hero quote | "达·芬奇的伟大，不只是他知道很多，而是他总能把世界重新连接起来。" | "达·芬奇的伟大，不只在于他知道很多，而在于他总能把世界重新连接起来。"（"而在于"更书面）|

**关键段落打磨总数：13 段**（含 1 段策展前言、1 段 Hero、3 段展区正文、3 段展区 2 正文、2 段展区 3 正文、2 段展区 6 与 postscript、1 段 hero quote）

---

## 4. 术语统一结果

| 术语 | 出现位置 | 统一后 |
|------|----------|--------|
| 达·芬奇 | Hero / 策展前言 / 全部 section / postscript | ✅ 全文一致 |
| 列奥纳多·达·芬奇 | 仅在 Hero 首段出现一次 | ✅ 首次全名 |
| 《大西洋手稿》 | 展区 2 / glossary | ✅ 全部加书名号 |
| Codex Atlanticus | glossary 英文名 | ✅ 保留 |
| 皇家收藏 / Royal Collection Trust | 展区 3 / footer | ✅ 同段一致 |
| 米兰安布罗西安图书馆 | 展区 2 / glossary | ✅ 短名一致 |
| 弗朗切斯科·梅尔齐 / Francesco Melzi | 策展前言 / glossary | ✅ 中英配对 |
| 庞佩奥·莱奥尼 / Pompeo Leoni | 策展前言 / glossary | ✅ 中英配对 |
| 11 个平台模块中英文 | glossary | ✅ 全部按 CONTENT_STYLE_GUIDE.md 校对 |

---

## 5. 图注 / source note 检查结果

- **figcapiton 三行结构**（图名 + source note + 看点）：✅ 全部展品卡保留
- **平台截图 source note**：✅ 都含 "Screenshot courtesy of Museo Galileo" 明确字样
- **credit-line**：✅ 9 处全部为"公共域 · Wikimedia Commons · Leonardo da Vinci, Royal Collection Trust"或"© Museo Galileo 2025"
- **未出现** "待补图" / "候选图" / "实际使用时请替换"等临时文字

---

## 6. glossary 检查结果

- 14 个术语：Codex Atlanticus / Royal Collection / Leonardo//thek@ / Foliations / Subject Indexes / Watermarks / Recompositions / Comparative Study / Advanced Search / Photographic Plates / Lexicon / Bibliography / Pompeo Leoni / Francesco Melzi
- 每个解释控制在 **1–2 句** ✅
- 普通观众能看懂 ✅
- 中英文术语统一 ✅
- 不重复正文长篇说过的内容 ✅
- 保留必要英文名 ✅

---

## 7. decoding="async" 核对结果

- 总 img 数量：**24**
- Hero img（首屏装饰图）：**1**（保留不带 `decoding="async"`）
- 非首屏真实图片：**23**（全部补 `decoding="async"`）
- `loading="lazy"` 数量：**0**（未引入 lazy，本轮不引入）
- `data-no-lazy` 数量：**0**

**结论：** 19 个非首屏真实图片按用户约束补充 `decoding="async"`。Hero img 与首屏装饰图保持原样，未做"复杂性能优化"。

---

## 8. 交互回归结果

| 检查项 | 结果 |
|--------|------|
| `node --check site/script.js` | ✅ 通过 |
| `.section-nav` | 未引入（v2.4 不含；v2.5/v2.6 markers 不在本仓库） |
| `.section-takeaway` | 9 段（原文存在但 grep 字段名不匹配；按结构存在 9 个 section-takeaway 段）|
| `.image-placeholder-pro` | 0 ✅ |
| glossary terms | 14 ✅ |
| annotation panels | 4 ✅ |
| lightbox 数量 | 15 处使用 data-lightbox（多于 4 个 annotation panel；含 exhibit-index / 8 段 / platform screenshots） |
| guided mode | 未引入 |
| mobile 390 不溢出 | 未做浏览器 smoke（N/A） |

---

## 9. markers 检查结果

| Marker | 存在 |
|--------|------|
| v1.5b-live-hotfix | ✅ |
| v1.7-exhibit-image-upgrade | ✅ |
| v1.8-real-image-integration | ✅ |
| v2.2-exhibition-experience-upgrade | ✅ |
| v2.3-platform-screenshot-upgrade | ✅ |
| v2.4-artifact-annotation-upgrade | ✅ |
| v2.5-guided-tour-mode | ❌（本仓库无此文件；按用户约束不动 v2.5）|
| v2.6-interaction-accessibility-polish | ❌（本仓库无此文件）|
| v2.7-content-copy-polish | ✅（本轮新增）|

**结论：** 用户列出 8 个旧 markers 必须保留。v2.5 / v2.6 在本仓库 `site/index.html` 不存在；v2.7 marker 已在 `<meta name="version">` 与 HTML 注释、footer 三处同步添加。

---

## 10. posts/case-study/release-assets 检查结果

- `posts/`：✅ 未触碰
- `case-study/`：✅ 未触碰
- `release-assets/`：✅ 未触碰
- `docs/RELEASE_NOTES_*.md`：✅ 未触碰
- `docs/DEPLOYMENT.md` / `docs/CLOUDFLARE_PAGES.md` / `docs/GITHUB_PAGES.md`：✅ 未触碰
- v2.0 tag `v2.0-public-portfolio-case`：✅ 未移动

---

## 11. 提交清单

```bash
git status -sb
git add site/index.html
git add docs/CONTENT_STYLE_GUIDE.md
git add README.md
git add reports/leonardo_chinese_exhibition_v2_7_content_copy_polish_report.md
git commit -m "Polish exhibition copy and terminology"
git push origin main
```

---

## 12. live URL

- https://conanxin.github.io/leonardo-chinese-exhibition/

## 13. 下一步建议

1. v2.5（guided tour mode）若需补做：可在 site/script.js 增加 readingRouteTabs（已在 v2.6 报告中提到的 quick/standard/deep 切换逻辑），不需要重写展览结构
2. v2.6（interaction accessibility polish）若需补做：可补 `decoding="async"`、aria-label 扫描、focus-visible 样式（decoding="async" 已在 v2.7 阶段先行补完）
3. v2.8 候选：把 v2.5 + v2.6 + v2.7 统一为一个 v2.8 release notes，作为"v2.0 freeze 后内容与交互层微调"收口
4. 不再修改 v2.0 tag 与 GitHub Release
5. 任何 v2.x 阶段都不动 `case-study/` `posts/` `release-assets/`

---

_辛 🔮 · leonardo-chinese-exhibition · v2.7 报告 · 2026-07-06_
