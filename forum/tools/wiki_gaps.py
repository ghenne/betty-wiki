#!/usr/bin/env python3
"""Ermittelt Forum-Themen, deren Inhalte im Wiki fehlen.

Vergleicht Titel und spezifische Fachbegriffe der Forum-Threads mit dem
Volltext des Wiki-Repos. Ausgabe ist eine lokale Arbeitsdatei
(WIKI-LUECKEN.md), die nicht eingecheckt wird.

Aufruf: python3 tools/wiki_gaps.py [--wiki ../betty-wiki] [--out WIKI-LUECKEN.md]
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WIKI = ROOT.parent / "betty-wiki"
DEFAULT_OUT = ROOT / "WIKI-LUECKEN.md"

STOP = set(
    """der die das und oder aber mit ohne für fuer von vom zum zur ein eine einen
    einem einer ist sind war wird werden hat habe haben kann können koennen sich
    nicht auch noch nur bei aus auf als wie was wer wo ich du er sie es wir ihr
    den dem des dieser diese dieses dass daß dann da dort hier so sehr mehr
    wenn weil aber auch schon immer wieder noch etwas alles allen alle allem
    thema beitrag beiträge beitraege antwort antworten frage fragen problem
    probleme hallo danke bitte gruß grüße gruesse moin hi hey ok okay
    the and for with that this from have has was were are you your not
    betty bettys bettyhacks forum wiki
    """.split()
)

KEYWORDS = {
    "Boop": ["boop", "menu", "menü", "taste", "tasten", "macro", "makro", "skript", "script"],
    "LPCTool / Flashen": ["lpctool", "flash", "flashen", "upload", "jtag", "openocd", "bootloader", "u-boot", "uboot"],
    "Toolchain / Build": ["gcc", "toolchain", "make", "makefile", "codesourcery", "cygwin", "linux", "kompil", "compil", "build", "svn"],
    "Firmware / Update": ["firmware", "update", "dump", "recovery", "serial", "log", "boot"],
    "Anwendungen": ["mpd", "vdr", "x10", "funksteckdose", "funksteckdosen", "fernsteuer", "ir", "infrarot", "oszi", "oszilloskop", "moodpxl", "sensor", "netzwerk", "lcdproc", "lirc"],
    "Hardware allg.": ["scart", "tae", "adapter", "pin", "pins", "spannung", "strom", "akku", "laderegler", "usb", "kabel", "platine"],
    "Display": ["lcd", "display", "graustufen", "kontrast", "hintergrund"],
    "Funk": ["cc1100", "rfm12", "funk", "433", "868", "antenne", "transceiver"],
    "Schnittstellen": ["uart", "spi", "i2c", "iic", "rs232", "seriell", "ppm", "pwm", "adc", "gpio", "jtag"],
}


def tokens(text: str) -> list[str]:
    text = text.lower()
    words = re.findall(r"[a-zäöüß0-9][a-zäöüß0-9_+#.\-]{2,}", text)
    out = []
    for w in words:
        w = w.strip("._-#+")
        if len(w) >= 3 and w not in STOP and not w.isdigit():
            out.append(w)
    return out


def load_wiki(wiki: Path) -> tuple[set[str], dict[str, set[str]]]:
    full: set[str] = set()
    page_tokens: dict[str, set[str]] = {}
    for f in wiki.glob("pages/*.md"):
        text = f.read_text(encoding="utf-8", errors="replace")
        toks = set(tokens(text))
        page_tokens[f.stem] = toks
        full |= toks
    return full, page_tokens


def best_wiki_title(ftitle: str, page_tokens: dict[str, set[str]]) -> tuple[str, float]:
    ft = set(tokens(ftitle))
    if not ft:
        return "", 0.0
    best, best_score = "", 0.0
    for name, toks in page_tokens.items():
        if not toks:
            continue
        common = ft & toks
        if not common:
            continue
        # Containment des Forum-Titels in der Wiki-Seite
        score = len(common) / len(ft)
        if score > best_score:
            best, best_score = name, score
    return best, best_score


def first_paragraph(topic_file: Path) -> str:
    text = topic_file.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^## 1\..*?\n\n(.*?)(?:\n\n|\Z)", text, re.S | re.M)
    body = m.group(1) if m else ""
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    body = re.sub(r"[*_>`#]", "", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body[:240]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", type=Path, default=DEFAULT_WIKI)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    wiki_full, page_tokens = load_wiki(args.wiki)
    meta = json.loads((ROOT / "_meta/topics.json").read_text(encoding="utf-8"))
    topics = meta["topics"]

    # Dokumentfrequenz der Forum-Begriffe
    doc_tokens: dict[int, list[str]] = {}
    df: Counter[str] = Counter()
    for t in topics:
        text = (ROOT / "topics" / t["file"]).read_text(encoding="utf-8", errors="replace")
        toks = tokens(t["title"] + "\n" + text)
        doc_tokens[t["topic_id"]] = toks
        df.update(set(toks))
    n = len(topics)

    rows = []
    for t in topics:
        toks = doc_tokens[t["topic_id"]]
        tf = Counter(toks)
        scored = []
        for w, c in tf.items():
            if c < 2:
                continue
            idf = math.log((n + 1) / (df[w] + 1))
            scored.append((c * idf, w))
        scored.sort(reverse=True)
        spec = [w for _s, w in scored[:12]]
        missing = [w for w in spec if w not in wiki_full]
        title, tscore = best_wiki_title(t["title"], page_tokens)
        gap = len(missing) / len(spec) if spec else 0.0
        rows.append(
            {
                **t,
                "gap": gap,
                "missing": missing,
                "wiki_title": title,
                "wiki_score": tscore,
                "snippet": first_paragraph(ROOT / "topics" / t["file"]),
            }
        )

    # Nur Themen mit echter Luecke: keine brauchbare Titelentsprechung
    # oder hoher Anteil fehlender Fachbegriffe.
    candidates = [
        r for r in rows
        if (r["wiki_score"] < 0.5 or r["gap"] >= 0.5) and r["posts"] >= 2
    ]
    candidates.sort(key=lambda r: (-r["gap"], -r["posts"]))

    def cluster(title: str) -> str:
        low = title.lower()
        for name, kws in KEYWORDS.items():
            if any(k in low for k in kws):
                return name
        return "Sonstiges"

    groups: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for r in candidates:
        groups[r["board"]][cluster(r["title"])].append(r)

    lines = [
        "# Wiki-Lücken: Forum-Inhalte ohne Wiki-Entsprechung",
        "",
        "> Lokale Arbeitsdatei — **nicht eingecheckt**.  ",
        "> Entscheidung pro Eintrag: `[ ]` offen, `[x]` übernehmen, `[-]` nicht übernehmen.  ",
        "> Ergänze bei Bedarf `Übertragen: ja/nein/teilweise` und Stichworte.",
        "",
        f"Aus {len(topics)} Forum-Themen wurden **{len(candidates)} Kandidaten** "
        "ermittelt, deren Titel oder Fachbegriffe im Wiki fehlen. "
        "Automatische Heuristik: Titelabgleich plus seltene Fachbegriffe; "
        "Support-/Frage-Threads sind nicht vollständig herausgefiltert.",
        "",
    ]

    board_order = ["Software", "Hardware", "Sonstiges", "Allgemeines", "News"]
    for board in board_order:
        if board not in groups:
            continue
        lines += [f"## {board}", ""]
        for cluster_name in sorted(groups[board]):
            lines += [f"### {cluster_name}", ""]
            for r in groups[board][cluster_name]:
                wiki_hint = (
                    f"Wiki-Treffer: `{r['wiki_title']}` (Titelabdeckung "
                    f"{r['wiki_score']:.0%})"
                    if r["wiki_score"] >= 0.3
                    else "Wiki: keine passende Seite gefunden"
                )
                missing = ", ".join(f"`{w}`" for w in r["missing"][:8]) or "—"
                lines += [
                    f"- [ ] **Thema {r['topic_id']} – {r['title']}** "
                    f"({r['posts']} Beiträge, {r['first_post'][:16]})",
                    f"  - {wiki_hint}",
                    f"  - Fehlende Begriffe im Wiki: {missing}",
                    f"  - Inhalt: {r['snippet'] or '—'}",
                    f"  - [Thread](topics/{r['file']})",
                ]
        lines.append("")

    lines += [
        "## Hinweise",
        "",
        "- Die Liste ist heuristisch. Ein Titel-Treffer bedeutet nicht, dass "
        "der Inhalt im Wiki steht; umgekehrt kann ein fehlender Titel auf "
        "eine reine Support-Frage hindeuten.",
        "- Vor dem Übertragen den Thread kurz gegen die genannte Wiki-Seite "
        "prüfen (Stand 2007–2012, teils veraltet).",
        "- Diese Datei ist über `.git/info/exclude` lokal ausgeschlossen.",
        "",
    ]
    args.out.write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(candidates)} Kandidaten -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
