---
title: "Was ist möglich?"
topic_id: 290
board: "Sonstiges"
board_id: 7
posts: 3
first_post: "28. Dez 2012, 17:52"
last_post: "22. Okt 2013, 14:38"
authors: ["OCMoe", "Robi2003", "mx"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=290.0"
---

# Was ist möglich?

[← Sonstiges](../boards/07-sonstiges.md) · Thema 290 · 3 Beiträge · 28. Dez 2012, 17:52 – 22. Okt 2013, 14:38

Beteiligt: OCMoe, Robi2003, mx

---

<a id="msg2100"></a>

## 1. Robi2003 · 28. Dez 2012, 17:52

Hallo!

Habe hier gerade meine alte Betty mit Scart-Anschluss und IP-Adapter gefunden...

Wollte mal gern wissen, was man damit noch so schönes machen kann...

Der IP-Adapter interessiert mich irgendwie mehr ^^
Es ist aber nicht möglich, daraus einen kleinen Server oder sowas zu machen?

Schöne Grüße und vielen Dank im Voraus!

[Permalink](http://bettyhacks.com/forum/index.php?topic=290.msg2100#msg2100)

---

<a id="msg2105"></a>

## 2. OCMoe · 14. Jan 2013, 20:20

Da werkelt ein kleiner Mikrocontroller (mit 8051-Kern) drin, der 512k Flash-Speicher und 32k RAM hat. Viel wirste damit nicht anstellen können, da du keinerlei Standardsoftware verwenden kannst. Schon einfach nur einen C-Compiler dafür zu bekommen dürfte nicht ganz leicht sein -- von Keil gibt es eine kommerzielle Lösung, und das wars, so scheint es. Da bist du z.B. mit einem AVR NetIO besser bedient, das du dann seriell an den SCART-Adapter anschliesst.

Falls du den dennoch sinnvoll verwendet wissen möchtest, kannst du ihn mir aber gerne verkaufen

[Permalink](http://bettyhacks.com/forum/index.php?topic=290.msg2105#msg2105)

---

<a id="msg2881"></a>

## 3. mx · 22. Okt 2013, 14:38

Nur der Vollständigkeit halber, auch für den 8051 gibt es einen freien Compiler:
[http://sdcc.sourceforge.net/](https://web.archive.org/web/2012/http://sdcc.sourceforge.net/)

[Permalink](http://bettyhacks.com/forum/index.php?topic=290.msg2881#msg2881)

---

[← Zurück zu Sonstiges](../boards/07-sonstiges.md) · [Gesamtindex](../index.md)
