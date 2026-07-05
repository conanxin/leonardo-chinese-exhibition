# Cloudflare Pages 发布说明

## Project Settings
- Project root: 仓库根目录
- Build command: （留空）
- Publish directory: `site`

## 部署步骤
1. 连接 GitHub 仓库
2. 设置 Publish directory 为 `site`
3. 保存并部署

## 部署后检查
- 访问 `https://<project>.pages.dev`
- 检查所有展区锚点跳转
- 检查图片占位与 source note
- 检查移动端显示

## 本地预览
```bash
python3 -m http.server 8787 -d site
```