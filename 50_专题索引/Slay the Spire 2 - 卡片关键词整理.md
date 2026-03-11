---
title: "Slay the Spire 2 - 卡片关键词整理"
type: topic_index
tags: [game-design, topic-index, slay-the-spire-2, glossary]
---

# Slay the Spire 2 - 卡片关键词整理

## 范围说明

- 本页整理截至 `2026-03-11` 可公开核对的《Slay the Spire 2》卡片关键词，目标是统一命名、释义和后续检索入口。
- 优先收录会直接出现在卡面或官方角色介绍里的词；`Quests`、`Enchantments`、`Afflictions` 这类相关系统术语单列处理。
- 本页是人工整理的专题索引，不替代游戏内词典，也不直接升格为 `40_设计模式/`。

## 主要来源

- 主参考：[[10_来源/Mobalytics|Mobalytics]] 的 [Slay the Spire 2 Keywords Explained](https://mobalytics.gg/slay-the-spire-2/guides/keywords)
- 官方交叉校验：
  - [The Neowsletter Issue 7](https://megacrit.com/news/2025-2-12-neowsletter-issue-7/)：`Enchantments`
  - [The Neowsletter Issue 8](https://megacrit.com/news/2025-3-12-neowsletter-issue-8/)：`Quests`
  - [The Neowsletter Issue 9](https://megacrit.com/news/2025-4-15-neowsletter-issue-9/)：`Afflictions`
  - [The Neowsletter Issue 10](https://megacrit.com/news/2025-5-15-neowsletter-issue-10/)：`Sly`
  - [The Neowsletter Issue 15](https://megacrit.com/news/2025-10-16-neowsletter-issue-15/)：`Summon`、`Doom`
  - [The Neowsletter Issue 17](https://megacrit.com/news/2025-12-11-neowsletter-issue-17/)：`Forge`

## 使用约定

- 主词条统一保留英文原词，中文只做最小必要释义；后续若建卡，文件名优先使用英文主词条。
- 先把“通用关键词”“角色专属新词”“相关系统术语”分开，避免后续把所有战斗词都混成同一层。
- 下列释义只保留检索和辨识所需信息，不展开 build 推荐或精确数值。

## 通用关键词

- `Artifact`：抵消下一次施加到自身的负面状态。
- `Block`：当前战斗回合里用于吸收伤害的护甲值。
- `Channel`：生成并放入一个 Orb。
- `Confused`：手牌费用会被随机改写。
- `Curse`：负面卡牌，通常会污染抽牌或限制操作。
- `Dark`：会随回合增长、被 `Evoke` 时爆发的 Orb。
- `Dexterity`：影响 `Block` 产出的属性。
- `Energy`：出牌资源。
- `Ethereal`：若回合结束时仍在手中，会被 `Exhaust`。
- `Evoke`：触发 Orb 的离场效果。
- `Exhaust`：把卡移出本场战斗循环。
- `Focus`：影响 Orb 效果强度的属性。
- `Frost`：偏防御向的 Orb。
- `Innate`：开局必定进入起始手牌。
- `Intangible`：把受到的伤害压到极低值。
- `Lightning`：偏伤害向的 Orb。
- `Plasma`：偏能量向的 Orb。
- `Poison`：按层数持续结算的伤害型负面状态。
- `Retain`：回合结束后继续留在手中。
- `Ritual`：会持续提高 `Strength` 的增益。
- `Status`：战斗中生成的杂质牌或负担牌。
- `Strength`：提高攻击伤害的属性。
- `Thorns`：受到攻击时反弹伤害。
- `Unplayable`：不能直接打出的卡。
- `Vulnerable`：会承受更多攻击伤害。
- `Weak`：攻击造成的伤害下降。

## 角色专属或明显新词

- `Doom`：`The Necrobinder` 相关负面状态；当目标的 `Doom` 达到或超过其当前生命值时，会在其回合结束时死亡。
- `Forge`：`The Regent` 相关关键词；每场战斗首次 `Forge` 会生成对应的 `Sovereign Blade`，后续 `Forge` 会继续提高这把剑的伤害。
- `Sly`：`The Silent` 的新关键词；带 `Sly` 的牌被弃掉时会免费自动打出。
- `Summon`：`The Necrobinder` 的核心动作；主要用于提高 `Osty` 的生命值，或在其死亡后重新召回。

## 相关系统术语

- `Quests`：官方定义的全新卡牌类型；拿到后需要满足各自条件，完成时会给出高价值回报。
- `Enchantments`：施加在牌组卡牌上的 run-long modifier，会持续整个 run。
- `Afflictions`：由敌人施加到卡牌上的负面 modifier，更像“被污染的卡牌状态”而不是通常意义上的战斗 Buff / Debuff。

## 当前分层判断

- 可以直接当“卡片关键词”检索的，当前以 `Mobalytics` 关键词页列出的 30 个词为主。
- `Doom`、`Forge`、`Sly`、`Summon` 虽然也可视为关键词，但更适合在后续按角色拆分时单独维护。
- `Quests`、`Enchantments`、`Afflictions` 更像系统层术语，不建议和常规卡面关键词混排到同一清单。

## 后续动作建议

- 若后续导入官方卡牌数据库或稳定 wiki，可把本页拆成“通用关键词总表 + 角色专属关键词页”。
- 当前阶段不新建 `40_设计模式/`，因为这些词是规则术语而非可复用设计模式。
- 后续新增条目时，优先沿用本页的英文主词条，避免出现 `Sly/狡诈`、`Summon/召唤` 这类并行命名。
