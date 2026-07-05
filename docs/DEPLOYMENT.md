# 部署说明

## 本地预览
```bash
python3 -m http.server 8787 -d site
```

## GitHub Pages 发布
1. 将仓库设为公开
2. Settings → Pages → Source 选择 `Deploy from a branch`
3. Branch 选择 `main`，Folder 选择 `/site`
4. 保存后等待部署完成

## Cloudflare Pages 发布
1. 连接 GitHub 仓库
2. Build settings：
   - Build command: （留空）
   - Build output directory: `site`
3. 保存并部署

## 构建命令
本项目**无需构建**，`site/` 目录可直接作为静态站点发布。

## 发布目录
`site/`（包含 index.html、style.css、assets/）