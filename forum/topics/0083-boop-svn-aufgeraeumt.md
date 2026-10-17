---
title: "boop svn - aufgeraeumt"
topic_id: 83
board: "Software"
board_id: 6
posts: 2
first_post: "06. Dez 2007, 12:00"
last_post: "15. Jan 2008, 13:12"
authors: ["fred", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=83.0"
---

# boop svn - aufgeraeumt

[← Software](../boards/06-software.md) · Thema 83 · 2 Beiträge · 06. Dez 2007, 12:00 – 15. Jan 2008, 13:12

Beteiligt: fred, netguy

---

<a id="msg608"></a>

## 1. netguy · 06. Dez 2007, 12:00

hallo alle zusammen,

ich habe die codebase fuer boop mal ein wenig aufgeraeumt & strukturiert.

so finden sich nun die einzelnen module (keyboard, infrarot, etc...) nun in eigenen unterordnern.
das interrupt-handling wurde verbessert, es gibt nun keine fehler mehr beim thumb-interworking und optimierten routinen (-Os flag).
den cc1100 code von telekatz habe ich uebernommen und einen kleinen bug darin gefixt: irqslot1 wurde bereits benutzt, liegt nun auf 2.

die fb-auswahl ist erstmal stark minimiert, da ich den entsprechenden auswahl-code vorruebergehend rausgenommen habe.
als naechstes steht die integration von colibris code an, sowie ein brauchbares und schoenes menu system.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=83.msg608#msg608)

---

<a id="msg732"></a>

## 2. fred · 15. Jan 2008, 13:12

Hi Chris

You are pointing to svn://svn.mamalala.org/boop/trunk but when I try to do a checkout it's failing with the message
"No connection could be made because the target machine actively refused it"

I'm using TurtoiseSVN (winxp) for this.

You probably know why....

Can you tell me what to do to get the whole trunk?

greatz
Fred

[Permalink](http://bettyhacks.com/forum/index.php?topic=83.msg732#msg732)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
