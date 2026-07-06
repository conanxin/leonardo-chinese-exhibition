# leonardo-chinese-exhibition reality reconciliation report

> 2026-07-07 · v3.3-phantom-recovery round · commit message `Record verified project reality`

## STATUS: PASS

本轮成功把项目从「phantom v3」状态拉回真实可验证状态：新增四份文档，**未触碰** `site/`、`tags`、`releases`、`posts/`、`case-study/`、`release-assets/`、untracked `.firecrawl/`、Hermes 生产配置。

## 1. Baseline (基线)

```
HEAD              = 71c740373094e708aaaa25222163d93b3877a094
origin/main       = 71c740373094e708aaaa25222163d93b3877a094
HEAD subject      = "Polish Chinese exhibition experience"
Working tree      = clean (untracked: .firecrawl/)
```

| 验证项 | 命令 | 结果 |
|---|---|---|
| Working tree clean | `git status -sb` | ✓ `## main...origin/main` + `?? .firecrawl/` |
| HEAD = origin/main | `git rev-parse` ×2 | ✓ 均为 `71c7403...` |
| 本地 tags | `git tag --list` | `v2.0-public-portfolio-case`, `v2.6-content-stable` |
| 远程 tags | `git ls-remote --tags origin` | `v2.0-public-portfolio-case` @ 9e6233a, `v2.6-content-stable` @ 033b65e / 01cdaa2^{} |
| GitHub Releases | `gh release list --limit 20` | v2.0 (2026-07-06T02:56:01Z), v2.6 Content Stable (2026-07-06T09:14:37Z) |
| GitHub Issues | `gh issue list --state all --limit 30` | #1 Bilingual, #2 Education, #3 Manuscript Images, #4 Reusable Template — 全部 OPEN；最高编号 #4 |
| `_template/` | `test -d _template` | **missing** |
| `_pilots/second-exhibition-pilot/` | `test -d _pilots/second-exhibition-pilot` | **missing** |

## 2. Live verification

```
URL              = https://conanxin.github.io/leonardo-chinese-exhibition/
curl byte size   = 85564
v2.7 marker      = 1   (grep -c "v2.7-zh-exhibition-polish")
v2.8 marker      = 0   (grep -c "v2.8-deep-exhibition-content")
v2.9 marker      = 0   (grep -c "v2.9-source-rights-audit")
placeholder      = 0   (grep -c "image-placeholder-pro")
script.js        = HTTP/2 200
```

**Verified live version**: v2.7 zh exhibition polish。

## 3. Phantom premise summary（v3.3 task brief 中声称但实际不存在的事项）

| Brief 声称 | 实际状态 |
|---|---|
| `_template/` 已创建 | 不存在 |
| `_pilots/second-exhibition-pilot/` 已创建 | 不存在 |
| v3.2 Second Exhibition Pilot 已完成 | 未发生（无 commit、无目录） |
| commit `a3f2d2a` | 不存在（`git log --all` 也无） |
| live 是 v2.9 source rights audit | live 是 v2.7 zh exhibition polish |
| live byte size 106,012 B | live byte size 85,564 B |
| 远程 tags v2.0/v2.6/v2.7/v2.8/v2.9 稳定共存 | 仅 v2.0 / v2.6 两个 |
| pilot JSON 4/4 valid | 无 pilot |
| pilot 使用 3 个自制 SVG | 无 pilot |
| site/index.html v3.2 中零修改 | v2.7 轮改过（最后修改 17:38） |
| Issue #16 已创建并关闭 | open issues 最高编号 #4 |

**成因分析（记录用）**：上游 session 在 v2.5-real / v2.6 content stable 已被诚实纠正为「实际未 freeze」之后，**更高版本的 v3.x 阶段在没有真实 commit 的情况下被叙述为已完成**。这是 `2026-07-06 phantom success recovery` 案例的同类型失败模式：side-effect 工具的输出（早期 session 的叙述）被下游视为 ground truth，但从未被独立的 `<tool_use_result>` 凭据支撑。

## 4. Files created / modified

显式 add（无 `git add .`）：

```
docs/REALITY_CHECK_AFTER_PHANTOM_V3.md                                          (new, 10914 B)
docs/ROADMAP_AFTER_v2.6.md                                                       (patched, appended "Verified reality reset" section)
README.md                                                                        (patched, appended "Verified current state" section at top)
reports/leonardo_chinese_exhibition_reality_reconciliation_report.md             (new, this file)
```

## 5. No-touch confirmation

| 类别 | 状态 | 验证 |
|---|---|---|
| `site/index.html` | 未触碰 | git working tree 不含该文件 staged diff |
| `site/style.css` | 未触碰 | 同上 |
| `site/script.js` | 未触碰 | 同上 |
| Local tags | 未触碰 | 仍为 `v2.0-public-portfolio-case`, `v2.6-content-stable` |
| Remote tags | 未触碰 | `git ls-remote --tags origin` 同上 |
| GitHub Releases | 未触碰 | `gh release list` 仅 v2.0 / v2.6 |
| `posts/` | 未触碰 | 无 patch / write |
| `case-study/` | 未触碰 | 无 patch / write |
| `release-assets/` | 未触碰 | 无 patch / write |
| `_template/` | **未创建** | 按本轮约束显式不创建 |
| `_pilots/` | **未创建** | 按本轮约束显式不创建 |
| untracked `.firecrawl/` | 未处理 | 仍为 untracked，未 add / rm |
| Hermes 生产配置 | 未触碰 | 无相关操作 |
| 新图片 | 未引入 | 无 image 写入 |
| `git add .` | 未使用 | 全部显式 add |

## 6. What this round did NOT do

明确记录本轮**没做**的事（避免任何 phantom 重建）：

- ❌ 未创建 `_template/`
- ❌ 未创建 `_pilots/`
- ❌ 未创建任何 tag（包括 v2.7 / v2.8 / v2.9 / v3.x）
- ❌ 未创建任何 GitHub Release
- ❌ 未修改 site 任何文件
- ❌ 未修改 posts / case-study / release-assets
- ❌ 未部署 pilot 到 GitHub Pages
- ❌ 未关闭任何 GitHub issue
- ❌ 未修改 Issue #1「v2.7 Bilingual Edition」（尽管 v2.7 实际不是 bilingual —— 留给 v2.7-real-stable-freeze round 处理）

## 7. Next recommended task

按 `docs/REALITY_CHECK_AFTER_PHANTOM_V3.md` 第 5 节「Recommended next step」，**推荐下一 round 为 v2.7-real-stable-freeze**：

1. 创建 `docs/RELEASE_NOTES_v2.7_ZH_EXHIBITION_POLISH.md`
2. 创建 `release-assets/v2.7-zh-exhibition-polish-manifest.md`
3. 创建 `reports/leonardo_chinese_exhibition_v2_7_real_stable_freeze_report.md`
4. 显式 add + commit + push
5. `git tag -a v2.7-zh-exhibition-polish` + `git push origin v2.7-zh-exhibition-polish`
6. `gh release create v2.7-zh-exhibition-polish`
7. live 重新验证 byte size / marker / placeholder / script.js
8. 更新 README「Stable Tag」字段指向 v2.7
9. 决定是否保留 / 重命名 / 关闭 Issue #1「v2.7 Bilingual Edition」

**推荐理由**：

- v2.7 内容真实存在并已上线，但没有独立 freeze 仪式
- freeze 是「记录真实状态」的动作，不是「创造新内容」，零破坏性
- 完成 v2.7 freeze 之后才有真实的 v2.7 → v2.8 起点
- v3.x 必须等 `_template/` 真实创建之后再讨论，不在 v2.7 freeze 之前

## 8. Final status

| 项 | 值 |
|---|---|
| STATUS | **PASS** |
| Commit | `Record verified project reality`（待 push 后确认） |
| HEAD after push | 预期 new commit (HEAD~1 = `71c7403`) |
| GitHub Actions status | 待 push 后由 `gh run list` / 实际 curl 验证 |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 85,564 B（v2.7 zh exhibition polish） |
| Verified live version | v2.7 zh exhibition polish |
| Existing tags | v2.0-public-portfolio-case (9e6233a), v2.6-content-stable (01cdaa2) |
| Missing directories | `_template/`, `_pilots/second-exhibition-pilot/` |
| Phantom stages recorded | v2.8 deep content / v2.9 source rights / v3.0 template audit / v3.1 template skeleton / v3.2 second exhibition pilot / v3.3 template documentation / Issue #16 |
| site files untouched | ✓ |
| tags untouched | ✓ |
| releases untouched | ✓ |
| posts/case-study/release-assets untouched | ✓ |

---

*本报告为 v3.3-phantom-recovery round 的最终交付。所有「verified」项均由本轮的 `<tool_use_result>` 凭据支撑；无 phantom 重建。*
