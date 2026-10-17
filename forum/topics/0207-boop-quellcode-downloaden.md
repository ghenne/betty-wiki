---
title: "Boop Quellcode downloaden?"
topic_id: 207
board: "Software"
board_id: 6
posts: 10
first_post: "06. Mai 2009, 11:33"
last_post: "07. Mai 2009, 13:16"
authors: ["AKtronik", "El_Barto", "Telekatz", "asgard", "gerdi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=207.0"
---

# Boop Quellcode downloaden?

[← Software](../boards/06-software.md) · Thema 207 · 10 Beiträge · 06. Mai 2009, 11:33 – 07. Mai 2009, 13:16

Beteiligt: AKtronik, El_Barto, Telekatz, asgard, gerdi

---

<a id="msg1406"></a>

## 1. AKtronik · 06. Mai 2009, 11:33

Hallo Leute,

hab da mal ne Frage.
Ich wollte den Boop-Quellcode (Rev 284) mit WinARM kompilieren, um zu versuchen Erweiterungen vorzunehmen, und unter folgendem Link downloaden.

[http://svn.mamalala.org/listing.php?repname=boop&path=%2Ftrunk%2F&rev=0&sc=0](https://web.archive.org/web/2012/http://svn.mamalala.org/listing.php?repname=boop&path=%2Ftrunk%2F&rev=0&sc=0)

Nun habe ich festgestellt, dass der Quellcode nicht als downloadbare *.zip oder Projektdateien vorliegt.
Wie kommt man denn an die Dateien ran?

MfG
AKtronik

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1406#msg1406)

---

<a id="msg1407"></a>

## 2. asgard · 06. Mai 2009, 13:43

such mal nach nem svn clienten (z.b. rapidsvn)...
damit kannst du den gesamten source auschecken...

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1407#msg1407)

---

<a id="msg1408"></a>

## 3. AKtronik · 06. Mai 2009, 16:07

Hallo asgard,

so geht das also, danke für denn Hinweis!
Hab es mal mit RapidSVN versucht.
Wenn ich im linken Fenster mit rechter Maustaste->[Neue Arbeitskopie auschecken...] und im Dialogfeld "Auschecken" den Link

[http://svn.mamalala.org/listing.php?repname=boop&path=%2F&sc=0](https://web.archive.org/web/2012/http://svn.mamalala.org/listing.php?repname=boop&path=%2F&sc=0)

oder

[http://svn.mamalala.org](https://web.archive.org/web/2012/http://svn.mamalala.org)

und das Zielverzeichnis eingebe, dann bekomme ich die Fehlermeldung:

Fehler beim Ausführen der Aktion: PROPFIND of '/listing.php': 200 OK ([http://svn.mamalala.org](https://web.archive.org/web/2012/http://svn.mamalala.org))

Kann mir vielleicht jemand sagen, was da schief läuft?!?

MfG
AKtronik

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1408#msg1408)

---

<a id="msg1409"></a>

## 4. gerdi · 06. Mai 2009, 17:32

Ich habs mit Lenny auf einem eeepc gemacht, genau nach WIKI

Auszug aus:
[http://www.bettyhacks.com/wiki/index.php/Entwicklungsumgebungen](../../pages/Entwicklungsumgebungen.md)

 Compileren von boop
Download

svn checkout svn://svn.mamalala.org/boop/trunk

Compilieren

cd boop/trunk

Wechselt in das Verzeichnis boop/trunk im aktuellen Verzeichnis. Wenn ihr alles richtig gemacht habt sollte nun ein

make

unter anderem die Datei boop_rom.bin erstellt haben

Lief perfekt

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1409#msg1409)

---

<a id="msg1410"></a>

## 5. AKtronik · 06. Mai 2009, 22:02

Hallo und Danke für die Hilfe!!!

Mit svn checkout svn://svn.mamalala.org/boop/trunk als URL hat das Runterladen der Dateien geklappt. Juhuu!
Anschießend wollte ich den Quellcode mit WinARM Kompilieren. Es sah erst gut aus.
Bis zur fehlermeldung:

> "make.exe" all
.
.
.
.
c:/Software/WinARM/bin/arm-elf-ld: ERROR: c:/Software/WinARM/lib/gcc/arm-elf/4.1.1/interwork\libgcc.a(_dvmd_tls.o) uses hardware FP, whereas boop_rom.elf uses software FP
c:/Software/WinARM/bin/arm-elf-ld: failed to merge target specific data of file c:/Software/WinARM/lib/gcc/arm-elf/4.1.1/interwork\libgcc.a(_dvmd_tls.o)
make.exe: *** [boop_rom.elf] Error 1

> Process Exit Code: 2
> Time Taken: 00:00

Ich habe nach Wiki folgendes gemacht:

WinARM nach C:\ entpacken
Systemeigenschaften -> Erweitert -> Umgebungsvariablen: PATH Variable setzen (siehe readme.htm)
Makefile.local.WinARM umbenennen in Makefile.local
In der Datei Makefile.local die Pfade anpassen. Kein abschließender Schrägstrich!
Die Zeile LIBPATH=$(ARMBASE)... löschen oder mit # versehen.
Die Datei C:\WinARM\lib\gcc\arm-elf\4.1.1\interwork\libgcc.a
ist durch die Datei ronetix-gnutools-arm-elf-4.1.1-linux.tar.bz2\ronetix-gnutools-arm-elf-4.1.1-linux.tar\usr\cross\arm-elf\lib\gcc\arm-elf\4.1.1\interwork\libgcc.a zu ersetzen.
Die libgcc.a kann hier als "7Z-Datei" bezogen werden.

Das Makefile.local sieht jetzt so aus:

ARMBASE = c:/Software/WinARM
INCLUDEPATH = $(ARMBASE)/include
# ~~LIBPATH = $(ARMBASE)/arm-elf/lib/interwork~~
ARMPATH = $(ARMBASE)/bin
TOOLPREFIX = arm-elf-
LPCTOOL = lpctool.exe

Leider kann ich die Ursache für den Fehhler trotz Forumsuche nicht nachvollziehen.
Hat da vielleicht jemand einen Tip?

MfG
AKtronik

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1410#msg1410)

---

<a id="msg1411"></a>

## 6. Telekatz · 06. Mai 2009, 22:16

Nimm LIBPATH wieder mit rein.

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1411#msg1411)

---

<a id="msg1412"></a>

## 7. El_Barto · 06. Mai 2009, 22:18

Hi,

die Compilierung wird bei dir an der Libgcc scheitern. Den Lib-Path hast du ja scheinbar gestrichen. Da gehört jedoch folgendes hin:
`LIBPATH = $(ARMBASE)/lib/gcc/arm-elf/4.1.1/interwork`

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1412#msg1412)

---

<a id="msg1413"></a>

## 8. AKtronik · 06. Mai 2009, 22:41

Danke für die schnellen Antworten!

Die Beschreibung im Wiki scheint falsch zu sein.
Ich habe ja vorher die "richtige" libgcc.a nach C:\WinARM\lib\gcc\arm-elf\4.1.1\interwork\ kopiert.

LIBPATH wieder reingenommen
LIBPATH = $(ARMBASE)/arm-elf/lib/interwork -> FEHLER
LIBPATH = $(ARMBASE)/lib/gcc/arm-elf/4.1.1/interwork -> FEHLER

Dann habe ich die "richtige" libgcc.a nach C:/Software/WinARM/arm-elf/lib/interwork kopiert und siehe da,

ES FUNKTIONIERT!!!

Vielen Dank für Eure tolle Hilfe.
Ohne Euch wäre ich nie darauf gekommen!

MfG
AKtronik

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1413#msg1413)

---

<a id="msg1414"></a>

## 9. asgard · 07. Mai 2009, 11:26

Hi AKtronik,
dann verbesser doch kurz das Wiki

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1414#msg1414)

---

<a id="msg1415"></a>

## 10. AKtronik · 07. Mai 2009, 13:16

Ok, erledigt.

MfG
AKtronik

[Permalink](http://bettyhacks.com/forum/index.php?topic=207.msg1415#msg1415)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
