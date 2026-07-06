# v2.5 real deploy recovery — report

**STATUS: PASS**

## 1. 起始状态

- v2.5-real 功能代码已在 commit `c512dbd1` 真实落地并 push 到 `origin/main` (`0d58fdc..c512dbd`)
- 本地 Playwright 36/36 PASS
- GitHub Pages deploy **失败**（transient "Deployment failed, try again later"，`actions/deploy-pages@v4` 抛错）
- Live 仍为 v2.7（77,474 字节，无 v2.5-real marker）

## 2. 恢复步骤

### Step 1: 真实基线确认

```
$ pwd
/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition

$ git status -sb
## main...origin/main
?? .firecrawl/

$ git rev-parse HEAD
c512dbd1ac6797cc4334f5981e1f56238389449c

$ git rev-parse origin/main
c512dbd1ac6797cc4334f5981e1f56238389449c

$ git rev-parse v2.0-public-portfolio-case
9e6233ab2b2c5aa3e1243565583f8f66c7df34b4   ← 未触碰
```

### Step 2: v2.5-real 文件本地核对

```
$ grep -n "v2.5-real-guided-accessibility" site/index.html
15:<meta name="version" content="v2.5-real-guided-accessibility">

$ grep -n "getTourSections\|createSectionNav\|applyGuidedMode" site/script.js
181:  function getTourSections() {
207:  function createSectionNav() {
208:    const sections = getTourSections();
237:    const sections = getTourSections();
301:  function applyGuidedMode(active) {
308:    const sections = getTourSections();
328:        applyGuidedMode(false);
341:        applyGuidedMode(active);
365:    createSectionNav();

$ grep -c '<aside class="section-takeaway"' site/index.html
9

$ grep -c "image-placeholder-pro" site/index.html
0
```

**全部通过** — `c512dbd` 真实包含 v2.5-real 内容。

### Step 3: 优先 rerun failed run

```
$ gh run list --workflow "Deploy GitHub Pages" --limit 5
28776529968  c512dbd1  failure  ← 待 rerun
28771570059  0d58fdc8  success
28771506209  31e51265  success
28766893442  c3c3e0ba  success
28766493923  988ebb9b  success

$ gh run rerun 28776529968 --failed
（rerun started, in_progress）

$ gh run watch 28776529968
X Error: Multiple artifacts named "github-pages" were unexpectedly found for this workflow run. Artifact count is 2.
```

**Rerun 失败** — 旧 failed run 留下的 `github-pages` artifact 还在，导致 `actions/deploy-pages@v4` 报 multi-artifact 冲突。属于 GitHub Pages 基础设施 transient issue。

### Step 4: empty commit 触发新 deploy

由于 rerun 失败，转用 empty commit 触发全新 run（不修改 site/）：

```
$ git commit --allow-empty -m "Retry Pages deploy for v2.5-real"
[main fe54737] Retry Pages deploy for v2.5-real

$ git log --oneline -3
fe54737 Retry Pages deploy for v2.5-real              ← deploy-only commit
c512dbd Rebuild guided accessibility from v2.4 baseline  ← 真实 v2.5-real 内容
0d58fdc docs: backfill v2.7 report with commit hash + live HTTP

$ git push origin main
To https://github.com/conanxin/leonardo-chinese-exhibition.git
   c512dbd..fe54737  main -> main
```

**注意**：`fe54737` 是 deploy-only empty commit，**不修改任何 site/ 文件**。它只是为了绕过旧 failed run 的 multi-artifact 冲突，触发一个全新的 workflow run。

## 3. GitHub Actions run

| Run ID | Commit | Status | 备注 |
|---|---|---|---|
| 28776529968 | c512dbd | failure (original) | "Deployment failed, try again later" |
| 28776529968 | c512dbd | failure (rerun) | "Multiple artifacts named github-pages" |
| **28777528759** | **fe54737** | **success (16s)** | **v2.5-real 真正上线** |

新 run 通过 `actions/configure-pages@v5` + `actions/upload-pages-artifact@v3` + `actions/deploy-pages@v4` 全部成功，仅有 Node 20 deprecation 警告（无关紧要）。

## 4. live verification

```
$ curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ | grep "v2.5-real-guided-accessibility"
<meta name="version" content="v2.5-real-guided-accessibility">

$ curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ | grep -c '<aside class="section-takeaway"'
9

$ curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ | grep -c "image-placeholder-pro"
0

$ curl -L -s https://conanxin.github.io/leonardo-chinese-exhibition/ | wc -c
82611   ← 之前 77,474，v2.5-real 已落地

$ curl -LIs https://conanxin.github.io/leonardo-chinese-exhibition/script.js
HTTP/2 200
server: GitHub.com
content-type: application/javascript; charset=utf-8
```

### Markers on live (按出现顺序)

```
v1.5b-live-hotfix                       ← 保留
v1.7-exhibit-image-upgrade              ← 保留
v1.8-real-image-integration             ← 保留
v2.2-exhibition-experience-upgrade      ← 保留
v2.3-platform-screenshot-upgrade        ← 保留
v2.4-artifact-annotation-upgrade        ← 保留
v2.7-content-copy-polish                ← 保留
v2.5-real-guided-accessibility          ← 新增（本轮）
```

**8 个 markers 全部保留** + **v2.5-real 新 marker 已上线**。

### Live Playwright 验证（13/13 PASS）

```
============================================================
PASS: 13
FAIL: 0
============================================================
```

| 检查 | 结果 |
|---|---|
| runtime section-nav ≥ 9 | ✓ |
| section-takeaway == 9 | ✓ |
| image-placeholder-pro == 0 | ✓ |
| v2.5-real marker 在 live | ✓ |
| v2.7 marker 保留 | ✓ |
| v2.4 marker 保留 | ✓ |
| v2.0 tag 不在 meta 中（git-only） | ✓ |
| tour progress 存在 | ✓ |
| tour jump links ≥ 9 | ✓ |
| 5-min button 存在 | ✓ |
| 0 console errors | ✓ |
| mobile 390: no overflow | ✓ |
| mobile 390: section-nav 仍 ≥ 9 | ✓ |

## 5. final commit

```
$ git log --oneline -3
fe54737 Retry Pages deploy for v2.5-real
c512dbd Rebuild guided accessibility from v2.4 baseline
0d58fdc docs: backfill v2.7 report with commit hash + live HTTP
```

| Commit | 角色 |
|---|---|
| `c512dbd` | **v2.5-real 功能代码**（marker + 9 takeaways + 23 lazy imgs + id=intro + id=exhibition-map + 重写 script.js + style.css 新增 +12 KB + 报告） |
| `fe54737` | **deploy-only empty commit**（仅触发全新 Pages workflow，绕过旧 failed run 的 multi-artifact 冲突） |

## 6. 严格不触碰

| 资产 | 状态 |
|---|---|
| v2.0 tag at `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4` | **未触碰** ✓ |
| GitHub Release (7 assets) | **未触碰** ✓ |
| `posts/` | **未触碰** ✓ |
| `case-study/` | **未触碰** ✓ |
| `release-assets/` | **未触碰** ✓ |
| untracked `.firecrawl/` | **未处理** ✓ |
| 6 张真实手稿 JPG | **未触碰** ✓ |
| 5 张平台截图 JPG | **未触碰** ✓ |
| 6 张原创 SVG 图解 | **未触碰** ✓ |
| v1.5b / v1.7 / v1.8 / v2.2 / v2.3 / v2.4 / v2.7 markers | **全部保留** ✓ |

## 7. live URL

https://conanxin.github.io/leonardo-chinese-exhibition/

## 8. 教训

- GitHub Pages `actions/deploy-pages@v4` 在某些情况下会因 multi-artifact 冲突 transient 失败。`gh run rerun --failed` 在这种情况下不解决问题（旧 artifact 仍在）。
- 最稳的恢复方式是：empty commit 触发全新 workflow run，绕开任何残留的 run state。
- 每次失败的 Pages deploy 后，都应考虑用 empty commit 而不是 rerun，除非 rerun 失败原因明确是 vcs / repo 配置问题。

**v2.5 real deploy recovery → PASS ✓**
