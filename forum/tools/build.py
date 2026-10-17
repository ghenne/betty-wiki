#!/usr/bin/env python3
"""Konvertiert den HTML-Cache in ein verlinktes Markdown-Repo.

Erzeugt:
    README.md                  Einstieg und Hinweise
    index.md                   Gesamtindex aller Themen
    boards/<id>-<slug>.md      Board-Uebersichten mit Themenliste
    topics/<id>-<slug>.md      ein Thema pro Datei, alle Beitraege
    autoren/<slug>.md          Beitraege je Autor
    _meta/bericht.md           Abdeckung und Luecken
    _meta/topics.json          Maschinenlesbare Metadaten

Aufruf: python3 tools/build.py
"""

from __future__ import annotations

import html as htmllib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, unquote

from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "_cache" / "html"
BOARDS = ROOT / "boards"
TOPICS = ROOT / "topics"
AUTHORS = ROOT / "autoren"
META = ROOT / "_meta"

WAYBACK_ORIGIN = "https://web.archive.org"
WIKI_REPO_NAME = "betty-wiki"
FORUM_REPO_NAME = "betty-forum"
BRANCH = "main"
WIKI_DIR = ROOT.parent
BOARD_NAMES = {
    1: ("News", "News on BettyHacks.com"),
    5: ("Hardware", "Alle Infos über die Hardware"),
    6: ("Software", "Alle Infos über die Software"),
    7: ("Sonstiges", "Sonstiges Interessantes"),
    8: ("Allgemeines", ""),
    9: ("Off-Topic", ""),
}

DATE_RE = re.compile(
    r"(\d{1,2}\.\s*[A-Za-zÄÖÜäöüß]{3,}\.?\s+\d{4},\s*\d{2}:\d{2})"
)

STOP = {
    "der", "die", "das", "und", "oder", "aber", "mit", "ohne", "für", "fuer",
    "von", "vom", "zum", "zur", "ein", "eine", "einen", "einem", "einer",
    "ist", "sind", "war", "wird", "werden", "hat", "habe", "haben", "kann",
    "können", "koennen", "sich", "nicht", "auch", "noch", "nur", "bei", "aus",
    "auf", "als", "wie", "was", "wer", "wo", "ich", "du", "er", "sie", "es",
    "the", "and", "for", "with", "that", "this", "from", "have", "has",
}


def slugify(text: str, maxlen: int = 60) -> str:
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    text = text.replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue")
    text = text.replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    text = re.sub(r"-{2,}", "-", text)
    return (text[:maxlen].rstrip("-") or "thema")


def clean_title(title: str) -> str:
    title = re.sub(r"\s+-\s+Page\s+\d+\s*$", "", title or "")
    return htmllib.unescape(title).strip() or "(ohne Titel)"


def unwrap_wayback(url: str) -> str:
    m = re.match(r"https?://web\.archive\.org/web/[^/]+/(https?://.*)", url)
    return m.group(1) if m else url


def original_of(url: str) -> str:
    return unwrap_wayback(url or "")


def topic_id_of(url: str) -> int | None:
    m = re.search(r"[?&]topic=(\d+)", original_of(url))
    return int(m.group(1)) if m else None


def board_id_of(url: str) -> int | None:
    m = re.search(r"[?&]board=(\d+)", original_of(url))
    return int(m.group(1)) if m else None


def msg_id_of(url: str) -> int | None:
    m = re.search(r"#msg(\d+)", url or "") or re.search(r"\.msg(\d+)", url or "")
    return int(m.group(1)) if m else None


def wayback_link(original: str, ts: str | None = None) -> str:
    if original.startswith(("mailto:", "#")):
        return original
    if "web.archive.org" in original:
        return original
    stamp = ts or "2012"
    return f"{WAYBACK_ORIGIN}/web/{stamp}/{original}"


class WikiResolver:
    """Loest Links auf bettyhacks.com/wiki/index.php/<Seite> auf lokale
    Wiki-Dateien und GitHub-URLs auf."""

    def __init__(self, wiki_dir: Path) -> None:
        self.by_lower: dict[str, str] = {}
        pages = wiki_dir / "pages"
        if not pages.is_dir():
            return
        for f in pages.glob("*.md"):
            self.by_lower[f.stem.lower()] = f.name

    def resolve(self, original: str) -> str | None:
        m = re.search(r"bettyhacks\.com/wiki/index\.php/([^?#\s]+)(#[^\s)]*)?", original)
        if not m:
            return None
        name = unquote(m.group(1)).replace("_", " ")
        if name.startswith(("User:", "Benutzer:")):
            name = "Benutzer_" + name.split(":", 1)[1]
        elif name.startswith("Talk:"):
            name = "Diskussion_" + name.split(":", 1)[1]
        elif name.startswith("Datei:"):
            name = "Datei_" + name.split(":", 1)[1]
        anchor = ""
        if m.group(2):
            raw = unquote(m.group(2)[1:])
            raw = raw.replace(".2F", "/").replace(".2f", "/").replace("_", " ")
            raw = raw.lower()
            raw = re.sub(r"[^\w\s\-]", "", raw)
            anchor = "#" + raw.replace(" ", "-")
        for key in (name, name.replace(" ", "_")):
            fname = self.by_lower.get(key.lower())
            if fname:
                return f"../../pages/{quote(fname, safe='')}{anchor}"
        return None


class Builder:
    def __init__(self) -> None:
        self.topic_files: dict[int, str] = {}
        self.board_files: dict[int, str] = {}
        self.topic_meta: dict[int, dict] = {}
        self.author_posts: dict[str, list[tuple[int, int, str]]] = defaultdict(list)
        self.incoming: dict[int, set[int]] = defaultdict(set)
        self.outgoing: dict[int, set[int]] = defaultdict(set)
        self.title_words: dict[int, set[str]] = {}
        self.lücken: list[str] = []
        self.warnings: list[str] = []
        self.board_topics: dict[int, list[dict]] = defaultdict(list)
        self.wiki = WikiResolver(WIKI_DIR)

    # ---------- Board-Uebersichten ----------

    def parse_boards(self) -> None:
        for path in sorted(CACHE.glob("board-*.html")):
            bid = int(re.match(r"board-(\d+)-", path.name).group(1))
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
            name, desc = BOARD_NAMES.get(bid, (f"Board {bid}", ""))
            for div in soup.select("div.windowbg"):
                a = div.select_one(".message_index_title a[href*='topic=']")
                if not a:
                    continue
                tid = topic_id_of(a["href"])
                if tid is None:
                    continue
                stats = div.select_one(".stats")
                replies = views = None
                if stats:
                    text = stats.get_text(" ", strip=True)
                    m1 = re.search(r"([\d.,]+)\s*Antworten", text)
                    m2 = re.search(r"([\d.,]+)\s*Aufrufe", text)
                    replies = int(m1.group(1).replace(".", "").replace(",", "")) if m1 else None
                    views = int(m2.group(1).replace(".", "").replace(",", "")) if m2 else None
                starter = div.select_one("p.floatleft a")
                last = div.select_one(".lastpost a[href*='#msg']")
                last_author = None
                if div.select_one(".lastpost"):
                    anchors = div.select_one(".lastpost").select("a[href*='profile']")
                    if anchors:
                        last_author = anchors[-1].get_text(" ", strip=True)
                entry = {
                    "topic_id": tid,
                    "title": clean_title(a.get_text(" ", strip=True)),
                    "starter": starter.get_text(" ", strip=True) if starter else None,
                    "replies": replies,
                    "views": views,
                    "last_date": last.get_text(" ", strip=True) if last else None,
                    "last_author": last_author,
                }
                self.board_topics[bid].append(entry)
            self.board_files[bid] = f"{bid:02d}-{slugify(name)}.md"

    # ---------- Themen ----------

    def parse_topics(self) -> None:
        files: dict[int, list[Path]] = defaultdict(list)
        for path in sorted(CACHE.glob("topic-*.html")):
            m = re.match(r"topic-(\d+)-", path.name)
            if m:
                files[int(m.group(1))].append(path)

        for tid in sorted(files):
            posts: dict[int, dict] = {}
            title = None
            board_id = None
            board_name = None
            views = None
            source = None
            for path in files[tid]:
                soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
                if title is None:
                    title = clean_title(soup.title.string if soup.title else None)
                if board_id is None:
                    for a in soup.select("a[href*='board=']"):
                        bid = board_id_of(a["href"])
                        if bid:
                            board_id = bid
                            board_name = a.get_text(" ", strip=True)
                            break
                wraps = soup.select("div.post_wrapper")
                parsed = (
                    [self.parse_post(w, tid) for w in wraps]
                    if wraps
                    else self.parse_old_posts(soup, tid)
                )
                for post in parsed:
                    if post:
                        posts.setdefault(post["msg_id"], post)
            if not posts:
                self.warnings.append(f"Thema {tid}: keine Beiträge extrahierbar")
                continue
            ordered = [posts[k] for k in sorted(posts)]
            title = title or f"Thema {tid}"
            if board_id is None:
                board_id = 0
                board_name = "Unbekannt"
            self.topic_meta[tid] = {
                "topic_id": tid,
                "title": title,
                "board_id": board_id,
                "board": board_name or BOARD_NAMES.get(board_id, (f"Board {board_id}", ""))[0],
                "posts": ordered,
                "post_count": len(ordered),
                "authors": sorted({p["author"] for p in ordered if p["author"]}),
                "first_date": ordered[0]["date"],
                "last_date": ordered[-1]["date"],
                "source": source or "",
            }
            self.title_words[tid] = {
                w.lower()
                for w in re.findall(r"[A-Za-zÄÖÜäöüß0-9]{4,}", title)
                if w.lower() not in STOP
            }

    def parse_old_posts(self, soup, tid: int) -> list[dict]:
        """SMF-1.x-Layout aelterer Captures: div.post in einer Tabellenzeile."""
        out: list[dict] = []
        for div in soup.select("div.post"):
            tr = div.find_parent("tr")
            if tr is None:
                continue
            author_el = (
                tr.select_one("td b a[href*='action=profile']")
                or tr.select_one("td a[href*='action=profile']")
            )
            author = author_el.get_text(" ", strip=True) if author_el else "(unbekannt)"
            date = ""
            href = ""
            for sm in tr.select("div.smalltext"):
                m = DATE_RE.search(sm.get_text(" ", strip=True))
                if m:
                    date = m.group(1)
                    break
            subj = tr.select_one("div[id^='subject_']")
            msg_id = None
            if subj:
                m = re.search(r"subject_(\d+)", subj.get("id", ""))
                if m:
                    msg_id = int(m.group(1))
            link = tr.select_one("a[href*='#msg']")
            if link:
                href = link.get("href", "")
                if msg_id is None:
                    msg_id = msg_id_of(href)
            if msg_id is None:
                continue
            if not href:
                href = (
                    f"{WAYBACK_ORIGIN}/web/2012/http://bettyhacks.com/forum/"
                    f"index.php?topic={tid}.msg{msg_id}#msg{msg_id}"
                )
            out.append(
                {
                    "msg_id": msg_id,
                    "author": author,
                    "date": date,
                    "href": unwrap_wayback(href),
                    "body_html": str(div),
                    "modified": "",
                    "signature_html": "",
                }
            )
        return out

    def parse_post(self, wrap, tid: int) -> dict | None:
        inner = wrap.select_one(".post .inner")
        if inner is None:
            return None
        msg_id = None
        m = re.match(r"msg_(\d+)", inner.get("id", ""))
        if m:
            msg_id = int(m.group(1))
        author_el = wrap.select_one(".poster h4 a") or wrap.select_one(".poster h4")
        author = author_el.get_text(" ", strip=True) if author_el else "(unbekannt)"
        keyinfo = wrap.select_one(".keyinfo")
        date = ""
        href = ""
        if keyinfo:
            a = keyinfo.select_one("h5 a.smalltext")
            if a:
                date = a.get_text(" ", strip=True)
                href = a.get("href", "")
            m = DATE_RE.search(keyinfo.get_text(" ", strip=True))
            if m:
                date = m.group(1)
        if msg_id is None:
            msg_id = msg_id_of(href) or abs(hash(inner.get_text())) % 10**9
        if not href:
            href = f"{WAYBACK_ORIGIN}/web/2012/http://bettyhacks.com/forum/index.php?topic={tid}.msg{msg_id}#msg{msg_id}"
        modified = ""
        mod = wrap.select_one(".modified")
        if mod:
            modified = mod.get_text(" ", strip=True)
        signature = ""
        sig = wrap.select_one(".signature")
        if sig:
            signature = str(sig)
        return {
            "msg_id": msg_id,
            "author": author,
            "date": date,
            "href": unwrap_wayback(href),
            "body_html": str(inner),
            "modified": modified,
            "signature_html": signature,
        }

    # ---------- HTML -> Markdown ----------

    def to_markdown(self, fragment: str, tid: int) -> str:
        soup = BeautifulSoup(fragment, "lxml")

        for s in soup.select("script, style"):
            s.decompose()
        for s in soup.select("img.smiley"):
            s.decompose()
        for head in soup.select(".codeheader"):
            head.decompose()
        for head in soup.select(".quoteheader"):
            text = head.get_text(" ", strip=True)
            head.replace_with(soup.new_string(f"\n\n> **{text}**\n> "))
        for code in soup.select(".code"):
            pre = soup.new_tag("pre")
            pre.string = code.get_text("\n")
            code.replace_with(pre)
        for q in soup.select(".quote"):
            q.name = "blockquote"

        for a in soup.select("a[href]"):
            href = a["href"]
            original = original_of(href)
            target = self.rewrite_link(original, tid, a.get_text(" ", strip=True))
            if target is None:
                a.unwrap()
            else:
                a["href"] = target

        for img in soup.select("img[src]"):
            src = original_of(img["src"])
            if "Themes/default/images" in src or "avatars/" in src:
                img.decompose()
                continue
            img["src"] = wayback_link(src)

        body = markdownify(
            str(soup),
            heading_style="ATX",
            bullets="-",
            strip=[],
            escape_asterisks=False,
            escape_underscores=False,
        )
        body = re.sub(r"[ \t]+\n", "\n", body)
        body = re.sub(r"\n{3,}", "\n\n", body)
        body = self.add_github_links(body)
        return body.strip()

    def add_github_links(self, body: str) -> str:
        """Links werden bereits als GitHub-URLs erzeugt."""
        return body

    def rewrite_link(self, original: str, tid: int, label: str) -> str | None:
        if original.startswith(("mailto:", "javascript:")):
            return None
        if original.startswith("#"):
            return original
        target_topic = topic_id_of(original)
        if target_topic:
            msg = msg_id_of(original)
            anchor = f"#msg{msg}" if msg else ""
            fname = self.topic_files.get(target_topic)
            if fname:
                self.outgoing[tid].add(target_topic)
                self.incoming[target_topic].add(tid)
                return f"{fname}{anchor}"
            return wayback_link(original)
        target_board = board_id_of(original)
        if target_board:
            fname = self.board_files.get(target_board)
            return f"../boards/{fname}" if fname else wayback_link(original)
        if "action=profile;u=" in original:
            return f"../autoren/uebersicht.md#{slugify(label)}"
        if re.fullmatch(r"https?://(?:www\.)?bettyhacks\.com/forum/?", original):
            return "../index.md"
        wiki = self.wiki.resolve(original)
        if wiki:
            return wiki
        return wayback_link(original)

    # ---------- Ausgabe ----------

    def plan_filenames(self) -> None:
        for bid in self.board_topics:
            name = BOARD_NAMES.get(bid, (f"Board {bid}", ""))[0]
            self.board_files[bid] = f"{bid:02d}-{slugify(name)}.md"
        for tid, meta in self.topic_meta.items():
            self.topic_files[tid] = f"{tid:04d}-{slugify(meta['title'])}.md"

    def related(self, tid: int, limit: int = 6) -> list[int]:
        scores: Counter[int] = Counter()
        for other in self.outgoing.get(tid, set()) | self.incoming.get(tid, set()):
            if other != tid and other in self.topic_meta:
                scores[other] += 3
        mine = self.title_words.get(tid, set())
        for other, words in self.title_words.items():
            if other == tid or other not in self.topic_meta:
                continue
            common = mine & words
            if common:
                scores[other] += len(common)
        return [t for t, _ in scores.most_common(limit) if scores[t] >= 2]

    def write_boards(self) -> None:
        BOARDS.mkdir(exist_ok=True)
        for bid, name in sorted(BOARD_NAMES.items()):
            entries = {e["topic_id"]: e for e in self.board_topics.get(bid, [])}
            # Themen, deren Board aus dem Breadcrumb stammt, ergaenzen
            for tid, meta in self.topic_meta.items():
                if meta["board_id"] == bid and tid not in entries:
                    entries[tid] = {
                        "topic_id": tid,
                        "title": meta["title"],
                        "starter": meta["authors"][0] if meta["authors"] else None,
                        "replies": max(meta["post_count"] - 1, 0),
                        "views": None,
                        "last_date": meta["last_date"],
                        "last_author": None,
                    }
            lines = [
                "---",
                f"board_id: {bid}",
                f'title: "{name[0]}"',
                f'description: "{name[1]}"',
                "---",
                "",
                f"# {name[0]}",
                "",
                name[1] or "",
                "",
                f"[← Zurück zum Index](../index.md) · "
                f"{len(entries)} Themen gelistet · "
                f"{sum(1 for e in entries.values() if e['topic_id'] in self.topic_files)} im Archiv · "
                f"{sum((e['replies'] or 0) + 1 for e in entries.values())} Beiträge laut Forum",
                "",
                "| Thema | Antworten | Aufrufe | Letzter Beitrag |",
                "|---|---:|---:|---|",
            ]
            for e in sorted(entries.values(), key=lambda x: x["topic_id"]):
                fname = self.topic_files.get(e["topic_id"])
                label = e["title"].replace("|", "\\|")
                link = (
                    f"[{label}](../topics/{fname})"
                    if fname
                    else f"{label} *(nicht archiviert)*"
                )
                last = " ".join(
                    x for x in [e["last_date"], e["last_author"] and f"({e['last_author']})"] if x
                )
                lines.append(
                    f"| {link} | {e['replies'] if e['replies'] is not None else ''} "
                    f"| {e['views'] if e['views'] is not None else ''} | {last} |"
                )
            lines += ["", "---", "", "*Quelle: Wayback-Sicherung des Bettyhacks-Forums.*", ""]
            (BOARDS / self.board_files[bid]).write_text("\n".join(lines), encoding="utf-8")

    def write_topics(self) -> None:
        TOPICS.mkdir(exist_ok=True)
        for tid, meta in sorted(self.topic_meta.items()):
            fname = self.topic_files[tid]
            board = self.board_files.get(meta["board_id"], "../index.md")
            authors = ", ".join(meta["authors"][:8])
            if len(meta["authors"]) > 8:
                authors += " …"
            lines = [
                "---",
                f'title: "{meta["title"].replace(chr(34), chr(39))}"',
                f"topic_id: {tid}",
                f'board: "{meta["board"]}"',
                f"board_id: {meta['board_id']}",
                f"posts: {meta['post_count']}",
                f'first_post: "{meta["first_date"]}"',
                f'last_post: "{meta["last_date"]}"',
                f'authors: [{", ".join(json.dumps(a, ensure_ascii=False) for a in meta["authors"])}]',
                f'source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic={tid}.0"',
                "---",
                "",
                f"# {meta['title']}",
                "",
                f"[← {meta['board']}](../boards/{board}) · "
                f"Thema {tid} · {meta['post_count']} Beiträge · "
                f"{meta['first_date']} – {meta['last_date']}",
                "",
            ]
            if authors:
                lines += [f"Beteiligt: {authors}", ""]
            lines += ["---", ""]
            for i, post in enumerate(meta["posts"], 1):
                lines += [
                    f'<a id="msg{post["msg_id"]}"></a>',
                    "",
                    f"## {i}. {post['author']} · {post['date']}",
                    "",
                ]
                body = self.to_markdown(post["body_html"], tid)
                if body:
                    lines += [body, ""]
                if post["modified"]:
                    lines += [f"*{post['modified']}*", ""]
                if post["signature_html"]:
                    sig = self.to_markdown(post["signature_html"], tid)
                    if sig:
                        lines += ["<sub>", "", sig, "", "</sub>", ""]
                lines += [f"[Permalink]({post['href']})", "", "---", ""]
            rel = self.related(tid)
            if rel:
                lines += ["## Verwandte Themen", ""]
                for other in rel:
                    lines.append(
                        f"- [{self.topic_meta[other]['title']}]({self.topic_files[other]})"
                    )
                lines.append("")
            lines += [
                f"[← Zurück zu {meta['board']}](../boards/{board}) · "
                "[Gesamtindex](../index.md)",
                "",
            ]
            (TOPICS / fname).write_text("\n".join(lines), encoding="utf-8")

    def write_authors(self) -> None:
        AUTHORS.mkdir(exist_ok=True)
        for tid, meta in self.topic_meta.items():
            for i, post in enumerate(meta["posts"], 1):
                self.author_posts[post["author"]].append((tid, post["msg_id"], post["date"]))
        lines = [
            "# Autoren",
            "",
            "Alle im Archiv gefundenen Beitragenden mit ihren Beiträgen.",
            "",
        ]
        for author in sorted(self.author_posts, key=str.lower):
            entries = self.author_posts[author]
            tid_count = len({t for t, _m, _d in entries})
            lines.append(f'<a id="{slugify(author)}"></a>')
            lines.append("")
            lines.append(f"## {author}")
            lines.append("")
            lines.append(f"{len(entries)} Beiträge in {tid_count} Themen")
            lines.append("")
            for tid, msg, date in entries:
                lines.append(
                    f"- {date}: [{self.topic_meta[tid]['title']}]"
                    f"(../topics/{self.topic_files[tid]}#msg{msg})"
                )
            lines.append("")
        (AUTHORS / "uebersicht.md").write_text("\n".join(lines), encoding="utf-8")

    def write_index(self) -> None:
        total_posts = sum(m["post_count"] for m in self.topic_meta.values())
        lines = [
            "# Bettyhacks-Forum — Gesamtindex",
            "",
            f"{len(self.topic_meta)} Themen · {total_posts} Beiträge · "
            f"{len(self.author_posts)} Autoren",
            "",
            "## Boards",
            "",
            "| Board | Themen | Beiträge |",
            "|---|---:|---:|",
        ]
        for bid, (name, _desc) in sorted(BOARD_NAMES.items()):
            tids = [t for t, m in self.topic_meta.items() if m["board_id"] == bid]
            posts = sum(self.topic_meta[t]["post_count"] for t in tids)
            lines.append(f"| [{name}](boards/{self.board_files[bid]}) | {len(tids)} | {posts} |")
        lines += ["", "## Alle Themen", "", "| ID | Thema | Board | Beiträge |", "|---:|---|---|---:|"]
        for tid in sorted(self.topic_meta):
            m = self.topic_meta[tid]
            label = m["title"].replace("|", "\\|")
            lines.append(
                f"| {tid} | [{label}](topics/{self.topic_files[tid]}) "
                f"| {m['board']} | {m['post_count']} |"
            )
        lines += [
            "",
            "## Nachschlagen",
            "",
            "- [Alle Autoren](autoren/uebersicht.md)",
            "- [Sprungziele nach Beitrags-ID](_meta/sprungziele.md)",
            "- [Abdeckungsbericht](_meta/bericht.md)",
            "",
        ]
        (ROOT / "index.md").write_text("\n".join(lines), encoding="utf-8")

    def write_readme(self) -> None:
        total_posts = sum(m["post_count"] for m in self.topic_meta.values())
        readme = f"""# Bettyhacks-Forum (Archiv)

Lokale, durchsuchbare und untereinander verlinkte Markdown-Fassung des
Bettyhacks-Forums, extrahiert aus der Wayback-Machine-Sicherung.

## Umfang

- **{len(self.topic_meta)} Themen** mit **{total_posts} Beiträgen**
- **{len(self.board_topics)} Boards**: News, Hardware, Software, Sonstiges,
  Allgemeines, Off-Topic
- **{len(self.author_posts)} Autoren** mit Beitragslisten
- Quelle: `https://web.archive.org/web/*/bettyhacks.com/forum/*`
  (Captures 2007–2026, je Seite die neueste verfügbare Fassung)

## Struktur

```text
README.md              dieser Einstieg
index.md               Gesamtindex (Boards, Themen, Autoren)
boards/                Board-Übersichten mit Themenlisten
topics/                ein Thread pro Datei, alle Beiträge chronologisch
autoren/uebersicht.md  alle Beitragenden mit ihren Beiträgen
_meta/bericht.md       Abdeckung, Lücken, technische Hinweise
_meta/topics.json      maschinenlesbare Metadaten
tools/                 Crawler und Generator (Python)
```

Jede Themendatei beginnt mit YAML-Frontmatter (`topic_id`, `board`,
`posts`, `authors`, `source`). Interne Links sind relativ und funktionieren
direkt in Gitea; externe Links zeigen auf die Wayback-Sicherung.

## Verwandte Repositories

- Wiki: [betty-wiki](../README.md) (Seiten, Anleitungen, Hardwareinfos)
- Dieses Forum-Archiv: `betty-forum` (dieses Repository)

## Einstieg

- [Gesamtindex](index.md)
- [Software](boards/06-software.md) · [Hardware](boards/05-hardware.md) ·
  [Sonstiges](boards/07-sonstiges.md)
- [Autoren](autoren/uebersicht.md)
- [Sprungziele nach Beitrags-ID](_meta/sprungziele.md) — für Links wie
  `?topic=51.msg314#msg314`
- [Abdeckungsbericht](_meta/bericht.md)

## Nutzung

Durchsuchen: In Gitea die Repository-Suche verwenden, lokal z. B.

```bash
grep -ri "mpd" topics/ boards/
rg -i "scart" topics/
```

Neu erzeugen (nur nötig, wenn der Cache geändert wurde):

```bash
python3 tools/crawl.py   # lädt fehlende Seiten in _cache/html
python3 tools/build.py   # schreibt boards/, topics/, autoren/, index.md
```

## Verknüpfung mit dem Wiki

Das Wiki (`betty-wiki`) und dieses Forum-Archiv (`betty-forum`) verweisen
aufeinander. Beide Repositories müssen nebeneinander liegen:

```text
betty-wiki/
betty-forum/
``` Forum-Links im Wiki der Form
`?topic=51.msg314#msg314` werden mit einem Hilfsskript auf die lokalen
GitHub-Seiten umgeschrieben:

```bash
python3 tools/link_forum.py ../Betty_Wiki_md          # Vorschau
python3 tools/link_forum.py ../Betty_Wiki_md --write  # anwenden
```

Die Zuordnung Beitrags-ID → Themendatei steht in
`_meta/msg-index.json`; eine lesbare Tabelle bietet
[Sprungziele](_meta/sprungziele.md).

## Hinweise

- Das Archiv ist unvollständig: Nicht jede Seite wurde von der Wayback
  Machine erfasst. Fehlende Themen und Seiten stehen im
  [Abdeckungsbericht](_meta/bericht.md).
- Beiträge sind unverändert übernommen, inklusive Rechtschreibung und
  damaliger Umlaute/Schreibweisen.
- Die Inhalte stammen aus einem öffentlichen Forum; Rechte an den Texten
  liegen bei den jeweiligen Autoren. Dieses Repository ist eine
  technische Sicherung für Recherchezwecke.
"""
        (ROOT / "README.md").write_text(readme, encoding="utf-8")

    def write_msg_index(self) -> None:
        """Nachschlagewerk fuer Links der Form topic=ID.msgNNN#msgNNN."""
        index: dict[str, dict] = {}
        by_topic: dict[int, list[dict]] = defaultdict(list)
        for tid, meta in sorted(self.topic_meta.items()):
            for post in meta["posts"]:
                entry = {
                    "topic_id": tid,
                    "topic": meta["title"],
                    "file": self.topic_files[tid],
                    "anchor": f"#msg{post['msg_id']}",
                    "author": post["author"],
                    "date": post["date"],
                }
                index[str(post["msg_id"])] = entry
                by_topic[tid].append(entry)
        (META / "msg-index.json").write_text(
            json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        lines = [
            "# Sprungziele (Beitrags-IDs)",
            "",
            "Auflösung für Links der Form "
            "`http://bettyhacks.com/forum/index.php?topic=51.msg314#msg314`.",
            "Die Zahl nach `msg` ist die Beitrags-ID; darunter steht der lokale Link.",
            "",
        ]
        for tid in sorted(by_topic):
            meta = self.topic_meta[tid]
            fname = self.topic_files[tid]
            lines += [f"## {tid} – {meta['title']}", ""]
            for e in by_topic[tid]:
                lines.append(
                    f"- `msg{e['anchor'][4:]}` · {e['author']} · {e['date']}: "
                    f"[Beitrag](../topics/{fname}{e['anchor']})"
                )
            lines.append("")
        (META / "sprungziele.md").write_text("\n".join(lines), encoding="utf-8")

    def write_meta(self) -> None:
        META.mkdir(exist_ok=True)
        data = {
            "topics": [
                {
                    "topic_id": tid,
                    "title": m["title"],
                    "board": m["board"],
                    "board_id": m["board_id"],
                    "posts": m["post_count"],
                    "authors": m["authors"],
                    "first_post": m["first_date"],
                    "last_post": m["last_date"],
                    "file": self.topic_files[tid],
                }
                for tid, m in sorted(self.topic_meta.items())
            ],
            "warnings": self.warnings,
        }
        (META / "topics.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        crawled = sorted(int(p.stem.split("-")[1]) for p in CACHE.glob("topic-*.html"))
        covered = set(self.topic_meta)
        lines = [
            "# Abdeckungsbericht",
            "",
            f"- Themen mit Inhalt: **{len(covered)}**",
            f"- Beiträge: **{sum(m['post_count'] for m in self.topic_meta.values())}**",
            f"- HTML-Seiten im Cache: **{len(list(CACHE.glob('*.html')))}**",
            "",
            "## Hinweise",
            "",
        ]
        for w in self.warnings:
            lines.append(f"- {w}")
        if not self.warnings:
            lines.append("- Keine Extraktionswarnungen.")
        lines += [
            "",
            "## Themen ohne extrahierbare Beiträge",
            "",
        ]
        missing = sorted(set(crawled) - covered)
        if missing:
            for tid in missing:
                lines.append(f"- Thema {tid}: Seiten vorhanden, aber keine Beiträge erkannt")
        else:
            lines.append("- keine")
        expected: dict[int, int] = {}
        for entries in self.board_topics.values():
            for e in entries:
                if e.get("replies") is not None:
                    expected[e["topic_id"]] = e["replies"] + 1
        gaps = []
        not_archived = []
        for tid, exp in sorted(expected.items()):
            if tid not in self.topic_meta:
                not_archived.append((tid, exp))
                continue
            got = self.topic_meta[tid]["post_count"]
            if got < exp:
                gaps.append((tid, got, exp))
        lines += ["", "## Nicht archivierte Themen", ""]
        if not_archived:
            lines += [
                f"{len(not_archived)} in den Board-Listen genannte Themen haben "
                "keine archivierte Themenseite:",
                "",
                "| Thema | Beiträge laut Forum |",
                "|---:|---:|",
            ]
            for tid, exp in not_archived:
                lines.append(f"| {tid} | {exp} |")
        else:
            lines.append("- keine")
        lines += ["", "## Themen mit fehlenden Beiträgen", ""]
        if gaps:
            lines += [
                "| Thema | extrahiert | laut Forum | fehlend |",
                "|---:|---:|---:|---:|",
            ]
            for tid, got, exp in gaps:
                title = self.topic_meta.get(tid, {}).get("title", "?")
                lines.append(f"| {tid} ({title}) | {got} | {exp} | {exp - got} |")
        else:
            lines.append("- keine bekannten Lücken")
        lines += [
            "",
            "## Bekannte Archivlücken",
            "",
            "- Seiten, die die Wayback Machine nicht erfasst hat, können nicht",
            "  rekonstruiert werden. Der Crawler protokolliert sie in",
            "  `_cache/failed.txt`.",
            "- Bei Themen, die nur über `topic=ID.msgNNN` archiviert sind, fehlt",
            "  unter Umständen die erste Seite; vorhandene Beiträge sind trotzdem",
            "  vollständig enthalten und werden über die Beitrags-ID dedupliziert.",
            "",
        ]
        (META / "bericht.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    b = Builder()
    b.parse_boards()
    b.parse_topics()
    b.plan_filenames()
    b.write_boards()
    b.write_topics()
    b.write_authors()
    b.write_index()
    b.write_readme()
    b.write_msg_index()
    b.write_meta()
    print(
        f"Fertig: {len(b.topic_meta)} Themen, "
        f"{sum(m['post_count'] for m in b.topic_meta.values())} Beiträge, "
        f"{len(b.author_posts)} Autoren"
    )


if __name__ == "__main__":
    main()
