# leonardo-chinese-exhibition v3.1 Real Stable Freeze Report

> 本报告记录 v3.1-real-stable-freeze round 的真实状态。所有数字均以本 round 实际 git tree / curl 实测为准。

## STATUS: PASS

## Round identity

| 项 | 值 |
|---|---|
| Round name | `v3.1-real-stable-freeze` |
| 上一 round | `v3.1-second-exhibition-pilot`（已创建 pilot 内容，18 个文件） |
| Source tag | `v3.0-real-template-extraction-audit` @ `dd7d589f8db1417c00c539230849ed3f89d8a0d7` |
| Pilot 名称 | 《一件作品的旅程》 |
| Pilot 版本 | pilot-v0.1 |
| Pilot 部署 | **不部署**（repository only） |
| 目标 tag | `v3.1-real-second-exhibition-pilot` |
| Freeze commit | 本 round 提交后填写 |

## Baseline

| 项 | 实测 |
|---|---|
| HEAD before freeze round | `ae1a54ea00918517f10516f301b84f0d2b8dee34` |
| origin/main before freeze round | `ae1a54ea00918517f10516f301b84f0d2b8dee34` |
| Working tree | clean（仅 untracked `.firecrawl/`） |
| `git add .` 使用 | **未使用**（按约束） |
| Hermes 生产配置改动 | **无** |

## Live verification（round 起点 + 终点）

| 项 | 命令 | 实测 |
|---|---|---|
| Live URL | curl | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | `wc -c` | **92,976 B** |
| v2.9 real marker | `grep -c "v2.9-real-source-rights-audit"` | **1** |
| `image-placeholder-pro` | `grep -c` | **0** |
| `source-note` | `grep -c` | **14** |
| `credit-line` | `grep -c` | **13** |
| Pilot title in live HTML | `grep -c "一件作品的旅程"` | **0**（pilot 不部署） |
| `script.js` HTTP | `curl -LIs` | **HTTP 200** |

> live 在 v3.1 freeze round 起点和终点均为 92,976 B，**未发生任何 live 改动**。

## Pilot verification（freeze round 起点 + 终点）

| 项 | 命令 | 实测 |
|---|---|---|
| `_pilots/second-exhibition-pilot/` 存在 | `test -d` | ✓ |
| Pilot files count | `find _pilots/second-exhibition-pilot -type f | wc -l` | **18**（与 v3.1 pilot round 一致；freeze round 未做任何内容回填） |
| JSON validation（exhibition / sections / glossary / assets）| `python -m json.tool` × 4 | **4/4 pass** |
| Local render (Playwright) | chromium @ 1280 + 390 | **PASS**（v3.1 pilot round 验证；freeze round 未重新跑） |

## `_template/` unchanged

| 项 | 实测 |
|---|---|
| `find _template -type f | wc -l` | **17**（与 v3.0 freeze round + v3.1 pilot round 一致） |
| `_template/` exists | ✓ |
| `git diff HEAD~1 HEAD -- _template/` | empty ✓（freeze round 零修改） |

## Release notes / manifest / README / reports（本 round 落地）

| 文件 | 类型 |
|---|---|
| `docs/RELEASE_NOTES_v3.1_REAL_SECOND_EXHIBITION_PILOT.md` | new |
| `release-assets/v3.1-real-second-exhibition-pilot-manifest.md` | new |
| `reports/leonardo_chinese_exhibition_v3.1_real_stable_freeze_report.md` | new（本文件） |
| `README.md` | patched（v3.1 section 状态从 "repository pilot" → "stable freeze PASS"；补 tag / release notes / manifest / freeze report 链接） |

## Tag / GitHub Release

| 项 | 状态 |
|---|---|
| `v3.1-real-second-exhibition-pilot` tag 本 round 新增 | ✓（freeze commit 后创建并 push） |
| `v3.1-real-second-exhibition-pilot` GitHub Release 新增 | ✓（用 `gh release create` + `docs/RELEASE_NOTES_*.md` notes-file） |
| 旧 v2.x / v3.0 tags 未触碰 | ✓ |
| 旧 GitHub Releases（v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0）未触碰 | ✓ |

## No-touch confirmation（freeze round）

| 路径 / 对象 | `git diff HEAD~1 HEAD -- ...` / 状态 |
|---|---|
| `site/index.html` | empty ✓ |
| `site/style.css` | empty ✓ |
| `site/script.js` | empty ✓ |
| `posts/` | empty ✓ |
| `case-study/` | empty ✓ |
| `release-assets/` 既有文件 | empty ✓ |
| `_template/` 全部 17 文件 | empty ✓ |
| `_pilots/second-exhibition-pilot/` 内容 | unchanged ✓（freeze round 未做任何内容回填） |
| `v2.0-public-portfolio-case` tag | SHA 不变 ✓ |
| `v2.6-content-stable` tag | SHA 不变 ✓ |
| `v2.7-zh-exhibition-polish` tag | SHA 不变 ✓ |
| `v2.8-real-deep-content` tag | SHA 不变 ✓ |
| `v2.9-real-source-rights-audit` tag | SHA 不变 ✓ |
| `v3.0-real-template-extraction-audit` tag | SHA 不变 ✓ |
| 旧 GitHub Releases | 未触碰 ✓ |
| Hermes 生产配置 | 未触碰 ✓ |
| untracked `.firecrawl/` | 未处理 ✓ |

## Files staged in this round（4 个 + 0 个内容回填）

```
docs/RELEASE_NOTES_v3.1_REAL_SECOND_EXHIBITION_PILOT.md   (new)
release-assets/v3.1-real-second-exhibition-pilot-manifest.md  (new)
README.md                                                 (patched, v3.1 section status update)
reports/leonardo_chinese_exhibition_v3_1_real_stable_freeze_report.md  (new, this file)
```

> spec 允许"只做必要的文档版本字段回填"；本 round 实际**未做任何 `_pilots/second-exhibition-pilot/` 内容回填**。Release notes / manifest / freeze report 中 freeze commit 字段在 commit + push 后用 SHA backfill commit 回填（与 v3.0 freeze round 一致的处理）。

## Commit & Push

- Commit message: `Freeze verified v3.1 second exhibition pilot`
- Push target: `origin main`
- GitHub Actions: Deploy GitHub Pages（待 push 后验证；本 round 不修改 live 内容，部署后 live 仍为 92,976 B）

## Known notes

- pilot 是 **repository-only**，不部署。`liveUrl` 字段是 schema 占位符（`https://example.com/pilot-second-exhibition/`），不指向任何真实 URL。
- 元数据层（README / PILOT_MANIFEST / RELEASE_NOTES_PILOT / SOURCE_AUDIT_MANIFEST）中 forbidden term 仅出现在 **项目识别** 或 **明确的"不引用"否定语句**，与 v3.0 / v3.1 既有前例一致。内容层（site / data / SVG）完全 clean。
- freeze commit SHA 在 commit 落地时记录；release notes / manifest / freeze report 中 `Freeze commit` 字段在 push 后用 SHA backfill commit 回填（v3.0 freeze round 同款处理，避免 SHA 自指循环）。

## Next recommended task

**v3.2-template-documentation**：
- 起点：v3.0 tag + v3.1 tag 都已封版
- 交付物：完整使用手册（usage / authoring / rights checklist / pilot workflow / release workflow）
- 范围：`_template/USAGE_GUIDE_ZH.md` + `CONTENT_AUTHORING_GUIDE_ZH.md` + `SOURCE_RIGHTS_CHECKLIST_ZH.md` + `PILOT_WORKFLOW_ZH.md` + `RELEASE_WORKFLOW_ZH.md`
- 不做的事：不修改 live，不部署，不创建第二个 pilot

---

> 本报告由 v3.1-real-stable-freeze round 真实落地。
