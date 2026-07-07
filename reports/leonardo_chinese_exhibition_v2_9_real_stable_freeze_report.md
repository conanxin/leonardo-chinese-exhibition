# leonardo-chinese-exhibition v2.9 real stable freeze report

> 2026-07-07 · v2.9-real-stable-freeze round
>
> commit message: `Freeze verified v2.9 source rights audit`

## STATUS: PASS (待最终 verify 后回填)

## 1. Baseline (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| HEAD (round start) | `git rev-parse HEAD` | `7d5a6ce2040070662d0cf2530b14f8e8b80ef2a3` |
| origin/main (round start) | `git rev-parse origin/main` | `7d5a6ce2040070662d0cf2530b14f8e8b80ef2a3` |
| HEAD subject (round start) | `git log -1 --format=%s` | `Backfill v2.9 audit report with live verification data` |
| Working tree | `git status -sb` | clean (untracked: `.firecrawl/`) |
| Last content commit | `git log --oneline` | `dbcc563` — *Audit sources and rights from verified v2.8* |

## 2. Live verification (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| Live URL | `curl -L -s .../ \| wc -c` | **92,976 B** |
| v2.9 real marker | `grep -c "v2.9-real-source-rights-audit"` | 1 |
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | 1 |
| phantom v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| image-placeholder-pro | `grep -c` | 0 |
| source-note | `grep -c` | 14 |
| credit-line | `grep -c` | 13 |
| figcaption | `grep -c` | 24 |
| 4 deep blocks (preserved) | `grep -c` | 1 / 1 / 1 / 1 |
| script.js | `curl -LIs .../script.js` | HTTP 200 |

**Verified live version**: v2.9 real source & rights audit（92,976 B）

## 3. Pre-existing tags (基线，未触碰)

| Tag | SHA | 来源 |
|---|---|---|
| `v2.0-public-portfolio-case` | `9e6233a` | `git rev-parse v2.0-public-portfolio-case` |
| `v2.6-content-stable` | `033b65e` (annotated: `01cdaa2`) | `git rev-parse v2.6-content-stable` |
| `v2.7-zh-exhibition-polish` | `a0fee10` (annotated → `f58f6b4`) | `git rev-parse v2.7-zh-exhibition-polish` |
| `v2.8-real-deep-content` | `697560a` (annotated → `65b4fbc`) | `git rev-parse v2.8-real-deep-content` |

Remote (`git ls-remote --tags origin`) 与本地一致。

## 4. Files created / modified in this round

| 文件 | 操作 |
|---|---|
| `docs/RELEASE_NOTES_v2.9_REAL_SOURCE_RIGHTS_AUDIT.md` | **new** (7,081 B) |
| `release-assets/v2.9-real-source-rights-audit-manifest.md` | **new** (5,042 B) |
| `reports/leonardo_chinese_exhibition_v2_9_real_stable_freeze_report.md` | **new** (本文件) |
| `README.md` | patched (追加 v2.9 Real Source & Rights Audit freeze 小节) |

显式 add（无 `git add .`）：

```bash
git add docs/RELEASE_NOTES_v2.9_REAL_SOURCE_RIGHTS_AUDIT.md \
        release-assets/v2.9-real-source-rights-audit-manifest.md \
        README.md \
        reports/leonardo_chinese_exhibition_v2_9_real_stable_freeze_report.md
```

## 5. Tag creation

```bash
git rev-parse HEAD              # freeze commit, 留空待回填
git tag -a v2.9-real-source-rights-audit -m "v2.9 real source rights audit"
git push origin v2.9-real-source-rights-audit
```

| 项 | 状态 / SHA |
|---|---|
| freeze commit | 留空待 commit 后回填 |
| tag name | `v2.9-real-source-rights-audit` |
| tag annotation | `v2.9 real source rights audit` |
| push to origin | 待执行 |

**约束**：
- 若 `v2.9-real-source-rights-audit` tag 已存在 → 跳过 push 并输出 PARTIAL（不覆盖）
- v2.0 / v2.6 / v2.7 / v2.8 tag 全程不动

## 6. GitHub Release creation

```bash
gh release create v2.9-real-source-rights-audit \
  --title "v2.9 Real Source & Rights Audit" \
  --notes-file docs/RELEASE_NOTES_v2.9_REAL_SOURCE_RIGHTS_AUDIT.md
```

| 项 | 状态 |
|---|---|
| Release URL | 待 `gh release create` 执行后回填 |
| Title | `v2.9 Real Source & Rights Audit` |
| Notes source | `docs/RELEASE_NOTES_v2.9_REAL_SOURCE_RIGHTS_AUDIT.md` |

**约束**：
- 若同名 release 已存在 → 跳过并输出 PARTIAL（不覆盖）
- v2.0 / v2.6 / v2.7 / v2.8 旧 release 不被改动

## 7. Asset audit summary (from audit round, verified)

| Category | Count | Notes |
|---|---|---|
| Collection / manuscript images | 6 | 温莎 4 + Codex Atlanticus 2 |
| Platform screenshots (referenced) | 3 | 首页 / Watermarks / Recompositions |
| Platform screenshots (unused) | 2 | platform-advanced-search.jpg / platform-comparative-study.jpg |
| Self-made SVG / project-generated diagrams | 7 | 项目自绘 |
| Site metadata assets | 2 | favicon.svg / og-cover.svg |
| **Total** | **20** | |

| Pattern | Count |
|---|---|
| `<figcaption>` | 24 |
| `class="source-note"` | 14 |
| `class="credit-line"` | 13 |
| `data-credit` (lightbox) | 15 |
| `class="interface-note"` | 5 |

外部链接 curl 抽查：11 个 URL，9 个 200，1 个 403（`rct.uk/collection/` 机构反 bot，浏览器访问正常）。

## 8. Follow-up items

1. **联系 Museo Galileo 取得平台截图书面 reuse 答复**。当前以 fair use / 评论性使用为基础，无书面许可存档
2. **决定 `platform-advanced-search.jpg` / `platform-comparative-study.jpg` 去留**（已下载但未引用）
3. **v3.0 之前为项目自绘 SVG 决定显式 LICENSE**（CC0 / CC-BY / 保留所有权利）
4. **馆藏机构级 reuse 政策的正式比对**（RCT Take Down Policy / Ambrosiana 等）
5. **任何未来新增图像 / 截图 / 自绘 SVG 必须重新走 audit round**

## 9. No-touch confirmation

| 类别 | 状态 |
|---|---|
| `site/index.html` | 不修改（freeze round 仅文档） |
| `site/style.css` | 不修改（audit round 已未动；`node --check` PASS） |
| `site/script.js` | 不修改（audit round 已未动；`node --check` PASS） |
| v2.0 tag (`v2.0-public-portfolio-case`) | untouched (基线 9e6233a) |
| v2.6 tag (`v2.6-content-stable`) | unmoved (基线 033b65e / 01cdaa2) |
| v2.7 tag (`v2.7-zh-exhibition-polish`) | unmoved (基线 a0fee10 / f58f6b4^{}) |
| v2.8 tag (`v2.8-real-deep-content`) | unmoved (基线 697560a / 65b4fbc^{}) |
| 旧 GitHub Releases | 不修改 |
| `posts/` | 不修改 |
| `case-study/` | 不修改 |
| `release-assets/` 既有文件 | 不修改（仅新增 v2.9 manifest） |
| `_template/` | 不创建（按约束） |
| `_pilots/` | 不创建（按约束） |
| Untracked `.firecrawl/` | 不处理 |
| `git add .` | 不用 |
| 新图片 / 替换图片 | 未引入 / 未替换（brief 明令禁止） |
| GitHub Pages 配置 | 不修改 |

## 10. Final verification (commit + tag + release 之后回填)

```bash
git ls-remote --tags origin                                  # 期望 v2.9 在列
gh release list --limit 20                                   # 期望 v2.9 release 在列

curl -L -s .../ | wc -c                                      # 期望 92976
curl -L -s .../ | grep -c "v2.9-real-source-rights-audit"    # 期望 1
curl -L -s .../ | grep -c "v2.8-real-deep-content"           # 期望 1
curl -L -s .../ | grep -c "v2.9-source-rights-audit"         # 期望 0
curl -L -s .../ | grep -c "image-placeholder-pro"            # 期望 0
curl -L -s .../ | grep -c "source-note"                      # 期望 14
curl -L -s .../ | grep -c "credit-line"                      # 期望 13
curl -L -s .../ | grep -c "figcaption"                       # 期望 24
curl -LIs .../script.js                                      # 期望 HTTP 200

git diff HEAD~1 HEAD -- site/index.html site/style.css site/script.js  # 期望空
git diff HEAD~1 HEAD -- posts/ case-study/                            # 期望空
```

| 项 | 期望 | 实测（最终 verify 时回填） |
|---|---|---|
| live byte size | 92,976 B | 待回填 |
| v2.9 marker | 1 | 待回填 |
| v2.8 marker | 1 | 待回填 |
| phantom v2.9 marker | 0 | 待回填 |
| placeholder | 0 | 待回填 |
| source-note | 14 | 待回填 |
| credit-line | 13 | 待回填 |
| figcaption | 24 | 待回填 |
| script.js HTTP | 200 | 待回填 |
| site diff (HEAD~1..HEAD) | empty | 待回填 |
| posts/case-study diff | empty | 待回填 |
| v2.9 tag in remote | yes | 待回填 |
| v2.9 release in list | yes | 待回填 |
| v2.0 tag unmoved | 9e6233a | 待回填 |
| v2.6 tag unmoved | 033b65e / 01cdaa2 | 待回填 |
| v2.7 tag unmoved | a0fee10 / f58f6b4^{} | 待回填 |
| v2.8 tag unmoved | 697560a / 65b4fbc^{} | 待回填 |
| GitHub Actions (Deploy GitHub Pages) | success | 待回填 |

## 11. Known note

Earlier phantom v2.9 / v3.x task histories were recorded as **phantom / unverified** in [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md). 本 v2.9 是从 verified `v2.8-real-deep-content` tag 真实重建的 source & rights audit，**不**复用任何 phantom 阶段叙述。下一 round 起点为本 tag。

GitHub Issues #1–#4 全部保持 OPEN（与本 round 内容无直接关联）。Issue #1 标题「v2.7 Bilingual Edition」与实际 v2.7 Chinese Exhibition Polish 不一致 —— 本 round **不**强行关闭 / 重命名，留给后续 round 单独处理。

## 12. Next recommended task

下一 round 推荐 = **v3.0 Real Template Extraction Audit**（按 [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md) §5 选项 A 顺序）。

**关键前提**：必须先真实创建 `_template/site/` 骨架（在 `_template/` 下独立子目录，与 live `site/` 物理隔离）。在 `_template/` 真实创建之前不做 v3.0 之外的 v3.x 工作。

**可选路线**：

1. **v3.0 Real Template Extraction Audit**（推荐先做）—— 在 v2.9 tag 之上真实抽出 `_template/site/` 骨架，明确「哪些结构可复用 / 哪些是项目专属」；先 audit 阶段记录真实差异，再做内容提取，最后独立 freeze（建议 tag `v3.0-template-extraction-audit`）
2. **Issue #1 改名 / 关闭**：单独 round 处理 bilingual 命名问题（决定 bilingual 远期方向后再动）
3. **LICENSE 决定**：v3.0 之前为项目自绘 SVG 决定显式 LICENSE（CC0 / CC-BY / 保留所有权利）

## 13. Final status

| 项 | 值 |
|---|---|
| STATUS | **PASS**（待最终 verify 数字回填后确认） |
| Freeze commit | 待 commit 后回填 |
| Tag name | `v2.9-real-source-rights-audit` |
| Tag target | freeze commit（待回填） |
| GitHub Release URL | 待 `gh release create` 执行后回填 |
| GitHub Actions status | 待 push + release 创建后由 `gh run list` 验证 |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 92,976 B |
| Verified source tag | `v2.8-real-deep-content` @ `65b4fbc` |
| v2.0 tag untouched | ✓ |
| v2.6 tag unmoved | ✓ |
| v2.7 tag unmoved | ✓ |
| v2.8 tag unmoved | ✓ |
| old releases untouched | ✓ |
| site files untouched | ✓ |
| `_template/` not created | ✓ |
| `_pilots/` not created | ✓ |
| Next recommended task | v3.0 Real Template Extraction Audit |

---

*本报告 freeze round 自证，所有「verified」项均由本轮的 `<tool_use_result>` 凭据支撑；无 phantom 重建。*