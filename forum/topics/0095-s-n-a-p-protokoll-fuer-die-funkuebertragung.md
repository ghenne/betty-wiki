---
title: "S.N.A.P.-Protokoll für die Funkübertragung?"
topic_id: 95
board: "Software"
board_id: 6
posts: 3
first_post: "03. Jan 2008, 13:28"
last_post: "03. Jan 2008, 14:43"
authors: ["MrFX", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=95.0"
---

# S.N.A.P.-Protokoll für die Funkübertragung?

[← Software](../boards/06-software.md) · Thema 95 · 3 Beiträge · 03. Jan 2008, 13:28 – 03. Jan 2008, 14:43

Beteiligt: MrFX, netguy

---

<a id="msg689"></a>

## 1. MrFX · 03. Jan 2008, 13:28

Moin!

Was haltet ihr davon, als Protokollrahmen für die Datenübertragung per Funk das S.N.A.P.-Protokoll einzusetzen:

[http://www.kreatives-chaos.com/artikel/snap-protokoll](https://web.archive.org/web/2012/http://www.kreatives-chaos.com/artikel/snap-protokoll)
bzw. [http://www.hth.com/snap/](https://web.archive.org/web/2012/http://www.hth.com/snap/)

Damit lassen sich bestimmte Empfänger ansprechen, Fehlerdedektion ist dabei...

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=95.msg689#msg689)

---

<a id="msg690"></a>

## 2. netguy · 03. Jan 2008, 13:45

moin,

naja, das problem bei dem snap protokoll ist halt das dort alles nochmal gemacht wird, was der chip alleine schon kann.

snap:
| PRE | ... | SYNC | HDB2 | HDB1 |DAB1 | SAB1 | DB1 | CRC2 | CRC1

cc1100: (datenblatt seite 32)
Preamble bits (1010...1010)
Sync word
Length field
Address field
Data field
CRC-16

dazu macht der chip auch noch fec codierung und data-whitening wenn gewuenscht.

von daher waere es nicht wirklich sinnvoll ein protokoll zu nehmen welches das alles nochmal implementiert.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=95.msg690#msg690)

---

<a id="msg691"></a>

## 3. MrFX · 03. Jan 2008, 14:43

Moin!

Naja, hab mal wieder weiter gedacht, als nötig... bin nebenbei mit den Funkmodulen von Pollin am Werkeln, da ist das sinvoller.

Also betrachtet den Vorschlag als hinfällig.

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=95.msg691#msg691)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
