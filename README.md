# 达·芬奇的纸上宇宙：被拆散的手稿与重新连接的思想

基于 Leonardo//thek@ 平台的中文数字展览项目。

## 项目简介

本项目为中文读者设计，聚焦达·芬奇手稿拆散与复原、平台研究工具、纸张证据与比较研究，而非传统生平介绍。

## 本地预览

```bash
cd /home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
python3 -m http.server 8787 -d site
```

然后访问 `http://localhost:8787`

## 发布方式

- **GitHub Pages**：直接将 `site/` 目录设为 Pages 源
- **Cloudflare Pages**：直接上传 `site/` 目录或连接 Git 仓库

## 文件结构

- `research/`：平台功能、手稿背景、图片候选
- `exhibition/`：策划案、策展前言、展陈文本、导览稿
- `site/`：可独立部署的静态展览网页
- `reports/`：各版本验收与发布报告

## 版本记录

- **v0.1**：初始内容框架与研究资料整理
- **v0.2**：网页升级（figure 结构 + 深色手稿风格 + 图片分类）
- **v0.3**：发布准备（meta/OG/导航/部署文档）

## 后续路线

- **v0.4**：公众号/小红书/X 长帖版本
- **v1.0**：完整公开展览站（真实图片 + 互动元素）