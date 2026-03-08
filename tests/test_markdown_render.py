from game_design_patterns.markdown import (
    render_entry_page_note,
    render_pattern_note,
    render_web_note,
)
from game_design_patterns.models import EntryCandidate, EntryPageNote, PatternNote, WebNote


def test_render_web_note_contains_fixed_sections() -> None:
    note = WebNote(
        title="Clash Royale Deconstruction",
        source="Deconstructor of Fun",
        url="https://example.com/clash-royale",
        author="Alice",
        published_at="2025-11-07",
        imported_at="2026-03-08",
        summary=["这篇文章拆解了留存与匹配节奏。"],
        pattern_links=["[[40_设计模式/三选一奖励|三选一奖励]]"],
        evidence=[
            "结论：奖励选择会放大局间策略。",
            "来源：文章正文。",
        ],
        notes=["后续可对比 Brawl Stars。"],
    )

    rendered = render_web_note(note)

    assert rendered.startswith("---\n")
    assert "type: web_note" in rendered
    assert 'url: "https://example.com/clash-royale"' in rendered
    assert "## 内容摘要" in rendered
    assert "## 提炼出的设计模式" in rendered
    assert "## 关键证据" in rendered


def test_render_entry_page_contains_candidates() -> None:
    note = EntryPageNote(
        title="Deconstructor of Fun - Deconstructions",
        source="Deconstructor of Fun",
        url="https://www.deconstructoroffun.com/blog?category=Deconstructions",
        status="active",
        summary=["这是 deconstruction 栏目入口页。"],
        candidates=[
            EntryCandidate(
                title="Deconstructing Clash Royale",
                url="https://example.com/clash-royale",
            )
        ],
        next_steps=["优先导入移动 F2P 代表案例。"],
    )

    rendered = render_entry_page_note(note)

    assert "type: entry_page" in rendered
    assert "## 候选链接" in rendered
    assert "- [ ] Deconstructing Clash Royale - https://example.com/clash-royale" in rendered


def test_render_pattern_note_contains_aliases_and_evidence() -> None:
    note = PatternNote(
        title="三选一奖励",
        aliases=["choice bundle", "draft pick reward"],
        domain="战斗后奖励",
        problem_space="让玩家在局内持续塑造构筑方向",
        definition=["每次奖励时提供多个备选项。"],
        use_cases=["卡牌构筑战斗后奖励。"],
        design_values=["强化选择感和路径分化。"],
        variants=["固定三选一", "稀有度影响选项池"],
        related_cases=["[[30_网页卡/Clash Royale Deconstruction|Clash Royale Deconstruction]]"],
        evidence_sources=["[[30_网页卡/Clash Royale Deconstruction|Clash Royale Deconstruction]]"],
        related_patterns=["[[40_设计模式/Meta Progression|Meta Progression]]"],
    )

    rendered = render_pattern_note(note)

    assert "type: pattern" in rendered
    assert 'aliases: ["choice bundle", "draft pick reward"]' in rendered
    assert "## 证据来源" in rendered
    assert "[[30_网页卡/Clash Royale Deconstruction|Clash Royale Deconstruction]]" in rendered
