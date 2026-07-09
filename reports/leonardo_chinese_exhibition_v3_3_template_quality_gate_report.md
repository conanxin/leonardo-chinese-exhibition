# leonardo-chinese-exhibition v3.3 Template Quality Gate Report

## STATUS: PASS

本报告记录 v3.3 Template Quality Gate 阶段的完整执行与验证。

---

## 1. baseline

- baseline HEAD = `0e3853d56b941e8c850fe0c2c36985dd6f0b9f1d`
- baseline origin/main = `0e3853d56b941e8c850fe0c2c36985dd6f0b9f1d`
- 本 round 起点 = `0e3853d`（HEAD 与 origin/main 一致，未漂移）
- baseline 工作树状态：clean（仅 untracked `.firecrawl/`，按规则单独记录但不处理）

## 2. source tag

- tag 名 = `v3.2-real-template-documentation`
- tag object = `77a89fb5ffccaae0f686ed2eb388453b1901fe33`
- tag target = `5a89fb2061ef3eee95c63dc3592d92fb859177fe`

## 3. live byte size before / after

- before（本 round 起点）= 92,976 B
- after（本 round 终点，commit 前）= 92,976 B
- 差值 = 0 B（本 round 不修改 live site）

## 4. script created

- 路径 = `scripts/template_quality_gate.py`
- 大小 = 13,226 bytes
- 行数 = ~370
- 依赖 = Python 标准库 only（json / os / re / sys / pathlib）
- exit code = 0（PASS）/ 1（FAIL）

## 5. quality gate result

```
FINAL STATUS: PASS
Total checks: 37
Passed:       37
Failed:       0
exit code: 0
```

37 项检查全部 PASS：

| Section | 项数 | 结果 |
|---|---|---|
| A. Required paths | 10 | PASS |
| B. JSON validation | 9 | PASS |
| C. Forbidden terms | 4 | PASS |
| D. Pilot structure | 7 | PASS |
| E. Release workflow rule | 4 | PASS |
| F. No accidental deployment signal | 3 | PASS |
| **总计** | **37** | **PASS** |

## 6. checks covered count

37 项

按大类：

- 路径类（10 项）：4 目录 + 6 文件
- JSON 校验（9 项）：5 模板 + 4 pilot
- 禁用词扫描（4 项）：4 个 forbidden term 各 1 次
- Pilot 结构（7 项）：1 marker + 1 artifact 阈值 + 1 glossary 阈值 + 4 deep block
- Release workflow（4 项）：4 个必需短语
- 部署信号（3 项）：3 个 live site 文件各 1 次

## 7. docs created

| 文件 | 用途 |
|---|---|
| `scripts/template_quality_gate.py` | 可重复运行的 Python 质量门禁 |
| `docs/TEMPLATE_QUALITY_GATE.md` | 门禁文档（purpose / what it checks / how to run / PASS criteria / what it doesn't do / when to run / failure handling） |
| `docs/V3_TEMPLATE_ROADMAP.md` | 更新：v3.2 标 Done，新增 v3.3 Template Quality Gate 小节，路径示意更新 |
| `README.md` | 更新：新增 v3.3 Template Quality Gate 小节 |
| `reports/leonardo_chinese_exhibition_v3_3_template_quality_gate_report.md` | 本报告 |

## 8. README / roadmap updates

### README.md

新增 "## v3.3 Template Quality Gate" 小节，列：

- source tag
- script path
- doc path
- checks covered
- 两条不做的事（不修改 live / 不部署 pilot）
- 运行命令

### docs/V3_TEMPLATE_ROADMAP.md

- v3.2 Template Documentation 状态从 "In progress" 改为 Done
- 新增 "## v3.3 Template Quality Gate" 小节（status / 起点 / 交付物 / 范围 / 不做的事 / 下一步）
- "## v3.3 Optional Real Second Exhibition" 重命名为 "## v3.4 Optional Real Second Exhibition"（避免与新 v3.3 冲突）
- 路径示意图更新：v3.2 → v3.3-template-quality-gate → v3.4+

## 9. live site no-change confirmation

```
git diff -- site/index.html site/style.css site/script.js
```

输出为空。

| 文件 | 是否修改 |
|---|---|
| site/index.html | 未修改 ✓ |
| site/style.css | 未修改 ✓ |
| site/script.js | 未修改 ✓ |

## 10. pilot no-change confirmation

```
git diff -- _pilots/second-exhibition-pilot/
```

输出为空。pilot 18 个文件全部未触碰。

## 11. _template/site and _template/data no-change confirmation

```
git diff -- _template/site/
git diff -- _template/data/
```

输出为空。`_template/site/*.template.{html,css,js}` 与 `_template/data/*.example.json` 全部未触碰。

## 12. old tags untouched

| tag | object | target | 状态 |
|---|---|---|---|
| v2.0-public-portfolio-case | 9e6233ab | 9e6233ab | 未触碰 ✓ |
| v2.6-content-stable | 033b65e2 | 01cdaa2d | 未触碰 ✓ |
| v2.7-zh-exhibition-polish | a0fee102 | f58f6b45 | 未触碰 ✓ |
| v2.8-real-deep-content | 697560af | 65b4fbc2 | 未触碰 ✓ |
| v2.9-real-source-rights-audit | 13814d34 | a1e667e3 | 未触碰 ✓ |
| v3.0-real-template-extraction-audit | 3b5404fe | dd7d589f | 未触碰 ✓ |
| v3.1-real-second-exhibition-pilot | f839187a | c5e93d0f | 未触碰 ✓ |
| v3.2-real-template-documentation | 77a89fb5 | 5a89fb2 | 未触碰 ✓（作为 source tag） |

## 13. old releases untouched

本 round 不修改任何 GitHub Releases。本 round 不创建新 release / tag。

| Release | 状态 |
|---|---|
| v2.0 — 达·芬奇的纸上宇宙 | 未触碰 ✓ |
| v2.6 Content Stable | 未触碰 ✓ |
| v2.7 Zh Exhibition Polish | 未触碰 ✓ |
| v2.8 Real Deep Content | 未触碰 ✓ |
| v2.9 Real Source & Rights Audit | 未触碰 ✓ |
| v3.0 Real Template Extraction Audit | 未触碰 ✓ |
| v3.1 Real Second Exhibition Pilot | 未触碰 ✓ |
| v3.2 Real Template Documentation (Latest) | 未触碰 ✓ |

## 14. Forbidden actions compliance

| 禁止事项 | 是否遵守 |
|---|---|
| 不修改 site/index.html | ✓ |
| 不修改 site/style.css | ✓ |
| 不修改 site/script.js | ✓ |
| 不修改 _pilots/second-exhibition-pilot/ 内容 | ✓ |
| 不修改 _template/site/ | ✓ |
| 不修改 _template/data/ | ✓ |
| 不改写 5 个手册正文 | ✓ |
| 不创建新 pilot | ✓ |
| 不部署 pilot | ✓ |
| 不移动任何旧 tag | ✓ |
| 不修改旧 GitHub Releases | ✓ |
| 不修改 posts/ | ✓ |
| 不修改 case-study/ | ✓ |
| 不修改 release-assets/ 既有文件 | ✓ |
| 不新增真实馆藏图片 | ✓ |
| 不替换任何 live 图片 | ✓ |
| 不处理 untracked .firecrawl/ | ✓（按规则忽略） |
| 不使用 `git add .` | ✓（explicit add） |

## 15. 本 round commit 准备

显式 add 5 个文件，未使用 `git add .`：

```
git add scripts/template_quality_gate.py
git add docs/TEMPLATE_QUALITY_GATE.md
git add docs/V3_TEMPLATE_ROADMAP.md
git add README.md
git add reports/leonardo_chinese_exhibition_v3_3_template_quality_gate_report.md

git commit -m "Add template quality gate"
git push origin main
```

## 16. next recommended task

**v3.3-real-stable-freeze**

下一 round 应对 v3.3 Template Quality Gate 做 stable freeze：

- 按 RELEASE_WORKFLOW_ZH.md 的 2-commit 模式（freeze 本体 → SHA backfill）
- 打 tag `v3.3-real-template-quality-gate`
- 写 GitHub Release
- 做 live verification（live byte size 应仍为 92,976 B）
- 记录 no-touch confirmation

或者跳过 freeze，直接进入 `v3.4-real-second-exhibition-hardening`，把 quality gate 用作前向工具。

freeze 后路径：

```
v2.9-real-source-rights-audit  (verified, freeze)
    ↓
v3.0-real-template-extraction-audit  (Done)
    ↓
v3.1-real-second-exhibition-pilot  (Done)
    ↓
v3.2-real-template-documentation  (Done)
    ↓
v3.3-template-quality-gate  (In progress — 本 round)
    ↓
v3.4+ optional real second exhibition
```

## 17. 三件套校验（本 round 提交前）

| 项 | 值 | 来源 |
|---|---|---|
| commit SHA | （待本 round commit 后回填） | `git rev-parse HEAD` |
| verified live byte | 92,976 B | `curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ \| wc -c` |
| verified source tag | `v3.2-real-template-documentation` → `5a89fb2061ef3eee95c63dc3592d92fb859177fe` | `git rev-parse v3.2-real-template-documentation^{}` |

提交后需要在 final verification 中独立校验 HEAD SHA 与 origin/main 一致。

---

> 本报告由 v3.3 Template Quality Gate 真实创建，所有 live / tag / 文件计数均来自本 round 实测。