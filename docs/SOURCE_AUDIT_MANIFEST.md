# Source Audit Manifest

> 2026-07-07 · v2.9-real-source-rights-audit round
>
> 本文档基于当前仓库文件系统与 `site/index.html` 实际引用盘点，不引用任何 phantom v2.9 历史。
>
> 配套文档：[`RIGHTS_AND_SOURCES.md`](RIGHTS_AND_SOURCES.md)。

## Verified baseline

- **Source tag**: `v2.8-real-deep-content`
- **Source tag target**: `65b4fbc2b1bc742f263559145bb273c11cb3c6b0`
- **Live byte size at audit start**: 92,507 B
- **Audit version**: `v2.9-real-source-rights-audit`
- **Audit method**: 直接对仓库 `site/assets/` 与 `site/index.html` grep + 人工逐图核 `data-credit` / `figcaption` / `source-note` / `interface-note`，不依赖记忆或上轮叙述

## Asset summary

| Category | Count | 已纳入审计 | 备注 |
|---|---|---|---|
| Collection / manuscript images | 6 | 6 | 温莎 4 + Codex Atlanticus 2 |
| Platform screenshots | 4 | 4 | Leonardo//thek@ 本地截图 |
| Self-made SVG / project diagrams | 7 | 7 | 含 tool-wall / thinking-map 等 |
| Site metadata assets | 2 | 2 | favicon / og-cover |

合计 19 个本地资产文件 + 8 个 Wikimedia 文件级 URL 引用（每张馆藏图各 1）+ 2 个机构级 URL 引用（RCT / Ambrosiana）+ 1 个平台 URL 引用（Museo Galileo）。

## Collection / manuscript images（馆藏图像）

每张均通过 Wikimedia Commons 公共域授权引用，原件由温莎皇家收藏或米兰安布罗西安图书馆保管。

| File path | 中文标签 | Source institution | Source page / identifier | Used in | alt | caption | source-note | credit-line | lightbox | Rights note | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `site/assets/images/royal-collection/royal-horse-studies-rcin-912310.jpg` | 马的研究 · c.1490 | Royal Collection Trust | https://www.rct.uk/collection/912310 · RCIN 912310 | exhibit-index C + section3 C | ✓ | ✓ | ✓ (`公共域 · Wikimedia Commons`) | ✓ (`公共域 · Wikimedia Commons · Leonardo da Vinci, Royal Collection Trust`) | ✓ `data-credit` | 公共域（PD-old-70 / PD-art-old 等授权由 Wikimedia 文件页给出） | **high** |
| `site/assets/images/royal-collection/royal-water-studies-rcin-912660.jpg` | 水的涡旋研究 · c.1510-12 | Royal Collection Trust | https://www.rct.uk/collection/912660 · RCIN 912660 | exhibit-index D + section3 D | ✓ | ✓ | ✓ | ✓ | ✓ | 同上 | **high** |
| `site/assets/images/royal-collection/royal-shoulder-arm-rcin-919003.jpg` | 肩臂肌肉 · Verso · c.1510-11 | Royal Collection Trust | https://www.rct.uk/collection/919003 · RCIN 919003 | exhibit-index E + section3 E | ✓ | ✓ | ✓ | ✓ | ✓ | 同上 | **high** |
| `site/assets/images/royal-collection/royal-cats-lions-dragon-rcin-912363.jpg` | 猫、狮子与龙 · c.1517-18 | Royal Collection Trust | https://www.rct.uk/collection/912363 · RCIN 912363 | exhibit-index F + section3 F | ✓ | ✓ | ✓ | ✓ | ✓ | 同上 | **high** |
| `site/assets/images/codex-atlanticus/codex-atlanticus-f719-recto.jpg` | Codex Atlanticus f.719 recto · 钢笔墨水 / 机械与飞行器 | Veneranda Biblioteca Ambrosiana | https://ambrosiana.it/percorso/opere/codice-atlantico/ · folio f.719 recto | section2 · 大西洋手稿 | ✓ | ✓ | ✓（`Codex Atlanticus f.719 / f.21 的高清数字影印来自 Wikimedia Commons（公共域），原物由米兰 Veneranda Biblioteca Ambrosiana 收藏`） | ✓ | ✓ | 公共域（Wikimedia Commons 文件页给出的具体授权文本为准） | **high** |
| `site/assets/images/codex-atlanticus/codex-atlanticus-f21-recto.jpg` | Codex Atlanticus f.21 recto · 早期混合主题页 | Veneranda Biblioteca Ambrosiana | https://ambrosiana.it/percorso/opere/codice-atlantico/ · folio f.21 recto | section2 · 早期混合主题 | ✓ | ✓ | ✓（同上合并段落） | ✓ | ✓ | 同上 | **high** |

### 6 张馆藏图共同的 rights note（v2.9 收敛表述）

- 这 6 张图像均为达·芬奇手稿 / 绘图的高清数字影印，原件由温莎皇家收藏（Royal Collection Trust）或米兰安布罗西安图书馆（Veneranda Biblioteca Ambrosiana）保管
- 本展览通过 Wikimedia Commons 引用，按 Commons 文件页给出的授权文本（多为 PD-old-70 / PD-old-auto / PD-art-old / public domain）使用
- 本项目不声称拥有这些图像的版权
- 任何外部复用者应回到 Wikimedia Commons 文件页与馆藏页面自行确认授权边界

## Platform screenshots（平台截图）

| File path | Source platform | 截图 URL | 模块 | Used in | source-note | credit-line | Confidence |
|---|---|---|---|---|---|---|---|
| `site/assets/images/platform/platform-home-leonardotheka.jpg` | Leonardo//thek@ (Museo Galileo) | https://teche.museogalileo.it/leonardo/home/index_en.html | 首页 | section7 · 研究界面说明（首页） | ✓（`截图自 teche.museogalileo.it/leonardo/home/index_en.html · 2026-07-06 · 作者本地存档`） | ✓（`© Museo Galileo 2025 · Screenshot courtesy of Museo Galileo / Leonardo//thek@`） | **high** |
| `site/assets/images/platform/platform-watermarks.jpg` | Leonardo//thek@ (Museo Galileo) | https://teche.museogalileo.it/leonardo/filigrane | Watermarks | section4/5 · 水印模块 | ✓（`截图自 teche.museogalileo.it/leonardo/filigrane · 2026-07-06 · 作者本地存档`） | ✓（同上 credit） | **high** |
| `site/assets/images/platform/platform-recompositions.jpg` | Leonardo//thek@ (Museo Galileo) | https://teche.museogalileo.it/leonardo/ricostruzioni | Recompositions | section5 · 复原模块 | ✓（`截图自 teche.museogalileo.it/leonardo/ricostruzioni · 2026-07-06 · 作者本地存档`） | ✓ | **high** |
| `site/assets/images/platform/platform-advanced-search.jpg` | Leonardo//thek@ (Museo Galileo) | https://teche.museogalileo.it/leonardo/ricerca-avan | Advanced Search | `site/assets/images/` 中存在，**未在 `site/index.html` `<img>` 中引用** | — | — | **medium**（仅入档；如不使用应在未来轮明确标记 unused） |
| `site/assets/images/platform/platform-comparative-study.jpg` | Leonardo//thek@ (Museo Galileo) | https://teche.museogalileo.it/leonardo/studio-compare | Comparative Study | 同上，**未在 `site/index.html` `<img>` 中引用** | — | — | **medium** |

### 4 张引用截图共同的 rights note

- 平台界面与功能截图来自 Museo Galileo 维护的 Leonardo//thek@ 平台
- 用途：研究界面说明与评论上下文，不冒充原始艺术作品
- 截图日期：2026-07-06（作者本地存档）
- 外部复用者应自行取得 Museo Galileo 的 reuse 许可；本项目目前无书面 reuse 许可存档，建议在后续轮联系 Museo Galileo 取得书面答复

## Self-made diagrams / SVG（项目自绘图解）

| File path | Title | project-generated | Source basis | Used in | Rights note |
|---|---|---|---|---|---|
| `site/assets/diagrams/collection-split.svg` | 手稿流散与重连路径 | ✓ | 基于公开学术资料 | hero + exhibit-index | 项目自绘 · CC0（如需开放许可请参见项目 LICENSE，v2.9 未生成） |
| `site/assets/diagrams/manuscript-journey.svg` | 大西洋手稿与温莎绘图的分藏 | ✓ | 基于安布罗西安图书馆与 Royal Collection Trust 公开资料 | section2 | 项目自绘 |
| `site/assets/diagrams/thinking-map.svg` | 图像即思考 | ✓ | 基于公开学术资料 | section4 | 项目自绘 |
| `site/assets/diagrams/watermark-evidence-chain.svg` | 水印与纸张证据链 | ✓ | 基于公开学术资料 | section5 | 项目自绘 |
| `site/assets/diagrams/recomposition-triptych.svg` | 复原三联图 | ✓ | 基于公开学术资料 | section5 | 项目自绘 |
| `site/assets/diagrams/platform-structure.svg` | 平台结构示意 | ✓ | 基于平台公开信息 | section7（context，未 `<img>` 引用） | 项目自绘 |
| `site/assets/diagrams/platform-tool-wall.svg` | 工具墙 · 9 模块 | ✓ | 基于平台公开信息 | section7 · 工具墙 | 项目自绘（明确为「示意图 · 作者基于平台公开信息绘制」） |

> 项目自绘图解的 source-note 在 `<figcaption>` 中统一以「示意图 · 作者绘制」形式标注，没有伪装为原始资料。

## Metadata assets

| File path | Purpose | 备注 |
|---|---|---|
| `site/assets/favicon.svg` | 网站图标 | 项目自绘 SVG，无外部素材 |
| `site/assets/og-cover.svg` | Open Graph 封面 | 项目自绘 SVG，无外部素材 |

## External links audited (lightweight curl -I)

| URL | HTTP | 用途 | Notes |
|---|---|---|---|
| `https://conanxin.github.io/leonardo-chinese-exhibition/` | 200 | live 主站 | ✓ |
| `https://github.com/conanxin/leonardo-chinese-exhibition` | 200 | 仓库 | ✓ |
| `https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.8-real-deep-content` | 200 | 上一轮 release | ✓ |
| `https://www.rct.uk/collection/` | **403** (curl) | 馆藏根 | ⚠️ 通常对 bot / 非浏览器 UA 返回 403；浏览器访问 200。页面中馆藏链接指向具体条目（912310 / 912660 / 919003 / 912363），按 brief 不修改 |
| `https://www.ambrosiana.it/` | 200 | 馆藏根 | ✓ |
| `https://teche.museogalileo.it/leonardo/` | 200 | 平台根 | ✓ |
| 6 张 Wikimedia Commons 文件页 | 200 | 馆藏图源 | ✓ |

## Missing / follow-up items

1. **Museo Galileo 平台截图 reuse 许可**：本项目目前没有书面 reuse 许可存档。截图仅用于研究说明与评论上下文（fair use 评论性使用），但若要在其他场景公开复用，应联系 Museo Galileo 取得书面答复
2. **`platform-advanced-search.jpg` / `platform-comparative-study.jpg` 是已下载但未引用**：本轮只在 manifest 中标注为「未引用 / 待后续轮决定」；如确认不再使用，应从仓库删除以减少混淆
3. **馆藏图复用边界细节**：本次审计只到 Wikimedia Commons 文件页层级；具体到机构级 reuse 政策（如 RCT 的「Take Down Policy」），未深入比对
4. **RCIN 编号与 Wikimedia Commons 文件 ID 的一致性**：本次 audit 已逐张核对 RCIN 编号（912310 / 912660 / 919003 / 912363）与 Wikimedia 文件名嵌入的编号一致；下次新增图时必须再做一次核对
5. **Leonardo//thek@ 平台界面变化**：平台是活体项目，截图会过期；如平台改版，需要重新截图并更新 source-note 中的截图日期
6. **项目 LICENSE 文件**：本项目仓库根无 LICENSE；项目自绘 SVG 与文案当前隐含「保留所有权利」。在 v3.0 之前不擅自声明开放许可

---

*本文档是 v2.9 真实审计的唯一真值表。下一轮（v2.9-real-stable-freeze）以本 manifest 的 audit 数字为基线。*