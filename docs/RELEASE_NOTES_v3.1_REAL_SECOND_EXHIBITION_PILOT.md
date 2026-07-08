# v3.1 Real Second Exhibition Pilot — Release Notes

Live:
https://conanxin.github.io/leonardo-chinese-exhibition/

Tag:
`v3.1-real-second-exhibition-pilot`

Verified live byte size:
**92,976 B**

Source tag:
`v3.0-real-template-extraction-audit` @ `dd7d589f8db1417c00c539230849ed3f89d8a0d7`

Pilot commit:
`ae1a54ea00918517f10516f301b84f0d2b8dee34`（v3.1 pilot round HEAD）

Freeze commit:
`de017f91c605ab65276283cb7a006164980f1986`

---

## What changed

v3.1 Real Second Exhibition Pilot 是基于真实 `_template/` 的**第一个 repository-only pilot**。

它创建 `_pilots/second-exhibition-pilot/`，用于验证中文数字展览模板能否独立组织一个小型研究型展览。**pilot 不部署到 live**。

主要内容：

- 创建 `_pilots/second-exhibition-pilot/`（18 个文件，物理隔离于 live）
- 创建 pilot site / data / docs / SVG diagrams
- Pilot 主题：**《一件作品的旅程》** — 从图像、来源、路径到知识网络
- Pilot 版本：**pilot-v0.1**
- 使用 3 个 project-generated SVG diagrams
- 使用 4 个 JSON data files
- 创建 source / rights / curatorial / research / release docs
- local render check **PASS**（Playwright，desktop + mobile 390，无 overflow，0 console errors）
- **不部署** pilot
- **不修改** live site
- **不修改** `_template/`

## Pilot summary

| 项 | 实测 |
|---|---|
| Pilot path | `_pilots/second-exhibition-pilot/` |
| Pilot files count | **18**（实测 `find _pilots/second-exhibition-pilot -type f | wc -l`） |
| SVG diagrams | 3（object-journey / evidence-chain / viewing-map） |
| JSON validation | 4/4 pass（exhibition / sections / glossary / assets） |
| Section count | 4（起点 / 流转 / 阅读 / 展示） |
| Artifact cards | 4 |
| Glossary items | 6 |
| Deep block types | deep-reading / material-evidence / visual-thinking / research-model（section-01 含全部 4 个） |
| pilot-v0.1 marker | 4 处（hero / footer / script.js console / metadata） |
| Forbidden terms (内容层 site+data+SVG) | **0** |
| Forbidden terms (元数据层) | 仅在"不引用"审计凭证 / 项目识别中出现（与 v3.0 meta-docs 前例一致） |
| Live 部署 | **否**（repository only） |

## Verification

| 项 | 命令 | 实测 |
|---|---|---|
| Live HTTP | `curl -LIs` | HTTP 200 |
| Live byte size | `wc -c` | **92,976 B** |
| v2.9 real marker | `grep -c "v2.9-real-source-rights-audit"` | **1** |
| `image-placeholder-pro` | `grep -c` | **0** |
| `source-note` | `grep -c` | **14** |
| `credit-line` | `grep -c` | **13** |
| Pilot title in live HTML | `grep -c "一件作品的旅程"` | **0**（pilot 不部署） |
| `script.js` HTTP | `curl -LIs` | **HTTP 200** |
| Pilot JSON validation | `python -m json.tool` × 4 | 4/4 pass |
| Local render (Playwright) | chromium @ 1280 + 390 | **PASS**（0 console errors, no overflow, 4 cards, 6 glossary, 4 block types） |
| `site/index.html` / `style.css` / `script.js` in v3.1 round | `git diff HEAD~1 HEAD -- site/` | empty ✓ |
| `_template/` in v3.1 round | `git diff HEAD~1 HEAD -- _template/` | empty ✓ |

## No-touch confirmation

- `v2.0-public-portfolio-case` tag ✓ untouched
- `v2.6-content-stable` tag ✓ unmoved
- `v2.7-zh-exhibition-polish` tag ✓ unmoved
- `v2.8-real-deep-content` tag ✓ unmoved
- `v2.9-real-source-rights-audit` tag ✓ unmoved
- `v3.0-real-template-extraction-audit` tag ✓ unmoved
- 旧 GitHub Releases（v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0）✓ untouched
- live site `site/index.html` / `style.css` / `script.js` ✓ unchanged
- `_template/` 17 文件 ✓ unchanged
- `posts/` ✓ untouched
- `case-study/` ✓ untouched
- `release-assets/` 既有文件 ✓ untouched
- `_pilots/second-exhibition-pilot/` 内容 ✓ unchanged（除 v3.1 round 自身原本的新增文件外，本 freeze round 未做任何内容回填）
- `git add .` ✓ 未使用
- untracked `.firecrawl/` ✓ 未处理
- Hermes 生产配置 ✓ 未触碰

## Known note

This release documents a **repository-only pilot**. The pilot is not deployed and should not be treated as live exhibition content. The `liveUrl` field in `data/exhibition.json` is a generic schema placeholder (`https://example.com/pilot-second-exhibition/`) and does not point to any real URL.

The pilot exists as proof that the `_template/` can be instantiated into a small, self-contained research-style exhibition without modifying the live site or the template itself.

## Follow-up（移交 v3.2+）

- **v3.2-template-documentation**：写完整使用手册（usage / authoring / rights checklist / pilot workflow / release workflow），把 v3.0 + v3.1 跑通过程沉淀为可复用文档
- 长期：跑更多 pilot（不同主题 / 不同策展视角 / 不同 source / rights 状态）验证模板边界
- `_template/site/` 是否补 README（说明模板站点不被部署）— 由 v3.2 决定
- ajv / jsonschema 运行时校验 — 由具体项目决定

## Manifest

详见 [`release-assets/v3.1-real-second-exhibition-pilot-manifest.md`](../release-assets/v3.1-real-second-exhibition-pilot-manifest.md)。
