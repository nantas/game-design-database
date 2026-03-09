---
title: "Postmortem: Irrational Games' System Shock 2"
type: web_note
source: "awesome-game-design"
url: "https://web.archive.org/web/20190325062431/http://www.gamasutra.com/view/feature/3406/postmortem_irrational_games_.php"
author: "Jonathan Chey"
published_at: 1999-12-07
imported_at: 2026-03-09
tags: ["game-design", "web-note", "postmortem", "awesome-list", "web-archive"]
---

# Postmortem: Irrational Games' System Shock 2

## 内容摘要
- 这是 Jonathan Chey 在 Gamasutra 发表的多页 postmortem，经 Wayback 访问；正文不只是项目管理复盘，还明确讨论了技术约束如何塑造系统设计。
- 第 2 页把 `designed to our technology` 说成核心方法，说明团队先分析可用技术，再反推适配的设计，而不是先画理想系统再强逼引擎追赶。
- 同页把 `simple, reusable game-play elements` 作为成功经验，拿 security camera / security system 举例，说明团队用可重复组合的低成本系统生成大量关卡玩法。
- 同页还明确写到为了降低前作门槛而重做界面，并解释为何继续放弃互动式 NPC，说明它既在谈关卡机制，也在谈续作的可进入性与叙事载体取舍。

## 来源关联
- [[10_来源/awesome-game-design|awesome-game-design]]

## 提炼出的设计模式
- 本轮只保留候选线索，不新建模式卡；筛查结论见 [[50_专题索引/awesome-game-design - 初始分诊策略|awesome-game-design - 初始分诊策略]]。

## 关键证据
- 第 2 页：作者明确写到团队采用 `designed to our technology`，先分析技术能力，再选择能落在现有引擎上的设计方向，并指出偏离这一原则时往往会出问题。
- 第 2 页：`simple, reusable game-play elements` 一节直接说明他们放弃高成本脚本序列，转而围绕简单可复用系统组织玩法。
- 第 2 页：security camera / security system 例子详细解释了摄像头如何触发怪物、迫使玩家潜行或先破坏装置，再把关闭安全系统的终端散布到关卡里，足以支撑可复述的系统设计判断。
- 第 2 页：作者写到续作为了更广泛受众而保留深度但简化前作界面，并通过双模态界面平衡鼠标视角与背包管理。
- 第 2 页：作者解释继续取消互动 NPC，是因为当时技术仍不足以支撑可信且有趣的互动，因此改用语音日志和邮件承载背景信息。

## 我的备注
- 首轮判定为“通过筛查”，因为正文已经明确覆盖系统复用、界面取舍和叙事载体选择，不是单纯的制作回忆。
- 入口 URL 是 Wayback 归档页；导入器没有稳定抽出正文，本轮依据同一资源的第 1 至 3 页做了人工复核，并刻意避开了 archive banner 与站点噪声。
