# Rights and Sources

> 2026-07-07 · v2.9-real-source-rights-audit round
>
> 本文档说明本项目如何使用图片、平台截图与图解，以及外部复用者应注意的边界。
>
> 配套清单：[`SOURCE_AUDIT_MANIFEST.md`](SOURCE_AUDIT_MANIFEST.md)。

## Purpose

本项目是「达·芬奇的纸上宇宙」中文数字展览与研究型展示项目。所有图片、平台截图、图解与图注用于**评论、研究、教育、展览说明与来源讨论**。

- 评论与研究：每张图都带 source-note / credit-line / data-credit，可在原机构页面交叉验证
- 教育：图注解释画作内容与方法，不替代原机构策展
- 展览说明：本项目可作为中文读者的入门，但**不替代**温莎皇家收藏、安布罗西安图书馆与 Leonardo//thek@ 平台本身的策展内容

## Source categories

### A. Collection / manuscript images（馆藏图像）

6 张高清数字影印，来自温莎皇家收藏（4 张）与《大西洋手稿》（2 张）：

- 温莎 4 张：horse studies / water studies / shoulder-arm / cats-lions-dragon（c.1490–1518）
- Codex Atlanticus 2 张：f.719 recto / f.21 recto

**授权路径**：通过 Wikimedia Commons 引用，按 Commons 文件页给出的具体授权文本（多为 PD-old-70 / PD-old-auto / PD-art-old）使用。

**注意**：
- Wikimedia Commons 文件页给出的授权状态是最终依据
- 本项目**不**声称拥有这些图像的版权
- 任何外部复用者应回到 Wikimedia Commons 文件页与馆藏页面自行确认授权边界

### B. Platform screenshots（平台截图）

4 张 Leonardo//thek@ 平台界面截图（首页 / Watermarks / Recompositions / 另 2 张已下载但未引用）。

**用途**：研究界面说明与评论上下文，明确说明「这是平台截图」，不冒充原始艺术作品。

**授权路径**：
- 截图来自 Museo Galileo 维护的 Leonardo//thek@ 平台
- 截图日期 2026-07-06，作者本地存档
- 本项目目前**无书面 reuse 许可存档**；以评论性使用（fair use / 评论上下文）为基础
- 若要在其他场景公开复用，应联系 Museo Galileo 取得书面答复（这是 v3.0 之前的 follow-up 项）

### C. Project-generated diagrams（项目自绘图解）

7 个 SVG 文件（collection-split / manuscript-journey / thinking-map / watermark-evidence-chain / recomposition-triptych / platform-structure / platform-tool-wall）。

**授权路径**：
- 项目作者原创
- 当前仓库根**无 LICENSE**，隐含「保留所有权利」
- v2.9 不擅自声明开放许可（如需 CC0 / CC-BY，请单独 round 处理）
- 在 `<figcaption>` 中统一以「示意图 · 作者绘制」形式标注，明确 project-generated 身份，不伪装为原始资料

### D. Site metadata assets（站点元数据）

- favicon.svg：项目自绘
- og-cover.svg：项目自绘

无外部素材。

## How sources are credited

本项目用三层方式标注来源：

1. **页面层（`<figcaption>` 内 `<span class="source-note">` 与 `<span class="credit-line">`）**：每张图都有 source-note + credit-line 双标注；项目自绘图解的 source-note 写「示意图 · 作者绘制」+ brief 依据
2. **lightbox 层（`data-credit` 属性）**：点击放大图后弹出层仍显示 credit，与 figcaption 一致
3. **文档层**：
   - [`SOURCE_AUDIT_MANIFEST.md`](SOURCE_AUDIT_MANIFEST.md) — 详细清单（每张图的文件、源机构、源 URL、授权边界、confidence）
   - release notes 与 manifest — 记录 audit round + 凭据

## Reuse caution

**重要声明**：

1. **本项目不声称拥有馆藏图像版权**。馆藏图像归温莎皇家收藏 / 安布罗西安图书馆所有；数字影印通过 Wikimedia Commons 按文件页授权文本引用
2. **外部复用馆藏图像时应回到原机构页面与 Wikimedia 文件页确认授权**。不同图像授权可能不同（PD-old-70 / PD-old-auto / PD-art-old / 其他）
3. **平台截图仅用于研究说明和评论上下文**。Museo Galileo 的 reuse 政策未单独存档；评论性使用之外应取得书面答复
4. **自制 SVG / 项目文案按本仓库当前实际状态处理**：仓库根无 LICENSE，目前隐含「保留所有权利」。除非显式 LICENSE 文件存在，否则**不要擅自声明 SVG 为公共域或开放许可**
5. **本文档不是法律意见**。如需正式授权判断，请咨询专业律师或直接联系馆藏机构

## Known limitations

- 部分具体授权边界需以 Wikimedia Commons 文件页与馆藏机构页面为准，本文档无法逐文件穷举
- 馆藏页面（如 rct.uk）可能改版或调整 reuse 政策；本审计基于 2026-07-07 的访问
- 平台界面（teche.museogalileo.it）是活体项目，截图会随平台改版而需要更新
- 当前审计仅基于仓库文件与可访问页面；如未来新增图像 / 截图 / 自绘 SVG，**必须重新审计**
- Museo Galileo 平台截图的 reuse 许可目前**未取得书面答复**；按 fair use / 评论性使用原则使用，重用前请联系

## Follow-up items

1. 联系 Museo Galileo 取得平台截图的书面 reuse 答复
2. 删除或保留 `platform-advanced-search.jpg` / `platform-comparative-study.jpg`（已下载但未引用）
3. 在 v3.0 之前为项目自绘 SVG 决定显式 LICENSE（CC0 / CC-BY / 保留所有权利）
4. 馆藏机构级 reuse 政策的正式比对（RCT「Take Down Policy」、Ambrosiana 等）

---

*本文档是 v2.9 round 的 rights 综述，不是法律意见。如需逐张图的详细审计，请参见 [`SOURCE_AUDIT_MANIFEST.md`](SOURCE_AUDIT_MANIFEST.md)。*