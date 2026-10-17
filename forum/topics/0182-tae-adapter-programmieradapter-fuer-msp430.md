---
title: "TAE Adapter - Programmieradapter für MSP430"
topic_id: 182
board: "Hardware"
board_id: 5
posts: 11
first_post: "14. Jan 2009, 22:36"
last_post: "11. Sep 2009, 19:02"
authors: ["MrFX", "Telekatz", "gerdi", "mcfloppy", "phaidros", "skolapper"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=182.0"
---

# TAE Adapter - Programmieradapter für MSP430

[← Hardware](../boards/05-hardware.md) · Thema 182 · 11 Beiträge · 14. Jan 2009, 22:36 – 11. Sep 2009, 19:02

Beteiligt: MrFX, Telekatz, gerdi, mcfloppy, phaidros, skolapper

---

<a id="msg1231"></a>

## 1. Telekatz · 14. Jan 2009, 22:36

Katertag,

ich habe mich mal mit dem TAE Adapter etwas näher beschäftigt und ein JTAG Programmieradapter für den MSP430 erstellt. Schaltplan, Stückliste, Bestückungsplan und Layout sind im angefängten PDF.

Der JTAG Adapter benötigt eine externe Stromversorgung über die der TAE Adapter zum Programmieren gleich mitversorgt wird.  An die Stiftleiste des TAE Adapters wird der JTAG Adapter 1:1 angeschlossen.

Die Schaltung ist kompatibel zu den gängigen MSP JTAG Parallelport Programmieradaptern und kann die gleiche Programmiertools verwenden (z.B. MSPFET [http://kurt.on.ufanet.ru/](https://web.archive.org/web/2012/http://kurt.on.ufanet.ru/) oder mit MSPGCC).

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1231#msg1231)

---

<a id="msg1232"></a>

## 2. phaidros · 15. Jan 2009, 01:34

Die Schaltung verstehe ich, habe mich aber mit dem ganzen JTAG Kram noch nie befasst.
Ist JTAG denn unbedingt nötig oder wäre eine Programmierung über den seriellen Bootloader BSL auch möglich?

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1232#msg1232)

---

<a id="msg1234"></a>

## 3. Telekatz · 15. Jan 2009, 09:18

BSL währe eventuell auch möglich. Die erforderlichen Pins des MSP sind aber nicht alle an der Stiftleiste herausgeführt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1234#msg1234)

---

<a id="msg1235"></a>

## 4. MrFX · 15. Jan 2009, 10:31

Moin!

Was könnte man denn überhaupt damit machen? Die Pins für 'nen UART z. B. sind ja auch nicht an der Stiftleiste...

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1235#msg1235)

---

<a id="msg1236"></a>

## 5. Telekatz · 15. Jan 2009, 11:55

z.B. könnte man versuchen einen ENC28J60 an den ARM anzuschließen, um daraus einen IP-Adapter zu machen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1236#msg1236)

---

<a id="msg1357"></a>

## 6. mcfloppy · 27. Apr 2009, 00:15

so, habs nachgelötet, aber iwie gehts nicht
01:13:39  Initialize...
01:13:40  Init failed. Could not find device (or device not supported).

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1357#msg1357)

---

<a id="msg1358"></a>

## 7. Telekatz · 27. Apr 2009, 20:24

"FET direct access" schonmal probiert?
Versorgungsspannung vorhanden?
TAE Adapter nur am Programmer anschließen, nicht am Telefonnetz.

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1358#msg1358)

---

<a id="msg1359"></a>

## 8. mcfloppy · 27. Apr 2009, 21:31

Im direct access sagt erschluss nicht öffnen. am TAE hängt er nicht, aber ich speiße die spannung über dien tae stecker ein.

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1359#msg1359)

---

<a id="msg1360"></a>

## 9. gerdi · 28. Apr 2009, 00:58

> **Zitat**
>
> z.B. könnte man versuchen einen ENC28J60 an den ARM anzuschließen, um daraus einen IP-Adapter zu machen.

Das verstehe ich leider nicht.

Aber vielleicht hat es etwas mit meiner Idee zu tun.
Wenn ich es recht verstanden habe, dann sendet die Betty über den TAE-Adapter ins Telefonnetz.

Ich telefoniere nur noch über das Internet, mittels eines Sip-Adapters.
Dieser Sip-Adapter hat noch einen Anschluss frei.
Nun möchte ich den TAE an diesen Anschluss hängen. Dann konfiguriere ich den Sip-Adapter so, dass der Anschluss nicht an die externe Sip-Adresse geht, sondern an meinen persönlichen Domain-Namen.

So könnte ich dann über mein Lan mit der Betty kommunizieren, auf Port 5060.

Hat jemand schon etwas in dieser Richtung gemacht?

(Ich habe am Lan noch einen Asus wl500gp hängen, auf dem ich einen Asterisk installieren könnte.)

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1360#msg1360)

---

<a id="msg1478"></a>

## 10. skolapper · 11. Sep 2009, 17:06

ist der adapter mit ftdi wirklich gut? mein allerwelts usb > rs232 adapter macht zwar die programmieradapter, aber nicht den umsetzer micromaster4 auf pc, vielleicht kennt jemand was kostengьnstiges das das auch kann.

<sub>

[my page](https://web.archive.org/web/2012/http://www.codeproject.com/Members/poretjelas)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1478#msg1478)

---

<a id="msg1479"></a>

## 11. Telekatz · 11. Sep 2009, 19:02

> **Zitat**
>
> ist der adapter mit ftdi wirklich gut? mein allerwelts usb > rs232 adapter macht zwar die programmieradapter, aber nicht den umsetzer micromaster4 auf pc, vielleicht kennt jemand was kostengьnstiges das das auch kann.

Was hat das mit diesem Thema zu tun? 
Hier wird der FTDI nicht mal erwähnt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=182.msg1479#msg1479)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
