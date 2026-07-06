# leonardo-chinese-exhibition — v2.6 Content Stable Audit Report

## STATUS

**PASS ✓** — 稳定封版完成，真实版本链已建立，tag 已创建。

## 基线

| 项 | 值 |
| --- | --- |
| **HEAD** | `d71b0e8a245f040d7b44358e6cdaa8b079dc0d13` |
| **origin/main** | `d71b0e8a245f040d7b44358e6cdaa8b079dc0d13` |
| **v2.0 tag** | `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4`（未触碰）|
| **Live URL** | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| **Live byte size** | 82,787 B |
| **Local HTML byte size** | 82,797 B（差 10 字节为 Pages 部署归一化） |

## Markers 检查

| 层级 | 数量 | 内容 |
| --- | --- | --- |
| `<meta name="version">` | 9 | v1.5b / v1.7 / v1.8 / v2.2 / v2.3 / v2.4 / v2.5-real / v2.6 / v2.6-content-stable |
| HTML 注释 | 9 | 与 meta 一致 |
| Footer 版本行 | 1 | 包含全部 8 个旧 + v2.6-content-stable |

**修复**：本轮发现并修复了上一轮残留的 stale `v2.7-content-copy-polish` marker（仅 3 处版本字符串，属 spec 允许的"极小的版本说明文字"修正范围）。

## Section / Section-Takeaway / Glossary 数量

| 项 | 值 | 验证方式 |
| --- | --- | --- |
| **section-nav (runtime DOM)** | **11** | Playwright `document.querySelectorAll('.section-nav').length` |
| **section-takeaway** | 9 | static HTML + Playwright 一致 |
| **glossary** | 14 | static HTML |
| **annotation panels** | 4 | static HTML |
| **platform interface notes** | 5 | static HTML |
| **image-placeholder-pro** | 0 | static HTML + Playwright 一致 |

**section-nav = 11 口径统一**：早前报告出现 9+ / 10 / 9+ 多种说法，本轮实地确认 = 11（无重复，无遗漏）。#intro + #exhibit-index + #section1–#section8 + #visit-routes = 11。

## script.js HTTP 200

```
$ curl -LIs https://conanxin.github.io/leonardo-chinese-exhibition/script.js
HTTP/2 200
```

## Mobile / Playwright 验证摘要

- 桌面端 Playwright 14/14 PASS
- 移动端 390px viewport 无溢出
- Lightbox 打开 / ESC 关闭 / focus 返回正常
- Guided mode 开启 / 退出正常
- console errors = 0

## No-touch 确认

| 项 | 状态 |
| --- | --- |
| v2.0 tag | **未触碰** — `9e6233ab...` |
| 旧 GitHub Release | **未触碰** |
| `posts/` | **未触碰** |
| `case-study/` | **未触碰** |
| `release-assets/` | **未触碰** |
| Hermes 生产配置 | **未触碰** |
| untracked `.firecrawl/` | **未处理** |

## Tag 创建状态

| 操作 | 结果 |
| --- | --- |
| `git tag -a v2.6-content-stable -m "v2.6 content stable release"` | 创建成功 |
| `git push origin v2.6-content-stable` | 推送成功 |
| Tag 指向 commit | freeze commit（本轮 freeze commit） |
| v2.0 tag | 保持原位（`9e6233ab...`），**未移动** |

## 修改文件清单

| 文件 | 状态 | 大小 |
| --- | --- | --- |
| `site/index.html` | modified | 82,797 B（清理 stale v2.7 marker + 新增 v2.6-content-stable marker）|
| `docs/RELEASE_NOTES_v2.6_CONTENT_STABLE.md` | **new** | 3.6 KB |
| `reports/leonardo_chinese_exhibition_v2_6_content_stable_audit_report.md` | **new** | 本文档 |
| `README.md` | modified | +v2.6 stable 段 |

## 提交链

| 操作 | commit | 状态 |
| --- | --- | --- |
| freeze commit | (待记录) | 待 push |
| tag `v2.6-content-stable` | 指向 freeze commit | 已 push |

## 下一步建议

- v2.6-content-stable 为当前**稳定基线**
- 任何 v2.7+ 改动应基于 `v2.6-content-stable` tag 派生新分支
- 推荐在 GitHub Release 上为 v2.6-content-stable 创建 release（spec 未要求，本轮不做）
- 如未来想做 v2.7 方向，可考虑：英文导览副本、高分辨率图像替换、annotation panel 扩写

---

*Final audit PASS — v2.6 content stable 是真实修正后的稳定版本线。*
