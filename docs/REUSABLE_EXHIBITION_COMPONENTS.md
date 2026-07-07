# Reusable Exhibition Components / 可复用展览组件

> 本文件记录从 `v2.9-real-source-rights-audit` 提取的可复用组件及其复用途径。
> 详细提取过程见 `docs/TEMPLATE_EXTRACTION_AUDIT.md`。
> 模板默认示例主题：示例展览：一件作品的旅程（通用占位）。

## 组件分级

| 等级 | 含义 | 复用方式 |
|---|---|---|
| **R1 — Ready to reuse** | 几乎不需要修改就能用 | 直接复制模板文件并填占位符 |
| **R2 — Reuse with edits** | 需要小改才能用于新项目 | 复制后改 section id / 名称 / 数据 |
| **R3 — Project-specific only** | 仅 Leonardo 项目能用 | 不进模板；只作为参考 |
| **R4 — Needs refactor** | 结构可复用但 live 中绑定过紧 | 抽离接口 / 用 data-attr 抽象 |

## R1 — Ready to reuse

| 组件 | live 来源 | 模板文件 | 备注 |
|---|---|---|---|
| Hero 区骨架 | `site/index.html` `.hero` | `_template/site/index.template.html` | class 通用，无项目专属 id |
| 3 分钟导览 | `site/index.html` `.quick-guide` | 同上 | `ol` 列表，5 点以内 |
| Exhibition map | `site/index.html` `.exhibition-map` | 同上 | `ul` + 锚链，4 个 section 起 |
| Section card | `site/index.html` `.section-card` | 同上 | kicker / title / body / takeaway / viewer-action |
| Artifact card | `site/index.html` `.artifact-card` | 同上 | image / alt / caption / source-note / credit-line |
| Glossary block | `site/index.html` `.glossary` | 同上 | `dl` 6 个术语 |
| Source / rights footer | `site/index.html` `.site-footer` | 同上 | rights-note + sources-details |
| CSS reset + 容器 + 卡片基础 | `site/style.css` | `_template/site/style.template.css` | 无外部依赖 |
| Lightbox API | `site/script.js` lightbox 部分 | `_template/site/script.template.js` `openLightbox()` | 不绑定具体选择器 |
| Guided mode API | `site/script.js` guided-mode 部分 | `_template/site/script.template.js` `showGuidedStep()` | 通过 `data-target-id` 抽象 |
| Section-nav 注册模式 | `site/script.js` initSectionNav | 同上 | 仅 `IntersectionObserver` 通用模式 |
| Accessibility helper（focus trap + reduced motion） | `site/script.js` | 同上 | 可直接调用 |
| JSON schema | 无（live 无 schema） | `_template/content.schema.json` | 轻量，2020-12 draft |
| Example data | 无（live 内联在 HTML） | `_template/data/*.example.json` | 通用占位主题 |
| Source manifest 模板 | `docs/SOURCE_AUDIT_MANIFEST.md` | `_template/source-manifest.example.md` | 占位符 + 表格 |
| Rights note 模板 | `docs/RIGHTS_AND_SOURCES.md` | `_template/rights-and-sources.example.md` | 检查模板，非法律意见 |
| Visitor guide 模板 | `docs/VISITOR_GUIDE_ZH.md` | `_template/visitor-guide.example.md` | 3–5 句导览 |
| Curatorial essay 模板 | `docs/CURATORIAL_ESSAY_ZH.md` | `_template/curatorial-essay.example.md` | 策展人视角 |
| Deep research notes 模板 | `docs/DEEP_RESEARCH_NOTES_ZH.md` | `_template/deep-research-notes.example.md` | 每 section 一节 |
| Release notes 模板 | `docs/RELEASE_NOTES_v2.9_REAL_SOURCE_RIGHTS_AUDIT.md` | `_template/release-notes.example.md` | 占位符 + 验证 checklist |
| Stable freeze report 模板 | `reports/leonardo_chinese_exhibition_v2.9_real_stable_freeze_report.md` | `_template/stable-freeze-report.example.md` | commit / tag / live byte |

## R2 — Reuse with edits

| 组件 | live 来源 | 模板文件 | 需要改什么 |
|---|---|---|---|
| Deep block 4 个 module | `site/index.html` 的 4 个 `.deep-block` | `_template/site/index.template.html` 同结构 | 真实项目应填入具体研究内容；模板默认 `hidden` |
| Quick guide 文案 | `site/index.html` 的 `<ol>` | 同上 | 5 个 bullet 的具体内容 |
| Hero 文案 | `site/index.html` 的 hero | 同上 | 一句话展览问题 + 入口按钮 |
| Source / rights footer 文案 | `site/index.html` 的 footer | 同上 | 权利边界具体声明 |

## R3 — Project-specific only（**不**进模板）

| 组件 | live 来源 | 说明 |
|---|---|---|
| 展览主标题 / 副标题 | `site/index.html` `<title>` | Leonardo 项目专属 |
| Royal Collection Trust 图像引用 | `assets/collections/*` | 仅 Royal Collection |
| Codex Atlanticus 图像引用 | `assets/collections/*` | 仅 Codex Atlanticus |
| Leonardo//thek@ 平台描述 | `site/index.html` 文本 | 仅该项目 |
| source-note / credit-line 精确计数 | live grep | 随项目变化 |
| live byte size | live `wc -c` | 随项目变化 |
| `case-study/release-assets/` 截图 | 仅 Leonardo 部署案例 | 不通用 |
| `posts/` 内容 | 仅该项目博客 | 不通用 |
| v2.9 真实资产审计数字 | `docs/SOURCE_AUDIT_MANIFEST.md` | 随项目变化 |

模板默认**不预设任何 R3 数字或名字**。R3 仅在 `_template/README.md` 与 `docs/TEMPLATE_EXTRACTION_AUDIT.md` 中作为"来源案例"被提及。

## R4 — Needs refactor

| 组件 | live 现状 | 模板抽象方式 | 为什么需要抽象 |
|---|---|---|---|
| runtime section-nav binding | live script.js 直接选择特定 section id | 模板只暴露 `IntersectionObserver` 通用注册模式 + `data-section-id` 数据驱动 | live 版本写死 5 个 id，模板要适配任意数量 |
| guided mode 步骤列表 | live script.js 内置 5 个真实 section 步骤 | 模板用 `<li data-target-id="...">` 数据驱动 | live 步骤与 section 一一对应，无法跨项目复用 |
| lightbox data-credit pattern | live script.js 通过 `data-credit` attribute 取 credit | 模板 API 直接接受 caption / credit 参数 | live 用 attribute，模板函数签名更清晰 |
| source manifest 命名约定 | live 用 `SOURCE_AUDIT_MANIFEST.md` + `RIGHTS_AND_SOURCES.md` | 模板用 `source-manifest.example.md` + `rights-and-sources.example.md` 拆分更细 | 模板要通用，文件名不带项目标识 |

---

## 用法

1. 找要复用的组件，确认等级
2. R1 直接复制；R2 复制后改；R3 跳过；R4 按抽象方式接入
3. 模板示例数据从 `_template/data/*.example.json` 出发，替换占位
4. 任何接入 live 的修改都要先经过 source rights audit

## 验证

每个 R1 / R2 组件在 `_template/` 中都已真实存在。grep + JSON 校验已通过。

详细验证记录在 `reports/leonardo_chinese_exhibition_v3_0_real_template_extraction_audit_report.md`。

---

> 本文件由 v3.0-real-template-extraction-audit 真实创建。