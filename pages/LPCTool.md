# LPCTool

lpctool überträgt [Firmware](Boop.md "Boop") über einen [Adapter](Interfaces%20PC%20zu%20Betty.md "Interfaces PC zu Betty") [seriell](http://de.wikipedia.org/wiki/RS-232) zur [Betty](Betty.md "Betty").

Siehe auch: [Betty-Heaven](Betty-Heaven.md "Betty-Heaven")

## Aktuelle Version

lpctool V0.9 This Software is free Software under GNU GPL 3 or later (c) 2007 Ch. Klippel \<ck@mamalala.net\>

Quellcode im SVN ansehen: <http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware/lpctool/trunk/>

## Forumsdiskussion

Die Ankündigung des Programms im Forum: <http://bettyhacks.com/forum/index.php?topic=54.0>

## Funktion

Siehe \#Flashvorgang.

1.  Bootloader aktivieren
    1.  Zusätzlich zu den Datenleitungen werden zwei Handshake-Signale benutzt

<!-- -->

    PC    Betty
    -----------
    TX  - RX
    RX  - TX
    DTR - nReset
    RTS - eINT1

1.  Flashtool ins RAM der Betty laden
2.  LPCTool sendet neue Firmware an Flashtool
3.  Flashtool schreibt neue Firmware in den Flash

## Unterstützte Hardware

Findet man unter [Interfaces PC zu Betty](Interfaces%20PC%20zu%20Betty.md "Interfaces PC zu Betty").

## Windows

<http://megabug.de/cmde/betty_pub/lpctool-cygwin.zip>

Es gibt aber Einschränkungen, siehe LPCTool#Lpctool-Probleme.

## Linux

### Debian Paket

Für Debian Basierte Distr. kann man folgendes Paket nehmen.

    http://www.grautier.com/grautier/index.php?/plugin/dlfile_108

### selbst kompilieren

Man benötigt die ARM-toolchain, siehe [Entwicklungsumgebungen](Entwicklungsumgebungen.md "Entwicklungsumgebungen")

Das LPCTool kann man unter Linux mit subversion herunterladen.

    svn co http://boopfirmware.svn.sourceforge.net/svnroot/boopfirmware/lpctool/ lpctool

Alsdann kann das Programm compiliert werden:

    cd trunk
    make
    sudo make install

Bei dem Paket für Debian Basierte Systeme

    dpkg -i LPCTool.deb

## Boop Flashen

### LPCTool Parameter

    usage: lpctool [-d NAME] [-i] [-r [NAME]] [-R ADDRESS] [-X [ADDRESS]] [-a [NAME] [-A ADRDESS]] [-e] [-b [NAME] [-B ADDRESS]] 
                   [-E] [-s] [-S] [-c] [-C] [-v] [-V]

            -d NAME         specify serial device, default is /dev/ttyS0
            -i              use compiled-in flash-tool instead of external ram image file
            -r NAME         specify file for ram,  default is ramtool.bin
            -R ADDRESS      optionally specifies the start-address to load into ram
                            default is 0x40000200 - must be specified in hex
            -X ADDRESS      set the execution address for the uploaded ram image
                            defualt is 0x40000200, omiting the address disables execution
            -a NAME         specify file for flash #0, default is flash0.bin
            -A ADDRESS      optionally specifies the start-address to load into flash #0
                            default is 0x80000000 - must be specified in hex
            -e              completely erase the first flash before writing
                            default is no erase
            -b NAME         specify file for flash #1, default is flash1.bin
            -B ADDRESS      optionally specifies the start-address to load into flash #1
                            default is 0x82000000 - must be specified in hex
            -E              completely erase the second flash before writing
                            defualt is no erase
            -S              only erase the first sector in flash before writing
                            this is a lot faster if only the first sector is used
            -c              write flash0 in chunk mode instead of write-all
            -C              write flash1 in chunk mode instead of write-all
                            in chunk mode, parts with 4 consectuive 0xFFFFFFFF or more
                            in the image are skipped. speeds upload when the image has
                            gaps. defualt is off
            -N              do not reset the device after uploading to flash
                            by default the device gets reset after upload
            -?              print this help
            -v              print version
            -V              be more verbose

  

### Linux

Flashen kann man dann z.B. so:

    ./lpctool -d /dev/ttyS0 -i -v -e -a boop_rom.bin

Wenn man LPCTool installiert hat (Debian-Paket oder `make install`) lässt man das `./` weg.

### Windows

Flashen kann man dann z.B. so:

    lpctool.exe -d /dev/com4 -i -v -e -a boop_rom.bin

  

### Flashvorgang

    lpctool -d /dev/ttyUSB0 -i -v -e -a boop_rom.bin

    lpctool V0.9

    This Software is free Software under GNU GPL 3 or later
    (c) 2007 Ch. Klippel <ck@mamalala.net>

    Info : erasing flash #0 before write
    Info : using flash #0 image boop_rom.bin
    Info : opening serial device /dev/ttyUSB0
    Info : reset into bootmode
    Info : opening bootloader
    Info : initiating auto-baud
    Info : awaiting autobaud response
    Info : got response, answering
    Info : setting frequency
    Info : switching baudrate
    Info : disabling echo
    Info : unlocking bootloader
    Info : uploading compiled-in ram image
    Info : starting ram upload
    Info : ram upload complete, total bytes: 0x000049CC
    Info : ram uploaded
    Info : executing code at ram address 0x40000200
    Info : code execution started 0x40000200
    Info : opening ram tool
    Info : opened ramtool
    Info : opening flash0 image boop_rom.bin
    Info : uploading flash0 image boop_rom.bin
    Info : setting address to 0x80000000
    Info : erasing whole flash
    Info : erasing flash
    Info : whole flash erased
    Info : enabling bulk write
    Info : setting total number of bytes to 0x000301D8
    Info : starting flash upload
    Info : flash upload complete, total bytes: 0x000301D8
    Info : flash #0 uploaded
    Info : reset device
    Info : closing file descriptor
    Info : closing serial device /dev/ttyUSB0

  

## Lpctool-Probleme

Falls nach dem Laden des Bootloaders (ramtool) die Fernbedienung neu startet (reset!) - im Quellcode die Geschwindigkeit (u.a. TOOLBAUD) von 115.200 baud auf 38.400 baud reduzieren. "tcsetattr" toggelt beim Baud-Wechsel (38.400-\>115.200) den reset-Pin (Linux, CentOS 5, USB-Seriell-Kabel, Windows mit FT232R, Linux mit PL2303(H?)X.

Eine gebremste lpctool-cygwin für Windows gibt es [im Forum](http://bettyhacks.com/forum/index.php?topic=54.msg842#msg842).

Eine mit cygwin für Windows gebaute Version, die ohne Baudratenwechsel bei 38400 baud auskommt gibt es ebenfalls [im Forum](http://bettyhacks.com/forum/index.php?topic=241.msg1667#msg1667). Getestet mit PL-230? USB-UART Wandler.

  
Stellen im Code von LPCTOOL:

**lpctool_serial.h** *Zeile 5*:

     #define TOOLBAUD 115200

muss geändert werden in

     #define TOOLBAUD 38400

**serial.c** *Zeile 170*:

     serial_setbrg (115200);

muss geändert werden in

     serial_setbrg (38400);

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

