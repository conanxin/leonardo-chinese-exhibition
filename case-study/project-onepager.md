---
title: "一页式项目说明 · leonardo-chinese-exhibition"
project: leonardo-chinese-exhibition
version: v2.0 (one-pager)
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
---

# 项目一页式说明

**项目名称**：达·芬奇的纸上宇宙 · 中文数字策展（leonardo-chinese-exhibition）

**项目类型**：独立数字策展 / 数字人文 / 静态网页展览

**关键词**：digital humanities · 中文策展 · editorial design · GitHub Pages · Leonardo da Vinci · Codex Atlanticus · 公共域手稿图像 · OpenAI editorial 视觉系统

**Live URL**：

> https://conanxin.github.io/leonardo-chinese-exhibition/

---

## 解决的问题

把意大利 Museo Galileo 推出的达·芬奇手稿研究平台 **Leonardo//thek@** 的英文/意文内容，转译成**适合中文受众独立阅读的 8 节数字展览**——保留学术专有词（RCIN、Codex Atlanticus），但把叙事、提问、节标题、判断词全部中文化。

## 产出物

| 类别 | 数量 / 形式 |
|---|---|
| 线上中文展览 | 1 个静态 HTML 主页 + 9 个 SVG 图解 + 6 张真实手稿 JPG |
| 节数 | 8 节主线 + 1 节序厅 + 1 节展品索引 + 1 节展览地图 |
| 真实手稿图像 | 6 张（温莎皇家收藏 × 4 + 大西洋手稿 × 2）|
| 原创 SVG 图解 | 9 张（手稿流散路径 / 分藏图 / 水印证据链 / 复原三联图 / 平台工具墙 / 思考地图 等）|
| 传播材料 | 公众号长文 / X 14 条 thread / 小红书图文稿 / 短视频脚本 / 作品集说明 / 标题库 |
| 报告 | 14 份版本/审计报告（reports/）|

## 技术栈

- **HTML 5 + CSS 3 · 纯静态页**
- **系统字体栈**：PingFang SC + Helvetica Neue
- **图像**：SVG（原创） + JPEG（Wikimedia Commons 公共域）
- **部署**：GitHub Pages + Actions（upload-pages-artifact@v3 + deploy-pages@v4）
- **零后端 · 零 JS · 零外部 CSS · 零位图**
- **总页面 weight**：HTML 40 KB + CSS 12 KB + SVG 24 KB + JPG 3.4 MB ≈ 3.6 MB

## 链接

| 类型 | URL |
|---|---|
| Live Demo | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| GitHub 仓库 | https://github.com/conanxin/leonardo-chinese-exhibition |
| 平台 | https://teche.museogalileo.it/leonardo/ |
| 温莎皇家收藏 | https://www.rct.uk/collection/ |
| 安布罗西安图书馆 | https://www.ambrosiana.it/ |
| 设计风格参考 | OpenAI 官网（openai.com）|

---

## 亮点 5 条

> 适合直接放进作品集首页的"5 秒钟看完项目"清单。

1. **真实手稿图像 + 原创 SVG 双驱动**——不是只放示意图，也不是纯文字长文，而是把 6 张温莎/Codex 公共域手稿直接嵌进展品卡，配套自制 SVG 用于把"剪碎—复原"的判断链可视化。
2. **三层 marker 版本体系**——`v1.5b / v1.7 / v1.8` 在 `<meta>`、HTML 注释、footer 各留标记，可被外部 `curl + grep` 在任何时间点验证。这种"工程可见性"在数字人文类项目里很少见。
3. **每节四件套结构**：`section-content + figure + meta-cards + viewing-guide`——从 v1.7 起 8 节稳定复用，让 8 分钟读完的展览既不"长文化"也不"过密"。
4. **零外部依赖**——0 张位图、0 个外部 JS、0 个外部 CSS。整个展览可以被任意 CDN、任意浏览器、任意屏幕尺寸读到，且不依赖任何第三方可用性。
5. **14 份版本报告 + 9 份审计报告**——每一步修改都留报告。每张图像、每个 RCIN、每个授权链都可追溯。把"独立项目"做成"可引用的案例"。

---

**最后更新**：2026-07-06
