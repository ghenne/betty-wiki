---
title: "PCD80718HL programmieren"
topic_id: 233
board: "Hardware"
board_id: 5
posts: 6
first_post: "18. Feb 2010, 10:45"
last_post: "19. Feb 2010, 09:36"
authors: ["Telekatz", "gunnar"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=233.0"
---

# PCD80718HL programmieren

[← Hardware](../boards/05-hardware.md) · Thema 233 · 6 Beiträge · 18. Feb 2010, 10:45 – 19. Feb 2010, 09:36

Beteiligt: Telekatz, gunnar

---

<a id="msg1601"></a>

## 1. gunnar · 18. Feb 2010, 10:45

Hallo,

hat sich schon mal jemand an diesen Chip im Scart Adapter gewagt und z.B. etwas mit OpenOCD gemacht?
Ich kann den PCD nicht per JTAG ansprechen, wahrscheinlich weil er vom MSP abgeschaltet ist:

> **Zitat von: Telekatz am 22. Okt 2008, 21:22**
>
> Der ARM wird wohl wirklich nur als Modem verwendet. Wenn keine Verbindung zur Bettyzentrale verlangt wird, ist die Stromversorgung zum ARM abgeschaltet.

Hat schon jemand herausgefunden über welchen Portpin des MSP man den PCD einschalten kann? Ich habe die betty_tae Firmware auf dem MSP, die schaltet den PCD aber anscheinend nicht ein.

@Telekatz und andere über das PCD80718HL Datenblatt verfügende:
Es wäre nett, wenn mir jemand das PCD Datenblatt schicken würde.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=233.msg1601#msg1601)

---

<a id="msg1602"></a>

## 2. Telekatz · 18. Feb 2010, 11:40

Hallo Gunnar,

Die Stromversorgung zum ARM müsste wenn ich mich noch recht erinnere über P2.5 LINE_CONTROL eingeschaltet werden.
Wie sieht deine Spannungsversorgung zum TAE Adapter aus?

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=233.msg1602#msg1602)

---

<a id="msg1603"></a>

## 3. gunnar · 18. Feb 2010, 12:01

Hallo Telekatz,

ich speise die 3,3V des Pollin CPLD Boards von dem ich auch die JTAG Signale abnehme über den Pfostenstecker ein. Zieht der PCD so viel Strom?
Hast Du die Datenblätter noch?

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=233.msg1603#msg1603)

---

<a id="msg1604"></a>

## 4. Telekatz · 18. Feb 2010, 20:06

Über den Pfostenstecker lässt sich nur der MSP fremdversorgen.
Um den ARM zu versorgen musst du schon am TAE Stecker einspeisen. Etwa 20V zwischen La und Lb müssten reichen.
Datenblatt kommt mit der elektrischen Post.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=233.msg1604#msg1604)

---

<a id="msg1605"></a>

## 5. gunnar · 18. Feb 2010, 22:31

Hallo Telekatz,

danke für den Tip! Daran liegt es wahrscheinlich, dass die Kontaktaufnahme per Jtag nicht geht. In der Betty TAE Firmware wird  der PCD  eingeschaltet, dort finden sich die Zeilen:
  P2DIR = ACLK | VEGA_MISO | ADC_IN1 | LINE_CONTROL;

  P2SEL = ACLK | XIN | XOUT;

  P2OUT = LINE_CONTROL;
Wobei mir da auffällt, dass in P2SEL eigentlich auch das LINE_CONTROL Bit gesetzt werden müsste, damit es ein normaler Portpin ist (MSP Datenblatt Seite 30), oder?
Danke für das PCD Datenblatt, das ist ein wirklich mächtiger Controller...

> **Zitat von: Telekatz am 18. Feb 2010, 20:06**
>
> Über den Pfostenstecker lässt sich nur der MSP fremdversorgen.
> Um den ARM zu versorgen musst du schon am TAE Stecker einspeisen. Etwa 20V zwischen La und Lb müssten reichen.
> Datenblatt kommt mit der elektrischen Post.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=233.msg1605#msg1605)

---

<a id="msg1606"></a>

## 6. Telekatz · 19. Feb 2010, 09:36

> **Zitat**
>
> Wobei mir da auffällt, dass in P2SEL eigentlich auch das LINE_CONTROL Bit gesetzt werden müsste, damit es ein normaler Portpin ist (MSP Datenblatt Seite 30), oder?

Das passt schon, siehe MSP430x1xx Family User Guide:

> **Zitat**
>
> Port pins are often multiplexed with other peripheral module functions. See the
> device-specific data sheet to determine pin functions. Each PxSEL bit is used
> to select the pin function − I/O port or peripheral module function.
> Bit = 0: I/O Function is selected for the pin
> Bit = 1: Peripheral module function is selected for the pin

[Permalink](http://bettyhacks.com/forum/index.php?topic=233.msg1606#msg1606)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
