# v2.9 Real Source & Rights Audit

> 2026-07-07 · 真实稳定封版 (real stable freeze)
>
> 本 release 把 v2.9 真实来源与权利审计正式独立 tag + release，作为下一 round（v3.0+）的真实起点。

## Release identity

- **Live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/
- **Tag**: `v2.9-real-source-rights-audit`
- **Source tag**: `v2.8-real-deep-content` @ `65b4fbc`
- **Verified live byte size**: **92,976 B**
- **Audit commit**: `dbcc563dbdce0f0c3db84e73f379cb1f58df42a3` — *Audit sources and rights from verified v2.8*
- **Backfill commit**: `7d5a6ce2040070662d0cf2530b14f8e8b80ef2a3` (报告数字回填)
- **Freeze commit**: 留空（freeze round 提交后回填）
- **Status**: verified source and rights audit

## What changed (相对于 v2.8-real-deep-content)

v2.9 Real Source & Rights Audit 是**基于真实 v2.8 tag** 的来源与权利审计版。它**不**新增展览内容、不新增图片、不做双语、不做教育版、不做模板化。

### 内容层面

- 审计当前展览使用的所有 collection / manuscript images
- 审计 Leonardo//thek@ 平台截图（4 张引用 + 2 张已下载未引用）
- 审计自制 SVG / project-generated diagrams
- 审计 site metadata assets
- 新增 [`docs/SOURCE_AUDIT_MANIFEST.md`](../docs/SOURCE_AUDIT_MANIFEST.md) — 详细清单（每张图的文件、源机构、源 URL、授权边界、confidence）
- 新增 [`docs/RIGHTS_AND_SOURCES.md`](../docs/RIGHTS_AND_SOURCES.md) — 4 类 source + 三层 credit + reuse caution + 已知限制
- 更新 [`research/image-candidates.md`](../research/image-candidates.md) 追加 v2.9 audit 状态、confidence、follow-up items
- 检查 source-note / credit-line / figcaption / data-credit 的完整性与一致性
- 检查关键外链（live / GitHub / 馆藏 / 平台 / Wikimedia 文件页）
- 收紧站点 footer wording：从「公共域授权使用」到「以公共域授权经 Wikimedia Commons 引用...具体授权边界请以 Wikimedia Commons 文件页与馆藏页面为准」

### 元数据层面

- v2.9 footer marker `v2.9 real source rights audit`（strong）
- v2.8 / v2.7 / v2.6 / v2.5-real / v1.5b 历史 marker 全部保留（三层：meta / comment / footer）
- **site/style.css 与 site/script.js 未触碰** —— audit round 的核心约束，避免引入意外视觉/交互变化

## Assets audited

| Category | Count | Notes |
|---|---|---|
| Collection / manuscript images | 6 | 温莎 4（RCIN 912310 / 912660 / 919003 / 912363）+ Codex Atlanticus 2（f.719 recto / f.21 recto） |
| Platform screenshots (referenced) | 3 | 首页 / Watermarks / Recompositions |
| Platform screenshots (unused) | 2 | platform-advanced-search.jpg / platform-comparative-study.jpg（已下载但未引用，follow-up 项） |
| Self-made SVG / project-generated diagrams | 7 | collection-split / manuscript-journey / thinking-map / watermark-evidence-chain / recomposition-triptych / platform-structure / platform-tool-wall |
| Site metadata assets | 2 | favicon.svg / og-cover.svg |
| **Total** | **20** | （含 2 张 unused） |

## Verification (live 实测 2026-07-07)

| 项 | 命令 | 结果 |
|---|---|---|
| Live HTTP | `curl -LIs` | 200 |
| Live byte size | `wc -c` on `curl -L -s` | **92,976 B** |
| v2.9 marker | `grep -c "v2.9-real-source-rights-audit"` | 1 |
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | 1 |
| phantom v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| image-placeholder-pro | `grep -c` | 0 |
| source-note | `grep -c` | 14 |
| credit-line | `grep -c` | 13 |
| figcaption | `grep -c` | 24 |
| 4 deep blocks (preserved from v2.8) | `grep -c` | 1 / 1 / 1 / 1 |
| script.js | `curl -LIs` | HTTP 200 |
| `node --check site/script.js` | syntax check | PASS |

### Playwright 运行时检查（python3.12 + Playwright 1.58.0）

| 项 | 结果 |
|---|---|
| section-nav runtime links | 31 (与 v2.5-real / v2.8 一致) |
| 4 deep blocks | 1 / 1 / 1 / 1 |
| v2.7 marker | 1 |
| v2.8 marker | 1 |
| placeholder | 0 |
| guided-mode toggle | **OK** (body class 切换 `guided-mode`) |
| lightbox open | **OK** (role=dialog 出现 1 次) |
| mobile 390 overflow | **0 px** ✓ |
| console errors | **[]** ✓ |

## No-touch confirmation (freeze round)

| 类别 | 状态 |
|---|---|
| v2.0 tag (`v2.0-public-portfolio-case`) | untouched (基线 9e6233a) |
| v2.6 tag (`v2.6-content-stable`) | untouched (基线 033b65e / 01cdaa2) |
| v2.7 tag (`v2.7-zh-exhibition-polish`) | untouched (基线 a0fee10 / f58f6b4^{}) |
| v2.8 tag (`v2.8-real-deep-content`) | untouched (基线 697560a / 65b4fbc^{}) |
| Old GitHub Releases (v2.0 / v2.6 / v2.7 / v2.8) | untouched |
| `site/index.html` | 不修改 (freeze round 仅文档) |
| `site/style.css` | 不修改 (audit round 也未修改) |
| `site/script.js` | 不修改 (audit round 也未修改) |
| `posts/` | 不修改 |
| `case-study/` | 不修改 |
| `release-assets/` 既有文件 | 不修改（仅新增 v2.9 manifest） |
| `_template/` | 不创建（按约束） |
| `_pilots/` | 不创建（按约束） |
| Untracked `.firecrawl/` | 不处理 |
| `git add .` | 不用 |

## Follow-up items

> 来自 [`docs/SOURCE_AUDIT_MANIFEST.md`](../docs/SOURCE_AUDIT_MANIFEST.md) 与 [`reports/leonardo_chinese_exhibition_v2_9_real_source_rights_audit_report.md`](../reports/leonardo_chinese_exhibition_v2_9_real_source_rights_audit_report.md)。

1. **联系 Museo Galileo 取得平台截图书面 reuse 答复**。当前 fair use / 评论性使用为基础，无书面许可存档
2. **决定 `platform-advanced-search.jpg` / `platform-comparative-study.jpg` 去留**（已下载但未引用）
3. **v3.0 之前为项目自绘 SVG 决定显式 LICENSE**（CC0 / CC-BY / 保留所有权利）
4. **馆藏机构级 reuse 政策的正式比对**（RCT Take Down Policy / Ambrosiana 等）
5. **任何未来新增图像 / 截图 / 自绘 SVG 必须重新走 audit round**

## Known note

Earlier phantom v2.9 / v3.x task histories were recorded as **phantom / unverified** in [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md). 本 v2.9 是从 verified `v2.8-real-deep-content` tag 真实重建的 source & rights audit，**不**复用任何 phantom 阶段叙述。下一 round 起点为本 tag。

GitHub Issues #1 / #2 / #3 / #4 全部保持 OPEN（与本 round 内容无直接关联）。Issue #1 标题「v2.7 Bilingual Edition」与实际做的「Chinese Exhibition Polish」命名不一致 —— 本 round **不**强行关闭 / 重命名，留给后续 round 单独处理。

## Files in this release

| 文件 | 角色 |
|---|---|
| `docs/RELEASE_NOTES_v2.9_REAL_SOURCE_RIGHTS_AUDIT.md` | 本文件 |
| `release-assets/v2.9-real-source-rights-audit-manifest.md` | release manifest |
| `reports/leonardo_chinese_exhibition_v2_9_real_stable_freeze_report.md` | freeze round 报告 |
| `README.md` | v2.9 Real Source & Rights Audit 小节更新 |

---

*v2.9-real-source-rights-audit 是真实 source & rights audit 的第一次正式 freeze。下一个 round（v3.0+）从本 tag 出发。*