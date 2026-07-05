# GitHub Pages 发布说明

## 仓库设置
1. 在 GitHub 创建仓库 `leonardo-chinese-exhibition`
2. 本地添加 remote：
   ```bash
   git remote add origin https://github.com/conanxin/leonardo-chinese-exhibition.git
   git branch -M main
   git push -u origin main
   ```

## Pages 配置
1. Settings → Pages
2. Source 选择 **Deploy from a branch**
3. Branch 选择 `main`
4. Folder 选择 `/site`
5. Save

## 发布目录
`site/`（直接作为 Pages 源）

## 本地预览
```bash
python3 -m http.server 8787 -d site
```

## 常见问题
- 部署后 5-10 分钟生效
- 根路径 404 是正常现象，`/site/index.html` 正常访问即可
- 图片占位路径使用相对路径 `assets/`