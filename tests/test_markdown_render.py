from game_design_patterns.markdown import (
    render_game_entry_note,
    upsert_bullet_in_section,
)


def test_render_game_entry_note_contains_fixed_sections_and_links() -> None:
    rendered = render_game_entry_note("Clash Royale")

    assert rendered.startswith("---\n")
    assert "type: game_master_index" in rendered
    assert "## 推荐阅读顺序" in rendered
    assert "[[10_游戏主卡/Clash Royale/Clash Royale - 核心体验|核心体验]]" in rendered
    assert "[[10_游戏主卡/Clash Royale/Clash Royale - 证据索引|证据索引]]" in rendered


def test_upsert_bullet_in_section_appends_and_removes_placeholder() -> None:
    markdown = """## 最近新增输入材料
-

## 其他
- a
"""

    updated, changed = upsert_bullet_in_section(
        markdown,
        "## 最近新增输入材料",
        "2026-03-11 - [Article](https://example.com)",
    )

    assert changed is True
    assert "- 2026-03-11 - [Article](https://example.com)" in updated
    assert "## 最近新增输入材料\n-\n" not in updated


def test_upsert_bullet_in_section_is_idempotent_for_same_item() -> None:
    markdown = """## 最近新增输入材料
- 2026-03-11 - [Article](https://example.com)
"""

    updated, changed = upsert_bullet_in_section(
        markdown,
        "## 最近新增输入材料",
        "2026-03-11 - [Article](https://example.com)",
    )

    expected = markdown if markdown.endswith("\n") else markdown + "\n"
    assert changed is False
    assert updated == expected
