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
  zu ersetzen. Die libgcc.a kann [hier](../forum/topics/0106-fehler-boop-kompileren.md#msg891) als "7Z-Datei" oder "zip-Datei" bezogen werden.
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

<!-- forum-links:start -->
## Forumsdiskussionen: Toolchain und Build

Ergänzend zur Toolchain-Übersicht: konkrete Builds unter Linux, macOS und Windows (WinARM, Cygwin, CodeSourcery, Debian, arm-launchpad), Makefile-Anpassungen und typische Compiler-/Linkerfehler.

### Toolchain für Mac OS X / Linux

- [Toolchain für Mac OS X / Linux](../forum/topics/0261-toolchain-fuer-mac-os-x-linux.md) — Boop unter Mac OS X/Linux kompilieren und Toolchain bauen.

### McBetty/Toolchain einrichten

- [Toolchain](../forum/topics/0273-toolchain.md) — McBetty aus GitHub-Quellen mit WinARM bauen.

### GCC 4.5.2 CodeSourcery: Alignment-Warnings

- [Aktueller GCC 4.5.2 von CodeSourcery produziert Alignment Warnings](../forum/topics/0269-aktueller-gcc-4-5-2-von-codesourcery-produziert-alignment-wa.md) — GCC 4.5.2 von CodeSourcery: Alignment-Warnungen und newlibc/uClibc.

### Debian Squeeze: passende Toolchain

- [Betty erstanden (Juni 2014!!!) - Probleme mit Debian Squeeze und Toolchain](../forum/topics/1049-betty-erstanden-juni-2014-probleme-mit-debian-squeeze-und-to.md) — Boop aus aktuellen Quellen unter Debian Squeeze bauen.

### arm-launchpad-Compiler

- [Betty für arm-launchpad compiler](../forum/topics/1050-betty-fuer-arm-launchpad-compiler.md) — ARM-Launchpad-Compiler für Betty.

### WinARM unter Windows 7 x64 / WinARM-Build

- [Probleme beim kompilieren mit WinARM unter Windows 7 x64](../forum/topics/1046-probleme-beim-kompilieren-mit-winarm-unter-windows-7-x64.md) — WinARM unter Windows 7 x64 einrichten und libgcc.a ersetzen.
- [Boop Kompilieren unter winarm](../forum/topics/0295-boop-kompilieren-unter-winarm.md) — Boop mit WinARM 20060606 kompilieren.

### Boop kompilieren: Fehler und Compilerfehler

- [Fehler - BOOP kompileren](../forum/topics/0106-fehler-boop-kompileren.md) — Typische Fehler beim Boop-Build.
- [Compilerfehler](../forum/topics/0289-compilerfehler.md) — Compilerfehler beim Boop-Build.

### undefined reference: strncpy/strncat/strnlen

- [undefined reference to 'strncpy'/'strncat'/'strnlen'](../forum/topics/0227-undefined-reference-to-strncpy-strncat-strnlen.md) — Linkerfehler bei strncpy/strncat/strnlen.

### Keil als alternative IDE

- [Software für Betty mit Keil erstellen](../forum/topics/0109-software-fuer-betty-mit-keil-erstellen.md) — Betty-Software mit Keil erstellen.

### Lokale Toolchain-Settings

- [toolchains, lokale settings](../forum/topics/0075-toolchains-lokale-settings.md) — Boop und lpctool mit GCC 4.1.1 bauen, lokale Settings.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

