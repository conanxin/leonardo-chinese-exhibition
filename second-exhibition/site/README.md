# 第二展览 · Site

> 本目录是《植物图谱与视觉分类》展览的网站源码。**当前发布状态：`production-deployed-v5.3`**，通过 v5.3 改造后的 GitHub Pages workflow 部署到 `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`。

## 本地运行（serving contract）

页面通过 `../assets/images/` 引用本地图片。**必须从 `second-exhibition/` 根目录启动 `http.server`，不要从 `second-exhibition/site/` 启动**——后者会让 `../assets/...` 解析错误。

```bash
# 从 repo root 运行：
python3 -m http.server 8770 --directory second-exhibition

# 然后访问：
# http://127.0.0.1:8770/site/
```

不要通过复制图片到 `site/` 来"修复"路径问题。`second-exhibition/site/` 仅承载 HTML / CSS / JS；图片始终来自 `second-exhibition/assets/images/`。

## 文件清单

- `index.html` — 入口页（marker `second-exhibition-v0.1`，当前发布状态 `production-deployed-v5.3`，6 件资产的当前发布状态 `published-in-v5.3`，历史导入记录 `imported-not-deployed` 保留在 `second-exhibition/assets/asset-import-manifest.json`）。
- `style.css` — 排版与组件样式。无外部资源、无第三方 CSS、无需联网。
- `script.js` — lightbox、ESC 关闭、导览模式切换。无第三方 JS、无网络请求、无自动播放。
- `README.md` — 本文件。

## 交互

- 顶部 section nav：4 节 + 术语 + 深度阅读。
- 顶部"开启导览模式"按钮：切换 guided-banner 的显示状态；按钮 `aria-pressed` 同步。
- artifact card 图片：点击 / Enter / Space 在 lightbox 中查看。
- lightbox：按 `Esc` 或点击遮罩或点击"关闭"按钮退出。
- C-06 的 lightbox 已被禁用（`data-lightbox-enabled="false"`）。

## 状态与版本

- `version`: `second-exhibition-v0.1`
- `status`: `production-deployed-v5.3`
- `publication_status`: `production-deployed-v5.3`（当前）
- `historical_import_status`: `imported-not-deployed`（v4.5 阶段，保留在 `second-exhibition/assets/asset-import-manifest.json`）
- 资产门：`python3 scripts/second_exhibition_asset_gate.py` → PASS（v4.5 阶段记录）
- 构建门：`python3 scripts/second_exhibition_build_gate.py` → PASS（v5.3b 已要求 exhibition 当前发布状态为 `production-deployed-v5.3`）
- 部署门：`python3 scripts/second_exhibition_staging_gate.py` → PASS（v5.3b 已要求 staged 页面包含 `production-deployed-v5.3`）

## 已知 caveat

- **C-06** 是 90×90 低分辨率缩略图，本页面不将其作为大幅展示；不放大；不启用 lightbox。
- **C-10** 的 Rijksmuseum IIIF Presentation API manifest `/manifest.json` 在 v4.5 阶段返回 HTTP 404；本页面不基于 manifest 撰写任何陈述。
- **C-03** 仅属于 Public-domain 子集；BHL 同 item 的 CC BY-NC-SA 子集仍被 blocked-from-import。

## 不允许

- 把本目录文件复制到顶层 `site/` 下作为部署路径。
- 在本目录中创建任何与 GitHub Pages workflow 相关的配置（`_config.yml`、`Gemfile`、`vercel.json` 等）。
- 引入第三方 JS / CSS 框架。
- 把本展览描述为 `approved` / `safe for commercial use` / `cleared for all uses` / `watermark-free originals` 中的任何一种。
- 抹去 `imported-not-deployed`（v4.5 历史导入记录）或 `import_status` 字段：这些字段是 v4.5 阶段的可审计证据，本展览作为公开发布不等于改写历史导入记录。
- 把 staging builder / staging gate 跳过，直接把 `second-exhibition/` 上传到 Pages；v5.3 改造后的 workflow 严格要求两步 gate 通过后才允许 upload-pages-artifact。