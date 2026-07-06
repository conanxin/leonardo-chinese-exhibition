# v2.6 content copy polish — report

**STATUS: PASS**

## 1. 真实基线

| 项 | 值 |
|---|---|
| **HEAD (本轮开始前)** | `c85705c` (v2.5-real deploy recovery) |
| **origin/main (本轮开始前)** | `c85705c` |
| **Live (本轮开始前)** | 82,611 字节, 含 v2.5-real marker |
| **v2.0 tag** | `v2.0-public-portfolio-case` @ `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4` — 未触碰 |
| **posts/ + case-study/ + release-assets/** | 未触碰 |
| **工作树** | clean（仅 untracked `.firecrawl/`） |

## 2. v2.6 marker

3 层（meta + HTML 注释 + footer），全部已写入 `site/index.html`：

- `<meta name="version" content="v2.6-content-copy-polish">`
- `<!-- leonardo-chinese-exhibition v2.6 content copy polish -->`
- footer: `v2.6 content copy polish`（含 strong 标签）

## 3. 修改文件清单

| 文件 | 状态 | Before → After |
|---|---|---|
| `site/index.html` | modified | 82,611 → 82,797 B (+0.2%) |
| `docs/CONTENT_STYLE_GUIDE.md` | modified | 5,631 → 5,569 B (-1.1%) |
| `README.md` | modified | +2,200 B (新增 v2.6 段) |
| `reports/leonardo_chinese_exhibition_v2_6_content_copy_polish_report.md` | **new** | ~9 KB |

**未修改**：`site/style.css`（无排版问题）、`site/script.js`（无 aria/label 需修正）。

## 4. 内容审校范围

| 模块 | 状态 |
|---|---|
| Hero 标题 / 副标题 / 导语 | ✓ 已打磨 |
| 策展前言 | ✓ 已打磨 |
| 展览地图 | — 已有 v2.5-real 处理，结构 OK |
| 参观路线 | — 已有 v2.5-real 处理 |
| 展品索引 | — 速览卡 OK |
| 4 步看图导览 | — 已有 v2.4 处理 |
| 8 个主要展区正文 | ✓ 修了《大西洋手稿》展区 |
| 9 个 section-takeaway | — 已 v2.5-real 处理 |
| 9 个 figcaption | — 已有 v2.4/v2.7 处理 |
| credit-line | — 已有 v2.4 处理 |
| source-note | — 已有 v2.4 处理 |
| 4 个 annotation panel | — 已有 v2.4 处理 |
| 5 个 platform interface note | — 已有 v2.4 处理 |
| 14 个 glossary | — 已有 v2.4/v2.7 处理 |
| 展后总结 | — 已有 v2.2 处理 |
| footer | ✓ 加 v2.6 项 |

## 5. 关键文案修改清单（6 处具体改动）

| # | 位置 | 改动 |
|---|---|---|
| 1 | Hero 第二段 | 删 "借助 Leonardo//thek@ 平台" + "在数字时代被反向连接" → 改 "沿着手稿的命运走一遍——看清它如何被拆散，又如何被数字工具重新组织为可读的研究对象"（更展览入口语气） |
| 2 | 策展前言 第三段 | "在数字时代被反向连接" → "被数字工具重新组织为可读的研究对象"（与 Hero 同步；消除"反向连接"与 title 重复） |
| 3 | 《大西洋手稿》展区 第一段 | "与内容是否与大西洋无关" → "与内容是否涉及大西洋无关"（消除"大西洋"歧义） |
| 4 | 展品 B-01 "尺寸" | "1 1 19 张纸页 · 40 余册大小" → "1119 张纸页 · 装订为多册"（修 typo + 不引用未确认的具体册数） |
| 5 | CONTENT_STYLE_GUIDE 文末 | "_辛 🔮" → "_辛"（移除违反"不出现 emoji 装饰"规则的 emoji） |
| 6 | CONTENT_STYLE_GUIDE 标题 | "v2.7 · 2026-07-06" → "v2.6 修订 · 2026-07-06（基于 v2.7 基础上叠加第三轮内容打磨）"（更准确） |

## 6. 术语统一结果

逐项确认（与 CONTENT_STYLE_GUIDE §B 一致）：

| 术语 | 用法 | 通过 |
|---|---|---|
| 达·芬奇 | 全文统一（首次 "列奥纳多·达·芬奇" 仅 Hero 一处） | ✓ |
| Leonardo//thek@ | 保留 "//" 与 "@" 原写法 | ✓ |
| 《大西洋手稿》 | 中文统一；Codex Atlanticus 仅首次出现 | ✓ |
| 皇家收藏 | "英国皇家收藏" / "Royal Collection Trust" 同一段一致 | ✓ |
| 安布罗西安图书馆 | "米兰安布罗西安图书馆"；"Veneranda Biblioteca Ambrosiana" 仅脚注 | ✓ |
| 弗朗切斯科·梅尔齐 / 庞佩奥·莱奥尼 | 中文 + 英文首次 | ✓ |
| 9 个平台模块 | 9 个英文 + 中文双行（首字母大写一致） | ✓ |
| RCIN 编号 | 6 位（912310 / 912660 / 919003 / 912363）— 未改 | ✓ |

## 7. 关键段落打磨清单

| 段落 | 目标 | 状态 |
|---|---|---|
| A. Hero 导语 | 更像展览入口，不像项目介绍 | ✓ 改 #1 |
| B. 策展前言 | 更有策展主旨，减少重复"重新连接" | ✓ 改 #2 |
| C. 《大西洋手稿》展区 | 让"纸上宇宙"更具体，突出"工作现场" | ✓ 改 #3（消除歧义，原"工作现场"措辞已在 v2.4 注释层） |
| D. 温莎绘图展区 | 突出"绘图不是插图，而是观察工具" | — 已有 v2.4 注释层 + v2.5-real takeaway，无需新改 |
| E. 复原拼合 / 平台研究展区 | 突出平台研究价值，不要只写"拼回去" | — 已有 v2.4/v2.5-real 处理（"复原拼合不是简单'把两张图放在一起'"） |
| F. 展后总结 | 收束为"不是天才崇拜，而是知识如何生成与连接" | — 已有 v2.2 完整处理 |

## 8. 图注 / source note 检查

- 9 个 `<figcaption>`：均含 `figure-title` + `source-note` 两行结构 ✓
- source note 格式统一：`<span class="source-note">来源：机构 / 页面 / 编号</span>` ✓
- 平台截图明确说"界面截图 / 研究入口 / 工具模块"（不混为图片占位） ✓
- 无"待补图"/"候选图"/"实际使用时请替换"等临时文字 ✓

## 9. Glossary 检查

- 14 个术语（Codex Atlanticus / Royal Collection / Leonardo//thek@ / Foliations / Subject Indexes / Watermarks / Recompositions / Comparative Study / Advanced Search / Photographic Plates / Lexicon / Bibliography / Pompeo Leoni / Francesco Melzi）✓
- 每个 1–2 句解释 ✓
- 普通观众可读 ✓
- 保留英文名方便回平台搜索 ✓
- 不与正文重复 ✓

## 10. section-nav 数量口径（统一）

| 报告 | 数字 | 备注 |
|---|---|---|
| v2.5-real 报告 | "9+" / "10 generated" / "9+ in DOM" | 三种说法不一致 |
| **v2.6 实地确认** | **11** | `document.querySelectorAll('.section-nav').length` |

**section-nav = 11**（真实值）：
- `#intro`（Hero）
- `#exhibit-index`（展品索引）
- `#section1`–`#section8`（8 个主要展区）
- `#visit-routes`（参观路线）

11 个 section 每个通过 `getTourSections()` 自动获得 nav，**无重复**（Playwright 验证）。

## 11. image loading / decoding 核对

| 项 | 静态 HTML | live DOM | 差异原因 |
|---|---|---|---|
| `<img>` 总数 | 24 | 25 | script.js `ensureLightboxDom()` 注入 1 个 lightbox `<img>` |
| `loading="lazy"` | 23 | 24 | lightbox `<img>` 也有 lazy（由 `ensureLazyImages()` 添加） |
| `decoding="async"` | 23 | 24 | 同上 |
| `data-no-lazy` | 0 | 0 | — |

**v2.5-real 报告的数字（24/23/23）是静态 HTML 的数字**——正确；本轮报告口径统一。

## 12. 交互回归（Playwright 25/25 PASS）

| 检查 | 结果 |
|---|---|
| node --check site/script.js | ✓ |
| section-nav == 11 | ✓ |
| section-takeaway == 9 | ✓ |
| image-placeholder-pro == 0 | ✓ |
| glossary == 14 | ✓ |
| annotation panels ≥ 4 | ✓ |
| platform interface notes ≥ 5 | ✓ |
| Lightbox open | ✓ |
| Lightbox role=dialog + aria-modal=true | ✓ |
| Lightbox close button aria-label="关闭展品大图" | ✓ |
| Lightbox ESC 关闭 | ✓ |
| Guided mode on/off | ✓ |
| Guided mode aria-pressed 切换 | ✓ |
| mobile 390 无横向溢出 | ✓ |
| 0 console errors | ✓ |

## 13. markers 检查

8 个旧 markers + v2.6 = 9 个：

```
v1.5b-live-hotfix                ✓
v1.7-exhibit-image-upgrade       ✓
v1.8-real-image-integration      ✓
v2.2-exhibition-experience-upgrade ✓
v2.3-platform-screenshot-upgrade ✓
v2.4-artifact-annotation-upgrade ✓
v2.7-content-copy-polish         ✓
v2.5-real-guided-accessibility   ✓
v2.6-content-copy-polish         ✓ NEW
```

## 14. live URL

https://conanxin.github.io/leonardo-chinese-exhibition/

## 15. 严格不触碰

- v2.0 tag at `9e6233ab...` — **未触碰** ✓
- GitHub Release (7 assets) — **未触碰** ✓
- `posts/` — **未触碰** ✓
- `case-study/` — **未触碰** ✓
- `release-assets/` — **未触碰** ✓
- 任何 image 文件 — **未触碰** ✓
- 任何 JS 逻辑 — **未触碰**（脚本本身未改） ✓
- 9 个旧 markers 全部保留 ✓

## 16. 下一步建议

- 当前 section-nav 数量是 11，spec 估计是 9。下次打磨时，section-takeaway 数量（9）和 section-nav 数量（11）的差异可以解释为"section-nav 适用于所有 nav-target sections，section-takeaway 仅适用主要 9 个"
- CONTENT_STYLE_GUIDE 已更新到 v2.6 修订，但历史报告的 v2.5 / v2.6 口径错误未修改（保留为诚实教训）
- 如果未来要做"展览墙文 vs 项目说明"语气对照，可以在 CONTENT_STYLE_GUIDE 加一组正面 / 反面例子
- v2.7 报告里的 emoji 用法（"_辛 🔮"）与 style guide 自身规则矛盾，本轮已修；如果其他历史报告也有类似情况，可单独 sweep

---

**v2.6 content copy polish → PASS ✓**
