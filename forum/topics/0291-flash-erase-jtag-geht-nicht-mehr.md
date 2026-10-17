---
title: "Flash erase -> JTAG geht nicht mehr"
topic_id: 291
board: "Software"
board_id: 6
posts: 3
first_post: "28. Dez 2012, 23:16"
last_post: "08. Apr 2013, 18:23"
authors: ["Telekatz", "koppi", "xenpac"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=291.0"
---

# Flash erase -> JTAG geht nicht mehr

[← Software](../boards/06-software.md) · Thema 291 · 3 Beiträge · 28. Dez 2012, 23:16 – 08. Apr 2013, 18:23

Beteiligt: Telekatz, koppi, xenpac

---

<a id="msg2102"></a>

## 1. koppi · 28. Dez 2012, 23:16

Flash gelöscht, Neustart.

JLink sagt:
Info: Could not measure total IR len. TDO is constant high.
Info: Could not measure total IR len. TDO is constant high.

Selbes mit OpenOCD und Turtelizer. Openocd-config hier aus dem Forum (telekatz).

Nach Neuflashen des Original-Binaries mit lpctool geht JTAG wieder normal.

Was ist da los? JTAG sollte ja mit dem Flashinhalt nix zu tun haben.
Reset-Problem?

Danke!

[Permalink](http://bettyhacks.com/forum/index.php?topic=291.msg2102#msg2102)

---

<a id="msg2103"></a>

## 2. Telekatz · 29. Dez 2012, 23:16

Du musst die entsprechenden Pins des µC auch als JTAG konfiguriert.  Bei den Original-Binaries passiert dies im Programm. Ohne Programm, das dies erledigt, muss P1.26 (RTCK) während des Resets auf Low Pegel gehalten werden.

[Permalink](http://bettyhacks.com/forum/index.php?topic=291.msg2103#msg2103)

---

<a id="msg2114"></a>

## 3. xenpac · 08. Apr 2013, 18:23

Hi,
Hab heute auchmal den J-Link an die Betty angeschlossen.

Mit Pulldown Widerstand am INT pin.

Segger flash program kann die ID des processors nicht auslesen, immer 0.

Kann sich nicht verbinden.

hmmm, Brauchts da irgendwelche weiteren Einstellungen, init kommandos?

[Permalink](http://bettyhacks.com/forum/index.php?topic=291.msg2114#msg2114)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
