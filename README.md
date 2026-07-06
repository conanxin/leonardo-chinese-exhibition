# 达·芬奇的纸上宇宙：被拆散的手稿与重新连接的思想

基于 Leonardo//thek@ 平台的中文数字展览项目。

## Live Demo
https://conanxin.github.io/leonardo-chinese-exhibition/

## 当前版本
v2.0 stable release · tag `v2.0-public-portfolio-case`（在 v1.5b / v1.5c / v1.6 / v1.7 / v1.8 / v1.9 + v2.0 public portfolio 之上冻结）

**Latest stable tag**: `v2.0-public-portfolio-case`

**Live URL**:

> https://conanxin.github.io/leonardo-chinese-exhibition/

## v2.0 stable release

本仓库的 v2.0 是稳定冻结版本。

- 展览本体 `site/` 在 v1.8 / v1.9 已成熟，v2.0 不再修改
- 7 件作品化文档全部在 `case-study/` 下发布
- Git tag `v2.0-public-portfolio-case` 已创建，可通过 `git checkout v2.0-public-portfolio-case` 切到稳定快照

**Release notes**: [`docs/RELEASE_NOTES_v2.0.md`](docs/RELEASE_NOTES_v2.0.md)
**v2.0 freeze 报告**: `reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md`

## GitHub Release

**v2.0 已在 GitHub Releases 发布**：<https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.0-public-portfolio-case>

附带了 6 张 Playwright 真实截图 + 1 份 asset manifest，全部为已上传状态。

**Release body 文件**：[`docs/GITHUB_RELEASE_v2.0.md`](docs/GITHUB_RELEASE_v2.0.md)（可作为 GitHub Release 页面文案复用）

## v2.1 release publishing kit

v2.1 是「发布收口」版本：在不改动展览本体和 case-study/ 的前提下，把 v2.0 整理成可在 GitHub Release / X / 作品集 / 个人站点直接复用的发布材料。

| 资产 | 用途 |
|---|---|
| `release-assets/screenshots/desktop-hero.png` | 1440×900 hero 主图，可作 GitHub Release top 缩图 + README 顶图 |
| `release-assets/screenshots/desktop-exhibit-index.png` | 1440×900 展品索引页截图 |
| `release-assets/screenshots/desktop-real-image-gallery.png` | 1440×900 真实手稿图像展区 |
| `release-assets/screenshots/desktop-platform-tools.png` | 1440×900 平台工具页截图 |
| `release-assets/screenshots/mobile-hero.png` | 390×844 mobile hero |
| `release-assets/screenshots/mobile-section.png` | 390×844 mobile section 截图 |
| `release-assets/manifest.md` | 全部截图用途 + 复用建议（README / Release / X / 作品集） |

**截图规格**：

- 全部 6 张由 Playwright + Chrome-for-Testing 149 通过 `headless=true` 从 live URL 抓取
- 桌面 1440×900 / 移动 390×844，与 README 设计网格一致
- 全部锚定到 `#hash` (`/`, `/` `#exhibit-index`, `/` `#section2`, `/` `#section7`) 确保取到正确 section
- 重新生成方法：`/tmp/pwtool/capture6.py`（约 30 秒）

**完整发布报告**：`reports/leonardo_chinese_exhibition_v2_1_release_publishing_kit_report.md`

### 关键里程碑

- v1.5b（`d69f516`）· live hotfix · marker 上线
- v1.5c（`53c4032`）· repo hygiene
- v1.6（`75fd9f9`）· distribution pack
- v1.7（`af07b15`）· exhibit image upgrade
- v1.8（`4f6d126`）· real image integration
- v1.9（`97f1670`）· final polish
- **v2.0（`ae946b3`）· public portfolio case → tag `v2.0-public-portfolio-case`**
- **v2.1（`9e6233a`-based）· release publishing kit + GitHub Release + 6 截图**

## v2.0 作品化（public portfolio case）

v2.0 是一个收口版本：把整个 v1.5 → v1.9 的工作流整理成可直接复用到个人作品集、个人主页、求职简历的 7 件文档。

| 文档 | 用途 |
|---|---|
| `case-study/portfolio-case-study.md` | 中文长篇案例（14 节 · 含背景 / 问题 / 方法 / IA / 视觉 / 图像系统 / 技术 / 版本演进 / 复用经验 / 后续路线） |
| `case-study/project-onepager.md` | 一页式项目说明（项目类型 / 关键词 / 解决问题 / 产出 / 技术栈 / 链接 / 亮点 5 条） |
| `case-study/portfolio-case-en.md` | 英文版短案例（适合国际作品集） |
| `case-study/readme-showcase-section.md` | README 顶部展示段（可直接拷贝） |
| `case-study/launch-x-post.md` | X 14 条中文长帖（发布用） |
| `case-study/project-retrospective.md` | 项目复盘（做对了什么 / 踩的坑 / v1.7-1.8 解决路径 / 对未来的启发） |
| `case-study/README.md` | case-study 目录导览 |

完整 v2.0 报告：`reports/leonardo_chinese_exhibition_v2_0_public_portfolio_case_report.md`

## 推荐阅读路径

如果你只有 5 秒：`case-study/project-onepager.md`

如果你只有 30 秒：`case-study/portfolio-case-en.md`（英文）或`case-study/readme-showcase-section.md`（中文 top-level）

如果你有 5 分钟：`case-study/portfolio-case-study.md`

如果你想看项目内幕：`case-study/project-retrospective.md`

## case-study/ 目录说明

`case-study/` 目录下所有文件均为**作品集展示**类内容，独立于展览本体（site/）。每份文档都自含目标读者、用途、可以如何引用。**与 posts/ 不同**：posts/ 是给读者的传播材料，case-study/ 是给雇主 / 合作方 / 学术同行 的展示材料。

## v1.9 最终展览 polish 与资产审计（final exhibition polish & asset reference audit）

v1.9 是真实图像集成后的收口版本。本版本聚焦"小修小补"，不重写任何内容。

完成的核心工作：

- 资产引用审计：6 张 JPG + 7 张 SVG + 2 张 favicon/og-cover 全部确认已在页面正确路径使用（除一张 `platform-structure.svg` 为 v0.3 保留资产，未被引用）；
- 补齐 `<link rel="icon">` 与 `og:image` 元数据，让 `assets/favicon.svg` 与 `assets/og-cover.svg` 这两个之前未挂载的资源上线；
- 修复 4 个温莎索引卡片的 `credit-line` 格式（从 `公共域 · Wikimedia Commons` 升级为 `公共域 · Wikimedia Commons · Leonardo da Vinci, Royal Collection Trust`），与展区 3 画廊卡片一致；
- 全 19/19 `<img>` 标签都有 alt text（0 missing）；
- 全 10/10 真实图像有统一格式的 credit-line（公共域 + 来源 + 馆藏）；
- 9 张 SVG figure 全部有 figcaption + source-note；
- 移动端 image-grid 单列布局已就绪；
- v1.5b / v1.7 / v1.8 三层 marker 完整保留。

完整 v1.9 报告：`reports/leonardo_chinese_exhibition_v1_9_final_exhibition_polish_report.md`

## v1.8 真实手稿图像集成（real image integration）

v1.8 解决了 v1.7 仍然只用原创 SVG 图解、缺乏真实手稿像素的问题。本版本：

- 从 Wikimedia Commons 公共域下载 6 张真实手稿图像：4 张温莎皇家收藏（RCIN 912310 / 912660 / 919003 / 912363）+ 2 张《大西洋手稿》（f.719 / f.21）
- 展品索引 4 张卡片（马 / 水 / 肩臂 / 猫龙）升级为 image-card，直接展示 RCIN 真实手稿像素
- 展区 2 增 2 张 Codex Atlanticus 代表页
- 展区 3 画廊完全真实化（4 张温莎手稿）
- section-5 / 6 / 7 各加 1 张 `.image-placeholder-pro` 截图候选卡（v1.9 待补）
- 修正 v1.7 报告中 SVG 数字计数不一致
- 修正 v1.7 报告里 3 个不准确的 RCIN 编号（912695→912310，919023→919003，912377→912363）
- 临时占位文案（"实际使用时请替换为真实手稿影像"）已彻底删除

完整 v1.8 报告：`reports/leonardo_chinese_exhibition_v1_8_real_image_integration_report.md`
图像资产说明：`site/assets/images/README.md`

## v1.7 展览图像升级（exhibit image upgrade）

v1.7 解决了"页面底部原来写着图片使用占位"的问题。本版本：

- 增加 4 个全新原创 SVG（collection-split / watermark-evidence-chain / recomposition-triptych / platform-tool-wall）+ 1 个升级版（manuscript-journey，从 ~1 KB 升级到 4 KB 的 editorial 风格）+ 2 个继承自 v0.3 的（thinking-map / platform-structure）。平台内容承担在 v1.7 之后由 `platform-tool-wall` 接替，page 不再引用 `platform-structure`。
- 增加"本展展品索引"section，8 张展品卡（A-H），进入页面即有"展览感"
- 8 个展区都升级为展品模块：每节必有 `figure` / `gallery` / 展品柜
- 温莎绘图以"展品卡 + RCIN 编号 + 外链"形式陈列，不直接嵌入第三方像素
- 平台 9 功能以"原创工具墙 + HTML 9 宫格"双层呈现
- 配色更克制：暖白 + 黑灰 + 古金 + 深绿；不再用黑底金字的视觉惯式

完整 v1.7 提交报告：`reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md`

## v1.6 传播包（distribution pack）

基于已上线的中文数字展览，一套可用于公众号、小红书、X、短视频和作品集展示的传播材料。

| 文件 | 用途 |
|---|---|
| `posts/wechat-longform.md` | 公众号长文（带章节、副标题、CTA） |
| `posts/x-thread.md` | X 14 条 thread |
| `posts/xiaohongshu.md` | 小红书图文稿（10 个标题 + 7 张图文卡片 + 互动钩子） |
| `posts/video-script-3min.md` | 3 分钟短视频口播稿（hook / 中段 / 结尾 CTA + 剪辑建议） |
| `posts/portfolio-case.md` | 作品集案例说明（项目背景 / 问题 / 方法 / 产出 / 技术 / 设计 / 反思） |
| `posts/title-options.md` | 标题库（公众号 10 + 小红书 10 + X 10 + 作品集 6 = 36 条） |

完整 v1.6 提交报告：`reports/leonardo_chinese_exhibition_v1_6_distribution_pack_report.md`

## posts/ 目录说明

`posts/` 目录下所有文件均为**散文 / 脚本 / 标题 / 卡片文案**类传播内容，不是展览本体。`site/index.html` 与 `site/style.css` 仍是线上展览页面的唯一来源。

发布时不要把 `posts/` 推到 GitHub Pages 的根（它属于仓库文档层，不会被 GitHub Pages 工作流加载）。

## 项目结构

```
.
├── site/                   # GitHub Pages 部署根（仅这一层被部署）
│   ├── index.html          # 中文展览主页（v1.5b-live-hotfix + v1.7-exhibit-image-upgrade marker）
│   ├── style.css
│   └── assets/
│       ├── diagrams/       # 6 个原创 SVG 图解（v1.7 升级与新增）
│       └── favicon.svg · og-cover.svg
├── posts/                  # v1.6 传播材料（公众号 / X / 小红书 / 视频 / 作品集 / 标题）
├── research/               # 学术背景资料 + image-candidates.md（v1.7 候选清单）
├── reports/                # 版本报告（v0.2 → v1.5c → v1.6 → v1.7）
├── docs/                   # DEPLOYMENT / GITHUB_PAGES / CLOUDFLARE / RELEASE_NOTES
├── exhibition/             # 策展脚本与计划
├── README.md
└── .github/workflows/pages.yml
```

## 本地预览命令
```bash
python3 -m http.server 8787 -d site
```

## 发布目录
site/

## 项目状态
v1.7 把页面从"文字型说明页"升级为"图文革新型数字展览"——8 个展区都有 figure / gallery / 图注 / source note / 展品卡。已不再用占位图的临时提示，外部展品用展品卡 + 外链的形式给出。移动端已专门适配（单列布局）。

v1.5b live hotfix marker 保留（meta + comment 两层）。
v1.6 distribution pack 6 个传播材料 + 36 标题保留。