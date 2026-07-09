# leonardo-chinese-exhibition v3.2 Real Stable Freeze Report

## STATUS: PASS

## Release identity

| 项 | 值 |
|---|---|
| Tag | `v3.2-real-template-documentation` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Verified live byte size | 92,976 B |
| Source tag | `v3.1-real-second-exhibition-pilot` |
| Documentation commit | `2f617b1e6dc02f40683c2eb69101c4557670bbc0` |
| Freeze commit | `5a89fb2061ef3eee95c63dc3592d92fb859177fe` |

## Baseline

- baseline HEAD = `2f617b1e6dc02f40683c2eb69101c4557670bbc0`
- baseline origin/main = `2f617b1e6dc02f40683c2eb69101c4557670bbc0`
- baseline 工作树状态：clean（仅 untracked `.firecrawl/`，按规则单独记录但不处理）

## Source tag

- source tag 名 = `v3.1-real-second-exhibition-pilot`
- source tag object = `f839187ae3c4382084b3b29aeba5df0c67238db8`
- source tag target = `c5e93d0f6387572e342213737ac1f7e191c2268e`

## Live verification

| 项 | 实测值 |
|---|---|
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 92,976 B |
| v2.9 marker | 1 |
| image-placeholder-pro | 0 |
| pilot title in live HTML | 0 |
| script.js | HTTP 200 |

## Documentation files (5)

1. `_template/USAGE_GUIDE_ZH.md`
2. `_template/CONTENT_AUTHORING_GUIDE_ZH.md`
3. `_template/SOURCE_RIGHTS_CHECKLIST_ZH.md`
4. `_template/PILOT_WORKFLOW_ZH.md`
5. `_template/RELEASE_WORKFLOW_ZH.md`

## Reality recovery rule check

| 项 | 状态 |
|---|---|
| RELEASE_WORKFLOW_ZH.md 包含 "commit SHA + verified live byte + verified tag" 短语 | yes（`grep -c` = 1） |
| 三件套校验方法文档化 | yes |
| 三件套在 release notes 中实写 | yes |
| 三件套在 manifest 中实写 | yes |

## Release artifacts

| Artifact | Path | Status |
|---|---|---|
| Release notes | `docs/RELEASE_NOTES_v3.2_REAL_TEMPLATE_DOCUMENTATION.md` | created |
| Manifest | `release-assets/v3.2-real-template-documentation-manifest.md` | created |
| Freeze report | `reports/leonardo_chinese_exhibition_v3_2_real_stable_freeze_report.md` | created（本文件） |
| Annotated tag | `v3.2-real-template-documentation` | created（见 tag creation status） |
| GitHub Release | `v3.2-real-template-documentation` | created（见 release creation status） |

## Tag creation status

- tag 名：`v3.2-real-template-documentation`
- tag 类型：annotated
- tag 创建时机：commit + push 成功之后
- tag target commit：freeze commit（commit 后回填）
- tag object SHA：创建后回填
- tag push：`git push origin v3.2-real-template-documentation`

## GitHub Release creation status

- release tag：`v3.2-real-template-documentation`
- release title：`v3.2 Real Template Documentation`
- notes file：`docs/RELEASE_NOTES_v3.2_REAL_TEMPLATE_DOCUMENTATION.md`
- creation method：`gh release create`
- release URL：创建后回填

## No-touch confirmation

- live site unchanged ✓
- pilot unchanged ✓
- posts/ untouched ✓
- case-study/ untouched ✓
- release-assets existing files untouched ✓（仅新增 `v3.2-real-template-documentation-manifest.md`，未修改任何旧文件）
- old tags untouched ✓（v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1 全部 object SHA 与 target SHA 与 v3.1 freeze 后一致）
- old GitHub Releases untouched ✓（本 round 不修改任何已有 release）

## Site files untouched in freeze round

- `site/index.html`：本 round 未修改 ✓
- `site/style.css`：本 round 未修改 ✓
- `site/script.js`：本 round 未修改 ✓

## Pilot untouched

- `_pilots/second-exhibition-pilot/`：本 round 未修改 ✓
- pilot 文件数：18 ✓
- pilot JSON validation：4/4 pass ✓

## Forbidden actions compliance

| 禁止事项 | 是否遵守 |
|---|---|
| 不修改 site/index.html | ✓ |
| 不修改 site/style.css | ✓ |
| 不修改 site/script.js | ✓ |
| 不修改 _pilots/second-exhibition-pilot/ | ✓ |
| 不修改 _template/ 手册正文 | ✓ |
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
| v3.1-real-second-exhibition-pilot | f839187a | c5e93d0f | 未触碰 ✓（作为 source tag） |

## Old releases confirmation

- v2.0-public-portfolio-case GitHub Release：未触碰 ✓
- v2.6-content-stable GitHub Release：未触碰 ✓
- v3.0-real-template-extraction-audit GitHub Release：未触碰 ✓
- v3.1-real-second-exhibition-pilot GitHub Release：未触碰 ✓

## Commit method

- 不使用 `git add .`
- 显式 add 4 个文件：
  - `docs/RELEASE_NOTES_v3.2_REAL_TEMPLATE_DOCUMENTATION.md`
  - `release-assets/v3.2-real-template-documentation-manifest.md`
  - `README.md`
  - `reports/leonardo_chinese_exhibition_v3_2_real_stable_freeze_report.md`
- commit message：`Freeze verified v3.2 template documentation`

## Three-piece set verification

| 项 | 值 | 来源 |
|---|---|---|
| commit SHA | `5a89fb2061ef3eee95c63dc3592d92fb859177fe` | `git rev-parse HEAD` |
| verified live byte | 92,976 B | `curl -L -s <live-url> \| wc -c` |
| verified tag | （tag 创建后回填） | `git rev-parse <tag>^{}` |

## Next recommended task

`v3.3-template-quality-gate` 或 `v3.3-real-second-exhibition-hardening`

候选方向：

- 给 `_template/` 补 README + ajv 校验
- 把 v3.1 pilot 中的人工写作部分沉淀为模板默认内容
- 在 `_template/data/` 中加入第二个 example 主题，验证模板对不同主题的可复用性
- 给 5 个手册加上英文版本
- 给 release workflow 加入自动化脚本（基于 reality recovery rule）

---

## freeze commit 回填（commit + tag 创建后填）

- freeze commit：`5a89fb2061ef3eee95c63dc3592d92fb859177fe`
- tag object：`77a89fb5ffccaae0f686ed2eb388453b1901fe33`
- tag target：`5a89fb2061ef3eee95c63dc3592d92fb859177fe`（annotated tag → freeze commit）
- GitHub Release URL：https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v3.2-real-template-documentation
- Actions run id：`28988636250`（覆盖 freeze `5a89fb2` + backfill `a092acb`，Pages deploy success）

---

> 本报告由 v3.2-real-stable-freeze 真实创建，所有 live / tag / 文件计数均来自本 round 实测。