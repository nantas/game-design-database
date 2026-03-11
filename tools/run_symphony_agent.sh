#!/bin/sh

set -eu

prompt_input="${PROMPT:-}"

if [ -z "$prompt_input" ]; then
  printf '%s\n' '{"status":"failed","summary":"missing_prompt","branch_name":null,"commit_sha":null,"requested_next_action":"provide_prompt"}'
  exit 0
fi

tmpdir="$(mktemp -d)"
last_message_file="$tmpdir/codex-last-message.txt"
codex_log="$tmpdir/codex.log"
test_log="$tmpdir/pytest.log"

cleanup() {
  rm -rf "$tmpdir"
}

trap cleanup EXIT INT TERM

branch_name="$(git branch --show-current)"
commit_sha="$(git rev-parse HEAD)"

if [ "$prompt_input" = "test prompt" ]; then
  codex_prompt="先阅读 AGENTS.md。不要修改任何文件，不要提交，只输出一句简短中文总结说明仓库已检查完毕。"
else
  codex_prompt="先阅读仓库根目录的 AGENTS.md 并严格遵守。请在当前工作区内完成以下任务，只做最小必要改动，运行必要验证，并在完成后提交改动：\n\n$prompt_input"
fi

if ! uv sync >"$tmpdir/uv-sync.log" 2>&1; then
  printf '{"status":"failed","summary":"uv_sync_failed","branch_name":"%s","commit_sha":"%s","requested_next_action":"inspect_uv_sync"}\n' "$branch_name" "$commit_sha"
  exit 0
fi

if ! codex exec \
  --cd "$PWD" \
  --dangerously-bypass-approvals-and-sandbox \
  --output-last-message "$last_message_file" \
  --color never \
  "$codex_prompt" >"$codex_log" 2>&1; then
  printf '{"status":"failed","summary":"codex_failed","branch_name":"%s","commit_sha":"%s","requested_next_action":"inspect_codex_log"}\n' "$branch_name" "$commit_sha"
  exit 0
fi

if ! uv run pytest tests -q >"$test_log" 2>&1; then
  printf '{"status":"failed","summary":"tests_failed","branch_name":"%s","commit_sha":"%s","requested_next_action":"inspect_test_log"}\n' "$branch_name" "$commit_sha"
  exit 0
fi

branch_name="$(git branch --show-current)"
commit_sha="$(git rev-parse HEAD)"

printf '{"status":"success","summary":"implemented","branch_name":"%s","commit_sha":"%s","requested_next_action":null}\n' "$branch_name" "$commit_sha"
