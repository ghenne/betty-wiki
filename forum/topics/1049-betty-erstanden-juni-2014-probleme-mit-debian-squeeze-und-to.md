---
title: "Betty erstanden (Juni 2014!!!) - Probleme mit Debian Squeeze und Toolchain"
topic_id: 1049
board: "Software"
board_id: 6
posts: 7
first_post: "03. Jun 2014, 06:59"
last_post: "10. Jun 2014, 15:52"
authors: ["balou1974", "bingo600"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=1049.0"
---

# Betty erstanden (Juni 2014!!!) - Probleme mit Debian Squeeze und Toolchain

[← Software](../boards/06-software.md) · Thema 1049 · 7 Beiträge · 03. Jun 2014, 06:59 – 10. Jun 2014, 15:52

Beteiligt: balou1974, bingo600

---

<a id="msg2887"></a>

## 1. balou1974 · 03. Jun 2014, 06:59

Hallo,

ich habe tatsächlich noch eine Betty erstanden, allerdings ohne TAE- und Scart-Adapter. Ich habe versucht "BOOP" zu bauen aus den Sourcen (aktuelles Repository) aber leider habe ich keine passende aktuelle Toolchain gefunden. Bei CodeSourcery (Mentor) bekommt man leider nicht alle Toolchain zu sehen und die zuerst aufgeführeten Tools bekomme ich nicht installiert ... Allerdings habe ich nach etwas suchen im Forum diese Toolchain entdeckt [https://launchpad.net/gcc-arm-embedded](https://web.archive.org/web/2012/https://launchpad.net/gcc-arm-embedded) . Verwendet die Jemand und was muss noch angepasst werden?

Gruss Balou

*Last Edit : 05. Jun 2014, 05:57 by balou1974*

[Permalink](http://bettyhacks.com/forum/index.php?topic=1049.msg2887#msg2887)

---

<a id="msg2888"></a>

## 2. bingo600 · 03. Jun 2014, 21:05

Seems like he's switched to summon

From the "repos"
boop    2013-04-16    gunnarhenne    [r57] Anpassung an summon ARM toolchain

Trunk
svn checkout svn://svn.code.sf.net/p/boopfirmware/code/ boopfirmware-code

I just compiled the trunk with the attached Makefile & linker-file.

I used this "arm launchpad" compiler , a newer one might also work
gcc version 4.7.4 20130913 (release) [ARM/embedded-4_7-branch revision 202601] (GNU Tools for ARM Embedded Processors)

It's strange that the makefile creator keeps using ld for linking and not gcc
That is NOT the recommended way , and that's why he has to specify those libraries manually.

I have corrected to use gcc as linker

Have fun

Ps: You have to adapt this line in the makefile , to point on there you have installed the arm-gcc toolchain
ARMBASE = $(HOME)/arm/arm-gcc/arm-gcc/

/Bingo
Dänemark"

[Permalink](http://bettyhacks.com/forum/index.php?topic=1049.msg2888#msg2888)

---

<a id="msg2889"></a>

## 3. bingo600 · 03. Jun 2014, 21:18

Ohh

I haven't loaded the firmware , just checkked that it could/would build

/Bingo

My old makefiles were here
[http://bettyhacks.com/forum/index.php?topic=289.msg2099#msg2099](0289-compilerfehler.md#msg2099)

Diffs against svn is in diff.txt

*Last Edit : 03. Jun 2014, 21:21 by bingo600*

[Permalink](http://bettyhacks.com/forum/index.php?topic=1049.msg2889#msg2889)

---

<a id="msg2891"></a>

## 4. balou1974 · 03. Jun 2014, 22:32

Thanks! I will try again with your mentioned thoughts

[Permalink](http://bettyhacks.com/forum/index.php?topic=1049.msg2891#msg2891)

---

<a id="msg2892"></a>

## 5. balou1974 · 04. Jun 2014, 22:24

Hello bingo600!!!

I downloaded the launchpad-toolchain modified your makefile for my needs (other path) and the firmware was build without error!!!
Hopefully it will work when I try it using betty

regards and lot of thanks!!!!

Ps. I will report if it is working fine

[Permalink](http://bettyhacks.com/forum/index.php?topic=1049.msg2892#msg2892)

---

<a id="msg2893"></a>

## 6. balou1974 · 05. Jun 2014, 05:56

@bingo600: Thanks a lot!!!!

My first try did not work because I am having the SWISSCOM-variant, I had to uncomment the SWISSCOM define in keyboard/keyboard.h but after doing that and make clean all followed by make, everything worked out fine!

regards balou

[Permalink](http://bettyhacks.com/forum/index.php?topic=1049.msg2893#msg2893)

---

<a id="msg2894"></a>

## 7. bingo600 · 10. Jun 2014, 15:52

Nice to hear that it works 

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=1049.msg2894#msg2894)

---

## Verwandte Themen

- [Compilerfehler](0289-compilerfehler.md)
- [Fehler - BOOP kompileren](0106-fehler-boop-kompileren.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
