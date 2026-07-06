# Release Notes — v2.0 stable release

**Tag**: `v2.0-public-portfolio-case`
**Release date**: 2026-07-06
**Last commit**: `ae946b3` — Create v2.0 public portfolio case

---

## 项目定位

**《达·芬奇的纸上宇宙 · 中文数字策展》** 是一个独立的数字策展项目。它把意大利 Museo Galileo 的达·芬奇手稿研究平台 Leonardo//thek@ 转译为中文受众的 8 节数字展览，含 **6 张温莎皇家收藏与大西洋手稿的真实公共域手稿图像**，全程静态网页 GitHub Pages 上线。

- **场景**：个人作品集案例 / 个人数字策展项目 / 数字人文工作流样例
- **不是**：博物馆官方项目 / 大流量商业平台 / 多语言版本（v2.0 仅中文）
- **Live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/

---

## Live URL

```
https://conanxin.github.io/leonardo-chinese-exhibition/
```

- 单页 8 节展览（含 1 节序厅），约 8 分钟读完
- 移动端单列布局
- 0 外部 JS · 0 外部 CSS · 0 位图（仅 6 张 Wikimedia Commons 公共域 JPG）

---

## v2.0 完成内容

### v2.0 = 作品化阶段

本版本不改变展览本体（site/），专注于把已有 v1.5 - v1.9 的工作流整理成 7 件可直接复用的作品集文档：

| 文档 | 用途 |
|---|---|
| `case-study/portfolio-case-study.md` | 中文长篇完整案例（14 节）|
| `case-study/project-onepager.md` | 一页式项目说明 |
| `case-study/portfolio-case-en.md` | 英文版短案例（国际向） |
| `case-study/readme-showcase-section.md` | README 顶部展示段（可直接粘贴）|
| `case-study/launch-x-post.md` | X 14 条中文长帖（发布用）|
| `case-study/project-retrospective.md` | 项目复盘（做对了什么 / 踩的坑 / v1.7-1.8 解决路径 / 对未来启发）|
| `case-study/README.md` | 目录导览 |

### v2.0 release 阶段

- 本 release notes `docs/RELEASE_NOTES_v2.0.md`（canonical release notes）
- v2.0 freeze 报告 `reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md`
- Git tag `v2.0-public-portfolio-case`
- README 增加 v2.0 stable release 段

### v2.0 严格未触动项

- ✓ site/index.html + site/style.css **零修改**
- ✓ posts/ 传播包（6 个 .md + title-options）**零修改**
- ✓ case-study/ 内容（7 个 .md 已发布于上一 commit）**零修改**
- ✓ 6 张真实手稿 JPG / 9 张 SVG / 2 张 favicon-og-cover **零修改**
- ✓ `.github/workflows/pages.yml` **零修改**
- ✓ posts/ 与 case-study/ 之间**不存在任何代码耦合**

---

## 版本演进摘要 v0.1 → v2.0

| 版本 | commit | 关键 |
|---|---|---|
| v0.2 | (历史) | 视觉评审 |
| v0.3 | (历史) | 发布前最后整理 |
| v1.0 | (历史) | 首次公开发布 |
| v1.1 - v1.4 | (历史) | 多轮部署与 visual publish 验证 |
| v1.5 | (历史) | redesign 到 OpenAI editorial 风格 |
| **v1.5b** | `d69f516` | live hotfix · 三层 marker 首次上线 |
| **v1.5c** | `53c4032` | repo hygiene · 30 文件 chmod 0600 → 0644 |
| **v1.6**  | `75fd9f9` | distribution pack · 公众号 / X / 小红书 / 视频脚本 / 作品集 / 标题库 |
| **v1.7**  | `af07b15` | exhibit image upgrade · 4 新 SVG + 14 展品卡 + 展品索引 |
| **v1.8**  | `4f6d126` | real image integration · 6 张公共域真实手稿像素 |
| **v1.9**  | `97f1670` | final polish · 资产引用审计 + favicon + og-cover + credit 一致 |
| **v2.0**  | `ae946b3` | public portfolio case · 7 件作品化文档 + tag 冻结 |

**共 16 份版本报告**（reports/），每步都可追溯。

---

## 核心产物清单

### A. 展览本体（site/ · 不受 v2.0 release 影响）

| 类别 | 数量 | 大小 |
|---|---|---|
| HTML | 1 文件 | 40 KB |
| CSS | 1 文件 | 12 KB |
| 原创 SVG 图解 | 9 文件 | 24 KB 总 |
| 真实手稿 JPG | 6 文件 | 3.4 MB 总 |
| favicon + og-cover | 2 SVG | 595 B 总 |
| **全 site/** | 17 文件 | **3.6 MB** |

### B. 8 节叙事（5 + 1 + 1 + 1 = 8 个核心模块）

- 序厅：被拆散的思想博物馆
- 1 · 纸页的命运
- 2 · 《大西洋手稿》
- 3 · 温莎的绘图
- 4 · 同一张纸上的艺术与科学
- 5 · 水印与纸张
- 6 · 复原拼合
- 7 · 平台如何工作
- 8 · 达·芬奇方法

### C. 真实手稿图像（v1.8 集成 · Wikimedia Commons 公共域）

| RCIN / folio | 名称 |
|---|---|
| RCIN 912310 | Studies of a horse · c.1490 |
| RCIN 912660 | Studies of water · c.1510-12 |
| RCIN 919003 | Verso: The muscles of the shoulder · c.1510-11 |
| RCIN 912363 | Cats, lions, and a dragon · c.1517-18 |
| Codex Atlanticus f.719 recto | 机械 / 飞行相关 |
| Codex Atlanticus f.21 recto | 早期混合主题 |

每张含 alt / figcaption 容器 / credit-line（公共域 + 来源 + 馆藏）/ 外链。

### D. 传播材料（posts/ · 不受 v2.0 release 影响）

- 公众号长文 (`posts/wechat-longform.md`)
- X 14 条 thread (`posts/x-thread.md`)
- 小红书图文稿 (`posts/xiaohongshu.md`)
- 3 分钟短视频脚本 (`posts/video-script-3min.md`)
- 作品集说明 (`posts/portfolio-case.md`)
- 标题库 36 条 (`posts/title-options.md`)

### E. 作品化文档（case-study/ · v2.0 引入）

- 7 件作品化文档（见上表）

### F. 文档与报告

- 11 个 docs/ 文档（含本 release notes）
- 16 份版本 / 审计 reports
- README.md 主入口

---

## 技术实现

| 层 | 选型 |
|---|---|
| HTML | 静态 HTML 5 · 0 框架 |
| CSS | 纯 CSS · 0 外部依赖 · system fonts |
| 字体 | PingFang SC + Helvetica Neue + system fallback |
| 图像 | SVG（原创） + JPG（Wikimedia Commons 公共域）|
| 部署 | GitHub Pages + Actions · upload-pages-artifact@v3 + deploy-pages@v4 |
| 版本系统 | 4 个 layered marker（v1.5b / v1.7 / v1.8 都活 · meta + comment + footer 三层）|
| 真实手稿来源 | Wikimedia Commons · 公共域授权 |
| 自动化 | GitHub Actions · 每次 push main 自动 build & deploy |

### GitHub Pages 部署状态

- **Workflow file**: `.github/workflows/pages.yml`
- **Trigger**: `push main` 或手动 `workflow_dispatch`
- **Permissions**: `contents: read` + `pages: write` + `id-token: write`
- **Path**: `site/` (上传为 pages artifact)
- **历史运行**: 12 次 commit-driven run，全部 success

---

## 已知限制

### 9 张 SVG 临时未引用

- `site/assets/diagrams/platform-structure.svg`（v0.3 平台示意图，2.3 KB）
  - 不被 page 引用，由 `platform-tool-wall.svg`（v1.7）内容接替
  - 保留作为可恢复资产（不删除）

### 3 张截图候选平台截图占位

- B1 · Leonardo//thek@ 首页 9 功能入口
- B4 · Watermarks 模块界面
- B5 · Recompositions 模块界面

仅以 `.image-placeholder-pro` 截图候选卡占位，未截图存证（涉及第三方内容合规 + 频率约束）。

### 图片源外链候选未本地化（4 张温莎 + 3 张 Codex）

- A5-A8（4 张温莎外链）· RCIN 912278 / 912406 / 912594 / 912478
- C3-C5（3 张 Codex 候选）· f.117 / f.272 / f.455

这些在 `research/image-candidates.md` 中保留为 `download_status: pending`，v2.1+ 可下载。

### 单语（中文）

- v2.0 仅中文版本
- 英文版（仅 portfolio-case-en.md 文档级翻译）已经发布，但展览本体（site/）仍为中文
- `/en` 完整双语版本是 v3.0+ 目标

### 平台截图依赖外部

- 9 个平台工具的 SVG 替代（platform-tool-wall）= 视觉可控
- 但不强等价于"看到真实界面"
- 观看者需要自行打开 `teche.museogalileo.it/leonardo` 验证平台

---

## 后续路线 v2.1+

### v2.1（短期）

- v2.0 release 的工作流可以复刻到其他数字策展项目
- 替换 3 张 screenshot-needed 卡为真实截图（B1 / B4 / B5）
- 转 webp 缩略版（节省 ~30% JPG 字节）

### v2.5（中期）

- 下载 A5-A8（4 张温莎外链） + C3-C5（3 张 Codex 候选）
- 给图像增加 lightbox / 全屏查看
- 增加 v2.1 + v2.2 报告

### v3.0（远期）

- `/en` 完整双语版本
- 给图像卡增加 zoom / 比较视图
- DOI / source URL 内嵌层
- 平台截图全自动更新机制（定时任务）

---

## 如何参考 v2.0

- **Live 看展览**：https://conanxin.github.io/leonardo-chinese-exhibition/
- **GitHub 看代码 + 历史**：https://github.com/conanxin/leonardo-chinese-exhibition
- **GitHub 在 v2.0 tag 看代码**：`git clone https://github.com/conanxin/leonardo-chinese-exhibition && cd leonardo-chinese-exhibition && git checkout v2.0-public-portfolio-case`
- **5 秒看完一个项目**：`case-study/project-onepager.md`
- **完整看案例**：`case-study/portfolio-case-study.md`
- **英文版**：`case-study/portfolio-case-en.md`
- **项目复盘**：`case-study/project-retrospective.md`
- **X 14 条长帖**：`case-study/launch-x-post.md`

---

## 16 份报告清单

| 版本 | 报告 |
|---|---|
| v0.2 | `reports/leonardo_chinese_exhibition_v0_2_visual_review.md` |
| v0.3 | `reports/leonardo_chinese_exhibition_v0_3_release_prep.md` |
| v1.0 | `reports/leonardo_chinese_exhibition_v1_0_public_release_report.md` |
| v1.1 | `reports/leonardo_chinese_exhibition_v1_1_deploy_report.md` |
| v1.2 | `reports/leonardo_chinese_exhibition_v1_2_live_publish_verification.md` |
| v1.3 | `reports/leonardo_chinese_exhibition_v1_3_openai_style_redesign_report.md` |
| v1.4 | `reports/leonardo_chinese_exhibition_v1_4_visual_publish_verification.md` |
| v1.5 | `reports/leonardo_chinese_exhibition_v1_5_live_release_report.md` |
| v1.5b | `reports/leonardo_chinese_exhibition_v1_5b_live_marker_verification_report.md` |
| v1.5c | `reports/leonardo_chinese_exhibition_v1_5c_repo_hygiene_report.md` |
| v1.6 | `reports/leonardo_chinese_exhibition_v1_6_distribution_pack_report.md` |
| v1.7 | `reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md` |
| v1.8 | `reports/leonardo_chinese_exhibition_v1_8_real_image_integration_report.md` |
| v1.9 | `reports/leonardo_chinese_exhibition_v1_9_final_exhibition_polish_report.md` |
| v2.0 (public portfolio) | `reports/leonardo_chinese_exhibition_v2_0_public_portfolio_case_report.md` |
| **v2.0 (release freeze)** | `reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md` |

**最后更新**：2026-07-06
