---
title: "Scart problems."
topic_id: 268
board: "Software"
board_id: 6
posts: 2
first_post: "23. Juni 2011, 19:23"
last_post: ""
authors: ["jannis", "rekordc"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=268.0"
---

# Scart problems.

[← Software](../boards/06-software.md) · Thema 268 · 2 Beiträge · 23. Juni 2011, 19:23 – 

Beteiligt: jannis, rekordc

---

<a id="msg1935"></a>

## 1. rekordc · 23. Juni 2011, 19:23

Hi,

got a problem with connecting scart <-> pc.

Adapter is programmed, led is blinking with every key press on the remote.
OS is linux, serial is /dev/ttyUSB0
With windows on the same PC I could programm the betty's with betty heaven so the USB->serial is working.

Mpdtools gives connections errors. Normal firmware also don't give any output.

I've connect the RX (square hole) of the scart adapter to pin 2 of a db9 connector, TX to pin 3 and gnd to pin 5.

Must the RX of the scart adapter be connected with the RX or TX of the PC? Right now I've RX - RX and TX - TX. But nothing on the terminal screen.

What am I doing wrong.

[Permalink](http://bettyhacks.com/forum/index.php?topic=268.msg1935#msg1935)

---

<a id="msg1936"></a>

## 2. jannis · 

tx transmitter -> rx receiver

[Permalink](http://bettyhacks.com/forum/index.php?topic=268.msg1936#msg1936)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
