---
title: "X 14 条发布长帖 · leonardo-chinese-exhibition"
project: leonardo-chinese-exhibition
version: v2.0 (X launch)
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
平台：X (Twitter)
条数：14
语言：中文
---

# X 14 条发布长帖

---

**1 / 14**

我用一年时间，做了一件挺小众的事——

把意大利 Museo Galileo 的一个达·芬奇手稿研究平台，
**完整翻译 + 重新策展**成一个中文 8 节数字展览。

里面还有 6 张真实的手稿像素。

📍 https://conanxin.github.io/leonardo-chinese-exhibition/

👇 thread

---

**2 / 14**

大多数人想到达·芬奇，会先想起《蒙娜丽莎》。

但他留下的真正遗产不是油画。
是七千多页纸。

这些纸上有飞行器、心脏解剖、水力、光学实验、几何、账本、涂鸦。

**它们不是"遗物"，是"思考"。**

---

**3 / 14**

16 世纪末，意大利雕塑家庞佩奥·莱奥尼拿到所有手稿。

他没有研究它们。
**他用剪刀把数千张纸裁开，混装，订成两本大册。**

一本藏米兰——今天的《大西洋手稿》。
另一本藏温莎——今天的温莎皇家收藏。

---

**4 / 14**

莱奥尼这一剪，做了三件事：

— 把同一笔记本的纸页强行打散
— 把不同笔记本的纸页混装到一起
— 让"看起来整齐"压过了"原本可读"

**结果**：我们过去 500 年以为达·芬奇"很杂"。
真相是：他的思考被剪碎了。

---

**5 / 14**

意大利人做了一个工具平台——Leonardo//thek@。
用图像比对、水印分析、虚拟复原反向拆散。

但对中文读者有三道门槛：
1. 语言（意/英语）
2. 没有叙事
3. 没有"完整故事"

**所以我做了这件事——把它做成中文 8 节展览。**

---

**6 / 14**

展览 8 节：

— 序厅：被拆散的思想博物馆
— 纸页的命运（怎么被拆的）
— 《大西洋手稿》（最大的纸上宇宙）
— 温莎的绘图（视觉研究）
— 同一页上的艺术与科学
— 水印与纸张（法证证据）
— 复原拼合（Recompositions）
— 平台如何工作（9 个工具）

---

**7 / 14**

我做了一个特殊的设计决定：

**所有真实手稿都从 Wikimedia Commons 公共域拿。**

不是因为节省精力，
而是因为版权与可引用性比"图像漂亮"更重要。

温莎皇家收藏 4 张：《马的研究》《水的研究》《肩臂肌肉》《猫狮子与龙》
大西洋手稿 2 张：f.719 / f.21

**每张都标注 RCIN、年代、原题、馆藏。**

---

**8 / 14**

但光有"图"不够。

我还画了 9 个原创 SVG 图解：

— 手稿流散路径
— 米兰/温莎分藏
— 水印证据链
— 复原三联图
— 平台 9 功能工具墙
— 思考方法循环
…

**SVG > 截图：** 版权零风险 + 视觉可控 + 永久可读。

---

**9 / 14**

整个展览的"工程可见性"：

— `<meta name="version">` 三个版本都写在里面
— HTML 注释同步
— footer 同步

意味着任何时候都可以 `curl + grep` 验证：

```
curl -L https://conanxin.github.io/leonardo-chinese-exhibition/ | grep v1.8
```

这种"被外部工程验证"是数字策展少见的。

---

**10 / 14**

形态上：

— 0 个外部 JS
— 0 个外部 CSS
— 0 张位图
— 9 张 SVG + 6 张 JPG
— HTML 40 KB + CSS 12 KB = 一屏全部缓存

**它可以被任何 CDN、任何浏览器、任何屏幕大小读到。**

不依赖任何第三方可用性。

---

**11 / 14**

8 节展览每节都有统一的"四件套"：

— section-content（叙事）
— figure（图）
— meta-cards（展品卡）
— viewing-guide（怎么看）

**避免"长文感"，也不"过密"。**

---

**12 / 14**

完整工作流：

1. v1.0 首发
2. v1.5 redesign 到 OpenAI editorial 风
3. v1.6 加了传播包（公众号/X/小红书/视频）
4. v1.7 把"图解"加进页面（5 个新 SVG）
5. v1.8 把 6 张真实手稿像素嵌进去
6. v1.9 做资产审计收口

**每一步都留 commit，每一步都留报告。**

---

**13 / 14**

如果你想看：

— 5 秒看完：README 顶部 highlight
— 30 秒看完：英文 portfolio-case-en
— 完整看：portfolio-case-study.md
— 项目复盘：project-retrospective.md

**这些都跟展览一起发布在 GitHub 上。**

— GitHub：https://github.com/conanxin/leonardo-chinese-exhibition
— Live：https://conanxin.github.io/leonardo-chinese-exhibition/

---

**14 / 14**

结尾送一句我自己反复想到的话：

> "好的知识库不是堆资料，而是建立关系。"

达·芬奇 500 年前就是这么写笔记的。
今天仍然成立。

— 中文展览：
📍 https://conanxin.github.io/leonardo-chinese-exhibition/

— 代码：
📍 https://github.com/conanxin/leonardo-chinese-exhibition

**fin. 转给一个学艺术史 / 学设计 / 做数字人文的朋友。**

---

*发帖节奏建议：每条之间停顿 30 秒以上，便于读者消化。*
