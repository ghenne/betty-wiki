---
title: "toolchains, lokale settings"
topic_id: 75
board: "Software"
board_id: 6
posts: 1
first_post: "15. Nov 2007, 06:47"
last_post: "15. Nov 2007, 06:47"
authors: ["netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=75.0"
---

# toolchains, lokale settings

[← Software](../boards/06-software.md) · Thema 75 · 1 Beiträge · 15. Nov 2007, 06:47 – 15. Nov 2007, 06:47

Beteiligt: netguy

---

<a id="msg537"></a>

## 1. netguy · 15. Nov 2007, 06:47

hallo alle zusammen,

so, boop & lpctool (genauer gesagt das ramtool in lpctool) ist nun unter einer 4.1.1 toolchain compilierbar.

die toolchains sind im wiki unter [http://www.bettyhacks.com/wiki/index.php/Entwicklungsumgebungen](../../pages/Entwicklungsumgebungen.md) verlinkt.

nomis hatte vor kurzem das key-handling geaendert, das habe ich jedoch vorerst mal wieder rausgenommen.
sorry dafuer, nomis

colibri, bezueglich deiner erweiterungen an boop, die muss ich in den naechsten tagen dann mal einpflegen, es sei denn du magst das selber gerne machen. gib hier kurz bescheid ob du oder ich das machen soll. wenn du das machst, dann bitte mit der winarm toolchain die auf dem wiki verlinkt ist. an den flags im makefile dann bitte nichts aendern, es muss mit dieser konfiguration fumktionieren.

ab jetzt kann man sich ein Makefile.local anlegen in das man die pfade zur toolchain eintraegt. ist diese datei vorhanden werden die dort angegebenen pfade benutzt, und nicht mehr die aus dem eigentlichen makefile. so kann jeder seine eigene config fuer die toolchain haben ohne jedesmal das makefile aendern zu muessen.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=75.msg537#msg537)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
