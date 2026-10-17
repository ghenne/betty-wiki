---
title: "Swisscom Betty"
topic_id: 128
board: "Hardware"
board_id: 5
posts: 4
first_post: "30. Mär 2008, 17:02"
last_post: "31. Mär 2008, 20:32"
authors: ["Gentoo07", "famos"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=128.0"
---

# Swisscom Betty

[← Hardware](../boards/05-hardware.md) · Thema 128 · 4 Beiträge · 30. Mär 2008, 17:02 – 31. Mär 2008, 20:32

Beteiligt: Gentoo07, famos

---

<a id="msg904"></a>

## 1. famos · 30. Mär 2008, 17:02

Hallo zusammen,

ich habe eine Swisscom Betty und musste feststellen, dass boop nur teilweise läuft. Das Logo und die Zeit werden angezeigt aber sonst geht nichts mehr.

Folgende Unterschiede habe ich bis jetzt rausgefunden:

- Der Print ist Revision V2.0
- Die FlashRoms sind vom Type EN29LV400AB-70TCP
- Das Keymapping ist unterschiedlich

Die Zuordnung der Keys habe ich mit dem Ohmmeter ausgetüftelt und in einer Tabelle zusammengefasst:
![](https://web.archive.org/web/2012/http://www.bettyhacks.com/wiki/images/1/11/SwissBetty_Key.jpg)

Gleich sind:
- Display Ansteuerung
- IR Diode
- Sound

Den RF Transceiver CC1100 habe ich noch nicht getest. Er ist nicht auf dem Mainboard sondern als Huckepack Modul auf dem Mainboard.

Ob Boop nach dem Ändern der Port Zuordnunggen läuft kann ich noch nicht sagen, da ich in der Source
Keyirq.c noch nicht verstehe warum da FIOPIN0, IOPIN3 und IOSET2 verwendet wird. Meine Keyroutine ist einfacher und sieht so aus:

`#include "keyboard.h"
#include "lpc2220.h"

unsigned char Rows[6]; // the pressed Keys ar stored here multiple Keys ar possibe
unsigned int keytest;
unsigned char help;

void initKeys(void)
{
        IODIR1=((1<<16)|(1<<17)|(1<<18)|(1<<19)|(1<<21)|(1<<22));  // 1=output
        IOSET1=((1<<16)|(1<<17)|(1<<18)|(1<<19)|(1<<21)|(1<<22));  // set to 1
        keys[0] = 0;
        keys[1] = 0;
}

void scanKeys(void)
{
 for (help=0;help<4;help++) //scan coluns P1.16 to P1.19
 {
  IOSET1=((1<<16)|(1<<17)|(1<<18)|(1<<19)|(1<<21)|(1<<22)); // 1
  keytest=IOPIN2&0x01fe0000; // read rows
  IOCLR1=(1<<(16+help));     // set low to scan
  keytest^=IOPIN2&0x01fe0000;// read rows and compare with previously read
  // Key scan algorithm: pressed Key will read as 1 after xor
  keys[help]=(unsigned char)(keytest>>18);
 }
  for (help=4;help<6;help++) //No. 20 will skipped
 {
  IOSET1=((1<<16)|(1<<17)|(1<<18)|(1<<19)|(1<<21)|(1<<22)); // 1
  keytest=IOPIN2&0x01fe0000;
  IOCLR1=(1<<(17+help));
  keytest^=IOPIN2&0x01fe0000;
  keys[help]=(unsigned char)(keytest>>18);
 }
}`

Mehr Beschreibung im Code würde allen helfen und Zeit sparen.

Danke famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=128.msg904#msg904)

---

<a id="msg905"></a>

## 2. famos · 30. Mär 2008, 22:03

Wer kann mir das für die DE-Betty ausfüllen?

![](https://web.archive.org/web/2012/http://www.bettyhacks.com/wiki/images/a/af/Matrix_DE_Betty.jpg)

Wenn nötig kann ich ein Testprogramm scannen liefern.

Danke

[Permalink](http://bettyhacks.com/forum/index.php?topic=128.msg905#msg905)

---

<a id="msg906"></a>

## 3. Gentoo07 · 30. Mär 2008, 23:17

Bitteschön, ich hab mal soweit die Bleistiftzeichnung aus dem Wiki übersetzt, scheint alles schlüssig zu sein.

Gruß

P.s.: Merkwürdige Verbindungen hier zwischen Forum und Wiki...

Ich habe gerade eben das Bild mit demselben Dateinamen ins Wiki hochgeladen, seitdem ist auch deine ehemals leere Tabelle hier im Forum durch meine volle ersetzt

*Last Edit : 30. Mär 2008, 23:59 by Gentoo07*

[Permalink](http://bettyhacks.com/forum/index.php?topic=128.msg906#msg906)

---

<a id="msg913"></a>

## 4. famos · 31. Mär 2008, 20:32

Danke!

Das schlechte Bild vom Flipchart konnte ich nicht lesen.

Gruss
famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=128.msg913#msg913)

---

## Verwandte Themen

- [Swisscom stellt interaktives Fernsehangebot (betty) wieder ein](0069-swisscom-stellt-interaktives-fernsehangebot-betty-wieder-ein.md)
- [Betty Swisscom läuft](0205-betty-swisscom-laeuft.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
