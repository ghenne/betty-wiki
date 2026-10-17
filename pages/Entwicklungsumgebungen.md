# Entwicklungsumgebungen

## Betty HHU

### Allgemeines

Zur zeit versuchen wir bzgl dem compilieren von boop (und allem was da noch so kommt) eine einheitliche Basis zu schaffen, damit wir nicht auf zig tausend Toolchains Rücksicht nehmen müssen wenn Leute sich an der Software-Entwicklung beteiligen möchten.

Geplant ist im Moment eine Toolchain für Linux und eine toolchain für Windows die ohne großartige Veränderungen an boop supportet werden soll.

### Linux

Die aktuell verwendete Toolchain ist von [Launchpad](https://launchpad.net/).

Zuletzt verwendet wurde die Version 4_9-2014q4. Die Toolchain steht kostenlos unter den unten stehenden Links zum Download zur Verfügung.

  

#### Compiler, Linker und Tools

Um Boop zu compilieren braucht ihr die [ARM GCC Toolchain](https://launchpad.net/gcc-arm-embedded)

Die Toolchain kann dann in ein beliebiges Verzeichnis einfach augepackt werden - in den Files aus dem SVN Repository wird /opt/toolchains/gcc-arm-none-eabi-4_9-2014q4 als Pfad angenommen.

#### Compileren von boop

##### Download

    svn checkout svn://svn.code.sf.net/p/boopfirmware/code/boop/trunk boopfirmware

##### Compilieren

    cd boopfirmware

Wechselt in das Verzeichnis boop/trunk im aktuellen Verzeichnis. Wenn ihr alles richtig gemacht habt sollte nun ein

    make

unter anderem die Datei **boop_rom.bin** erstellt haben

### Windows

Um Boop zu compilieren braucht ihr ebenfalls die [ARM GCC Toolchain](https://launchpad.net/gcc-arm-embedded). Ihr müsst nur den Pfad, in dem Ihr die Toolchain installiert habt, im Makefile als "ARMBASE" Pfad angeben.

Folgendes ist obsolet:

Die aktuell verwendete Toolchain ist [WinARM](http://www.siwawi.arubi.uni-kl.de/avr_projects/arm_projects/#winarm).

Aktuell verwendet wird die Version 20060606. Diese steht [hier](http://www.siwawi.arubi.uni-kl.de/avr_projects/arm_projects/WinARM-20060606.zip) zum Download zur Verfügung.

- WinARM nach C:\\ entpacken
- Systemeigenschaften -\> Erweitert -\> Umgebungsvariablen: PATH Variable setzen (siehe readme.htm)
- Makefile.local.WinARM umbenennen in Makefile.local
- In der Datei Makefile.local die Pfade anpassen, wenn nicht nach C:\\ entpackt wurde. Kein abschließender Schrägstrich!
- Die Datei C:\WinARM\arm-elf\lib\interwork\libgcc.a (320292 Byte)  
  ist durch die Datei ronetix-gnutools-arm-elf-4.1.1-linux.tar.bz2\ronetix-gnutools-arm-elf-4.1.1-linux.tar\usr\cross\arm-elf\lib\gcc\arm-elf\4.1.1\interwork\libgcc.a (323938 Byte)  
  zu ersetzen. Die libgcc.a kann [hier](http://bettyhacks.com/forum/index.php?topic=106.msg891#msg891) als "7Z-Datei" oder "zip-Datei" bezogen werden.
- Ggf. in C:\WinARM\utils\bin die Datei "sed_WinARM.exe" zu "sed.exe" umbenennen

Inhalt der Datei Makefile.local:

**\###############################################################**  
**\#####**  
**\##### Makefile.local.WinARM for boop**  
**\##### Created in the early morninghours**  
**\#####**  
**\##### Makefile.local.WinARM V1.0 by alterego - alteregon@gmx.net**  
**\#####**  
**\##### Copy this file to Makefile.local for your Windows**  
**\##### installation**  
**\#####**  
**\###############################################################**  
**ARMBASE = c:/WinARM**  
**INCLUDEPATH = \$(ARMBASE)/include**  
**LIBPATH = \$(ARMBASE)/arm-elf/lib/interwork**  
**ARMPATH = \$(ARMBASE)/bin**  
**TOOLPREFIX = arm-elf-**  
**LPCTOOL = lpctool.exe**  
**\######################## EOF \##################################**

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

