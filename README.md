# 达·芬奇的纸上宇宙：被拆散的手稿与重新连接的思想

基于 Leonardo//thek@ 平台的中文数字展览项目。

## Live Demo
https://conanxin.github.io/leonardo-chinese-exhibition/

## 当前版本
v1.6 distribution pack（在 v1.5b live hotfix + v1.5c repo hygiene 之上叠加传播材料包）

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
├── site/                  # GitHub Pages 部署根（仅这一层被部署）
│   ├── index.html         # 中文展览主页（v1.5b-live-hotfix marker）
│   ├── style.css
│   └── assets/            # SVG 结构图 + favicon
├── posts/                 # v1.6 传播材料（公众号 / X / 小红书 / 视频 / 作品集 / 标题）
├── reports/               # 版本报告（v0.2 → v1.5c → v1.6）
├── docs/                  # DEPLOYMENT / GITHUB_PAGES / CLOUDFLARE / RELEASE_NOTES
├── exhibition/            # 策展脚本与计划
├── research/              # 学术背景资料
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
已完成 OpenAI-style 极简 editorial 重构，8 个展区正文完整，SVG 图解齐全，移动端适配良好，可公开发布。

v1.5b live hotfix 已上线（含 `<meta name="version">` + footer 版本文字）。
v1.5c repo hygiene 审计已闭合（30 个文件权限 0600 → 0644，workflow 通过）。
v1.6 distribution pack 已生成 6 个传播材料 + 36 条标题。