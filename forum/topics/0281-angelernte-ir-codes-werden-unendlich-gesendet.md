---
title: "Angelernte IR-Codes werden 'unendlich' gesendet"
topic_id: 281
board: "Software"
board_id: 6
posts: 6
first_post: "17. Okt 2012, 07:22"
last_post: "18. Okt 2012, 22:51"
authors: ["eazee", "gunnar", "mx"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=281.0"
---

# Angelernte IR-Codes werden "unendlich" gesendet

[← Software](../boards/06-software.md) · Thema 281 · 6 Beiträge · 17. Okt 2012, 07:22 – 18. Okt 2012, 22:51

Beteiligt: eazee, gunnar, mx

---

<a id="msg2042"></a>

## 1. eazee · 17. Okt 2012, 07:22

Hallo,

auch auf die Gefahr hin, dass es relativ lange dauert, bis es eine Antwort gibt, stelle ich trotzdem meine Frage. ;-)

Ich habe schon stundenlang gesucht, finde die Ursache für folgendes Problem aber nicht.
Angelernte IR-Codes werden nach erfolgreicher Programmierung undendlich lange gesendet. Im Testmodus während des Anlernens funktioniert es allerdings einwandfrei. Sobald man zurück zum "Normalmodus" geht und eine Taste drückt, wird der IR-Code gesendet und gesendet und gesendet.

Die Betty hängt sich dabei nicht auf, die Uhr läuft beispielsweise problemlos weiter. IR wird aber halt nicht abgeschaltet.

Wo muss ich nochmal hinschauen, damit man das korrigieren kann? ir_raw...?

Schöne Grüße und schon mal Danke,
eazee

[Permalink](http://bettyhacks.com/forum/index.php?topic=281.msg2042#msg2042)

---

<a id="msg2043"></a>

## 2. gunnar · 17. Okt 2012, 10:07

Hallo,

ich habe die Betty auch als FB benutzt und konnte so einen Effekt nicht beobachten. Vielleicht klemmt die Taste?
Mit einer Digitalkamera oder Webcam kann man das Infrarotlicht ganz gut sichtbar machen.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=281.msg2043#msg2043)

---

<a id="msg2044"></a>

## 3. eazee · 17. Okt 2012, 10:20

Hallo gunnar,

danke für deine schnelle Antwort!!!!
vielleicht hätte ich erwähnen sollen, dass bereits boop drauft läuft und alle anderen (bspweise lirc) ohne Probleme läuft.
Nur angelernte codes, die im RAW landen (wenn ich die sources richtig lese?) werden immer unendlich gesendet nach Tastendruck.
(egal ob von DBOx2 oder TV angelernt)

Sieht fast so aus, als würde man niemals im void RAW_Stop(void) landen?!

*Last Edit : 17. Okt 2012, 12:07 by eazee*

[Permalink](http://bettyhacks.com/forum/index.php?topic=281.msg2044#msg2044)

---

<a id="msg2045"></a>

## 4. eazee · 17. Okt 2012, 19:56

Sodele, es gibt was neues.

Oben genannte Probleme hatte ich bei einer Swisscom Betty, hab den gleichen Code mal (natürlich ohne die Swisscom-Anpassungen) mal auf ne Betty Betty geflasht, und man höre und staune: ES GEHT!

Stellt sich natürlich nur die Frage: Warum?

[Permalink](http://bettyhacks.com/forum/index.php?topic=281.msg2045#msg2045)

---

<a id="msg2046"></a>

## 5. mx · 18. Okt 2012, 15:23

Da ist wohl die Tastenmatrix nicht der einzige Unterschied zwischen den Hardwareversionen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=281.msg2046#msg2046)

---

<a id="msg2049"></a>

## 6. eazee · 18. Okt 2012, 22:51

Scheint wohl so zu sein, hab bis jetzt den "Fehler" aber noch nicht gefunden - leider.
Mal sehen ob mans lösen kann...

[Permalink](http://bettyhacks.com/forum/index.php?topic=281.msg2049#msg2049)

---

## Verwandte Themen

- [Bettys bei Pollin](0279-bettys-bei-pollin.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
