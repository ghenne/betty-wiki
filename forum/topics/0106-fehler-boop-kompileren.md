---
title: "Fehler - BOOP kompileren"
topic_id: 106
board: "Software"
board_id: 6
posts: 17
first_post: "26. Feb 2008, 16:38"
last_post: "02. Jan 2015, 22:33"
authors: ["4ou", "MrFX", "Telekatz", "asgard", "bingo600", "elrost", "eme", "fred", "gunnar", "pcsquirrel"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=106.0"
---

# Fehler - BOOP kompileren

[← Software](../boards/06-software.md) · Thema 106 · 17 Beiträge · 26. Feb 2008, 16:38 – 02. Jan 2015, 22:33

Beteiligt: 4ou, MrFX, Telekatz, asgard, bingo600, elrost, eme, fred …

---

<a id="msg782"></a>

## 1. pcsquirrel · 26. Feb 2008, 16:38

Hallo,

beim kompilieren von BOOP bin ich folgendes auf Problem gestoßen:

Der Linker meckert an, daß BOOP mit software FP kompiliert ist, die libgcc aber mit hardware FP (siehe Log weiter unten). So wie ich das verstehe würde ich eine libgcc brauchen, die mit software FP kompiliert ist. Leider finde ich keine. Ich verwende WinARM 20060606 von [http://www.siwawi.arubi.uni-kl.de/avr_projects/arm_projects/](https://web.archive.org/web/2012/http://www.siwawi.arubi.uni-kl.de/avr_projects/arm_projects/) habe aber auch schon die 2007er Version, SDK4ARM und noch 2 weiter versucht. Immer mit dem selben Problem.

Ich hoffe mir kann jemand den entscheidenten Tip geben.

Danke, Philipp

SCHNIPP
E:/winarm/bin/arm-elf-ld: ERROR: E:/winarm/lib/gcc/arm-elf/4.1.1/interwork
\libgcc.a(_udivsi3.o) uses hardware FP, whereas boop_rom.elf uses software FP
E:/winarm/bin/arm-elf-ld: failed to merge target specific data of file E:/winarm
/lib/gcc/arm-hitex-elf/4.0.3/interwork\libgcc.a(_udivsi3.o)
E:/winarm/bin/arm-elf-ld: ERROR: E:/winarm/lib/gcc/arm-elf/4.1.1/interwork
\libgcc.a(_divsi3.o) uses hardware FP, whereas boop_rom.elf uses software FP
E:/winarm/bin/arm-elf-ld: failed to merge target specific data of file E:/winarm
/lib/gcc/arm-hitex-elf/4.0.3/interwork\libgcc.a(_divsi3.o)
E:/winarm/bin/arm-elf-ld: ERROR: E:/winarm/lib/gcc/arm-elf/4.1.1/interwork
\libgcc.a(_umodsi3.o) uses hardware FP, whereas boop_rom.elf uses software FP
E:/winarm/bin/arm-elf-ld: failed to merge target specific data of file E:/winarm
/lib/gcc/arm-hitex-elf/4.0.3/interwork\libgcc.a(_umodsi3.o)
SCHNAPP

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg782#msg782)

---

<a id="msg783"></a>

## 2. Telekatz · 26. Feb 2008, 19:19

Hallo,

das Problem hatte ich auch. Lad dir die Linux Tolchain, die im WIKI verlink ist, herunter. Da ist eine passende libgcc drin.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg783#msg783)

---

<a id="msg784"></a>

## 3. pcsquirrel · 26. Feb 2008, 19:53

Danke,

das war der entscheidende Tip. Jetzt geht´s

pcsquirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg784#msg784)

---

<a id="msg819"></a>

## 4. fred · 19. Mär 2008, 10:42

Hi you all, (sorry for writing in english. reading German is no problem for me however so if you reply to this post you can stick to German if you like )

I just downloaded the source 'trunk' and tried to make the whole project using winarm.
To get them I used "svn checkout svn://svn.mamalala.org/boop/trunk" as suggested in the wiki pages

When I do a makeall everything seems to work fine up to the linking process.
During this step I also have a problem.

the message is: /WinARM//bin/arm-elf-ld: cannot find -lgcc

what I did
1/ looking for a gcc library but I can't find any in the winarm lib folders
2/ changed -lgcc in the makefile in  -llibgcc
    same error
   the path being used in the makefile is -L/winarm/WinARM//arm-elf/lib/interwork/
3/ there's also a /winarm/lib/gcc/arm-elf/4.1.1/interwork folder
    When I change the path to this one I get the same errors ( hardware\software FP ) as in this post

the questions I have are
 is the -lgcc indeed wrong and should it be libgcc
 should the library path be /winarm/lib/gcc/arm-elf/4.1.1/interwork  instead of /winarm/WinARM//arm-elf/lib/interwork/
 and if so should I also get the libgcc library from the linux library

Are the sources I downloaded the most actual ones or should I get the from somewhere else?

Hopefully you can give me some help to get going..!
thanks
fred

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg819#msg819)

---

<a id="msg820"></a>

## 5. pcsquirrel · 19. Mär 2008, 11:20

Hallo,

kompilierst du unter windows oder linux? du mußt nämlich "Makefile.local.WinARM" oder "Makefile.local.linuxARM" in "Makefile.local" umbenennen.
Darin muss noch der Pfad (ARMBASE) entsprechend angepasset werden.

hier meine als beispiel:

 `###############################################################
#####
##### Makefile.local.WinARM for boop
##### Created in the early morninghours
#####
##### Makefile.local.WinARM V1.0 by alterego - alteregon@gmx.net
#####
###############################################################

###############################################################
#####
##### PATHS (default installation)
#####
##### You can put your path-config into Makefile.local
##### to override these defaults
#####
###############################################################

ARMBASE=D:/Downloads/WinARM-20070505_sfx/WinARM
INCLUDEPATH=$(ARMBASE)/include
#LIBPATH=$(ARMBASE)/arm-elf/lib/interwork
LIBPATH=$(ARMBASE)/lib/gcc/arm-elf/4.1.2/interwork
ARMPATH=$(ARMBASE)/bin
TOOLPREFIX=/arm-elf-

######################## EOF ##################################`

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg820#msg820)

---

<a id="msg821"></a>

## 6. fred · 19. Mär 2008, 18:04

Hi thnx for your reply!

I'm trying to get this done under vista

I did change the settings in the file you suggested and copied that to "makefile.local"

somewhere in the makefile is written that settings in makefile.local is overruling the ones which are default in the makefile
this is working because do I recognize my settings which are listed during the make process.

I will compare the content of your file with mine to see if I can find any strange differences anyway!

[update] *Bingo!!!!
my downloaded makefile.local.winarm was not pointing to LIBPATH=$(ARMBASE)/lib/gcc/arm-elf/4.1.2/interwork
my makefile was pointing to -lgcc instead of -llibgcc
your file is pointing to 4.1.2  the level of my winarm is 4.1.1

last problem was the same one this topic started with. Got the library from the linux crosschain and now the whole make process ends with exit 0  !!!

Next I have to see what the most easiest way is to get the firmware into Betty..
When that all works I can find out what I want to change*[/update]

*Last Edit : 19. Mär 2008, 20:29 by fred*

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg821#msg821)

---

<a id="msg886"></a>

## 7. eme · 29. Mär 2008, 17:30

Wie kommt man an die libgcc für in der verlinkten Toolchain (endet auf .sh) heran (für Windows)?

Winarm 20060606 spuckt folgendes aus:

c:/WinARM/bin/arm-elf-ld -Os -Tlpc2220_rom.ld -Map boop.map -Os -Lc:/WinARM/arm-elf/lib/interwork -o boop_rom.elf crt.o main.o interrupt/interrupt.o display/display.a keyboard/keyboard.a audio/audio.a infrared/infrared.a serial/serial.o flash/flash.a cc1100/rf.a gui/gui.a timer/timer.a games/games.a adc/adc.a rtc/rtc.a -lgcc
c:/WinARM/bin/arm-elf-ld: cannot find -lgcc
make.exe: *** [boop.elf] Error 1

> Process Exit Code: 2

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg886#msg886)

---

<a id="msg887"></a>

## 8. eme · 29. Mär 2008, 17:35

Habe jetzt noch in Makefile.local durch folgende Zeile ersetzt:

LIBPATH=$(ARMBASE)/lib/gcc/arm-elf/4.1.1/interwork

Wieder ein Fehler:

c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -c -Wall -mthumb-interwork -msoft-float -Ic:/WinARM/include -I../ -I../interrupt/ -I../keyboard/ -I../display/ -I../flash/ -I../cc1100/ -mthumb -o codes.o codes.c
make[1]: *** [codes.o] Error 1
make[1]: Leaving directory `C:/...../boop/infrared'
make.exe: *** [infrared/infrared.a] Error 2

> Process Exit Code: 2

update:

habe jetzt statt make clean einfach mehrmals auf make 'bestanden', viele fehler,  aber jetzt bekomme ich auch den fehler

c:/WinARM/bin/arm-elf-ld: ERROR: c:/WinARM/lib/gcc/arm-elf/4.1.1/interwork\libgcc.a(_dvmd_tls.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:/WinARM/bin/arm-elf-ld: failed to merge target specific data of file c:/WinARM/lib/gcc/arm-elf/4.1.1/interwork\libgcc.a(_dvmd_tls.o)
make.exe: *** [boop.elf] Error 1

> Process Exit Code: 2

*Last Edit : 29. Mär 2008, 17:42 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg887#msg887)

---

<a id="msg888"></a>

## 9. eme · 29. Mär 2008, 17:47

Ah, gemeint war die Datei libgcc.a in

ronetix-gnutools-arm-elf-4.1.1-linux.tar.bz2\ronetix-gnutools-arm-elf-4.1.1-linux.tar\usr\cross\arm-elf\lib\gcc\arm-elf\4.1.1\interwork\

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg888#msg888)

---

<a id="msg891"></a>

## 10. eme · 29. Mär 2008, 19:01

Ich hänge sie mal an, dann spart ihr euch den download der 80mb.

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg891#msg891)

---

<a id="msg1279"></a>

## 11. 4ou · 01. Feb 2009, 19:08

Wer den Zusatzaufwand mit dem 7Z-Format einsparen möchte,
kann die anliegende zip-Datei nutzen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg1279#msg1279)

---

<a id="msg1508"></a>

## 12. MrFX · 04. Nov 2009, 09:08

Moin!

Ich dachte, der ist gesperrt?

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg1508#msg1508)

---

<a id="msg1509"></a>

## 13. asgard · 04. Nov 2009, 13:41

> **Zitat von: MrFX am 04. Nov 2009, 09:08**
>
> Moin!
>
> Ich dachte, der ist gesperrt?
>
> MfG
> MrFX

Dachte ich auch! Er war/ist in der Bannliste...komische Sache...hab ihn jetzt gelöscht!

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg1509#msg1509)

---

<a id="msg2902"></a>

## 14. elrost · 15. Nov 2014, 12:46

Laufe auf die gleichen Probleme. Habe allerdings in meiner Toolchain

LIBPATH = $(ARMBASE)/lib/gcc/arm-elf/4.1.1/interwork

und nicht die 4.1.2 Version. Weiß jemand wo ich die 4.1.2 Lib-Files downloaden/finden kann?

Hat sich erledigt! Die libca.a musste auch ersetzt werden. Im Forum habe ich eine passende libc.a gefunden

*Last Edit : 16. Nov 2014, 13:03 by elrost*

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg2902#msg2902)

---

<a id="msg2903"></a>

## 15. bingo600 · 27. Nov 2014, 11:41

Brauch doch die neue arm launchpad compiler
[https://launchpad.net/gcc-arm-embedded](https://web.archive.org/web/2012/https://launchpad.net/gcc-arm-embedded)

See for new make & linkerfile
[http://bettyhacks.com/forum/index.php?topic=1049.msg2888#msg2888](1049-betty-erstanden-juni-2014-probleme-mit-debian-squeeze-und-to.md#msg2888)

Copy (replace) the files from the archive to boop/trunk , and it will work wit the launchpad compiler

No need for external libs etc

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg2903#msg2903)

---

<a id="msg2912"></a>

## 16. gunnar · 23. Dez 2014, 15:22

Hallo zusammen,

ich habe die Einstellungen für die Toolchain von Launchpad aus dem vorherigen Beitrag eingecheckt und die Bauanleitung im Wiki überarbeitet. Es baut alles gut durch, nur testen kann ich vorerst nicht, da ich meinen Betty Kram noch in irgendeinem der Umzugskartons stehen habe.

Interessant finde ich auch diese Toolchain: [http://crosstool-ng.org/](https://web.archive.org/web/2012/http://crosstool-ng.org/)
Die hat den Vorteil, dass man sie selber kompilieren kann. Z.B. auf dem RaspberryPI ;-)

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg2912#msg2912)

---

<a id="msg2914"></a>

## 17. bingo600 · 02. Jan 2015, 22:33

> **Zitat von: gunnar am 23. Dez 2014, 15:22**
>
> ich habe die Einstellungen für die Toolchain von Launchpad aus dem vorherigen Beitrag eingecheckt

Thanx 

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=106.msg2914#msg2914)

---

## Verwandte Themen

- [Betty erstanden (Juni 2014!!!) - Probleme mit Debian Squeeze und Toolchain](1049-betty-erstanden-juni-2014-probleme-mit-debian-squeeze-und-to.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
