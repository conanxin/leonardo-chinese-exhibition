# v2.6 Content Stable — Leonardo Chinese Exhibition

> 达·芬奇的纸上宇宙 — 内容稳定版

## Live

https://conanxin.github.io/leonardo-chinese-exhibition/

## Tag

`v2.6-content-stable`

## Stable commit

`01cdaa2dc1487a5f7877c8702720d0df8dbb17ce`

## What this release is

这是《达·芬奇的纸上宇宙》中文数字展览的内容稳定版。它基于 Leonardo//thek@ 与相关馆藏资料，完成了真实手稿图像、平台截图、展品注释、术语表、导览模式、lightbox、runtime section-nav 与内容审校。

它是 v2.5-real 误报被纠正后形成的真实稳定版本线，作为当前可对外引用的展览快照。

## Highlights

- 中文数字展览主页
- 真实手稿图像与平台截图
- 展品索引
- 参观路线
- 5 分钟导览模式（guided mode）
- runtime-generated section-nav
- tour progress 顶部进度条
- lightbox 展品放大阅读（含 focus trap、ESC 关闭、focus 返回）
- 展品 annotation panels ×4（温莎手稿关键图版）
- 研究平台 interface notes ×5
- glossary 术语表 ×14
- 内容审校与术语统一
- GitHub Pages live deployment（workflow-driven build）

## Corrected version line

记录真实版本线：

| 版本 | 用途 | commit |
| --- | --- | --- |
| v2.4 artifact annotation upgrade | 展品注释面板 + glossary | `c3c3e0b` |
| v2.5-real guided accessibility recovery | 重建导览 + 无障碍 + runtime section-nav | `c512dbd` |
| v2.6 content copy polish | 全站中文文案审校、术语统一、图注 / source note 统一 | `d71b0e8` |
| **v2.6-content-stable** | **稳定封版、release notes、final audit、清理 stale v2.7 marker** | `01cdaa2` |

**说明**：早前 v2.5 / v2.6 曾出现误报。后续通过 v2.5-real recovery 与 v2.6 content copy polish 重新校正，并以 `v2.6-content-stable` 作为当前真实稳定版。

## Verification

| 项 | 值 |
| --- | --- |
| Live HTTP | 200 |
| Live byte size | 82,803 B |
| section-nav runtime DOM | 11 |
| static HTML section-nav | 0（正确，runtime 生成） |
| section-takeaway | 9 |
| image-placeholder-pro | 0 |
| glossary | 14 |
| annotation panels | 4 |
| platform interface notes | 5 |
| script.js | HTTP 200 |
| v2.7 stale marker | 0（已清理）|
| mobile 390 overflow | 0 px |
| console errors | 0 |
| Playwright live | 15/15 PASS |
| GitHub Pages deploy | success |

## No-touch confirmation

- `v2.0-public-portfolio-case` tag — **未触碰**
- 旧 v2.0 GitHub Release — **未触碰**
- `posts/` — **未触碰**
- `case-study/` — **未触碰**
- `release-assets/` 既有文件 — **未触碰**（本轮仅新增 v2.6 release manifest）
- `site/index.html` / `style.css` / `script.js` — **未触碰**

## Notes

这个 release 主要冻结展览本体与内容稳定状态，不包含新的社交传播素材或新一轮功能扩展。

任何 v2.7+ 的迭代应基于 `v2.6-content-stable` tag 派生新分支。

---

*Released: v2.6 Content Stable — 真实达·芬奇手稿数字展览稳定版。*
