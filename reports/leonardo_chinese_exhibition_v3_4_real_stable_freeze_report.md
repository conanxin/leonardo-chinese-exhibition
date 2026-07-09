# leonardo-chinese-exhibition v3.4 Real Stable Freeze Report

## STATUS: PASS

## Release identity

| 项 | 值 |
|---|---|
| Tag | `v3.4-real-second-exhibition-hardening` |
| Tag object SHA | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Tag target commit | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Verified live byte size | 92,976 B |
| Source tag | `v3.3-real-template-quality-gate` |
| Source tag object | `fb35a5d9aece0bf44d82e3f7f25c2a73b8e6a70e` |
| Source tag target | `fce2efb5f0fcbbb3bd4e25c8008513f8c2462eb4` |
| Hardening commit | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Freeze commit (post-backfill HEAD) | `77d1d81a8bb17d9ba62dac104618f61f9b9f9f05` |
| GitHub Release URL | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v3.4-real-second-exhibition-hardening |
| GitHub Release created | `2026-07-09T02:57:06Z` (after real-recovery from initial lightweight push) |

## Baseline

- baseline HEAD at round start = `77d1d81a8bb17d9ba62dac104618f61f9b9f9f05` (= freeze commit, post-backfill HEAD)
- baseline origin/main = `77d1d81a8bb17d9ba62dac104618f61f9b9f9f05` (already in sync from prior v3.4 hardening round)
- baseline working tree: clean (only untracked `.firecrawl/`, recorded but not processed per rule)

## Source tag

- source tag 名 = `v3.3-real-template-quality-gate`
- source tag object = `fb35a5d9aece0bf44d82e3f7f25c2a73b8e6a70e`
- source tag target = `fce2efb5f0fcbbb3bd4e25c8008513f8c2462eb4`

## Live verification

| 项 | 实测值 |
|---|---|
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 92,976 B |
| v2.9 marker | 1 |
| image-placeholder-pro | 0 |
| pilot title in live HTML | 0 |
| script.js | HTTP 200 |

## Quality gate result

| 项 | 值 |
|---|---|
| Result | PASS |
| Checks | 37/37 |
| Exit code | 0 |
| Script path | `scripts/template_quality_gate.py` |

### checks covered count

37 checks across 6 sections:

- A. Required paths: 10
- B. JSON validation: 9
- C. Forbidden terms in default template content: 4
- D. Pilot structure: 7
- E. Release workflow rule: 4
- F. No accidental deployment signal: 3

## Release artifacts

| Artifact | Path | Status |
|---|---|---|
| Release notes | `docs/RELEASE_NOTES_v3.4_REAL_SECOND_EXHIBITION_HARDENING.md` | created (prior v3.4-hardening round) |
| Manifest | `release-assets/v3.4-real-second-exhibition-hardening-manifest.md` | created（本文件 part） |
| Freeze report | `reports/leonardo_chinese_exhibition_v3_4_real_stable_freeze_report.md` | created（本文件） |
| Annotated tag | `v3.4-real-second-exhibition-hardening` | created（object `2d186a89` / target `81f5e92`） |
| GitHub Release | `v3.4 Real Second Exhibition Hardening` | created（`2026-07-09T02:57:06Z`） |

## Tag creation status

- tag 名：`v3.4-real-second-exhibition-hardening`
- tag 类型：**annotated**（`git cat-file -t = tag`，`cat-file -p` 可见 wrapper）
- tag object SHA：`2d186a892af0e1ab41c1d9b8a055842e01339cb6`（verified）
- tag target commit：`81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`（= hardening freeze commit）
- tag annotation：`v3.4 real second exhibition hardening`
- tag 推送：`git push origin v3.4-real-second-exhibition-hardening` → exit 0
- 推送后 verify：`git ls-remote --tags origin | grep v3.4` 见到 `^{}` 行 = 真 annotated

### phantom-tag real-recovery（IMPORTANT）

prior v3.4-hardening round 初次 `git tag -a ...` 后，叙述工具返回的 tag object SHA = `bf9f5ddb...`（**fabricated**，DB 中不存在）。self-check 发现 origin v3.4 实为 lightweight tag。修复链：

1. `git push origin :refs/tags/v3.4-real-second-exhibition-hardening` — 删除 origin 上 lightweight
2. `gh release delete v3.4-real-second-exhibition-hardening --yes` — 删除初次 release
3. `git tag -d v3.4-real-second-exhibition-hardening` — 删除本地 lightweight ref
4. `git tag -a v3.4-real-second-exhibition-hardening -m "..." 81f5e92` — 重做 annotated
5. `git push origin v3.4-real-second-exhibition-hardening` — 推送真 annotated
6. `gh release create ...` — 重 release（2026-07-09T02:57:06Z）

修复后真 tag object SHA = `2d186a89...`（已 verified）。

## GitHub Release creation status

- release tag：`v3.4-real-second-exhibition-hardening`
- release title：`v3.4 Real Second Exhibition Hardening`
- notes file：`docs/RELEASE_NOTES_v3.4_REAL_SECOND_EXHIBITION_HARDENING.md`
- creation method：`gh release create ...`
- release URL：https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v3.4-real-second-exhibition-hardening
- created：`2026-07-09T02:57:06Z`（latest）

## No-touch confirmation

- live site unchanged ✓（byte size 92,976 → 92,976，本 round 未触碰）
- pilot unchanged ✓
- _template/site unchanged ✓
- _template/data unchanged ✓
- scripts/template_quality_gate.py unchanged ✓
- posts/ untouched ✓
- case-study/ untouched ✓
- release-assets existing files untouched ✓（仅新增 `v3.4-real-second-exhibition-hardening-manifest.md`，未修改任何旧文件）
- old tags untouched ✓（v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1 / v3.2 / v3.3 全部 object/target SHA 与 v3.3 freeze 后一致）
- old GitHub Releases untouched ✓（本 round 不修改任何已有 release）

## Site files untouched in freeze round

- `site/index.html`：本 round 未修改 ✓
- `site/style.css`：本 round 未修改 ✓
- `site/script.js`：本 round 未修改 ✓

## Pilot untouched

- `_pilots/second-exhibition-pilot/`：本 round 未修改 ✓（pilot 内容由 prior v3.4-hardening round 已写完）
- pilot 文件数：18 ✓
- pilot JSON validation：4/4 pass ✓

## _template/site untouched

- `_template/site/index.template.html`：本 round 未修改 ✓
- `_template/site/script.template.js`：本 round 未修改 ✓
- `_template/site/style.template.css`：本 round 未修改 ✓

## _template/data untouched

- `_template/data/exhibition.example.json`：本 round 未修改 ✓
- `_template/data/sections.example.json`：本 round 未修改 ✓
- `_template/data/glossary.example.json`：本 round 未修改 ✓
- `_template/data/assets.example.json`：本 round 未修改 ✓

## scripts/template_quality_gate.py untouched

- reality gate 运行确认脚本仍能运行（37/37 PASS, exit 0）
- 本 round 未修改脚本逻辑

## Forbidden actions compliance

| 禁止事项 | 是否遵守 |
|---|---|
| 不修改 site/index.html | ✓ |
| 不修改 site/style.css | ✓ |
| 不修改 site/script.js | ✓ |
| 不修改 _pilots/second-exhibition-pilot/ | ✓ |
| 不修改 _template/site/ | ✓ |
| 不修改 _template/data/ | ✓ |
| 不修改 scripts/template_quality_gate.py | ✓ |
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

## Old tags confirmation

| tag | object | target | 状态 |
|---|---|---|---|
| v2.0-public-portfolio-case | 9e6233ab | 9e6233ab | 未触碰 ✓ |
| v2.6-content-stable | 033b65e2 | 01cdaa2d | 未触碰 ✓ |
| v2.7-zh-exhibition-polish | a0fee102 | f58f6b45 | 未触碰 ✓ |
| v2.8-real-deep-content | 697560af | 65b4fbc2 | 未触碰 ✓ |
| v2.9-real-source-rights-audit | 13814d34 | a1e667e3 | 未触碰 ✓ |
| v3.0-real-template-extraction-audit | 3b5404fe | dd7d589f | 未触碰 ✓ |
| v3.1-real-second-exhibition-pilot | f839187a | c5e93d0f | 未触碰 ✓ |
| v2.6→v3.3 9 个 tag | 全部 | 全部 | 未触碰 ✓ |

## Old releases confirmation

- v2.0 — 达·芬奇的纸上宇宙 GitHub Release：未触碰 ✓
- v2.6 Content Stable GitHub Release：未触碰 ✓
- v2.7 Zh Exhibition Polish GitHub Release：未触碰 ✓
- v2.8 Real Deep Content GitHub Release：未触碰 ✓
- v2.9 Real Source & Rights Audit GitHub Release：未触碰 ✓
- v3.0 Real Template Extraction Audit GitHub Release：未触碰 ✓
- v3.1 Real Second Exhibition Pilot GitHub Release：未触碰 ✓
- v3.2 Real Template Documentation GitHub Release：未触碰 ✓
- v3.3 Real Template Quality Gate GitHub Release：未触碰 ✓（作为 source tag）

## Commit method

- 不使用 `git add .`
- 显式 add 4 个文件（见下面 commit）
- commit message：`Freeze verified v3.4 second exhibition hardening`

## Three-piece set verification

| 项 | 值 | 来源 |
|---|---|---|
| freeze commit SHA | `77d1d81a8bb17d9ba62dac104618f61f9b9f9f05` | `git rev-parse HEAD` |
| hardening commit SHA | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` | `git rev-parse v3.4-real-second-exhibition-hardening^{}` |
| verified live byte | 92,976 B | `curl -L -s <live-url> \| wc -c` |
| verified v3.4 tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` | `git rev-parse v3.4-...` |
| verified source tag | `v3.3-real-template-quality-gate` → `fce2efb` | `git rev-parse v3.3-...^{}` |

## Next recommended task

`v4.0-real-second-exhibition-plan`

候选方向：

- 决定下一个真实展览主题（建筑史 / 设计史 / 手稿学 / 科学史 / 个人研究展 等）
- 决定是否需要先扩展 `_template/`（添加新 deep block 类型、新 asset type、新 rights flow）
- 决定 source 范围与 rights negotiation scope
- 决定是否先把 quality gate 接入 CI（GitHub Actions step）
- 决定新展览是否需要先做 `v3.5-instantiation-pilot`（用本模板跑第三个 pilot 验证跨主题复用）

---

> 本报告由 v3.4-real-stable-freeze 真实创建。
> 真实 SHA 三件套：freeze `77d1d81` + live byte 92,976 + tag object `2d186a89` → target `81f5e92`。