---
title: "lpctool, ubuntu linux, Reset/eINT1-Timingprobleme mit PL-2303"
topic_id: 228
board: "Software"
board_id: 6
posts: 15
first_post: "30. Jan 2010, 22:08"
last_post: "03. Feb 2010, 23:05"
authors: ["Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=228.0"
---

# lpctool, ubuntu linux, Reset/eINT1-Timingprobleme mit PL-2303

[← Software](../boards/06-software.md) · Thema 228 · 15 Beiträge · 30. Jan 2010, 22:08 – 03. Feb 2010, 23:05

Beteiligt: Telekatz, eme

---

<a id="msg1564"></a>

## 1. eme · 30. Jan 2010, 22:08

Guten Abend, ich habe mir endlich mal ein Datenkabel organisiert ([http://www.dealextreme.com/details.dx/sku.13638).](https://web.archive.org/web/2012/http://www.dealextreme.com/details.dx/sku.13638).) Wenn man sich durch das Spritzgussgehäuse nagt, kommt man an eine Platine mit COB (PL-2303), die Handshakeleitungen sind teils herausgeführt (DTR, RTS), Pegel 3,5 V..

Nach [http://www.grautier.com/grautier/uploads/Elektronik/Betty/RIMG0001.JPG](https://web.archive.org/web/2012/http://www.grautier.com/grautier/uploads/Elektronik/Betty/RIMG0001.JPG) und [http://bettyhacks.com/wiki/index.php/LPCTool](../../pages/LPCTool.md) verdrahtet.

lpctool compiliert:
`boopfirmware/lpctool/trunk$ make
/opt/armtool/4.1.1/bin/arm-elf-gcc -mcpu=arm7tdmi-s -c -Wall -mthumb-interwork -msoft-float -I/opt/armtool/4.1.1/include -o serial.o serial.c
/opt/armtool/4.1.1/bin/arm-elf-gcc -mcpu=arm7tdmi-s -c -Wall -mthumb-interwork -msoft-float -I/opt/armtool/4.1.1/include -o ramtool.o ramtool.c
/opt/armtool/4.1.1/bin/arm-elf-ld -Os -Tlpc2220.ld -o ramtool.elf crt.o serial.o lcd.o fonty.o flash.o ramtool.o
/opt/armtool/4.1.1/bin/arm-elf-objcopy -O binary ramtool.elf ramtool.bin
/opt/armtool/4.1.1/bin/arm-elf-gcc -mcpu=arm7tdmi-s -c -Wall -mthumb-interwork -msoft-float -I/opt/armtool/4.1.1/include -DRESIDENT -o romtool.o ramtool.c
/opt/armtool/4.1.1/bin/arm-elf-ld -Os -Tlpc2220_rom.ld -o romtool.elf crt.o serial.o lcd.o fonty.o flash.o romtool.o
/opt/armtool/4.1.1/bin/arm-elf-objcopy -O binary romtool.elf romtool.bin
gcc -Os bin2h.c -o bin2h
bin2h.c: In function 'main':
bin2h.c:18: warning: format '%08X' expects type 'unsigned int', but argument 2 has type 'long unsigned int'
strip bin2h
./bin2h > tool_data.h
gcc -Os infohelper.c lpctool_serial.c bootcom.c toolcom.c lpctool.c -o lpctool
infohelper.c: In function 'printInfoH':
infohelper.c:39: warning: format '%08X' expects type 'unsigned int', but argument 3 has type 'long unsigned int'
bootcom.c: In function 'goBootLoader':
bootcom.c:172: warning: format '%i' expects type 'int', but argument 3 has type 'long unsigned int'
bootcom.c: In function 'uploadData':
bootcom.c:200: warning: format '%i' expects type 'int', but argument 3 has type 'long unsigned int'
bootcom.c:226: warning: format '%i' expects type 'int', but argument 3 has type 'long unsigned int'
bootcom.c:226: warning: format '%i' expects type 'int', but argument 4 has type 'long unsigned int'
strip lpctool`

Und versucht zu flashen:
`boopfirmware/lpctool/trunk$ ./lpctool -d /dev/ttyUSB0 -i -v -e -a boop_rom.bin

lpctool V0.9

This Software is free Software under GNU GPL 3 or later
(c) 2007 Ch. Klippel <ck@mamalala.net>

Info : erasing flash #0 before write
Info : using flash #0 image boop_rom.bin
Info : opening serial device /dev/ttyUSB0
Info : reset into bootmode
Info : opening bootloader
Info : initiating auto-baud
Info : awaiting autobaud response
^C`

Mit Oszi sehe ich, dass 1..3 Zeichen gesendet werden PC_TX->BETTY_RX.
Reset macht folgende Pulse 0,5 ms low, 0,5 ms high, 0,2 ms low
eINT1/Bootloader: 0,6 ms low, 0,1 ms high, 0,6 ms low

etwa so:

 `---__---__---
---___-____--`

Reset und eINT1 haben sind mit der ersten fallende Flanke gleichzeitig, danach stimmt das Timing.

BETTY_TX: macht nur 1 ms low, weil dann gleich wieder ein reset kommt.

Deutet ja alles auf [http://bettyhacks.com/wiki/index.php/LPCTool#Lpctool-Probleme](../../pages/LPCTool.md#lpctool-probleme)

 (die Probleme hatte ich ja schonmal, mit anderer Hardware: [http://bettyhacks.com/forum/index.php?topic=54.msg833#msg833)](0054-lpctool-schneller-upload.md#msg833)

Mit [http://www.grautier.com/grautier/index.php?/plugin/dlfile_108](https://web.archive.org/web/2012/http://www.grautier.com/grautier/index.php?/plugin/dlfile_108) geht es aber auch nicht (dieselbe, doppelte Pulsfolge)

Liegt es also am PL-2303? Kann ich noch was in lpctool ändern (baudrate ist schon runtergesetzt auf 38400)?

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1564#msg1564)

---

<a id="msg1565"></a>

## 2. eme · 30. Jan 2010, 23:41

Mit ner neuen Betty komme ich immerhin bis:
`Info : erasing flash #0 before write
Info : using flash #0 image boop_rom.bin
Info : opening serial device /dev/ttyUSB0
Info : compensating openport-reset
Info : reset into bootmode
Info : opening bootloader
Info : initiating auto-baud
Info : awaiting autobaud response
ERROR: autobaud detection failed
ERROR: Error opening BootLoader
Info : closing serial device /dev/ttyUSB0`

lpctool.c habe ich an Zeile 355 erweitert um

`printInfoS(2,"compensating openport-reset",0);
  setRTS(0);
        usleep(1000000);
        usleep(1000000);`

Damit ist die Reihenfolge aus [http://bettyhacks.com/wiki/index.php/Firmware_flashen](../../pages/Firmware%20flashen.md) eingehalten, bringt aber trotzdem nix.

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1565#msg1565)

---

<a id="msg1566"></a>

## 3. eme · 31. Jan 2010, 00:19

Wenn ich manuell mit dem Adapter und nem Terminalprogramm
RTS 1
DTR 1
DTR 0
RTS 0

und dann

?\r\n

sende, kommt 99 AD 86 B5 B5 AB 00 A1 51 FC zurück (10 Zeichen). Es werden wohl mehr erwartet!?

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1566#msg1566)

---

<a id="msg1567"></a>

## 4. eme · 31. Jan 2010, 00:27

Falsche Baudrate, mit 38400 kommt tatsächlich "Synchronized\r\n" zurück.

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1567#msg1567)

---

<a id="msg1568"></a>

## 5. eme · 31. Jan 2010, 00:55

Mit den Zeiten in enterBootLD() x100 komme ich sogar weiter.

`Info : erasing flash #0 before write
Info : using flash #0 image boop_rom.bin
Info : opening serial device /dev/ttyUSB0
setting 38400
Info : compensating openport-reset
Info : reset into bootmode
Info : opening bootloader
Info : initiating auto-baud
Info : awaiting autobaud response
Info : Synchronized
�
 (14)
Info : got response, answering
Info : setting frequency
Info : switching baudrate
setting 38400
Info : disabling echo
Info : unlocking bootloader
Info : uploading compiled-in ram image
Info : starting ram upload
Info : ram upload complete, total bytes: 0x00004B28
Info : ram uploaded
Info : executing code at ram address 0x40000200
Info : code execution started 0x40000200
setting 38400
Info : opening ram tool`

Dann hängt es an den Timeouts und bekommt "HELO" nie vom Flashtool..

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1568#msg1568)

---

<a id="msg1569"></a>

## 6. eme · 31. Jan 2010, 10:48

Ich kann's nicht ganz nachvollziehen, plötzlich funktioniert die Verbindung mit dem FlashTool.
Ich habe den mancherorts vorgeschlagenen Pull-Up wieder eingebaut, aber bin nicht ganz sicher, dass es daran liegt.
lpctool hat nämlich vorher schon in getRESULT das HELO bekommen.

Nächste Frage: warum kann ich meine bereits geflashte Betty flashen, eine brandneue aber nicht?

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1569#msg1569)

---

<a id="msg1572"></a>

## 7. eme · 31. Jan 2010, 13:14

Problem gelöst:

Die Betty Original-Firmware sendet nach dem Reset sofort Zeichen, die beim Einlesen der FlashTool Antwort stören.

Also in bootcom.c noch ein tcflush(serialDev, TCIOFLUSH); vor dem Einlesen.
Ich hatte mich schon gewundert, warum das Flushen nichts bringt; erst einige makes später ist dem Compiler eingefallen, dass er serialDev gar nicht kennt..

Daher:
lpctool_serial.c - static int serialDev = -1;
lpctool_serial.c + int serialDev = -1;

lpctool_serial.h + extern int serialDev;

Dann wird der Müll gelöscht und das "Synchronized\r\n" wird korrekt empfangen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1572#msg1572)

---

<a id="msg1574"></a>

## 8. eme · 31. Jan 2010, 15:06

Nächstes Problem:

Ich möchte die betty-tv Universalfernbedienung flashen ([http://bettyhacks.com/wiki/index.php/Original_Firmware).](https://web.archive.org/web/2012/http://bettyhacks.com/wiki/index.php/Original_Firmware).)

Der erste Flash schafft es auch, doch beim zweiten bei 0x82080000 (= das 524288. Byte) gibt es ein NACK!

`.....
Info : flash #0 uploaded
Info : opening flash1 image Flash2_UniFB.bin
Info : uploading flash1 image Flash2_UniFB.bin
Info : setting address to 0x82000000
Info : enabling bulk write
Info : setting total number of bytes to 0x00100000
Info : starting flash upload
ERROR: wrong response, expected ACK!          ]
ERROR: flash write failed
Info : closing file descriptor
Info : closing serial device /dev/ttyUSB0`

Ist der Fehler schonmal aufgetreten? Wie kann ich das Problem weiter eingrenzen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1574#msg1574)

---

<a id="msg1575"></a>

## 9. eme · 31. Jan 2010, 16:03

Andere Betty (R1.: 0x82010000, 0x82010000 (an derselben Stelle)
Die vorige: 0x82080000 (dieselbe Stelle)

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1575#msg1575)

---

<a id="msg1576"></a>

## 10. eme · 31. Jan 2010, 16:47

Um meinen Monolog fortzusetzen:

Beide Bettys starten, ich vermute aber dass sie fehlerhaft sind, weil sie im TV-Modus (vermutlich RC5) beide nicht die Zifferntasten unterstützen, und eine sogar den Standby-Knopf (An/Aus) nicht packt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1576#msg1576)

---

<a id="msg1582"></a>

## 11. Telekatz · 31. Jan 2010, 20:51

> **Zitat**
>
> Der erste Flash schafft es auch, doch beim zweiten bei 0x82080000 (= das 524288. Byte) gibt es ein NACK!

Wieso willst du überhaupt etwas in des zweite Flash schreiben? Boop wird nur in das erste Flash geschrieben.

> **Zitat**
>
> Beide Bettys starten, ich vermute aber dass sie fehlerhaft sind, weil sie im TV-Modus (vermutlich RC5) beide nicht die Zifferntasten unterstützen, und eine sogar den Standby-Knopf (An/Aus) nicht packt.

Welche HW Version wird denn im Info Menu angezeigt? Sind das vielleicht schweizerische Bettys?

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1582#msg1582)

---

<a id="msg1583"></a>

## 12. eme · 31. Jan 2010, 21:48

> **Zitat**
>
> Wieso willst du überhaupt etwas in des zweite Flash schreiben? Boop wird nur in das erste Flash geschrieben.

Ja, boop kann ich mittlerweile einwandfrei übertragen. Dann wollte ich mal die betty-tv Universalfernbedienung flashen ([http://bettyhacks.com/wiki/index.php/Original_Firmware).](https://web.archive.org/web/2012/http://bettyhacks.com/wiki/index.php/Original_Firmware).)

> **Zitat**
>
> Welche HW Version wird denn im Info Menu angezeigt? Sind das vielleicht schweizerische Bettys?

Boop sagt "Betty HW Version 03". Über amazon.de gekauft.

> **Zitat**
>
> Beide Bettys starten, ich vermute aber dass sie fehlerhaft sind,

Sollte heissen, die Firmware ist nicht vollständig übertragen..

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1583#msg1583)

---

<a id="msg1586"></a>

## 13. Telekatz · 01. Feb 2010, 16:02

> **Zitat**
>
> Ja, boop kann ich mittlerweile einwandfrei übertragen. Dann wollte ich mal die betty-tv Universalfernbedienung flashen ([http://bettyhacks.com/wiki/index.php/Original_Firmware).](https://web.archive.org/web/2012/http://bettyhacks.com/wiki/index.php/Original_Firmware).)

Betty mit Original Betty-TV Universalfernbedienungs Firmware? Das ist ja wie D-BOX2 mit Betanova. Pervers!

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1586#msg1586)

---

<a id="msg1587"></a>

## 14. eme · 01. Feb 2010, 19:38

Kann ich nicht beurteilen, es läuft ja nicht ;-)
Werde irgendwann versuchen, dem FlashTool aufschlussreichere Fehlermeldungen beizubringen..

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1587#msg1587)

---

<a id="msg1591"></a>

## 15. eme · 03. Feb 2010, 23:05

So, nochmal probiert, nichts verändert - es hat funktioniert.

[Permalink](http://bettyhacks.com/forum/index.php?topic=228.msg1591#msg1591)

---

## Verwandte Themen

- [lpctool - schneller upload](0054-lpctool-schneller-upload.md)
- [soft-reset nach dem flashen mit lpctool](0189-soft-reset-nach-dem-flashen-mit-lpctool.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
