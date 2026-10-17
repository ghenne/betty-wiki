---
title: "Betty Swisscom läuft"
topic_id: 205
board: "Hardware"
board_id: 5
posts: 9
first_post: "04. Mai 2009, 18:39"
last_post: "05. Mai 2009, 10:38"
authors: ["AKtronik", "Telekatz", "gerdi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=205.0"
---

# Betty Swisscom läuft

[← Hardware](../boards/05-hardware.md) · Thema 205 · 9 Beiträge · 04. Mai 2009, 18:39 – 05. Mai 2009, 10:38

Beteiligt: AKtronik, Telekatz, gerdi

---

<a id="msg1390"></a>

## 1. gerdi · 04. Mai 2009, 18:39

Die Tabelle von famos und die Angaben von Telekatz waren sehr genau.
Es hat alles gestimmt.

Nun spiele ich auf der Betty Swisscom Tic-Tac-Toe.

An Telekatz:
Du hast gesagt, dass es noch ein Problem mit dem Speicher der Swisscom gäbe.
Wenn du mir genau sagst, was ich machen soll schaffe ich es vielleicht.

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1390#msg1390)

---

<a id="msg1392"></a>

## 2. AKtronik · 04. Mai 2009, 19:10

Hey, ist ja super!

So wie es aussieht, habe ich auch eine SwissCom-Betty.
Ich habe leider noch keine IDE am laufen.
Könntest Du dem Forum vielleicht die Flash.bin´s zur Verfügung stellen.

MfG
AKtronik

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1392#msg1392)

---

<a id="msg1393"></a>

## 3. gerdi · 04. Mai 2009, 19:32

Gerne!
Wie soll ich das machen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1393#msg1393)

---

<a id="msg1394"></a>

## 4. AKtronik · 04. Mai 2009, 20:14

Wenn Du die beiden Flash.bin´s einzeln zippst sollte dei erste kleiner 250KByte sein.
Die Zweite noch viel kleiner.

Dann kannst Du die Dateien unter [Erweiterte Optionen] Deinem nächsten posting anhängen.
Wenn das nicht geht, dann kannst Du meine eMail anklicken.
Nur bringt das dem Forum nichts.

Wäre vielleicht ein Denkanstoß für die Admins diese Optionen zu erweitern, damit das Board noch userfreundlicher wird und
"Forschergruppen" ihre Ergebnisse einfacher teilen können.

MfG
AKtronik

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1394#msg1394)

---

<a id="msg1397"></a>

## 5. Telekatz · 04. Mai 2009, 22:44

> **Zitat**
>
> An Telekatz:
> Du hast gesagt, dass es noch ein Problem mit dem Speicher der Swisscom gäbe.
> Wenn du mir genau sagst, was ich machen soll schaffe ich es vielleicht.

Hab ich zwar nicht, aber egal.

Du musst in bfs.h den Speicherbereich für das Filesystem anpassen falls deine Flash Speicherbausteine nur 512kB groß sind. Ausserdem darf Boop dann auch nur maximal 512kB groß werden (was momenton noch nicht der Fall ist).

Ich hab in Boop eine Info Page eingebaut mit der man ermitteln kann, welcher Flash eingebaut ist. Bei der 1024KB Version wird die Device ID 0x5B angezeigt, bei der 512kB Version müsste es 0xBA sein.
Zusätzlich wird noch die Hardwareversion der Betty PCB angezeigt. Die Versionen kleiner 3 müssten die mit der Swisscom Tastenmatrix sein.

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1397#msg1397)

---

<a id="msg1398"></a>

## 6. gerdi · 04. Mai 2009, 23:38

Die Info-Page konnte ich nicht finden.
Hast du eine neue Firmware?

Das ist noch das Rom ohne Speicherkorrektur.

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1398#msg1398)

---

<a id="msg1400"></a>

## 7. Telekatz · 05. Mai 2009, 08:22

Die Info Page ist seit gestern im SVN.

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1400#msg1400)

---

<a id="msg1401"></a>

## 8. gerdi · 05. Mai 2009, 08:30

Willst du meine Änderungen nicht auch in den svn aufnehmen?

Dann kann man mit dem #define "SWISSCOM" für die Swisscom Betty kompilieren.

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1401#msg1401)

---

<a id="msg1402"></a>

## 9. Telekatz · 05. Mai 2009, 10:38

Schick mir deine Änderungen mal.

[Permalink](http://bettyhacks.com/forum/index.php?topic=205.msg1402#msg1402)

---

## Verwandte Themen

- [Swisscom stellt interaktives Fernsehangebot (betty) wieder ein](0069-swisscom-stellt-interaktives-fernsehangebot-betty-wieder-ein.md)
- [Swisscom Betty](0128-swisscom-betty.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
