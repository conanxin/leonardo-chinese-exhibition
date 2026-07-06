# leonardo-chinese-exhibition — v2.6 Post-release Maintenance Report

## STATUS

**PASS ✓** — v2.6 发布后维护整理完成。README 顶部重整，post-release maintenance 与 roadmap docs 创建，4 个 roadmap GitHub Issues 创建，GitHub repo About 更新成功，no-touch 严格遵守。

## Baseline

| 项 | 值 |
| --- | --- |
| **HEAD (at start)** | `20eb71a0bb0541b06e1d087e7d5f03a5022baa30` |
| **origin/main (at start)** | `20eb71a0bb0541b06e1d087e7d5f03a5022baa30` |
| **Stable tag** | `v2.6-content-stable` |
| **Tag target commit** | `01cdaa2dc1487a5f7877c8702720d0df8dbb17ce` |
| **GitHub Release URL** | <https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.6-content-stable> |
| **Live URL** | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| **Live byte size** | 82,803 B（site 未改动）|
| **v2.0 tag** | `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4`（未触碰）|

## README updated

README 顶部重整为更清晰的项目入口区：

- 标题简化为 `# 达·芬奇的纸上宇宙`（去掉副标题）
- 增加项目定位描述（基于 Leonardo//thek@、Codex Atlanticus 与英国皇家收藏）
- 顶部新增 5 项关键信息：Live Exhibition / Stable Release / Stable Tag / Status / Current stable line
- 简化 `## 当前版本` 段：只保留 active / legacy tag + live URL
- 链接至 `docs/POST_RELEASE_MAINTENANCE.md` 与 `docs/ROADMAP_AFTER_v2.6.md`

未改动 site/ 任何文件。

## Docs created

| 文件 | 大小 | 用途 |
| --- | --- | --- |
| `docs/POST_RELEASE_MAINTENANCE.md` | 3.8 KB | 发布后维护整理（safe / risky tasks、deployment checklist、historical lessons）|
| `docs/ROADMAP_AFTER_v2.6.md` | 2.1 KB | v2.7 / v2.8 / v2.9 / v3.0 方向 + backlog |

## GitHub Issues created

4 个 roadmap issues 全部创建成功：

| # | 标题 | 标签 | URL |
| --- | --- | --- | --- |
| 1 | v2.7 Bilingual Edition | enhancement, roadmap | <https://github.com/conanxin/leonardo-chinese-exhibition/issues/1> |
| 2 | v2.8 Education / Teacher Guide | enhancement, education, roadmap | <https://github.com/conanxin/leonardo-chinese-exhibition/issues/2> |
| 3 | v2.9 More Manuscript Images | enhancement, content, roadmap | <https://github.com/conanxin/leonardo-chinese-exhibition/issues/3> |
| 4 | v3.0 Reusable Digital Exhibition Template | enhancement, template, roadmap | <https://github.com/conanxin/leonardo-chinese-exhibition/issues/4> |

标签创建：先创建 `roadmap` / `content` / `education` / `template` 4 个标签（仓库内原本不存在），再为 4 个 issue 贴标。

## GitHub repo About updated

`gh repo edit` 成功更新：

| 字段 | 值 |
| --- | --- |
| **Description** | 中文数字展览：达·芬奇手稿、Leonardo//thek@ 与纸上宇宙 |
| **Homepage** | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| **Topics** | chinese, digital-exhibition, digital-humanities, leonardo-da-vinci |

## Live verification

| 项 | 值 | 状态 |
| --- | --- | --- |
| Live byte size | 82,803 B | ✓（site 未改动）|
| v2.6-content-copy-polish marker | 1 | ✓ |
| v2.6-content-stable marker | 1 | ✓ |
| image-placeholder-pro | 0 | ✓ |
| section-takeaway | 9 | ✓ |
| script.js HTTP | 200 | ✓ |
| v2.0 tag | `9e6233ab...` 未触碰 | ✓ |
| v2.6 tag | `01cdaa2` 未移动 | ✓ |

## No-touch confirmation

| 项 | 状态 |
| --- | --- |
| `v2.0-public-portfolio-case` tag | **未触碰**（仍 `9e6233ab...`）|
| `v2.6-content-stable` tag | **未移动**（仍指向 freeze commit `01cdaa2`）|
| 旧 GitHub Release（v2.0） | **未触碰**（publishedAt 仍 `2026-07-06T02:56:01Z`）|
| `site/index.html` | **未触碰** |
| `site/style.css` | **未触碰** |
| `site/script.js` | **未触碰** |
| `posts/` | **未触碰**（last commit `75fd9f9`）|
| `case-study/` | **未触碰**（last commit `ae946b3`）|
| `release-assets/` 既有文件 | **未触碰**（`manifest.md` / `screenshots/*`）|
| Hermes 生产配置 | **未触碰** |
| untracked `.firecrawl/` | **未处理** |

## Commit chain (v2.6-post-release-maintenance)

| commit | message | 状态 |
| --- | --- | --- |
| (待记录) | Add post-release maintenance plan | 待 push |

## Next step recommendation

- v2.6 Content Stable 已是稳定基线
- 4 个 roadmap issues 已建立，可在 GitHub 上跟踪未来方向
- 日常维护参考 `docs/POST_RELEASE_MAINTENANCE.md` 的 safe / risky tasks 分类
- 任何对 site/ 的改动应在独立分支实施，并以新 tag 收口

---

*v2.6 post-release maintenance PASS — 稳定基线已建立长期维护框架。*
