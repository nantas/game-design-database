---
title: "Prince of Persia 2 - Design Bible"
type: web_note
source: "awesome-game-design"
url: "https://www.popot.org/documentation/documents/1991-08-08_PoP2_Design_Bible.pdf"
author: ""
published_at: ""
imported_at: 2026-03-09
tags: ["game-design", "web-note", "pdf", "awesome-list"]
---

# Prince of Persia 2 - Design Bible

## 内容摘要
- 这份 PDF 是关卡、分镜、动画与交互说明混合在一起的 design bible，虽然扫描噪声较高，但仍能回收到具体的关卡设计判断。
- 第 81 页把一段水池通行写成“practice session”，说明它不是单纯的场景描写，而是在先教玩家掌握水中移动和出水后的状态反馈。
- 第 82 页继续列出 water shimmer、water level rising、ripples、splash 等特殊效果，说明水域交互被当成一个需要完整视听反馈支持的机制段落。
- 第 121 至 122 页明确写到 throne room 暂时不能直接进入，玩家必须改走下方迷宫，并说明 broken sword 会让未来所有战斗都只造成半点伤害，表现出路线绕行与持续性代价设计。

## 来源关联
- [[10_来源/awesome-game-design|awesome-game-design]]

## 提炼出的设计模式
- 本轮只保留候选线索，不新建模式卡；筛查结论见 [[50_专题索引/awesome-game-design - 初始分诊策略|awesome-game-design - 初始分诊策略]]。

## 关键证据
- 第 81 页 OCR：可识别到 `Crossing the water poses no particular difficulty` 与 `this is merely a practice session`，可支撑“先用低风险场景教学，再在后续放大难度”的判断。
- 第 82 页 OCR：列出 `Surface of water shimmers`、`Water level rising`、`Water ripples`、`Splash`、`Puddle-splashing` 等效果，说明该机制段需要专门反馈设计。
- 第 121 页 OCR：可识别到 `You would like to enter the room`、`for now`、`labyrinth of passageways beneath`、`snakes and ... guards`，说明关卡通过绕路和敌人布置制造门禁。
- 第 122 页 OCR：可识别到 `broken sword`、`half a point of damage`、`applies to all your future opponents`，说明装备损伤会跨后续战斗持续生效。
- 第 165 页 OCR：可识别到 Jaffar 制造假象、房间消失并把 Prince 转移到新地点，说明场景切换与叙事机关是联动设计的一部分。

## 我的备注
- 原始 PDF 为扫描件，正文依据本地 OCR 复核；整份文档并不适合逐页直接引用，但关键页足以建立首轮证据卡。
- 首轮判定为“通过筛查”，但若后续要继续做候选模式归并，仍需要补读更多页面做人工复核。
