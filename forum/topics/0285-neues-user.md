---
title: "Neues user"
topic_id: 285
board: "Sonstiges"
board_id: 7
posts: 12
first_post: "20. Nov 2012, 22:41"
last_post: "30. Nov 2012, 23:30"
authors: ["bingo600", "ocalex", "swausd"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=285.0"
---

# Neues user

[← Sonstiges](../boards/07-sonstiges.md) · Thema 285 · 12 Beiträge · 20. Nov 2012, 22:41 – 30. Nov 2012, 23:30

Beteiligt: bingo600, ocalex, swausd

---

<a id="msg2061"></a>

## 1. bingo600 · 20. Nov 2012, 22:41

Hallo forum

Ich komme von Dänemark, und meiner schule deutch sind nicht gut 

Ich habe gestern einer 1-pack Bettys bestellt von asgard , und warte die ankunft nach Dänemark.
Hoffentlich im 8..10 tages zeit.

Ich habe die Boop trunk angepasst zum die neue Codesourcery arm-none-eabi toolchain.
Aber habe kein hw zum testen am 

Sind die forum interssiert im die änderungen ?

mfg
Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2061#msg2061)

---

<a id="msg2063"></a>

## 2. ocalex · 21. Nov 2012, 16:37

Ich denke es ist besser, wenn du in englisch schreibst...

I think its better to write in english... If you can.

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2063#msg2063)

---

<a id="msg2064"></a>

## 3. bingo600 · 21. Nov 2012, 17:41

That would be great to write in english.

I can read german quite ok , but writing is not good (i know) 
Well i only had it for 2 years in school.

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2064#msg2064)

---

<a id="msg2065"></a>

## 4. ocalex · 22. Nov 2012, 00:02

German is not so easy, i know... but for two years it wasnt bad. I had french for four years and can't speak any word... Back to topic, you've checked out the trunk build and adapted it to the arm-none-eabi toolchain, right? I'm sorry, but I can't help with hardware to test thad, because i've also ordered an betty-pack from asgard a few days ago and i'm an absolute newbie in the betty (and ARM) topic... But I hope somebody can help you..

alex

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2065#msg2065)

---

<a id="msg2067"></a>

## 5. bingo600 · 22. Nov 2012, 17:35

I'll just wait for the 16 units to arrive.

But it seems like you'd need to  get an old 4.11 toolchain if you want to use the "stock" makefiles.
I'd like to see if i can use either Codesourcery or the one from launchpad.
[https://launchpad.net/gcc-arm-embedded](https://web.archive.org/web/2012/https://launchpad.net/gcc-arm-embedded)

I have several Jtags , including "Raw" FTDI-FT2232H's

I'm 90% linux based (Boot windows maybe every 2'nd week) , so i face some challenges .. Especially in the debugging area.

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2067#msg2067)

---

<a id="msg2070"></a>

## 6. bingo600 · 22. Nov 2012, 17:48

A FTDI Unit supported by OOCD
[http://www.exp-tech.de/Hacking---Measurement/FT2232H-USB-2-0-Hi-Speed-breakout-board.html](https://web.archive.org/web/2012/http://www.exp-tech.de/Hacking---Measurement/FT2232H-USB-2-0-Hi-Speed-breakout-board.html)

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2070#msg2070)

---

<a id="msg2076"></a>

## 7. bingo600 · 28. Nov 2012, 17:23

Update ...

Got my Bettys today - Thnx asgaard

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2076#msg2076)

---

<a id="msg2078"></a>

## 8. bingo600 · 28. Nov 2012, 21:51

I have succeded in compiling the boop/trunk under Linux (Ubuntu 10.04)

I didn't succed in using Codesourcery Lite , maybe because it hasn't got any interwork libraries.

So i used the suggested Ronetix Toolchain from here
[http://download.ronetix.info/toolchains/arm/ronetix-gnutools-arm-elf-4.1.1-linux.tar.bz2](https://web.archive.org/web/2012/http://download.ronetix.info/toolchains/arm/ronetix-gnutools-arm-elf-4.1.1-linux.tar.bz2)

Extract the above toolchain somewhere.

I had to modify a bit in the makefile , so copy the Makefile.local from the makefiles-trunk.zip into the boop/trunkdir.

Adapt the below line in the Makefile.local , po point at where the armlelf directory of the toolchain is
ARMBASE = ${HOME}/arm/arm-gcc/arm-elf

Do a : make clean all

Connect your 3v3 serialadapter to the Betty (I had to cross the RX & TX lines)
Put your Betty in bootloader mode (I do it manually)

1: Connect Bootloader-pin to Gnd
2: Connect Reset-Pin to Gnd
3: Disconnect Reset-Pin from Gnd
4: Disconnect Bootloader-pin from Gnd

First now ... Start the lpctool program

lpctool -d /dev/ttyUSB0 -i -v -e -a boop_rom.bin

And away you go .....

After the Upload , connect/disconnrct reset to Gnd , and Betty shows.

Hope it helps a bit

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2078#msg2078)

---

<a id="msg2079"></a>

## 9. bingo600 · 28. Nov 2012, 21:52

More files

Including a working firmware , made today

Ohh the lpctool binary is build under Ubuntu 10.04 32-bit

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2079#msg2079)

---

<a id="msg2083"></a>

## 10. bingo600 · 30. Nov 2012, 17:48

I succeded in getting Codesourcery to compile also

I added -nostartfiles and -mthumb-interwork

LDFLAGS = -mthumb-interwork -nostartfiles -Xlinker -Map -Xlinker boop.map -Tlpc2220_rom.ld

And added a section to the linkerfile

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2083#msg2083)

---

<a id="msg2084"></a>

## 11. swausd · 30. Nov 2012, 18:36

Hi Bingo600,

I am using the current Yagarto-Environment and I am quite happy with it. On this forum [http://www.mikrocontroller.net/topic/274543?goto=2939314#2939314](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/274543?goto=2939314#2939314) is a discussion to implement a little OS, so Betty can be used as an ARM learning platform. May be this ist interessting for your too. Just go to the end of the thread and work your way back to ignore the "noise".

Nochmal in Klartext, damit es jeder verstehen kann:
ich benutze die aktuelle Yagarto Umgebung und bin damit ganz zufrieden. In diesem Forum [http://www.mikrocontroller.net/topic/274543?goto=2939314#2939314](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/274543?goto=2939314#2939314) läuft eine Diskussion, um der Betty ein kleines OS zu verpassen, damit sie als ARM Lehr- bzw. Lernplattform benutzt werden kann. Am Besten hinten im Thread anfangen, um dem Rauschen zu entgehen ;-)

Greetings

Siegfried

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2084#msg2084)

---

<a id="msg2085"></a>

## 12. bingo600 · 30. Nov 2012, 23:30

Hi Siegfried

Thanx , but i know that url WS pointed me to it here 

[http://www.mikrocontroller.net/topic/278675#2938127](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/278675#2938127)

I actually got the Bettys as a remote to my upcomming homeautomation , where i use RFM12 433Mhz radios. The Bettys are perfect as user interface & displayunits.

Now i need some guidance in the Menu system & in the CC1100 to RFM12 communication.

/Bingo

*Last Edit : 01. Dez 2012, 00:50 by bingo600*

[Permalink](http://bettyhacks.com/forum/index.php?topic=285.msg2085#msg2085)

---

[← Zurück zu Sonstiges](../boards/07-sonstiges.md) · [Gesamtindex](../index.md)
