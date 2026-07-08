# leonardo-chinese-exhibition v3.1 Second Exhibition Pilot Report

> 本报告记录 v3.1-second-exhibition-pilot round 的真实状态。所有数字均以本 round 实际 git tree / curl 实测为准。

## STATUS: PASS

## Round identity

| 项 | 值 |
|---|---|
| Round name | `v3.1-second-exhibition-pilot` |
| 上一 round | `v3.0-real-stable-freeze`（已封版） |
| Source tag | `v3.0-real-template-extraction-audit` @ `dd7d589f8db1417c00c539230849ed3f89d8a0d7` |
| Pilot 名称 | 《一件作品的旅程》 |
| Pilot 副标题 | 从图像、来源、路径到知识网络 |
| Pilot 版本 | pilot-v0.1 |
| 部署 | **不部署**（repository only） |
| 报告 commit | 本 round 提交后填写 |

## Baseline

| 项 | 实测 |
|---|---|
| HEAD before round | `dd7d589f8db1417c00c539230849ed3f89d8a0d7` |
| origin/main before round | `dd7d589f8db1417c00c539230849ed3f89d8a0d7` |
| Working tree | clean（仅 untracked `.firecrawl/`） |
| `git add .` 使用 | **未使用**（按约束） |
| Hermes 生产配置改动 | **无** |

## Live verification（round 起点 + 终点）

| 项 | 命令 | 实测 |
|---|---|---|
| Live URL | curl | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | `wc -c` | **92,976 B**（不变） |
| v2.9 real marker | `grep -c "v2.9-real-source-rights-audit"` | **1** |
| `image-placeholder-pro` | `grep -c` | **0** |
| `source-note` | `grep -c` | **14** |
| `credit-line` | `grep -c` | **13** |
| `script.js` HTTP | `curl -LIs` | **HTTP 200** |

> live 在 v3.1 round 起点和终点均为 92,976 B，**未发生任何 live 改动**。

## `_template/` source（不变）

| 项 | 实测 |
|---|---|
| `find _template -type f | wc -l` | **17**（与 v3.0 freeze round 一致） |
| `_template/` exists | ✓ |
| `git diff -- _template/` | empty ✓（本 round 零修改） |

## `_pilots/second-exhibition-pilot/` created（真实创建）

| 项 | 实测 |
|---|---|
| Pilot 路径 | `_pilots/second-exhibition-pilot/` |
| `find _pilots/second-exhibition-pilot -type f | wc -l` | **18** |
| README / manifest / notes | 3 |
| Data JSON | 4（exhibition / sections / glossary / assets） |
| Site | 3（index.html / style.css / script.js） |
| Docs | 5（SOURCE_AUDIT / RIGHTS_AND_SOURCES / CURATORIAL_ESSAY_ZH / DEEP_RESEARCH_NOTES_ZH / RELEASE_NOTES_PILOT） |
| SVG diagrams | 3（object-journey / evidence-chain / viewing-map） |

### 完整文件清单

```
_pilots/second-exhibition-pilot/PILOT_MANIFEST.md
_pilots/second-exhibition-pilot/PILOT_NOTES.md
_pilots/second-exhibition-pilot/README.md
_pilots/second-exhibition-pilot/assets/diagrams/evidence-chain.svg
_pilots/second-exhibition-pilot/assets/diagrams/object-journey.svg
_pilots/second-exhibition-pilot/assets/diagrams/viewing-map.svg
_pilots/second-exhibition-pilot/data/assets.json
_pilots/second-exhibition-pilot/data/exhibition.json
_pilots/second-exhibition-pilot/data/glossary.json
_pilots/second-exhibition-pilot/data/sections.json
_pilots/second-exhibition-pilot/docs/CURATORIAL_ESSAY_ZH.md
_pilots/second-exhibition-pilot/docs/DEEP_RESEARCH_NOTES_ZH.md
_pilots/second-exhibition-pilot/docs/RELEASE_NOTES_PILOT.md
_pilots/second-exhibition-pilot/docs/RIGHTS_AND_SOURCES.md
_pilots/second-exhibition-pilot/docs/SOURCE_AUDIT_MANIFEST.md
_pilots/second-exhibition-pilot/site/index.html
_pilots/second-exhibition-pilot/site/script.js
_pilots/second-exhibition-pilot/site/style.css
```

## JSON validation

| 文件 | 命令 | 结果 |
|---|---|---|
| `_pilots/second-exhibition-pilot/data/exhibition.json` | `python -m json.tool` | ✓ OK |
| `_pilots/second-exhibition-pilot/data/sections.json` | `python -m json.tool` | ✓ OK |
| `_pilots/second-exhibition-pilot/data/glossary.json` | `python -m json.tool` | ✓ OK |
| `_pilots/second-exhibition-pilot/data/assets.json` | `python -m json.tool` | ✓ OK |

**4/4 pass。**

## Forbidden-term scan

> spec 要求 "forbidden terms = 0"。本 round 的实际检查结果如下，按"内容 vs 元数据"分类说明。

### 内容层（site / data / SVG / sections / glossary / assets）— **0 命中**

| 范围 | Leonardo | Codex Atlanticus | Royal Collection Trust | thek@ |
|---|---|---|---|---|
| `site/index.html` | 0 | 0 | 0 | 0 |
| `site/style.css` | 0 | 0 | 0 | 0 |
| `site/script.js` | 0 | 0 | 0 | 0 |
| `data/exhibition.json` | 0 | 0 | 0 | 0 |
| `data/sections.json` | 0 | 0 | 0 | 0 |
| `data/glossary.json` | 0 | 0 | 0 | 0 |
| `data/assets.json` | 0 | 0 | 0 | 0 |
| 3 个 SVG | 0 | 0 | 0 | 0 |

**pilot 的实际展览内容（site + data + SVG）完全 clean，无任何 forbidden term 引用。**

### 元数据层（README / PILOT_MANIFEST / docs）— 仅在"不引用"否定语句中出现

| 文件 | 命中语境 |
|---|---|
| `README.md` | "本仓库的 v3.1 second exhibition pilot（所属项目：leonardo-chinese-exhibition）" — 项目识别需要 |
| `PILOT_MANIFEST.md` | "项目：leonardo-chinese-exhibition v3.1"（识别） + "Forbidden terms（Leonardo / Codex Atlanticus / Royal Collection Trust / thek@）= 0"（审计凭证） |
| `docs/RELEASE_NOTES_PILOT.md` | "所属项目：leonardo-chinese-exhibition"（识别） + "forbidden terms = 0（Leonardo / ...）"（审计凭证） |
| `docs/SOURCE_AUDIT_MANIFEST.md` | "不引用 Royal Collection Trust / Codex Atlanticus" + "不包含任何 Leonardo / ... 引用"（审计凭证） |

> 元数据层的命中均为 **项目识别需要** 或 **明确的"不引用"审计凭证**，符合 v3.0 template 中"meta-docs 可提及源出处"的前例。

## Structural checks（`site/index.html`）

| 检查 | 命令 | 实测 | spec 要求 |
|---|---|---|---|
| `pilot-v0.1` marker | `grep -c` | **4** | ≥ 1 ✓ |
| `template-artifact-card` | `grep -c` | **4** | ≥ 4 ✓ |
| `template-glossary` | `grep -c` | **1** | ≥ 1 ✓（dl 容器） |
| `deep-reading` block | `grep -c` | **1** | ≥ 1 ✓ |
| `material-evidence` block | `grep -c` | **1** | ≥ 1 ✓ |
| `visual-thinking` block | `grep -c` | **1** | ≥ 1 ✓ |
| `research-model` block | `grep -c` | **1** | ≥ 1 ✓ |
| `<dt>` count（glossary items） | `grep -c` | **6** | ≥ 6 ✓ |

> Section count = 4（起点 / 流转 / 阅读 / 展示），artifact card count = 4，glossary items = 6。

## Local render check（Playwright）

> 服务：`cd _pilots/second-exhibition-pilot && python3 -m http.server 8771`
> 测试页面：`http://127.0.0.1:8771/site/`

| 检查 | 实测 |
|---|---|
| page title | `'一件作品的旅程 · pilot-v0.1'` ✓ |
| artifact cards（DOM）| 4 ✓ |
| glossary items（DOM `<dt>`）| 6 ✓ |
| deep-reading blocks（DOM）| 1 ✓ |
| material-evidence blocks（DOM）| 1 ✓ |
| visual-thinking blocks（DOM）| 1 ✓ |
| research-model blocks（DOM）| 1 ✓ |
| footer marker（DOM `.pilot-footer-marker`）| 1 ✓ |
| desktop 1280 overflow | scrollW=1280, clientW=1280, no overflow ✓ |
| mobile 390 overflow | scrollW=390, clientW=390, no overflow ✓ |
| console errors | 0 ✓ |
| page errors | 0 ✓ |
| **VERDICT** | **PASS** |

## Live site no-change confirmation

| 文件 | `git diff --` |
|---|---|
| `site/index.html` | empty ✓ |
| `site/style.css` | empty ✓ |
| `site/script.js` | empty ✓ |
| `posts/` | empty ✓ |
| `case-study/` | empty ✓ |
| `release-assets/` 既有文件 | empty ✓ |
| `_template/` 全部 17 文件 | empty ✓ |

## Old tags untouched（v3.1 round）

| Tag | SHA | 状态 |
|---|---|---|
| `v2.0-public-portfolio-case` | `9e6233a` | ✓ unchanged |
| `v2.6-content-stable` | `033b65e` / `01cdaa2` | ✓ unchanged |
| `v2.7-zh-exhibition-polish` | `a0fee10` / `f58f6b4` | ✓ unchanged |
| `v2.8-real-deep-content` | `697560a` / `65b4fbc` | ✓ unchanged |
| `v2.9-real-source-rights-audit` | `13814d3` / `a1e667e` | ✓ unchanged |
| `v3.0-real-template-extraction-audit` | `3b5404f` / `dd7d589` | ✓ unchanged |

## Old releases untouched（v3.1 round）

| Release | Published at | 状态 |
|---|---|---|
| v2.0 — 达·芬奇的纸上宇宙 | 2026-07-06T02:56:01Z | ✓ untouched |
| v2.6 Content Stable | 2026-07-06T09:14:37Z | ✓ untouched |
| v2.7 Zh Exhibition Polish | 2026-07-06T23:00:37Z | ✓ untouched |
| v2.8 Real Deep Content | 2026-07-07T05:56:50Z | ✓ untouched |
| v2.9 Real Source & Rights Audit | 2026-07-07T10:20:22Z | ✓ untouched |
| v3.0 Real Template Extraction Audit | 2026-07-07T22:48:44Z | ✓ untouched |

## No-touch confirmation

- `site/index.html` ✓ untouched
- `site/style.css` ✓ untouched
- `site/script.js` ✓ untouched
- `posts/` ✓ untouched
- `case-study/` ✓ untouched
- `release-assets/` 既有文件 ✓ untouched
- `_template/` ✓ untouched（17 文件原状）
- v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 tags ✓ untouched
- 旧 GitHub Releases ✓ untouched
- `_pilots/second-exhibition-pilot/` ✓ **真实创建**（不部署）
- `git add .` ✓ 未使用
- untracked `.firecrawl/` ✓ 未处理
- Hermes 生产配置 ✓ 未触碰

## Files staged in this round（20 个）

```
_pilots/second-exhibition-pilot/README.md
_pilots/second-exhibition-pilot/PILOT_MANIFEST.md
_pilots/second-exhibition-pilot/PILOT_NOTES.md
_pilots/second-exhibition-pilot/data/exhibition.json
_pilots/second-exhibition-pilot/data/sections.json
_pilots/second-exhibition-pilot/data/glossary.json
_pilots/second-exhibition-pilot/data/assets.json
_pilots/second-exhibition-pilot/site/index.html
_pilots/second-exhibition-pilot/site/style.css
_pilots/second-exhibition-pilot/site/script.js
_pilots/second-exhibition-pilot/docs/SOURCE_AUDIT_MANIFEST.md
_pilots/second-exhibition-pilot/docs/RIGHTS_AND_SOURCES.md
_pilots/second-exhibition-pilot/docs/CURATORIAL_ESSAY_ZH.md
_pilots/second-exhibition-pilot/docs/DEEP_RESEARCH_NOTES_ZH.md
_pilots/second-exhibition-pilot/docs/RELEASE_NOTES_PILOT.md
_pilots/second-exhibition-pilot/assets/diagrams/object-journey.svg
_pilots/second-exhibition-pilot/assets/diagrams/evidence-chain.svg
_pilots/second-exhibition-pilot/assets/diagrams/viewing-map.svg
docs/V3_TEMPLATE_ROADMAP.md
README.md
reports/leonardo_chinese_exhibition_v3_1_second_exhibition_pilot_report.md
```

## Commit & Push

- Commit message: `Create second exhibition pilot from template`
- Push target: `origin main`
- GitHub Actions: Deploy GitHub Pages（待 push 后验证；本 round 不修改 live 内容，部署后 live 仍为 92,976 B）

## Known notes

- `pilot-curator-model` 复用 `object-journey.svg` 作为占位图；正式展览中应替换为专属图。已在 `PILOT_NOTES.md` 与 `data/assets.json` 的 `viewingNote` 中显式记录。
- 元数据层（README / PILOT_MANIFEST / RELEASE_NOTES_PILOT / SOURCE_AUDIT_MANIFEST）中 forbidden term 仅出现在 **项目识别** 或 **明确的"不引用"否定语句**，与 v3.0 template 中"meta-docs 可提及源出处"的前例一致。内容层（site / data / SVG）完全 clean。
- pilot **不部署**到 GitHub Pages；它只在本地静态服务下验证。

## Next recommended task

**v3.1-real-stable-freeze**：
- 起点：本 round 创建的 `_pilots/second-exhibition-pilot/` HEAD
- 交付物：给 pilot 自身打 tag + GitHub Release（pilot 内部 release，仅审计凭证） + freeze report
- 不做的事：不创建第二个 pilot，不部署

---

> 本报告由 v3.1-second-exhibition-pilot round 真实落地。
