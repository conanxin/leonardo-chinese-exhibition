# 达·芬奇的纸上宇宙：被拆散的手稿与重新连接的思想

基于 Leonardo//thek@ 平台的中文数字展览项目。

## Live Demo
https://conanxin.github.io/leonardo-chinese-exhibition/

## 当前版本
v1.7 exhibit image upgrade（在 v1.5b live hotfix + v1.5c repo hygiene + v1.6 distribution pack 之上，把展览从"文字型说明页"升级为"图文革新型数字展览"）

## v1.7 展览图像升级（exhibit image upgrade）

v1.7 解决了"页面底部原来写着图片使用占位"的问题。本版本：

- 增加 5 个原创 SVG 图解（manuscript-journey / collection-split / watermark-evidence-chain / recomposition-triptych / platform-tool-wall）以及 1 个升级版（thinking-map）
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