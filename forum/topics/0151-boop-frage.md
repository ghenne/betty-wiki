---
title: "Boop-Frage"
topic_id: 151
board: "Software"
board_id: 6
posts: 2
first_post: "28. Jun 2008, 14:23"
last_post: "29. Jun 2008, 15:53"
authors: ["Gentoo07", "temp12"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=151.0"
---

# Boop-Frage

[← Software](../boards/06-software.md) · Thema 151 · 2 Beiträge · 28. Jun 2008, 14:23 – 29. Jun 2008, 15:53

Beteiligt: Gentoo07, temp12

---

<a id="msg1067"></a>

## 1. temp12 · 28. Jun 2008, 14:23

Hi alle,

Betty hat doch 2 Flashspeicher oder? Benutzt Boop die beide Speicher oder nur einen? Und weiss jemand wo der Bootloader von Betty einprogrammiert ist? Kann man den Bootloader schmeissen und eigenen Bootloader hochladen? Weiss jemand Bescheid?

Danke
Temp

[Permalink](http://bettyhacks.com/forum/index.php?topic=151.msg1067#msg1067)

---

<a id="msg1068"></a>

## 2. Gentoo07 · 29. Jun 2008, 15:53

Moin,

Ja sie hat gut erkennbar 2 identische Flashspeicher, in Betty-Heaven getrennt anzuwählen.
Boop wird momentan nur in Flash 1 geschriebenum zu funktionieren, Flash 2 dürfte daher frei sein.

Zum Bootloader musst du in das UserManual des LPC2220 gucken.
Dort ist ein serieller Bootloader integriert, der Zugriff auf den internen RAM erlaubt.
Du MUSST also weiteren Code nachladen um überhaupt Zugriff auf den Flashspeicher zu bekommen und darfst dir diesen natürlich auch selbst ausdenken.

Was möchtest du denn an dem Bootloader verbessern?

Gruß
Gentoo

[Permalink](http://bettyhacks.com/forum/index.php?topic=151.msg1068#msg1068)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
