# Bettyhacks-Forum (Archiv)

Lokale, durchsuchbare und untereinander verlinkte Markdown-Fassung des
Bettyhacks-Forums, extrahiert aus der Wayback-Machine-Sicherung. Sie liegt
als Unterverzeichnis `forum/` im Betty-Wiki-Repository.

## Umfang

- **196 Themen** mit **1444 Beiträgen**
- **5 Boards**: News, Hardware, Software, Sonstiges,
  Allgemeines, Off-Topic
- **185 Autoren** mit Beitragslisten
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
direkt in der Web-Oberfläche (Gitea/GitHub); externe Links zeigen auf die Wayback-Sicherung.

## Verwandte Bereiche

- Wiki: [betty-wiki](../README.md) (Seiten, Anleitungen, Hardwareinfos)
- Dieses Forum-Archiv: `forum/` in diesem Repository

## Einstieg

- [Gesamtindex](index.md)
- [Software](boards/06-software.md) · [Hardware](boards/05-hardware.md) ·
  [Sonstiges](boards/07-sonstiges.md)
- [Autoren](autoren/uebersicht.md)
- [Sprungziele nach Beitrags-ID](_meta/sprungziele.md) — für Links wie
  `?topic=51.msg314#msg314`
- [Abdeckungsbericht](_meta/bericht.md)

## Nutzung

Durchsuchen: In der Web-Oberfläche die Repository-Suche verwenden, lokal z. B.

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

Das Wiki und dieses Forum-Archiv verweisen relativ aufeinander; das Forum
liegt im Wiki-Repository unter `forum/`:

```text
betty-wiki/
├── pages/          Wiki-Seiten
└── forum/          dieses Forum-Archiv
```
Forum-Links im Wiki der Form `?topic=51.msg314#msg314` werden mit einem
Hilfsskript auf die lokalen, relativen Pfade umgeschrieben:

```bash
python3 tools/link_forum.py ..          # Vorschau
python3 tools/link_forum.py .. --write  # anwenden
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
