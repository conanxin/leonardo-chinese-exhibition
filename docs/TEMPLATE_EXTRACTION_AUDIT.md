# Template Extraction Audit / 模板提取审计

> 本文件记录 v3.0 Real Template Extraction Audit 的真实提取过程与判断依据。
> 来源 tag：`v2.9-real-source-rights-audit` @ `a1e667e302d0d8106a9d0e4961159ae5c14aae4a`
> 状态：本 round 完成（v3.0-real-template-extraction-audit）
> 后续 freeze：`v3.0-real-stable-freeze`（独立 round 单独处理）

## 1. Verified source baseline

| 项 | 值 |
|---|---|
| 起点 tag | `v2.9-real-source-rights-audit` |
| 起点 tag object | `13814d345bcd47860b778323c9915460ef72fb28` |
| 起点 tag target | `a1e667e302d0d8106a9d0e4961159ae5c14aae4a` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Verified live byte size | 92,976 B |
| v2.9 marker | 1（live 上） |
| v2.8 marker | 1（live 上） |
| phantom v2.9 marker | 0（live 上） |
| placeholder | 0 |
| source-note | 14 |
| credit-line | 13 |
| figcaption | 24 |
| script.js HTTP | 200 |
| audit 资产总数 | 20 |

## 2. live 结构盘点（v2.9 已封版状态）

live 站点 `site/` 由三个文件驱动：

| 文件 | 大小 | 状态 |
|---|---|---|
| `site/index.html` | （v2.9 freeze 后未改） | source of truth for live |
| `site/style.css` | 42,079 B | 未触碰 |
| `site/script.js` | 14,594 B | 未触碰 |

live 站点同时还引用 `assets/` 下的 6 张馆藏图、5 张平台截图、7 张自制 SVG、2 张 metadata 资产。

live 站点本身**不进入模板**。模板只提取它的**结构**与**文档流**。

## 3. 分类清单

### 3.1 Reusable（直接可复用）

这些结构从 live 站点提取，**不需要任何 Leonardo 专属内容**就可以独立工作：

| 组件 | live 来源 | 模板对应文件 | 复用度 |
|---|---|---|---|
| Hero 区 | `site/index.html` 的 hero block | `site/index.template.html` 中 `.hero` | 高 |
| 3 分钟导览 | `site/index.html` 的 quick-guide block | `site/index.template.html` 中 `.quick-guide` | 高 |
| Exhibition map | `site/index.html` 的 exhibition-map block | `site/index.template.html` 中 `.exhibition-map` | 高 |
| Section body | `site/index.html` 的 section-card | `site/index.template.html` 中 `.section-card` | 高 |
| Artifact card | `site/index.html` 的 artifact-card | `site/index.template.html` 中 `.artifact-card` | 高 |
| Glossary | `site/index.html` 的 glossary block | `site/index.template.html` 中 `.glossary` | 高 |
| Source note / credit line 标签 | `site/index.html` 内嵌的 `.source-note` / `.credit-line` | `site/index.template.html` 中同类标签 | 高 |
| Rights footer | `site/index.html` 的 site-footer block | `site/index.template.html` 中 `.site-footer` | 高 |
| Deep blocks（4 个 module） | `site/index.html` 的 deep-reading-block / material-evidence-block / visual-thinking-block / research-model-block | `site/index.template.html` 中 `.deep-block` 系列 | 高 |
| release workflow | live 已有的 `docs/RELEASE_NOTES_v*.md` 流 | `release-notes.example.md` + `stable-freeze-report.example.md` | 高 |

### 3.2 Project-specific only（仅 Leonardo 项目）

这些**只属于 Leonardo 项目**，模板默认**不包含**：

- ✗ Leonardo 主标题 / 副标题 / 描述
- ✗ Royal Collection Trust 图像引用
- ✗ Codex Atlanticus 图像引用
- ✗ Leonardo//thek@ 平台描述
- ✗ 当前的 source-note / credit-line / figcaption 精确计数（14 / 13 / 24）
- ✗ 当前 live byte size（92,976 B）
- ✗ `case-study/release-assets/` 下的截图
- ✗ `posts/` 内容
- ✗ `docs/CURATORIAL_ESSAY_ZH.md` / `docs/VISITOR_GUIDE_ZH.md` 等 v2.9 项目专属文档

模板默认示例主题是 **"示例展览：一件作品的旅程"**，通用策展方法占位，与 Leonardo 无关。

### 3.3 Needs refactor（需要先改才能复用）

这些结构在 live 中存在，但**与具体 section id / 具体内容绑定**过紧，直接抽出需要先抽象：

| 组件 | live 现状 | 模板抽象方式 |
|---|---|---|
| runtime section-nav binding | live script.js 直接 `querySelector` 特定 section id | 模板只暴露 `initSectionNav()` + `IntersectionObserver` 通用模式 |
| guided mode 步骤列表 | live script.js 内置了 5 个步骤，对应 5 个真实 section | 模板只暴露 `showGuidedStep(index)` + `data-target-id` 数据驱动模式 |
| lightbox data-credit pattern | live script.js 通过 `data-credit` 属性获取 credit line | 模板只暴露 `openLightbox(src, alt, caption, credit)` 调用接口 |
| source manifest 命名约定 | live 用 `docs/SOURCE_AUDIT_MANIFEST.md` + `docs/RIGHTS_AND_SOURCES.md` | 模板用 `source-manifest.example.md` + `rights-and-sources.example.md` 拆分更细 |

### 3.4 Phantom / not used（phantom v3.x 历史）

不在本审计范围：

- 早期 phantom `v3.0-source-rights-audit` / `v3.1-template-audit` / `v3.2-second-exhibition-pilot` 等声称已完成的状态
- phantom `_template/` / `_pilots/` 子目录
- phantom Issue #16 已创建并关闭等历史

v3.0-real-template-extraction-audit 是**从 verified v2.9 重新创建** `_template/`，**不接受任何 phantom 历史**。

## 4. 提取风险

| 风险 | 影响 | 缓解 |
|---|---|---|
| 把 Leonardo 专属词混入模板默认内容 | 误导其他项目 | grep + 报告检查 |
| 把 live 站点代码片段直接复制进 `_template/site/` | live 与模板物理隔离失败 | 模板站点文件**重新撰写**，不复制 live |
| 模板 `_template/site/` 被 GitHub Pages 误部署 | live 出错 | live 部署源是根目录，模板目录不会被 GitHub Pages 拣选 |
| 模板 JSON 示例数据用了真实机构数据 | 权利边界不清 | 示例数据用通用主题 + 自制 SVG |
| 文档用 v2.9 的真实资产数字作为模板默认 | 误导 | 模板文档用 `{{PLACEHOLDER}}`，仅在来源案例段落提及 v2.9 |

## 5. v3.0 本 round 真实创建的 `_template/` 文件

```
_template/
├── README.md                           (6,736 B)
├── TEMPLATE_MANIFEST.md                (4,556 B)
├── content.schema.json                 (7,215 B, JSON valid)
├── source-manifest.example.md          (2,605 B)
├── rights-and-sources.example.md       (2,399 B)
├── visitor-guide.example.md            (1,506 B)
├── curatorial-essay.example.md         (2,033 B)
├── deep-research-notes.example.md      (1,356 B)
├── release-notes.example.md            (2,062 B)
├── stable-freeze-report.example.md     (2,884 B)
├── data/
│   ├── exhibition.example.json         (480 B, JSON valid)
│   ├── sections.example.json           (3,043 B, JSON valid)
│   ├── glossary.example.json           (1,441 B, JSON valid)
│   └── assets.example.json             (2,957 B, JSON valid)
└── site/
    ├── index.template.html             (9,365 B)
    ├── style.template.css              (8,967 B)
    └── script.template.js              (6,711 B, JS lint ok)
```

共 **18 个文件**（不含 `data/` 与 `site/` 子目录）。

## 6. 不做 pilot 的原因

v3.0 明确**不创建** `_pilots/`，原因：

1. 模板骨架刚提取出，还没经历过完整 freeze；先用独立 freeze round 验证骨架本身可用
2. pilot 必须基于已稳定的模板，否则会污染模板假设
3. pilot 应在 `v3.0-real-stable-freeze` 之后的 `v3.1 Second Exhibition Pilot` 单独 round 创建

## 7. 下一步

- **v3.0-real-stable-freeze**：基于本 round 创建的 `_template/` 做独立 freeze round，创建 `v3.0-real-template-extraction-audit` tag + GitHub Release
- **v3.1 Second Exhibition Pilot**：基于已冻结的模板建一个 pilot（在 `_pilots/` 下），不部署到 GitHub Pages
- **v3.2 Template Documentation**：补完整使用手册（usage / authoring / rights checklist / pilot workflow / release workflow）
- **v3.3+ Optional Real Second Exhibition**：只有 pilot 验证模板真正可复用后，才做第二个真实展览

任何 phantom v3.x 计划**都不被本审计接受为基线**。

---

> 本文件由 v3.0-real-template-extraction-audit 真实创建。