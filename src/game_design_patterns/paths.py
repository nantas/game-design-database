import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from game_design_patterns.models import PageType


def classify_page_type(url: str) -> PageType:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    if "category" in query:
        return PageType.ENTRY_PAGE

    return PageType.ARTICLE


def _note_path(directory: str, title: str) -> Path:
    safe_title = re.sub(r'[\\/:*?"<>|]+', " - ", title)
    safe_title = re.sub(r"\s+", " ", safe_title).strip().rstrip(".")
    return Path(directory) / f"{safe_title}.md"


def source_note_path(title: str) -> Path:
    return _note_path("10_来源", title)


def entry_page_path(title: str) -> Path:
    return _note_path("20_入口页", title)


def web_note_path(title: str) -> Path:
    return _note_path("30_网页卡", title)


def pattern_note_path(title: str) -> Path:
    return _note_path("40_设计模式", title)
