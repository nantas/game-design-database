# Design Pattern Principle Co-Creation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 基于现有 `Slay the Spire 2` 数据源，采用“用户共创确认 + 小批次归纳”方式建立 `设计模式拆解原则` 初版，并回写到游戏卡固定五页结构内。

**Architecture:** 先以 `核心体验` 为锚点抽取系统/机制/内容候选，再按“当前游戏内可扩产复刻”规则筛选模式。模式归纳采用每轮 3 条候选并由用户裁决，避免早期过度抽象与噪声。原则文档只沉淀已确认规则，允许形成“母模式 + 并列模式 + 细化方向”的模式簇结构，并明确后续需通过多游戏卡持续校准，不一次性定稿模板。

**Tech Stack:** Obsidian Markdown、obsidian-cli、rg、git

---

### Task 1: 建立 StS2 候选归纳基线

**Files:**
- Review: `AGENTS.md`
- Review: `80_原则/核心体验拆解原则.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 设计模式.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 游戏内容.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md`

**Step 1: 读取当前约束与样例页面**

Run: `sed -n '1,260p' AGENTS.md && printf '\n---\n' && sed -n '1,220p' '80_原则/核心体验拆解原则.md' && printf '\n---\n' && sed -n '1,260p' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md' && printf '\n---\n' && sed -n '1,220p' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 设计模式.md' && printf '\n---\n' && sed -n '1,220p' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 游戏内容.md' && printf '\n---\n' && sed -n '1,320p' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'`
Expected: 明确“设计模式页结论化、内容页未系统回链、证据缺口仍在”的现状。

**Step 2: 固化本轮归纳口径（不改模板）**

Expected:
- 只从支撑核心体验的系统/机制/内容提炼模式。
- 可复刻判断以“当前游戏内可扩产”优先。
- 早期每轮只讨论 3 条候选，由用户裁决。
- 不新增“反模式”章节到设计模式页。

**Step 3: 提交基线计划**

```bash
git add docs/plans/2026-03-13-design-pattern-principle-co-creation-design.md
git commit -m "docs: add co-creation plan for design pattern principle"
```

### Task 2: 建立候选模式工作台（仅内部归纳）

**Files:**
- Create: `docs/plans/2026-03-13-sts2-pattern-candidate-workbench.md`

**Step 1: 创建候选工作台骨架**

```md
# STS2 Pattern Candidate Workbench

## 使用规则
- 每轮最多 3 条候选
- 每条必须回链核心体验锚点
- 每条必须标注可复刻性（当前游戏内）
- 每条必须标注证据强度（可确认/低风险/待验证）

## 候选池
### 候选 A
- 核心体验锚点：
- 机制/内容条目：
- 可复刻性判断：
- 证据映射：
- 用户裁决：

### 候选 B
...

### 候选 C
...
```

**Step 2: 写入首轮三条候选（A/B/C）**

Expected:
- A 为已确认母模式（分层循环可学习性）。
- B 与 C 按用户裁决标注“暂不纳入/跳过”。
- 后续轮次允许新增并列模式与细化方向，不强行套单树状子模式结构。
- 保留理由，不删除记录。

**Step 3: 校验结构**

Run: `rg -n -e '^#|^##|^###|^- ' 'docs/plans/2026-03-13-sts2-pattern-candidate-workbench.md'`
Expected: 可见规则区与 A/B/C 三条候选结构。

**Step 4: 提交工作台**

```bash
git add 'docs/plans/2026-03-13-sts2-pattern-candidate-workbench.md'
git commit -m "docs: add sts2 pattern candidate workbench"
```

### Task 3: 回写 StS2 设计模式页（仅已确认模式）

**Files:**
- Modify: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 设计模式.md`

**Step 1: 删除未确认模式的确定性表述**

Expected:
- 暂不保留 B/C 的确定性语句。
- 待验证条目保留在“待验证模式线索”，但不作为模式清单主体。

**Step 2: 写入母模式定义与作用**

Expected:
- 写入“分层循环可学习性模式”定义。
- 强调“无无意义选择 + 可控代价学习 + 全程强反馈”。
- 当样例已确认并列模式时，允许在同页扩展模式簇成员与细化方向。
- 保留可迁移性判断为“当前游戏内可扩产成立，跨游戏待校准”。

**Step 3: 结构检查**

Run: `rg -n -e '^title:|^type:|^game:|^tags:|^## ' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 设计模式.md'`
Expected: frontmatter 与模板章节完整。

**Step 4: 提交设计模式页**

```bash
git add '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 设计模式.md'
git commit -m "docs: refocus sts2 design patterns on confirmed mother pattern"
```

### Task 4: 回写游戏内容页与证据索引的模式回链

**Files:**
- Modify: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 游戏内容.md`
- Modify: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md`

**Step 1: 在游戏内容页标注“模式归属/未归属”**

Expected:
- 大部分内容条目标注回链到已确认模式。
- 例外条目标注为“暂不归入模式（待验证或独立判例）”。

**Step 2: 在证据索引中补充“模式证据映射”**

Expected:
- 每条模式结论回链对应证据条目。
- 标注证据强度，不抬高语气。

**Step 3: 运行检查**

Run: `rg -n '模式|回链|待验证|可确认|低风险' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 游戏内容.md' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'`
Expected: 可直接检索到模式回链与证据强度标签。

**Step 4: 提交回链修订**

```bash
git add '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 游戏内容.md' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'
git commit -m "docs: add sts2 content-to-pattern backlinks and evidence mapping"
```

### Task 5: 新建设计模式拆解原则（共创迭代版）

**Files:**
- Create: `80_原则/设计模式拆解原则.md`

**Step 1: 创建 frontmatter**

```md
---
title: 设计模式拆解原则
type: design_principle
tags: [game-design, design-principle, design-patterns]
status: draft
---
```

**Step 2: 写入固定章节**

```md
## 这份原则解决什么问题
## 最小执行流程
## 模式准入规则
## 模式层级关系
## 与游戏内容/证据索引的回链规则
## 用户共创确认机制
## 当前校准状态
```

**Step 3: 写入已确认规则**

Expected:
- 子模式门槛：同一游戏内至少两个不同机制/内容条目共同指向。
- 单条强证据需用户确认。
- 反模式不进设计模式页。
- 允许 `母模式 / 并列模式 / 细化方向` 共存，不要求所有条目强行变成父子树。
- 该原则必须通过多游戏卡继续迭代，不在首样例定稿。

**Step 4: 结构检查**

Run: `rg -n -e '^title:|^type:|^tags:|^status:|^## ' '80_原则/设计模式拆解原则.md'`
Expected: frontmatter 与章节齐全，无重复 key。

**Step 5: 提交原则初稿**

```bash
git add '80_原则/设计模式拆解原则.md'
git commit -m "docs: add draft design pattern decomposition principle"
```

### Task 6: 总体验证与收口

**Files:**
- Review: `80_原则/设计模式拆解原则.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 设计模式.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 游戏内容.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md`

**Step 1: 跑结构与标题检查**

Run: `rg -n -e '^type:|^tags:|^## ' 10_游戏主卡 80_原则 90_模板与规范`
Expected: 页面结构仍与仓库约束一致。

**Step 2: 跑主卡链路检查**

Run: `rg -n '设计模式拆解原则|设计模式|游戏内容|证据索引|回链' '80_原则' '10_游戏主卡/Slay the Spire 2'`
Expected: 原则与样例卡之间存在清晰回链。

**Step 3: 提交收口小修**

```bash
git add '80_原则/设计模式拆解原则.md' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 设计模式.md' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 游戏内容.md' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'
git commit -m "docs: validate sts2-backed design pattern principle draft"
```

## 备注

- 在形成至少 3 个不同游戏卡样例前，不修改 `90_模板与规范/设计模式模板.md`。
- 每轮候选讨论保持 3 条，避免噪声和早收敛。
