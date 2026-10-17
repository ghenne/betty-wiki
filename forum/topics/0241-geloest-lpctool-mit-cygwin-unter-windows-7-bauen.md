---
title: "[gelöst] lpctool mit Cygwin unter Windows 7 bauen?"
topic_id: 241
board: "Software"
board_id: 6
posts: 7
first_post: "04. Okt 2010, 10:05"
last_post: "06. Okt 2010, 20:02"
authors: ["Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=241.0"
---

# [gelöst] lpctool mit Cygwin unter Windows 7 bauen?

[← Software](../boards/06-software.md) · Thema 241 · 7 Beiträge · 04. Okt 2010, 10:05 – 06. Okt 2010, 20:02

Beteiligt: Telekatz, eme

---

<a id="msg1665"></a>

## 1. eme · 04. Okt 2010, 10:05

Hallo allerseits,

ich möchte nun doch noch einmal versuchen, lpctool unter Windows zum Laufen zu bekommen.
lpctool-cygwin bleibt bei mir leider an ganz neuer Stelle hängen:

[font=courier]lpctool-cygwin>lpctool.exe -d /dev/com3 -i -v -e -a boop_rom.bin

lpctool V0.9

This Software is free Software under GNU GPL 3 or later
(c) 2007 Ch. Klippel <ck@mamalala.net>

Info : erasing flash #0 before write
Info : using flash #0 image boop_rom.bin
Info : opening serial device /dev/com3
Info : reset into bootmode
Info : opening bootloader
Info : initiating auto-baud
Info : awaiting autobaud response
Info : got response, answering
Info : setting frequency
Info : switching baudrate
Info : disabling echo[/font]

Das ist unter Windows 7 und mit einem Prolific USB-UART Wandler.

Cygwin habe ich per Default installiert - kann mir jemand sagen, welche Pakete ich brauche (gcc-??)?

*Last Edit : 04. Okt 2010, 11:43 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=241.msg1665#msg1665)

---

<a id="msg1666"></a>

## 2. eme · 04. Okt 2010, 10:33

Ok, ich habe einfach ein paar gcc...core Pakete ausgewählt, die Abhängigkeiten werden automatisch installiert. Dann cygwin gestartet und über /cygdrive in lpctool/trunk navigiert. make hat funktioniert, aber auch dort bleibt's bei "disabling echo" hängen.
meine "testing" branch mag er noch nicht, weil cygwin die arm-toolchain nicht kennt. da werde ich wohl pfade anpassen müssen..

[Permalink](http://bettyhacks.com/forum/index.php?topic=241.msg1666#msg1666)

---

<a id="msg1667"></a>

## 3. eme · 04. Okt 2010, 11:41

Das ist gar kein neues Problem, dasselbe hatte ich schonmal vor Längerem:

[http://bettyhacks.com/forum/index.php?topic=54.msg833#msg833](0054-lpctool-schneller-upload.md#msg833)

Nachdem in openBootLoader der Baudratenwechsel deaktiviert ist läuft es weiter bis "executing code at ram adress"

Ist so lange her.. jedenfalls geht das Ganze wohl mit 19200 baud los

Ok, noch besser, "setBaud(38400);" in openSerial und die Änderungen aus dem Wiki (lpctool_serial.h Zeile 5:
 #define TOOLBAUD 115200
muss geändert werden in
 #define TOOLBAUD 38400
serial.c Zeile 170:
 serial_setbrg (115200);
muss geändert werden in
 serial_setbrg (38400)

so komme ich bis "opening ram tool"

Man kann das Pfad-Problem (ARM unter cygwin) umgehen, indem man das Makefile so anpasst, dass unter Windows cmd ramtool etc gebaut werden, und in cygwin lpctool.. Nicht elegant :-)

Tortzdem komme ich nicht weiter, auf dem Stand war ich wohl schon.

reconfSerial in openRamTool auskommentiert..

und auch sonst ... geht. :-)

anbei, gepackt mit upx und gezippt

[Permalink](http://bettyhacks.com/forum/index.php?topic=241.msg1667#msg1667)

---

<a id="msg1669"></a>

## 4. eme · 04. Okt 2010, 11:48

Aber doch mal eine Frage: Warum ist im Original der Wechsel der Baudrate eigentlich erforderlich?
Kann man nicht die ganze Zeit 115200 baud benutzen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=241.msg1669#msg1669)

---

<a id="msg1670"></a>

## 5. Telekatz · 04. Okt 2010, 13:58

Für die Auto-baud Erkennung darf die anfängliche Baudrate nicht beliebig hoch sein. Die Grenze liegt bei etwa 58k Baud.

*Last Edit : 04. Okt 2010, 18:05 by Telekatz*

[Permalink](http://bettyhacks.com/forum/index.php?topic=241.msg1670#msg1670)

---

<a id="msg1671"></a>

## 6. eme · 04. Okt 2010, 15:37

Danke.
Vgl. UM10114 Volume 1 Chapter 19: OnChipBoot (p. 255)

Demnach ist bei 10 MHz Quarz der ISP auf 38,4 kbaud limitiert (flashtool (ramtool.c) ins ram laden). Danach könnte es also schneller gehen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=241.msg1671#msg1671)

---

<a id="msg1676"></a>

## 7. eme · 06. Okt 2010, 20:02

Wie kann denn das schon wieder sein? Mit einer anderen Betty bekomme ich beim Senden von HELO_CMD ein "Permission denied".
Unterschiedliches Verhalten von Bettys hatte ich schonmal in [http://bettyhacks.com/forum/index.php?topic=228.0](0228-lpctool-ubuntu-linux-reset-eint1-timingprobleme-mit-pl-2303.md)

Aber wie kann die Betty eine Schreibzugriffsproblem verursachen? Zwingt Ramtool den UART-Wandler in die Knie? Unterschiedliche Hardware?

[Permalink](http://bettyhacks.com/forum/index.php?topic=241.msg1676#msg1676)

---

## Verwandte Themen

- [lpctool, ubuntu linux, Reset/eINT1-Timingprobleme mit PL-2303](0228-lpctool-ubuntu-linux-reset-eint1-timingprobleme-mit-pl-2303.md)
- [lpctool - schneller upload](0054-lpctool-schneller-upload.md)
- [Probleme beim kompilieren mit WinARM unter Windows 7 x64](1046-probleme-beim-kompilieren-mit-winarm-unter-windows-7-x64.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
