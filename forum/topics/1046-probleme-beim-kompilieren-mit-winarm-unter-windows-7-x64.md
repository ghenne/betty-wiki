---
title: "Probleme beim kompilieren mit WinARM unter Windows 7 x64"
topic_id: 1046
board: "Software"
board_id: 6
posts: 3
first_post: "02. Okt 2013, 15:17"
last_post: "22. Okt 2013, 08:05"
authors: ["bingo600", "samerbaer"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=1046.0"
---

# Probleme beim kompilieren mit WinARM unter Windows 7 x64

[← Software](../boards/06-software.md) · Thema 1046 · 3 Beiträge · 02. Okt 2013, 15:17 – 22. Okt 2013, 08:05

Beteiligt: bingo600, samerbaer

---

<a id="msg2878"></a>

## 1. samerbaer · 02. Okt 2013, 15:17

Hallo,

ich habe bisher folgendes gemacht:
WinARM-20060606 installiert
PATH Variablen erstellt
Makefile.local.WinARM umbenannt und Pfade angepasst
Den Fehler durch die libgcc.a behoben (Hardware FP), indem ich die libgcc.a aus "ronetix-gnutools-arm-elf-4.1.1-linux.tar.bz2" verwendet habe
Den Fehler durch die libc.a behoben (Hardware FP), indem ich die libc.a aus "ronetix-gnutools-arm-elf-4.1.1-linux.tar.bz2" verwendet habe
Jetzt habe ich aber folgenden Fehler:
`` c:/WinARM//bin/arm-elf-ld -Tlpc2220_rom.ld -Map boop.map -Lc:/WinARM//lib/gcc/arm-elf/4.1.1/interwork -Lc:/WinARM//arm-elf/lib/interwork -o boop_rom.elf crt.o m
ain.o global.o buffer.o syscalls.o audio/soundirq.o infrared/infraredirq.o interrupt/irq.o keyboard/keyirq.o serial/serirq.o timer/timerirq.o adc/adc.thumb.o ad
c/adcirq.thumb.o audio/sound.thumb.o audio/sid.thumb.o cc1100/cc1100.thumb.o cc1100/rf.thumb.o cc1100/fs20.thumb.o display/lcd.thumb.o display/fonty.thumb.o dis
play/drawDigit.thumb.o display/drawIcon.thumb.o display/backlight.thumb.o flash/flash.thumb.o flash/bfs.thumb.o games/gamesmenu.thumb.o games/tic_tac_toe.thumb.
o games/sokoban.thumb.o games/connect4.thumb.o gui/menu.thumb.o gui/mainmenu.thumb.o gui/testmenu.thumb.o gui/settingsmenu.thumb.o gui/controls.thumb.o infrared
/infrared.thumb.o infrared/codes.thumb.o infrared/encoders.thumb.o infrared/ir_capture.thumb.o infrared/ir_selector.thumb.o keyboard/keyboard.thumb.o rtc/rtc.th
umb.o rtc/i2c.thumb.o rtc/rtctimer.thumb.o serial/serial.thumb.o serial/redirector.thumb.o timer/timerfuncs.thumb.o tools/toolsmenu.thumb.o tools/scart_icp.thum
b.o infrared/ir_itt.thumbunopt.o infrared/ir_nrc17.thumbunopt.o infrared/ir_raw.thumbunopt.o infrared/ir_rc5.thumbunopt.o infrared/ir_rc6.thumbunopt.o infrared/
ir_rca.thumbunopt.o infrared/ir_rcmm.thumbunopt.o infrared/ir_rec80.thumbunopt.o infrared/ir_recs80.thumbunopt.o infrared/ir_rf.thumbunopt.o infrared/ir_sirc.th
umbunopt.o infrared/ir_spaceenc.thumbunopt.o infrared/ir_lirc.thumbunopt.o -lc -lgcc
c:/WinARM//arm-elf/lib/interwork\libc.a(syscalls.o): In function `_sbrk':
/home/src/cross/newlib-1.14.0/newlib/libc/sys/arm/syscalls.c:476: multiple definition of `_sbrk'
syscalls.o:syscalls.c:(.text+0x0): first defined here
c:/WinARM//bin/arm-elf-ld: Warning: size of symbol `_sbrk' changed from 48 in syscalls.o to 84 in c:/WinARM//arm-elf/lib/interwork\libc.a(syscalls.o)
make.exe: *** [boop_rom.elf] Error 1 ``

Hierzu kann ich nichts im Forum finden, kann mir hier jemand helfen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=1046.msg2878#msg2878)

---

<a id="msg2879"></a>

## 2. bingo600 · 08. Okt 2013, 22:20

Probier mal diser Codesourcery makefile
[http://bettyhacks.com/forum/index.php?topic=285.msg2083#msg2083](0285-neues-user.md#msg2083)

Mit diser compiler
[https://launchpad.net/gcc-arm-embedded](https://web.archive.org/web/2012/https://launchpad.net/gcc-arm-embedded)

Andere instrukse
[http://bettyhacks.com/forum/index.php?topic=285.msg2078#msg2078](0285-neues-user.md#msg2078)

/Bingo

[Permalink](http://bettyhacks.com/forum/index.php?topic=1046.msg2879#msg2879)

---

<a id="msg2880"></a>

## 3. samerbaer · 22. Okt 2013, 08:05

Hi,
das installieren einer neuen Toolchain war mir dann doch zu viel Arbeit.

Ich habe in der syscalls.c die Zeile:
`caddr_t _sbrk ( int incr )`
in:
`caddr_t _sbrk2 ( int incr )`
und schon klappt das compilieren.
Betty geflasht und läuft.

Trozdem Dank für die Hilfe

[Permalink](http://bettyhacks.com/forum/index.php?topic=1046.msg2880#msg2880)

---

## Verwandte Themen

- [Neues user](0285-neues-user.md)
- [Boop Kompilieren unter winarm](0295-boop-kompilieren-unter-winarm.md)
- [Probleme beim boop flashen](0178-probleme-beim-boop-flashen.md)
- [[gelöst] lpctool mit Cygwin unter Windows 7 bauen?](0241-geloest-lpctool-mit-cygwin-unter-windows-7-bauen.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
