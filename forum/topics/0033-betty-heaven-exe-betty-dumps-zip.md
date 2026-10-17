---
title: "Betty-Heaven.exe / Betty-Dumps.zip"
topic_id: 33
board: "Software"
board_id: 6
posts: 15
first_post: "13. Aug 2007, 16:59"
last_post: "03. Okt 2007, 20:46"
authors: ["Colibri", "asgard", "fG", "kackhart", "netguy", "theborg"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=33.0"
---

# Betty-Heaven.exe / Betty-Dumps.zip

[← Software](../boards/06-software.md) · Thema 33 · 15 Beiträge · 13. Aug 2007, 16:59 – 03. Okt 2007, 20:46

Beteiligt: Colibri, asgard, fG, kackhart, netguy, theborg

---

<a id="msg201"></a>

## 1. Colibri · 13. Aug 2007, 16:59

Hallo Leute,

Es gibt ein Windows-Tool "Betty-Heaven" mit dem man mit der Betty Fernbedienung Daten austauschen kann.

Es gibt auch ein Packet "Betty-Dumps.zip" in dem die Flash-Dumps, der ISP-BootLoader und aus der Firmware gerippte .wav Dateien enthalten sind.

Derzeit ist nur die Backup-Funktion (Flashinhalt auf dem PC speichern) enthalten. Eine Restore-Funktion, um eigene Daten ins Flash zu schreiben, ist geplant.

Details im Wiki unter: Software von Colibri

Viel Spass,
Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg201#msg201)

---

<a id="msg202"></a>

## 2. theborg · 13. Aug 2007, 18:48

hm aber flash2.bin ist auch lehr also auch net weiter als wir

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg202#msg202)

---

<a id="msg204"></a>

## 3. Colibri · 13. Aug 2007, 19:47

Interessant wäre ob einen ein anderes jungfreuliches (AGB-Text wird angezeigt) Flash1.bin 100% identisch ist oder ob man evtl. einen kleinen unterschiedlichen Bereich findet in dem z.B. die individuelle ID gespeichert ist.
Falls das Flash identisch ist müsste die ID im 8 pol. Smartcard Chip 66C24PE gespeichert sein.

Security & Chip Card ICs
SLE 66C24PE
8/16-Bit Security Controller
68-Kbytes ROM, 2304 Bytes RAM, 2-Kbytes EEPROM
Dual Key Triple DES

Dieser Smartcard Chip wird vom Prozessor über UART1 angesteuert. TXD1 und RXD1 sind verbunden weil die Smartcard nur einen I/O-Pin hat.

Im normalen Betrieb werden ja über den Servicestecker (UART0) nur Logmeldungen ausgegeben aber keine Befehle angenommen. Interessant ist deswegen der Text bei 8004168C:"got secret key - accept serial input" und der Text bei 8003F9B0:"Gurkensalat" die beiden Texte werden im Unterprogram sub_80023BE4 verwendet.

Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg204#msg204)

---

<a id="msg205"></a>

## 4. theborg · 13. Aug 2007, 20:42

Jup

was auch spannend ist ist

0004:3280 entry %d....LCD_UC1610_Flip(%d)

Bei googel finde ich da nen lcd Treiber chip eventuell der fürs Display

[http://www.pacificdisplay.com/ics_app%20notes/ultra-chip/UC1610.pdf](https://web.archive.org/web/2012/http://www.pacificdisplay.com/ics_app%20notes/ultra-chip/UC1610.pdf)

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg205#msg205)

---

<a id="msg209"></a>

## 5. kackhart · 14. Aug 2007, 18:07

hi colibri,

leider ist in den zip files kein source dabei. daher eine frage, hast du eine idee was beim fwbc code

-> [http://www.hackdaworld.org/cgi-bin/gitweb.cgi?p=my-code/arm.git;a=blob;f=betty/fwbc.c;](https://web.archive.org/web/2012/http://www.hackdaworld.org/cgi-bin/gitweb.cgi?p=my-code/arm.git;a=blob;f=betty/fwbc.c;)

schief laeuft?

hier mal ein auszug aus meinem dump:

00000000  f0 20 00 00 f0 20 00 00  f0 20 00 00 f0 20 00 00 
00000010  f0 24 00 00 00 00 00 00  ff f0 00 00 f0 14 00 00 
00000020  4f 42 00 00 32 64 00 00  00 54 00 00 00 48 00 00 

in 4 byte abstaenden bekomme ich die ersten 2 bytes genauso raus wie du (modulo endianness). die letzten 2 byte sind immer '00 00'.

gru3,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg209#msg209)

---

<a id="msg210"></a>

## 6. Colibri · 14. Aug 2007, 18:26

Wenn Du folgendes einfügst, sollte es funktionieren

`//Flash1 auf 16 bit einstellen (ist vom ISP-BootLoader noch auf 32 bit eingestellt)
BCFG0 = 0x1000FBEF;`

Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg210#msg210)

---

<a id="msg211"></a>

## 7. kackhart · 14. Aug 2007, 21:45

hi,

> **Zitat von: Colibri am 14. Aug 2007, 18:26**
>
> Wenn Du folgendes einfügst, sollte es funktionieren
>
> `//Flash1 auf 16 bit einstellen (ist vom ISP-BootLoader noch auf 32 bit eingestellt)
> BCFG0 = 0x1000FBEF;`

danke, so funktioniert es. ich dachte das wuerde durch die BOOT[1:0] pins schon so gesetzt werden. tatsaechlich hatte ich das sogar schon probiert, allerdings durch BCFG0|=(1<<28), was wohl keine gute idee war, da er (so vermute ich) dabei wohl bei manchen bits unsinn liest (und dann setzt).

danke,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg211#msg211)

---

<a id="msg212"></a>

## 8. fG · 17. Aug 2007, 11:21

Hallo

wo gibt die Betty-Heaven.exe ?

Gruß fG

-found-

*Last Edit : 17. Aug 2007, 11:49 by fG*

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg212#msg212)

---

<a id="msg214"></a>

## 9. asgard · 17. Aug 2007, 16:23

HI,

wollte mal fragen, obs schon Vorschritte beim einspielen einer Firmware gibt?

Zudem würde es mich interessieren, ob schon jemand weitere Files aus der Firmware extrahiert hat?

Grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg214#msg214)

---

<a id="msg215"></a>

## 10. theborg · 17. Aug 2007, 17:45

> **Zitat von: fG am 17. Aug 2007, 11:21**
>
> Hallo
>
> wo gibt die Betty-Heaven.exe ?
>
> Gruß fG
>
> -found-

Hi im Wiki ist ein link

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg215#msg215)

---

<a id="msg327"></a>

## 11. Colibri · 09. Sep 2007, 19:46

Habe das Betty-Dumps.zip upgedatet:
Der Inhalt des 8 KByte EEPROMS vom Scart-Adapter ist jetzt auch mit dabei (Scart_EEPROM.bin).

Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg327#msg327)

---

<a id="msg409"></a>

## 12. Colibri · 03. Okt 2007, 19:08

Die Version 1.03 von Betty-Heaven ist jetzt verfügbar. Sie unterstützt auch das Auslesen und Beschreiben des Flashinhalts vom P89LPC931-Chip im Scart-Adapter.

Habe gleich meinen Scart-Adapter ausgelesen und das Betty-Dumps.zip upgedatet:
Neben dem Inhalt des 8 KByte EEPROMS vom Scart-Adapter ist jetzt auch der 8 KByte Flashinhalt vom P89LPC931-Chip mit dabei (Scart_Flash.bin).

Als Interface für den Scart-Adapter kann man folgendes benutzen:
[http://bettyhacks.com/wiki/index.php/Scart-Betty-Kombiinterface](../../pages/SCART-Betty-Kombiinterface.md)

Durch ein Umflashen könnte man über den Scart-Adapter Daten vom PC drahtlos zur Betty schicken und auf dem Display ausgeben lassen.

Viel Spass,
Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg409#msg409)

---

<a id="msg410"></a>

## 13. asgard · 03. Okt 2007, 19:16

Super!!

Klasse Arbeit!

Grüße und vielen dank für deine Arbeit

Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg410#msg410)

---

<a id="msg411"></a>

## 14. netguy · 03. Okt 2007, 20:19

hallo colibri,

sehr gut!

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg411#msg411)

---

<a id="msg412"></a>

## 15. netguy · 03. Okt 2007, 20:46

hallo nochmals,

sag mal, colibri ... haettest du lust mit mir zusammen unsere tools zusammenzufassen und daraus ein cross-platform taugliches paket zu machen? mittels der qt bibliothek kann man ja schoene guis erstellen die auf win, linux und mac laufen....

ich habe vor einiger zeit mal die tools fuer mein fpga-board von win nach linux portiert, [http://mamalala.org/tools.png](https://web.archive.org/web/2012/http://mamalala.org/tools.png) und der quellcode [http://mamalala.org/xstools-4.0.6-ck.tgz](https://web.archive.org/web/2012/http://mamalala.org/xstools-4.0.6-ck.tgz)
( leider in der form unter win ohne kommunikation mit dem parport, da ich won win-programmierung ca. 0 ahnung habe....)

die tools sind drei teile: einmal eine lib mit der gesamten funktionalitaet, dann einmal kommandozeilen-tools die diese lib nutzen, als auch die gui-tools, die ebenfalls diese lib benutzen. so hat man beide welten....

sowas wie das qxsload, halt nur fuer die betty sachen .... ich bin auch dabei einen usb auf seriell/jtag dongle zu machen, um moeglichst alles nutzen zu koennen.

was haelst du davon?

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=33.msg412#msg412)

---

## Verwandte Themen

- [Installation Betty Heaven](0107-installation-betty-heaven.md)
- [Handydatenkabel und Betty Heaven](0152-handydatenkabel-und-betty-heaven.md)
- [Betty-Heaven Problem: Keine Com-Ports](0180-betty-heaven-problem-keine-com-ports.md)
- [Betty-Heaven tot?](0296-betty-heaven-tot.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
