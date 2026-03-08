# GitHub Awesome Entry Page Design

## 背景

目标是在现有单 URL 导入流程中支持一类 GitHub awesome 仓库页，把它们识别为 `entry_page`，并从 README 正文中抽取后续候选链接。

## 样例与约束

- 用户指定样例：`https://github.com/KenneyNL/awesome-gamedev`
- 该 URL 在 2026-03-08 实测返回 `404`
- 为保证抽取链路可做真实验证，实现保持对该 URL 形态的分类支持，并使用当前可访问的同类页面 `https://github.com/Calinou/awesome-gamedev` 做真实 HTML fixture 与导入验证

## 方案比较

### 方案 A：只按 GitHub 仓库 URL 统一当作入口页

- 优点：实现最简单
- 缺点：会把普通 README 仓库误判成入口页

### 方案 B：按 GitHub 仓库 URL 且仓库名匹配 `awesome`

- 优点：足够小，能覆盖 awesome 列表页而不影响普通仓库
- 缺点：只能覆盖基于命名约定的 awesome 页

### 方案 C：先抓 HTML 再基于 DOM 判断

- 优点：理论上更精确
- 缺点：需要改动现有导入流程顺序，超出本次最小实现范围

## 采用方案

采用方案 B。

- 页面分类：`github.com/<owner>/<repo>` 且 repo 名含 `awesome` 时判为 `entry_page`
- 抽取范围：仅扫描 README 正文容器 `.markdown-body`
- 候选过滤：过滤锚点、自仓库内链接、空标题、常见许可证链接，并按规范化 URL 去重
- 标题生成：`GitHub - <owner>/<repo>`
- 导入落库：继续写入 `20_入口页/`

## 测试计划

1. 页面分类：awesome 仓库 URL 判为 `entry_page`，普通 GitHub 仓库不误判
2. 抽取：从真实 GitHub fixture 中提取稳定标题与已知候选项
3. 过滤：不保留 anchor、自仓库链接、许可证链接；候选 URL 去重
4. CLI / 导入：`import_url()` 能把 GitHub awesome 页写入入口页 Markdown
