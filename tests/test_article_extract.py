from pathlib import Path

from game_design_patterns.html_extract import extract_article


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "deconstructor_article.html"
GAME_DESIGN_SKILLS_FIXTURE_PATH = (
    Path(__file__).parent / "fixtures" / "game_design_skills_core_loop.html"
)


def test_extract_article_title_author_and_date() -> None:
    extracted = extract_article(
        FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation",
    )

    assert extracted.title == "The Sweet Art of Feature Adaptation"
    assert extracted.author == "Jared Gibbons"
    assert extracted.published_at == "2024-11-12"


def test_extract_article_summary_is_not_empty() -> None:
    extracted = extract_article(
        FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation",
    )

    assert extracted.summary
    assert len(extracted.summary[0]) > 40


def test_extract_article_summary_skips_author_bio() -> None:
    extracted = extract_article(
        FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation",
    )

    assert not extracted.summary[0].startswith("Written by")
    assert "gaming industry" in extracted.summary[0]


def test_extract_article_pattern_candidates_are_present() -> None:
    extracted = extract_article(
        FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation",
    )

    assert "Feature Adaptation" in extracted.pattern_candidates


def test_extract_article_supports_game_design_skills_article() -> None:
    extracted = extract_article(
        GAME_DESIGN_SKILLS_FIXTURE_PATH.read_text(encoding="utf-8"),
        "https://gamedesignskills.com/game-design/core-loops-in-gameplay/",
    )

    assert extracted.title == "Designing The Core Gameplay Loop: A Beginner’s Guide"
    assert extracted.author == "Alexander Brazie"
    assert extracted.published_at == "2023-10-06"
    assert extracted.summary
    assert "gameplay loop" in extracted.summary[0].lower()
