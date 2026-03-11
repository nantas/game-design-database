---
title: "Slay the Spire 2 - 卡片关键词归纳整理"
type: topic_index
tags: [game-design, topic-index, slay-the-spire-2, deckbuilder]
---

# Slay the Spire 2 - 卡片关键词归纳整理

## 范围说明

- 本页基于 [[10_来源/Spire Codex|Spire Codex]] 在 2026-03-11 可公开访问的 `https://www.spire-codex.com/api/keywords` 与 `https://www.spire-codex.com/api/cards` 数据整理。
- 目标是先冻结当前已经进入卡牌 `keywords` 字段的术语，避免把 `power`、`affliction`、`orb` 或一般卡面描述混进同一层。
- 本页只整理“卡片关键词”层，不扩展到角色能力、敌人意图或其他数据库对象。

## 数据快照

- 当前卡牌总数：576。
- 带至少一个关键词的卡牌：147。
- `api/keywords` 返回 8 个条目，其中 7 个在 `cards.keywords` 中实际出现。
- `PERIOD` 当前为空描述，且没有落到任何卡牌 `keywords` 字段，先视为未启用占位项。

## 当前可见关键词清单

### Exhaust

- 定义：打出后会在本场战斗内移出牌组循环。
- 当前卡牌数：92。
- 分布：`colorless:17`、`defect:14`、`necrobinder:12`、`silent:11`、`event:9`、`ironclad:9`、`regent:8`、`token:8`，另有少量 `curse` 与 `status`。
- 代表牌：`Adrenaline`、`Feed`、`Royal Gamble`、`Shiv`。

### Unplayable

- 定义：卡牌不能直接打出。
- 当前卡牌数：25。
- 分布：`curse:16`、`status:6`、`quest:3`。
- 代表牌：`Burn`、`Dazed`、`Bad Luck`、`Byrdonis Egg`。

### Ethereal

- 定义：若回合结束时仍在手牌中，则会被 `Exhaust`。
- 当前卡牌数：16。
- 分布：`necrobinder:8` 最集中，其余分散在 `curse`、`status`、`event`、`defect`、`regent` 与 `token`。
- 代表牌：`Defile`、`Defy`、`Apparition`、`Dying Star`。

### Retain

- 定义：回合结束时不会因常规弃牌而离开手牌。
- 当前卡牌数：11。
- 分布：`necrobinder:5`，其余见于 `colorless`、`token`、`silent` 与 `curse`。
- 代表牌：`Eradicate`、`Reap`、`Sacrifice`、`Purity`。

### Innate

- 定义：每场战斗开始时会直接进入起手。
- 当前卡牌数：9。
- 分布：`silent:3`，`colorless:2`，`curse:2`，另有 `defect` 与 `event` 各 1。
- 代表牌：`Backstab`、`Boot Sequence`、`Mind Blast`、`Suppress`。

### Sly

- 定义：若本回合结束前，这张牌从手牌中被弃掉，则免费自动打出。
- 当前卡牌数：8。
- 分布：全部来自 `silent`。
- 代表牌：`Abrasive`、`Reflex`、`Tactician`、`Untouchable`。

### Eternal

- 定义：不能从牌组中被移除或变形。
- 当前卡牌数：7。
- 分布：`curse:6`，`necrobinder:1`。
- 代表牌：`Ascender's Bane`、`Greed`、`Folly`、`Forbidden Grimoire`。

## 结构观察

- 明显的通用关键词是 `Exhaust`、`Unplayable`、`Ethereal`、`Retain`、`Innate`；它们都跨多个池子出现。
- `Sly` 是当前最明确的角色专属关键词，只出现在 `Silent` 卡池里。这个判断来自当前数据分布，不是官方声明。
- `Eternal` 目前几乎等同于“永久性负担 / 特殊绑定牌”标记，主要附着在 `curse` 上。
- `Unplayable` 目前也强烈偏向负面牌、状态牌与任务物件，而不是正向 build-around 关键词。
- `Ethereal` 和 `Retain` 在 `Necrobinder` 的出现频次都偏高，说明该角色当前更强调“手牌时机窗口”和“保留到合适时点再打”的操作空间。这里是基于分布的归纳，不是站点原文结论。

## 代表牌分组

- 开局型：`Backstab`、`Boot Sequence`、`Mind Blast`、`Suppress`。
- 弃牌联动型：`Abrasive`、`Flick-Flack`、`Reflex`、`Tactician`。
- 负面负担型：`Ascender's Bane`、`Bad Luck`、`Clumsy`、`Dazed`、`Burn`。
- 一次性爆发型：`Adrenaline`、`Feed`、`Fiend Fire`、`Royal Gamble`。

## 异常与后续关注

- `PERIOD` 已出现在 `api/keywords`，但当前没有描述文本，也没有对应卡牌实例；后续如果站点补全，需要重新核对它究竟是正式关键词、解析占位符，还是数据残留。
- 本页只冻结“当前公开数据库里已经落到卡牌字段”的关键词，不代表抢先体验或后续版本的最终全集。
- 若后续要继续扩展，优先方向是补一张“关键词对应代表牌与角色 archetype”对照页，而不是直接升格为 `40_设计模式/`。

## 相关链接

- 来源页：[[10_来源/Spire Codex|Spire Codex]]
- 关键接口：`https://www.spire-codex.com/api/keywords`
- 关键接口：`https://www.spire-codex.com/api/cards`
