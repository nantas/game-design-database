# 策略档位与阈值（按需加载）

## 策略档位

- `precision`：`cli_3step + budget=3 + path_prior=v2`
- `balanced`：`cli_1step + budget=2 + path_prior=v2`
- `speed`：`hybrid + budget=1 + path_prior=v2`
- `fix`：`rg` 定点检索优先，用于“已知目标/单点修复”

## 选择规则（按顺序命中）

1. 若 `intent` 明确：
   - `update/archive/summarize` -> `precision`
   - `retrieve` -> `balanced`
   - 明确“修复/改名/断链/单条排查” -> `fix`
2. 若 `intent` 缺失，用问题关键词兜底：
   - 包含“更新/写入/归档/总结/报告” -> `precision`
   - 包含“快速看下/先找一下/是否有/大概” -> `speed`
   - 包含“断链/修复/改名/替换/单条” -> `fix`
   - 其他 -> `balanced`
3. 执行中满足以下任一条件，立即从 `balanced/speed` 升级到 `precision`：
   - `Top1-Top2 score < 0.15`
   - Top1 不是 `.md` 页面
4. 执行中满足以下任一条件，立即从 `precision/balanced` 降级到 `fix`：
   - 已明确目标路径或唯一标题
   - 仅需修复单条链接或命名
   - `obsidian unresolved verbose` 输出过大或超出上下文预算

## 指标备注（可忽略）

- `precision` 在 20 条联调中 `Hit@1` 最高（约 `0.45`）
- `speed` 在 20 条联调中 `TTFR` 最低（约 `9ms`）
- 融合策略矩阵参考：
  `30_研究/知识库/Obsidian_CLI_Artifacts/Obsidian_CLI_融合工作流_策略选择矩阵_2026-03-03.md`
