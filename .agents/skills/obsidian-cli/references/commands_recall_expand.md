# Recall/Expand 命令编排（按需加载）

## Preflight

```bash
obsidian help
```

如需定向 vault，在命令前加 `vault="<VaultName>"`。

## Recall（召回）

```bash
obsidian search query="<query>" limit=20 format=json
obsidian tags counts
obsidian properties
```

规则：
- 默认 `limit=20`，scope 很窄时降到 `10`
- 目录/主题约束命中时优先排序（例如 `20_项目/OrbitOS/`）
- 召回后先给出候选 Top3

## Expand（扩展）

```bash
obsidian search:context query="<query>" limit=5 format=json
obsidian backlinks path="<Top1 路径>"
obsidian links path="<Top1 路径>"
obsidian read path="<Top1 路径>"
```

规则：
- 优先扩展 Top1，再按预算扩展 Top2/Top3
- 证据片段优先选“标题 + 关键段 + 关联链接”

## 排序先验（path_prior=v2）

- 优先 `.md` 页面，降低 `.json` 工件优先级
- 查询存在 `scope` 时，优先 scope 内路径
- 非报告型问题降低 `10_日记/` 与 `Reports/` 聚合页权重
