# v3.0 Real Template Extraction Audit Report

> 本 round 报告。所有数字均以本 round 实际 git tree / curl 实测为准。

## STATUS: **PASS**（候选；待本 round 提交 + push + Actions success 后最终确认）

## Baseline

| 项 | 实测 |
|---|---|
| HEAD before round | `8e1fdfdf7905fb4f95ffd0284814ebe2d79434d4` |
| origin/main before round | `8e1fdfdf7905fb4f95ffd0284814ebe2d79434d4` |
| Working tree | clean（round 起点允许 untracked `.firecrawl/`） |

## Source tag

- `v2.9-real-source-rights-audit` @ `a1e667e302d0d8106a9d0e4961159ae5c14aae4a`
- tag object: `13814d345bcd47860b778323c9915460ef72fb28`
- 起点：v2.9 已 freeze + 已发布 GitHub Release + live 92,976 B

## Live verification (round start)

| 项 | 命令 | 实测 |
|---|---|---|
| Live URL | curl | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | `wc -c` | **92,976 B** |
| v2.9 real marker | `grep -c "v2.9-real-source-rights-audit"` | **1** |
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | **1** (preserved) |
| phantom v2.9 marker | `grep -c "v2.9-source-rights-audit"` | **0** |
| `image-placeholder-pro` | `grep -c` | **0** |
| `source-note` | `grep -c` | **14** |
| `credit-line` | `grep -c` | **13** |
| `script.js` HTTP | `curl -LIs` | **HTTP 200** |

## `_template/` created（真实创建）

| 路径 | 类型 | 大小 |
|---|---|---|
| `_template/README.md` | new | 6,736 B |
| `_template/TEMPLATE_MANIFEST.md` | new | 4,556 B |
| `_template/content.schema.json` | new | 7,215 B |
| `_template/source-manifest.example.md` | new | 2,605 B |
| `_template/rights-and-sources.example.md` | new | 2,399 B |
| `_template/visitor-guide.example.md` | new | 1,506 B |
| `_template/curatorial-essay.example.md` | new | 2,033 B |
| `_template/deep-research-notes.example.md` | new | 1,356 B |
| `_template/release-notes.example.md` | new | 2,062 B |
| `_template/stable-freeze-report.example.md` | new | 2,884 B |
| `_template/data/exhibition.example.json` | new | 480 B |
| `_template/data/sections.example.json` | new | 3,043 B |
| `_template/data/glossary.example.json` | new | 1,441 B |
| `_template/data/assets.example.json` | new | 2,957 B |
| `_template/site/index.template.html` | new | 9,365 B |
| `_template/site/style.template.css` | new | 8,967 B |
| `_template/site/script.template.js` | new | 6,711 B |
| **共 17 个文件**（v3.0 freeze round 实测 `find _template -type f | wc -l`；此前 round brief 中误写 18，本报告以 freeze round 实测为准） | | |

## JSON validation

| 文件 | 命令 | 结果 |
|---|---|---|
| `_template/content.schema.json` | `python -m json.tool > /tmp/template-schema-check.json` | OK (11,809 B 输出) |
| `_template/data/exhibition.example.json` | `python -m json.tool` | OK |
| `_template/data/sections.example.json` | `python -m json.tool` | OK |
| `_template/data/glossary.example.json` | `python -m json.tool` | OK |
| `_template/data/assets.example.json` | `python -m json.tool` | OK |

**所有 5 个 JSON 文件通过 lint / json.tool 校验。**

## Template default content forbidden-term scan

| 范围 | 扫描词 | 结果 |
|---|---|---|
| `_template/data/*.example.json` | Leonardo / Codex Atlanticus / Royal Collection Trust / Leonardo//thek@ | **(none)** ✓ |
| `_template/site/index.template.html` (排除 `<!-- -->` 注释) | Leonardo / Codex Atlanticus / Royal Collection Trust | **(none)** ✓ |
| `_template/site/script.template.js` (排除 `/* */` 注释) | Leonardo / Codex Atlanticus / Royal Collection Trust | **(none)** ✓ |
| `_template/README.md` 全文 | 全部 4 个词 | 仅在 "**NOT** allowed" 列表 + "source case" 段落提及 ✓ |
| `_template/TEMPLATE_MANIFEST.md` 全文 | Leonardo | 仅在 "不含 Leonardo 专属内容" / "无 Leonardo 专属选择器" 描述中 ✓ |

**template 默认内容（data + 实际渲染的 HTML/JS）clean，无 Leonardo 项目专属词。**  
**docs mention as source case 是允许的（README / MANIFEST / 提取审计 / 路线图）。**  
**template default content clean 是 hard requirement（已达成）。**

## Docs created

| 文件 | 类型 | 大小 |
|---|---|---|
| `docs/TEMPLATE_EXTRACTION_AUDIT.md` | new | 8,071 B |
| `docs/REUSABLE_EXHIBITION_COMPONENTS.md` | new | 6,437 B |
| `docs/V3_TEMPLATE_ROADMAP.md` | new | 3,631 B |

## README.md updated

| 文件 | 操作 | +lines |
|---|---|---|
| `README.md` | patched（追加 v3.0 Real Template Extraction Audit 小节，位于 `## 当前版本` 之前） | +24 lines |

## Live site no-change confirmation

| 文件 | `git diff HEAD --` |
|---|---|
| `site/index.html` | empty ✓ |
| `site/style.css` | empty ✓ |
| `site/script.js` | empty ✓ |
| `posts/` | empty ✓ |
| `case-study/` | empty ✓ |
| `release-assets/` 既有文件 | empty ✓ |

## Old tags untouched

| Tag | SHA | 状态 |
|---|---|---|
| `v2.0-public-portfolio-case` | `9e6233a` | ✓ unchanged |
| `v2.6-content-stable` | `033b65e` / `01cdaa2` | ✓ unchanged |
| `v2.7-zh-exhibition-polish` | `a0fee10` / `f58f6b4` | ✓ unchanged |
| `v2.8-real-deep-content` | `697560a` / `65b4fbc` | ✓ unchanged |
| `v2.9-real-source-rights-audit` | `13814d3` / `a1e667e` | ✓ unchanged |

## Old releases untouched

| Release | Published at | 状态 |
|---|---|---|
| v2.0 — 达·芬奇的纸上宇宙 | 2026-07-06T02:56:01Z | ✓ untouched |
| v2.6 Content Stable | 2026-07-06T09:14:37Z | ✓ untouched |
| v2.7 Zh Exhibition Polish | 2026-07-06T23:00:37Z | ✓ untouched |
| v2.8 Real Deep Content | 2026-07-07T05:56:50Z | ✓ untouched |
| v2.9 Real Source & Rights Audit | 2026-07-07T10:20:22Z | ✓ untouched |

## No-touch confirmation

- `site/index.html` ✓ untouched
- `site/style.css` ✓ untouched
- `site/script.js` ✓ untouched
- `posts/` ✓ untouched
- `case-study/` ✓ untouched
- `release-assets/` 既有文件 ✓ untouched
- v2.0 tag ✓ untouched
- v2.6 tag ✓ untouched
- v2.7 tag ✓ untouched
- v2.8 tag ✓ untouched
- v2.9 tag ✓ untouched
- 旧 GitHub Releases ✓ untouched
- `_pilots/` ✓ **不存在**（按约束未创建）
- `git add .` ✓ 未使用
- untracked `.firecrawl/` ✓ 未处理
- Hermes 生产配置 ✓ 未触碰

## Files staged in this round（22 个）

```
_template/README.md
_template/TEMPLATE_MANIFEST.md
_template/content.schema.json
_template/source-manifest.example.md
_template/rights-and-sources.example.md
_template/visitor-guide.example.md
_template/curatorial-essay.example.md
_template/deep-research-notes.example.md
_template/release-notes.example.md
_template/stable-freeze-report.example.md
_template/data/exhibition.example.json
_template/data/sections.example.json
_template/data/glossary.example.json
_template/data/assets.example.json
_template/site/index.template.html
_template/site/style.template.css
_template/site/script.template.js
docs/TEMPLATE_EXTRACTION_AUDIT.md
docs/REUSABLE_EXHIBITION_COMPONENTS.md
docs/V3_TEMPLATE_ROADMAP.md
README.md
reports/leonardo_chinese_exhibition_v3_0_real_template_extraction_audit_report.md
```

## Commit & Push

- Commit message: `Extract reusable exhibition template from verified v2.9`
- Push target: `origin main`
- GitHub Actions: Deploy GitHub Pages（待 push 后验证）

## Follow-up items

- **v3.0-real-stable-freeze**：下一 round 独立 freeze `v3.0-real-template-extraction-audit` tag + GitHub Release
- `_template/site/` 是否需要增加 README（说明模板站点不被部署）— 下一 round 视情况补
- 模板 JSON schema 是否引入 ajv / jsonschema 等运行时校验 — 留给具体项目
- 自制 SVG 许可证统一（推荐 CC0 1.0）— 留给具体项目
- 是否补 `assets/diagrams/` 真实占位 SVG 文件 — 当前模板用 path 占位，不附带文件；下一 round 视情况补

## Known notes

- phantom v3.x 历史（v3.0-source-rights-audit / v3.1-template-audit / v3.2-second-exhibition-pilot / Issue #16 等）**不**作为本 round 基线
- phantom `_template/` / `_pilots/` "已存在" **不**作为本 round 基线
- 本 round `_template/` **真实创建**于 verified v2.9 之上

## Next recommended task

**v3.0-real-stable-freeze**：
- 起点：本 round 创建的 `_template/` HEAD
- 交付物：tag `v3.0-real-template-extraction-audit` + GitHub Release + freeze report
- 不做的事：不创建 `_pilots/`，不修改 live

---

> 本报告由 v3.0-real-template-extraction-audit 真实创建。