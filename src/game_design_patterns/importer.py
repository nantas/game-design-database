from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from urllib.request import Request, urlopen

from game_design_patterns.html_extract import extract_article
from game_design_patterns.markdown import (
    render_game_content_note,
    render_game_core_experience_note,
    render_game_design_patterns_note,
    render_game_entry_note,
    render_game_evidence_index_note,
    upsert_bullet_in_section,
)
from game_design_patterns.paths import (
    game_content_path,
    game_core_experience_path,
    game_design_patterns_path,
    game_entry_note_path,
    game_evidence_index_path,
    note_link,
)


def fetch_html(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/137.0.0.0 Safari/537.36"
            )
        },
    )
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def import_url(
    url: str,
    vault_root: Path,
    game: str,
    html: str | None = None,
    imported_at: str | None = None,
) -> list[Path]:
    imported_at = imported_at or date.today().isoformat()
    _ensure_content_directories(vault_root)
    html_content = html or fetch_html(url)
    extracted = extract_article(html_content, url)

    touched_paths: list[Path] = []

    def track(path: Path) -> None:
        if path not in touched_paths:
            touched_paths.append(path)

    for created in _ensure_game_pages(vault_root, game):
        track(created)

    evidence_link = note_link(game_evidence_index_path(game), f"{game} - 证据索引")

    updates: list[tuple[Path, str, str]] = [
        (
            game_entry_note_path(game),
            "## 最近新增输入材料",
            f"{imported_at} - [{extracted.title}]({url})",
        ),
        (
            game_core_experience_path(game),
            "## 新输入待吸收",
            (
                f"{imported_at}：已登记《{extracted.title}》，待判断其对核心体验/决策/反馈循环"
                f"的贡献。证据见 {evidence_link}。"
            ),
        ),
        (
            game_evidence_index_path(game),
            "## 证据来源清单",
            (
                f"[ ] [{extracted.title}]({url})（来源：{extracted.source_name}；"
                f"作者：{extracted.author or '未知'}；发布时间：{extracted.published_at or '未知'}；"
                f"导入：{imported_at}）"
            ),
        ),
        (
            game_evidence_index_path(game),
            "## 来源可靠性与用途",
            f"{extracted.source_name}：待评估；用途：用于《{extracted.title}》相关判断。",
        ),
        (
            game_evidence_index_path(game),
            "## 证据到结论的映射",
            f"《{extracted.title}》 -> 待映射（核心体验/设计模式/游戏内容）",
        ),
    ]

    if extracted.pattern_candidates:
        updates.append(
            (
                game_design_patterns_path(game),
                "## 待验证模式线索",
                f"{imported_at}：{extracted.pattern_candidates[0]}（来自《{extracted.title}》）",
            )
        )

    for relative_path, section_heading, item in updates:
        absolute_path = vault_root / relative_path
        if _upsert_markdown_section_bullet(absolute_path, section_heading, item):
            track(absolute_path)

    return touched_paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="导入单游戏网页到游戏主卡")
    parser.add_argument("url", help="要导入的网页 URL")
    parser.add_argument("--game", required=True, help="目标游戏名")
    parser.add_argument(
        "--vault-root",
        default=Path(__file__).resolve().parents[2],
        type=Path,
        help="目标仓库根目录，默认使用当前项目根目录",
    )
    parser.add_argument(
        "--imported-at",
        default=None,
        help="导入日期，默认使用今天",
    )
    args = parser.parse_args(argv)

    touched = import_url(
        args.url,
        vault_root=args.vault_root,
        game=args.game,
        imported_at=args.imported_at,
    )
    for file_path in touched:
        print(file_path)
    return 0


def _ensure_game_pages(vault_root: Path, game: str) -> list[Path]:
    pages: list[tuple[Path, str]] = [
        (game_entry_note_path(game), render_game_entry_note(game)),
        (game_core_experience_path(game), render_game_core_experience_note(game)),
        (game_design_patterns_path(game), render_game_design_patterns_note(game)),
        (game_content_path(game), render_game_content_note(game)),
        (game_evidence_index_path(game), render_game_evidence_index_note(game)),
    ]

    created: list[Path] = []
    for relative_path, content in pages:
        absolute_path = vault_root / relative_path
        if absolute_path.exists():
            continue
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        absolute_path.write_text(content, encoding="utf-8")
        created.append(absolute_path)
    return created


def _upsert_markdown_section_bullet(path: Path, section_heading: str, item: str) -> bool:
    original = path.read_text(encoding="utf-8")
    updated, changed = upsert_bullet_in_section(original, section_heading, item)
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


def _ensure_content_directories(vault_root: Path) -> None:
    for directory in [
        "10_游戏主卡",
        "50_专题索引",
        "90_模板与规范",
    ]:
        (vault_root / directory).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
