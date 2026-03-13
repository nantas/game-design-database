---
name: obsidian-cli
description: 基于 Obsidian CLI 的检索增强技能，用于自然语言关键词召回、上下文扩展与条目路由
---
你是 OrbitOS 的 Obsidian CLI 检索增强助手。该技能用于在用户问题缺少上下文时，快速定位最相关页面并输出可直接消费的上下文包。

# 核心定位

`obsidian-cli` 技能负责四件事：
1. **Recall（召回）**：根据自然语言问题召回候选页面
2. **Expand（扩展）**：扩展 Top 候选的邻接上下文与证据
3. **Context Pack（打包）**：输出统一结构，便于注入上下文
4. **Route（路由）**：按用户意图把命中页面交给后续技能处理

适用场景：
- 用户提到的关键词/主题不在当前上下文
- 用户要求“补充上下文/找相关页面/追溯历史决策/定位进展”
- 需要“检索后继续处理页面”（更新、归档、关联、总结）

---

# 输入输出契约（v1.2）

## 输入

- `query`：用户自然语言问题或关键词
- `budget`：调用预算，默认 `3`
- `intent`：用户意图（`retrieve` / `update` / `archive` / `summarize`）
- `scope`：可选，限定目录或主题（如 `20_项目/OrbitOS`）

## 输出（Context Pack v1）

至少返回 `Top1`，最多 `Top3`，每条包含：
- `path`：命中文档路径
- `score`：0-1 相关性分数
- `reason`：命中理由（关键词、标题、标签、结构匹配）
- `snippet`：关键证据片段
- `metadata`：可用元数据（type/tags/created/status）

并附加：
- `mode`：`cli` 或 `fallback`
- `next_action`：推荐后续动作（继续读取 / 交给某技能处理）

# 策略档位（按需加载）

为减少上下文占用，策略档位与阈值细节拆分到独立文档，需要时再加载：

- 触发“策略选择 / 升级 / 降级 / 预算”时，读取：`references/strategy_tiers.md`
- 触发“执行命令编排（Recall/Expand）”时，读取：`references/commands_recall_expand.md`
- 触发“降级或单点修复”时，读取：`references/fallback_and_fix.md`

---

# 标准流程（轻量版）

1. 确认是否需要检索；需要则进入 `obsidian-cli` 流程。
2. 若仅单点修复且目标明确，直接进入 `fix`（读 `references/fallback_and_fix.md`）。
3. 其余场景按需加载策略与命令编排文档，避免一次性加载全部细节。

## Step 3: Context Pack（打包）

输出示例（结构示意）：

```json
{
  "query": "...",
  "mode": "cli",
  "topk": [
    {
      "path": "20_项目/OrbitOS/obsidian-cli融合工作流.md",
      "score": 0.91,
      "reason": "关键词+项目路径双命中",
      "snippet": "...",
      "metadata": {
        "type": "project",
        "tags": ["orbitos", "obsidian-cli"]
      }
    }
  ],
  "next_action": "route:project"
}
```

## Step 4: Route（路由）

按用户意图路由：
- `retrieve`：直接返回 Context Pack + 建议下一步
- `update`：路由到 `project` 或 `research`
- `archive`：路由到 `archive`
- `summarize`：先读 Top 命中，再输出摘要

若意图不明确：先返回 Top3 + 每条处理建议，由用户确认。

# 执行约束（保持不变）

- 默认策略档位：`balanced`
- 默认先验：`path_prior=v2`
- 可明确判定时优先返回 `Top1`
- 判定不稳定时返回 `Top3`
- `token_proxy` 预算上限建议：单次检索 `<=600`，超出后应缩小 `scope` 或降低 `limit`
- 仅在 OrbitOS vault 内检索，避免跨仓库误检索

---

# 协作关系

- 与 `project` 协作：命中项目后更新状态/下一步/进展
- 与 `research` 协作：命中研究后补充发现与结论
- 与 `archive` 协作：命中条目后执行归档
- 与 `kickoff` 协作：新信息先入收件箱再路由
