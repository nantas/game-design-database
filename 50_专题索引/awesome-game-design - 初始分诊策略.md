---
title: "awesome-game-design - 初始分诊策略"
type: topic_index
tags: [game-design, topic-index, awesome-list, triage]
---

# awesome-game-design - 初始分诊策略

## 定位说明

- 本页基于 [[20_入口页/awesome-game-design - README|awesome-game-design - README]] 当前冻结的 README 结构整理。
- `awesome-game-design` 在本仓库中只作为定向来源与入口页处理；README 自身不是直接设计模式证据。
- 本页的目标是先把 README 内部链接做路由与优先级划分，避免把整张 awesome list 误当成“可直接抽模式的网页卡”。

## 链接类型路由

### 路由 A：已上线游戏的 GDD / design bible / pitch 文档

- 适用区块：`Finished games GDDs`
- 路由方式：优先作为高价值候选导入；后续逐条判断是进入 `30_网页卡/`，还是先补来源说明。
- 处理原则：优先选择已上线游戏、可直接访问、文档完整度较高、能看到系统/循环/关卡/经济等设计信息的材料。

### 路由 B：文本型 postmortem 与开发复盘

- 适用区块：`Postmortems`
- 路由方式：纳入高价值候选主队列，但优先文本正文，不优先视频与播放列表。
- 处理原则：优先挑选明确讨论设计决策、取舍、失败原因与系统演化的复盘，而不是纯商业或制作管理总结。

### 路由 C：理论、框架、博客与 wiki 入口

- 适用区块：`Learning materials`
- 路由方式：进入“理论 / 框架队列”，先作为来源页或入口页处理，不直接当模式证据。
- 处理原则：这类链接更适合补术语、框架与分析视角；只有在后续具体文章具备足够正文证据时，才进入网页卡层。

### 路由 D：模板、工具与泛开发资源

- 适用区块：`Templates and examples`、`GDD Creation Tools`、`Game design tools`、`Game development`
- 路由方式：默认排除出本轮主队列，不进入模式沉淀工作流。
- 处理原则：这些资源最多作为工作流或资料背景参考，不应和游戏设计模式证据混在同一批次里处理。

### 路由 E：视频、播放列表与无稳定正文资源

- 适用区块：GDC Vault 视频、YouTube 播放列表、无公开正文的条目
- 路由方式：默认延后；除非后续明确需要，否则不进入当前导入主线。
- 处理原则：当前阶段优先文本与可引用正文，避免在缺少稳定文本载体时制造低质量网页卡。

## 三个执行队列

### 高价值候选队列

- 目标：先筛出最可能产生高质量 `30_网页卡/` 的一手或强复盘材料。
- 纳入条件：已上线游戏、文本可访问、对象明确、预计能提炼出具体设计对象与设计判断。
- 当前首批候选：
  - Monaco
  - Id Doom
  - Prince of Persia 2
  - Condor's Diablo 1
  - Grim Fandango
  - Balatro Timeline
  - System Shock 2
  - Deus Ex
  - Diablo II
  - BioShock

### 理论 / 框架队列

- 目标：补设计术语、观察框架与长期参考来源，不把它们误当成单篇证据。
- 纳入条件：更像站点级入口、理论文章、博客专栏、wiki 或播客，而不是单篇设计事实页。
- 当前首批候选：
  - Lost Garden
  - The Door Problem
  - Designer Notes
  - Game Design Patterns Wiki

### 暂缓 / 排除队列

- 目标：明确哪些链接本轮不处理，避免队列持续膨胀。
- 纳入条件：工具站、模板库、泛开发资源、视频播放列表、与当前“游戏设计模式证据沉淀”目标不直接对齐的内容。
- 当前典型条目：
  - Generic example 1 / 2 / 3
  - Dundoc / Nuclino / Affine / IMS Creators
  - Arrow / Twine / articy:draft / Ink / Yarn Spinner / Arcweave / Fungus / Machinations
  - 3D Math Primer for Graphics and Game Development / COLLISION DETECTION
  - Bevy / Godot / Defold / LÖVE / Pico-8
  - GDC Postmortems 播放列表与其他视频优先条目

## 推荐处理顺序

1. 先处理 `Finished games GDDs` 中可直接打开、来自已上线游戏的一手设计文档。
2. 再处理 `Postmortems` 中文本型、能明确讨论设计决策与系统取舍的复盘。
3. 然后处理 `Learning materials` 里的高信号理论入口，优先建立来源页或入口页，不急于产出模式结论。
4. `Templates and examples` 只在需要补 GDD 工作流背景时再回头处理。
5. `GDD Creation Tools`、`Game design tools`、`Game development` 继续留在暂缓 / 排除队列，除非后续任务明确转向工具或流程研究。

## 初始优先候选清单

### P1：最先处理的一手设计文档

- Monaco
  理由：已上线游戏原始 GDD，最符合“一手设计文档”优先原则。
- Id Doom
  理由：Doom Bible 属于经典设计圣经材料，预期能提供大量原始设计结构信息。
- Prince of Persia 2
  理由：明确的 design bible 形态，且对象清晰，适合建立早期设计文档样例。
- Condor's Diablo 1
  理由：早期 pitch / design 文档，适合观察玩法目标与系统构思如何被表达。
- Grim Fandango
  理由：成品游戏设计文档，题材与叙事结构都可能提供不同类型的设计信息。

### P2：随后处理的强复盘材料

- Balatro Timeline
  理由：现代、可直接访问、作者自述型材料，进入成本低。
- System Shock 2
  理由：经典 postmortem，适合提炼系统取舍与开发反思。
- Deus Ex
  理由：经典沉浸式模拟案例，预期有高价值设计判断。
- Diablo II
  理由：成熟 ARPG 案例，适合关注循环、掉落与长期驱动结构。
- BioShock
  理由：强设计导向的 AAA 复盘，可能提供机制与叙事结合的可复述判断。

### T1 / T2：延后处理的理论入口

- Lost Garden
  理由：长期高信号博客，更适合作为来源页或入口页，而不是直接模式证据。
- The Door Problem
  理由：单篇经典理论文，适合作为“设计职责与系统思维”背景材料。
- Designer Notes
  理由：站点型入口，后续应按具体文章或播客分流。
- Game Design Patterns Wiki
  理由：理论索引价值高，但需要谨慎处理其学术框架与仓库现有模式卡的关系。

## 本轮边界

- 不尝试导入 README 中的全部链接。
- 不把 `awesome-game-design` README 本身当作 `30_网页卡/` 的直接证据页。
- 不在本轮新建 `30_网页卡/` 或 `40_设计模式/`。
- 不把工具、引擎、泛开发学习资源混入当前游戏设计模式证据主队列。

## 2026-03-09 P1 稳定 intake triage

- Monaco
  结果：`blocked`
  资源形态：Facebook 社交页 HTML。
  阻塞：当前 URL 指向社交平台页面，不是稳定正文载体；也不符合仓库当前“非目标”里的社媒页面范围。
  下一步：仅记录阻塞，后续如找到同文档的公开镜像或可稳定访问副本，再重新进入 intake。
- Id Doom
  结果：`blocked`
  资源形态：PDF 直链，但当前请求返回 Cloudflare challenge HTML。
  阻塞：原始 PDF 目前不可稳定直取，无法作为常规导入输入。
  下一步：补找同源或高可信镜像；在拿到稳定 PDF 入口前不进入导入。
- Prince of Persia 2
  结果：`ready-for-next-step`
  资源形态：公开可访问 PDF。
  判断：当前链接返回 `application/pdf`，可作为仓库常规下一步的候选输入。
  下一步：后续按单 URL 正常流程建立网页卡并提炼模式候选。
- Condor's Diablo 1
  结果：`ready-for-next-step`
  资源形态：公开可访问 PDF。
  判断：当前链接返回 `application/pdf`，可作为仓库常规下一步的候选输入。
  下一步：后续按单 URL 正常流程建立网页卡并提炼模式候选。
- Grim Fandango
  结果：`ready-for-next-step`
  资源形态：公开可访问 PDF。
  判断：当前链接返回 `application/pdf`，可作为仓库常规下一步的候选输入。
  下一步：后续按单 URL 正常流程建立网页卡并提炼模式候选。
