---
title: "Boop Kompilieren unter winarm"
topic_id: 295
board: "Software"
board_id: 6
posts: 4
first_post: "19. Mai 2013, 09:56"
last_post: "21. Mai 2013, 09:57"
authors: ["gunnar", "wollywell"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=295.0"
---

# Boop Kompilieren unter winarm

[← Software](../boards/06-software.md) · Thema 295 · 4 Beiträge · 19. Mai 2013, 09:56 – 21. Mai 2013, 09:57

Beteiligt: gunnar, wollywell

---

<a id="msg2119"></a>

## 1. wollywell · 19. Mai 2013, 09:56

Hallo,

ich habe wie angegeben winarm Version 20060606 nach c:\winarm entpackt.
auch die libgcc.a ersetzt.

im makefile ist folgendes
...
ARMBASE = /opt/summon-arm-toolchain
INCLUDEPATH = $(ARMBASE)/include
LIBGCCPATH = $(ARMBASE)/lib/gcc/arm-none-eabi/4.7.3/thumb/arm7tdmi-s
LIBCPATH = $(ARMBASE)/arm-none-eabi/lib/thumb/arm7tdmi-s
ARMPATH = $(ARMBASE)/bin
TOOLPREFIX = arm-none-eabi-
LPCTOOL = lpctool
OPENOCD = openocd -f betty.cfg -f interface/parport.cfg
...
die zeilen LIBGCCPATH und LIBCPATH existieren gar nicht und werden in makefile.local (.winarm) nicht ersetzt

habe folgende Fehlermeldungen:

> "make.exe" all
echo -n '#define SVNVERSION 0' > version.h
svnversion -n |cut -f1 -d M -n >> version.h
/usr/bin/sh: svnversion: command not found
echo >> version.h
mkdir -p .deps
mkdir -p adc/.deps
mkdir -p audio/.deps
mkdir -p cc1100/.deps
mkdir -p display/.deps
mkdir -p flash/.deps
mkdir -p games/.deps
mkdir -p gui/.deps
mkdir -p infrared/.deps
mkdir -p interrupt/.deps
mkdir -p keyboard/.deps
mkdir -p rtc/.deps
mkdir -p serial/.deps
mkdir -p timer/.deps
mkdir -p tools/.deps
c:/WinARM/bin/arm-elf-as -mcpu=arm7tdmi-s -D --gstabs -mthumb-interwork -mfpu=softfpa -o crt.o crt.s
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Iaudio -Iinfrared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Os -c -MMD -MF ./.deps/main.o -o main.o main.c
...
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Iaudio -Iinfrared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -mthumb -c -MMD -MF infrared/.deps/ir_lirc.thumbunopt.o -o infrared/ir_lirc.thumbunopt.o infrared/ir_lirc.c
c:/WinARM/bin/arm-elf-ld -Tlpc2220_rom.ld -Map boop.map -Lc:/WinARM/lib/gcc/arm-none-eabi/4.7.3/thumb/arm7tdmi-s -Lc:/WinARM/arm-none-eabi/lib/thumb/arm7tdmi-s -o boop_rom.elf crt.o main.o global.o buffer.o syscalls.o audio/soundirq.o infrared/infraredirq.o interrupt/irq.o keyboard/keyirq.o serial/serirq.o timer/timerirq.o adc/adc.thumb.o adc/adcirq.thumb.o audio/sound.thumb.o audio/sid.thumb.o cc1100/cc1100.thumb.o cc1100/rf.thumb.o cc1100/fs20.thumb.o display/lcd.thumb.o display/fonty.thumb.o display/drawDigit.thumb.o display/drawIcon.thumb.o display/backlight.thumb.o flash/flash.thumb.o flash/bfs.thumb.o games/gamesmenu.thumb.o games/tic_tac_toe.thumb.o games/sokoban.thumb.o games/connect4.thumb.o gui/menu.thumb.o gui/mainmenu.thumb.o gui/testmenu.thumb.o gui/settingsmenu.thumb.o gui/controls.thumb.o infrared/infrared.thumb.o infrared/codes.thumb.o infrared/encoders.thumb.o infrared/ir_capture.thumb.o infrared/ir_selector.thumb.o keyboard/keyboard.thumb.o rtc/rtc.thumb.o rtc/i2c.thumb.o rtc/rtctimer.thumb.o serial/serial.thumb.o serial/redirector.thumb.o timer/timerfuncs.thumb.o tools/toolsmenu.thumb.o tools/scart_icp.thumb.o infrared/ir_itt.thumbunopt.o infrared/ir_nrc17.thumbunopt.o infrared/ir_raw.thumbunopt.o infrared/ir_rc5.thumbunopt.o infrared/ir_rc6.thumbunopt.o infrared/ir_rca.thumbunopt.o infrared/ir_rcmm.thumbunopt.o infrared/ir_rec80.thumbunopt.o infrared/ir_recs80.thumbunopt.o infrared/ir_rf.thumbunopt.o infrared/ir_sirc.thumbunopt.o infrared/ir_spaceenc.thumbunopt.o infrared/ir_lirc.thumbunopt.o -lc -libgcc.a
c:/WinARM/bin/arm-elf-ld: cannot find -lgcc
make.exe: *** [boop_rom.elf] Error 1

> Process Exit Code: 2
> Time Taken: 00:06

Kann mir bitte jemand sagen wie ich das hinkriege?
an der geänderten Keyboard.h kanns nicht liegen , oder? hab da das #define SWISSCOM verwendet da ich eine solche habe.

Danke,

Thomas

[Permalink](http://bettyhacks.com/forum/index.php?topic=295.msg2119#msg2119)

---

<a id="msg2120"></a>

## 2. gunnar · 20. Mai 2013, 11:57

Hallo Thomas,

geh mal im svn zurück auf die Revision bevor ich die Anpassungen an die aktuellere Toolchain gemacht habe.
Ich habe es gerade selber mit der aktuellen Toolchain von CodeSourcery unter Windows probiert, aber da kommt beim Linken dieser Fehler:

C:/Programme/CodeSourcery/Sourcery_CodeBench_Lite_for_ARM_EABI/lib/gcc/arm-none-eabi/4.7.3/thumb\libgcc.a(_divdi3.o).ARM.exidx+0x0): relocation truncated to fit: R_ARM_PREL31 against `.text'

C:/Programme/CodeSourcery/Sourcery_CodeBench_Lite_for_ARM_EABI/lib/gcc/arm-none-eabi/4.7.3/thumb\libgcc.a(_udivdi3.o).ARM.exidx+0x0): relocation truncated to fit: R_ARM_PREL31 against `.text'

Du kannst auch mal versuchen, den LIBGCCPATH in Makefile.local auf den Pfad anzupassen, wo die libgcc.a Deiner Toolchain liegt. Es gibt da oft mehrere Versionen, eine die etwas mit Thumb und evtl. Interwork zu tun hat, sollte die richtige sein.
Wenn es baut, dann schick mir bitte Dein Makefile.local.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=295.msg2120#msg2120)

---

<a id="msg2121"></a>

## 3. wollywell · 21. Mai 2013, 09:06

hi.

habs mit revision 55 probiert, dann kommt zwar der fehler oben nicht mehr, allerdings findet er dann den svn.entries eintrag nicht und beim versuch zuvor kam irgendwas mit libc.a uses FP....

solangsam nervt es mich*grummel*
hat niemand eine funktionierende winarm/boop kombination für mich?
Biiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiittttttttttttttttttttttttttäääääääääääääääääääääääääääääää  :'(

[Permalink](http://bettyhacks.com/forum/index.php?topic=295.msg2121#msg2121)

---

<a id="msg2122"></a>

## 4. wollywell · 21. Mai 2013, 09:57

Juhuuuuuuu
habs hinbekommen
hab in der makefile datei in der zeile wo die version.h erzeugt wird das -n gelöscht und hinter #define SVNVERSION ne 1 gesetzt
dann kam das mit libc.a uses hardware FP und hab die libc.a ersetzt mit der aus [http://bettyhacks.com/forum/index.php?topic=227.msg1558#msg1558](0227-undefined-reference-to-strncpy-strncat-strnlen.md#msg1558)
nun kompiliert er ohne fehler.           

hat noch jemand ne Swisscom betty?
meine springt im menu beim hoch oder runter drücken manchmal direkt bis zum Anfang/ende der menuliste anstatt ein feld Runter/hoch 
liegt das an meiner betty? das da nicht immer die taste ordentlich gedrückt wird? oder eventuell noch ne andere tastenbelegung?

thomas

[Permalink](http://bettyhacks.com/forum/index.php?topic=295.msg2122#msg2122)

---

## Verwandte Themen

- [undefined reference to 'strncpy'/'strncat'/'strnlen'](0227-undefined-reference-to-strncpy-strncat-strnlen.md)
- [Probleme beim kompilieren mit WinARM unter Windows 7 x64](1046-probleme-beim-kompilieren-mit-winarm-unter-windows-7-x64.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
