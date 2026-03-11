import re
from pathlib import Path


def _safe_name(value: str) -> str:
    safe_title = re.sub(r'[\\/:*?"<>|]+', " - ", value)
    safe_title = re.sub(r"\s+", " ", safe_title).strip().rstrip(".")
    return safe_title or "untitled"


def note_link(note_path: Path, label: str) -> str:
    return f"[[{note_path.with_suffix('').as_posix()}|{label}]]"


def game_root_path() -> Path:
    return Path("10_游戏主卡")


def game_directory_path(game: str) -> Path:
    return game_root_path() / _safe_name(game)


def game_entry_note_path(game: str) -> Path:
    safe_game = _safe_name(game)
    return game_directory_path(game) / f"{safe_game}.md"


def game_core_experience_path(game: str) -> Path:
    safe_game = _safe_name(game)
    return game_directory_path(game) / f"{safe_game} - 核心体验.md"


def game_design_patterns_path(game: str) -> Path:
    safe_game = _safe_name(game)
    return game_directory_path(game) / f"{safe_game} - 设计模式.md"


def game_content_path(game: str) -> Path:
    safe_game = _safe_name(game)
    return game_directory_path(game) / f"{safe_game} - 游戏内容.md"


def game_evidence_index_path(game: str) -> Path:
    safe_game = _safe_name(game)
    return game_directory_path(game) / f"{safe_game} - 证据索引.md"
