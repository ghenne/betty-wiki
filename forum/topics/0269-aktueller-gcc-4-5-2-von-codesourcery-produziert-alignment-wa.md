---
title: "Aktueller GCC 4.5.2 von CodeSourcery produziert Alignment Warnings"
topic_id: 269
board: "Software"
board_id: 6
posts: 4
first_post: "13. Jul 2011, 16:07"
last_post: "16. Apr 2013, 21:41"
authors: ["glotzi", "gunnar"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=269.0"
---

# Aktueller GCC 4.5.2 von CodeSourcery produziert Alignment Warnings

[← Software](../boards/06-software.md) · Thema 269 · 4 Beiträge · 13. Jul 2011, 16:07 – 16. Apr 2013, 21:41

Beteiligt: glotzi, gunnar

---

<a id="msg1939"></a>

## 1. gunnar · 13. Jul 2011, 16:07

Hallo,

ich habe gesehen, dass McBetty mit dem Compiler von CodeSourcery kompiliert wird und wollte diesen ziemlich aktuellen Compiler auch für Boop nehmen. Ihm unterliegt nicht die newlibc sondern die uClibc. Eine kleine Änderung musste ich machen: siprintf in sprintf umbenennen, ansonsten lief es gut durch bis auf etliche Alignment Warnings im Thumb-Code:
 `` /opt/CodeSourcery-arm-uclinux/bin/arm-uclinuxeabi-ld.real: Warning: alignment 1 of symbol `default_RFsettings' in cc1100/rf.thumb.o is smaller than 4 in infrared/ir_rf.thumbunopt.o
/opt/CodeSourcery-arm-uclinux/bin/arm-uclinuxeabi-ld.real: Warning: alignment 1 of symbol `default_RFsettings' in cc1100/rf.thumb.o is smaller than 4 in infrared/ir_lirc.thumbunopt.o
/opt/CodeSourcery-arm-uclinux/bin/arm-uclinuxeabi-ld.real: Warning: alignment 1 of symbol `conf' in cc1100/cc1100.thumb.o is smaller than 4 in infrared/ir_lirc.thumbunopt.o
/opt/CodeSourcery-arm-uclinux/bin/arm-uclinuxeabi-ld.real: Warning: alignment 1 of symbol `confasync' in cc1100/cc1100.thumb.o is smaller than 4 in infrared/ir_lirc.thumbunopt.o ``

Eigentlich ist es doch richtig, dass Thumb Code ein anderes Alignment hat, wieso kommt trotzdem ein Linker Warning?
Oder führt diese Konstellation sogar zu richtigen Fehlern beim Zugriff auf die falsch aligneten Daten? Wahrscheinlich gibt es Probleme wenn der ARM Code darauf zugreift, aber nicht wenn ausschließlich aus dem Thumb Code darauf zugegriffen wird, oder?

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=269.msg1939#msg1939)

---

<a id="msg1953"></a>

## 2. glotzi · 16. Aug 2011, 07:39

Warum nimmst du überhaupt den CodeSourcery Kram? Dieser ganze kommerzielle Kram ist mir zu aufgeblasen und undurchsichtig.

Ich nehme die hier
[https://github.com/esden/summon-arm-toolchain](https://web.archive.org/web/2012/https://github.com/esden/summon-arm-toolchain)

[Permalink](http://bettyhacks.com/forum/index.php?topic=269.msg1953#msg1953)

---

<a id="msg1965"></a>

## 3. gunnar · 04. Nov 2011, 15:05

Hallo Glotzi,

ich habe mal die summon Toolchain ausprobiert. Dazu musste ich eine Dummy Funktion für _setbrk einfügen, sonst linkte es nicht. Die alignment Warnungen kommen aber auch mit dieser Toolchain.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=269.msg1965#msg1965)

---

<a id="msg2117"></a>

## 4. gunnar · 16. Apr 2013, 21:41

Hallo,

ich habe die aktuelle summon Toolchain mit dem GCC 4.7.3 vom Linaro Projekt gebaut. Das Build Script gibt es hier:
[https://github.com/esden/summon-arm-toolchain](https://web.archive.org/web/2012/https://github.com/esden/summon-arm-toolchain)
Ich habe kleine Änderungen für diese Toolchain gemacht, u.A. auch das Alignment fest auf 4 Bytes eingestellt.

Jetzt kommen die Warnungen nicht mehr und das Binary läuft. :-)

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=269.msg2117#msg2117)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
