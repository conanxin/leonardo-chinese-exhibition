# v3.0 Real Template Extraction Audit — Release Notes

Live:
https://conanxin.github.io/leonardo-chinese-exhibition/

Tag:
`v3.0-real-template-extraction-audit`

Verified live byte size:
**92,976 B**（v3.0 round 起点 + freeze round live 均未修改）

Source tag:
`v2.9-real-source-rights-audit` @ `a1e667e302d0d8106a9d0e4961159ae5c14aae4a`

Extraction commit:
`9aea3aed5d79a11f18f8715f51cfca6d350e3e04`（v3.0 extraction round HEAD）

Freeze commit:
`beb2d7b132948fb98ffb0019105ca633ecb980fa`

---

## What changed

v3.0 Real Template Extraction Audit 是基于真实 `v2.9-real-source-rights-audit` tag 的**模板提取审计版**。

它**不修改 live site**，**不创建 pilot**，**不引用任何 phantom v3.x 历史**。

主要交付物：

- 创建 `_template/` 模板骨架（17 个文件，实测 `find _template -type f | wc -l`）
- 创建 `_template/site/` 最小 HTML / CSS / JS 模板（与 live 物理隔离，不部署）
- 创建 `_template/content.schema.json`（JSON schema，5/5 通过 `python -m json.tool` 校验）
- 创建 4 个 example data JSON（exhibition / sections / glossary / assets，5/5 通过 lint）
- 创建 7 个 markdown 文档模板（source-manifest / rights-and-sources / visitor-guide / curatorial-essay / deep-research-notes / release-notes / stable-freeze-report）
- 创建 `docs/TEMPLATE_EXTRACTION_AUDIT.md`（v3.0 提取审计）
- 创建 `docs/REUSABLE_EXHIBITION_COMPONENTS.md`（可复用组件分级表）
- 创建 `docs/V3_TEMPLATE_ROADMAP.md`（v3 路线图）
- `README.md` 增补 v3.0 小节
- `reports/leonardo_chinese_exhibition_v3_0_real_template_extraction_audit_report.md` 已有；freeze round 修正 file count 18 → 17（实测）
- `reports/leonardo_chinese_exhibition_v3_0_real_stable_freeze_report.md`（本轮新增）

## Template summary

| 项 | 实测 |
|---|---|
| `_template/` exists | ✓ |
| `_template/site/` exists | ✓ |
| `_template/data/` exists | ✓ |
| Template files count | **17**（`find _template -type f | wc -l`） |
| JSON validation | 5/5 pass（`content.schema.json` + 4 个 example data JSON） |
| Default template data clean | ✓（4 个 `data/*.example.json` 0 命中 Leonardo / Codex Atlanticus / Royal Collection Trust / `thek@`） |
| Default template render layer clean | ✓（`site/*.template.*` 实际渲染内容 0 命中；meta 注释中"不引用 Leonardo"声明除外） |

## Verification

| 项 | 命令 | 实测 |
|---|---|---|
| Live HTTP | `curl -LIs` | HTTP 200 |
| Live byte size | `wc -c` | **92,976 B** |
| v2.9 real marker | `grep -c "v2.9-real-source-rights-audit"` | **1** |
| `image-placeholder-pro` | `grep -c` | **0** |
| `source-note` | `grep -c` | **14** |
| `credit-line` | `grep -c` | **13** |
| `script.js` HTTP | `curl -LIs` | **HTTP 200** |
| `site/index.html` 改动 | `git diff HEAD~1 HEAD -- site/index.html` | **empty** |
| `site/style.css` 改动 | `git diff HEAD~1 HEAD -- site/style.css` | **empty** |
| `site/script.js` 改动 | `git diff HEAD~1 HEAD -- site/script.js` | **empty** |
| `posts/` 改动 | `git diff HEAD~1 HEAD -- posts/` | **empty** |
| `case-study/` 改动 | `git diff HEAD~1 HEAD -- case-study/` | **empty** |

> `site/index.html` / `style.css` / `script.js` 在 v3.0 extraction round 和 v3.0 freeze round 均零修改。

## No-touch confirmation

- `v2.0-public-portfolio-case` tag ✓ untouched
- `v2.6-content-stable` tag ✓ unmoved
- `v2.7-zh-exhibition-polish` tag ✓ unmoved
- `v2.8-real-deep-content` tag ✓ unmoved
- `v2.9-real-source-rights-audit` tag ✓ unmoved
- 旧 GitHub Releases（v2.0 / v2.6 / v2.7 / v2.8 / v2.9）✓ untouched
- live site `site/index.html` / `style.css` / `script.js` ✓ unchanged
- `posts/` ✓ untouched
- `case-study/` ✓ untouched
- `release-assets/` 既有文件 ✓ untouched
- `_pilots/` ✓ **不存在**（按约束未创建；留给 v3.1）
- Hermes 生产配置 ✓ 未触碰
- `git add .` ✓ 未使用
- untracked `.firecrawl/` ✓ 未处理

## Known note

Earlier phantom v3.x histories（`v3.0-source-rights-audit` / `v3.1-template-audit` / `v3.2-second-exhibition-pilot` / Issue #16 等）remain unverified and are **not** used as this release baseline. This v3.0 is rebuilt from verified `v2.9-real-source-rights-audit`.

## Follow-up（移交 v3.1+）

- v3.1: 创建 `_pilots/second-exhibition-pilot/`（基于 `_template/`）
- v3.0+ 后续可能：补 `_template/site/README.md`（说明模板站点不被部署）、ajv 校验脚本、Museo Galileo / British Library 截图书面 reuse、二次审计新图、模板 LICENSE

## Manifest

详见 [`release-assets/v3.0-real-template-extraction-audit-manifest.md`](../release-assets/v3.0-real-template-extraction-audit-manifest.md)。