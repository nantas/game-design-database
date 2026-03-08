from game_design_patterns.models import PageType
from game_design_patterns.paths import classify_page_type


def test_deconstructor_category_url_is_entry_page() -> None:
    url = "https://www.deconstructoroffun.com/blog?category=Deconstructions"

    assert classify_page_type(url) is PageType.ENTRY_PAGE


def test_blog_article_url_is_article() -> None:
    url = "https://www.deconstructoroffun.com/blog/2025/11/07/example-article"

    assert classify_page_type(url) is PageType.ARTICLE


def test_unknown_url_defaults_to_article() -> None:
    url = "https://example.com/game-design-patterns"

    assert classify_page_type(url) is PageType.ARTICLE

