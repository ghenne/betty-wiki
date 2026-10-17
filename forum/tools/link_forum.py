#!/usr/bin/env python3
"""Schreibt Bettyhacks-Forum-Links in Markdown-Dateien auf lokale Seiten um.

Unterstuetzt insbesondere Links der Form

    http://bettyhacks.com/forum/index.php?topic=51.msg314#msg314

die aus dem Wiki in das Forum zeigen. Ziel ist die lokale Themendatei
mit Anker, z.B. ``topics/0051-lcd-treiber-chip.md#msg314``.

Standardmaessig nur Vorschau (Dry-Run). Mit --write werden die Dateien
geaendert, optional mit --backup als .bak gesichert.

Beispiele:
    python3 tools/link_forum.py ../Betty_Wiki_md
    python3 tools/link_forum.py ../Betty_Wiki_md --write
    python3 tools/link_forum.py ../Betty_Wiki_md/pages --write --backup
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "_meta"
TOPICS_DIR = ROOT / "topics"
BOARDS_DIR = ROOT / "boards"

FORUM_REPO = "ghenne/betty-forum"
FORUM_REPO_NAME = "betty-forum"
BRANCH = "main"
GITHUB_WEB = "https://github.com"
GITHUB_ORG = "ghenne"
USE_RELATIVE = True
WIKI_ROOT: Path | None = None

# topic=ID, optional .msgNNN oder .<offset>, optional ;parameter, optional #msgNNN
FORUM_RE = re.compile(
    r"https?://(?:www\.)?bettyhacks\.com/forum/index\.php\?topic=(\d+)"
    r"(?:\.([^#\s)\">\]]*))?"
    r"(#[^\s)\">\]]*)?"
)
START_RE = re.compile(
    r"https?://(?:www\.)?bettyhacks\.com/forum/?(?=[\s)\]\"'<>]|$)"
)
GITHUB_FORUM_RE = re.compile(
    r"https://github\.com/ghenne/betty-forum/blob/main/([^)#\s<>\]\"]+)"
    r"(#[^\s)<>\]\"]*)?"
)
GITHUB_FORUM_ROOT_RE = re.compile(
    r"https://github\.com/ghenne/betty-forum/?(?=[\s)\]\"'<>]|$)"
)
BOARD_RE = re.compile(
    r"https?://(?:www\.)?bettyhacks\.com/forum/index\.php\?board=(\d+)"
    r"(?:\.([^#\s)\">\]]*))?"
    r"(#[^\s)\">\]]*)?"
)


def load_index() -> tuple[dict, dict]:
    msg = json.loads((META / "msg-index.json").read_text(encoding="utf-8"))
    topics = {
        t["topic_id"]: t
        for t in json.loads((META / "topics.json").read_text(encoding="utf-8"))["topics"]
    }
    return msg, topics


def rel_target(src: Path, target: Path) -> str:
    return Path(os.path.relpath(target, start=src.parent)).as_posix()


def forum_rel(src: Path, rel: str) -> str:
    """Relativer Pfad von der Wiki-Seite zum Forum-Eintrag."""
    target = ROOT / rel
    r = os.path.relpath(target, start=src.parent).replace(os.sep, "/")
    return quote(r, safe="/._-")


def forum_root_rel(src: Path) -> str:
    r = os.path.relpath(ROOT, start=src.parent).replace(os.sep, "/")
    return quote(r, safe="/._-") or "."


def topic_target(src: Path, tid: int, msg: int | None, msg_index: dict, topics: dict) -> str | None:
    entry = topics.get(tid)
    if entry is None:
        return None
    if USE_RELATIVE:
        rel = forum_rel(src, f"topics/{entry['file']}")
    else:
        rel = (
            f"https://github.com/{FORUM_REPO}/blob/{BRANCH}"
            f"/topics/{quote(entry['file'], safe='')}"
        )
    if msg is not None and str(msg) in msg_index:
        rel += f"#msg{msg}"
    return rel


def board_target(src: Path, bid: int) -> str | None:
    name = {1: "News", 5: "Hardware", 6: "Software", 7: "Sonstiges", 8: "Allgemeines", 9: "Off-Topic"}
    if bid not in name:
        return None
    slug = re.sub(r"[^a-z0-9]+", "-", name[bid].lower()).strip("-")
    target = BOARDS_DIR / f"{bid:02d}-{slug}.md"
    if not target.exists():
        return None
    if USE_RELATIVE:
        return forum_rel(src, f"boards/{target.name}")
    return (
        f"https://github.com/{FORUM_REPO}/blob/{BRANCH}"
        f"/boards/{quote(target.name, safe='')}"
    )


def fix_autolinks(text: str, topics: dict) -> str:
    """Wandelt <../../betty-forum/...> in echte Markdown-Links um.

    Markdown-Autolinks funktionieren nur mit absoluten URLs; ein relativer
    Pfad in spitzen Klammern wird sonst als Text angezeigt.
    """
    by_file = {e["file"]: e["title"] for e in topics.values()}
    def repl(m: re.Match) -> str:
        target = m.group(1)
        rel = target.split("#")[0].replace("../../betty-forum/", "")
        title = by_file.get(rel, rel)
        return f"[{title}]({target})"
    return re.sub(r"<((?:\.\./)+betty-forum/(?:topics|boards)/[^>]+)>", repl, text)


def rewrite(text: str, src: Path, msg_index: dict, topics: dict) -> tuple[str, int, list[str]]:
    replaced = 0
    unresolved: list[str] = []

    def topic_sub(m: re.Match) -> str:
        nonlocal replaced
        tid = int(m.group(1))
        suffix = m.group(2) or ""
        frag = m.group(3) or ""
        mm = re.search(r"msg(\d+)", suffix) or re.search(r"msg(\d+)", frag)
        msg = int(mm.group(1)) if mm else None
        target = topic_target(src, tid, msg, msg_index, topics)
        if target is None:
            unresolved.append(m.group(0))
            return m.group(0)
        replaced += 1
        return target

    def board_sub(m: re.Match) -> str:
        nonlocal replaced
        target = board_target(src, int(m.group(1)))
        if target is None:
            unresolved.append(m.group(0))
            return m.group(0)
        replaced += 1
        return target

    def start_sub(m: re.Match) -> str:
        nonlocal replaced
        replaced += 1
        if USE_RELATIVE:
            return forum_root_rel(src)
        return f"https://github.com/{FORUM_REPO}"

    def github_sub(m: re.Match) -> str:
        nonlocal replaced
        replaced += 1
        rel = m.group(1)
        anchor = m.group(2) or ""
        if USE_RELATIVE:
            return forum_rel(src, rel) + anchor
        return f"https://github.com/{FORUM_REPO}/blob/{BRANCH}/{rel}{anchor}"

    text = FORUM_RE.sub(topic_sub, text)
    text = BOARD_RE.sub(board_sub, text)
    text = GITHUB_FORUM_RE.sub(github_sub, text)
    text = START_RE.sub(start_sub, text)
    text = GITHUB_FORUM_ROOT_RE.sub(start_sub, text)
    text = fix_autolinks(text, topics)
    text = add_github_links(text)
    return text, replaced, unresolved


def add_github_links(text: str) -> str:
    """Links werden bereits als GitHub-URLs erzeugt."""
    return text


def main() -> int:
    global FORUM_REPO, BRANCH, USE_RELATIVE
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", help="Dateien oder Verzeichnisse")
    ap.add_argument("--write", action="store_true", help="Aenderungen schreiben")
    ap.add_argument("--backup", action="store_true", help="vorher .bak anlegen")
    ap.add_argument(
        "--forum-repo", default=FORUM_REPO, help="GitHub-Repo (owner/name)"
    )
    ap.add_argument("--branch", default=BRANCH, help="Branch für GitHub-Links")
    ap.add_argument(
        "--github", action="store_true", help="absolute GitHub-URLs statt relativer Pfade"
    )
    ap.add_argument(
        "--wiki-root", help="Wurzel des Wiki-Repos (Default: aus dem Pfad abgeleitet)"
    )
    args = ap.parse_args()
    FORUM_REPO, BRANCH = args.forum_repo, args.branch
    global WIKI_ROOT
    USE_RELATIVE = not args.github
    if args.wiki_root:
        WIKI_ROOT = Path(args.wiki_root).resolve()
    else:
        for raw in args.paths:
            cand = Path(raw)
            if cand.is_dir() and (cand / "pages").is_dir():
                WIKI_ROOT = cand.resolve()
                break
        if WIKI_ROOT is None and args.paths:
            WIKI_ROOT = Path(args.paths[0]).resolve().parent

    msg_index, topics = load_index()
    files: list[Path] = []
    for raw in args.paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            files.append(p)

    total = 0
    changed_files = 0
    all_unresolved: list[tuple[Path, str]] = []
    for src in files:
        original = src.read_text(encoding="utf-8")
        new, count, unresolved = rewrite(original, src, msg_index, topics)
        all_unresolved.extend((src, u) for u in unresolved)
        if count:
            total += count
        if new != original:
            changed_files += 1
            print(f"{src}: {count} Forum-Link(s), Text geändert")
            if args.write:
                if args.backup:
                    shutil.copy2(src, src.with_suffix(src.suffix + ".bak"))
                src.write_text(new, encoding="utf-8")

    mode = "geschrieben" if args.write else "Vorschau (--write zum Schreiben)"
    print(f"\n{total} Link(s) in {changed_files} Datei(en) ersetzt — {mode}")
    if all_unresolved:
        print(f"{len(all_unresolved)} Link(s) ohne lokales Ziel:")
        for src, url in all_unresolved[:20]:
            print(f"  {src}: {url}")
        if len(all_unresolved) > 20:
            print(f"  … und {len(all_unresolved) - 20} weitere")
    return 0


if __name__ == "__main__":
    sys.exit(main())
