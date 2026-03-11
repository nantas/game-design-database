# Core Experience Principle Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 在仓库中新增一张可复用的“核心体验拆解原则”方法卡，并用它重写 `Slay the Spire 2` 的核心体验相关页面，使结论按证据分层、循环层级和玩家类型承接来表达。

**Architecture:** 先固化方法论，再回到样例游戏重写内容。实现顺序保持“原则卡 -> 证据索引 -> 核心体验页”，避免先写结论再倒找依据。当前阶段默认可使用所有文本来源作为潜在证据池，但正文落库时只保留已回链、已标边界的判断。

**Tech Stack:** Markdown、Obsidian wikilinks、rg、git、现有主卡固定五页结构

---

### Task 1: 建立核心体验重写基线

**Files:**
- Review: `AGENTS.md`
- Review: `90_模板与规范/核心体验模板.md`
- Review: `90_模板与规范/游戏主卡结构规范.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md`

**Step 1: 读取仓库约束与当前样例页**

Run: `sed -n '1,220p' AGENTS.md && printf '\n---\n' && sed -n '1,220p' '90_模板与规范/核心体验模板.md' && printf '\n---\n' && sed -n '1,240p' '90_模板与规范/游戏主卡结构规范.md' && printf '\n---\n' && sed -n '1,260p' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md' && printf '\n---\n' && sed -n '1,280p' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'`
Expected: 明确当前页存在“系统清单代替体验拆解”“证据层级混用”“高峰体验未单列”的问题。

**Step 2: 写下当前重写目标清单**

Expected: 至少确认以下 5 点后再动手：
- 核心体验从宣传可感知、首局可体会的卖点起笔
- 第一印象之后按真实决策-反馈循环逐层展开
- 循环层边界优先由重置点、资源回收点、阶段性结算识别
- 高峰体验与首局体验必须连续但不能混写
- 玩家类型满足路径单独补充，不与循环层次混写

**Step 3: 提交基线笔记**

```bash
git add docs/plans/2026-03-11-core-experience-principle-design.md
git commit -m "docs: add core experience rewrite plan"
```
Expected: 当前计划文件已入库，后续执行以此为准。

### Task 2: 新建原则卡 `80_原则/核心体验拆解原则.md`

**Files:**
- Create: `80_原则/核心体验拆解原则.md`
- Review: `docs/plans/2026-03-11-core-experience-principle-design.md`

**Step 1: 创建 `80_原则` 目录与原则卡 frontmatter**

```md
---
title: 核心体验拆解原则
type: design_principle
tags: [game-design, design-principle, core-experience]
status: draft
---
```

Expected: `80_原则` 目录存在，原则卡从第 1 行开始包含合法 frontmatter。

**Step 2: 按已批准结构写入固定章节**

```md
## 原则定义
## 为什么这样拆
## 拆解步骤
## 层次判定规则
## 玩家类型补充规则
## 证据分层与来源优先级
## 证据要求
## 常见误判
## 参考游戏卡
## 当前校准状态
```

Expected: 章节顺序与已讨论设计一致，不额外扩展无关章节。

**Step 3: 写入已批准正文要点**

Expected: 至少完整覆盖以下内容：
- 核心体验是宣传可传达且首局可体会的核心卖点
- 第一印象之后按真实循环层级展开，不套固定层数模板
- 新循环层由新的决策目标、资源视角、重置点/回收点、策略影响共同定义
- 玩家类型满足路径单列，区分局部满足与完整高峰体验
- 证据按宣传层、结构层、体验层、意图层分层使用
- `wiki` 只能单独支撑结构判断，不能单独推出高确定性体验结论
- `Slay the Spire 2` 作为参考游戏卡链接进入原则卡

**Step 4: 运行最小 Markdown 结构检查**

Run: `rg -n -e '^title:|^type:|^tags:|^status:|^## ' '80_原则/核心体验拆解原则.md'`
Expected: 输出 frontmatter 关键字段与全部二级标题，无重复 key，无缺失章节。

**Step 5: 提交原则卡**

```bash
git add '80_原则/核心体验拆解原则.md'
git commit -m "docs: add core experience principle"
```
Expected: 原则卡单独成提交，便于后续方法论迭代。

### Task 3: 重做 `Slay the Spire 2` 的核心体验证据索引

**Files:**
- Modify: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md`
- Review: `80_原则/核心体验拆解原则.md`

**Step 1: 先重排证据结构，不急着补结论**

Expected: 将证据索引至少重构为以下视角：
- 证据来源清单
- 来源可靠性与用途
- 证据分层（宣传层 / 结构层 / 体验层 / 意图层）
- 证据到结论的映射
- 证据缺口

**Step 2: 把现有 wiki 证据降级到结构层用途**

Expected: 明确写出当前 `wiki` 证据可支撑：
- 系列类型定位
- 可见系统与目录结构
- 角色 / 卡牌 / 遗物 / 地图 / Event Log 等模块存在

Expected: 同时明确写出当前 `wiki` 证据暂不能单独支撑：
- 第一印象卖点强度
- 玩家是否持续感到高价值决策
- 玩家是否实际利用 Event Log 形成复盘学习
- 高峰体验与玩家类型承接

**Step 3: 补录待引入的文本来源槽位**

Expected: 在不伪造内容的前提下，为后续补证保留文本来源方向，例如：
- 官方商店页或官方宣传文案
- 预告片文本信息或可转写内容
- 媒体 preview / hands-on 文章
- 开发者访谈或开发日志

**Step 4: 更新“证据到结论映射”语气强度**

Expected: 把结论重新标为“可确认判断 / 低风险判断 / 待验证判断”或等价表达，避免当前高确定性语气覆盖证据缺口。

**Step 5: 检查主卡证据回链**

Run: `rg -n '证据|待验证|宣传层|结构层|体验层|意图层' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'`
Expected: 证据页中能直接看出来源分工与缺口，不再把目录信息当作体验事实。

**Step 6: 提交证据页修订**

```bash
git add '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'
git commit -m "docs: rebalance slay the spire 2 evidence index"
```
Expected: 证据层修订与原则卡分开提交。

### Task 4: 按原则重写 `Slay the Spire 2 - 核心体验`

**Files:**
- Modify: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md`
- Review: `80_原则/核心体验拆解原则.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md`

**Step 1: 保留模板骨架，重写“这款游戏想让玩家持续获得什么体验”**

Expected: 首段要从 `Slay the Spire 2` 的体验承诺起笔，强调：
- 玩家持续面临高价值决策
- 选择对错会收到明确而强烈的反馈
- 从单回合到整局构筑都在不断放大这种判断压力与收益

Expected: 不再直接使用“Roguelike Deckbuilder”之类类型标签充当核心结论。

**Step 2: 在“关键玩家决策”中按真实循环层级展开**

Expected: 至少检查并区分以下层级是否成立：
- 单回合出牌顺序
- 单场战斗资源规划
- 单层推进与风险管理
- 单局构筑目标

Expected: 每层都要写出：
- 决策对象
- 资源范围
- 可能的重置点或回收点
- 这一层为什么不能被上下层替代

**Step 3: 在“关键反馈循环”中写出层与层之间的传导**

Expected: 明确说明：
- 局部正确出牌如何转化为战斗优势
- 战斗结果如何改变单层资源策略
- 单层决策如何回流到整局构筑目标
- 构筑成型后如何降低随机洗牌对策略执行的干扰

**Step 4: 在“当前判断边界”中显式分层**

Expected: 清楚区分：
- 当前已被结构层证据稳定支撑的部分
- 当前仍需要宣传层 / 体验层 / 意图层补证的部分
- 不把“每日任务模式更适合轻度玩家”写成已确认结论，除非已有对应文本证据

**Step 5: 在“新输入待吸收”中列出下一轮补证方向**

Expected: 待补内容直接对应缺口，例如：
- 商店页 / trailer 文本中的第一印象卖点表达
- 媒体试玩对高价值决策与强反馈的描述
- 模式差异对不同玩家承接的文本证据

**Step 6: 运行页内结构检查**

Run: `rg -n -e '^title:|^type:|^game:|^tags:|^## ' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md'`
Expected: frontmatter 与固定二级标题仍符合模板。

**Step 7: 提交核心体验重写**

```bash
git add '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md'
git commit -m "docs: rewrite slay the spire 2 core experience"
```
Expected: 核心体验页改动单独成提交，便于后续继续校准。

### Task 5: 总体验证与交叉检查

**Files:**
- Review: `80_原则/核心体验拆解原则.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md`
- Review: `10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md`

**Step 1: 跑 Markdown 结构与标题检查**

Run: `rg -n -e '^type:|^tags:|^## ' 10_游戏主卡 80_原则 90_模板与规范`
Expected: 新增/修改文档仍符合仓库固定结构与可检索性要求。

**Step 2: 检查原则卡与样例卡的链接**

Run: `rg -n 'Slay the Spire 2|核心体验拆解原则' 80_原则 '10_游戏主卡/Slay the Spire 2'`
Expected: 原则卡能回链样例卡，样例卡的重写逻辑能被原则卡解释。

**Step 3: 人工复核三类风险**

Expected: 至少逐项确认：
- 是否仍有系统清单冒充体验判断
- 是否仍有高峰体验与首局体验混写
- 是否仍有证据强度与语气强度不匹配

**Step 4: 提交最终校验结果**

```bash
git add '80_原则/核心体验拆解原则.md' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 核心体验.md' '10_游戏主卡/Slay the Spire 2/Slay the Spire 2 - 证据索引.md'
git commit -m "docs: validate core experience principle rollout"
```
Expected: 最终收尾提交只包含验证后必要的小修，不混入无关改动。
