from pathlib import Path

from game_design_patterns.importer import import_url


FIXTURES_DIR = Path(__file__).parent / "fixtures"


def test_import_entry_page_writes_markdown_file(tmp_path: Path) -> None:
    created = import_url(
        "https://www.deconstructoroffun.com/blog?category=Deconstructions",
        vault_root=tmp_path,
        html=(
            FIXTURES_DIR / "deconstructor_category.html"
        ).read_text(encoding="utf-8"),
        imported_at="2026-03-08",
    )

    entry_note = tmp_path / "20_入口页" / "Deconstructor of Fun - Deconstructions.md"

    assert entry_note in created
    assert entry_note.exists()
    content = entry_note.read_text(encoding="utf-8")
    assert "type: entry_page" in content
    assert "## 候选链接" in content


def test_import_article_writes_web_note_and_pattern_note(tmp_path: Path) -> None:
    created = import_url(
        "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation",
        vault_root=tmp_path,
        html=(FIXTURES_DIR / "deconstructor_article.html").read_text(encoding="utf-8"),
        imported_at="2026-03-08",
    )

    web_note = tmp_path / "30_网页卡" / "The Sweet Art of Feature Adaptation.md"
    pattern_note = tmp_path / "40_设计模式" / "Feature Adaptation.md"

    assert web_note in created
    assert pattern_note in created
    assert web_note.exists()
    assert pattern_note.exists()
    assert "[[40_设计模式/Feature Adaptation|Feature Adaptation]]" in web_note.read_text(
        encoding="utf-8"
    )
    assert "[[30_网页卡/The Sweet Art of Feature Adaptation|The Sweet Art of Feature Adaptation]]" in pattern_note.read_text(
        encoding="utf-8"
    )
