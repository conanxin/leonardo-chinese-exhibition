# v2.0 — 达·芬奇的纸上宇宙：中文数字展览稳定版

> 中文数字展览 · Leonardo//thek@ 平台转译 · 真实手稿图像集成 · GitHub Pages 稳定发布

**Live Demo**: https://conanxin.github.io/leonardo-chinese-exhibition/

稳定版基于 commit `9e6233a`，tag：`v2.0-public-portfolio-case`。

---

## 🎯 这个版本是什么

一个完整的中文策展项目：从数字研究平台的转译，到图文展览，到真实 Codex Atlanticus 高清手稿集成，到 GitHub Pages 上线，到作品集案例和发布传播包——**一条从原料到线上展览的完整工作流**。

它不是单页静态展示，而是一个小型的中文数字展览系统：

- 9 个策展章节，覆盖「序厅」到「达·芬奇方法今天还能用吗」
- 6 张真实 Codex Atlanticus 高清手稿
- 9 张自制 SVG 概念图（结构图、复原拼合示意、纸张证据示意图等）
- 1 个本地 OG-cover / favicon
- 作品集 + 项目卡片 + 短宣三种长度的案例文档
- 6 张社交媒体传播文案（小红书 / X / LinkedIn / Instagram / 小宇宙简介 / QQ群文案）

---

## ✨ Highlights

- **中文数字展览** — 一座被拆散的思想博物馆的中文叙事
- **Leonardo//thek@ 平台转译** — 数字研究平台 → 中文策展长文
- **OpenAI-style editorial design** — 一栏正文、报刊级 typographic rhythm、专色呼出
- **真实手稿图像集成** — 6 张 Codex Atlanticus JPG（CC0 / 公有领域）
- **GitHub Pages 发布** — workflow 自动部署 + live URL
- **posts/ 传播包** — 6 个平台传播稿（小红书 / X / LinkedIn / Instagram / 小宇宙 / QQ群）
- **case-study/ 作品集案例** — portfolio 全文 + onepager + 简短英文版

---

## 📦 What's included

```
site/                       展览主体（HTML / CSS / 6 JPG / 9 SVG / OG / favicon）
posts/                      6 个平台传播稿 + 标题候选
case-study/                 作品集长文 + onepager + 英文短案例
docs/                       release notes + 部署 + GitHub Pages 说明
reports/                    17 个版本演进报告（v0.1 → v2.0 完整链路）
release-assets/             GitHub Release 发布材料（6 张截图 + manifest）
.github/workflows/          Pages 自动部署 workflow
```

---

## 🏷 Stable tag

```
v2.0-public-portfolio-case
```

指向 commit `9e6233a`（"Freeze v2.0 stable release"）。完整 release notes 详见
[`docs/RELEASE_NOTES_v2.0.md`](RELEASE_NOTES_v2.0.md) + 冻结报告
[`reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md`](https://github.com/conanxin/leonardo-chinese-exhibition/blob/main/reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md)。

---

## ⚠️ Known limitations

- 部分平台截图仍为候选（posts/ 下的标题 / cover 还可以迭代）
- 后续可继续补充更多 Codex Atlanticus 高清图像（现在 6 张，可扩到 12+）
- 可继续制作互动时间线（静态版已可用，动态版留待 v3.0+）
- 暂未做英文版展览正文（仅提供了英文作品集短案例）

---

## 🚀 Next

- **v2.1** — 发布截图包 + GitHub Release 可视化附件（本版本 ✓）
- **v2.2** — 视觉传播资产（X 卡 / 小红书封面 / LinkedIn banner） + 45 秒介绍视频
- **v3.0** — 通用展览模板：把这个工作流抽象成可复用框架，让任何中文研究主题都能 1-2 天上线

---

## 🛠 技术实现

- **HTML / vanilla CSS** — 单页 HTML，无 build step，纯静态
- **GitHub Pages** — Actions workflow (upload-pages-artifact@v3 + deploy-pages@v4) 自动部署
- **No JS framework** — 全文零运行时依赖（设计感来自排版和卡片结构）
- **资源本地化** — 所有手稿图像 / SVG / OG 都下到 `site/assets/`，无第三方 CDN
- **Case study** — 纯 Markdown，case-study / 4 个短文档组成 1+1+1 作品集套装

---

## 📊 版本演进摘要 v0.1 → v2.0

| 版本 | 阶段 | 主要产出 |
|---|---|---|
| v0.1 | Leonardo//thek@ 数据采集 | 研究脚手架 |
| v0.5 | 中文长文转译 | 策展稿件初稿 |
| v1.0 | 单页展览 + 美学设计 | 第一个可发布的版本 |
| v1.5 | Live hotfix + deploy 治理 | Pages workflow 切到 Actions |
| v1.7 | 真实手稿图像初步集成 | 6 张 JPG 上线 |
| v1.8 | 真实图像 + OG / favicon | OG-cover 上线 |
| v1.9 | 最终展览打磨 | section 标题微调 |
| **v2.0** | **作品集 + 发布包** | **本版本** |

---

## 🧪 如何验证本版本

1. 访问 https://conanxin.github.io/leonardo-chinese-exhibition/ — 9 章展览
2. 切换到 raw 仓库：`https://github.com/conanxin/leonardo-chinese-exhibition/tree/v2.0-public-portfolio-case`
3. 查看 `docs/RELEASE_NOTES_v2.0.md` 获取完整 release notes
4. 查看 `case-study/portfolio-case-study.md` 获取作品集长文

---

**作者**: Xin Conan · **平台**: Leonardo//thek@ + GitHub Pages · **许可**: 文字 MIT · 手稿图像 CC0

> "一张被拆散的纸，重新接回来，是一件比写论文更接近达·芬奇的事。" — 展览序厅
