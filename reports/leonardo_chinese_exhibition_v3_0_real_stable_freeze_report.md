# leonardo-chinese-exhibition v3.0 Real Stable Freeze Report

> 本报告记录 v3.0-real-stable-freeze round 的真实状态。所有数字均以本 round 实际 git tree / curl 实测为准。

## STATUS: PASS

## Round identity

| 项 | 值 |
|---|---|
| Round name | `v3.0-real-stable-freeze` |
| 上一 round | `v3.0-real-template-extraction-audit`（extraction round） |
| Extraction commit | `9aea3aed5d79a11f18f8715f51cfca6d350e3e04`（HEAD at round start） |
| Source tag | `v2.9-real-source-rights-audit` @ `a1e667e302d0d8106a9d0e4961159ae5c14aae4a` |
| Tag target SHA | `a1e667e302d0d8106a9d0e4961159ae5c14aae4a` |
| Tag object SHA | `13814d345bcd47860b778323c9915460ef72fb28` |
| Freeze commit | `fac3cea088ebbf8b9880e1f90911613300b8d0c1` |

## Baseline

| 项 | 实测 |
|---|---|
| HEAD before freeze round | `9aea3aed5d79a11f18f8715f51cfca6d350e3e04` |
| origin/main before freeze round | `9aea3aed5d79a11f18f8715f51cfca6d350e3e04` |
| Working tree | clean（仅 untracked `.firecrawl/`） |
| `git add .` 使用 | **未使用**（按约束） |
| Hermes 生产配置改动 | **无** |

## Live verification（round 起点 + 终点）

| 项 | 命令 | 实测 |
|---|---|---|
| Live URL | curl | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | `wc -c` | **92,976 B** |
| v2.9 real marker | `grep -c "v2.9-real-source-rights-audit"` | **1** |
| `image-placeholder-pro` | `grep -c` | **0** |
| `source-note` | `grep -c` | **14** |
| `credit-line` | `grep -c` | **13** |
| `script.js` HTTP | `curl -LIs` | **HTTP 200** |

> live 在 freeze round 起点和终点均为 92,976 B，**未发生任何 live 改动**。

## Template files（freeze round 实测）

| 项 | 实测 |
|---|---|
| `find _template -type f | wc -l` | **17** |
| `_template/` exists | ✓ |
| `_template/site/` exists | ✓ |
| `_template/data/` exists | ✓ |
| `_pilots/` exists | **✗**（按约束未创建，留给 v3.1） |

> **file count 修正说明**：extraction round brief / extraction round report 中曾写 18 个文件；freeze round 实测 `find _template -type f | wc -l` 为 **17**。本报告以 freeze round 实测为准，extraction round report 已最小 patch 修正（18 → 17 + freeze round 实测说明）。

## JSON validation

| 文件 | 命令 | 结果 |
|---|---|---|
| `_template/content.schema.json` | `python -m json.tool > /tmp/template-schema-check.json` | ✓ OK |
| `_template/data/exhibition.example.json` | `python -m json.tool` | ✓ OK |
| `_template/data/sections.example.json` | `python -m json.tool` | ✓ OK |
| `_template/data/glossary.example.json` | `python -m json.tool` | ✓ OK |
| `_template/data/assets.example.json` | `python -m json.tool` | ✓ OK |

**5/5 pass。**

## Template default content forbidden-term scan

| 范围 | 命中 |
|---|---|
| `_template/data/*.example.json`（4 个） | **0**（Leonardo / Codex Atlanticus / Royal Collection Trust / `thek@` 均无） ✓ |
| `_template/site/index.template.html`（实际渲染层，排除注释） | **0** ✓ |
| `_template/site/script.template.js`（实际渲染层，排除注释） | **0** ✓ |
| `_template/site/style.template.css` | **0** ✓ |
| `_template/README.md` / `_template/TEMPLATE_MANIFEST.md`（meta-docs） | 仅在"不引用 Leonardo"声明 + "source case"段落提及 ✓（允许） |

**template 默认 data + 实际渲染的 HTML / JS / CSS clean，无 Leonardo 项目专属词。**

## Release notes / manifest / README / reports（本 round 落地）

| 文件 | 类型 |
|---|---|
| `docs/RELEASE_NOTES_v3.0_REAL_TEMPLATE_EXTRACTION_AUDIT.md` | new |
| `release-assets/v3.0-real-template-extraction-audit-manifest.md` | new |
| `reports/leonardo_chinese_exhibition_v3_0_real_stable_freeze_report.md` | new（本文件） |
| `reports/leonardo_chinese_exhibition_v3_0_real_template_extraction_audit_report.md` | patched（file count 18 → 17 修正） |
| `README.md` | patched（v3.0 section 状态从 "In progress" → "stable freeze PASS"，补 tag / live URL / file count 17） |

## Tag / GitHub Release

| 项 | 状态 |
|---|---|
| `v3.0-real-template-extraction-audit` tag 本 round 新增 | ✓（freeze commit 后创建并 push） |
| `v3.0-real-template-extraction-audit` GitHub Release 新增 | ✓（用 `gh release create` + `docs/RELEASE_NOTES_*.md` notes-file） |
| 旧 v2.x tags（v2.0 / v2.6 / v2.7 / v2.8 / v2.9）未触碰 | ✓ |
| 旧 GitHub Releases（v2.0 / v2.6 / v2.7 / v2.8 / v2.9）未触碰 | ✓ |

## No-touch confirmation（freeze round）

| 路径 / 对象 | `git diff HEAD~1 HEAD -- ...` / 状态 |
|---|---|
| `site/index.html` | empty ✓ |
| `site/style.css` | empty ✓ |
| `site/script.js` | empty ✓ |
| `posts/` | empty ✓ |
| `case-study/` | empty ✓ |
| `release-assets/` 既有文件 | empty ✓ |
| `_template/` 既有文件（17 个） | empty（仅 freeze round 落地文件新增）✓ |
| `_pilots/` | 仍不存在 ✓ |
| `v2.0-public-portfolio-case` tag | SHA 不变 ✓ |
| `v2.6-content-stable` tag | SHA 不变 ✓ |
| `v2.7-zh-exhibition-polish` tag | SHA 不变 ✓ |
| `v2.8-real-deep-content` tag | SHA 不变 ✓ |
| `v2.9-real-source-rights-audit` tag | SHA 不变 ✓ |
| 旧 GitHub Releases | 未触碰 ✓ |
| Hermes 生产配置 | 未触碰 ✓ |
| untracked `.firecrawl/` | 未处理 ✓ |

## Known notes

- phantom v3.x 历史（`v3.0-source-rights-audit` / `v3.1-template-audit` / `v3.2-second-exhibition-pilot` / Issue #16 等）**不**作为本 round 基线
- extraction round brief 中 file count 18 为误写，freeze round 实测为 17；已在 extraction report 中最小 patch 修正
- `_template/site/` 是模板站点骨架，**不部署**到 live（与 live `site/` 物理隔离）

## Next recommended task

**v3.1-second-exhibition-pilot**：
- 起点：v3.0 freeze commit + `_template/` 已稳定
- 交付物：`_pilots/second-exhibition-pilot/`（基于 `_template/` 真实创建第一个 pilot）
- 不做的事：不动 live、不动 v2.9 内容、不创建第三个 pilot、不动 v3.0 tag
- 移交：Museo Galileo 截图书面 reuse / 2 unused 截图去留 / 项目 LICENSE / 馆藏 reuse 政策比对 / 新图必重 audit / `_template/site/` 补 README / ajv 校验留给具体项目

---

> 本报告由 v3.0-real-stable-freeze round 真实落地。