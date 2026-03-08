from pathlib import Path

from game_design_patterns.paths import (
    entry_page_path,
    pattern_note_path,
    source_note_path,
    web_note_path,
)


def test_source_note_path_uses_source_directory() -> None:
    assert source_note_path("Deconstructor of Fun") == Path(
        "10_来源/Deconstructor of Fun.md"
    )


def test_entry_page_path_uses_entry_directory() -> None:
    assert entry_page_path("Deconstructor of Fun - Deconstructions") == Path(
        "20_入口页/Deconstructor of Fun - Deconstructions.md"
    )


def test_web_note_path_uses_web_note_directory() -> None:
    assert web_note_path("Clash Royale Deconstruction") == Path(
        "30_网页卡/Clash Royale Deconstruction.md"
    )


def test_pattern_note_path_uses_pattern_directory() -> None:
    assert pattern_note_path("Meta Progression") == Path(
        "40_设计模式/Meta Progression.md"
    )
