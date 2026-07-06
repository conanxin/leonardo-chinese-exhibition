# v2.7 Zh Exhibition Polish

> 2026-07-07 · 真实稳定封版 (real stable freeze)
>
> 本 release 把已上线的 v2.7 中文展览体验精修内容正式独立 tag + release，作为下一个 round（v2.8+）的真实起点。

## Release identity

- **Live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/
- **Tag**: `v2.7-zh-exhibition-polish`
- **Verified live byte size**: **85,564 B**
- **Content commit**: `71c7403` — *Polish Chinese exhibition experience*
- **Freeze commit**: 留空（freeze round 提交后回填）
- **Status**: verified live baseline

## What changed (相对于 v2.6-content-stable)

v2.7 是中文展览体验精修版。它不做双语、不做教育版、不做模板化，而是在 v2.6 Content Stable 之后专注中文观展体验。

### 内容层面

- 新增「如果你只有 3 分钟」中文导览摘要（live 中 `quick-guide-zh` 命中 1 次）
- 新增 [`docs/VISITOR_GUIDE_ZH.md`](../docs/VISITOR_GUIDE_ZH.md) — 中文观展手册（3 / 15 / 60 分钟三档路线 + 5 件最重要展品 + 10 个必知术语）
- 清理 4 处重复表达（section 7 工具模块 / section 8 思考方法 / postscript 关系网等）
- 新增 4 个「如何观看」动作提示（viewer-action，live 命中 4 次）
- 保留 guided mode / lightbox / runtime section-nav / tour progress 全部 v2.6 stable 交互能力
- 在 README 与 docs/ROADMAP_AFTER_v2.6.md 中明确标记 v2.7 为「Chinese Exhibition Polish」（不是 Bilingual Edition）

### 元数据层面

- v2.7 footer marker `v2.7 zh exhibition polish`（strong）
- v2.5-real guided accessibility marker 保留
- v2.6 content stable marker 保留
- v1.5b live hotfix marker 保留
- 所有旧 marker 三层（meta / comment / footer）一致

### Issue 状态

- GitHub Issue #1「v2.7 Bilingual Edition」仍保持 OPEN。Issue 标题与本 release 的「Chinese Exhibition Polish」不一致 —— 这是历史遗留命名差异。本 release 不强行关闭 / 重命名 #1，留给后续 round 单独处理（避免误把 bilingual 话题与 v2.7 zh polish 混淆）。
- 详见 [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md)。

## Verification (live 实测 2026-07-07)

| 项 | 命令 | 结果 |
|---|---|---|
| Live HTTP | `curl -LIs` | 200 |
| Live byte size | `wc -c` on `curl -L -s` | **85,564 B** |
| v2.7 marker | `grep -c "v2.7-zh-exhibition-polish"` | 1 |
| v2.8 marker | `grep -c "v2.8-deep-exhibition-content"` | 0 |
| v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| quick-guide-zh | `grep -c "quick-guide-zh"` | 1 |
| viewer-action | `grep -c "viewer-action"` | 4 |
| image-placeholder-pro | `grep -c "image-placeholder-pro"` | 0 |
| section-takeaway | `grep -c "section-takeaway"` | 18 (multiple references per aside) |
| script.js | `curl -LIs` | HTTP 200 |

## No-touch confirmation (freeze round)

| 类别 | 状态 |
|---|---|
| v2.0 tag (`v2.0-public-portfolio-case`) | untouched (基线 9e6233a) |
| v2.6 tag (`v2.6-content-stable`) | untouched (基线 033b65e / 01cdaa2) |
| Old GitHub Releases | untouched |
| `site/index.html` | 不修改 |
| `site/style.css` | 不修改 |
| `site/script.js` | 不修改 |
| `posts/` | 不修改 |
| `case-study/` | 不修改 |
| `release-assets/` 既有文件 | 不修改 |
| `_template/` | 不创建（按约束） |
| `_pilots/` | 不创建（按约束） |
| Untracked `.firecrawl/` | 不处理 |
| `git add .` | 不用 |

## Known note

Earlier v2.8 / v2.9 / v3.x task histories were recorded as **phantom / unverified** in [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md). v2.7-zh-exhibition-polish is the current **verified live baseline**，下一个 round 起点。

## Files in this release

| 文件 | 角色 |
|---|---|
| `docs/RELEASE_NOTES_v2.7_ZH_EXHIBITION_POLISH.md` | 本文件 |
| `release-assets/v2.7-zh-exhibition-polish-manifest.md` | release manifest |
| `reports/leonardo_chinese_exhibition_v2_7_real_stable_freeze_report.md` | freeze round 报告 |
| `README.md` | 顶部 verified-state 与 v2.7 polish 小节更新 |

---

*v2.7-zh-exhibition-polish 是真实 live baseline 的第一次正式 freeze。下一个 round 从本 tag 出发。*