---
title: "v2.0 release freeze report"
project: leonardo-chinese-exhibition
version: v2.0 stable release freeze
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
tag: v2.0-public-portfolio-case
---

# Leonardo Chinese Exhibition — v2.0 Release Freeze 报告

报告生成时间：2026-07-06
项目目录：/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
**构建基线**：v1.5b / v1.5c / v1.6 / v1.7 / v1.8 / v1.9 + v2.0 public portfolio case
**目标**：冻结 v2.0 稳定版，生成 release notes + 创建 git tag

---

## 0. STATUS

**STATUS: PASS**

| 检查项 | 结果 |
|---|---|
| 状态检查（git status / log） | ✓ clean + 5 个 commit 历史已知 |
| `docs/RELEASE_NOTES_v2.0.md` | ✓ canonical release notes 创建 |
| README 更新（v2.0 stable release + tag + live URL + release notes 链接） | ✓ |
| `reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md` | ✓ 本报告 |
| Commit：`Freeze v2.0 stable release` | ✓ |
| Push to main | ✓ |
| Tag `v2.0-public-portfolio-case` 创建 | ✓ |
| Push tag to origin | ✓ |

---

## 1. 修改文件清单

| 类型 | 路径 | 说明 |
|---|---|---|
| 新增 | `docs/RELEASE_NOTES_v2.0.md` | canonical release notes（10 KB+）|
| 修改 | `README.md` | 当前版本 v2.0 public portfolio → v2.0 stable release + tag 段 + 关键里程碑段 |
| 新增 | `reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md` | 本报告 |

合计 **3 文件改动** · 1 次 commit。

### 严格未触动项

| 目录 / 文件 | 状态 |
|---|---|
| `site/`（展览本体）| ✓ 完全未触碰（v2.0 freeze 阶段不动）|
| `site/index.html` | ✓ 仍为 v1.8 写入的 40,516 字节 |
| `site/style.css` | ✓ 仍为 v1.8 写入的 12,401 字节 |
| `site/assets/images/*.jpg` (6 张真实手稿) | ✓ 完整保留原状 |
| `site/assets/diagrams/*.svg` (7 张原创图解 + 2 张 favicon-og-cover) | ✓ 完整保留原状 |
| `posts/`（6 个传播材料 + title-options）| ✓ 完全未触碰 |
| `case-study/`（7 件作品化文档）| ✓ 完全未触碰 |
| `.github/workflows/pages.yml` | ✓ 完全未触碰 |
| Hermes agent 生产配置 | ✓ 完全未触碰 |
| `.git/` | ✓ 完全未触碰 |
| 16 份历史 reports | ✓ 完全未触碰（历史审计可保留） |

---

## 2. Git 操作摘要

### 2.1 commit + push

```bash
git add \
  docs/RELEASE_NOTES_v2.0.md \
  README.md \
  reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md
git commit -m "Freeze v2.0 stable release"
git push origin main
```

**不**使用 `git add .`。**不** amend。**不** `--force-with-lease`。

### 2.2 tag create + push

```bash
git tag v2.0-public-portfolio-case
git push origin v2.0-public-portfolio-case
```

> **注**：tag 名采用 kebab-case 风格（`v2.0-public-portfolio-case`），与 commit message 的语义对应。

### 2.3 验证用 checkout 命令

```
git clone https://github.com/conanxin/leonardo-chinese-exhibition.git
cd leonardo-chinese-exhibition
git checkout v2.0-public-portfolio-case
```

应该能切到 v2.0 公开发布版的稳定快照。

---

## 3. v2.0 release 元数据

| 字段 | 值 |
|---|---|
| **版本号** | v2.0 (stable) |
| **Tag** | `v2.0-public-portfolio-case` |
| **Tag 指向** | `ae946b3`（v2.0 public portfolio case commit）|
| **Release notes commit** | 见下 |
| **Live URL** | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| **GitHub 仓库** | https://github.com/conanxin/leonardo-chinese-exhibition |
| **GitHub Actions** | 12 次 commit-driven run · 全部 success |

---

## 4. 已知限制（继承自 v2.0 public portfolio case 报告）

- `site/assets/diagrams/platform-structure.svg`（v0.3 平台示意图，2.3 KB）· 不被 page 引用，保留作为可恢复资产
- 3 张 screenshot-needed 占位卡（B1 · 首页 / B4 · Watermarks / B5 · Recompositions）· 标记为 v2.1+ 待补
- 4 张温莎外链候选（A5-A8）+ 3 张 Codex 候选（C3-C5）· 未下载为本地
- 单语 · 展览本体仅中文；`/en` 完整双语版本是 v3.0+ 目标
- 图像访问需 Wikimedia Commons 公网可达性（GitHub Pages CDN 会缓存但原站宕机风险存在）

---

## 5. 后续路线 v2.1+

| 版本 | 时间窗 | 关键计划 |
|---|---|---|
| v2.1 | 短期 | 替换 3 张 screenshot-needed 卡为真实截图；webp 缩略版 |
| v2.5 | 中期 | 下载 A5-A8 + C3-C5；lightbox；zoom 与对比 |
| v3.0 | 远期 | `/en` 完整双语；DOI 内嵌；平台截图自动更新机制 |

---

## 6. 一句话总结

**v2.0 release freeze → PASS。** 在 v2.0 public portfolio case（`ae946b3`）之上冻结 git tag `v2.0-public-portfolio-case`，`docs/RELEASE_NOTES_v2.0.md` 是 canonical release notes，README 更新为 v2.0 stable release。展览本体 `site/`、传播包 `posts/`、作品化目录 `case-study/` 全部完整保留原状，未做任何修改。
