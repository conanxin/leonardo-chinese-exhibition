---
title: "作品集案例：达·芬奇的纸上宇宙——中文数字策展"
project: leonardo-chinese-exhibition
year: 2026
role: 策展 / 内容设计 / 视觉设计 / Web 开发
version: v1.6 distribution pack
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
github_url: https://github.com/conanxin/leonardo-chinese-exhibition
---

# 作品集案例 · 达·芬奇的纸上宇宙（中文数字策展）

---

## 一、项目背景

达·芬奇身后留下七千多页手稿，分布在米兰安布罗西安图书馆与英国皇家收藏。
这些手稿在 16 世纪被意大利雕塑家庞佩奥·莱奥尼"破坏性装订"——剪裁、混装、订成两本大册。
由此塑造了过去 500 年人们对达·芬奇的扁平印象。

意大利 Museo Galileo 推出了 **Leonardo//thek@** 数字平台，使用图像比对、水印分析、虚拟复原等技术反向重建原始笔记本结构。但该平台以意大利语 / 英语为主，对中文读者有三道门槛：

1. 语言门槛
2. 没有针对中文受众的策展叙事
3. 没有把"拆散—复原"讲成一个完整故事

**本项目**：以中文受众为目标，做一个独立的数字策展展览，把学术工具转译成可阅读的中文叙事。

## 二、问题

- 如何把"被拆散的手稿如何重新连接"做成展览主线？
- 如何为中文读者呈现**学术工具的研究价值**，而不是"蒙娜丽莎"的媚俗？
- 如何在不直接使用达·芬奇真迹影像（受版权 + 视觉媚俗影响）的前提下，让展览仍然可信？
- 如何在 **Web 静态页**上做出**博物馆级策展体感**？

## 三、方法

### 1. 重新结构化叙事

放弃按时间线或作品分类的常规博物馆叙事。
采用**单一主线 + 9 节模块**：

- 序厅：被拆散的思想博物馆
- 纸页的命运
- 《大西洋手稿》
- 温莎的绘图
- 同一张纸上的艺术与科学
- 水印与纸张证据
- 复原拼合
- 平台如何工作
- 达·芬奇方法在今天

每节用同样的结构卡片：
- **核心问题**：本节要解决什么
- **如何观看**：观众应该看哪些细节
- **平台对应功能**：Leonardo//thek@ 用什么工具回应

### 2. OpenAI-style editorial 视觉语言

- 大白底 + 深灰文字 + 单一暖色点缀
- 章节化 + 卡片化 + 大量留白
- **去掉**黑底金字 / 古典装饰 / 博物馆 logo 海报
- 强调"先读内容，再看视觉"

### 3. 没有图片也能做展览

- 使用结构图（手稿流散路径 / 平台架构 / 思考方法图）作为视觉锚点
- 不直接展示达·芬奇真迹影像，避免版权 + 媚俗
- 强化"纸页证据"的法证式叙事

### 4. 静态网页 + 学术规范

- 全站纯静态 HTML / CSS，可托管于 GitHub Pages
- 引用与标注按学术规范给出
- 每个版本（v1.0 → v1.6）都有 release report / audit report 可追溯

## 四、产出

| 类别 | 内容 |
|---|---|
| **展览网页** | 8 节中文数字展，约 8 分钟读完 |
| **3 个版本迭代** | v1.0（首版）→ v1.5（redesign）→ v1.5b live hotfix |
| **可追溯的报告链** | release / visual review / verification / hygiene audit 共 8+ 篇 |
| **完整 schema 工作流** | GitHub Pages Actions workflow 自动化部署 |
| **v1.6 传播包** | 公众号长文 / X 14 条 thread / 小红书图文 / 3 min 视频脚本 / 作品集说明 / 30+ 标题库 |

## 五、技术实现

| 技术 | 说明 |
|---|---|
| **HTML5 + CSS3** | 纯静态页，无 JS 框架负担 |
| **GitHub Pages + Actions** | upload-pages-artifact@v3 + deploy-pages@v4 自动化部署 |
| **SVG 矢量图** | 所有结构图均为 SVG，无外部图片资源依赖 |
| **Open Graph meta** | og-cover.svg 提供社交分享卡片 |
| **版本化 schema** | meta name="version" + HTML 注释 + footer 版本文字，三层冗余可追溯 |
| **可重现工作流** | 每次发布都留 `release report` + `verification report`，便于回滚 |

**页脚技术指标**：HTML 13KB / CSS 3.5KB / 8 SVG / 0 张位图 / 0 个外部 JS。

## 六、设计风格

> 关键词：**克制 / 编辑 / 章回 / 法证**

**不做的事**

- ✗ 黑底金字博物馆海报
- ✗ 小红书柔光卡贴
- ✗ 大段引文配古画背景
- ✗ 神化达·芬奇的浪漫叙事

**做**

- ✓ 大白底深灰字
- ✓ 章节 + 卡片
- ✓ 关键名词用粗体，正文用细字
- ✓ 大量留白
- ✓ 引用用 blockquote 独立呈现
- ✓ 结构图全部 SVG 矢量，可无损放大

## 七、最终链接

- **线上展览**：https://conanxin.github.io/leonardo-chinese-exhibition/
- **GitHub 仓库**：https://github.com/conanxin/leonardo-chinese-exhibition
- **版本**：v1.5b live hotfix（含 `v1.5c` repo hygiene audit + `v1.6` distribution pack）

## 八、复用价值

- **人文学科 × 数字工具**：可作为中文数字策展的范式参考
- **OpenAI-style editorial 静态网页**：可作为低成本、中高质量展览页范式
- **静态网站版本化发布**：可作为 GitHub Pages + Actions 部署的样例
- **AI-assisted 学术翻译**：把意 / 英语学术平台转译为中文受众的展陈叙事

## 九、反思

- 如果要给中文研究者进一步使用，可以加**注释层 / 引用层**（DOI、source URL 内嵌）
- 如果要做国际版本，要重做 sprite + 字体 fallback
- 视频版本（v1.6 短视频脚本）目前还是口播稿，可以补一支真实的 3 min 视频

---

**关键词**：数字策展、数字人文、中文展览、OpenAI editorial design、GitHub Pages 静态网站、人文学科可视化、Leonardo da Vinci
