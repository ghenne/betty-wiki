---
title: "Wieviel Speicher bleibt in Boop für weitere Variablen"
topic_id: 266
board: "Software"
board_id: 6
posts: 3
first_post: "05. Jun 2011, 17:42"
last_post: "06. Jun 2011, 23:30"
authors: ["Telekatz", "Walter"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=266.0"
---

# Wieviel Speicher bleibt in Boop für weitere Variablen

[← Software](../boards/06-software.md) · Thema 266 · 3 Beiträge · 05. Jun 2011, 17:42 – 06. Jun 2011, 23:30

Beteiligt: Telekatz, Walter

---

<a id="msg1930"></a>

## 1. Walter · 05. Jun 2011, 17:42

Habe vor kurzem die Betty entdeckt und bin begeistert.
Danke für Eure Arbeit.

Wie kann ich denn feststellen wieviel Platz noch für weitere Software in Boop ist,
sowohl RAM für Variablen als auch Flash fürs Programm?
Gibt es ein malloc?
Wenn keine Doku zu Funktionen da ist würde ich mir mit Hilfe der SOurcen eine machen und zur Verfügung stellen

[Permalink](http://bettyhacks.com/forum/index.php?topic=266.msg1930#msg1930)

---

<a id="msg1931"></a>

## 2. Telekatz · 06. Jun 2011, 21:10

Wieviel Speicher noch frei ist kannst du nach dem compilen in der boop.map herausfinden.

Das Programm liegt im ersten Flash, das von 0x80000000 bis 0x800FFFFF geht.  Aktuell bis 0x80039844 belegt.

Ram von 0x40000000 bis 0x4000FFFF, belegt bis 0x400035c4.

[Permalink](http://bettyhacks.com/forum/index.php?topic=266.msg1931#msg1931)

---

<a id="msg1933"></a>

## 3. Walter · 06. Jun 2011, 23:30

Danke,
(hätte ich auch selber drauf kommen können)

[Permalink](http://bettyhacks.com/forum/index.php?topic=266.msg1933#msg1933)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
