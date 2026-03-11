from pathlib import Path

from game_design_patterns.paths import (
    game_content_path,
    game_core_experience_path,
    game_design_patterns_path,
    game_directory_path,
    game_entry_note_path,
    game_evidence_index_path,
)


def test_game_directory_path_uses_game_master_root() -> None:
    assert game_directory_path("Clash Royale") == Path("10_游戏主卡/Clash Royale")


def test_game_entry_note_path_uses_game_directory() -> None:
    assert game_entry_note_path("Clash Royale") == Path(
        "10_游戏主卡/Clash Royale/Clash Royale.md"
    )


def test_game_core_experience_path_uses_fixed_suffix() -> None:
    assert game_core_experience_path("Clash Royale") == Path(
        "10_游戏主卡/Clash Royale/Clash Royale - 核心体验.md"
    )


def test_game_design_patterns_path_uses_fixed_suffix() -> None:
    assert game_design_patterns_path("Clash Royale") == Path(
        "10_游戏主卡/Clash Royale/Clash Royale - 设计模式.md"
    )


def test_game_content_path_uses_fixed_suffix() -> None:
    assert game_content_path("Clash Royale") == Path(
        "10_游戏主卡/Clash Royale/Clash Royale - 游戏内容.md"
    )


def test_game_evidence_index_path_uses_fixed_suffix() -> None:
    assert game_evidence_index_path("Clash Royale") == Path(
        "10_游戏主卡/Clash Royale/Clash Royale - 证据索引.md"
    )
