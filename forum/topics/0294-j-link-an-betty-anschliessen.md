---
title: "J-Link an Betty anschliessen"
topic_id: 294
board: "Software"
board_id: 6
posts: 3
first_post: "08. Apr 2013, 18:29"
last_post: "21. Aug 2014, 16:30"
authors: ["gunnar", "xenpac"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=294.0"
---

# J-Link an Betty anschliessen

[← Software](../boards/06-software.md) · Thema 294 · 3 Beiträge · 08. Apr 2013, 18:29 – 21. Aug 2014, 16:30

Beteiligt: gunnar, xenpac

---

<a id="msg2115"></a>

## 1. xenpac · 08. Apr 2013, 18:29

Hallo,

Ich hab versucht den J-Link von Segger an die Betty anzuschliessen.
Nutze Coocox IDE.

Hat das schonmal jemand zum Laufen gebracht?

Ich kriege keine Verbindung mit der CPU.

[Permalink](http://bettyhacks.com/forum/index.php?topic=294.msg2115#msg2115)

---

<a id="msg2883"></a>

## 2. xenpac · 19. Mär 2014, 11:44

Klappt nun.

am besten gehts mit adaptive clocking.

mit jlink und openocd geht aucg das flashen.

der betty flash chip unterstützt NICHT das CFI protokoll.

(daher erkennt die segger software auch den flash speicher nicht)

[Permalink](http://bettyhacks.com/forum/index.php?topic=294.msg2883#msg2883)

---

<a id="msg2895"></a>

## 3. gunnar · 21. Aug 2014, 16:30

Hallo,

waren Änderungen an den eingecheckten Files nötig damit es mit OpenOCD klappt? Falls ja könnte ich die ins Repository aufnehmen.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=294.msg2895#msg2895)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
