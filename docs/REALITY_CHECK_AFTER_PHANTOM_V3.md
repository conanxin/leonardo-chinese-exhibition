# Reality Check after Phantom v3

> 本文档用于对账项目在 2026-07-07 收到的「v3.3 模板文档」任务 brief 与实际仓库 / live / tag / release / issue 状态之间的偏差。
>
> v3.3 task brief 的前置条件与仓库真实情况严重不符。本文档记录真实状态，把曾被报告为「已完成」但实际并不存在的阶段标记为不可信，并定义后续工作的恢复起点。

---

## 1. Verified current state (2026-07-07)

下列项目均为当前在裸仓库或 live 验证的真实状态，无推论。

| 项目 | 值 | 验证方式 |
|---|---|---|
| `HEAD` | `71c740373094e708aaaa25222163d93b3877a094` | `git rev-parse HEAD` |
| `origin/main` | `71c740373094e708aaaa25222163d93b3877a094` | `git rev-parse origin/main` |
| `HEAD` subject | `Polish Chinese exhibition experience` | `git log -1 --format=%s` |
| Working tree | clean (允许 untracked `.firecrawl/`) | `git status -sb` |
| Live URL | `https://conanxin.github.io/leonardo-chinese-exhibition/` | `curl -L` |
| Live `index.html` byte size | **85,564 B** | `wc -c` on `curl -L -s` |
| Live 主 marker | `v2.7-zh-exhibition-polish`（命中 1 次） | `grep -c` |
| Live `v2.8-deep-exhibition-content` | 0 | `grep -c` |
| Live `v2.9-source-rights-audit` | 0 | `grep -c` |
| Live `image-placeholder-pro` | 0 | `grep -c` |
| Live `script.js` | HTTP/2 200 | `curl -LIs` |
| Local tags | `v2.0-public-portfolio-case`, `v2.6-content-stable` | `git tag --list` |
| Remote tags | `v2.0-public-portfolio-case`, `v2.6-content-stable` | `git ls-remote --tags origin` |
| GitHub Releases | `v2.0 — 达·芬奇的纸上宇宙...` (2026-07-06T02:56:01Z), `v2.6 Content Stable` (2026-07-06T09:14:37Z) | `gh release list` |
| GitHub Issues (open) | `#1 v2.7 Bilingual Edition`, `#2 v2.8 Education / Teacher Guide`, `#3 v2.9 More Manuscript Images`, `#4 v3.0 Reusable Digital Exhibition Template` | `gh issue list --state all` |
| `_template/` 目录 | **不存在** | `test -d _template` |
| `_pilots/second-exhibition-pilot/` 目录 | **不存在** | `test -d _pilots/second-exhibition-pilot` |
| `docs/V3_TEMPLATE_ROADMAP.md` | **不存在** | `find docs -name V3_TEMPLATE_ROADMAP.md` |
| `reports/leonardo_chinese_exhibition_v3_*.md` | **不存在** | `ls reports/` |

> 注意：live byte size 与 task brief 中声称的 106,012 B 不一致；HEAD commit 与 task brief 中声称的 `a3f2d2a` 不一致；live marker 与 task brief 中声称的 `v2.9-source-rights-audit` 不一致。这些偏差为客观事实，不为任何「应该如此」的叙述所覆盖。

---

## 2. Confirmed real stages

下列阶段在 git history、live 或 GitHub Releases / Issues 中有可验证证据，可视为真实完成。

### v2.0 Public Portfolio Case
- Tag: `v2.0-public-portfolio-case` @ `9e6233a`
- Release: `v2.0 — 达·芬奇的纸上宇宙：中文数字展览稳定版` (2026-07-06T02:56:01Z)
- 证据：tag、GitHub Release、commit history
- 状态：**Stable, untouched**

### v2.6 Content Stable
- Tag: `v2.6-content-stable` @ `01cdaa2`（annotated）
- Release: `v2.6 Content Stable` (2026-07-06T09:14:37Z)
- 证据：tag、GitHub Release、commit history（commit `01cdaa2` "Freeze v2.6 content stable release"）
- 状态：**Stable, untouched**

### v2.7 Chinese Exhibition Polish（实际发生过 commit，但尚未独立 freeze / tag / release）
- Git history 证据（`git log --oneline --decorate -30`）：
  - `c85705c` Record v2.5-real deploy recovery
  - `c512dbd` Rebuild guided accessibility from v2.4 baseline
  - `0d58fdc` docs: backfill v2.7 report with commit hash + live HTTP
  - `31e5126` Polish exhibition copy and terminology
  - `c3c3e0b` Add artifact annotation and glossary layer
  - `988ebb9` Replace remaining placeholders with platform screenshots
  - `e1ca01f` Upgrade exhibition visitor experience
  - `71c7403` **Polish Chinese exhibition experience** ← 当前 HEAD
- Live 证据：HTML 含 `v2.7-zh-exhibition-polish` marker（footer `<strong>v2.7 zh exhibition polish</strong>`）
- 报告证据：`reports/leonardo_chinese_exhibition_v2_7_zh_exhibition_polish_report.md`
- **但**：
  - 没有 `v2.7-zh-exhibition-polish` tag
  - 没有 `v2.7-zh-exhibition-polish` GitHub Release
  - 没有独立的 v2.7 内容 stable freeze 文档（`docs/RELEASE_NOTES_v2.7.md` 不存在）
- 状态：**Content shipped to live, but not yet stable-freeze / tagged / released**

> 这就是真实的「v2.7」状态：内容已上线、commit 链真实存在，但 freeze 仪式（独立 tag + Release + release notes）尚未完成。GitHub Issue #1 仍 OPEN，标题是「v2.7 Bilingual Edition」（并非「v2.7 zh exhibition polish」），所以严格说 v2.7 zh polish 也未在 issue 层有正式收口。

---

## 3. Phantom / unverified stages

下列阶段在 v3.3 task brief 中被描述为「已完成」或「已存在」，但当前 git / live / tag / release / issue / filesystem 检查均不支持其真实完成。**这些阶段不可作为后续工作的前置条件**。

| 阶段 | task brief 中的主张 | 实际状态 | 不可信原因 |
|---|---|---|---|
| v2.8 Deep Exhibition Content | live 是 v2.8 deep content | live 无 `v2.8-deep-exhibition-content` marker；无 v2.8 tag；无 v2.8 release | 不存在 |
| v2.9 Source & Rights Audit | live 是 v2.9 source rights audit；byte size 106,012 B | live 无 `v2.9-source-rights-audit` marker；无 v2.9 tag；无 v2.9 release；live 实际 85,564 B | 不存在 |
| v3.0 Template Extraction Audit | v3.0 已完成 | 无 v3.0 tag；Issue #4 OPEN；无 v3.0 commit chain | 不存在 |
| v3.1 Template Skeleton | `_template/` 已存在 | `_template/` 目录不存在；无 v3.1 commit | 不存在 |
| v3.2 Second Exhibition Pilot | pilot 已完成；4 JSON valid；3 SVG；commit `a3f2d2a` | `_pilots/` 不存在；无 `a3f2d2a` commit（`git log --all` 也找不到） | 不存在 |
| v3.3 Template Documentation | 在 v3.2 之上做文档 | v3.2 不存在 → v3.3 的前置条件不成立；本 round 自身就是 v3.3 | 当前 round |
| Issue #16 created and closed | Issue #16 已存在 | `gh issue list` 最高编号 #4 | 不存在 |

> 这些「phantom stage」最可能的成因：上游任务描述（在更早的 session 中被生成）继承了 phantom success —— 即在 v2.7 / v2.5-real 已被诚实纠正为「实际未上线 / 实际未 freeze」后，**更高版本的阶段在没有真实 commit 的情况下被叙述为已完成**。这与 `2026-07-06 phantom success recovery` 案例是同一类失败模式。

---

## 4. Recovery rule

后续所有任务（包括 v3.3 本轮以及任何 v2.8+ 重启）在生成任务 brief / 报告 / commit message / release notes 时，**必须**遵循：

1. **真实起点**：从 `HEAD = 71c7403` 出发，不引用任何不存在的 commit、tag、release、issue number、directory、JSON 状态作为前置。
2. **真实 live**：live 当前是 v2.7 内容（85,564 B，含 v2.7 marker）。任何 byte size、marker、placeholder 数都必须由本轮 `curl -L -s` 重新抓取确认，**不得**沿用 task brief 的数字。
3. **真实 tags**：只有 `v2.0-public-portfolio-case` 和 `v2.6-content-stable` 两个 tag 存在。任何提到 v2.7 / v2.8 / v2.9 / v3.x tag 的内容都是 phantom。
4. **真实目录**：`_template/` 和 `_pilots/` 当前不存在。任何提到它们「已存在」「已包含 N 文件」「4/4 JSON valid」的内容都是 phantom。
5. **真实 issues**：open issues 编号目前最大为 #4（`gh issue list` 实证）。任何提到 #16 或更高编号的叙述都需要先 `gh issue view` 确认。
6. **side-effect 工具的输出必须独立校验**：所有 `git commit` / `git push` / `gh issue create` / `gh release create` / `curl -L -s` 之后的「成功」叙述都必须由独立的 `<tool_use_result>` 凭据支撑；凭据缺失 → 重跑工具 → 再叙述。
7. **不要 fabricate「如果 brief 是对的，那么...」**：本轮起任何报告都先列「真实状态 → brief 主张 → 偏差」三段，绝不假装 brief 是对的。

---

## 5. Recommended next step

按「先 freeze 已知真实内容，再增量扩展」的最小风险顺序：

### 选项 A（推荐）：先做 v2.7-real-stable-freeze

> **理由**：v2.7 内容实际上线了，但没有独立的 tag / release / release notes / release-assets manifest。这是当前真实存在的 gap，不是 phantom。修复它是「把真实状态记录成可验证状态」，无破坏性。

**建议步骤**（仅作记录，本轮不执行）：
1. 在 `docs/` 新增 `RELEASE_NOTES_v2.7_ZH_EXHIBITION_POLISH.md`
2. 在 `release-assets/` 新增 `v2.7-zh-exhibition-polish-manifest.md`
3. 编写 `reports/leonardo_chinese_exhibition_v2_7_real_stable_freeze_report.md`
4. 显式 add（无 `git add .`），commit + push
5. `git tag -a v2.7-zh-exhibition-polish <commit> -m "..."`
6. `git push origin v2.7-zh-exhibition-polish`
7. `gh release create v2.7-zh-exhibition-polish` 并 attach manifest
8. live 验证：byte size / marker / placeholder count / `script.js` 200
9. 在 `README.md` 把 stable tag 指向 `v2.7-zh-exhibition-polish`

### 选项 B：再做 v2.8 + v2.9，再回 v3.x

跳过 v2.7 freeze，直接做 v2.8 deep content / v2.9 source rights。**不推荐**：会让 phantom 状态延续，且与「先 freeze 真实再做增量」的顺序相悖。

### 选项 C：跳过 v2.7 / v2.8 / v2.9，直接做 v3.x template

**不推荐**：v3.x 必须建立在 `_template/` 之上，而 `_template/` 当前不存在；要在「先做 v3.x」之前先做「v3.0 template extraction audit」（真实创建 `_template/site/` 骨架），那是另一轮完整工作。

### 选项 D：维持现状，先发本文档

> **本轮选这个**。本文档 = 选项 D 的产物：把真实状态写下来，定义恢复规则，让下一个 round 在真实前提下做选择。

---

## 6. 当前 round 的 scope（reality reconciliation round）

本轮（v3.3-phantom-recovery round，commit message `Record verified project reality`）只做四件事：

1. 创建本文档（`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`）
2. 在 `docs/ROADMAP_AFTER_v2.6.md` 追加「Verified reality reset」小节
3. 在 `README.md` 顶部追加「Verified current state」小节
4. 创建 `reports/leonardo_chinese_exhibition_reality_reconciliation_report.md`

**明确不做**：

- 不创建 `_template/`
- 不创建 `_pilots/`
- 不创建任何 v2.7 / v2.8 / v2.9 / v3.x tag
- 不创建任何 GitHub Release
- 不修改 `site/index.html` `site/style.css` `site/script.js`
- 不修改 `posts/` `case-study/` `release-assets/` 既有文件
- 不引入新图片
- 不改 GitHub Actions 配置
- 不处理 untracked `.firecrawl/`
- 不 `git add .`

---

*本文档是项目在 phantom-v3 阶段的真实状态快照。后续任何工作请从 `HEAD = 71c7403` 出发，把本文档当作 ground truth 校对基准。*
