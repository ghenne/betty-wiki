---
title: "PLL umschalten"
topic_id: 267
board: "Software"
board_id: 6
posts: 1
first_post: "06. Jun 2011, 23:20"
last_post: "06. Jun 2011, 23:20"
authors: ["Walter"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=267.0"
---

# PLL umschalten

[← Software](../boards/06-software.md) · Thema 267 · 1 Beiträge · 06. Jun 2011, 23:20 – 06. Jun 2011, 23:20

Beteiligt: Walter

---

<a id="msg1932"></a>

## 1. Walter · 06. Jun 2011, 23:20

Nabend,

nachdem ich für PIN-Toggeln in C nur eine Frequenz von 0,66 MHz erreicht habe,  habe ich versucht mit der Funktion setSpeed die Frequenz auf 60MHz zu stellen,
im Vergleich zu 30MHz ergibt sich kaum ein Unterschied.

Kann es sein dass der PLL gar nicht läuft?
Im Datenblatt steht, dass man nach dem Einschalten des PLL erst warten muss bis er "gelocked" ist bevor man ihn als Taktquelle auswählt, im Startup Code wird er gleichzeitig mit dem Einschalten auch connected,
kann das das Problem sein?

Gute Nacht
Walter

[Permalink](http://bettyhacks.com/forum/index.php?topic=267.msg1932#msg1932)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
