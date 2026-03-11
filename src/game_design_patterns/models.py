from dataclasses import dataclass, field


@dataclass(slots=True)
class ExtractedArticle:
    title: str
    source_name: str
    source_url: str
    author: str = ""
    published_at: str = ""
    summary: list[str] = field(default_factory=list)
    pattern_candidates: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
