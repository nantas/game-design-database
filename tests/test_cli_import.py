from pathlib import Path

from game_design_patterns.importer import import_url


FIXTURES_DIR = Path(__file__).parent / "fixtures"


def test_import_article_writes_five_game_master_pages(tmp_path: Path) -> None:
    created = import_url(
        "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation",
        vault_root=tmp_path,
        game="Clash Royale",
        html=(FIXTURES_DIR / "deconstructor_article.html").read_text(encoding="utf-8"),
        imported_at="2026-03-11",
    )

    game_dir = tmp_path / "10_游戏主卡" / "Clash Royale"
    entry_page = game_dir / "Clash Royale.md"
    core_page = game_dir / "Clash Royale - 核心体验.md"
    patterns_page = game_dir / "Clash Royale - 设计模式.md"
    content_page = game_dir / "Clash Royale - 游戏内容.md"
    evidence_page = game_dir / "Clash Royale - 证据索引.md"

    assert entry_page in created
    assert core_page in created
    assert patterns_page in created
    assert content_page in created
    assert evidence_page in created

    entry_text = entry_page.read_text(encoding="utf-8")
    assert "type: game_master_index" in entry_text
    assert (
        "2026-03-11 - [The Sweet Art of Feature Adaptation](https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation)"
        in entry_text
    )

    core_text = core_page.read_text(encoding="utf-8")
    assert "## 新输入待吸收" in core_text
    assert "[[10_游戏主卡/Clash Royale/Clash Royale - 证据索引|Clash Royale - 证据索引]]" in core_text

    patterns_text = patterns_page.read_text(encoding="utf-8")
    assert "## 待验证模式线索" in patterns_text
    assert "Feature Adaptation" in patterns_text

    evidence_text = evidence_page.read_text(encoding="utf-8")
    assert "type: game_evidence_index" in evidence_text
    assert "The Sweet Art of Feature Adaptation" in evidence_text
    assert "来源：Deconstructor of Fun" in evidence_text


def test_import_article_does_not_duplicate_same_input(tmp_path: Path) -> None:
    kwargs = {
        "url": "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation",
        "vault_root": tmp_path,
        "game": "Clash Royale",
        "html": (FIXTURES_DIR / "deconstructor_article.html").read_text(encoding="utf-8"),
        "imported_at": "2026-03-11",
    }
    first = import_url(**kwargs)
    second = import_url(**kwargs)

    assert first
    assert second == []

    evidence_page = (
        tmp_path / "10_游戏主卡" / "Clash Royale" / "Clash Royale - 证据索引.md"
    )
    evidence_text = evidence_page.read_text(encoding="utf-8")
    assert (
        evidence_text.count(
            "https://www.deconstructoroffun.com/blog/2024/11/11/the-art-of-feature-adaptation"
        )
        == 1
    )
