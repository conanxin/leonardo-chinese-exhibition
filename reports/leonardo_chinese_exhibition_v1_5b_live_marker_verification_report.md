# Leonardo Chinese Exhibition — v1.5b-live-hotfix 线上验证报告

报告生成时间：2026-07-06
项目：leonardo-chinese-exhibition
目标站：https://conanxin.github.io/leonardo-chinese-exhibition/

---

## 1. 验证结论（一行摘要）

✓ **线上页面已是新版展览结构**，**v1.5b-live-hotfix marker 已写入 `site/index.html` 并成功部署**，**GitHub Actions 通过**，**curl 验证 marker 在线上页面可被检索到**。

| 检查项 | 结果 |
|---|---|
| 线上页面是否为新版展览页 | ✓ 是 |
| `v1.5b-live-hotfix` marker 是否已写入 `site/index.html` | ✓ 是（3 处） |
| GitHub Actions 是否成功 | ✓ 是（run #28758282236 → success） |
| curl 验证 marker 是否通过 | ✓ 通过 |

---

## 2. 线上页面版本判断（老版 / 新版 fork 检测）

通过 `curl -L https://conanxin.github.io/leonardo-chinese-exhibition/ -o /tmp/leonardo-live.html`
获取 13,078 字节有效 UTF-8 HTML 进行差异化探测。

### 2.1 新版特征命中（必须存在）

| 新版特征字符串 | 命中行 |
|---|---|
| `被拆散的手稿与重新连接的思想` (主标题副标题) | line 6, 29 |
| `策展前言` | line 48 |
| `达·芬奇的伟大，不只是他知道很多` | line 50, 57 |
| `展览地图` | line 62 |
| `资料来源与延伸阅读` | line 258 |

→ **5/5 全部命中**。新版展览导航骨架（策展前言 / 展览地图 / 8 展区 + 序厅 / 资料来源）完整存在。

### 2.2 旧版特征命中（不应作为"展示性旧特征"出现）

| 旧版特征字符串 | 命中行 | 判断 |
|---|---|---|
| `个人展区` | 0 | ✓ 无 |
| `图片占位` | 0 | ✓ 无 |
| `浅色占位` | 0 | ✓ 无 |
| `一座被拆散的思想博物馆` | line 64, 80 | ⚠ 命中 2 次——需进一步判断 |

→ `一座被拆散的思想博物馆` 在新版中是 **序厅（intro hall）章节的小标题**，
作为章节命名被保留在新结构中（line 64 是导航锚点"序厅：一座被拆散的思想博物馆"，
line 80 是 intro section 的 `<h2>`）。它不是旧版"黑底卡片页 + 浅色占位"的破损痕迹，
而是新版展览对同一叙事的章节命名复用。**判定为新版合法保留**，不影响版本结论。

### 2.3 版本判断

✓ **线上页面 = 新版 OpenAI editorial 风展览页**（策展前言 / 展览地图 / 8 展区 + 序厅 / 资料来源与延伸阅读）。

---

## 3. marker 写入 `site/index.html`

将 `v1.5b-live-hotfix` 版本标记写入三个位置：

### 3.1 `<head>` 中加入 `<meta name="version">`

```html
<meta name="version" content="v1.5b-live-hotfix">
```

### 3.2 `<body>` 顶部加入 HTML 注释

```html
<!-- leonardo-chinese-exhibition v1.5b-live-hotfix -->
```

### 3.3 footer 中显示版本文字

```html
<p class="version-footer">版本：v1.5b live hotfix</p>
```

### 3.4 本地验证

```
$ grep -nE "v1\.5b-live-hotfix|版本：v1\.5b" site/index.html
8:  <meta name="version" content="v1.5b-live-hotfix">
13:<!-- leonardo-chinese-exhibition v1.5b-live-hotfix -->
272:  <p class="version-footer">版本：v1.5b live hotfix</p>
```

3 个位置全部就位。

---

## 4. GitHub Actions 部署

| 项 | 值 |
|---|---|
| 触发 commit | `d69f516` "Add live hotfix version marker" |
| Run ID | 28758282236 |
| Workflow | GitHub Pages deploy（upload-pages-artifact@v3 + deploy-pages@v4） |
| 状态 | success |
| 启动时间 | 2026-07-05 23:16:01 UTC |
| 完成时间 | 2026-07-05 23:16:12 UTC |
| 耗时 | ~11 秒 |

### 4.1 步骤结果

所有 5 个步骤（Set up job / checkout / configure-pages / upload-pages-artifact / deploy-pages）以及 Post-Run / Complete job 全部 `success`。

未使用 Re-run jobs；每次成功都来自新 commit，符合用户约束"用新 commit 触发 fresh run"。

---

## 5. curl 线上 marker 验证

```
$ curl -sS -L https://conanxin.github.io/leonardo-chinese-exhibition/ -o /tmp/leonardo-final.html \
  -w "HTTP:%{http_code} BYTES:%{size_download}\n"
HTTP:200 BYTES:13245

$ grep -nE "v1\.5b-live-hotfix|版本：v1\.5b" /tmp/leonardo-final.html
8:  <meta name="version" content="v1.5b-live-hotfix">
13:<!-- leonardo-chinese-exhibition v1.5b-live-hotfix -->
272:  <p class="version-footer">版本：v1.5b live hotfix</p>

$ grep -c "v1\.5b-live-hotfix" /tmp/leonardo-final.html
2
```

✓ HTTP 200，13,245 字节（比上一次 13,078 增加 167 字节 ≈ 3 行新内容）
✓ meta + comment 两个 hyphenated marker 实例命中
✓ footer 显示版本：v1.5b live hotfix

---

## 6. 提交时间线

| 时间 (UTC) | 事件 | SHA / Run |
|---|---|---|
| 2026-07-05 23:12:55 | 触发 deploy commit "Fix live release deploy state" | `2d3180e` → run 28758201911 → success |
| 2026-07-05 23:15:57 | 触发 marker commit "Add live hotfix version marker" | `d69f516` → run 28758282236 → success |
| 2026-07-05 23:16:12 | 线上 marker 校验通过 | HTTP 200, 3 处 marker 可检索 |

主线分支：`main`
仓库：`conanxin/leonardo-chinese-exhibition`

---

## 7. 备注 / 已知事项

- 工作仓库中部分跟踪文件 (`site/index.html`, `site/style.css`) 文件模式为 `0600`，本次未触碰，不影响 deploy，但若以后需要在线编辑/共享请留意。
- `一座被拆散的思想博物馆` 是新版序厅章节标题，不是旧版破损占位特征——如果未来想统一新/旧两个分支的措辞，需要在 PR 描述中单独标注。
- 本次 marker commit 不影响内容版面（仅 +4 行），页面视觉与结构与 commit `2d3180e` 完全一致。
