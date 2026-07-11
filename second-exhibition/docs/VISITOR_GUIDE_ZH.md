# 3 分钟导览 / Visitor Guide

> 本文件是《植物图谱与视觉分类》展览的 3 分钟导览。展览当前状态为 **repository-only / not deployed**——本仓库仅用于本地 QA 与字段校验，并不部署到 GitHub Pages。本轮（v4.6）不修改 live Leonardo 展览，不修改任何 tag / GitHub Release。

## 第一步：理解状态

在打开任何图像之前，先看页面顶部与底部的 `repository-status` 区块。本展览所有 6 件资产都标记为 `imported-not-deployed`：

- 文件存在于 `second-exhibition/assets/images/`；
- 不在 `site/` 顶层、不在任何 live URL；
- 元数据完整但 **不构成对最终读者的可见承诺**。

## 第二步：先读策展短文（约 60 秒）

打开 `second-exhibition/docs/CURATORIAL_ESSAY_ZH.md` 的「一句话总结」与「四个分节的关键命题」。策展短文不替代实物观察，只提供坐标系。

## 第三步：按节浏览

按页面顶部的 4 节地图（观察 / 分类 / 复制 / 再组织）逐节阅读。每节先读 kicker 与 takeaway，再打开至少 1 件 artifact card。card 上同时显示 source note 与 credit line，请把这两者当作字段证据，而不只是说明文字。

## 第四步：把 6 件资产放回资产使用图谱

打开 `second-exhibition/docs/BUILD_ASSET_USAGE.md`。它把 6 件资产的 page role、display size、lightbox 状态与 caveat 列成一张表。请用这张表回答：哪些资产在本展览中承担"分类秩序的对照点"角色，哪些资产承担"复制技术的证据点"角色？

## 第五步（可选）：进入深度阅读

打开 `second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md`。它把策展假设、可验证事实、推断、后续研究方向分开标注。如果你想做下一轮研究，这是入口。

---

## 给第一次访问者的提示

- **不要把本展览当作最终版本。** 6 件资产都是 v4.5 阶段导入的，尚未在 v4.7 repository QA 中经过完整逐页复核。
- **C-06 是低分辨率缩略图。** 这是 NMNH Botany 当前 `/media/?i=…` 端点直接返回的尺寸（90×90）。在本展览中它被用作"机构元数据与命名秩序的对照点"，而非视觉证据。**不要试图在 lightbox 中放大它。**
- **C-03 仅属于 Public-domain 子集。** BHL 同 item 的 CC BY-NC-SA 子集仍被 blocked-from-import。
- **C-10 的 IIIF Presentation API manifest 在 v4.5 阶段返回 404。** 本展览不基于 manifest 撰写任何陈述。
- **重复验证原则。** 本展览在每一次外部引用前都必须重新打开 6 件资产的官方 source URL 与 rights URL 重新核对。本轮 (v4.6) 已经做过一次核对；下一次 v4.7 / future round 必须再做一次。

---

## 状态与版本

- `version`: `second-exhibition-v0.1`
- `status`: `repository-only-not-deployed`
- `marker`: `second-exhibition-v0.1`
- 部署状态：`not deployed`
- 资产状态：`imported-not-deployed`（6 件）
- 资产门：`python3 scripts/second_exhibition_asset_gate.py` → PASS
- 构建门：`python3 scripts/second_exhibition_build_gate.py` → PASS

## 离线阅读建议

如果你的网络不可访问：本导览 + 4 个数据 JSON + 4 篇内容文档已经足以在没有浏览器的情况下理解本展览的结构。详见 `second-exhibition/data/` 与 `second-exhibition/docs/`。