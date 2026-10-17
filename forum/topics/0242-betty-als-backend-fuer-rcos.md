---
title: "Betty als Backend für RCOS !?"
topic_id: 242
board: "Sonstiges"
board_id: 7
posts: 4
first_post: "05. Okt 2010, 21:33"
last_post: "08. Feb 2011, 19:03"
authors: ["eme", "olli"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=242.0"
---

# Betty als Backend für RCOS !?

[← Sonstiges](../boards/07-sonstiges.md) · Thema 242 · 4 Beiträge · 05. Okt 2010, 21:33 – 08. Feb 2011, 19:03

Beteiligt: eme, olli

---

<a id="msg1674"></a>

## 1. eme · 05. Okt 2010, 21:33

Ich weiß nicht genau, was es damit auf sich hat, aber in irgendeinem Zusammenhang mit DIY Modellfernsteuerungen wird die Betty genannt:

rCos (RemoteControl-OperatingSystem) is a software- and toolset for building modern computer remote controls for rc-models. In the core of the system there is an STM32 Microcontroller with C Open-Source firmware and multiple hardware expansion interfaces (SPI, Serial, I2C, ...).

[http://www.rcos.eu/targets/betty-backend/index.html](https://web.archive.org/web/2012/http://www.rcos.eu/targets/betty-backend/index.html)

[Permalink](http://bettyhacks.com/forum/index.php?topic=242.msg1674#msg1674)

---

<a id="msg1687"></a>

## 2. olli · 13. Okt 2010, 19:25

Hi,
ich kann dir sagen was es zu bedeuten hat 

rCOS ist wie gesagt eine Firmware für RC-Fersteuerungen,
da die Software möglichst Kompatiebel gehalten werden sollte,
wurden alle verfügbaren Controller-Boards genommen und die Software daran angepasst.
Wirklich nutzen tut diese Portierung nichts, da die Betty etwas Unförmig ist und auch nicht auf Anhieb genug ADC_Eingänge bietet.
Wer das Ding jedoch in ein Sender-Gehäuse bekommt und ein paar Tasten in ADC-Pin's umbaut kann da auch ne Fernsteuerung draus bauen !

DBD
 Olli

[Permalink](http://bettyhacks.com/forum/index.php?topic=242.msg1687#msg1687)

---

<a id="msg1689"></a>

## 3. eme · 14. Okt 2010, 19:24

D.h. RCOS ist GUI, Modellspeicher, Mixer, Kanalzuweiser, PPM-Generator? Also "ein paar Knöpfe" und ein HF-Modul an die Betty und los geht's?

[Permalink](http://bettyhacks.com/forum/index.php?topic=242.msg1689#msg1689)

---

<a id="msg1868"></a>

## 4. olli · 08. Feb 2011, 19:03

Hi,
und sorry für die späte Reaktion !

>> D.h. RCOS ist GUI, Modellspeicher, Mixer, Kanalzuweiser, PPM-Generator? Also "ein paar Knöpfe" und ein HF-Modul an die Betty und los geht's?

Da der Betty zu wenige ADC's zur Verfühgung stehen und das Gehäuse-Format etwas unpraktisch ist,
macht es nicht viel Sinn diese als Fernsteuerung zu nutzen.

Sollte nur ein Portierungs-Test sein !!!

Sinn hat es aber trotzdem gemacht, da ich auf dieser Basis was anderes gebastelt habe:
 [http://bettyhacks.com/forum/index.php?topic=258.0](0258-betty-als-lowcost-oszilloskop.md)

Grüße,
 Olli

[Permalink](http://bettyhacks.com/forum/index.php?topic=242.msg1868#msg1868)

---

## Verwandte Themen

- [Betty als lowcost Oszilloskop](0258-betty-als-lowcost-oszilloskop.md)

[← Zurück zu Sonstiges](../boards/07-sonstiges.md) · [Gesamtindex](../index.md)
