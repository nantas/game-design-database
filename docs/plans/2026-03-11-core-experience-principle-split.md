# Core Experience Principle Split Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 将 `80_原则/核心体验拆解原则.md` 重构为短主文档加 5 个按需读取的细节页，降低 agent 默认装载的上下文体积，同时保留明确的继续阅读索引。

**Architecture:** 保留原主文档作为唯一入口，但把长解释迁移到 `80_原则/核心体验拆解原则/` 子目录下的主题细节页。实现顺序采用“先建细节页，再收缩主文档，再验证链接与结构”的方式，避免迁移过程中出现内容丢失或悬空链接。

**Tech Stack:** Markdown、Obsidian wikilinks、rg、git

---

### Task 1: 建立拆分基线与迁移映射

**Files:**
- Review: `80_原则/核心体验拆解原则.md`
- Review: `docs/plans/2026-03-11-core-experience-principle-split-design.md`

**Step 1: 读取当前长文与设计文档**

Run: `sed -n '1,260p' '80_原则/核心体验拆解原则.md' && printf '\n---\n' && sed -n '1,260p' 'docs/plans/2026-03-11-core-experience-principle-split-design.md'`
Expected: 明确当前长文的章节内容和未来 5 个子页的承载边界。

**Step 2: 写下迁移映射清单**

Expected: 至少确认以下映射：
- `原则定义 + 为什么这样拆 + 精简步骤` -> `01_快速执行.md`
- `层次判定规则` -> `02_循环层级判定.md`
- `玩家类型补充规则` -> `03_玩家类型补充.md`
- `证据分层与来源优先级 + 证据要求` -> `04_证据分层与写作边界.md`
- `常见误判` -> `05_常见误判.md`
- `参考游戏卡 + 当前校准状态 + 短摘要` -> 保留在主文档

**Step 3: 提交实现基线计划**

```bash
git add docs/plans/2026-03-11-core-experience-principle-split.md
git commit -m "docs: add core experience principle split plan"
```
Expected: 实现计划单独入库，作为执行基线。

### Task 2: 创建细节页目录与 5 个子文档

**Files:**
- Create: `80_原则/核心体验拆解原则/01_快速执行.md`
- Create: `80_原则/核心体验拆解原则/02_循环层级判定.md`
- Create: `80_原则/核心体验拆解原则/03_玩家类型补充.md`
- Create: `80_原则/核心体验拆解原则/04_证据分层与写作边界.md`
- Create: `80_原则/核心体验拆解原则/05_常见误判.md`

**Step 1: 创建子目录与统一 frontmatter**

Expected: 每个子文档都包含：
- `title`
- `type: design_principle_detail`
- `tags`
- `parent: [[80_原则/核心体验拆解原则]]`

**Step 2: 写入每个子页的“适用场景”章节**

Expected: 每页开头都明确说明“什么时候需要继续读这页”。

**Step 3: 写入主题内容**

Expected:
- `01_快速执行.md` 只保留快速开始需要的定义、步骤、最低输出要求
- `02_循环层级判定.md` 只保留循环边界、重置点、传导关系
- `03_玩家类型补充.md` 明确“默认不主动做玩家分层，只有证据提示时才深入”
- `04_证据分层与写作边界.md` 只保留来源分层、结论强度、最低写作检查
- `05_常见误判.md` 只保留误判清单、自检问题与回读链接

**Step 4: 运行结构检查**

Run: `rg -n -e '^title:|^type:|^tags:|^parent:|^## ' '80_原则/核心体验拆解原则'`
Expected: 5 个子文档都包含统一 frontmatter 和至少一个二级标题。

**Step 5: 提交子文档创建**

```bash
git add '80_原则/核心体验拆解原则'
git commit -m "docs: add core experience principle detail pages"
```
Expected: 细节页作为独立提交，便于单独回滚或调整。

### Task 3: 收缩主文档为短入口索引

**Files:**
- Modify: `80_原则/核心体验拆解原则.md`
- Review: `80_原则/核心体验拆解原则/01_快速执行.md`
- Review: `80_原则/核心体验拆解原则/02_循环层级判定.md`
- Review: `80_原则/核心体验拆解原则/03_玩家类型补充.md`
- Review: `80_原则/核心体验拆解原则/04_证据分层与写作边界.md`
- Review: `80_原则/核心体验拆解原则/05_常见误判.md`

**Step 1: 保留主文档 frontmatter 与标题**

Expected: 不改动主文档的 `title`、`type`、`tags`、`status`，保持它仍是原则入口。

**Step 2: 将正文压缩为 5 个章节**

Expected: 主文档只保留：
- `## 这份原则解决什么问题`
- `## 最小执行流程`
- `## 何时继续读取细节`
- `## 参考游戏卡`
- `## 当前校准状态`

**Step 3: 为每个子页写明确的读取触发条件**

Expected: 主文档中的每条链接都带条件，例如：
- 当你只需要快速开始拆一个新游戏时，先读 `01_快速执行.md`
- 当你不确定某一层循环是否应该单独成层时，继续读 `02_循环层级判定.md`
- 当证据明确提示存在玩家分层问题时，继续读 `03_玩家类型补充.md`
- 当你不确定证据够不够、或该用什么来源时，继续读 `04_证据分层与写作边界.md`
- 当你已经写完一稿，想排查典型错误时，继续读 `05_常见误判.md`

**Step 4: 保留参考游戏卡与校准状态摘要**

Expected: 主文档仍保留 `Slay the Spire 2` 链接和已知有效点 / 待校准点的短摘要，但不再保留长解释。

**Step 5: 检查主文档长度与结构**

Run: `wc -l '80_原则/核心体验拆解原则.md' && rg -n -e '^title:|^type:|^tags:|^status:|^## ' '80_原则/核心体验拆解原则.md'`
Expected: 主文档行数显著低于原版本，且结构只剩 5 个二级标题。

**Step 6: 提交主文档收缩**

```bash
git add '80_原则/核心体验拆解原则.md'
git commit -m "docs: slim core experience principle entry"
```
Expected: 主文档瘦身与子页创建分开提交。

### Task 4: 验证链接、结构与上下文装载优化目标

**Files:**
- Review: `80_原则/核心体验拆解原则.md`
- Review: `80_原则/核心体验拆解原则/`

**Step 1: 检查主文档到子页的链接**

Run: `rg -n '\[\[80_原则/核心体验拆解原则/' '80_原则/核心体验拆解原则.md'`
Expected: 主文档包含指向 5 个子页的明确链接。

**Step 2: 检查子页回链主文档**

Run: `rg -n '\[\[80_原则/核心体验拆解原则\]\]' '80_原则/核心体验拆解原则'`
Expected: 5 个子页都带有 `parent` 回链。

**Step 3: 检查玩家分层噪音边界已落文**

Run: `rg -n '默认不主动|证据明确提示|噪音' '80_原则/核心体验拆解原则/03_玩家类型补充.md'`
Expected: 页面中能直接看出“玩家分层不是默认必写项”的边界。

**Step 4: 人工检查上下文优化目标是否达成**

Expected: 至少确认：
- 主文档可作为默认装载入口
- 子页标题与适用场景足够清楚
- agent 不需要一次性读完整方法论才能开始工作

**Step 5: 提交最终验证结果**

```bash
git add '80_原则/核心体验拆解原则.md' '80_原则/核心体验拆解原则'
git commit -m "docs: validate core experience principle split"
```
Expected: 收尾提交只包含验证后必要的小修。

### Task 5: 仓库级 Markdown 检查

**Files:**
- Review: `80_原则/`

**Step 1: 跑结构检查**

Run: `rg -n -e '^type:|^tags:|^## ' 80_原则`
Expected: 新增文档均符合仓库 Markdown 检索结构。

**Step 2: 检查工作区状态**

Run: `git status --short`
Expected: 只包含本次拆分相关文档改动，无无关变更。

**Step 3: 记录最终交付边界**

Expected: 最终结果只涉及原则文档拆分，不修改游戏主卡内容。
