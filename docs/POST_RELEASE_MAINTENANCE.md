# Post-release Maintenance

> v2.6 Content Stable 发布后的维护整理

## Current stable version

| 项 | 值 |
| --- | --- |
| **Active stable tag** | `v2.6-content-stable` |
| **Tag target commit** | `01cdaa2dc1487a5f7877c8702720d0df8dbb17ce` |
| **Live URL** | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| **GitHub Release** | <https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.6-content-stable> |
| **Live byte size** | 82,803 B |
| **Latest deploy run** | 见 `reports/` 中最新报告 |

## What should not change casually

以下项目在 v2.6-content-stable 之上**不应随意改动**：

- `site/index.html`（展览本体）
- `site/style.css`（排版）
- `site/script.js`（交互逻辑）
- `v2.0-public-portfolio-case` tag（历史 portfolio 冻结点）
- `v2.6-content-stable` tag（当前稳定基线）
- 旧 GitHub Releases（v2.0 release 等）
- `release-assets/` 既有截图与 manifest 文件

任何针对以上项目的修改都属于"破坏稳定基线"的操作，应在新版本（v2.7+）中处理。

## Safe maintenance tasks

这些任务**安全**且不破坏稳定基线：

- 修正错别字、标点、空格
- 优化 README 结构
- 新增 `docs/` 下的说明性 markdown
- 新增 `reports/` 下的诊断与 audit 报告
- 新增 GitHub Issues（路线跟踪）
- 为未来版本撰写 release notes 草稿
- 在 `docs/` 下补充 background / context / source notes

## Risky tasks requiring a new version

这些任务**应在新版本（v2.7+）中处理**，并通过新的 tag 冻结：

- 新增 / 替换图片
- 新增 / 修改交互逻辑
- 中英双语版本
- Education / Teacher Guide 模式
- 展览模板抽象 / 复用
- 大规模文案重写
- 修改 `site/index.html` / `style.css` / `script.js`

每一项都应在 GitHub Issue 中先讨论，再以独立分支实施，并以新 tag 收口。

## Deployment checklist

每次部署后应核查（**不要凭印象**，按 curl / Playwright 实地确认）：

- [ ] GitHub Actions workflow run = **success**
- [ ] `curl -L https://conanxin.github.io/leonardo-chinese-exhibition/ | grep "v2.6-content-stable"` → 1
- [ ] `curl -L ... | grep -c "image-placeholder-pro"` → **0**
- [ ] `curl -L ... | grep -c '<aside class="section-takeaway"'` → **9**
- [ ] `curl -LIs .../script.js` → **HTTP 200**
- [ ] 桌面端 Playwright → **15/15 PASS**（含 lightbox open/ESC, guided mode on/off, mobile 390 无溢出, 0 console errors）
- [ ] runtime section-nav DOM = **11**（用 Playwright `document.querySelectorAll('.section-nav').length` 确认；不要凭 static HTML grep = 0 误判）
- [ ] live byte size 与上次部署一致

## Known historical lessons

- 早前 v2.5 / v2.6 曾被报告为"已完成并上线"，但实际**从未进入 git 仓库**，live 一度仍为 v2.4。
- v2.5-real 阶段从真实 v2.4 / v2.7 当前状态重新实现并真实部署了导览与无障碍功能。
- v2.6 content copy polish 阶段补回了真实的中文文案审校、术语统一、图注 / source note 打磨。
- v2.6-content-stable 阶段清理了上一轮残留的 stale `v2.7-content-copy-polish` marker，统一版本字符串。
- v2.6 release publication 阶段创建了 GitHub Release 并发布了完整 release body。
- GitHub Pages deploy 有时会因为缓存或内部 race 出现 "Deployment failed, try again later" 错误，**retry 模式 = empty commit** 是有效 workaround（与 v2.5-real / v2.6 / v2.6-content-stable 一致）。

## Routine tasks

- 定期核查 live 状态（每天或每次 commit 后）
- 定期 review 既有 GitHub Issues
- 在新版本发布前更新 `docs/RELEASE_NOTES_<version>.md`
- 在新版本发布前更新 `reports/` 中的 audit / publication 报告

---

*Post-release maintenance plan — 配合 v2.6-content-stable 长期维护。*
