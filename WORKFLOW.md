---
active_states:
  - Todo
terminal_states:
  - Done
hooks:
  after_create: []
  before_run:
    - uv sync
  after_run:
    - uv run pytest tests -q
  before_remove: []
retry_policy:
  max_attempts: 3
  backoff_seconds: 60
pr_policy:
  require_pr: true
completion_policy:
  close_issue_on_merge: true
---
# Repository Workflow

先阅读仓库根目录的 `AGENTS.md`，严格遵守其中的语言、测试、目录职责和提交约束。

当前任务：

- Issue: `{{issue_identifier}}`
- 标题: `{{issue_title}}`
- 当前状态: `{{issue_state}}`

任务说明：

{{issue_description}}

执行要求：

- 先确认改动边界，只修改完成任务所需的文件。
- 如涉及行为变更，优先补测试后做最小实现。
- 若需要创建 PR，按仓库当前 Git remote / branch 工作流执行。
- 若任务不要求 PR，则以本地验证通过与结果可解释为完成标准。
- 完成后确保工作区可提交，并给出清晰总结。
