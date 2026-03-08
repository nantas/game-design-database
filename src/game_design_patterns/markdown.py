from collections.abc import Iterable
import re

from game_design_patterns.models import EntryPageNote, PatternNote, WebNote
from game_design_patterns.paths import note_link, source_note_path


def _quote(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def _format_scalar(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_.-]+", value):
        return value
    return _quote(value)


def _format_list(values: list[str]) -> str:
    return "[" + ", ".join(_quote(value) for value in values) + "]"


def _frontmatter(properties: dict[str, str | list[str]]) -> str:
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


def render_web_note(note: WebNote) -> str:
    source_link = note_link(source_note_path(note.source), note.source)
    frontmatter = _frontmatter(
        {
            "title": note.title,
            "type": "web_note",
            "source": note.source,
            "url": note.url,
            "author": note.author,
            "published_at": note.published_at,
            "imported_at": note.imported_at,
            "tags": note.tags,
        }
    )

    sections = [
        frontmatter,
        "",
        f"# {note.title}",
        "",
        "## 内容摘要",
        *_bullet_lines(note.summary),
        "",
        "## 来源关联",
        *_bullet_lines([source_link]),
        "",
        "## 提炼出的设计模式",
        *_bullet_lines(note.pattern_links),
        "",
        "## 关键证据",
        *_bullet_lines(note.evidence),
        "",
        "## 我的备注",
        *_bullet_lines(note.notes),
    ]
    return "\n".join(sections) + "\n"


def render_entry_page_note(note: EntryPageNote) -> str:
    frontmatter = _frontmatter(
        {
            "title": note.title,
            "type": "entry_page",
            "source": note.source,
            "url": note.url,
            "status": note.status,
            "tags": note.tags,
        }
    )
    candidate_lines = [
        f"- [ ] {candidate.title} - {candidate.url}" for candidate in note.candidates
    ] or ["- [ ] "]

    sections = [
        frontmatter,
        "",
        f"# {note.title}",
        "",
        "## 页面摘要",
        *_bullet_lines(note.summary),
        "",
        "## 候选链接",
        *candidate_lines,
        "",
        "## 后续处理",
        *_bullet_lines(note.next_steps),
    ]
    return "\n".join(sections) + "\n"


def render_pattern_note(note: PatternNote) -> str:
    frontmatter = _frontmatter(
        {
            "title": note.title,
            "type": "pattern",
            "aliases": note.aliases,
            "domain": note.domain,
            "problem_space": note.problem_space,
            "tags": note.tags,
        }
    )

    sections = [
        frontmatter,
        "",
        f"# {note.title}",
        "",
        "## 定义",
        *_bullet_lines(note.definition),
        "",
        "## 适用场景",
        *_bullet_lines(note.use_cases),
        "",
        "## 设计价值",
        *_bullet_lines(note.design_values),
        "",
        "## 常见变体",
        *_bullet_lines(note.variants),
        "",
        "## 相关案例",
        *_bullet_lines(note.related_cases),
        "",
        "## 证据来源",
        *_bullet_lines(note.evidence_sources),
        "",
        "## 相关模式",
        *_bullet_lines(note.related_patterns),
    ]
    return "\n".join(sections) + "\n"
