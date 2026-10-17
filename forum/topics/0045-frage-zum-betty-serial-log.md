---
title: "Frage zum Betty Serial Log"
topic_id: 45
board: "Software"
board_id: 6
posts: 2
first_post: "04. Sep 2007, 05:47"
last_post: "04. Sep 2007, 18:19"
authors: ["alterego"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=45.0"
---

# Frage zum Betty Serial Log

[← Software](../boards/06-software.md) · Thema 45 · 2 Beiträge · 04. Sep 2007, 05:47 – 04. Sep 2007, 18:19

Beteiligt: alterego

---

<a id="msg293"></a>

## 1. alterego · 04. Sep 2007, 05:47

Hi leute,

die frage richtet sich (denke ich mal) hauptsächlich an die leute die eine aktivierte und für den zweck bestimmte betty am laufen haben.
Ich wollte mal fragen ob bei euch das log u.a. ähnlich dem hier aussieht:

...
w~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
spw~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
spw~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
spw~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
spwLS rem 10s
~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/[1;31m123***[0m
spw~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
spw~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
spw~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
spw~b:+kXlTvn1: ~    0x00000000/00/C0/S1D1/0[0m
...

man beachte die escape-sequenzen und das "spw" und "w~b" prefix sowie das häufige auftreten des zeichens "~"

sieht das bei euch auch so aus? oder ähnlich?

alterego

Nachtrag: generell sieht das log an anderer stelle perfekt aus, download der firmware funktioniert und ist bei 5 von 5 mal identisch... so schliesse ich probleme mit meiner schaltung und sonstigen übertragungsfehlern aus.

*Last Edit : 04. Sep 2007, 06:02 by alterego*

[Permalink](http://bettyhacks.com/forum/index.php?topic=45.msg293#msg293)

---

<a id="msg297"></a>

## 2. alterego · 04. Sep 2007, 18:19

wie mir theborg und netguy eben versichert haben, passt das alles und ist "normal" ebenso die ansi-escape-sequenzen...
thema erledigt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=45.msg297#msg297)

---

## Verwandte Themen

- [Frage zum Simple Serial Interface](0104-frage-zum-simple-serial-interface.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
