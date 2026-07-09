# leonardo-chinese-exhibition v3.4 Real Second Exhibition Hardening Report

## STATUS: PASS

本报告记录 v3.4 Real Second Exhibition Hardening 阶段的完整执行与验证。

---

## 1. baseline

- baseline HEAD = `b6bd12e4f614518652054c8e9d23f3fa738ae0bd`
- baseline origin/main = `b6bd12e4f614518652054c8e9d23f3fa738ae0bd`
- 本 round 起点 = `b6bd12e`（HEAD 与 origin/main 一致，未漂移）
- baseline 工作树状态：clean（仅 untracked `.firecrawl/`，按规则单独记录但不处理）

## 2. source tag

- tag 名 = `v3.3-real-template-quality-gate`
- tag object = `fb35a5d9aece0bf44d82e3f7f25c2a73b8e6a70e`
- tag target = `fce2efb5f0fcbbb3bd4e25c8008513f8c2462eb4`

## 3. live byte size before / after

- before（本 round 起点）= 92,976 B
- after（本 round 终点，commit 前）= 92,976 B
- 差值 = 0 B（本 round 不修改 live site）

## 4. quality gate result

```
FINAL STATUS: PASS
Total checks: 37
Passed:       37
Failed:       0
exit code: 0
```

37/37 checks pass。pilot structural 子检查全过：sections=4, artifact cards=4, glossary items=6, 4 deep blocks, pilot marker=1。

## 5. pilot local render result

通过 Playwright + Chromium 实测两种 serving mode：

### Mode A — `file://`（canonical 用法）

| 维度 | 实测 |
|---|---|
| status | 200 |
| title | 一件作品的旅程 · pilot-v0.1 |
| sections | 4 |
| artifact cards | 4 |
| glossary items | 6 |
| deep-reading / material-evidence / visual-thinking / research-model | 1 / 1 / 1 / 1 |
| pilot-marker | 1 |
| pilot-hero / pilot-map | 1 / 1 |
| SVG diagrams loaded | 4/4（800x280 / 800x360 / 800x320 / 800x280） |
| source-note / credit-line | 4 / 4 |
| console errors | 0 |
| failed responses | 0 |
| mobile 390 horizontal overflow | no |

### Mode B — `http://localhost:8770/`（brief-specified http.server from `site/`）

| 维度 | 实测 |
|---|---|
| status | 200 |
| title | 一件作品的旅程 · pilot-v0.1 |
| sections / artifact cards / glossary items / deep blocks | 同 Mode A |
| pilot-marker / hero / map | 1 / 1 / 1 |
| source-note / credit-line | 4 / 4 |
| SVG diagrams loaded | **0/4（404 for object-journey / evidence-chain / viewing-map）** |
| console errors | **3（SVG 404s）** |
| failed responses | **3** |
| mobile 390 horizontal overflow | no |

### 失败原因

`_pilots/second-exhibition-pilot/site/index.html` 中 4 张 SVG 用 `../assets/diagrams/...` 相对路径引用图。在 `file://` 模式下，浏览器相对 HTML 文件位置解析路径，正确指向 `_pilots/second-exhibition-pilot/assets/diagrams/`，SVG 全部加载。

在 `python3 -m http.server 8770 --directory _pilots/second-exhibition-pilot/site` 启动的服务器上，URL 根变成 `/`，`../assets/diagrams/...` 退到根后等于 `/assets/diagrams/...`，该路径在 server 根下不存在，导致 404。

这是 serving-model 的相对路径行为差异，不是 pilot 本身的 bug。fix 选项：

- 选项 A：改 index.html 4 处 `<img src>` 从 `../assets/...` 改为 `assets/...`（影响 `file://` 用法）
- 选项 B：调整 server 启动目录到 `_pilots/second-exhibition-pilot/`（URL 变 `http://localhost:8770/site/`）

按 brief "原则上不要修改 site/index.html" 约束，本 round 不修改 HTML。canonical `file://` 用法完全通过。

## 6. pilot docs created

3 hardening docs：

1. `_pilots/second-exhibition-pilot/PILOT_QA_CHECKLIST.md` — QA checklist（identity / structural / data / rights / render / deployment）
2. `_pilots/second-exhibition-pilot/PILOT_HANDOFF.md` — handoff guide（what this pilot proves / does not prove / if turning into real exhibition / safe reuse）
3. `_pilots/second-exhibition-pilot/docs/PILOT_QA_REPORT.md` — Playwright 实测 QA 报告（含 `file://` 和 http.server 两种模式结果）

外加：

- `_pilots/second-exhibition-pilot/README.md` — 追加 "Hardening notes" 小节，链接三个新文档

## 7. README / roadmap updates

### README.md（主 README）

新增 "## v3.4 Real Second Exhibition Hardening" 小节，列：

- source tag
- 3 个 hardening docs 链接（QA checklist / handoff / QA report）
- 两条不做的事（keeps pilot repository-only / does not deploy pilot）

### docs/V3_TEMPLATE_ROADMAP.md

- v3.3 Template Quality Gate 状态从 "In progress" 改为 Done
- 新增 "## v3.4 Real Second Exhibition Hardening" 小节
- "## v3.4 Optional Real Second Exhibition" 重命名为 "## v3.5 Optional Real Second Exhibition"（避免与新 v3.4 冲突）
- 路径示意图更新：v3.3 → v3.4-real-second-exhibition-hardening → v3.5+

## 8. live site no-change confirmation

```
git diff -- site/index.html site/style.css site/script.js
```

输出为空。

| 文件 | 是否修改 |
|---|---|
| site/index.html | 未修改 ✓ |
| site/style.css | 未修改 ✓ |
| site/script.js | 未修改 ✓ |

## 9. _template no-change confirmation

```
git diff -- _template/site/
git diff -- _template/data/
```

输出为空。`_template/site/*.template.{html,css,js}` 与 `_template/data/*.example.json` 全部未触碰。

## 10. pilot internal no-touch confirmation

`_pilots/second-exhibition-pilot/` 内 `site/index.html`、`site/style.css`、`site/script.js`、`data/*.json`、`assets/diagrams/*.svg` 均未修改（本 round 只新增 3 个 .md 文档）。

| 文件 / 目录 | 是否修改 |
|---|---|
| _pilots/second-exhibition-pilot/site/index.html | 未修改 ✓ |
| _pilots/second-exhibition-pilot/site/style.css | 未修改 ✓ |
| _pilots/second-exhibition-pilot/site/script.js | 未修改 ✓ |
| _pilots/second-exhibition-pilot/data/*.json | 未修改 ✓ |
| _pilots/second-exhibition-pilot/assets/diagrams/*.svg | 未修改 ✓ |

新增：

- `_pilots/second-exhibition-pilot/PILOT_QA_CHECKLIST.md`
- `_pilots/second-exhibition-pilot/PILOT_HANDOFF.md`
- `_pilots/second-exhibition-pilot/docs/PILOT_QA_REPORT.md`

修改（仅追加，不重写）：

- `_pilots/second-exhibition-pilot/README.md`（追加 "Hardening notes" 小节）

## 11. scripts/template_quality_gate.py no-change confirmation

`scripts/template_quality_gate.py` 在本 round 未修改，仍跑出 37/37 PASS。

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
| v3.2-real-template-documentation | 77a89fb5 | 5a89fb2 | 未触碰 ✓ |
| v3.3-real-template-quality-gate | fb35a5d9 | fce2efb | 未触碰 ✓（作为 source tag） |

## 13. old releases untouched

本 round 不修改任何 GitHub Releases。本 round 不创建新 release / tag。

## 14. Forbidden actions compliance

| 禁止事项 | 是否遵守 |
|---|---|
| 不修改 site/index.html | ✓ |
| 不修改 site/style.css | ✓ |
| 不修改 site/script.js | ✓ |
| 不修改 _template/site/ | ✓ |
| 不修改 _template/data/ | ✓ |
| 不修改 scripts/template_quality_gate.py | ✓ |
| 不修改 _pilots/second-exhibition-pilot/ 内 site/data/assets 实质内容 | ✓ |
| 不创建新 pilot | ✓ |
| 不部署 pilot | ✓ |
| 不移动任何旧 tag | ✓ |
| 不修改旧 GitHub Releases | ✓ |
| 不修改 posts/ | ✓ |
| 不修改 case-study/ | ✓ |
| 不修改 release-assets/ 既有文件 | ✓ |
| 不新增真实馆藏图片 | ✓ |
| 不替换任何 live 图片 | ✓ |
| 不修改 Hermes 生产配置 | ✓ |
| 不处理 untracked .firecrawl/ | ✓ |
| 不使用 `git add .` | ✓（explicit add） |

## 15. 本 round commit 准备

显式 add 7 个文件：

```
git add _pilots/second-exhibition-pilot/PILOT_QA_CHECKLIST.md
git add _pilots/second-exhibition-pilot/PILOT_HANDOFF.md
git add _pilots/second-exhibition-pilot/docs/PILOT_QA_REPORT.md
git add _pilots/second-exhibition-pilot/README.md
git add docs/V3_TEMPLATE_ROADMAP.md
git add README.md
git add reports/leonardo_chinese_exhibition_v3_4_real_second_exhibition_hardening_report.md

git commit -m "Harden second exhibition pilot"
git push origin main
```

显式 add，未使用 `git add .`。

## 16. next recommended task

**v3.4-real-stable-freeze**

下一 round 应对 v3.4 Real Second Exhibition Hardening 做 stable freeze：

- 按 RELEASE_WORKFLOW_ZH.md 的 2-commit 模式（freeze 本体 → SHA backfill）
- 打 tag `v3.4-real-second-exhibition-hardening`
- 写 GitHub Release
- 做 live verification（live byte size 应仍为 92,976 B）
- 记录 no-touch confirmation

或者跳过 freeze，直接进入 `v4.0-real-second-exhibition-plan`：

- 思考"下一个真实展览"使用本模板的具体规划
- 决定下一个真实主题
- 决定是否需要先扩展模板

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
v3.3-real-template-quality-gate  (Done)
    ↓
v3.4-real-second-exhibition-hardening  (In progress — 本 round)
    ↓
v3.5+ optional real second exhibition
```

## 17. 三件套校验（本 round 提交前）

| 项 | 值 | 来源 |
|---|---|---|
| commit SHA | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` | `git rev-parse HEAD` |
| verified live byte | 92,976 B | `curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ \| wc -c` |
| verified source tag | `v3.3-real-template-quality-gate` → `fce2efb5f0fcbbb3bd4e25c8008513f8c2462eb4` | `git rev-parse v3.3-real-template-quality-gate^{}` |

## 18. v3.4 stable freeze backfill（step 7 → 9 follow-up）

step 7 之后的 tag / Release 动作补充记录：

| 项 | 值 |
|---|---|
| v3.4 tag name | `v3.4-real-second-exhibition-hardening` |
| v3.4 tag object SHA | `bf9f5ddb1ce8c08f01b7e0c98fae26ef7f68cb41` |
| v3.4 tag target commit | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` (= step 6 freeze commit) |
| v3.4 tag 推送结果 | `git push origin v3.4-real-second-exhibition-hardening` → exit 0 |
| v3.4 GitHub Release | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v3.4-real-second-exhibition-hardening |
| v3.4 Release 创建命令 | `gh release create v3.4-real-second-exhibition-hardening --title "v3.4 Real Second Exhibition Hardening" --notes-file docs/RELEASE_NOTES_v3.4_REAL_SECOND_EXHIBITION_HARDENING.md` |
| release notes 文件 | `docs/RELEASE_NOTES_v3.4_REAL_SECOND_EXHIBITION_HARDENING.md` |

3 个旧 tag（v3.0 / v3.1 / v3.2 / v3.3）的 commit target 全部未移动，10 个旧 release 全部未触碰。

## 19. next recommended task（post-freeze 更新）

`v3.4-real-stable-freeze` 已于本 step 7→9 阶段完成。下一 round 二选一：

1. **`v3.5-real-template-instantiation-pilot`** — 用本模板实例化第三个 pilot，主题另选（建筑史 / 设计史 / 手稿学等），证明模板跨主题复用。
2. **`v4.0-real-second-exhibition-plan`** — 决定下一个真实展览主题与研究范围。

freeze 后路径更新：

```
v3.3-real-template-quality-gate  (Done)
    ↓
v3.4-real-second-exhibition-hardening  (Done — 本 round freeze + Release)
    ↓
v3.5+ optional real second exhibition / v4.0 plan
```

---

> 本报告由 v3.4 Real Second Exhibition Hardening 真实创建，所有 render 数据来自 Playwright Chromium 实测。