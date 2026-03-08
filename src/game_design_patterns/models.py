from dataclasses import dataclass, field
from enum import StrEnum


class PageType(StrEnum):
    ARTICLE = "article"
    ENTRY_PAGE = "entry_page"


@dataclass(slots=True)
class EntryCandidate:
    title: str
    url: str


@dataclass(slots=True)
class EntryPageNote:
    title: str
    source: str
    url: str
    status: str = "active"
    summary: list[str] = field(default_factory=list)
    candidates: list[EntryCandidate] = field(default_factory=list)
    next_steps: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=lambda: ["game-design", "entry-page"])


@dataclass(slots=True)
class WebNote:
    title: str
    source: str
    url: str
    author: str = ""
    published_at: str = ""
    imported_at: str = ""
    summary: list[str] = field(default_factory=list)
    pattern_links: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=lambda: ["game-design", "web-note"])


@dataclass(slots=True)
class PatternNote:
    title: str
    aliases: list[str] = field(default_factory=list)
    domain: str = ""
    problem_space: str = ""
    definition: list[str] = field(default_factory=list)
    use_cases: list[str] = field(default_factory=list)
    design_values: list[str] = field(default_factory=list)
    variants: list[str] = field(default_factory=list)
    related_cases: list[str] = field(default_factory=list)
    evidence_sources: list[str] = field(default_factory=list)
    related_patterns: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=lambda: ["game-design", "pattern"])
