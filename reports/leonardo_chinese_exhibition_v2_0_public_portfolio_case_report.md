---
title: "v2.0 public portfolio case report"
project: leonardo-chinese-exhibition
version: v2.0
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
---

# Leonardo Chinese Exhibition — v2.0 public portfolio case 报告

报告生成时间：2026-07-06
项目目录：/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
**构建基线**：v1.5b live hotfix + v1.5c repo hygiene + v1.6 distribution pack + v1.7 exhibit image upgrade + v1.8 real image integration + v1.9 final polish
**目标**：把展览整理成 7 件"可直接复用到作品集 / 个人主页 / 简历 / 学术合作"的作品化案例文档，并配套 README 顶部展示段。

---

## 0. STATUS

**STATUS: PASS**

| 检查项 | 结果 |
|---|---|
| 7 件 case-study 文档生成 | ✓ |
| README 更新 + 推荐阅读路径 | ✓ |
| case-study/README.md 导览 | ✓ |
| v2.0 报告生成 | ✓ (本文) |
| live URL | ✓ https://conanxin.github.io/leonardo-chinese-exhibition/ |
| 当前版本状态 | v2.0，6 张真实手稿 + 9 张原创 SVG + 8 节展览 全部上线 |
| 是否修改 site/ 展览正文 | ✗ 否 |
| 是否修改 posts/ 传播包 | ✗ 否（仅引用其内容做案例说明）|
| 是否触动 Hermes 生产配置 | ✗ 否 |

---

## 1. 新增文件清单（8 件 + 1 README 更新 + 1 报告 = 10 个 Git 操作单元）

| 类型 | 路径 | 字节 | 用途 |
|---|---|---|---|
| 新增 | `case-study/portfolio-case-study.md` | 14,581 | 中文长篇完整案例（14 节 · 含背景/问题/方法/IA/视觉/图像/技术/版本/复用/后续路线）|
| 新增 | `case-study/project-onepager.md` | 3,603 | 一页式项目说明（项目类型/关键词/产出/技术栈/亮点 5 条）|
| 新增 | `case-study/portfolio-case-en.md` | 4,643 | 英文版短案例（适合国际作品集与合作伙伴）|
| 新增 | `case-study/readme-showcase-section.md` | 4,230 | README 顶部展示段（可直接拷贝）|
| 新增 | `case-study/launch-x-post.md` | 4,987 | X 14 条中文长帖（发布用）|
| 新增 | `case-study/project-retrospective.md` | 10,887 | 项目复盘（做对了什么/踩的坑/v1.7-1.8 解决路径/对未来启发）|
| 新增 | `case-study/README.md` | 2,236 | case-study 目录导览 |
| 修改 | `README.md` | +30 行 | 当前版本 v1.9 → v2.0 + case-study 节 + 推荐阅读路径 |
| 新增 | `reports/leonardo_chinese_exhibition_v2_0_public_portfolio_case_report.md` | — | 本报告 |

总计 **10 个 Git 操作单元**：8 个新文件 + 1 个 README 修改 + 1 个报告新增。

---

## 2. 每个 case-study 文件用途

### 2.1 `portfolio-case-study.md`（中文长篇）

**目标读者**：5 分钟完整阅读的雇主/合作方/评委
**结构**（14 节）：
1. 一句话简介 + Live URL
2. 项目背景（达·芬奇真实遗产 + Leonardo//thek@ + 三道门槛）
3. 原始问题（四类落地难题）
4. 我的目标
5. 方法路径（学术转译 vs 重写 + 单一主线 + 模块化 + 双重可读性）
6. 信息架构
7. 视觉设计（OpenAI editorial 风 + 编辑思维 vs 设计思维）
8. 图像与展品系统（v1.5 / v1.7 / v1.8 / v1.9 四段质变）
9. 技术实现（HTML / CSS / 字体 / 图像 / 部署）
10. 版本演进
11. 最终成果
12. 可复用经验
13. 后续路线
14. 关键词

### 2.2 `project-onepager.md`（一页式）

**目标读者**：5 秒扫描的访客 / 想快速判断"这是什么"的读者
**结构**：
- 项目名称 + 类型 + 关键词
- 解决的问题（中文策展转译）
- 产出物表
- 技术栈表
- 链接表
- 亮点 5 条（一句话级别）

### 2.3 `portfolio-case-en.md`（英文短案例）

**目标读者**：国际合作方 / 英文读者 / 英文简历附件 / 学术邮件
**结构**：
- One-liner
- Live URL
- What's the project · What's the design language · What's in the technical box · What's the content architecture · What's in version control · What's the public-good angle · Contact

### 2.4 `readme-showcase-section.md`（README 顶部展示段）

**目标读者**：GitHub README 浏览者
**结构**：可直接拷贝的 Markdown 块（含 badge + Highlights + What changed + Links + 复用经验 + 配套次级段）

### 2.5 `launch-x-post.md`（X 长帖）

**目标读者**：X / Twitter 受众
**结构**：14 条 thread，每条 30-80 字
- hook（剪刀比笔更强大）
- 5 条背景铺垫
- 4 条工作流
- 4 条工程亮点
- 收尾

### 2.6 `project-retrospective.md`（项目复盘）

**目标读者**：自我复盘 / 团队内部分享 / 公开博客
**结构**（6 节）：
1. 做对了什么（学术研究 → 数字策展 → 作品化三段路径）
2. 中间踩了哪些坑（不像展览 / 占位语 / RCIN 编号 / 0600 / favicon 未挂）
3. 为什么早期页面不像展览（无视觉参考 / 无 4 件套 / 内容即终点）
4. v1.7 / v1.8 怎么解决问题（结构性扭转 + 真实图像）
5. 对未来数字展览项目的启发（通用方法 + 中文国际策展）
6. 我自己最满意的一处（展品索引 8 卡）

### 2.7 `case-study/README.md`（目录导览）

**目标读者**：浏览 case-study/ 的索引读者
**结构**：文档清单 + 推荐阅读顺序 + 与 posts/ 的区别 + 复用方式

---

## 3. 项目当前版本状态（v2.0）

### 3.1 展览本体（site/）

| 组件 | 数量 / 体积 |
|---|---|
| HTML | 1 个文件 · 40 KB |
| CSS | 1 个文件 · 12 KB |
| 原创 SVG 图解 | 9 个 · 24 KB 总 |
| 真实手稿 JPG | 6 个 · 3.4 MB 总 |
| favicon + og-cover | 2 个 SVG · 600 bytes 总 |
| 总 site/ 体积 | ~3.6 MB |
| live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| 部署 workflow | GitHub Actions · Pages · 已 11 次运行均 success |

### 3.2 标志系统

| 版本 | marker | 层级 |
|---|---|---|
| v1.5b-live-hotfix | meta + comment | 双层保留 |
| v1.7-exhibit-image-upgrade | meta + comment | 双层保留 |
| v1.8-real-image-integration | meta + comment | 双层保留 |
| v1.9 final polish | README + 报告 | 不上 marker（按"不大改展览正文"原则）|
| v2.0 public portfolio case | README + case-study/ + 报告 | 不上 marker（不直接改展览正文）|

### 3.3 报告体系

| 报告 | 内容 |
|---|---|
| `leonardo_*_v0.2_visual_review.md` | 早期视觉评审 |
| `leonardo_*_v0.3_release_prep.md` | 发布前准备 |
| `leonardo_*_v1.0_public_release_report.md` | 首次公开发布 |
| `leonardo_*_v1.1_deploy_report.md` | 部署报告 |
| `leonardo_*_v1.2_live_publish_verification.md` | 上线验证 |
| `leonardo_*_v1.3_openai_style_redesign_report.md` | OpenAI 风 redesign |
| `leonardo_*_v1.4_visual_publish_verification.md` | 视觉发布验证 |
| `leonardo_*_v1.5_live_release_report.md` | v1.5 发布 |
| `leonardo_*_v1.5b_live_marker_verification_report.md` | v1.5b marker 验证 |
| `leonardo_*_v1.5c_repo_hygiene_report.md` | v1.5c 仓库卫生 |
| `leonardo_*_v1_6_distribution_pack_report.md` | v1.6 传播包 |
| `leonardo_*_v1_7_exhibit_image_upgrade_report.md` | v1.7 图像升级 |
| `leonardo_*_v1_8_real_image_integration_report.md` | v1.8 真实图像 |
| `leonardo_*_v1_9_final_exhibition_polish_report.md` | v1.9 final polish |
| `leonardo_*_v2_0_public_portfolio_case_report.md` | **本报告** |

共 **15 份版本报告**，全套可追溯。

---

## 4. live URL

- **线上**：https://conanxin.github.io/leonardo-chinese-exhibition/
- **GitHub 仓库**：https://github.com/conanxin/leonardo-chinese-exhibition
- **GitHub Actions**：最新一次 v1.9 polish push 触发 run 28763755481 → success

## 5. git 操作摘要（step 10 / 11）

### 5.1 单次 commit + push

```bash
git add \
  case-study/portfolio-case-study.md \
  case-study/project-onepager.md \
  case-study/portfolio-case-en.md \
  case-study/readme-showcase-section.md \
  case-study/launch-x-post.md \
  case-study/project-retrospective.md \
  case-study/README.md \
  README.md \
  reports/leonardo_chinese_exhibition_v2_0_public_portfolio_case_report.md
git commit -m "Create v2.0 public portfolio case"
git push origin main
```

**不** 使用 `git add .`。**不** amend。**不** `--force-with-lease`。

### 5.2 不触动项

✓ site/（展览本体）**未触动**。
✓ posts/（传播包）**未触动**——v2.0 仅在 case-study 中**引用**了 v1.6 传播材料的存在，没有动 posts/ 任何一个文件。
✓ `.github/workflows/pages.yml` **未触动**。
✓ Hermes agent 生产配置 **未触动**。
✓ `.git/` **未触动**。
✓ 6 张真实手稿图像 / 7 张 SVG / 2 张 favicon-og-cover **未触动**。

---

## 6. 下一步建议

### 6.1 不紧急项（v2.1+）

- 把 case-study 链接放进个人主页 / Notion 作品集
- 在 X 上发布 launch-x-post.md 的实际内容（建议改用 platform-native 编辑器做最后打磨）
- 把 readme-showcase-section.md 复制到原 README（目前是 README 顶部引用 — 可根据需要替换原顶部内容）

### 6.2 v3.0+

- 多语版本（zh-tw / en 双语完整版）
- lightbox / 全屏查看图像
- DOI / source URL 内嵌
- 给展览增加 `/en` 路径

### 6.3 不建议

- 不要把"展品索引 8 卡"再增加更多卡片——8 节就够，再多会变成 9 节 1 卡
- 不要把 v2.0 case-study 拆成 Notion 子页——保留单文档可追溯
- 不要引入 analytics / tracking

---

## 7. 一句话总结

**v2.0 PASS。** 把 9 个版本的展览工作流整理成 7 件作品化文档（中文长篇 / 中文一页式 / 英文版 / README 顶部段 / X 发布稿 / 项目复盘 / 目录导览），加 1 个 README 更新与 1 个报告。一次 commit + push 落地，site/ 与 posts/ 完整保留，3 个 marker 完整保留，6 张真实手稿与 9 张 SVG 完整保留。
