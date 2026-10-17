---
title: "Compilerfehler"
topic_id: 289
board: "Software"
board_id: 6
posts: 3
first_post: "15. Dez 2012, 10:52"
last_post: "17. Dez 2012, 21:51"
authors: ["Michel", "bingo600"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=289.0"
---

# Compilerfehler

[← Software](../boards/06-software.md) · Thema 289 · 3 Beiträge · 15. Dez 2012, 10:52 – 17. Dez 2012, 21:51

Beteiligt: Michel, bingo600

---

<a id="msg2097"></a>

## 1. Michel · 15. Dez 2012, 10:52

Hallo,

ich habe hier jetzt einiges durchgelesen aber komme nicht wirklich weiter. Ich versuche gerade ein Projekt der Betty zu kompilieren und ahbe alles wie auf der Wiki Seite erklärt runtergeladen , ersetzt und Pfade angepasst. Wenn ich 'Make' ausführen erhalte ich folgende Fehler :
`` c:\WinARM\bin/arm-elf-ld -Tlpc2220_rom.ld -Map boop.map -Lc:\WinARM\arm-elf\lib\interwork -o boop_rom.elf crt.o main.o global.o buffer.o audio/soundir
q.o infrared/infraredirq.o interrupt/irq.o keyboard/keyirq.o serial/serirq.o timer/timerirq.o adc/adc.thumb.o adc/adcirq.thumb.o audio/sound.thumb.o a
udio/sid.thumb.o cc1100/cc1100.thumb.o cc1100/rf.thumb.o cc1100/fs20.thumb.o display/lcd.thumb.o display/fonty.thumb.o display/drawDigit.thumb.o displ
ay/drawIcon.thumb.o display/backlight.thumb.o flash/flash.thumb.o flash/bfs.thumb.o games/gamesmenu.thumb.o games/tic_tac_toe.thumb.o games/sokoban.th
umb.o games/connect4.thumb.o gui/menu.thumb.o gui/mainmenu.thumb.o gui/testmenu.thumb.o gui/settingsmenu.thumb.o gui/controls.thumb.o infrared/infrare
d.thumb.o infrared/codes.thumb.o infrared/encoders.thumb.o infrared/ir_capture.thumb.o infrared/ir_selector.thumb.o keyboard/keyboard.thumb.o rtc/rtc.
thumb.o rtc/i2c.thumb.o rtc/rtctimer.thumb.o serial/serial.thumb.o serial/redirector.thumb.o timer/timerfuncs.thumb.o tools/toolsmenu.thumb.o tools/sc
art_icp.thumb.o moodpxl/moodpxlMenu.thumb.o moodpxl/mpxlRF.thumb.o infrared/ir_itt.thumbunopt.o infrared/ir_nrc17.thumbunopt.o infrared/ir_raw.thumbun
opt.o infrared/ir_rc5.thumbunopt.o infrared/ir_rc6.thumbunopt.o infrared/ir_rca.thumbunopt.o infrared/ir_rcmm.thumbunopt.o infrared/ir_rec80.thumbunop
t.o infrared/ir_recs80.thumbunopt.o infrared/ir_rf.thumbunopt.o infrared/ir_sirc.thumbunopt.o infrared/ir_spaceenc.thumbunopt.o infrared/ir_lirc.thumb
unopt.o -lc -lgcc
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(memset.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(memset.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(siprintf.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(siprintf.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(strcmp.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(strcmp.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(vfiprintf.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(vfiprintf.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(wcrtomb.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(wcrtomb.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(wcsrtombs.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(wcsrtombs.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(wctomb_r.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(wctomb_r.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(wsetup.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(wsetup.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(fflush.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(fflush.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(findfp.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(findfp.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(freer.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(freer.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(fvwrite.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(fvwrite.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(fwalk.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(fwalk.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(impure.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(impure.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(locale.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(locale.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(makebuf.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(makebuf.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(mallocr.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(mallocr.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(memchr.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(memchr.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(memmove.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(memmove.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(mlock.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(mlock.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(reallocr.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(reallocr.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(stdio.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(stdio.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(strlen.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(strlen.o)
c:\WinARM\bin/arm-elf-ld: ERROR: c:\WinARM\arm-elf\lib\interwork\libc.a(fclose.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:\WinARM\bin/arm-elf-ld: failed to merge target specific data of file c:\WinARM\arm-elf\lib\interwork\libc.a(fclose.o)
gui/controls.thumb.o: In function `trackbar_draw':
controls.c:(.text+0x804): relocation truncated to fit: R_ARM_THM_CALL against symbol `_draw_block' defined in .text.fastcode section in display/lcd.th
umb.o
controls.c:(.text+0x83e): relocation truncated to fit: R_ARM_THM_CALL against symbol `_draw_block' defined in .text.fastcode section in display/lcd.th
umb.o
controls.c:(.text+0x8d2): relocation truncated to fit: R_ARM_THM_CALL against symbol `_draw_block' defined in .text.fastcode section in display/lcd.th
umb.o
c:\WinARM\arm-elf\lib\interwork\libc.a(freer.o): In function `_malloc_trim_r':
mallocr.c:(.text+0x48): undefined reference to `_sbrk_r'
mallocr.c:(.text+0x64): undefined reference to `_sbrk_r'
mallocr.c:(.text+0x84): undefined reference to `_sbrk_r'
c:\WinARM\arm-elf\lib\interwork\libc.a(makebuf.o): In function `__smakebuf':
makebuf.c:(.text+0x3c): undefined reference to `_fstat_r'
makebuf.c:(.text+0x110): undefined reference to `isatty'
c:\WinARM\arm-elf\lib\interwork\libc.a(mallocr.o): In function `_malloc_r':
mallocr.c:(.text+0x40c): undefined reference to `_sbrk_r'
mallocr.c:(.text+0x4b4): undefined reference to `_sbrk_r'
c:\WinARM\arm-elf\lib\interwork\libc.a(stdio.o): In function `__sclose':
stdio.c:(.text+0x10): undefined reference to `_close_r'
c:\WinARM\arm-elf\lib\interwork\libc.a(stdio.o): In function `__sseek':
stdio.c:(.text+0x3c): undefined reference to `_lseek_r'
c:\WinARM\arm-elf\lib\interwork\libc.a(stdio.o): In function `__swrite':
stdio.c:(.text+0x94): undefined reference to `_lseek_r'
stdio.c:(.text+0xb8): undefined reference to `_write_r'
c:\WinARM\arm-elf\lib\interwork\libc.a(stdio.o): In function `__sread':
stdio.c:(.text+0xe4): undefined reference to `_read_r'
make: *** [boop_rom.elf] Error 1 ``

mein Makefile.local sieht so aus :
 `###############################################################
#####
##### Makefile.local.WinARM for boop
##### Created in the early morninghours
#####
##### Makefile.local.WinARM V1.0 by alterego - alteregon@gmx.net
#####
##### Copy this file to Makefile.local for your Windows
##### installation
#####
###############################################################

ARMBASE = c:\WinARM
INCLUDEPATH = $(ARMBASE)\include
LIBPATH = $(ARMBASE)\arm-elf\lib\interwork
ARMPATH = $(ARMBASE)\bin
TOOLPREFIX = arm-elf-
LPCTOOL = lpctool.exe
#OPENOCD = C:\OpenOCD\openocd.exe -f betty.cfg -f C:\OpenOCD\OpenOCD\interface\parport.cfg

######################## EOF ##################################`

Merkwürdig war, dass ich keine ligcc.a im Winarm...\lib\interwork Verzeichnis hatte. Ich habe die entsprechende Datei bei
[http://download.ronetix.info/toolchains/arm/](https://web.archive.org/web/2012/http://download.ronetix.info/toolchains/arm/) runtergeladen und reinkopiert.

ich komm hier echt nicht weiter, hat Jemand von euch eine Idee ?
Ich benutze als Betriebssystem Windows 7.

viele Grüße
Michel

[Permalink](http://bettyhacks.com/forum/index.php?topic=289.msg2097#msg2097)

---

<a id="msg2098"></a>

## 2. Michel · 15. Dez 2012, 11:02

aaah ,

habe jetzt doch noch etwas gefunden un zumindest die Software / Hardware Meldungen beseitigt.
Die Lösung stand hier :
[http://bettyhacks.com/forum/index.php?topic=227.msg1558#msg1558](0227-undefined-reference-to-strncpy-strncat-strnlen.md#msg1558)

jetzt meckert er noch hier :
`` echo -n '#define SVNVERSION ' > version.h
c:\WinARM\bin/arm-elf-ld -Tlpc2220_rom.ld -Map boop.map -Lc:\WinARM\arm-elf\lib\interwork -o boop_rom.elf crt.o main.o global.o buffer.o audio/soundir
q.o infrared/infraredirq.o interrupt/irq.o keyboard/keyirq.o serial/serirq.o timer/timerirq.o adc/adc.thumb.o adc/adcirq.thumb.o audio/sound.thumb.o a
udio/sid.thumb.o cc1100/cc1100.thumb.o cc1100/rf.thumb.o cc1100/fs20.thumb.o display/lcd.thumb.o display/fonty.thumb.o display/drawDigit.thumb.o displ
ay/drawIcon.thumb.o display/backlight.thumb.o flash/flash.thumb.o flash/bfs.thumb.o games/gamesmenu.thumb.o games/tic_tac_toe.thumb.o games/sokoban.th
umb.o games/connect4.thumb.o gui/menu.thumb.o gui/mainmenu.thumb.o gui/testmenu.thumb.o gui/settingsmenu.thumb.o gui/controls.thumb.o infrared/infrare
d.thumb.o infrared/codes.thumb.o infrared/encoders.thumb.o infrared/ir_capture.thumb.o infrared/ir_selector.thumb.o keyboard/keyboard.thumb.o rtc/rtc.
thumb.o rtc/i2c.thumb.o rtc/rtctimer.thumb.o serial/serial.thumb.o serial/redirector.thumb.o timer/timerfuncs.thumb.o tools/toolsmenu.thumb.o tools/sc
art_icp.thumb.o moodpxl/moodpxlMenu.thumb.o moodpxl/mpxlRF.thumb.o infrared/ir_itt.thumbunopt.o infrared/ir_nrc17.thumbunopt.o infrared/ir_raw.thumbun
opt.o infrared/ir_rc5.thumbunopt.o infrared/ir_rc6.thumbunopt.o infrared/ir_rca.thumbunopt.o infrared/ir_rcmm.thumbunopt.o infrared/ir_rec80.thumbunop
t.o infrared/ir_recs80.thumbunopt.o infrared/ir_rf.thumbunopt.o infrared/ir_sirc.thumbunopt.o infrared/ir_spaceenc.thumbunopt.o infrared/ir_lirc.thumb
unopt.o -lc -lgcc
gui/controls.thumb.o: In function `trackbar_draw':
controls.c:(.text+0x804): relocation truncated to fit: R_ARM_THM_CALL against symbol `_draw_block' defined in .text.fastcode section in display/lcd.th
umb.o
controls.c:(.text+0x83e): relocation truncated to fit: R_ARM_THM_CALL against symbol `_draw_block' defined in .text.fastcode section in display/lcd.th
umb.o
controls.c:(.text+0x8d2): relocation truncated to fit: R_ARM_THM_CALL against symbol `_draw_block' defined in .text.fastcode section in display/lcd.th
umb.o
make: *** [boop_rom.elf] Error 1 ``

[Permalink](http://bettyhacks.com/forum/index.php?topic=289.msg2098#msg2098)

---

<a id="msg2099"></a>

## 3. bingo600 · 17. Dez 2012, 21:51

Hier ist makefiles für ronetics
[http://bettyhacks.com/forum/index.php?topic=285.msg2078#msg2078](0285-neues-user.md#msg2078)

Und für Codesourcery
[http://bettyhacks.com/forum/index.php?topic=285.msg2083#msg2083](0285-neues-user.md#msg2083)

03-jun-2014
Für arm-launchpad
[http://bettyhacks.com/forum/index.php?topic=1049.msg2888#msg2888](1049-betty-erstanden-juni-2014-probleme-mit-debian-squeeze-und-to.md#msg2888)

/Bingo Dänemark

*Last Edit : 03. Jun 2014, 21:16 by bingo600*

[Permalink](http://bettyhacks.com/forum/index.php?topic=289.msg2099#msg2099)

---

## Verwandte Themen

- [Betty erstanden (Juni 2014!!!) - Probleme mit Debian Squeeze und Toolchain](1049-betty-erstanden-juni-2014-probleme-mit-debian-squeeze-und-to.md)
- [undefined reference to 'strncpy'/'strncat'/'strnlen'](0227-undefined-reference-to-strncpy-strncat-strnlen.md)
- [Neues user](0285-neues-user.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
