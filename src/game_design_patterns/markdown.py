from collections.abc import Iterable
import re

from game_design_patterns.paths import (
    game_content_path,
    game_core_experience_path,
    game_design_patterns_path,
    game_entry_note_path,
    game_evidence_index_path,
    note_link,
)


def _quote(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def _format_scalar(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_.-]+", value):
        return value
    return _quote(value)


def _format_list(values: list[str]) -> str:
    return "[" + ", ".join(_quote(value) for value in values) + "]"


def frontmatter(properties: dict[str, str | list[str]]) -> str:
    lines = ["---"]

    for key, value in properties.items():
        if isinstance(value, list):
            lines.append(f"{key}: {_format_list(value)}")
        else:
            lines.append(f"{key}: {_format_scalar(value)}")

    lines.append("---")
    return "\n".join(lines)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    values = list(items)
    if not values:
        return ["- "]
    return [f"- {item}" for item in values]


def render_game_entry_note(game: str) -> str:
    front = frontmatter(
        {
            "title": game,
            "type": "game_master_index",
            "game": game,
            "tags": ["game-design", "game-master-card"],
        }
    )
    sections = [
        front,
        "",
        f"# {game}",
        "",
        "## 定位",
        "- 这张主卡聚焦该游戏的核心体验、设计判断与内容组织。",
        "",
        "## 推荐阅读顺序",
        f"- {note_link(game_core_experience_path(game), '核心体验')}",
        f"- {note_link(game_design_patterns_path(game), '设计模式')}",
        f"- {note_link(game_content_path(game), '游戏内容')}",
        f"- {note_link(game_evidence_index_path(game), '证据索引')}",
        "",
        "## 当前分析焦点",
        "- ",
        "",
        "## 固定页导航",
        f"- {note_link(game_entry_note_path(game), '入口页')}",
        f"- {note_link(game_core_experience_path(game), '核心体验')}",
        f"- {note_link(game_design_patterns_path(game), '设计模式')}",
        f"- {note_link(game_content_path(game), '游戏内容')}",
        f"- {note_link(game_evidence_index_path(game), '证据索引')}",
        "",
        "## 最近新增输入材料",
        "- ",
    ]
    return "\n".join(sections) + "\n"


def render_game_core_experience_note(game: str) -> str:
    front = frontmatter(
        {
            "title": f"{game} - 核心体验",
            "type": "game_core_experience",
            "game": game,
            "tags": ["game-design", "core-experience"],
        }
    )
    sections = [
        front,
        "",
        f"# {game} - 核心体验",
        "",
        "## 这款游戏想让玩家持续获得什么体验",
        "- ",
        "",
        "## 支撑该体验的关键玩家决策",
        "- ",
        "",
        "## 支撑该体验的关键反馈循环",
        "- ",
        "",
        "## 当前判断边界",
        "- 当前哪些判断证据充分，哪些仍待验证。",
        "",
        "## 新输入待吸收",
        "- ",
    ]
    return "\n".join(sections) + "\n"


def render_game_design_patterns_note(game: str) -> str:
    front = frontmatter(
        {
            "title": f"{game} - 设计模式",
            "type": "game_design_patterns",
            "game": game,
            "tags": ["game-design", "game-patterns"],
        }
    )
    sections = [
        front,
        "",
        f"# {game} - 设计模式",
        "",
        "## 模式清单",
        "- ",
        "",
        "## 每个模式的作用",
        "- ",
        "",
        "## 触发方式与生效条件",
        "- ",
        "",
        "## 可迁移性判断",
        "- 哪些结论可跨游戏复用。",
        "- 哪些结论仍依赖该游戏语境。",
        "",
        "## 待验证模式线索",
        "- ",
    ]
    return "\n".join(sections) + "\n"


def render_game_content_note(game: str) -> str:
    front = frontmatter(
        {
            "title": f"{game} - 游戏内容",
            "type": "game_content_design",
            "game": game,
            "tags": ["game-design", "game-content"],
        }
    )
    sections = [
        front,
        "",
        f"# {game} - 游戏内容",
        "",
        "## 内容如何服务核心体验",
        "- ",
        "",
        "## 内容池如何组织、分层和控量",
        "- ",
        "",
        "## 内容如何持续扩展而不破坏主体验",
        "- ",
        "",
        "## 当前内容设计缺口",
        "- ",
    ]
    return "\n".join(sections) + "\n"


def render_game_evidence_index_note(game: str) -> str:
    front = frontmatter(
        {
            "title": f"{game} - 证据索引",
            "type": "game_evidence_index",
            "game": game,
            "tags": ["game-design", "evidence-index"],
        }
    )
    sections = [
        front,
        "",
        f"# {game} - 证据索引",
        "",
        "## 证据来源清单",
        "- ",
        "",
        "## 来源可靠性与用途",
        "- ",
        "",
        "## 证据到结论的映射",
        "- ",
        "",
        "## 证据缺口",
        "- ",
    ]
    return "\n".join(sections) + "\n"


def upsert_bullet_in_section(markdown_text: str, section_heading: str, item: str) -> tuple[str, bool]:
    bullet_line = f"- {item}".rstrip()
    lines = markdown_text.splitlines()

    if bullet_line in lines:
        return markdown_text, False

    try:
        section_start = next(
            index for index, line in enumerate(lines) if line.strip() == section_heading
        )
    except StopIteration as exc:
        raise ValueError(f"section not found: {section_heading}") from exc

    body_start = section_start + 1
    while body_start < len(lines) and lines[body_start].strip() == "":
        body_start += 1

    section_end = body_start
    while section_end < len(lines) and not lines[section_end].startswith("## "):
        section_end += 1

    cleaned_body: list[str] = []
    for body_line in lines[body_start:section_end]:
        if body_line.strip() == "-":
            continue
        cleaned_body.append(body_line)

    updated_lines = lines[:body_start] + cleaned_body + [bullet_line] + lines[section_end:]
    updated_text = "\n".join(updated_lines).rstrip() + "\n"
    return updated_text, True
