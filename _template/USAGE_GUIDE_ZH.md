# 中文数字展览模板使用手册

本手册介绍如何从 `_template/` 起步，做出一个可发布的中文数字展览网站。
本模板来自 leonardo-chinese-exhibition v3.0 真实抽离与 v3.1 真实 pilot 验证，结构稳定，可复用。

---

## 这个模板适合什么项目？

### 适合

- 艺术家专题展
- 古籍、手稿、档案专题展
- 建筑史、科学史、设计史展览
- 小型数字人文项目
- 个人研究型展览
- 课程或工作坊的展示型项目

### 不适合

- 大型 CMS
- 多用户后台系统
- 复杂数据库项目
- 高并发图片平台
- 未完成版权核验的大规模图片站

---

## 从模板开始的 8 步

1. 复制 `_template/` 到新项目目录
2. 确定展览主题和观众问题
3. 填写 `data/*.json`
4. 准备图片、平台截图或自制 SVG
5. 写展品卡、source note、credit line
6. 写 visitor guide / curatorial essay / research notes
7. 做 source and rights audit
8. 做 pilot / freeze / release

---

## 最小可行展览

一个最小可用的中文数字展览，必须包含：

- Hero（首屏导语）
- 3 分钟导览
- 展览地图
- 至少 4 个 section
- 至少 4 个 artifact card
- 至少 6 个 glossary terms
- source manifest
- rights note
- release report

---

## 推荐目录结构

```
site/                    # 静态站点 (HTML / CSS / JS)
data/                    # 结构化数据 (JSON)
assets/                  # 图片、自制图解、平台截图
docs/                    # 设计说明、roadmap、阶段报告
reports/                 # 每个版本的验证报告
release-assets/          # GitHub Release 配套材料
_template/               # 本模板
_pilots/                 # 不部署的试验性展览
```

每个目录的边界：

- `site/` 只放最终上线的 HTML / CSS / JS
- `data/` 只放 JSON，禁止混入项目专属词
- `assets/` 不存放未经 rights audit 的馆藏图
- `_pilots/` 不部署，不影响 live tag

---

## 常见错误

至少列 12 个真实可踩的坑：

1. 先做视觉，不做 source note
2. 图片有图注但没有来源
3. rights note 写得太绝对（"可自由使用"等断言必须删除）
4. template 里混入项目专属词（"达·芬奇"、"手稿"等）
5. 过早引入框架（React / Vue / 构建工具）
6. 忘记 mobile check
7. 忘记 release report
8. 用 `git add .`（会把 untracked 内容一起塞进 commit）
9. 直接改 live 而不是先在 pilot 验证
10. 没有 stable freeze（不封版直接部署）
11. 没有记录 live byte size
12. 没有记录 tag target commit

进阶错误：

13. 把 draft / pilot 当 stable 推进
14. 把 phantom memory 当真实起点（v3 之前的教训）
15. release notes 写好但不回填 commit SHA

---

## 下一步阅读

- 内容怎么写：[CONTENT_AUTHORING_GUIDE_ZH.md](./CONTENT_AUTHORING_GUIDE_ZH.md)
- 图片与权利怎么查：[SOURCE_RIGHTS_CHECKLIST_ZH.md](./SOURCE_RIGHTS_CHECKLIST_ZH.md)
- 怎么先做 pilot：[PILOT_WORKFLOW_ZH.md](./PILOT_WORKFLOW_ZH.md)
- 怎么封版与发布：[RELEASE_WORKFLOW_ZH.md](./RELEASE_WORKFLOW_ZH.md)