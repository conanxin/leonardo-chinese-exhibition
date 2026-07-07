# leonardo-chinese-exhibition v2.8 real stable freeze report

> 2026-07-07 · v2.8-real-stable-freeze round
>
> commit message: `Freeze verified v2.8 deep content`

## STATUS: PASS

## 1. Baseline (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| HEAD (round start) | `git rev-parse HEAD` | `dfecf202d07b430e7df2e50676c3613464b4c03c` |
| origin/main (round start) | `git rev-parse origin/main` | `dfecf202d07b430e7df2e50676c3613464b4c03c` |
| HEAD subject (round start) | `git log -1 --format=%s` | `Backfill v2.8 deep content report with live verification data` |
| Working tree | `git status -sb` | clean (untracked: `.firecrawl/`) |
| Last content commit | `git log --oneline` | `18b551b` — *Rebuild v2.8 deep content from verified baseline* |

## 2. Live verification (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| Live URL | `curl -L -s .../ \| wc -c` | **92,507 B** |
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | 1 |
| v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| deep-reading-block | `grep -c` | 1 |
| material-evidence-block | `grep -c` | 1 |
| visual-thinking-block | `grep -c` | 1 |
| research-model-block | `grep -c` | 1 |
| quick-guide-zh | `grep -c` | 1 |
| viewer-action | `grep -c` | 4 |
| image-placeholder-pro | `grep -c` | 0 |
| script.js | `curl -LIs .../script.js` | HTTP 200 |

**Verified live version**: v2.8 real deep content（92,507 B）

## 3. Pre-existing tags (基线，未触碰)

| Tag | SHA | 来源 |
|---|---|---|
| `v2.0-public-portfolio-case` | `9e6233a` | `git rev-parse v2.0-public-portfolio-case` |
| `v2.6-content-stable` | `033b65e` (annotated: `01cdaa2`) | `git rev-parse v2.6-content-stable` |
| `v2.7-zh-exhibition-polish` | `a0fee10` (annotated → `f58f6b4`) | `git rev-parse v2.7-zh-exhibition-polish` |

Remote (`git ls-remote --tags origin`) 与本地一致。

## 4. Files created / modified in this round

| 文件 | 操作 |
|---|---|
| `docs/RELEASE_NOTES_v2.8_REAL_DEEP_CONTENT.md` | **new** (6,265 B) |
| `release-assets/v2.8-real-deep-content-manifest.md` | **new** (4,222 B) |
| `reports/leonardo_chinese_exhibition_v2_8_real_stable_freeze_report.md` | **new** (本文件) |
| `README.md` | patched (追加 v2.8 Real Deep Content 节) |

显式 add（无 `git add .`）：

```bash
git add docs/RELEASE_NOTES_v2.8_REAL_DEEP_CONTENT.md \
        release-assets/v2.8-real-deep-content-manifest.md \
        README.md \
        reports/leonardo_chinese_exhibition_v2_8_real_stable_freeze_report.md
```

## 5. Tag creation

```bash
git rev-parse HEAD              # freeze commit, 留空待回填
git tag -a v2.8-real-deep-content -m "v2.8 real deep content"
git push origin v2.8-real-deep-content
```

| 项 | 状态 / SHA |
|---|---|
| freeze commit | **`65b4fbc2b1bc742f263559145bb273c11cb3c6b0`** |
| tag name | `v2.8-real-deep-content` |
| tag object SHA | `697560af9822addbcbe9f865e2bd6d1e33da9a93` |
| tag target | freeze commit `65b4fbc` (annotated → dereferenced to commit) |
| tag annotation | `v2.8 real deep content` |
| tag type | annotated (`git cat-file -t` = `tag`) |
| push to origin | **✓ pushed** (`git ls-remote --tags origin` 含 `v2.8-real-deep-content`) |

**约束**：
- 若 `v2.8-real-deep-content` tag 已存在 → 跳过 push 并输出 PARTIAL（不覆盖）
- v2.0 / v2.6 / v2.7 tag 全程不动

## 6. GitHub Release creation

```bash
gh release create v2.8-real-deep-content \
  --title "v2.8 Real Deep Content" \
  --notes-file docs/RELEASE_NOTES_v2.8_REAL_DEEP_CONTENT.md
```

| 项 | 状态 |
|---|---|
| Release URL | **https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.8-real-deep-content** |
| Title | `v2.8 Real Deep Content` |
| Notes source | `docs/RELEASE_NOTES_v2.8_REAL_DEEP_CONTENT.md` |
| Tag | `v2.8-real-deep-content` @ `65b4fbc` |
| draft / prerelease | false / false |
| author | conanxin |
| created | 2026-07-07T05:56:33Z |
| published | 2026-07-07T05:56:50Z |
| status | Latest |

**约束**：
- 若同名 release 已存在 → 跳过并输出 PARTIAL（不覆盖）
- v2.0 / v2.6 / v2.7 旧 release 不被改动

## 7. No-touch confirmation

| 类别 | 状态 |
|---|---|
| `site/index.html` | 不修改（freeze round 仅文档） |
| `site/style.css` | 不修改 |
| `site/script.js` | 不修改（v2.8 content round 已不动；`node --check` PASS） |
| v2.0 tag (`v2.0-public-portfolio-case`) | untouched (基线 9e6233a) |
| v2.6 tag (`v2.6-content-stable`) | unmoved (基线 033b65e / 01cdaa2) |
| v2.7 tag (`v2.7-zh-exhibition-polish`) | unmoved (基线 a0fee10 / f58f6b4^{}) |
| 旧 GitHub Releases | 不修改 |
| `posts/` | 不修改 |
| `case-study/` | 不修改 |
| `release-assets/` 既有文件 | 不修改（仅新增 v2.8 manifest） |
| `_template/` | 不创建（按约束） |
| `_pilots/` | 不创建（按约束） |
| Untracked `.firecrawl/` | 不处理 |
| `git add .` | 不用 |
| 新图片 | 未引入 |
| GitHub Pages 配置 | 不修改 |

## 8. Final verification (commit + tag + release 之后回填)

```bash
git ls-remote --tags origin                                  # 期望 v2.8 在列
gh release list --limit 20                                   # 期望 v2.8 release 在列

curl -L -s .../ | wc -c                                      # 期望 92507
curl -L -s .../ | grep -c "v2.8-real-deep-content"           # 期望 1
curl -L -s .../ | grep -c "v2.9-source-rights-audit"         # 期望 0
curl -L -s .../ | grep -c "deep-reading-block"               # 期望 1
curl -L -s .../ | grep -c "material-evidence-block"          # 期望 1
curl -L -s .../ | grep -c "visual-thinking-block"            # 期望 1
curl -L -s .../ | grep -c "research-model-block"             # 期望 1
curl -L -s .../ | grep -c "image-placeholder-pro"            # 期望 0
curl -LIs .../script.js                                      # 期望 HTTP 200

git diff HEAD~1 HEAD -- site/index.html site/style.css site/script.js  # 期望空
git diff HEAD~1 HEAD -- posts/ case-study/                            # 期望空
```

| 项 | 期望 | 实测 |
|---|---|---|
| live byte size | 92,507 B | **92,507 B** ✓ |
| v2.8 marker | 1 | **1** ✓ |
| v2.9 marker | 0 | **0** ✓ |
| 4 deep blocks | 1 / 1 / 1 / 1 | **1 / 1 / 1 / 1** ✓ |
| placeholder | 0 | **0** ✓ |
| script.js HTTP | 200 | **200** ✓ |
| site diff (HEAD~1..HEAD) | empty | **empty** ✓ |
| posts/case-study diff | empty | **empty** ✓ |
| v2.8 tag in remote | yes | **yes** (`697560a` / `65b4fbc^{}`) ✓ |
| v2.8 release in list | yes | **yes** (2026-07-07T05:56:50Z, "Latest") ✓ |
| v2.0 tag unmoved | 9e6233a | **9e6233a** ✓ |
| v2.6 tag unmoved | 033b65e / 01cdaa2 | **033b65e / 01cdaa2** ✓ |
| v2.7 tag unmoved | a0fee10 / f58f6b4^{} | **a0fee10 / f58f6b4^{}** ✓ |
| GitHub Actions (Deploy GitHub Pages) | success | **success** (run 28844907944, 13s) ✓ |

## 9. Known note

Earlier phantom v2.8 / v2.9 / v3.x task histories were recorded as **phantom / unverified** in [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md). 本 v2.8 是从 verified `v2.7-zh-exhibition-polish` tag 真实重建，**不**复用任何 phantom 阶段叙述。下一 round 起点为本 tag。

GitHub Issues #1–#4 全部保持 OPEN（与本 round 内容无直接关联）。Issue #1 标题「v2.7 Bilingual Edition」与实际 v2.7 Chinese Exhibition Polish 不一致 —— 本 round **不**强行关闭 / 重命名，留给后续 round 单独处理。

## 10. Next recommended task

下一 round 推荐顺序（按 [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md) §5 选项 A）：

1. **v2.9 Real Source & Rights Audit**（推荐先做）—— 在 v2.8 tag 之上逐图核 source note、RCIN 编号、Wikimedia Commons 授权、credit line；先 audit 阶段记录真实差异，再做内容修订，最后独立 freeze（建议 tag `v2.9-source-rights-audit`）。
2. **Issue #1 改名 / 关闭**：单独 round 处理 bilingual 命名问题（决定 bilingual 远期方向后再动）。
3. **v3.x Reusable Template**：必须先真实创建 `_template/site/` 骨架（在 `_template/` 下独立子目录，与 live `site/` 物理隔离）。在 `_template/` 真实创建之前不做 v3.0 之外的 v3.x 工作。

## 11. Final status

| 项 | 值 |
|---|---|
| STATUS | **PASS** |
| Freeze commit | `65b4fbc2b1bc742f263559145bb273c11cb3c6b0` |
| Tag name | `v2.8-real-deep-content` |
| Tag object SHA | `697560af9822addbcbe9f865e2bd6d1e33da9a93` |
| Tag target commit | `65b4fbc2b1bc742f263559145bb273c11cb3c6b0` |
| GitHub Release URL | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.8-real-deep-content |
| GitHub Actions status | **success** (Deploy GitHub Pages run 28844907944) |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 92,507 B |
| Verified source tag | `v2.7-zh-exhibition-polish` @ `f58f6b4` |
| v2.0 tag untouched | ✓ (9e6233a unchanged) |
| v2.6 tag unmoved | ✓ (033b65e / 01cdaa2 unchanged) |
| v2.7 tag unmoved | ✓ (a0fee10 / f58f6b4^{} unchanged) |
| old releases untouched | ✓ |
| site files untouched | ✓ (`git diff HEAD~1 HEAD -- site/...` empty) |
| `_template/` not created | ✓ |
| `_pilots/` not created | ✓ |
| Next recommended task | v2.9 Real Source & Rights Audit |

---

*本报告 freeze round 自证，所有「verified」项均由本轮的 `<tool_use_result>` 凭据支撑；无 phantom 重建。*