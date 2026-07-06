---
title: "README 顶部展示段 · leonardo-chinese-exhibition"
project: leonardo-chinese-exhibition
version: v2.0 (showcase section)
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
note: 可直接粘贴进项目 README 顶部
---

# README 顶部展示段

> 复制下面的整块 Markdown 到个人 GitHub 项目 README 的最顶端即可。

---

````markdown
# 达·芬奇的纸上宇宙 · 中文数字策展

> 一个独立的中文数字策展案例：把意大利 Museo Galileo 的 Leonardo//thek@ 学术平台转译为中文受众的 8 节数字展览，含 6 张温莎皇家收藏与大西洋手稿的真实公共域手稿图像，全程静态网页 GitHub Pages 上线。

## 📍 Live Demo

**https://conanxin.github.io/leonardo-chinese-exhibition/**

8 分钟读完 · 中文 · 移动端适配 · 0 外部依赖

## ✨ Highlights

- **真实手稿图像**：温莎皇家收藏（RCIN 912310 / 912660 / 919003 / 912363）+ 《大西洋手稿》f.719 / f.21 — 6 张全部为公共域授权使用
- **原创 SVG 图解**：9 张自制 editorial 矢量图，复原拼合、水印证据链、手稿流散路径等
- **三层 marker 版本体系**：`v1.5b-live-hotfix`、`v1.7-exhibit-image-upgrade`、`v1.8-real-image-integration` 在 `<meta>`、HTML 注释、footer 三处保留，可被 `curl + grep` 在任意时间点验证
- **每节四件套结构**：`section-content + figure + meta-cards + viewing-guide`，8 节稳定复用
- **零外部依赖**：0 个 JS / 0 个外部 CSS / 0 张位图，3.6 MB 总量

## 🪜 What changed from v0.1 to v1.9

| 版本 | 关键 | commit |
|---|---|---|
| v0.2 | 视觉评审 | — |
| v0.3 | 发布前最后整理 | — |
| v1.0 | 首次公开发布 | — |
| v1.5 | redesign 到 OpenAI editorial 风格 | — |
| v1.5b | live hotfix · marker 上线 | `d69f516` |
| v1.5c | repo hygiene · 30 文件 chmod | `53c4032` |
| v1.6 | distribution pack（公众号/X/小红书/视频/标题库）| `75fd9f9` |
| v1.7 | exhibit image upgrade · 4 个原创 SVG | `af07b15` |
| v1.8 | real image integration · 6 张公共域手稿 | `4f6d126` |
| v1.9 | final polish · 资产审计 | `97f1670` |
| v2.0 | public portfolio case · 本 README 顶部段 | — |

## 🔗 Links

- **Live**：https://conanxin.github.io/leonardo-chinese-exhibition/
- **GitHub**：https://github.com/conanxin/leonardo-chinese-exhibition
- **平台**：https://teche.museogalileo.it/leonardo/
- **温莎皇家收藏**：https://www.rct.uk/collection/
- **安布罗西安图书馆**：https://www.ambrosiana.it/
- **设计风格参考**：OpenAI editorial 系统

## 🏛 完整案例文档

详细案例见 `case-study/portfolio-case-study.md`（中文长篇）、`case-study/project-onepager.md`（一页式）、`case-study/portfolio-case-en.md`（英文版）。

14 份版本演进报告见 `reports/`。

## 📜 授权

- **代码层**：MIT / 自由派生
- **图像层**：所有真实手稿为 Wikimedia Commons 公共域（Royal Collection Trust / Veneranda Biblioteca Ambrosiana）
- **原创 SVG 图解**：CC BY 4.0
- **中文叙事**：CC BY-SA 4.0
````

---

## 配套的次级 README 段（项目内说明）

如果想再写一段次级段，放在 "项目目录" 前作为正文补充：

````markdown
## 这是什么

一个独立的中文数字策展展览：

- 主题：达·芬奇手稿被莱奥尼剪碎与复原
- 数据基础：意大利 Leonardo//thek@ 平台 + 温莎皇家收藏 + 大西洋手稿
- 交付：8 节展览 + 9 张原创图解 + 6 张真实手稿图像
- 部署：GitHub Pages

## 工作流

1. **学术翻译**：意/英语学术平台转译为中文受众的策展叙事
2. **图解先行**：在没图之前，先把路径画清楚
3. **真实图像集成**：从公共域补充真正的手稿像素
4. **GitHub Pages 上线**：3 层 marker 让版本可被外部 grep 验证
5. **传播包 + 作品化**：公众号 / X / 小红书 / 视频脚本 / 作品集

## 推荐阅读路径

- 5 秒看完：`case-study/project-onepager.md`
- 30 秒看完英文版：`case-study/portfolio-case-en.md`
- 完整看：`case-study/portfolio-case-study.md`（中文）
- 项目复盘：`case-study/project-retrospective.md`
````
