# Pilot Manifest

## 标识

| 项 | 值 |
|---|---|
| Pilot 名称 | 一件作品的旅程 |
| Pilot 副标题 | 从图像、来源、路径到知识网络 |
| Pilot 版本 | pilot-v0.1 |
| 项目 | leonardo-chinese-exhibition v3.1 |
| 源模板 | `_template/`（`v3.0-real-template-extraction-audit` @ `dd7d589`） |
| 部署 | **不部署** |
| Live 影响 | **无** |

## 文件清单（共 16 个文件）

### 入口（3）

- `README.md` — pilot 入口
- `PILOT_MANIFEST.md` — 本文件
- `PILOT_NOTES.md` — pilot 验证笔记 + 模板可复用性观察

### 数据（4）

- `data/exhibition.json` — 展览元数据（title / subtitle / description / version / liveUrl / status）
- `data/sections.json` — 4 个 section（起点 / 流转 / 阅读 / 展示）
- `data/glossary.json` — 6 个术语（单件作品研究 / 流转链 / 源出处 / 权利边界 / 自制示意图 / pilot）
- `data/assets.json` — 4 张 artifact + 1 个 favicon

### 站点（3）

- `site/index.html` — pilot 站点骨架
- `site/style.css` — pilot 样式
- `site/script.js` — pilot 脚本（section nav / lightbox / guided-mode / a11y / pilot-v0.1 marker console）

### 文档（5）

- `docs/SOURCE_AUDIT_MANIFEST.md`
- `docs/RIGHTS_AND_SOURCES.md`
- `docs/CURATORIAL_ESSAY_ZH.md`
- `docs/DEEP_RESEARCH_NOTES_ZH.md`
- `docs/RELEASE_NOTES_PILOT.md`

### 资产（1 dir, 3 svg）

- `assets/diagrams/object-journey.svg`
- `assets/diagrams/evidence-chain.svg`
- `assets/diagrams/viewing-map.svg`

## 验证清单（pilot 内部）

| 项 | 实测 |
|---|---|
| JSON validation 4/4 | ✓ |
| Section count | 4（起点 / 流转 / 阅读 / 展示） |
| Artifact card count | 4（pilot-object-journey / pilot-evidence-chain / pilot-viewing-map / pilot-curator-model） |
| Glossary item count | 6 |
| Deep-reading block | ✓（section-01） |
| Material-evidence block | ✓（section-01） |
| Visual-thinking block | ✓（section-01） |
| Research-model block | ✓（section-01） |
| Forbidden terms（Leonardo / Codex Atlanticus / Royal Collection Trust / `thek@`）| **0** ✓ |
| pilot-v0.1 marker | ✓（hero / footer / script.js console） |
| Footer marker | ✓（`pilot-footer-marker`） |
| sourceNote + creditLine 双字段 | ✓（每个 artifact 都有） |
| Live site unchanged | ✓（92,976 B） |
| _template/ unchanged | ✓（17 文件） |

## 不在 pilot 范围

- 真实馆藏图 / 机构截图
- 双语 / i18n
- 服务端 / 数据库
- SEO / meta-tag 优化
- Tag / GitHub Release
