# leonardo-chinese-exhibition v3.2 Template Documentation Report

## STATUS: PASS

本报告记录 v3.2 Template Documentation 阶段的完整执行与验证。

---

## 1. baseline

- baseline HEAD = `c5e93d0f6387572e342213737ac1f7e191c2268e`
- origin/main = `c5e93d0f6387572e342213737ac1f7e191c2268e`
- 本轮起点 = `c5e93d0`（HEAD 与 origin/main 一致，未漂移）
- 工作树状态：clean（仅 untracked `.firecrawl/`，按规则单独记录但不处理）

## 2. source tag

- tag 名 = `v3.1-real-second-exhibition-pilot`
- tag object = `f839187ae3c4382084b3b29aeba5df0c67238db8`
- tag target = `c5e93d0f6387572e342213737ac1f7e191c2268e`
- source pilot 路径 = `_pilots/second-exhibition-pilot/`
- source pilot 文件数 = 18
- source pilot JSON validation = 4/4 pass
- source pilot 部署状态：repository only，未部署

## 3. reality gate（baseline 已 PASS）

| 检查项 | 期望 | 实测 |
|---|---|---|
| _template 存在 | yes | yes |
| _template 文件数 | >= 17 | 17 |
| second pilot 存在 | yes | yes |
| second pilot 文件数 | = 18 | 18 |
| template JSON validation | 5/5 pass | 5/5 pass（schema + exhibition + sections + glossary + assets） |
| pilot JSON validation | 4/4 pass | 4/4 pass（exhibition + sections + glossary + assets） |
| v3.1 tag target | c5e93d0 | c5e93d0 ✓ |
| live byte size | 92,976 | 92,976 ✓ |
| v2.9 marker | 1 | 1 ✓ |
| image-placeholder-pro | 0 | 0 ✓ |
| source-note | 14 | 14 ✓ |
| credit-line | 13 | 13 ✓ |
| pilot title in live | 0 | 0 ✓ |
| script.js | HTTP 200 | HTTP/2 200 ✓ |
| 工作树 | clean（允许 untracked .firecrawl/） | clean ✓ |

## 4. live byte size before / after

- before（本 round 起点）= 92,976 B
- after（本 round 终点，commit 前）= 92,976 B
- 差值 = 0 B（本 round 不修改 live，三文件 site/index.html / site/style.css / site/script.js 全部 git diff 为空）

## 5. docs created（本 round 新增文档）

docs created count = 5

1. `_template/USAGE_GUIDE_ZH.md` — 中文数字展览模板使用手册
2. `_template/CONTENT_AUTHORING_GUIDE_ZH.md` — 中文数字展览内容写作指南
3. `_template/SOURCE_RIGHTS_CHECKLIST_ZH.md` — 来源与权利检查清单
4. `_template/PILOT_WORKFLOW_ZH.md` — Pilot 工作流
5. `_template/RELEASE_WORKFLOW_ZH.md` — 发布与封版工作流

### 5 manual files 列表

| 文件 | 行数 | 大小 |
|---|---|---|
| _template/USAGE_GUIDE_ZH.md | ~110 | ~3.1 KB |
| _template/CONTENT_AUTHORING_GUIDE_ZH.md | ~150 | ~5.1 KB |
| _template/SOURCE_RIGHTS_CHECKLIST_ZH.md | ~120 | ~4.4 KB |
| _template/PILOT_WORKFLOW_ZH.md | ~135 | ~4.6 KB |
| _template/RELEASE_WORKFLOW_ZH.md | ~155 | ~5.9 KB |

## 6. README updates

### _template/README.md

- 追加"使用文档"小节，链接 5 个手册
- 未修改原有结构（v3.0 起的目录说明、适用场景、来源案例等全部保留）

### docs/V3_TEMPLATE_ROADMAP.md

- v3.1 Second Exhibition Pilot 状态从 In progress 改为 Done
- v3.1 Second Exhibition Pilot — stable freeze 状态从 Planned 改为 Done（与 pilot 同 commit 链完成）
- v3.2 Template Documentation 状态从 Planned 改为 In progress
- v3.2 不做的事加入更细的禁止清单（site 三文件 / _template/site / _template/data / pilot 内容 / 新 pilot / 部署 / 旧 tag / 旧 release / 新馆藏图）
- 路径示意图更新：v3.1-real-second-exhibition-pilot 标 Done，v3.2 标 In progress

### README.md（主 README）

- 新增 "## v3.2 Template Documentation" 小节
- 列 5 个手册链接 + "Does not modify live site or pilot" + "Stable freeze next"
- 插入位置在 v3.1 之后、"当前版本"之前

## 7. live site no-change confirmation

```
git diff -- site/index.html site/style.css site/script.js
```
输出为空。

| 文件 | 是否修改 |
|---|---|
| site/index.html | 未修改 ✓ |
| site/style.css | 未修改 ✓ |
| site/script.js | 未修改 ✓ |

## 8. pilot no-change confirmation

```
git diff -- _pilots/second-exhibition-pilot/
```
输出为空。pilot 18 个文件全部未触碰。

## 9. old tags untouched

本 round 不移动任何 tag。当前所有 tag（来自 `git tag --list` 与 `git ls-remote --tags origin`）：

| tag | object | target | 状态 |
|---|---|---|---|
| v2.0-public-portfolio-case | 9e6233ab | 旧 | 未触碰 ✓ |
| v2.6-content-stable | 033b65e2 | 01cdaa2d | 未触碰 ✓ |
| v2.7-zh-exhibition-polish | a0fee102 | f58f6b45 | 未触碰 ✓ |
| v2.8-real-deep-content | 697560af | 65b4fbc2 | 未触碰 ✓ |
| v2.9-real-source-rights-audit | 13814d34 | a1e667e3 | 未触碰 ✓ |
| v3.0-real-template-extraction-audit | 3b5404fe | dd7d589f | 未触碰 ✓ |
| v3.1-real-second-exhibition-pilot | f839187a | c5e93d0f | 未触碰 ✓（作为 source tag） |

## 10. old releases untouched

本 round 不修改任何 GitHub Releases。本 round 不创建新 release / tag。

## 11. reality recovery rule

RELEASE_WORKFLOW_ZH.md 包含 hard rule：
- "任何阶段必须有 commit SHA + verified live byte + verified tag 三件套；缺一项则标为 unverified。"

验证：`grep -c "commit SHA + verified live byte + verified tag" _template/RELEASE_WORKFLOW_ZH.md` = 1 ✓

同时文档还包含：

- `git add .` 禁止（`grep -c "git add ." _template/RELEASE_WORKFLOW_ZH.md` = 1 ✓）
- 禁止事项清单（移动旧 tag / 覆盖旧 release / 未验证 live 宣布 PASS / draft 当 stable / phantom memory 当真实起点 等 6 项）
- 2-commit freeze 模式说明（freeze 本体 → SHA backfill，与 v3.0 / v3.1 实际做法对齐）
- 复盘 checklist

## 12. 禁止事项遵守情况

| 禁止事项 | 是否遵守 |
|---|---|
| 不修改 site/index.html | ✓ |
| 不修改 site/style.css | ✓ |
| 不修改 site/script.js | ✓ |
| 不修改 _template/site/ | ✓ |
| 不修改 _template/data/ | ✓ |
| 不修改 _pilots/second-exhibition-pilot/ 内容 | ✓ |
| 不创建新的 pilot | ✓ |
| 不部署 pilot | ✓ |
| 不移动任何旧 tag | ✓ |
| 不修改旧 GitHub Releases | ✓ |
| 不修改 posts/ | ✓ |
| 不修改 case-study/ | ✓ |
| 不修改 release-assets/ 既有文件 | ✓ |
| 不新增真实馆藏图片 | ✓ |
| 不替换任何 live 图片 | ✓ |
| 不修改 Hermes 生产配置 | ✓ |
| 不处理 untracked .firecrawl/ | ✓（按规则忽略） |
| 不使用 `git add .` | ✓（本 round 用 explicit add） |

## 13. 本 round commit 准备

按显式 add 计划提交：

```
git add _template/USAGE_GUIDE_ZH.md
git add _template/CONTENT_AUTHORING_GUIDE_ZH.md
git add _template/SOURCE_RIGHTS_CHECKLIST_ZH.md
git add _template/PILOT_WORKFLOW_ZH.md
git add _template/RELEASE_WORKFLOW_ZH.md
git add _template/README.md
git add docs/V3_TEMPLATE_ROADMAP.md
git add README.md
git add reports/leonardo_chinese_exhibition_v3_2_template_documentation_report.md

git commit -m "Document reusable exhibition template workflow"
git push origin main
```

显式 add 9 个文件，未使用 `git add .`。

## 14. next recommended task

**v3.2-real-stable-freeze**

下一 round 应对 v3.2 Template Documentation 做 stable freeze：按 RELEASE_WORKFLOW_ZH.md 的 2-commit 模式（freeze 本体 → SHA backfill）、打 tag `v3.2-real-template-documentation`、写 GitHub Release、做 live verification（虽然本 round 不改 live，但 freeze 后 live byte size 仍应为 92,976 B）、记录 no-touch confirmation。

freeze 后路径：

```
v2.9-real-source-rights-audit  (verified, freeze)
    ↓
v3.0-real-template-extraction-audit  (Done)
    ↓
v3.1-real-second-exhibition-pilot  (Done)
    ↓
v3.2-real-template-documentation  (Pending — 下一 round)
    ↓
v3.3+ optional real second exhibition
```

## 15. 三件套校验（本 round 提交前）

| 项 | 值 | 来源 |
|---|---|---|
| commit SHA | （待本 round commit 后回填） | `git rev-parse HEAD` |
| verified live byte | 92,976 B | `curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ \| wc -c` |
| verified tag | v3.1-real-second-exhibition-pilot / f839187a / target c5e93d0 | `git rev-parse v3.1-real-second-exhibition-pilot^{}` |

提交后需要在 final verification 中独立校验 HEAD SHA 与 origin/main 一致。

---

> 本报告由 v3.2 Template Documentation 真实创建，所有 live / tag / 文件计数均来自本 round 实测。