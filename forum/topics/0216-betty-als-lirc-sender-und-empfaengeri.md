---
title: "Betty als LIRC Sender und EmpfängerI"
topic_id: 216
board: "Hardware"
board_id: 5
posts: 6
first_post: "06. Jul 2009, 12:25"
last_post: "10. Jul 2009, 11:14"
authors: ["MrFX", "famos", "gerdi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=216.0"
---

# Betty als LIRC Sender und EmpfängerI

[← Hardware](../boards/05-hardware.md) · Thema 216 · 6 Beiträge · 06. Jul 2009, 12:25 – 10. Jul 2009, 11:14

Beteiligt: MrFX, famos, gerdi

---

<a id="msg1452"></a>

## 1. gerdi · 06. Jul 2009, 12:25

Ich möchte die Betty als Infrarot Sender/Empfänger an einen PC anschliessen (z.B über USB).
Er läuft mit Linux.

Am liebsten wäre mir, wenn die Betty so LIRC-kompatibel wäre.

Hat jemand eine Idee für einen Umbau?

[Permalink](http://bettyhacks.com/forum/index.php?topic=216.msg1452#msg1452)

---

<a id="msg1460"></a>

## 2. famos · 09. Jul 2009, 22:35

Hallo Gerdi,

die Betty kann man sicher für jenes gebrauchen. Nur als LIRC Sende/Empfänger am PC ist sie fast zu schade. Falls Du das machen möchtest gibt es verschieden Möglichkeiten:
Du verwendest einen FTDI FT245 Chip, den kann man an den Bus hängen und die Performance ist recht gut. 800kB/sec liegen schon drin. Oder du verwendest die serielle Schnittstelle, so wie du die Betty programmiert, oder über einen FT232.

Gruss famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=216.msg1460#msg1460)

---

<a id="msg1461"></a>

## 3. gerdi · 10. Jul 2009, 00:41

Danke Famos.

Eigentlich habe ich die Betty vor allem deshalb gekauft.

Ich möchte endlich meinen Fernseher und meine Stereo per Computer ein- und ausschalten. Ich kenne mich aber mit Hardware nicht aus.
Nirgends findet man einen LIRC-Sender. Alles ist zu schnell (Handy IR-USB-Stick geht nicht.)

Ich glaube der Lirc-Sender braucht noch eine Batterie, damit er ausreichend Amperes hat, um auf ein paar Meter zu senden, bei geringem Verbrauch.

Sicher kein kompliziertes Bauteil, aber nirgends zu finden!!!!

Ich will einfach einen LIRC-Sender mit USB. Wenn die Betty das kann sind alle meine Probleme gelöst.

[Permalink](http://bettyhacks.com/forum/index.php?topic=216.msg1461#msg1461)

---

<a id="msg1462"></a>

## 4. MrFX · 10. Jul 2009, 06:18

Moin!

Technisch kann das die Betty sicher, aber dann musst du dir die passende Software dazu programmieren.

Einfacher würde es natürlich gehen, wenn du so was nimmst:

[http://www.huitsing.nl/irftdi/](https://web.archive.org/web/2012/http://www.huitsing.nl/irftdi/)

Da brauchst du eigentlich nicht viel dazu... zumal du für die Betty-Lösung auch mindestens einen USB-Serial-Wandler benötigst.

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=216.msg1462#msg1462)

---

<a id="msg1463"></a>

## 5. gerdi · 10. Jul 2009, 08:39

"Nehmen" ist gut gesagt.

So etwas bringe ich nie zu Stande. Ich habe noch nicht einmal einen vernünftigen Lötkolben.
Ich weiss noch nicht einmal, wo ich die Teile in der Schweiz zu vernünftigen Preisen erhalte.
Testen könnte ich schon gar nicht, falls mir ein Fehler unterliefe.

... und noch etwas:
Hat der Kondensator genug Kapazität, dass das IR-Signal ein paar Meter schiesst?

Auf der Software-Seite habe ich da viel weniger Schwierigkeiten.

*Last Edit : 10. Jul 2009, 08:42 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=216.msg1463#msg1463)

---

<a id="msg1464"></a>

## 6. MrFX · 10. Jul 2009, 11:14

Moin!

Ja, aber für die Betty brauchst du ja auch erstmal Hardware, um sie mit dem Rechner zu verbinden...
Wenn du die natürlich schon hast, dann kannst du ja loslegen mit dem Programmieren...

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=216.msg1464#msg1464)

---

## Verwandte Themen

- [Betty, andere Sender?](0056-betty-andere-sender.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
