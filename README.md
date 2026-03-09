# Game Design Patterns

这是一个面向 Agent 的游戏设计资料库仓库，目标是把任意网页中的游戏机制、内容设计模式与成功案例，沉淀成可被 Obsidian 直接打开与检索的 Markdown 页面。

当前仓库仍处于第一阶段，后续会补充：

- 单 URL 导入流程
- 入口页候选链接抽取
- 网页卡片与设计模式卡片模板
- 基于 `Deconstructor of Fun` 的首批样例

## 仓库定位

这个仓库同时承担两种角色：

- 作为 Obsidian 可直接打开的知识库，保存来源页、入口页、网页卡和设计模式卡
- 作为最小 Python 工具仓库，提供 URL 导入与卡片生成能力

## 第一阶段支持范围

优先支持：

- 标准博客文章页
- 官方文档页
- GitHub README
- 分类页、导航页、`awesome-xxx` 汇总页

当前不处理：

- 视频页
- 社媒长帖
- 登录墙页面
- 重度依赖 JavaScript 才能读正文的页面

## 目录概览

- `10_来源/`：来源站点说明
- `20_入口页/`：栏目页、导航页、`awesome-xxx` 等入口页面
- `30_网页卡/`：单篇网页沉淀
- `40_设计模式/`：核心机制 / 模式卡片
- `50_专题索引/`：人工整理的导航页
- `90_模板与规范/`：模板与命名规范
- `tools/`：最小必要工具
- `src/`：Python 实现
- `tests/`：自动化测试

## 当前工作流

第一阶段只围绕一个核心动作：`导入一个 URL`。

- 如果 URL 指向文章页，则先生成网页卡片，再按正文证据判断是否有资格进入模式整理
- 如果 URL 指向入口页，则生成入口页卡，并抽取后续待处理链接
- 查询层默认依赖 Obsidian 与文本搜索，不额外维护数据库

补充约束：

- 本仓库只关心游戏设计模式，不会把所有导入页面都强行推进到模式聚类。
- 单篇网页如果达不到有意义的游戏设计相关性与信息量门槛，应停留在网页卡或进入归档，不产出模式结论。

## Deconstructor 第二批说明

- `Deconstructor of Fun` 当前第二批不再采用“先按标题聚类”的工作法。
- 正确流程是先逐网页卡筛查，判断其是否通过游戏设计相关性与有效信息门槛。
- 旧的标题级 cluster guess 只保留为历史暂定线索，不能当作正式模式结论。
- 当前评审入口见 `50_专题索引/Deconstructor of Fun - 第二批逐卡筛查.md`

## 如何在 Obsidian 中使用

1. 在 Obsidian 中选择“Open folder as vault”
2. 打开 `~/projects/game-design-patterns/`
3. 优先从 `10_来源/`、`20_入口页/` 和 `40_设计模式/` 开始浏览

## 导入命令

首次安装依赖：

```bash
uv sync
```

导入入口页：

```bash
uv run python tools/import_url.py 'https://www.deconstructoroffun.com/blog?category=Deconstructions'
```

导入单篇文章：

```bash
uv run python tools/import_url.py 'https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation'
```

## 当前样例

- 来源页：`10_来源/Deconstructor of Fun.md`
- 入口页：`20_入口页/Deconstructor of Fun - Deconstructions.md`
- 网页卡：`30_网页卡/The Sweet Art of Feature Adaptation.md`
- 模式卡：`40_设计模式/Feature Adaptation.md`
- 第二批逐卡筛查说明：`50_专题索引/Deconstructor of Fun - 第二批逐卡筛查.md`
- 第二来源页：`10_来源/Game Design Skills.md`
- 第二来源网页卡：`30_网页卡/Designing The Core Gameplay Loop - A Beginner’s Guide.md`
- 第二来源模式卡：`40_设计模式/Core Gameplay Loop.md`
