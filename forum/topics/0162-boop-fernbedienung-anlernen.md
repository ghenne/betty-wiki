---
title: "Boop: Fernbedienung anlernen"
topic_id: 162
board: "Software"
board_id: 6
posts: 16
first_post: "17. Okt 2008, 12:10"
last_post: "21. Dez 2008, 18:04"
authors: ["Hartmut", "Megabug", "Telekatz", "edison", "eme", "loswillios", "temp12"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=162.0"
---

# Boop: Fernbedienung anlernen

[← Software](../boards/06-software.md) · Thema 162 · 16 Beiträge · 17. Okt 2008, 12:10 – 21. Dez 2008, 18:04

Beteiligt: Hartmut, Megabug, Telekatz, edison, eme, loswillios, temp12

---

<a id="msg1122"></a>

## 1. Hartmut · 17. Okt 2008, 12:10

Mahlzeit,

ist es mittlerweile möglich, Boop per anderen Fernbedienung anzulernen (so wie es bei der Original-Betty war), oder was ist mit "Es ist auch möglich, ein IR-Signal aufzuzeichnen und wieder abzuspielen." gemeint?

Gruß
Hartmut

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1122#msg1122)

---

<a id="msg1123"></a>

## 2. Telekatz · 17. Okt 2008, 18:32

Damit ist gemeint, das die Anlernfunktion noch nicht über das Teststadium hinausgekommen ist. Hatte bisher noch nicht die Zeit/Lust/Notwendigkeit das funktionstauglich zu implementieren.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1123#msg1123)

---

<a id="msg1147"></a>

## 3. edison · 04. Nov 2008, 13:14

Schade eigentlich, genau das trennt Boop noch von meinem Wohnzimmer.

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1147#msg1147)

---

<a id="msg1162"></a>

## 4. Telekatz · 17. Nov 2008, 19:16

Hallo,

ich hab mal damit angefangen die Anlernfunktion zu implementieren. Momentan lässt sich nur eine Fernbedienung anlernen und auf eine der Tasten A-D legen. Die Anlernfunktion ist im Menü "Settings" zu finden, als Encoder isr "learn/RAW slot1" zu verwenden.

Sollte jemand eine Fernbedienung haben, dessen Codes sich nicht anlernen lassen, dann bitte hier den Typ posten.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1162#msg1162)

---

<a id="msg1165"></a>

## 5. temp12 · 18. Nov 2008, 12:55

> **Zitat von: Telekatz am 17. Nov 2008, 19:16**
>
> Hallo,
>
> ich hab mal damit angefangen die Anlernfunktion zu implementieren. Momentan lässt sich nur eine Fernbedienung anlernen und auf eine der Tasten A-D legen. Die Anlernfunktion ist im Menü "Settings" zu finden, als Encoder isr "learn/RAW slot1" zu verwenden.
>
> Sollte jemand eine Fernbedienung haben, dessen Codes sich nicht anlernen lassen, dann bitte hier den Typ posten.
>
> Gruß
> Telekatz

Wird nur RC5 unterstützt oder auch andere Codecs?

Gruß

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1165#msg1165)

---

<a id="msg1166"></a>

## 6. eme · 18. Nov 2008, 18:53

Vielleicht kannst Du die lirc Formate unterstützen? Oder eine Möglichkeit vorsehen, dass lirc Daten benuzt werden können? Nur als Anregung, ich habe vorerst keinen Bedarf.

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1166#msg1166)

---

<a id="msg1167"></a>

## 7. Telekatz · 18. Nov 2008, 19:10

> **Zitat**
>
> Wird nur RC5 unterstützt oder auch andere Codecs?

Das hat mit RC5 nichts zu tun, es gehen auch andere.

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1167#msg1167)

---

<a id="msg1168"></a>

## 8. edison · 20. Nov 2008, 13:35

Superbesten Dank,
- wenn das klappt, dann bin ich erstmal wieder zutiefst beeindruckt

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1168#msg1168)

---

<a id="msg1169"></a>

## 9. edison · 22. Nov 2008, 21:21

Betty boop im Wohnzimmer
Habs geschafft und ein Mischmasch von 3 Fernbedieningen angelernt.
Mein Sohn ist begeistert - Spiele auf der Fernbedienung
DANKE

einziger Haken:
einen RC5 Code hab ich nicht reinbekommen - wenn ich jetzt die TV taste drücke stürzt Betty ab

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1169#msg1169)

---

<a id="msg1170"></a>

## 10. Telekatz · 23. Nov 2008, 12:44

> **Zitat**
>
> einziger Haken:
> einen RC5 Code hab ich nicht reinbekommen - wenn ich jetzt die TV taste drücke stürzt Betty ab

Lies mal mit Betty Heaven den Inhalt von Flash2 aus und schick es mir.

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1170#msg1170)

---

<a id="msg1195"></a>

## 11. Megabug · 20. Dez 2008, 09:00

Telekatz: Super mit dem anlernen!

Wenn man jetzt noch mehr wie 4 Fernbedienungen belegen könnte, währe es perfekt.

Also sowas wie Betty+A-D um 8 FBs zu nutzen währe super.

Gruß

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1195#msg1195)

---

<a id="msg1196"></a>

## 12. loswillios · 20. Dez 2008, 16:50

wow, funktioniert klasse! Meine Betty startet zwar ganz gern mal neu aber die Änderungen sind ja zum Glueck konstant

Hat es schon jemand hinbekommen die Fernbedienung der S100 anzulernen? Es funktioniert zwar, aber wenn ich anschliessend die Tasten aufrufe ist es ein Gluecksspiel ob die S100 auf das Signal reagiert

*Last Edit : 20. Dez 2008, 16:52 by loswillios*

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1196#msg1196)

---

<a id="msg1197"></a>

## 13. eme · 20. Dez 2008, 23:46

> anzulernen ... Gluecksspiel ... reagiert

Vielleicht wird beim Anlernen die Toggle-Information nicht erkannt?

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1197#msg1197)

---

<a id="msg1198"></a>

## 14. loswillios · 20. Dez 2008, 23:58

Koennte sein.. Kann ich das testen? Die S100 reagiert wirklich sehr selten auf das Signal, und wenn dann nur nach langem rumdruecken auf der Betty.

Manchmal ist es auch so, dass die Betty reproduzierbar neustartet wenn ich eine Taste druecke, auf der ein S100 Code liegt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1198#msg1198)

---

<a id="msg1199"></a>

## 15. Telekatz · 21. Dez 2008, 16:34

Toggle-Bit wird beim anlernen noch nicht unterstützt.

Hab den Code der S100 mal auf meine Harmony geladen und die Betty damit angelernt. Sieht eigentlich ganz normal aus. Bei welcher Taste startet die Betty denn neu?

Schick mir mal den Inhalt vom Flash2 deiner Betty.

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1199#msg1199)

---

<a id="msg1200"></a>

## 16. loswillios · 21. Dez 2008, 18:04

nach einem tip von telekatz habe ich in der ir_capture.c zeile 312 von cmd->borders = 0x13; nach cmd->borders = 0x12; geaendert und nun laeuft's!

[Permalink](http://bettyhacks.com/forum/index.php?topic=162.msg1200#msg1200)

---

## Verwandte Themen

- [Neue Fernebdienung mit lirc anlernen für Boop](0259-neue-fernebdienung-mit-lirc-anlernen-fuer-boop.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
