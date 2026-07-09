# Template Quality Gate

## Purpose

v3.3 Template Quality Gate 用于防止模板、pilot、文档和 release workflow 之间发生漂移，也用于避免 phantom premise 再次进入路线。

本 gate 由 `scripts/template_quality_gate.py` 实现，是项目自身的"门禁"工具，任何对 `_template/`、`_pilots/second-exhibition-pilot/`、`_template/RELEASE_WORKFLOW_ZH.md` 或 live site 的修改前后都应运行一次。

## What it checks

| Section | 检查内容 |
|---|---|
| A. Required paths | `_template/`、`_template/site/`、`_template/data/`、`_pilots/second-exhibition-pilot/` 四个目录；`docs/V3_TEMPLATE_ROADMAP.md`；5 个手册文件（`USAGE_GUIDE_ZH.md` / `CONTENT_AUTHORING_GUIDE_ZH.md` / `SOURCE_RIGHTS_CHECKLIST_ZH.md` / `PILOT_WORKFLOW_ZH.md` / `RELEASE_WORKFLOW_ZH.md`） |
| B. JSON validity | 模板：`content.schema.json` + 4 个 `data/*.example.json`；pilot：4 个 `data/*.json` |
| C. Forbidden terms | 默认模板内容（`data/*.example.json` + `site/*.template.*`）中不应出现 `Leonardo` / `Codex Atlanticus` / `Royal Collection Trust` / `Leonardo//thek@`。README / MANIFEST 等文档说明文件可以提到 source case，不纳入失败项 |
| D. Pilot structure | `_pilots/second-exhibition-pilot/site/index.html` 必须包含：`pilot-v0.1` marker >= 1、`template-artifact-card` >= 4、`<dt>` glossary term >= 6、4 类 deep block 各 >= 1（deep-reading / material-evidence / visual-thinking / research-model） |
| E. Release workflow rule | `_template/RELEASE_WORKFLOW_ZH.md` 必须包含：`commit SHA + verified live byte + verified tag`、`git add .`、不移动旧 tag、不覆盖旧 release |
| F. No accidental deployment signal | `site/index.html` / `site/script.js` / `site/style.css` 不应包含 pilot title 或 pilot marker（仅检查本地文件，不访问网络） |
| G. Summary | 打印每个 section 的 PASS / FAIL 与最终 STATUS |

## How to run

```bash
# 从 repo root 运行
python3 scripts/template_quality_gate.py
```

exit code：
- `0` — 所有检查通过
- `1` — 至少一项检查失败

运行时会按 section 打印检查项与 PASS / FAIL 标记，最后打印 `FINAL STATUS: PASS` 或 `FINAL STATUS: FAIL`。

## PASS criteria

必须同时满足：

- required paths all exist（4 目录 + 6 文件 = 10 项）
- template JSON 5/5 valid（schema + 4 example）
- pilot JSON 4/4 valid
- default template content forbidden terms = 0（4 个 term × 7 个扫描文件）
- pilot structural checks pass（7 项：marker / artifact / glossary / 4 类 deep block）
- release workflow rule present（4 个必需短语）
- live site does not contain pilot title / pilot marker（3 文件均 clean）

合计 37 项检查。

## What this gate does not do

明确不做的事：

- **不做法律判断**。rights check 只查模板默认内容是否提到 source case，不判断复用合法性
- **不访问外部版权页面**。任何对原机构许可状态的核验应由人工或独立流程完成
- **不部署 pilot**。本 gate 不触发任何 GitHub Pages / GitHub Release 操作
- **不验证 GitHub Release 是否存在**。tag 与 release 状态在 freeze round 单独验证
- **不替代 Playwright 全量 UI 检查**。本 gate 只检查结构与文本标记，不做渲染 / 交互测试
- **不访问 live URL**。live site 状态在 freeze round 用 `curl` 独立验证

## When to run

建议在以下时点运行：

- 修改 `_template/` 后
- 修改 `_pilots/` 后
- 准备 release freeze 前
- 新增图片 / 截图 / SVG 前后
- 发现 memory 与 git 状态不一致时

## Failure handling

如果 gate FAIL：

1. 不要硬改无关内容
2. 只修复真正的问题
3. 如果问题需要修改 `_template/site/` 或 `_pilots/` 内容，先在报告中说明，并尽量停止为 PARTIAL，等用户确认

## Notes

- 本 gate 是 v3.3 round 新增，第一次运行基于 `v3.2-real-template-documentation` tag 验证 PASS（37/37）
- 本 gate 只读 `_template/` / `_pilots/` / `site/` 三个目录，不修改任何文件
- 本 gate 不需要外部依赖（Python 标准库 only）

## See also

- `_template/RELEASE_WORKFLOW_ZH.md` — reality recovery rule（三件套）
- `docs/V3_TEMPLATE_ROADMAP.md` — v3.3 路线图小节
- `reports/leonardo_chinese_exhibition_v3_3_template_quality_gate_report.md` — 本 round 报告