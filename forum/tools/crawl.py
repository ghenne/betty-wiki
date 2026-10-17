#!/usr/bin/env python3
"""Crawlt die Wayback-Sicherung des Bettyhacks-Forums in einen lokalen Cache.

Der Cache ist die Arbeitsgrundlage fuer tools/build.py: erst komplett
herunterladen, dann offline konvertieren. So sind Konvertierungslaeufe
wiederholbar, ohne das Archiv erneut zu belasten.

Pro Seite wird die NEUESTE verfuegbare Capture verwendet. Das Forum war
bis 2026 online, daher sind spaetere Captures vollstaendiger als die
2012er Sicherung.

Aufruf:
    python3 tools/crawl.py            # Boards + alle Themen
    python3 tools/crawl.py --boards   # nur Board-Uebersichten
    python3 tools/crawl.py --limit 5  # zum Testen
    python3 tools/crawl.py --force    # Cache ignorieren
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

import requests

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "_cache"
HTML = CACHE / "html"
CDX_FILE = CACHE / "cdx" / "forum.json"
MANIFEST = CACHE / "manifest.jsonl"

BASE = "http://bettyhacks.com/forum/index.php"
WAYBACK = "https://web.archive.org/web/{ts}id_/{url}"
DELAY = 1.0
RETRIES = (5, 15, 45, 90)

SESSION = requests.Session()
SESSION.headers.update(
    {"User-Agent": "bettyhacks-forum-archive/1.0 (private research)"}
)


def log(msg: str) -> None:
    print(msg, flush=True)


def load_cdx() -> list[tuple[str, str]]:
    """Liste (original_url, timestamp), statuscode 200."""
    if not CDX_FILE.exists():
        log("CDX wird geladen ...")
        url = (
            "http://web.archive.org/cdx/search/cdx"
            "?url=bettyhacks.com/forum/index.php&matchType=prefix"
            "&output=json&collapse=urlkey&filter=statuscode:200"
            "&fl=original,timestamp,statuscode"
        )
        r = SESSION.get(url, timeout=180)
        r.raise_for_status()
        CDX_FILE.write_text(r.text, encoding="utf-8")
    rows = json.loads(CDX_FILE.read_text(encoding="utf-8"))
    return [(o, ts) for o, ts, _s in rows[1:]]


def page_key(url: str) -> tuple[str, int, int] | None:
    """(kind, id, offset) oder None.

    msg-Links werden verworfen (sie zeigen auf die Seite der jeweiligen
    Nachricht). prev_next-Links werden verworfen: SMF laesst die topic-ID
    in der URL stehen, zeigt aber das naechste/vorherige Thema an.
    """
    if "prev_next=" in url:
        return None
    if "topic=" in url:
        kind = "topic"
        m = re.search(r"[?&]topic=(\d+)(?:\.([^&;#]*))?", url)
    elif "board=" in url:
        kind = "board"
        m = re.search(r"[?&]board=(\d+)(?:\.([^&;#]*))?", url)
    else:
        return None
    if not m:
        return None
    ident = int(m.group(1))
    suffix = m.group(2)
    if suffix is None or suffix == "":
        off = 0
    elif suffix.isdigit():
        off = int(suffix)
    else:
        return None  # z.B. msg1974: nicht als Offsets nutzbar
    return kind, ident, off


def looks_right(kind: str, ident: int, body: str) -> bool:
    """Prueft, ob die geladene Seite wirklich zum angefragten Ziel gehoert."""
    if kind == "topic":
        return bool(re.search(rf"topic={ident}\.msg\d+", body))
    return bool(re.search(rf"board={ident}\.", body))


def collect_targets(cdx: list[tuple[str, str]]) -> dict[tuple[str, int, int], tuple[str, str]]:
    """Beste (neueste) URL je Seite."""
    best: dict[tuple[str, int, int], tuple[str, str]] = {}
    for url, ts in cdx:
        key = page_key(url)
        if key is None:
            continue
        old = best.get(key)
        if old is None or ts > old[1]:
            best[key] = (url, ts)
    return best


def cache_path(kind: str, ident: int, off: int) -> Path:
    return HTML / f"{kind}-{ident:04d}-{off:04d}.html"


def fetch(
    target: tuple[str, str], dest: Path, kind: str, ident: int,
    force: bool = False,
) -> bool:
    url, ts = target
    if dest.exists() and dest.stat().st_size > 2000 and not force:
        if looks_right(kind, ident, dest.read_text(encoding="utf-8")):
            return True
        log("    Cache-Datei gehoert nicht zum Ziel, lade neu")
        dest.unlink(missing_ok=True)
    wayback = WAYBACK.format(ts=ts, url=url)
    for attempt in range(len(RETRIES) + 1):
        if attempt:
            wait = RETRIES[attempt - 1]
            log(f"    warte {wait}s ...")
            time.sleep(wait)
        try:
            r = SESSION.get(wayback, timeout=120)
            if r.status_code == 404:
                log(f"    NICHT ARCHIVIERT: {url}")
                return False
            if r.status_code in (429, 500, 502, 503, 504):
                log(f"    HTTP {r.status_code}, Retry")
                continue
            r.raise_for_status()
            body = r.text
            if "has not archived that URL" in body or len(body) < 1500:
                log(f"    LEER/NICHT ARCHIVIERT: {url}")
                return False
            if not looks_right(kind, ident, body):
                log("    FALSCHE SEITE (Validierung), verworfen")
                continue
            dest.write_text(body, encoding="utf-8")
            with MANIFEST.open("a", encoding="utf-8") as fh:
                fh.write(
                    json.dumps(
                        {"url": url, "wayback_ts": ts, "capture": wayback},
                        ensure_ascii=False,
                    )
                    + "\n"
                )
            return True
        except requests.RequestException as exc:
            log(f"    Fehler ({exc.__class__.__name__}), Retry")
    log(f"    AUFGEGEBEN: {url}")
    return False


TOPIC_LINK_RE = re.compile(r"[?&]topic=(\d+)\.(\d+)")
BOARD_LINK_RE = re.compile(r"[?&]board=(\d+)\.(\d+)")


def msg_topics(cdx: list[tuple[str, str]]) -> dict[int, tuple[str, str]]:
    """Topics, die nur als topic=ID.msgNNN archiviert sind -> neueste URL."""
    out: dict[int, tuple[str, str]] = {}
    for url, ts in cdx:
        m = re.search(r"[?&]topic=(\d+)\.msg\d+", url)
        if not m:
            continue
        tid = int(m.group(1))
        if tid not in out or ts > out[tid][1]:
            out[tid] = (url, ts)
    return out


def crawl_msg_only(
    cdx: list[tuple[str, str]],
    already: set[int],
    force: bool = False,
) -> list[int]:
    """Laedt msg-Seiten und daraus die verlinkten nummerischen Seiten."""
    only = {tid: v for tid, v in msg_topics(cdx).items() if tid not in already}
    log(f"\n=== {len(only)} Themen nur ueber msg-Links ===")
    failed: list[int] = []
    for i, (tid, target) in enumerate(sorted(only.items()), 1):
        log(f"[{i}/{len(only)}] Thema {tid} (msg)")
        dest = HTML / f"topic-{tid:04d}-msg.html"
        if not fetch(target, dest, "topic", tid, force=force):
            failed.append(tid)
            continue
        html = dest.read_text(encoding="utf-8")
        offs = {int(o) for t, o in TOPIC_LINK_RE.findall(html) if int(t) == tid}
        if not offs:
            # Einzige Seite: als Seite 0 bereitstellen.
            (HTML / f"topic-{tid:04d}-0000.html").write_text(html, encoding="utf-8")
            log("    einzelne Seite uebernommen")
        for off in sorted(offs):
            p = cache_path("topic", tid, off)
            if p.exists():
                continue
            url = f"{BASE}?topic={tid}.{off}"
            # Neueste Capture fuer diese Seite suchen, sonst msg-Timestamp.
            ts = target[1]
            for u, t in cdx:
                if re.search(rf"[?&]topic={tid}\.{off}(?:[&;]|$)", u) and t > ts:
                    ts = t
            if not fetch((url, ts), p, "topic", tid, force=force):
                failed.append(tid)
            time.sleep(DELAY)
        time.sleep(DELAY)
    return failed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--boards", action="store_true", help="nur Board-Uebersichten")
    ap.add_argument("--msg", action="store_true", help="nur msg-only Themen")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    HTML.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    cdx = load_cdx()
    targets = collect_targets(cdx)
    boards = {k: v for k, v in targets.items() if k[0] == "board"}
    topics = {k: v for k, v in targets.items() if k[0] == "topic"}
    log(f"CDX: {len(cdx)} URLs -> {len(boards)} Board-Seiten, {len(topics)} Topic-Seiten")

    failed: list[str] = []
    if args.msg:
        f = crawl_msg_only(cdx, set(), force=args.force)
        (CACHE / "msg_failed.txt").write_text(
            "\n".join(str(t) for t in f) + "\n", encoding="utf-8"
        )
        return 0

    for kind, group in (("board", boards), ("topic", topics)):
        keys = sorted(group)
        if kind == "topic" and args.boards:
            continue
        if kind == "topic" and args.limit:
            limited = sorted({k[1] for k in keys})[: args.limit]
            keys = [k for k in keys if k[1] in limited]
        for i, key in enumerate(keys, 1):
            _, ident, off = key
            log(f"[{i}/{len(keys)}] {kind} {ident} offset {off}")
            dest = cache_path(*key)
            if not fetch(group[key], dest, key[0], key[1], force=args.force):
                failed.append(f"{kind} {ident}.{off}")
            time.sleep(DELAY)

    if not args.boards:
        failed_ids = crawl_msg_only(cdx, {k[1] for k in topics}, force=args.force)
        failed += [f"topic {t} (msg)" for t in failed_ids]

    (CACHE / "failed.txt").write_text("\n".join(failed) + "\n", encoding="utf-8")
    topic_ids = sorted({k[1] for k in topics} | set(msg_topics(cdx)))
    (CACHE / "topics.txt").write_text(
        "\n".join(str(t) for t in topic_ids) + "\n", encoding="utf-8"
    )
    log(f"\nFertig. Themen: {len(topic_ids)}, fehlgeschlagene Seiten: {len(failed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
