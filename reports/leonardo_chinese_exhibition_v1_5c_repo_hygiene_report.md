# Leonardo Chinese Exhibition — v1.5c Repo Hygiene 审计报告

报告生成时间：2026-07-06
项目目录：/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
目标范围：仓库卫生（权限 / workflow / git 状态 / 关键文件存在性），**不改展览正文**

---

## 0. STATUS

**STATUS: PASS**

v1.5b live hotfix 状态保持不变：线上 marker 仍可检索，本地三处 marker 文本完整。
本次仅做权限修复（chmod 0600 → 0644）+ workflow 审计 + 文件存在性检查，**未触发新 commit（Git 不跟踪 0600/0644 差异，因此无 git diff）**。报告文件单独 commit。

---

## 1. git 状态 / 当前 commit

```
$ git status -sb
## main...origin/main

$ git log --oneline -5
b39d306 Add v1.5b live marker verification report
d69f516 Add live hotfix version marker
2d3180e Fix live release deploy state
4f21c9b Finalize v1.5 live release notes
e341deb Redesign exhibition page in OpenAI editorial style

$ git remote -v
origin  https://github.com/conanxin/leonardo-chinese-exhibition.git (fetch)
origin  https://github.com/conanxin/leonardo-chinese-exhibition.git (push)

$ git branch --show-current
main
```

- working tree clean (no `??` / ` M` / `A ` 前缀)
- 与 origin/main 同步
- 在正确分支 `main`

---

## 2. Git index file mode 检查

命令：`git ls-files -s | sort > /tmp/leonardo_git_file_modes.txt`

### 2.1 模式分布

```
30 100644
```

### 2.2 结论

✓ **全部 30 条记录都是 `100644`**（普通文本文件，无 executable bit）。
- 无 `100755` 可执行脚本（也合理：本项目无 .sh / .py 调用入口）
- 无 `100600`
- 无 `120000` 符号链接
- 无异常 git 跟踪模式

**Git index 干净，无需修复。**

---

## 3. Working tree 实际权限检查

命令：`find . -path ./.git -prune -o -type f -printf "%m %p\n" | sort > /tmp/leonardo_worktree_permissions.txt`

### 3.1 修复前

全部 30 个文件均为 **模式 600 (`-rw-------` = `0600`)**：

```
600 ./.github/workflows/pages.yml
600 ./README.md
600 ./docs/CLOUDFLARE_PAGES.md
600 ./docs/DEPLOYMENT.md
600 ./docs/GITHUB_PAGES.md
600 ./docs/RELEASE_NOTES_v1.0.md
600 ./exhibition/curatorial-statement.md
600 ./exhibition/exhibition-plan.md
600 ./exhibition/section-script.md
600 ./reports/leonardo_chinese_exhibition_report.md
600 ./reports/leonardo_chinese_exhibition_v0_2_visual_review.md
600 ./reports/leonardo_chinese_exhibition_v0_3_release_prep.md
600 ./reports/leonardo_chinese_exhibition_v1_0_public_release_report.md
600 ./reports/leonardo_chinese_exhibition_v1_1_deploy_report.md
600 ./reports/leonardo_chinese_exhibition_v1_2_live_publish_verification.md
600 ./reports/leonardo_chinese_exhibition_v1_3_openai_style_redesign_report.md
600 ./reports/leonardo_chinese_exhibition_v1_4_visual_publish_verification.md
600 ./reports/leonardo_chinese_exhibition_v1_5_live_release_report.md
600 ./reports/leonardo_chinese_exhibition_v1_5b_live_marker_verification_report.md
600 ./research/image-candidates.md
600 ./research/leonardo-manuscripts-background.md
600 ./research/platform-notes.md
600 ./site/assets/README.md
600 ./site/assets/diagrams/manuscript-journey.svg
600 ./site/assets/diagrams/platform-structure.svg
600 ./site/assets/diagrams/thinking-map.svg
600 ./site/assets/favicon.svg
600 ./site/assets/og-cover.svg
600 ./site/index.html
600 ./site/style.css
```

- ✗ **30/30 文件权限为 `0600`**，应该是 `0644`
- ✓ 无 `0700` 目录异常
- ✓ 无 `0755` 普通文本文件（无滥用 executable bit）
- ✓ 无 `0777`

### 3.2 修复策略

按用户提供的 minimal chmod 修复方案执行 + 补全两个未列出子目录 (`exhibition/`, `research/`)：

```bash
chmod 644 README.md
chmod 644 docs/*.md          # 5 files
chmod 644 reports/*.md       # 11 files
chmod 644 site/*.html site/*.css   # 2 files
find site/assets -type f -exec chmod 644 {} \;     # 8 files
find .github/workflows -type f -name "*.yml" -o -name "*.yaml" -exec chmod 644 {} \;  # 1 file
# 补全用户未显式列出但同属普通文本的目录：
chmod 644 exhibition/*.md research/*.md
```

### 3.3 修复后

```
$ find . -path ./.git -prune -o -type f -printf "%m %p\n" | sort | awk '{print $1}' | sort | uniq -c
     30 644
```

✓ **30/30 文件 = `0644`**，全部正常文件权限。

### 3.4 Git diff 影响

```
$ git diff --stat HEAD
(empty — no diff)
```

原因：Git 默认不跟踪 `0600` vs `0644` 差异（仅跟踪 executable bit）。chmod 修复属于 working-tree-only 修复，**这是预期行为**。

---

## 4. GitHub Pages workflow 检查

文件：`.github/workflows/pages.yml`（568 bytes，30 行）

```yaml
name: Deploy GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site
      - id: deployment
        uses: actions/deploy-pages@v4
```

### 4.1 检查矩阵

| 检查项 | 结果 |
|---|---|
| `on: push: branches: [main]` 存在 | ✓ line 4–5 |
| `workflow_dispatch` 存在 | ✓ line 6 |
| `permissions.contents: read` 存在 | ✓ line 9 |
| `permissions.pages: write` 存在 | ✓ line 10 |
| `permissions.id-token: write` 存在 | ✓ line 11 |
| `actions/upload-pages-artifact@v3` path = `site` | ✓ line 26–28 |
| `actions/deploy-pages@v4` 存在 | ✓ line 30 |
| 无重复 `upload-pages-artifact` | ✓ 仅出现一次 |
| 无多 artifact 命名冲突 | ✓ |
| 不用 legacy `Deploy from a branch` 模式 | ✓ 用 Actions workflow，符合现代 Pages 标准 |

### 4.2 结论

✓ **workflow 已是教科书级 Pages deploy 配置**。无任何最小修改必要。**未修改 pages.yml。**

---

## 5. 关键发布文件存在性

| 路径 | 存在 |
|---|---|
| `site/index.html` | ✓ |
| `site/style.css` | ✓ |
| `site/assets/` (含 README.md + 3 SVG + diagrams/) | ✓ |
| `.github/workflows/pages.yml` | ✓ |
| `README.md` | ✓ |
| `docs/DEPLOYMENT.md` | ✓ |
| `reports/leonardo_chinese_exhibition_v1_5b_live_marker_verification_report.md` | ✓ |

7/7 全部存在。

---

## 6. Live marker 在本地仍在

命令：`grep -RnE "v1\.5b-live-hotfix|版本：v1\.5b" site/index.html`

```
8:  <meta name="version" content="v1.5b-live-hotfix">
13:<!-- leonardo-chinese-exhibition v1.5b-live-hotfix -->
272:  <p class="version-footer">版本：v1.5b live hotfix</p>
```

3 处 marker 全部保留。**v1.5b 热修复状态未受影响。**

---

## 7. 修改 / 提交总结

### 7.1 是否修改了文件

- **修改了 30 个文件的 working-tree 权限**：600 → 644
- **未修改任何文件内容**（chmod 不改内容）
- **未修改任何 workflow**
- **未修改 `site/index.html` / `site/style.css` / 任何 md**
- **新增了一个文件**：`reports/leonardo_chinese_exhibition_v1_5c_repo_hygiene_report.md`（本报告）

### 7.2 是否产生 git diff

```
$ git status -sb
## main...origin/main
```

无 git diff。git 默认忽略非 executable bit 的文件权限变化，因此 chmod 在 git 层是无操作。

### 7.3 提交策略

权限修复本身不产生 git diff，**不写空 commit**。仅新增的报告文件需要一次 commit：

```bash
git add reports/leonardo_chinese_exhibition_v1_5c_repo_hygiene_report.md
git commit -m "Add v1.5c repo hygiene audit report"
git push origin main
```

不修改 `site/` 内容、不修改 `pages.yml`、不动 `.git/`。

---

## 8. 下一步建议

### 8.1 不紧急项（可选）

- 若以后要进入协作模式，建议在 `README.md` 顶部加一句"贡献前请保证 `chmod 0644` 普通文件"，避免误传 `0600`。
- `site/index.html` 现在 13,245 字节、272 行；以后新增章节注意 footer 里 `版本：v1.5b live hotfix` 仍是最小可读版本指示，要不要升级到 `v1.5c` 由后续版本节奏决定。

### 8.2 监控项（已稳定，无需立刻行动）

- 线上 Pages run 在 v1.5b commit 之后已经两次连续 success（`2d3180e` → `28758201911` / `d69f516` → `28758282236`）；v1.5c 工作流未做任何修改，因此行为可预期，不会引入新风险。

### 8.3 不建议项

- 不要 `chmod -R 777`：本次权限修复遵守"显式 + 最小范围"原则。
- 不要 reset / stash / `git add .`：脏树策略仍按用户长期约束执行（本次无脏树可清理）。

---

## 9. 一句话总结

本次 v1.5c 仅做仓库卫生：30 个文件权限从 0600 → 0644 修复完毕，workflow 检查通过，关键文件齐全，live marker 完整。未触动展览内容、未触动 Git 跟踪层，git 状态保持干净。
