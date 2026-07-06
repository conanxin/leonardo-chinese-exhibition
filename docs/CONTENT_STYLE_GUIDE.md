# CONTENT_STYLE_GUIDE

> 行旅图谱 · leonardo-chinese-exhibition 内容审校与文案打磨标准
> v2.6 修订 · 2026-07-06（基于 v2.7 基础上叠加第三轮内容打磨）
> 适用范围: site/index.html · 全部图注 / source note / credit-line / annotation panel / glossary / 段落正文

## A. 中文文案风格

- 清晰、克制、**展览墙文感**：像挂在展柜边的展签，而不是博客文章
- 不写营销语：不出现"震撼""神级""天才炸裂""封神""必看"等口语或情绪词
- 避免过度解释：尽量让图自己说话；图注是"补充说明"，不是"重写图像"
- 每段尽量 **80–180 字**：过长的段落需拆短；过短的需补一句"它为什么重要"
- 句式以陈述句为主：减少"是不是""会不会""或许"等推测式开头
- 标点：中文段落用全角标点（，。：；""、）；中英文之间保留一个半角空格
- 不出现 emoji 装饰（任何地方，包括文末署名）

## B. 术语统一

| 中文 | 英文 / 原名 | 备注 |
|------|------------|------|
| 列奥纳多·达·芬奇（首次）/ 达·芬奇（后续） | Leonardo da Vinci | 全文统一用「达·芬奇」 |
| Leonardo//thek@ | teche.museogalileo.it/leonardo | 保留 "//" 与 "@" 原写法 |
| 《大西洋手稿》 | Codex Atlanticus | 注意 "Atlanticus" 与大西洋无关（装订尺寸） |
| 英国皇家收藏（温莎） | Royal Collection Trust / Royal Collection | 同一段内主写法一致 |
| 米兰安布罗西安图书馆 | Veneranda Biblioteca Ambrosiana | 首次可写全名，后续用短名 |
| 弗朗切斯科·梅尔齐 | Francesco Melzi | 弟子 · 1519 年继承手稿 |
| 庞佩奥·莱奥尼 | Pompeo Leoni | 16 世纪末雕塑家 |
| 水印 | Watermarks | 纸的"指纹" |
| 复原拼合 | Recompositions | 平台核心模块 |
| 比较研究 | Comparative Study | 跨页并置 |
| 页码系统 | Foliations | 推测原笔记本页码 |
| 主题索引 | Subject Indexes | 跨页检索 |
| 摄影图版 | Photographic Plates | 6000+ 像素宽高分辨率扫描 |
| 词汇索引 | Lexicon | 解剖 / 植物 / 机械 / 几何 |
| 书目 | Bibliography | 已发表研究 |
| 高级检索 | Advanced Search | 多字段 SQL 查询 |

## C. 图注格式

统一为三行结构：

1. **图名 / 年代 / 馆藏或来源**（一句话）
2. **它展示了什么**（一句说明）
3. **为什么重要**（一句延伸）

```html
<figcaption>
  <span class="figure-title">图 X · 图名</span>
  <span class="source-note">来源：机构名 / 页面名 / 编号或模块名</span>
</figcaption>
```

## D. source note 格式

统一为：

```
来源：机构名 / 页面名 / 编号或模块名
```

例：
- 来源：Veneranda Biblioteca Ambrosiana · Codex Atlanticus · f.719 recto
- 来源：Royal Collection Trust · rct.uk/collection/912310
- 来源：Leonardo//thek@ · Recompositions 模块截图

## E. credit-line 格式

统一为：

```
公共域 · Wikimedia Commons · Leonardo da Vinci, Royal Collection Trust
© Museo Galileo 2025 · Screenshot courtesy of Museo Galileo / Leonardo//thek@
```

平台截图 credit 应明确「截图」字样，避免与手稿原图 credit 混淆。

## F. 展品卡格式

每张展品卡统一检查：

- 中文标题
- 英文原题（如有）
- 年代（如有）
- 馆藏 / 来源
- 看点
- 为什么重要
- source note
- credit line
- 外链（如有）
- 对应平台功能

## G. annotation panel 格式

每个 annotation panel 统一检查：

- `annotation-tag`：细读提示 · 展品 X
- `annotation-heading`：图名 · 这张图在画什么
- 3–5 条 `annotation-list`：逐点说明
- 1 条 `annotation-so-what`：它对接了哪个平台功能

## H. glossary 术语表打磨

- 14 个术语（Codex Atlanticus / Royal Collection / Leonardo//thek@ / Foliations / Subject Indexes / Watermarks / Recompositions / Comparative Study / Advanced Search / Photographic Plates / Lexicon / Bibliography / Pompeo Leoni / Francesco Melzi）
- 每个解释控制在 **1–2 句**
- 普通观众能看懂：避免学术腔（如"leonardesque"等生僻词）
- 中英文术语统一：与正文一致
- 不重复正文长篇说过的内容：只放一句话级别的注释
- 保留必要英文名：方便读者回到 Leonardo//thek@ 平台搜索

## I. 标点 / 空格 / 大小写

- 中文标点：，。：；""、——（破折号占两格）
- 中英文之间：保留一个半角空格（如"达·芬奇 的 1119 页"）
- Leonardo//thek@：不转义、不变形
- Codex Atlanticus：英文严格按此大小写
- Royal Collection Trust：英文严格按此大小写
- RCIN 编号：6 位数字（如 912310 / 912660 / 919003），不增减数字
- footer 版本信息：可读、版本号清晰、与 `<meta name="version">` 一致

## J. 事实与边界

- 达·芬奇 **1519 年去世**（这是事实基础）
- 手稿由 **弗朗切斯科·梅尔齐 继承**
- 庞佩奥·莱奥尼 **约 1580–1590 年** 获得手稿，进行破坏性装订
- 《大西洋手稿》含 **1119 张** 纸页（具体数字已锁定）
- 温莎皇家收藏约 **600 张** 达·芬奇绘图（具体数字已锁定）
- 《大西洋手稿》名称源于装订尺寸，与大西洋无关（不要混淆）

## K. 不允许

- ❌ 营销语 / 口语化情绪词
- ❌ emoji 装饰
- ❌ 未经确认的具体年份 / 数量 / 判断
- ❌ "待补图" / "候选图" / "实际使用时请替换"等临时文字
- ❌ 「震撼」「神级」「天才炸裂」等口语词
- ❌ 在新文案中擅自补充未确认事实

---

_辛 · leonardo-chinese-exhibition · 内容风格指南 · v2.6 修订 · 2026-07-06_
