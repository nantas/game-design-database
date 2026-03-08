# 第二来源验证 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 选择一个非 Deconstructor of Fun 的第二来源，验证来源页、网页卡、设计模式卡与导入流程是否可复用，并在必要时以最小改动修复兼容问题。

**Architecture:** 先基于现有抽取器的页面假设评估多个真实候选来源，再用真实 URL 在临时目录执行导入验证。若发现兼容问题，仅对抽取逻辑做小范围回退扩展，并优先补真实 HTML fixture 与对应测试，最后把成功样例落入仓库内容层。

**Tech Stack:** Python 3.11、BeautifulSoup4、pytest、uv、Markdown/Obsidian

---

### Task 1: 基线检查与候选来源评估

**Files:**
- Review: `AGENTS.md`
- Review: `README.md`
- Review: `src/game_design_patterns/html_extract.py`
- Review: `src/game_design_patterns/importer.py`
- Review: `tests/test_article_extract.py`
- Review: `tests/test_cli_import.py`

**Step 1: 检查当前分支与工作区状态**

Run: `but status --json`
Expected: 工作区干净，可安全开始本次验证。

**Step 2: 评估 2-3 个真实候选来源**

Run: `curl -L -A 'Mozilla/5.0' '<url>'`
Expected: 拿到可读 HTML，并识别标题、站点名、正文容器与作者/时间线索。

**Step 3: 选定低风险来源**

Expected: 选定一个正文静态可抓取、结构稳定、内容适合沉淀为模式卡的来源。

### Task 2: 先验证失败，再补测试

**Files:**
- Create: `tests/fixtures/game_design_skills_core_loop.html`
- Modify: `tests/test_article_extract.py`
- Modify: `tests/test_cli_import.py`

**Step 1: 用真实 URL 在临时目录跑导入**

Run: `uv run python tools/import_url.py '<url>' --vault-root '<tmpdir>' --imported-at 2026-03-08`
Expected: 若摘要/证据为空，确认问题位于正文抽取层。

**Step 2: 添加失败测试**

Expected: 新 fixture 与测试能稳定复现“新来源正文未被抽出”的问题。

**Step 3: 运行最小测试确认失败**

Run: `uv run pytest tests/test_article_extract.py -v`
Expected: 新增用例失败，且失败原因与正文/作者/日期抽取缺口一致。

### Task 3: 做最小兼容修复

**Files:**
- Modify: `src/game_design_patterns/html_extract.py`

**Step 1: 扩展通用正文容器回退**

Expected: 在保持 Deconstructor of Fun 现有行为不变的前提下，支持至少一种非 Squarespace 正文容器。

**Step 2: 视需要补作者/发布时间回退**

Expected: 新来源可抽到稳定作者与发布日期，避免依赖页面更新时间。

**Step 3: 回跑最小测试**

Run: `uv run pytest tests/test_article_extract.py tests/test_cli_import.py -v`
Expected: 新旧用例均通过。

### Task 4: 落库第二来源样例

**Files:**
- Create: `10_来源/<第二来源>.md`
- Create: `30_网页卡/<网页标题>.md`
- Create: `40_设计模式/<模式名>.md`
- Modify: `README.md`（仅在必要时）

**Step 1: 用真实 URL 导入到仓库根目录**

Run: `uv run python tools/import_url.py '<url>' --imported-at 2026-03-08`
Expected: 自动生成网页卡与模式卡。

**Step 2: 人工整理来源页与模式卡**

Expected: 来源页、网页卡、模式卡形成双向链接与中文说明闭环。

### Task 5: 验证与收尾

**Files:**
- Review: `tests/`
- Review: `README.md`

**Step 1: 跑相关最小测试**

Run: `uv run pytest tests/test_article_extract.py tests/test_cli_import.py -v`
Expected: 相关行为全部通过。

**Step 2: 跑全量测试**

Run: `uv run pytest tests -v`
Expected: 全量通过。

**Step 3: 检查 Markdown 结构**

Run: `rg -n -e '^type:|^aliases:|^## ' 10_来源 20_入口页 30_网页卡 40_设计模式`
Expected: 新增内容符合固定结构与可检索性要求。
