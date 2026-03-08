from pathlib import Path

from game_design_patterns.html_extract import extract_entry_page


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "deconstructor_category.html"
GITHUB_FIXTURE_PATH = Path(__file__).parent / "fixtures" / "github_awesome_gamedev.html"


def test_extract_entry_page_title_from_category_url() -> None:
    extracted = extract_entry_page(
        FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://www.deconstructoroffun.com/blog?category=Deconstructions",
    )

    assert extracted.title == "Deconstructor of Fun - Deconstructions"


def test_extract_entry_page_candidates_in_stable_order() -> None:
    extracted = extract_entry_page(
        FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://www.deconstructoroffun.com/blog?category=Deconstructions",
    )

    assert extracted.candidates[0].title == (
        "Hay Day With a To-Do List: How Focus Friend Cracked Productivity Retention"
    )
    assert extracted.candidates[0].url == (
        "https://www.deconstructoroffun.com/blog/"
        "hay-day-with-a-to-do-list-how-focus-friend-cracked-productivity-retention"
    )


def test_extract_entry_page_deduplicates_article_links() -> None:
    extracted = extract_entry_page(
        FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://www.deconstructoroffun.com/blog?category=Deconstructions",
    )
    urls = [candidate.url for candidate in extracted.candidates]

    assert len(urls) == len(set(urls))
    assert (
        "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation"
        in urls
    )


def test_extract_github_awesome_page_title_from_repo_url() -> None:
    extracted = extract_entry_page(
        GITHUB_FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://github.com/Calinou/awesome-gamedev",
    )

    assert extracted.title == "GitHub - Calinou/awesome-gamedev"


def test_extract_github_awesome_page_candidates_from_readme() -> None:
    extracted = extract_entry_page(
        GITHUB_FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://github.com/Calinou/awesome-gamedev",
    )

    assert extracted.candidates[0].title == "free software"
    assert extracted.candidates[0].url == "https://www.fsf.org/about/what-is-free-software"
    assert any(
        candidate.title == "Bosca Ceoil Blue"
        and candidate.url == "https://github.com/YuriSizov/boscaceoil-blue"
        for candidate in extracted.candidates
    )


def test_extract_github_awesome_page_filters_noise_and_deduplicates() -> None:
    extracted = extract_entry_page(
        GITHUB_FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://github.com/Calinou/awesome-gamedev",
    )
    urls = [candidate.url for candidate in extracted.candidates]

    assert len(urls) == len(set(urls))
    assert "https://opensource.org/license/MIT" not in urls
    assert not any(
        url.startswith("https://github.com/Calinou/awesome-gamedev#") for url in urls
    )
