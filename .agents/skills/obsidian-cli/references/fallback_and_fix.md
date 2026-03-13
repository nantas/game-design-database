# 降级与单点修复（按需加载）

## 触发条件

- `obsidian` 命令不可用
- Obsidian 应用未运行
- 目标 vault 不匹配或访问失败
- 单点修复场景（已知路径/唯一标题/单条链接）

## 降级顺序

`CLI -> 本地文本检索`

## 本地检索模板

```bash
rg -n "<query>" 20_项目 30_研究 40_知识库
```

## 输出要求

- 仍返回 `Top1-Top3 + reason + snippet + next_action`
- `mode` 标注为 `fallback`
- 明确提示本次结果来自降级链路

## fix 策略要点

- 目标明确时可跳过 CLI 预检
- 优先 `rg` 定点定位，再用 `obsidian read/backlinks` 验证
- 避免直接跑 `obsidian unresolved verbose`（除非做全库巡检）
