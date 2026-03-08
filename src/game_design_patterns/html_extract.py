from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup

from game_design_patterns.models import EntryCandidate, ExtractedEntryPage


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
