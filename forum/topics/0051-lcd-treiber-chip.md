---
title: "lcd treiber chip"
topic_id: 51
board: "Hardware"
board_id: 5
posts: 6
first_post: "06. September 2007, 15:52"
last_post: "07. September 2007, 21:06"
authors: ["asgard", "minipilot", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=51.0"
---

# lcd treiber chip

[← Hardware](../boards/05-hardware.md) · Thema 51 · 6 Beiträge · 06. September 2007, 15:52 – 07. September 2007, 21:06

Beteiligt: asgard, minipilot, netguy

---

<a id="msg307"></a>

## 1. netguy · 06. September 2007, 15:52

hallo allerseits,

so wie es aussieht ist der verwendete controller des lcd's von epson. den genauen typen habe ich nocht raus, allerding kann man z.b. mal in das datenblatt der S1D15710 serie schauen. das ist zwar nur ein s/w controller, und nicht 4 graustufen, aber soweit passen alle aufgefuehrten kommandos:
E1 = reset power save, E2 = reset, 81 = electronic control (kontrast), 80/81 display noprmal/umgedreht, AE/AF = display off/on, etc...

wer mag kann ja mal bei epson nach graustufen-controllern schauen (4 stufen), ansonsten mache ich das mal am wo-ende.

gruesse,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=51.msg307#msg307)

---

<a id="msg312"></a>

## 2. minipilot · 06. September 2007, 23:04

Ich weiss nicht, ob es hilft:

[http://doc.chipfind.ru/epson/](https://web.archive.org/web/2012/http://doc.chipfind.ru/epson/)

Das Dokument 218 scheint eine Art übersicht zu sein. Bei Epson selbst habe ich nichts vernünftiges finden können.

Die Befehle scheinen bei allen der Serie gleich zu sein...

Grüße minipilot

[Permalink](http://bettyhacks.com/forum/index.php?topic=51.msg312#msg312)

---

<a id="msg314"></a>

## 3. netguy · 07. September 2007, 13:46

hallo,

so, soweit ich sehen kann handelt es sich um diesen chip:
[http://www.datasheet4u.com/html/S/S/D/SSD1854_ETC.pdf.html](https://web.archive.org/web/2012/http://www.datasheet4u.com/html/S/S/D/SSD1854_ETC.pdf.html)

alle kommandos der init sequenz stehen da ebenfalls drin, und sie machen tatsaechlich sinn ;-)
das display kann einige nette spielereien, wird zeit fuer mich die lcd-ansteuerung zu ueberarbeiten ...

gruesse,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=51.msg314#msg314)

---

<a id="msg315"></a>

## 4. asgard · 07. September 2007, 16:38

Hey,

netguy du bist einfach spitze!  ![Cool](https://web.archive.org/web/2012/http://bettyhacks.com/forum/Smileys/default/cool.gif)

Grüße und weiter so ![Zwinkernd](https://web.archive.org/web/2012/http://bettyhacks.com/forum/Smileys/default/wink.gif)

asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=51.msg315#msg315)

---

<a id="msg319"></a>

## 5. minipilot · 07. September 2007, 19:38

Doch nicht epson.

Wie hast du das rausgefunden?

Ich bin mal gespannt was sich dahinter verbirgt:

F0~FF 1111 XXXX Extended
Features
Test mode commands and Extended features

Gruss

minipilot

[Permalink](http://bettyhacks.com/forum/index.php?topic=51.msg319#msg319)

---

<a id="msg322"></a>

## 6. netguy · 07. September 2007, 21:06

> **Zitat von: minipilot am 07. September 2007, 19:38**
>
> Doch nicht epson.
>
> Wie hast du das rausgefunden?

ersttmal habe ich epson abgegrast, aber da gabs nix passendes von der aufloesung her ...
dann habe ich nac "lcd driver 160 x 128" gegoogelt und mir einfach solange alle datenblaetter angesehen, bis das passende aufgetaucht ist ![Zwinkernd](https://web.archive.org/web/2012/http://bettyhacks.com/forum/Smileys/default/wink.gif)

und es ist exact das display, das sieht man gegen ende des datenblattes, da ist eine zechnung des flex-traegers mit chip drin, die exact dem des display in der betty entspricht.

eigentluich schade das es kein epson ist: die haben naemlich einen read-modify-write modus, in dem der interne zaehler nur bei einem write weiterzaehlt, aber nicht bei einem read. naja, was solls, geht ja auch so ;-D

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=51.msg322#msg322)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
