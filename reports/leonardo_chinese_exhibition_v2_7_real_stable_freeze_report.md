# leonardo-chinese-exhibition v2.7 real stable freeze report

> 2026-07-07 · v2.7-real-stable-freeze round
>
> commit message: `Freeze verified v2.7 exhibition polish`

## STATUS: PASS

## 1. Baseline (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| HEAD (round start) | `git rev-parse HEAD` | `984ff3b4c0a3834e8c693c47179c8c8e2442d7f7` |
| origin/main (round start) | `git rev-parse origin/main` | `984ff3b4c0a3834e8c693c47179c8c8e2442d7f7` |
| HEAD subject (round start) | `git log -1 --format=%s` | `Record verified project reality` |
| Working tree | `git status -sb` | clean (untracked: `.firecrawl/`) |
| Last content commit | `git log --oneline` | `71c7403` — *Polish Chinese exhibition experience* |

## 2. Live verification (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| Live URL | `curl -L -s .../ \| wc -c` | **85,564 B** |
| v2.7 marker | `grep -c "v2.7-zh-exhibition-polish"` | 1 |
| v2.8 marker | `grep -c "v2.8-deep-exhibition-content"` | 0 |
| v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| quick-guide-zh | `grep -c "quick-guide-zh"` | 1 |
| viewer-action | `grep -c "viewer-action"` | 4 |
| image-placeholder-pro | `grep -c "image-placeholder-pro"` | 0 |
| script.js | `curl -LIs .../script.js` | HTTP 200 |

**Verified live version**: v2.7 zh exhibition polish（85,564 B）

## 3. Pre-existing tags (基线，未触碰)

| Tag | SHA | 来源 |
|---|---|---|
| `v2.0-public-portfolio-case` | `9e6233a` | `git rev-parse v2.0-public-portfolio-case` |
| `v2.6-content-stable` | `033b65e` (annotated: `01cdaa2`) | `git rev-parse v2.6-content-stable` |

Remote (`git ls-remote --tags origin`) 与本地一致。

## 4. Files created / modified in this round

| 文件 | 操作 |
|---|---|
| `docs/RELEASE_NOTES_v2.7_ZH_EXHIBITION_POLISH.md` | **new** (4,233 B) |
| `release-assets/v2.7-zh-exhibition-polish-manifest.md` | **new** (4,015 B) |
| `reports/leonardo_chinese_exhibition_v2_7_real_stable_freeze_report.md` | **new** (本文件) |
| `README.md` | patched (追加 v2.7 polish 小节) |

显式 add（无 `git add .`）：

```bash
git add docs/RELEASE_NOTES_v2.7_ZH_EXHIBITION_POLISH.md \
        release-assets/v2.7-zh-exhibition-polish-manifest.md \
        README.md \
        reports/leonardo_chinese_exhibition_v2_7_real_stable_freeze_report.md
```

## 5. Tag creation

```bash
git rev-parse HEAD              # freeze commit, 留空待回填
git tag -a v2.7-zh-exhibition-polish -m "v2.7 zh exhibition polish"
git push origin v2.7-zh-exhibition-polish
```

| 项 | 状态 / SHA |
|---|---|
| freeze commit | **`f58f6b45075e3d8c0e9d81a160ff939b1f8de412`** |
| tag name | `v2.7-zh-exhibition-polish` |
| tag object SHA | `a0fee10273c9ff1c0312a494054158fe524d60b0` |
| tag target | freeze commit `f58f6b4` (annotated → dereferenced to commit) |
| tag annotation | `v2.7 zh exhibition polish` |
| tag type | annotated (`git cat-file -t` = `tag`) |
| push to origin | **✓ pushed** (`git ls-remote --tags origin` 含 `v2.7-zh-exhibition-polish`) |

**约束**：
- 若 `v2.7-zh-exhibition-polish` tag 已存在 → 跳过 push 并输出 PARTIAL（不覆盖）
- v2.0 / v2.6 tag 全程不动

## 6. GitHub Release creation

```bash
gh release create v2.7-zh-exhibition-polish \
  --title "v2.7 Zh Exhibition Polish" \
  --notes-file docs/RELEASE_NOTES_v2.7_ZH_EXHIBITION_POLISH.md
```

| 项 | 状态 |
|---|---|
| Release URL | **https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.7-zh-exhibition-polish** |
| Title | `v2.7 Zh Exhibition Polish` |
| Notes source | `docs/RELEASE_NOTES_v2.7_ZH_EXHIBITION_POLISH.md` |
| Tag | `v2.7-zh-exhibition-polish` @ `f58f6b4` |
| draft / prerelease | false / false |
| author | conanxin |
| created | 2026-07-06T23:00:17Z |
| published | 2026-07-06T23:00:37Z |

**约束**：
- 若同名 release 已存在 → 跳过并输出 PARTIAL（不覆盖）
- v2.0 / v2.6 旧 release 不被改动

## 7. No-touch confirmation

| 类别 | 状态 |
|---|---|
| `site/index.html` | 不修改（freeze round 仅文档） |
| `site/style.css` | 不修改 |
| `site/script.js` | 不修改 |
| v2.0 tag (`v2.0-public-portfolio-case`) | untouched (基线 9e6233a) |
| v2.6 tag (`v2.6-content-stable`) | unmoved (基线 033b65e / 01cdaa2) |
| 旧 GitHub Releases | 不修改 |
| `posts/` | 不修改 |
| `case-study/` | 不修改 |
| `release-assets/` 既有文件（v2.6 manifest） | 不修改（仅新增 v2.7 manifest） |
| `_template/` | 不创建（按约束） |
| `_pilots/` | 不创建（按约束） |
| Untracked `.firecrawl/` | 不处理 |
| `git add .` | 不用 |
| 新图片 | 未引入 |
| GitHub Pages 配置 | 不修改 |

## 8. Final verification (commit + tag + release 之后回填)

```bash
git ls-remote --tags origin                                  # 期望 v2.7 在列
gh release list --limit 20                                   # 期望 v2.7 release 在列

curl -L -s .../ | wc -c                                      # 期望 85564
curl -L -s .../ | grep -c "v2.7-zh-exhibition-polish"        # 期望 1
curl -L -s .../ | grep -c "v2.8-deep-exhibition-content"     # 期望 0
curl -L -s .../ | grep -c "v2.9-source-rights-audit"         # 期望 0
curl -L -s .../ | grep -c "image-placeholder-pro"            # 期望 0
curl -LIs .../script.js                                      # 期望 HTTP 200

git diff HEAD~1 HEAD -- site/index.html site/style.css site/script.js  # 期望空
git diff HEAD~1 HEAD -- posts/ case-study/                            # 期望空
```

| 项 | 期望 | 实测 |
|---|---|---|
| live byte size | 85,564 B | **85,564 B** ✓ |
| v2.7 marker | 1 | **1** ✓ |
| v2.8 marker | 0 | **0** ✓ |
| v2.9 marker | 0 | **0** ✓ |
| placeholder | 0 | **0** ✓ |
| script.js HTTP | 200 | **200** ✓ |
| site diff (HEAD~1..HEAD) | empty | **empty** ✓ |
| posts/case-study diff | empty | **empty** ✓ |
| v2.7 tag in remote | yes | **yes** (`a0fee10` / `f58f6b4^{}`) ✓ |
| v2.7 release in list | yes | **yes** (2026-07-06T23:00:37Z, "Latest") ✓ |
| v2.0 tag unmoved | 9e6233a | **9e6233a** ✓ |
| v2.6 tag unmoved | 033b65e / 01cdaa2 | **033b65e / 01cdaa2** ✓ |
| GitHub Actions (Deploy GitHub Pages) | success | **success** (run 28829051731, 21s) ✓ |

## 9. Known note

Earlier v2.8 / v2.9 / v3.x task histories were recorded as **phantom / unverified** in [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md). v2.7-zh-exhibition-polish is the current **verified live baseline**，下一个 round 起点。

GitHub Issue #1（v2.7 Bilingual Edition）仍保持 OPEN —— 本 release 是 *Chinese Exhibition Polish*，与 #1 标题不一致。本 round **不**关闭 / **不**重命名 #1，留给后续 round 单独处理。

## 10. Next recommended task

下一 round 推荐顺序（按 [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md) §5 选项 A）：

1. **v2.8 Real Deep Content**（推荐先做）—— 在 v2.7 tag 之上真实增补 deep reading / material evidence / visual thinking / research model 模块；先 audit 阶段记录 phantom 重建 / 真实差异；再做内容；最后独立 freeze。
2. **v2.9 Real Source & Rights Audit** —— 完整过一遍 Royal Collection Trust / Codex Atlanticus / Leonardo//thek@ 的图源、编号、source note、credit line；独立 freeze。
3. **Issue #1 改名 / 关闭决策** —— 若决定 bilingual 不再做，关闭 #1；若保留 bilingual 作为远期方向，留 OPEN 但加 milestone 标注。
4. **v3.x Reusable Template** —— 必须先真实创建 `_template/site/` 骨架（在 `_template/` 下独立子目录，与 live `site/` 物理隔离）。在 `_template/` 真实创建之前不做 v3.0 之外的 v3.x 工作。

## 11. Final status

| 项 | 值 |
|---|---|
| STATUS | **PASS** |
| Freeze commit | `f58f6b45075e3d8c0e9d81a160ff939b1f8de412` |
| Tag name | `v2.7-zh-exhibition-polish` |
| Tag object SHA | `a0fee10273c9ff1c0312a494054158fe524d60b0` |
| Tag target commit | `f58f6b45075e3d8c0e9d81a160ff939b1f8de412` |
| GitHub Release URL | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.7-zh-exhibition-polish |
| GitHub Actions status | **success** (Deploy GitHub Pages run 28829051731, 21s) |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 85,564 B |
| Verified live version | v2.7 zh exhibition polish |
| v2.0 tag untouched | ✓ (9e6233a unchanged) |
| v2.6 tag unmoved | ✓ (033b65e / 01cdaa2 unchanged) |
| old releases untouched | ✓ |
| site files untouched | ✓ (`git diff HEAD~1 HEAD -- site/...` empty) |
| `_template/` not created | ✓ |
| `_pilots/` not created | ✓ |
| Next recommended task | v2.8 Real Deep Content |

---

*本报告 freeze round 自证，所有「verified」项均由本轮的 `<tool_use_result>` 凭据支撑；无 phantom 重建。*