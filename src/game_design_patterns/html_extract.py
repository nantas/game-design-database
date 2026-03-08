import re
from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup

from game_design_patterns.models import (
    EntryCandidate,
    ExtractedArticle,
    ExtractedEntryPage,
)


def extract_entry_page(html: str, source_url: str) -> ExtractedEntryPage:
    soup = BeautifulSoup(html, "html.parser")
    source_name = _extract_site_name(soup, source_url)
    title = _build_entry_page_title(source_name, source_url)
    candidates: list[EntryCandidate] = []
    seen_urls: set[str] = set()

    for anchor in soup.find_all("a", href=True):
        raw_href = anchor["href"]
        absolute_url = urljoin(source_url, raw_href)

        if not _is_article_url(absolute_url):
            continue

        if absolute_url in seen_urls:
            continue

        candidate_title = _extract_anchor_title(anchor)
        if not candidate_title:
            continue

        candidates.append(EntryCandidate(title=candidate_title, url=absolute_url))
        seen_urls.add(absolute_url)

    summary = [
        f"来源站点：{source_name}",
        f"候选文章数：{len(candidates)}",
    ]

    return ExtractedEntryPage(
        title=title,
        source_name=source_name,
        source_url=source_url,
        candidates=candidates,
        summary=summary,
    )


def extract_article(html: str, source_url: str) -> ExtractedArticle:
    soup = BeautifulSoup(html, "html.parser")
    source_name = _extract_site_name(soup, source_url)
    title = _extract_article_title(soup)
    author = _extract_author(soup)
    published_at = _extract_published_at(soup)
    paragraphs = _extract_article_paragraphs(soup)
    summary = _build_summary(paragraphs)
    pattern_candidates = _pattern_candidates_from_title(title)
    evidence = [paragraphs[0]] if paragraphs else []

    return ExtractedArticle(
        title=title,
        source_name=source_name,
        source_url=source_url,
        author=author,
        published_at=published_at,
        summary=summary,
        pattern_candidates=pattern_candidates,
        evidence=evidence,
    )


def _extract_site_name(soup: BeautifulSoup, source_url: str) -> str:
    meta = soup.find("meta", attrs={"property": "og:site_name"})
    if meta and meta.get("content"):
        return meta["content"].strip()

    hostname = urlparse(source_url).hostname or ""
    hostname = hostname.removeprefix("www.")
    if hostname:
        return hostname
    return "Unknown Source"


def _build_entry_page_title(source_name: str, source_url: str) -> str:
    query = parse_qs(urlparse(source_url).query)
    categories = query.get("category")
    if categories:
        return f"{source_name} - {categories[0]}"
    return source_name


def _is_article_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.netloc and "deconstructoroffun.com" not in parsed.netloc:
        return False
    if not parsed.path.startswith("/blog/"):
        return False
    if parsed.path.startswith("/blog/category/"):
        return False
    if parsed.path == "/blog/":
        return False
    if parsed.query:
        return False
    return True


def _extract_anchor_title(anchor) -> str:
    text = anchor.get_text(" ", strip=True)
    if text:
        return " ".join(text.split())

    image = anchor.find("img")
    if image and image.get("alt"):
        return " ".join(image["alt"].split())

    return ""


def _extract_article_title(soup: BeautifulSoup) -> str:
    heading = soup.find("h1")
    if heading:
        return " ".join(heading.get_text(" ", strip=True).split())

    if soup.title and soup.title.string:
        return soup.title.string.split("—")[0].strip()

    return "Untitled Article"


def _extract_author(soup: BeautifulSoup) -> str:
    author_link = soup.select_one(".blog-author-name")
    if author_link:
        return " ".join(author_link.get_text(" ", strip=True).split())

    author_meta = soup.find("meta", attrs={"name": "author"})
    if author_meta and author_meta.get("content"):
        return author_meta["content"].strip()

    twitter_label = soup.find("meta", attrs={"name": "twitter:label1"})
    twitter_data = soup.find("meta", attrs={"name": "twitter:data1"})
    if (
        twitter_label
        and twitter_data
        and twitter_label.get("content", "").strip().lower() == "written by"
        and twitter_data.get("content")
    ):
        return twitter_data["content"].strip()

    return ""


def _extract_published_at(soup: BeautifulSoup) -> str:
    meta = soup.find("meta", attrs={"itemprop": "datePublished"})
    if meta and meta.get("content"):
        return meta["content"][:10]

    article_meta = soup.find("meta", attrs={"property": "article:published_time"})
    if article_meta and article_meta.get("content"):
        return article_meta["content"][:10]

    time_tag = soup.find("time")
    if time_tag and time_tag.get("datetime"):
        return time_tag["datetime"][:10]

    return ""


def _extract_article_paragraphs(soup: BeautifulSoup) -> list[str]:
    selectors = [
        ".sqs-html-content p",
        ".elementor-widget-theme-post-content p",
        "[class*='entry-content'] p",
        "[class*='post-content'] p",
        "[itemprop='articleBody'] p",
        "article p",
        "main p",
    ]

    for selector in selectors:
        paragraphs = _collect_paragraphs(soup.select(selector))
        if paragraphs:
            return paragraphs

    return []


def _collect_paragraphs(nodes) -> list[str]:
    paragraphs: list[str] = []

    for paragraph in nodes:
        text = " ".join(paragraph.get_text(" ", strip=True).split())
        if len(text) < 40:
            continue
        if _looks_like_author_bio(text):
            continue
        if text in paragraphs:
            continue
        paragraphs.append(text)

    return paragraphs


def _build_summary(paragraphs: list[str]) -> list[str]:
    if not paragraphs:
        return []
    return paragraphs[:3]


def _pattern_candidates_from_title(title: str) -> list[str]:
    normalized = re.sub(r"^(The|A|An)\s+", "", title).strip()
    normalized = re.sub(r"^(Sweet|Great|Art of)\s+", "", normalized).strip()
    normalized = re.sub(r"^(Sweet Art of)\s+", "", normalized, flags=re.IGNORECASE)

    replacements = [
        ("The Sweet Art of ", ""),
        ("The Art of ", ""),
        ("The Magic Behind ", ""),
    ]
    for prefix, replacement in replacements:
        if normalized.startswith(prefix):
            normalized = normalized.replace(prefix, replacement, 1).strip()

    if title.startswith("The Sweet Art of "):
        normalized = title.removeprefix("The Sweet Art of ").strip()
    elif title.startswith("The Art of "):
        normalized = title.removeprefix("The Art of ").strip()

    return [normalized] if normalized else []


def _looks_like_author_bio(text: str) -> bool:
    lowered = text.lower()
    if lowered.startswith("written by "):
        return True
    if lowered.startswith("when ") and "you’ll find" in lowered:
        return True
    if lowered.startswith("when ") and "isn’t busy" in lowered:
        return True
    return False
