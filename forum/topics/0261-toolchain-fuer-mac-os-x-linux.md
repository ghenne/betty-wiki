---
title: "Toolchain für Mac OS X / Linux"
topic_id: 261
board: "Software"
board_id: 6
posts: 16
first_post: "13. Mär 2011, 09:57"
last_post: "20. Mär 2011, 21:12"
authors: ["Televio", "gunnar", "temp12", "thinkJD", "tugstugi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=261.0"
---

# Toolchain für Mac OS X / Linux

[← Software](../boards/06-software.md) · Thema 261 · 16 Beiträge · 13. Mär 2011, 09:57 – 20. Mär 2011, 21:12

Beteiligt: Televio, gunnar, temp12, thinkJD, tugstugi

---

<a id="msg1887"></a>

## 1. Televio · 13. Mär 2011, 09:57

Hi,

ich suche eine Toolchain mit der ich Boop unter Mac OS X compilieren kann. Ich bin für jeden Hinweis dankbar. Oder vielleicht gibt es ja auch ein Script das eine passende Toolchain z.B. für Linux baut. Das könnte ich dann an OSX anpassen. Auf der Bettyhacks Wikiseite zum Thema konnte ich leider keinen Link auf ein passendes Toolchian buildscript finden.

Gruss,
Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1887#msg1887)

---

<a id="msg1888"></a>

## 2. tugstugi · 13. Mär 2011, 22:31

Hi Andreas,

probiere mal [http://dl.dropbox.com/u/16982795/arm-toolchain-macosx-softfloat.tar.bz2](https://web.archive.org/web/2012/http://dl.dropbox.com/u/16982795/arm-toolchain-macosx-softfloat.tar.bz2)
Das habe ich mir selber durchgebaut und benutze unter MacOS ohne Probleme. Wenn du die Toolchain selber durchbauen willst, dann kannst du dieses Skript benutzen: [https://github.com/danderson/nxos/blob/master/scripts/build_arm_toolchain.sh](https://web.archive.org/web/2012/https://github.com/danderson/nxos/blob/master/scripts/build_arm_toolchain.sh)

Gruß
tugstugi

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1888#msg1888)

---

<a id="msg1889"></a>

## 3. Televio · 14. Mär 2011, 21:04

Danke für den Link und die Toolchain. Funktioniert einwandfrei.

Gruß,
Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1889#msg1889)

---

<a id="msg1892"></a>

## 4. thinkJD · 17. Mär 2011, 14:50

Klasse :-)
Jetzt fehlt nur noch ein lauffähiges LPC-Tool und ich wäre glücklich.
Hast du so etwas am start oder einen Patch, der das Port Problem unter OSX behebt?

Ich bin auch gerade dabei mich intensiv mit der Betty auseinander zu setzen.
Sie funkt mittlerweile auch zuverlässig mit dem RFM12 von Hope RF :-)

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1892#msg1892)

---

<a id="msg1894"></a>

## 5. tugstugi · 17. Mär 2011, 22:29

> **Zitat von: thinkJD am 17. Mär 2011, 14:50**
>
> Klasse :-)
> Jetzt fehlt nur noch ein lauffähiges LPC-Tool und ich wäre glücklich.
> Hast du so etwas am start oder einen Patch, der das Port Problem unter OSX behebt?
>
> Ich bin auch gerade dabei mich intensiv mit der Betty auseinander zu setzen.
> Sie funkt mittlerweile auch zuverlässig mit dem RFM12 von Hope RF :-)

Was meinst du mit einem lauffähiges LPC-Tool? Ich habe das LPC-Tool unter Mac selber durchgebaut und es funktioniert. Das Port-Problem ist einbischen ätzend man muss halt jedes mal den USB-Stecker rausziehen und reinstecken wenn man was hochladen will.

Ich habe auch gerade vor ein Paar Tagen rfm12 modul aufgebaut aber noch nocht geschaft mit Betty zu kommunizieren. Kannst du eventuell deinen Kode teilen?

Gruß
tugstugi

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1894#msg1894)

---

<a id="msg1895"></a>

## 6. gunnar · 18. Mär 2011, 09:32

Hallo tugstugi,

> **Zitat von: thinkJD am 17. Mär 2011, 14:50**
>
> Ich bin auch gerade dabei mich intensiv mit der Betty auseinander zu setzen.
> Sie funkt mittlerweile auch zuverlässig mit dem RFM12 von Hope RF :-)

Wie hast Du die Betty mit dem RFM12 verbunden? Meinst Du damit, dass Du ein RFM12 Modul an die Ports der Betty angeschlossen hast? Oder meinst Du, dass Du den CC1100 in der Betty so konfiguriert hast, dass Du mit einem RFM12 Modul, dass an einen anderen Controller angeschlossen ist kommunizieren kannst?

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1895#msg1895)

---

<a id="msg1896"></a>

## 7. thinkJD · 18. Mär 2011, 10:34

Letzteres :-)

Klar teile ich meinen Code, ich muss ds nur noch ein wenig aufbereiten.
Ist aber gar kein Problem. Der CC1100 kann das von haus aus. Man muss nur die Frequenz und das Syncword entsprechend einstellen. Der RFM12 erkennt das Syncword (0x2DD4) und schiebt brav die Daten aus dem FiFo :-)

Mal ne dumme Frage, ich habe die Toolchain ausgepackt, das Makefile angepasst aber der Compiler meckert immer noch. Fehlen da die Libs? Falls ja, wo bekomme ich die her?

Gruß JD

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1896#msg1896)

---

<a id="msg1897"></a>

## 8. thinkJD · 18. Mär 2011, 11:05

Er findet wohl die libmpc.2.dylib nicht. War das bei euch auch der Fall?

sed -n '4p' .svn/entries >> version.h
/opt/arm/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float -I/opt/arm/include -I. -Iinterrupt -Idisplay -Ikeyboard -Iaudio -Iinfrared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Os -c -MMD -MF ./.deps/main.o -o main.o main.c
dyld: Library not loaded: /opt/local/lib/libmpc.2.dylib
  Referenced from: /opt/arm/bin/../libexec/gcc/arm-elf/4.5.2/cc1
  Reason: image not found
arm-elf-gcc: Internal error: Trace/BPT trap (program cc1)

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1897#msg1897)

---

<a id="msg1898"></a>

## 9. tugstugi · 18. Mär 2011, 11:13

> **Zitat von: thinkJD am 18. Mär 2011, 11:05**
>
> Er findet wohl die libmpc.2.dylib nicht. War das bei euch auch der Fall?
>
>
> sed -n '4p' .svn/entries >> version.h
> /opt/arm/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float -I/opt/arm/include -I. -Iinterrupt -Idisplay -Ikeyboard -Iaudio -Iinfrared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Os -c -MMD -MF ./.deps/main.o -o main.o main.c
> dyld: Library not loaded: /opt/local/lib/libmpc.2.dylib
>   Referenced from: /opt/arm/bin/../libexec/gcc/arm-elf/4.5.2/cc1
>   Reason: image not found
> arm-elf-gcc: Internal error: Trace/BPT trap (program cc1)

Beim Builden habe ich gegen Macports gebaut, da ich gcc 4.5 benutzen wollte. Daher musst du zuerst Macports installieren und dann die fehlende Libs (oder einfach gcc45 installieren dann sind alle benötigte Libs mitinstalliert).

Gruß
tugstugi

PS: @thinkJD: Bist du das?: [http://www.mikrocontroller.net/topic/194471](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/194471)

*Last Edit : 18. Mär 2011, 11:16 by tugstugi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1898#msg1898)

---

<a id="msg1899"></a>

## 10. thinkJD · 18. Mär 2011, 11:16

Cool, danke für die Info.

Jop, der thinkJD in dem Thread. Ich habe ein bissel gekämpft, bis die Timings soweit waren, dann lief alles. Kopier dir mal den Code, schalte das Data Whitening aus und ab geht's.

P.S.
Nicht das es zu Missverständnissen kommt, ich habe das nicht alles selbst gemacht. Das meiste kommt von Oldies dem Threadstarter.

*Last Edit : 18. Mär 2011, 11:30 by thinkJD*

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1899#msg1899)

---

<a id="msg1900"></a>

## 11. thinkJD · 18. Mär 2011, 21:16

Hm jetzt fehlt noch eine lib ..

infrared/ir_sirc.thumbunopt.o infrared/ir_spaceenc.thumbunopt.o infrared/ir_lirc.thumbunopt.o -lc -lgcc
/opt/arm/bin/arm-elf-ld: cannot find -lc

ist das die glibc?
Das ist gar nicht so einfach, wenn man Visual Studio gewohnt ist :-)

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1900#msg1900)

---

<a id="msg1901"></a>

## 12. temp12 · 18. Mär 2011, 21:21

> **Zitat von: thinkJD am 18. Mär 2011, 21:16**
>
> Hm jetzt fehlt noch eine lib ..
>
> infrared/ir_sirc.thumbunopt.o infrared/ir_spaceenc.thumbunopt.o infrared/ir_lirc.thumbunopt.o -lc -lgcc
> /opt/arm/bin/arm-elf-ld: cannot find -lc
>
> ist das die glibc?
> Das ist gar nicht so einfach, wenn man Visual Studio gewohnt ist :-)

Ja, das ist libc. Es liegt unter $(ARMBASE)/arm-elf/lib/interwork

Das musst du halt in deiner Makefile includieren.

Gruß
tugstugi

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1901#msg1901)

---

<a id="msg1902"></a>

## 13. thinkJD · 18. Mär 2011, 21:49

THX!
Hatte den Pfad falsch gesetzt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1902#msg1902)

---

<a id="msg1903"></a>

## 14. thinkJD · 20. Mär 2011, 15:33

Gnah!
Kaum kann ich boop kompilieren, bahnt sich auch schon das nächste Problem an.
Beim bauen des LPCTools bekomme ich folgende Fehlermeldung:

/opt/arm/binarm-elf-as -mcpu=arm7tdmi-s -D --gstabs -mthumb-interwork -mfpu=softfpa -o crt.o crt.s
make: /opt/arm/binarm-elf-as: No such file or directory
make: *** [crt.o] Error 1

Was fehlt da noch? Ist meine Toolchain noch nicht komplett?
Gruß JD

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1903#msg1903)

---

<a id="msg1904"></a>

## 15. tugstugi · 20. Mär 2011, 16:43

> **Zitat von: thinkJD am 20. Mär 2011, 15:33**
>
> Gnah!
> Kaum kann ich boop kompilieren, bahnt sich auch schon das nächste Problem an.
> Beim bauen des LPCTools bekomme ich folgende Fehlermeldung:
>
>
> /opt/arm/binarm-elf-as -mcpu=arm7tdmi-s -D --gstabs -mthumb-interwork -mfpu=softfpa -o crt.o crt.s
> make: /opt/arm/binarm-elf-as: No such file or directory
> make: *** [crt.o] Error 1
>
>
> Was fehlt da noch? Ist meine Toolchain noch nicht komplett?
> Gruß JD

Nein, da fehlt nur ein /. Guck deine Makefile wieder an.

tugstugi

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1904#msg1904)

---

<a id="msg1905"></a>

## 16. thinkJD · 20. Mär 2011, 21:12

Meine Güte ich muss echt Tomaten auf den Augen haben.
Danke jetzt klappt alles :-)

[Permalink](http://bettyhacks.com/forum/index.php?topic=261.msg1905#msg1905)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
