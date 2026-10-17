---
title: "Possible wrong define in  cc1100/rf.h"
topic_id: 1057
board: "Software"
board_id: 6
posts: 1
first_post: "09. Mär 2017, 22:16"
last_post: "09. Mär 2017, 22:16"
authors: ["bingo600"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=1057.0"
---

# Possible wrong define in  cc1100/rf.h

[← Software](../boards/06-software.md) · Thema 1057 · 1 Beiträge · 09. Mär 2017, 22:16 – 09. Mär 2017, 22:16

Beteiligt: bingo600

---

<a id="msg2921"></a>

## 1. bingo600 · 09. Mär 2017, 22:16

[http://www.ewetel.net/~horst.raap/](https://web.archive.org/web/2012/http://www.ewetel.net/~horst.raap/)
[https://github.com/HerrSchrader/McBetty](https://web.archive.org/web/2012/https://github.com/HerrSchrader/McBetty)

Using : launchpad arm-gcc
gcc version 4.8.4 20140526 (release) [ARM/embedded-4_8-branch revision 211358] (GNU Tools for ARM Embedded Processors)

When compiling McBetty/McBetty/scart_image/boop.orig

I get a linker error
/home/cfo/arm/arm-gcc/gcc-arm-none-eabi-4_8-2014q2/bin/../lib/gcc/arm-none-eabi/4.8.4/../../../../arm-none-eabi/bin/ld: Warning: alignment 1 of symbol `default_RFsettings' in cc1100/rf.thumb.o is smaller than 4 in infrared/ir_rf.thumbunopt.o

I think there is a wrong definiton in  cc1100/rf.h

To solve : In McBetty/McBetty/scart_image/boop.orig/cc1100/rf.h

Change :

const struct RFsettings_ default_RFsettings;

to

extern const struct RFsettings_ default_RFsettings;

The struct is declared and initialized in rf.c , but actually also defined  in the above rf.h

const struct RFsettings_ default_RFsettings =
{
0x01, //address
0x01 //channel
};

The same error is in the current boop svn (rev 60)

Does that make sense ??

/Bingo

Edit:
Added the makefile & linkerfile used for McBetty (boop.orig) , overwrite the files from svn
Added makefile for 8051 scart_image

*Last Edit : 10. Mär 2017, 19:01 by bingo600*

[Permalink](http://bettyhacks.com/forum/index.php?topic=1057.msg2921#msg2921)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
