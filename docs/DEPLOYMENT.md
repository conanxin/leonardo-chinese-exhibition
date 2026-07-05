# 部署说明

## Live URL
https://conanxin.github.io/leonardo-chinese-exhibition/

## 本地预览
```bash
python3 -m http.server 8787 -d site
```

## GitHub Pages
- Source: GitHub Actions
- Workflow: .github/workflows/pages.yml
- Publish directory: site

## 线上检查清单
- 首页 Hero
- 8 个展区完整正文
- SVG 图解
- 移动端适配
- 来源说明

## 更新发布方式
每次 push main 后，GitHub Actions 自动部署。