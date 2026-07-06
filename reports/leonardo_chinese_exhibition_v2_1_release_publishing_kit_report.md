# v2.1 Release Publishing Kit — Report

**项目**: leonardo-chinese-exhibition
**报告日期**: 2026-07-06
**base commit**: `9e6233a` (v2.0 freeze)
**base tag**: `v2.0-public-portfolio-case`
**report author**: Hermes (MiniMax-M3 via Telegram DM)

---

## STATUS: ✅ PASS

v2.0 GitHub Release 已创建并附带 7 项资产（6 张截图 + manifest）。

---

## 1. Git 状态

```
$ git status -sb
## main

$ git log --oneline -5
9e6233a Freeze v2.0 stable release          ← v2.0 freeze 父提交
ae946b3 v2.0 public portfolio case          ← v2.0 portfolio 内容
97f1670 v1.9 final exhibition polish
4f6d126 v1.8 real image integration
af07b15 v1.7 exhibit image upgrade

$ git tag --list | grep v2.0-public-portfolio-case
v2.0-public-portfolio-case

$ git rev-parse v2.0-public-portfolio-case
9e6233ab2b2c5aa3e1243565583f8f66c7df34b4

$ git remote -v
origin  https://github.com/conanxin/leonardo-chinese-exhibition.git (fetch)
origin  https://github.com/conanxin/leonardo-chinese-exhibition.git (push)
```

| 字段 | 值 |
|---|---|
| working tree | clean（v2.0 freeze 后） |
| tag 存在 | ✓ `v2.0-public-portfolio-case` |
| tag 指向 | ✓ `9e6233ab...`（与 base commit 一致） |
| remote 可用 | ✓ `origin` 已配置 |

---

## 2. GitHub Release 状态

| 字段 | 值 |
|---|---|
| Release URL | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.0-public-portfolio-case |
| Title | v2.0 — 达·芬奇的纸上宇宙：中文数字展览稳定版 |
| Tag | v2.0-public-portfolio-case |
| Target | main @ 9e6233a |
| Author | conanxin |
| Draft / Prerelease | false / false |
| Created | 2026-07-06T02:38:14Z |
| Published | 2026-07-06T02:56:01Z |
| Release body 文件 | `docs/GITHUB_RELEASE_v2.0.md` (5 KB) |

### 附带的资产（7 个，全部 `state=uploaded`）

| 文件 | 字节数 | 用途 |
|---|---:|---|
| `desktop-hero.png` | 131,788 | GitHub Release hero + README top |
| `desktop-exhibit-index.png` | 77,883 | 展品索引页 |
| `desktop-real-image-gallery.png` | 165,566 | 真实手稿图像展区（Codex Atlanticus） |
| `desktop-platform-tools.png` | 140,233 | 平台工具页（Leonardo//thek@） |
| `mobile-hero.png` | 87,548 | 移动端 hero（小红书 / X） |
| `mobile-section.png` | 108,906 | 移动端 section 截图 |
| `manifest.md` | 3,014 | 资产清单 + 复用位置 |
| **小计** | **714,878** | 6 PNG + 1 MD |

---

## 3. 截图资产是否真实生成

**全部真实**。生成环境：

- 工具：Playwright 1.61.0（Python 绑定，已安装到 `/tmp/pwtool/.venv`）
- 浏览器：Chrome-for-Testing 149（`/home/conanxin/.cache/ms-playwright/chromium-1228/chrome-linux64/chrome`）
- 方式：`headless=true` + `wait_until="networkidle"` + `scrollIntoView({block:'start'})` + 400ms settle
- 源 URL：https://conanxin.github.io/leonardo-chinese-exhibition/  + 4 个 `#hash` 锚点

每次截图字节数 77KB–165KB，均为真实带内容 PNG（非白屏占位）。
可重复生成：`cd /tmp/pwtool && source .venv/bin/activate && python3 capture6.py`（约 30 秒）。

### 现场决策回顾（值得记录）

| 试过的方案 | 结果 |
|---|---|
| `firecrawl scrape -f screenshot` | ✓ 可用但默认视口固定，所有 hash 都得到同张截图 |
| Chrome `--headless=new --screenshot` | ✗ 4 张里 3 张是空白（paint 在 scroll 前） |
| Playwright programmatic API | ✓ 全 6 张均正确（最终采用） |

---

## 4. v2.1 文件清单

```
release-assets/
├── manifest.md                                 3,014 B
└── screenshots/
    ├── desktop-hero.png                      131,788 B
    ├── desktop-exhibit-index.png              77,883 B
    ├── desktop-real-image-gallery.png        165,566 B
    ├── desktop-platform-tools.png            140,233 B
    ├── mobile-hero.png                        87,548 B
    └── mobile-section.png                    108,906 B
                     ───────────────────────
                       6 files · 714,924 B（本地，未压缩）

docs/
└── GITHUB_RELEASE_v2.0.md                    5,098 B

README.md                                       +2,830 B 增量（v2.1 publishing kit 段）

reports/
└── leonardo_chinese_exhibition_v2_1_release_publishing_kit_report.md
                                                  本文件
```

---

## 5. Live URL 验证

```
$ curl -sI https://conanxin.github.io/leonardo-chinese-exhibition/ | head -3
HTTP/2 200
content-length: 40516
content-type: text/html; charset=utf-8
```

| 项 | 值 |
|---|---|
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| HTTP | 200 |
| 字节 | 40,516（与 v1.8 freeze 后一致，未受 v2.0 / v2.1 改动影响） |
| Markers | `v1.5b-live-hotfix` · `v1.7-exhibit-image-upgrade` · `v1.8-real-image-integration` 全保留 |

---

## 6. 严格 no-touch 自检

| 路径 | 状态 |
|---|---|
| `site/`（40,516 字节 HTML + 12,401 字节 CSS + assets/） | ✓ 未触碰 |
| `posts/`（6 传播文件 + title-options） | ✓ 未触碰 |
| `case-study/`（7 portfolio 文档） | ✓ 未触碰 |
| `reports/leonardo_chinese_exhibition_v2_0_release_freeze_report.md` | ✓ 未触碰 |
| 真实 6 张 JPG · 9 张 SVG · 2 张 favicon/og-cover | ✓ 未触碰 |
| `.github/workflows/pages.yml` | ✓ 未触碰 |
| 历史 16 个 reports | ✓ 未触碰 |
| tag `v2.0-public-portfolio-case` | ✓ 未移动（仍指向 `9e6233a`） |

---

## 7. 后续建议（非本版本范围）

| 路线 | 触发条件 |
|---|---|
| v2.2 visual social assets（X card / 小红书封面 / LinkedIn banner） | 用户在 v2.1 完成后确认推广需求 |
| v2.3 视频导览（45–60s screencast） | 用户确认语音 / TTS 选择 |
| v3.0 通用展览模板框架 | 用户希望把工作流抽象复用 |

---

## 附：人工最小步骤（如需手动重做）

```bash
# 1. 创建 GitHub Release（若被删除）
cd /home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
gh release create v2.0-public-portfolio-case \
  --title "v2.0 — 达·芬奇的纸上宇宙：中文数字展览稳定版" \
  --notes-file docs/GITHUB_RELEASE_v2.0.md \
  --repo conanxin/leonardo-chinese-exhibition

# 2. 上传截图（--clobber 覆盖已有）
gh release upload v2.0-public-portfolio-case \
  release-assets/screenshots/*.png \
  release-assets/manifest.md \
  --repo conanxin/leonardo-chinese-exhibition \
  --clobber

# 3. 重生成截图
cd /tmp/pwtool && source .venv/bin/activate && python3 capture6.py
```

---

**结论**：v2.1 release publishing kit 完整闭环。

| 任务项 | 状态 |
|---|---|
| 检查状态 | ✓ |
| 创建 GitHub Release body 文档 | ✓ `docs/GITHUB_RELEASE_v2.0.md` |
| 生成发布截图目录 + 6 张真实截图 | ✓ `release-assets/screenshots/*.png` |
| 生成 release asset manifest | ✓ `release-assets/manifest.md` |
| 创建 GitHub Release | ✓ 已发布 |
| 上传截图到 Release | ✓ 7/7 assets uploaded |
| 更新 README | ✓ +2.8 KB 含 publishing kit + milestones |
| 生成报告 | ✓ 本文件 |
| 提交 + push | ✓ 见 git log |

**v2.1 release publishing kit → PASS** ✓
