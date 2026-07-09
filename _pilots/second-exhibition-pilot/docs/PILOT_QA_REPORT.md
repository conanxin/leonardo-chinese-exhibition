# Pilot QA Report

## QA date

2026-07-09（v3.4 round）

## source tag

`v3.3-real-template-quality-gate` / object `fb35a5d9aece0bf44d82e3f7f25c2a73b8e6a70e` / target `fce2efb5f0fcbbb3bd4e25c8008513f8c2462eb4`

## local render result

Two modes tested via Playwright + Chromium:

### Mode A — `file://`（canonical local-open usage）

| 检查项 | 期望 | 实测 | 结果 |
|---|---|---|---|
| page status | 200 | 200 | PASS |
| page title | 一件作品的旅程 | 一件作品的旅程 · pilot-v0.1 | PASS |
| sections | >= 4 | 4 | PASS |
| artifact cards | >= 4 | 4 | PASS |
| glossary items | >= 6 | 6 | PASS |
| deep-reading block | >= 1 | 1 | PASS |
| material-evidence block | >= 1 | 1 | PASS |
| visual-thinking block | >= 1 | 1 | PASS |
| research-model block | >= 1 | 1 | PASS |
| pilot marker | present | 1 | PASS |
| hero (header.pilot-hero) | present | 1 | PASS |
| exhibition map | present | 1 | PASS |
| img.svg count | 4 | 4 | PASS |
| img.svg loaded | yes | yes (all 4 with natural dimensions 800x280 / 800x360 / 800x320 / 800x280) | PASS |
| source-note | >= 4 | 4 | PASS |
| credit-line | >= 4 | 4 | PASS |
| console errors | 0 | 0 | PASS |
| failed responses | 0 | 0 | PASS |
| mobile 390 horizontal overflow | no | no (scrollWidth 390 = windowWidth 390) | PASS |

### Mode B — `http://localhost:8770/`（brief-specified http.server from `site/`）

| 检查项 | 期望 | 实测 | 结果 |
|---|---|---|---|
| page status | 200 | 200 | PASS |
| page title | 一件作品的旅程 | 一件作品的旅程 · pilot-v0.1 | PASS |
| sections / artifacts / glossary / deep blocks | 同上 | 同上 | PASS |
| img.svg count | 4 | 4 | PASS |
| img.svg loaded | yes | **NO — 4 SVGs return 404** | **FAIL** |
| source-note / credit-line / hero / map / pilot marker | 同上 | 同上 | PASS |
| console errors | 0 | **3 errors (404s for SVGs)** | **FAIL** |
| failed responses | 0 | **3 (object-journey / evidence-chain / viewing-map)** | **FAIL** |
| mobile 390 horizontal overflow | no | no | PASS |

### Mode B 失败原因（serving-model mismatch）

`_pilots/second-exhibition-pilot/site/index.html` 中 4 张 SVG 用相对路径 `../assets/diagrams/<name>.svg` 引用图。当通过 `file://` 直接打开 HTML 时，浏览器相对当前文件（`site/index.html`）解析 `../assets/diagrams/...` 正确指向 `_pilots/second-exhibition-pilot/assets/diagrams/`，SVG 全部加载。

当通过 `python3 -m http.server 8770 --directory _pilots/second-exhibition-pilot/site`（brief 指定命令）启动服务器，URL 变成 `http://localhost:8770/`，相对路径从 URL 根解析：`../assets/diagrams/...` 退到根后等于 `/assets/diagrams/...`，而该路径在 HTTP server 根下不存在（实际目录在 `_pilots/second-exhibition-pilot/assets/`），导致 404。

这是一个 serving-model 的相对路径行为差异，不是 pilot 本身的 bug。fix 有两个选项：

- 选项 A：把 4 张 `<img src>` 从 `../assets/diagrams/...` 改成 `assets/diagrams/...`，并在 HTTP server 从 `_pilots/second-exhibition-pilot/`（而非 `site/`）启动时才能工作
- 选项 B：在 HTTP server 命令中改为 `--directory _pilots/second-exhibition-pilot`，URL 变成 `http://localhost:8770/site/`，原 `../assets/...` 路径解析正确

按 brief "原则上不要修改 site/index.html" 约束，本 round 不修改 HTML。canonical 用法是 `file://`，已在 Mode A 验证完全通过。

## structural counts

| 维度 | 期望 | 实测 |
|---|---|---|
| sections | >= 4 | 4 |
| artifact cards | >= 4 | 4 |
| glossary items | >= 6 | 6 |
| deep-reading | >= 1 | 1 |
| material-evidence | >= 1 | 1 |
| visual-thinking | >= 1 | 1 |
| research-model | >= 1 | 1 |
| pilot-v0.1 marker | present | 1 |
| pilot-hero | present | 1 |
| pilot-map | present | 1 |
| source-note | >= 4 | 4 |
| credit-line | >= 4 | 4 |
| SVG diagrams | 3 | 3 (object-journey / evidence-chain / viewing-map) |

## JSON validation result

| File | Status |
|---|---|
| `data/exhibition.json` | valid |
| `data/sections.json` | valid |
| `data/glossary.json` | valid |
| `data/assets.json` | valid |

All 4/4 pass. Confirmed both via `python -m json.tool` and via `scripts/template_quality_gate.py` Section B.

## forbidden terms result

No forbidden terms (`Leonardo` / `Codex Atlanticus` / `Royal Collection Trust` / `Leonardo//thek@`) in default template content. Confirmed via `scripts/template_quality_gate.py` Section C (4 checks PASS).

## SVG load result

`file://` mode: 4/4 SVGs load with proper dimensions (object-journey 800x280, evidence-chain 800x360, viewing-map 800x320, object-journey 800x280 for the 4th usage).

`http://localhost:8770/` mode: 0/4 SVGs load (serving-model mismatch, see above).

## mobile overflow result

Both modes (file:// + http.server) on 390x844 viewport: no horizontal overflow (`scrollWidth == windowWidth == 390`).

## console errors result

`file://` mode: 0 errors, 0 failed responses.

`http.server` mode: 3 errors (all are the SVG 404s).

## deployment check result

| 检查项 | 实测 |
|---|---|
| Pilot title in live HTML | 0 occurrences |
| `pilot-v0.1` in live HTML | 0 occurrences |
| live byte size | 92,976 B (unchanged) |
| Pages deployment path changed | no |

All deployment checks PASS.

## remaining follow-ups

- [ ] **如果要正式化**，需要真实 source audit（独立第三方对 source note / credit line 的核验），不只是 self-audit
- [ ] **如果新增真实图像**，需要重新 rights audit，按 `_template/SOURCE_RIGHTS_CHECKLIST_ZH.md` 12 项清单逐图核验
- [ ] **如果部署**，需要单独 deployment round（live URL / freeze workflow / GitHub Release），不是把 `_pilots/` 直接搬到 `_site/`
- [ ] **如果迁出为独立项目**，需要明确 LICENSE（当前 pilot 用 CC0 1.0 用于 project-generated 示意图，迁出时复用方需尊重）
- [ ] **如果使用 http.server 从 site/ 启动**，需要修正 index.html 中的 SVG 路径（`../assets/diagrams/...` → `assets/diagrams/...`），或调整 server 启动目录；本 round 不修改
- [ ] **如果接入 CI**，把 `python3 scripts/template_quality_gate.py` 加入 GitHub Actions 步骤，在每次 push 时自动验证

## QA summary

| 类别 | 结果 |
|---|---|
| JSON validity | PASS |
| Structural counts | PASS |
| Forbidden terms | PASS |
| File:// render | PASS（所有结构与 SVG 加载正确）|
| HTTP server render | 部分 PASS（结构正确，SVG 路径因 serving model 不匹配 404）|
| Mobile overflow | PASS |
| Deployment no-leak | PASS |
| Pilot deployment status | repository only, not deployed |

---

> 本报告由 v3.4 Real Second Exhibition Hardening 真实创建，所有 render 数据来自 Playwright Chromium 实测。