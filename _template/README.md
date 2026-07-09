# 中文数字展览模板 / Chinese Digital Exhibition Template

> **状态**：v3.0-real-template-extraction-audit 创建的初始骨架
> **来源 tag**：`v2.9-real-source-rights-audit`
> **基线 live**：https://conanxin.github.io/leonardo-chinese-exhibition/ (92,976 B, 已封版)
> **重要**：本目录是模板，不是 live 站点。live 站点在 `site/`，本目录在 `_template/`。

这是一套从真实 `v2.9` 达·芬奇展览项目中**提取并抽象**的可复用中文数字展览模板骨架。它不是复制 live 站点，而是把 live 中验证过的展览结构、组件、文档流抽出来，让别的项目可以基于此模板快速启动自己的中文数字展览。

模板默认内容**不包含**任何 Leonardo 项目专属词：
- ✗ 不默认引用 Leonardo / Codex Atlanticus / Royal Collection Trust
- ✗ 不默认引用 Leonardo//thek@ 平台
- ✗ 不默认使用任何真实馆藏图片
- ✗ 不默认使用 live 站的固定标题、副标题、版本号
- ✓ 所有示例数据都是通用占位（"示例展览：一件作品的旅程"）

文档里可以把 Leonardo 项目作为"**来源案例**"提及（说明本模板从哪里提取），但模板示例数据和模板默认骨架必须保持通用。

---

## 适用场景

适合用本模板的项目：

- 艺术家专题展
- 古籍 / 手稿 / 档案专题展
- 建筑史 / 园林史展
- 科学史 / 技术史展
- 个人研究型数字展览
- 小型数字人文项目
- 教学用的策展原型

## 不适用场景

- 大型 CMS / 多用户后台系统
- 复杂数据库驱动的目录检索
- 未完成版权核验的大规模图片站
- 需要后端 + 登录 + 支付的交互展
- 视频流媒体主导的展览

本模板定位是**轻量静态 HTML + JSON + 文档流**，目的是做严肃但小型、可被单人维护、可长期封版的中文展览。

---

## 推荐使用流程（8 步）

1. **复制 `_template/`** 到独立项目目录
2. **确定展览主题**（一句话说清观众会看到什么）
3. **填写 `data/exhibition.json`**（标题、副标题、版本、liveUrl）
4. **填写 `data/sections.json`**（推荐 4 个 section 起，含 kicker / title / body / takeaway）
5. **填写 `data/glossary.json`**（推荐 6 个术语起，每个 50–100 字）
6. **准备图像**（自制 SVG / 已授权图片 / 平台截图）
7. **写 5 个文档**：source-manifest / rights-and-sources / visitor-guide / curatorial-essay / deep-research-notes
8. **做 stable freeze**：写 release-notes / stable-freeze-report → 部署 → 验证 → tag → Release

## 目录结构

```
_template/
├── README.md                           ← 本文件
├── TEMPLATE_MANIFEST.md                ← 每个模板文件的用途说明
├── content.schema.json                 ← exhibition / sections / artifacts / glossary / sources 的轻量 JSON schema
├── source-manifest.example.md          ← 来源清单模板
├── rights-and-sources.example.md       ← 权利说明模板
├── visitor-guide.example.md            ← 观众导览文案模板
├── curatorial-essay.example.md         ← 策展短文模板
├── deep-research-notes.example.md      ← 深度研究笔记模板
├── release-notes.example.md            ← 版本发布说明模板
├── stable-freeze-report.example.md     ← 封版报告模板
├── data/
│   ├── exhibition.example.json         ← 展览元数据示例
│   ├── sections.example.json           ← 展区列表示例
│   ├── glossary.example.json           ← 术语表示例
│   └── assets.example.json             ← 图像资源示例
└── site/
    ├── index.template.html             ← 站点骨架（hero / quick guide / map / section / artifact / glossary / footer）
    ├── style.template.css              ← 站点骨架样式（无外部依赖）
    └── script.template.js              ← 站点骨架脚本（仅 placeholder，不绑定具体 section id）
```

正式项目使用时应把 `data/` 内容直接放进自己项目根目录或 `site/data/`；`site/*.template.*` 复制后改名为去掉 `.template` 后缀。

---

## 最小可行展览（MVE）

一个最小可行的中文数字展览必须包含：

| 组件 | 数量 | 备注 |
|---|---|---|
| Hero 区 | 1 | 标题 + 一句展览问题 + 入口按钮 |
| 3 分钟导览 | 1 | 5 点以内，每点一句 |
| Exhibition map | 1 | 4 个 section 标题 + 锚链 |
| Section 卡 | 4 | 每个含 kicker / title / body / takeaway / viewer-action |
| Artifact 卡 | 4 | 每张含 title / image / alt / caption / source-note / credit-line |
| Glossary 术语 | 6 | 每个 50–100 字 |
| Source manifest | 1 | 每张图片 / 截图 / 自制图都登记 |
| Rights note | 1 | 写在 README 或 footer，明确权利边界 |
| Release notes | 1 | 每个 freeze 版本一份 |
| Stable freeze report | 1 | 记录 commit / tag / live byte / 验证项 |

少于上述任何一项，都不构成"可封版"的展览。

---

## 来源案例 / Source case

本模板的具体结构、组件、文档流是从以下真实项目提取：

- **v2.9-real-source-rights-audit**（leonardo-chinese-exhibition）：达·芬奇纸上作品中文数字展览
- 来源 tag SHA：`13814d345bcd47860b778323c9915460ef72fb28`（annotated）
- tag target commit：`a1e667e302d0d8106a9d0e4961159ae5c14aae4a`
- live byte size：92,976 B
- audit 资产：20 项（collection 6 + 平台截图 5 + SVG 7 + metadata 2）
- source-note 数：14
- credit-line 数：13
- figcaption 数：24

详细 extraction 记录在 `docs/TEMPLATE_EXTRACTION_AUDIT.md`，可复用组件对照表在 `docs/REUSABLE_EXHIBITION_COMPONENTS.md`。

---

## 后续 pilot / 真实展览

v3.0 只创建骨架，不创建 pilot：

- v3.0-real-stable-freeze：封版 v3.0 模板骨架（独立 tag）
- v3.1 Second Exhibition Pilot：基于模板建一个 pilot（在 `_pilots/` 下）
- v3.2 Template Documentation：补完整使用手册（usage / authoring / rights checklist / pilot workflow / release workflow）
- v3.3+ Optional Real Second Exhibition：只有 pilot 验证模板真正可复用后，才做第二个真实展览

任何 v3.x 之前的 phantom v3.x 计划都不被本模板接受为基线。

---

## 使用文档

v3.2 新增五份中文手册，分别覆盖模板使用、内容写作、来源与权利核验、pilot 工作流、发布与封版：

- [USAGE_GUIDE_ZH.md](./USAGE_GUIDE_ZH.md) — 中文数字展览模板使用手册：从模板开始的 8 步、最小可行展览、目录结构、常见错误
- [CONTENT_AUTHORING_GUIDE_ZH.md](./CONTENT_AUTHORING_GUIDE_ZH.md) — 内容写作指南：标题 / Hero / 3 分钟导览 / section / artifact card / deep block / glossary 的写作原则
- [SOURCE_RIGHTS_CHECKLIST_ZH.md](./SOURCE_RIGHTS_CHECKLIST_ZH.md) — 来源与权利检查清单：图片 / 平台截图 / 自制图解 / 发布前核验
- [PILOT_WORKFLOW_ZH.md](./PILOT_WORKFLOW_ZH.md) — Pilot 工作流：为什么先做 pilot、pilot 应包含什么、不应做什么、如何从 pilot 到正式展览
- [RELEASE_WORKFLOW_ZH.md](./RELEASE_WORKFLOW_ZH.md) — 发布与封版工作流：版本阶段、必须记录项、禁止事项、stable freeze checklist、Reality recovery rule

---

## 重要约束（使用本模板时也适用）

- 不要修改 live 站点 `site/` 来"顺手"补模板
- 不要 `git add .`（要显式 add）
- 不要移动上游已封版的 tag
- 不要在未做 source rights 审计前上线
- 不要部署 template 到 GitHub Pages 作为展览

---

> 本 README 是 v3.0-real-template-extraction-audit 真实创建的（commit 待 v3.0 落地后回填）。