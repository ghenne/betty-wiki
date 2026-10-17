---
title: "Hallo allerseits"
topic_id: 276
board: "Sonstiges"
board_id: 7
posts: 4
first_post: "11. Dez 2011, 09:31"
last_post: "16. Dez 2011, 20:01"
authors: ["Flunder", "jannis", "togeil"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=276.0"
---

# Hallo allerseits

[← Sonstiges](../boards/07-sonstiges.md) · Thema 276 · 4 Beiträge · 11. Dez 2011, 09:31 – 16. Dez 2011, 20:01

Beteiligt: Flunder, jannis, togeil

---

<a id="msg1986"></a>

## 1. togeil · 11. Dez 2011, 09:31

Hallo allerseits,

obwohl hier die Aktivität schon ziemlich zurück gegangen ist, möchte ich ins Betty-Hacken mit einsteigen. Leider lässt sich der Boop bei mir noch nicht flashen.

Ich benutze Fedora 16 und habe das lpctool selbst übersetzt. Mein Kabel basiert auf einem FDTI-Chip und hat mir für andere Geräte schon gute Dienste geleistet. (Wenn man RX & TX am Ausgang brückt, kommen die Eingaben im Terminal brav zurück.) Das Flashtool scheitert, beim Verbinden mit dem Bootloader, da kein "Synchronized" zurück kommt.

Gibt es irgendwo eine Liste, was man alles falsch machen kann? Im Moment bin ich für jede Hilfe dankbar...  :'(

Grüße,
Torsten

[Permalink](http://bettyhacks.com/forum/index.php?topic=276.msg1986#msg1986)

---

<a id="msg1987"></a>

## 2. jannis · 11. Dez 2011, 11:09

Welchen Pegel hat dein Kabel? 3,3V?
Hast du den Bootloader pin auch wirklich auf ground gezogen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=276.msg1987#msg1987)

---

<a id="msg1988"></a>

## 3. Flunder · 11. Dez 2011, 17:20

> **Zitat von: jannis am 11. Dez 2011, 11:09**
>
> Hast du den Bootloader pin auch wirklich auf ground gezogen?

Ich möchte hier noch ergänzen: Beim Reset bzw. beim Einlegen der Batterien um einen Reset zu erzeugen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=276.msg1988#msg1988)

---

<a id="msg1989"></a>

## 4. togeil · 16. Dez 2011, 20:01

He mit so schneller Hilfe hatte ich gar nicht gerechnet. Vielen Dank.

Mein Adapter arbeitet eher mit 5 V, da ich die Signale direkt am FDTI-Chip abgreife. In Ausgangsrichtung habe ich deshalb relative große Widerstände (irgendwas im Kilo-Ohm-Bereich aus der Bastelkiste) drin. Da der FDTI-Chip nicht kurzschlussfest ist, müssen es mindestens 300 Ohm sein. (Sowas hatte ich nicht rumliegen.)

In meinem heutigen Versuch sieht es schon etwas besser aus. Ich verwende statt der Akkus jetzt ein Labornetzteil, welches an den Batteriekontakten angeschlossen ist. Anstatt dem erwarteten "Synchronized" kommen jetzt irgendwelche Versionsinformationen... Kann es sein, dass ich zwar den Reset ausgelöst habe, aber den Bootloader nicht aktiviert habe? - Mein Interface versucht per DTR den Reset bzw. per RTS den Bootloader auszulösen.

Grüße,
Torsten

[Permalink](http://bettyhacks.com/forum/index.php?topic=276.msg1989#msg1989)

---

[← Zurück zu Sonstiges](../boards/07-sonstiges.md) · [Gesamtindex](../index.md)
