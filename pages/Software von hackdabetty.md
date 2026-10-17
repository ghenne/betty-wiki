# Software von hackdabetty

|  |  |
|----|----|
| [<img src="../images/b/bb/Wichtig.50px.png" width="50" height="42" alt="Wichtig.50px" />](Datei_Wichtig.50px.png.md) | **Diese Software gilt als veraltet.** Sie wurde durch **[LPCTool](LPCTool.md "LPCTool")** ersetzt, welche aktueller, schneller und wesentlich sauberer ist, als die von hackdabetty |

  
**Benoetigte Software**

Benoetigt werden die arm-linux-tools [\[1\]](http://opensrc.sec.samsung.com/download/arm-uclinux-tools-base-gcc3.4.0-20040713.sh) und lpcprog + Die Firmware Files [\[2\]](http://www.hackdaworld.org/cgi-bin/gitweb.cgi?p=my-code/arm.git;a=tree;f=betty).

  
**Software vorbereiten**

Als erstes entpackt ihr die Dateien vom Hackdaworld-Wiki[\[3\]](http://www.hackdaworld.org/cgi-bin/gitweb.cgi?p=my-code/arm.git;a=snapshot;h=1df785469a4cf54778b37de7b976e7e703693d1b), danach habt ihr folgende Dateien:

    Makefile
    lpcload.c
    lpc2xxx.h
    fwbc.c
    fwdump.c
    betty.c

Jetzt muesst ihr die Makefile Datei noch editieren z.b. mit NANO (theborg@TBM:~/Desktop/betty/flash\$ nano Makefile) da aendert ihr

    4 ARMCC = /scratch/arm-elf/bin/arm-elf-gcc
    5 ARMCFLAGS = -Wall -mcpu=arm7tdmi-s 
    6 ARMOBJCOPY = /scratch/arm-elf/bin/arm-elf-objcopy

in

    4 ARMCC = arm-elf-gcc
    5 ARMCFLAGS = -Wall -mcpu=arm7tdmi-s 
    6 ARMOBJCOPY = arm-elf-objcopy

Wenn ihr das gemacht habt reicht ein einfaches make um die benoetigten Programme und Dateien zu erstellen. Das sieht in etwa dann so aus.

    theborg@TBM:~/Desktop/betty/flash$ make
    gcc -Wall    lpcload.c   -o lpcload
    arm-elf-gcc -Wall -mcpu=arm7tdmi-s  -c fwbc.c -o fwbc
    arm-elf-objcopy -O ihex fwbc fwbc.hex

**Dateien Flashen**

    ./lpcload -d /dev/ttyUSB0 -f fwbc.hex -c 10000000

Die Ausgabe sollte dann wie folgt aussehen(wer etwas mehr sehen moechte kann -v noch hinten anhaengen).

    theborg@TBM:~/Desktop/betty/flash$ ./lpcload -d /dev/ttyS0 -f fwbc.hex
    boot loader init ...
    write firmware to ram ...
    unlock go command ...
    go ...
    txrx bad return code!

    the above error might be due to the jump!

    continue listening on serial port? (ctrl+c to quit) [y|n]: n

**Original Software Auslesen**

    ./fwdump /dev/ttyS0 flash_content

Dieses dauert sehr lange

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

