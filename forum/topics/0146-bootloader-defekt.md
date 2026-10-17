---
title: "Bootloader defekt?"
topic_id: 146
board: "Hardware"
board_id: 5
posts: 2
first_post: "15. Mai 2008, 00:01"
last_post: "15. Mai 2008, 19:06"
authors: ["Gentoo07", "fussel_dlx"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=146.0"
---

# Bootloader defekt?

[← Hardware](../boards/05-hardware.md) · Thema 146 · 2 Beiträge · 15. Mai 2008, 00:01 – 15. Mai 2008, 19:06

Beteiligt: Gentoo07, fussel_dlx

---

<a id="msg1026"></a>

## 1. fussel_dlx · 15. Mai 2008, 00:01

Hallo,

ich habe mir vor kurzem das Simple Serial Interface zusammengebaut aber mir ist aufgefalle das beim Flashvorgang die Betty nur neustartet.

Jetzt habe ich mal versucht manuell den Bootloader zu starten, wie es im Wiki steht, aber wenn ich EINT auf GND brücke und dann einen Reset mache, startet sie nicht mehr.
Erst wenn ich EINT löse und Reset mache geht se wieder.

Gibt es da einen Trick oder ist die Betty einfach nur defekt?

[Permalink](http://bettyhacks.com/forum/index.php?topic=146.msg1026#msg1026)

---

<a id="msg1028"></a>

## 2. Gentoo07 · 15. Mai 2008, 19:06

> **Zitat von: fussel_dlx am 15. Mai 2008, 00:01**
>
> ... wenn ich EINT auf GND brücke und dann einen Reset mache, startet sie nicht mehr.

Woher weisst du das?

Dass das Display hierbei nichts anzeigt ist normal, aber wenn dein Interface und die Schnittstelle am PC richtig funktionieren solltest du z.B. mit Betty-Heaven jetzt die Software auslesen und neu schreiben können. Das ist die Funktionalität des Bootloaders, das Display wird einfach nicht angesteuert.

[Permalink](http://bettyhacks.com/forum/index.php?topic=146.msg1028#msg1028)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
