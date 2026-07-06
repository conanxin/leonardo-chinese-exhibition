# leonardo-chinese-exhibition — v2.6 GitHub Release Publication Report

## STATUS

**PASS ✓** — v2.6 GitHub Release 已创建并发布，docs / manifest / README 全部就位，no-touch 严格遵守。

## Baseline

| 项 | 值 |
| --- | --- |
| **HEAD (at start of v2.6-release-publication)** | `3a422510873e88198b555971e504062f3b5c38bf` |
| **origin/main (at start)** | `3a422510873e88198b555971e504062f3b5c38bf` |
| **HEAD (at end of v2.6-release-publication)** | `3f74094...`（retry 后的 deploy commit）|
| **stable tag name** | `v2.6-content-stable` |
| **tag target commit** | `01cdaa2dc1487a5f7877c8702720d0df8dbb17ce`（freeze commit，未移动）|
| **v2.0 tag** | `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4`（未触碰）|
| **Live URL** | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| **Live byte size** | 82,803 B（site 未改动，与 v2.6-content-stable 一致）|

## GitHub Release

| 项 | 值 |
| --- | --- |
| **Release URL** | <https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.6-content-stable> |
| **Tag** | `v2.6-content-stable` |
| **Title** | v2.6 Content Stable |
| **Draft** | `false` ✓ |
| **Prerelease** | `false` ✓ |
| **Author** | conanxin |
| **Created (tag)** | 2026-07-06T08:52:32Z |
| **Published (with notes)** | 2026-07-06T09:14:37Z |
| **Notes file** | `docs/GITHUB_RELEASE_v2.6_CONTENT_STABLE.md`（通过 `--notes-file` 上传）|
| **targetCommitish** | main |

## Docs / manifest created

| 文件 | 状态 | 大小 |
| --- | --- | --- |
| `docs/GITHUB_RELEASE_v2.6_CONTENT_STABLE.md` | **new** | 3.0 KB |
| `release-assets/v2.6-content-stable-manifest.md` | **new** | 3.1 KB |
| `README.md` | modified | +1 Stable release 段 + GitHub Release 段补充 v2.6 链接 |

## README updated

- 增加 `## Stable release` 段（说明 v2.6-content-stable 为 active stable release）
- 更新 `## 当前版本` 段（增加 v2.6-content-stable 为 Active stable tag）
- 更新 `## GitHub Release` 段（增加 v2.6 release 链接与 docs / manifest 引用）

## Live verification

| 项 | 值 | 状态 |
| --- | --- | --- |
| Live HTTP | 200 | ✓ |
| Live byte size | 82,803 B | ✓ |
| v2.6-content-copy-polish marker | 1 | ✓ |
| v2.6-content-stable marker | 1 | ✓ |
| image-placeholder-pro | 0 | ✓ |
| section-takeaway | 9 | ✓ |
| script.js HTTP | 200 | ✓ |
| site/index.html | 未改动 | ✓ |
| site/style.css | 未改动 | ✓ |
| site/script.js | 未改动 | ✓ |

## Commit chain (v2.6-release-publication)

| commit | message | 状态 |
| --- | --- | --- |
| `6023408` | Prepare v2.6 GitHub release package | pushed, Pages run 28780795419 success |
| `ee356a8` | Add v2.6 GitHub release link | pushed, Pages run 28780868817 failure (transient) |
| `3f74094` | Retry Pages deploy (post-release-link-backfill) | pushed, Pages run 28780905727 success |
| `reports/...` | Record v2.6 GitHub release publication | (本文件，待提交) |

## No-touch confirmation

| 项 | 状态 |
| --- | --- |
| `v2.0-public-portfolio-case` tag | **未触碰**（仍 `9e6233ab...`）|
| 旧 v2.0 GitHub Release | **未触碰**（标题 "v2.0 — 达·芬奇的纸上宇宙：中文数字展览稳定版"）|
| `v2.6-content-stable` tag | **未移动**（仍指向 freeze commit `01cdaa2`）|
| `posts/` | **未触碰**（last commit `75fd9f9` Create v1.6 distribution pack）|
| `case-study/` | **未触碰**（last commit `ae946b3` Create v2.0 public portfolio case）|
| `release-assets/` 既有文件 | **未触碰**（`manifest.md` / `screenshots/*` 未改动；仅新增 `v2.6-content-stable-manifest.md`）|
| `site/index.html` / `style.css` / `script.js` | **未触碰** |
| Hermes 生产配置 | **未触碰** |
| untracked `.firecrawl/` | **未处理** |

## Screenshot assets policy

- 本轮 **不新增截图**
- 复用 v2.1 release 已有截图（`release-assets/screenshots/` 中既有 v2.1 截图）作为历史发布资产
- **不修改** `release-assets/` 既有截图与文件
- 仅新增本 manifest（`v2.6-content-stable-manifest.md`）作为 v2.6 release 的发布记录

## Next step recommendation

- v2.6 GitHub Release 是当前最稳定可对外引用的版本快照
- 后续如做 v2.7+，建议基于 `v2.6-content-stable` tag 派生新分支
- 若未来要为 v2.6 release 补充截图，建议在 `release-assets/screenshots/v2.6/` 下新建子目录，不修改既有截图
- v2.0 GitHub Release 保持原样作为 portfolio 历史，**不删**

---

*v2.6 release publication PASS — 真实稳定版快照已发布。*
