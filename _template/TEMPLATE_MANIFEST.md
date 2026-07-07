# Template Manifest / 模板清单

每个文件的具体用途与注意事项。

## 文档

| 文件 | 用途 | 是否模板默认 | 备注 |
|---|---|---|---|
| `README.md` | 模板总入口 | ✓ | 适用 / 不适用 / 8 步 / 目录 / MVE / 来源案例 |
| `TEMPLATE_MANIFEST.md` | 本文件 | ✓ | 每个文件的用途清单 |

## 内容 / 数据

| 文件 | 用途 | 是否模板默认 | 备注 |
|---|---|---|---|
| `content.schema.json` | exhibition / sections / artifacts / glossary / sources 的轻量 JSON schema | ✓ | 用于人工校对，不强制运行；正式项目可加 ajv 等校验 |
| `data/exhibition.example.json` | 展览元数据示例（标题 / 副标题 / 描述 / 版本 / liveUrl） | ✓（通用占位） | 不含 Leonardo 专属内容 |
| `data/sections.example.json` | 展区列表示例（推荐 4 个 section） | ✓（通用占位） | 占位主题："示例展览：一件作品的旅程" |
| `data/glossary.example.json` | 术语表示例（推荐 6 个） | ✓（通用占位） | 术语均为通用词，与项目无关 |
| `data/assets.example.json` | 图像资源示例 | ✓（通用占位） | 仅引用 `project-generated` 占位 SVG |

## 站点骨架

| 文件 | 用途 | 是否模板默认 | 备注 |
|---|---|---|---|
| `site/index.template.html` | 最小 HTML 骨架：hero / quick-guide / map / section-card / artifact-card / deep-block / glossary / rights-footer | ✓ | 通用 class，无 live 站专属 id |
| `site/style.template.css` | 骨架样式：栅格 / 类型 / 卡片 / footer | ✓ | 无外部依赖，无 build step |
| `site/script.template.js` | 骨架脚本：section nav placeholder / lightbox placeholder / guided-mode placeholder / accessibility helper | ✓ | 仅占位函数，不绑定具体 section id，无 Leonardo 专属选择器 |

## 文档模板

| 文件 | 用途 | 是否模板默认 | 备注 |
|---|---|---|---|
| `source-manifest.example.md` | 来源清单模板：每张图 / 截图 / SVG 必填字段 | ✓ | 占位符 `{{TAG_NAME}}` / `{{LIVE_URL}}` / `{{BYTE_SIZE}}` |
| `rights-and-sources.example.md` | 权利说明模板：声明 reuse 边界 + follow-up | ✓ | 通用法律免责模板，**非法律意见** |
| `visitor-guide.example.md` | 观众导览文案模板：3–5 句导览 + 路径建议 | ✓ | 中文为主 |
| `curatorial-essay.example.md` | 策展短文模板：策展人视角 | ✓ | 中文为主 |
| `deep-research-notes.example.md` | 深度研究笔记模板：每个 section 背后的研究材料 | ✓ | 中文为主 |
| `release-notes.example.md` | 版本发布说明模板：每个 freeze 版本一份 | ✓ | 占位符 `{{TAG_NAME}}` / `{{LIVE_URL}}` / `{{BYTE_SIZE}}` / `{{AUDIT_COMMIT}}` |
| `stable-freeze-report.example.md` | 封版报告模板：commit / tag / live byte / 验证项 / no-touch | ✓ | 同上占位符 |

---

## 使用约定

- **示例文件** (`*.example.*`)：直接复制为正式文件的起点，**必须替换占位主题与占位资产**
- **模板骨架** (`site/*.template.*`)：复制后去掉 `.template` 后缀，再按项目数据填实
- **不要**把 `*.example.*` 直接拿去上线——它们是占位数据，不是真实展览
- **不要**把 `site/*.template.*` 的 `{{PLACEHOLDER}}` 留在 live 站点 HTML 里

## 与 live 站的关系

- live 站点 = `site/` (v2.9 verified, 92,976 B)
- 模板骨架 = `_template/site/`
- 二者**物理隔离**：`_template/site/` 不会被 `index.html` 引用，不会被 GitHub Pages 部署
- live 站对模板的引用：仅作为来源案例写在文档里，不作为部署依赖

---

## 占位符约定

模板文档中可能出现的占位符：

| 占位符 | 含义 | 替换时机 |
|---|---|---|
| `{{TAG_NAME}}` | 本次 freeze 的 tag 名 | stable freeze round |
| `{{TAG_OBJECT}}` | annotated tag object SHA | stable freeze round |
| `{{TAG_TARGET}}` | tag target commit SHA | stable freeze round |
| `{{LIVE_URL}}` | 部署后的 GitHub Pages URL | 部署后 |
| `{{BYTE_SIZE}}` | `curl -s URL \| wc -c` 实测字节 | 验证 round |
| `{{AUDIT_COMMIT}}` | source rights 审计的 commit SHA | audit round |
| `{{FREEZE_COMMIT}}` | 本次 freeze 提交 SHA | freeze round |
| `{{COLLECTION_COUNT}}` | 馆藏 / 手稿图片数 | audit round |
| `{{SCREENSHOT_COUNT}}` | 平台截图数 | audit round |
| `{{SVG_COUNT}}` | 自制 SVG 数 | audit round |
| `{{METADATA_COUNT}}` | metadata 资产数 | audit round |

---

> 本 manifest 是 v3.0-real-template-extraction-audit 真实创建的。所有文件状态以 git tree 为准。