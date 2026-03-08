from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from urllib.request import Request, urlopen

from game_design_patterns.html_extract import extract_article, extract_entry_page
from game_design_patterns.markdown import (
    render_entry_page_note,
    render_pattern_note,
    render_web_note,
)
from game_design_patterns.models import EntryPageNote, PatternNote, WebNote
from game_design_patterns.paths import (
    classify_page_type,
    entry_page_path,
    pattern_note_path,
    web_note_path,
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
    html: str | None = None,
    imported_at: str | None = None,
) -> list[Path]:
    imported_at = imported_at or date.today().isoformat()
    _ensure_content_directories(vault_root)
    page_type = classify_page_type(url)
    html_content = html or fetch_html(url)

    if page_type.value == "entry_page":
        return _import_entry_page(url, vault_root, html_content)

    return _import_article(url, vault_root, html_content, imported_at)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="导入游戏设计网页到 Markdown 仓库")
    parser.add_argument("url", help="要导入的网页 URL")
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

    created_files = import_url(
        args.url,
        vault_root=args.vault_root,
        imported_at=args.imported_at,
    )
    for file_path in created_files:
        print(file_path)
    return 0


def _import_entry_page(url: str, vault_root: Path, html: str) -> list[Path]:
    extracted = extract_entry_page(html, url)
    note = EntryPageNote(
        title=extracted.title,
        source=extracted.source_name,
        url=url,
        status="active",
        summary=extracted.summary,
        candidates=extracted.candidates,
        next_steps=["优先挑选一篇代表性文章继续导入。"],
    )
    output_path = vault_root / entry_page_path(note.title)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_entry_page_note(note), encoding="utf-8")
    return [output_path]


def _import_article(
    url: str,
    vault_root: Path,
    html: str,
    imported_at: str,
) -> list[Path]:
    extracted = extract_article(html, url)
    pattern_title = extracted.pattern_candidates[0] if extracted.pattern_candidates else extracted.title
    pattern_link = f"[[40_设计模式/{pattern_title}|{pattern_title}]]"
    web_link = f"[[30_网页卡/{extracted.title}|{extracted.title}]]"

    web_note = WebNote(
        title=extracted.title,
        source=extracted.source_name,
        url=url,
        author=extracted.author,
        published_at=extracted.published_at,
        imported_at=imported_at,
        summary=extracted.summary,
        pattern_links=[pattern_link],
        evidence=extracted.evidence or extracted.summary,
        notes=["自动导入生成，建议人工复核模式归并与证据表述。"],
    )
    pattern_note = PatternNote(
        title=pattern_title,
        aliases=[],
        domain="待补充",
        problem_space="待补充",
        definition=[f"由《{extracted.title}》提炼出的候选设计模式。"],
        use_cases=["需要围绕现有产品吸收外部成功特征时。"],
        design_values=extracted.summary[:1],
        variants=["待补充"],
        related_cases=[web_link],
        evidence_sources=[web_link],
        related_patterns=[],
    )

    web_note_path_abs = vault_root / web_note_path(web_note.title)
    pattern_note_path_abs = vault_root / pattern_note_path(pattern_note.title)
    web_note_path_abs.parent.mkdir(parents=True, exist_ok=True)
    pattern_note_path_abs.parent.mkdir(parents=True, exist_ok=True)
    web_note_path_abs.write_text(render_web_note(web_note), encoding="utf-8")
    pattern_note_path_abs.write_text(
        render_pattern_note(pattern_note),
        encoding="utf-8",
    )
    return [web_note_path_abs, pattern_note_path_abs]


def _ensure_content_directories(vault_root: Path) -> None:
    for directory in [
        "10_来源",
        "20_入口页",
        "30_网页卡",
        "40_设计模式",
        "50_专题索引",
        "90_模板与规范",
    ]:
        (vault_root / directory).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
