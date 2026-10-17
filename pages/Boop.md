# Boop

Boop ([Namensgeberin](http://de.wikipedia.org/wiki/Betty_Boop))ist eine Software (Firmware) fuer die Betty TV, welche von **netguy** entwickelt wurde, und von einigen anderen erweitert wird. Die Firmware dient derzeit haupsaechlich als "testbed" um die Hardware der Betty anzusprechen. Die Firmware enthält Routinen für das Ansprechen der meisten Hardwarekomponenten der Betty.

## Features

Siehe [Boop Features](Boop%20Features.md "Boop Features"). Für andere Verwendungen der Betty Hardware siehe [Projekte](Projekte.md "Projekte").

## Lizenz

**boop** steht unter der [GPL](http://www.gnu.org/copyleft/gpl.html)v3. Bitte beachtet das wenn, ihr an der Software herumbastelt!

## Download

Den aktuellen Source erhält man über [SVN](SVN.md "SVN") [hier](https://sourceforge.net/projects/boopfirmware/develop). Das aktuelle RAW-Binary zum download: [boop_rom.bin](https://boopfirmware.svn.sourceforge.net/svnroot/boopfirmware/boop/trunk/boop_rom.bin)

## Mitarbeit

Wenn Du Fehler findest, oder anders helfen möchtest, melde Dich am Besten im [Forum](http://bettyhacks.com/forum). Zum Entwickeln: [Coding Style](Coding%20Style.md "Coding Style").

  

## Das System

Die Firmware ist in C geschrieben für den 32-bit Mikroprozessor mit ARM7 Kern (siehe [Entwicklungsumgebungen](Entwicklungsumgebungen.md "Entwicklungsumgebungen")). Es sind 64kb SRAM und 16mbit (= 2 MiByte) externer Flash-Speicher vorhanden.

Es ist möglich, ein Programm direkt aus dem RAM auszuführen. Das Überschreiben des Flashspeichers entfällt so (siehe [Forum](http://bettyhacks.com/forum/index.php?topic=215.msg1449#msg1449)).

Näheres zu den Komponenten unter [Betty Hardware](Betty%20Hardware.md "Betty Hardware") und [hackdaworld](http://www.hackdaworld.org/cgi-bin/awki.cgi/BettyTV)

### Das 'Betriebssystem' Timer, Interrupts, ...

Die Timers und Interrupts sind unter [Boop Peripherie](Boop%20Peripherie.md "Boop Peripherie") aufgelistet.

### Hardwareunterstützung

#### Serielle Schnittstelle

(an der Stiftleiste) txd0, rxd0

- Baudrate <http://www.standardics.nxp.com/support/documents/microcontrollers/xls/lpc2000.uart.baudrate.calculator.xls>

#### Display

- Anbindung über Speicheradresse 0x81000000 (CMD) und 0x81000001 (DATA)
- Kontrast einstellbar (in Grenzen)
- Diverse Grafik- und Schriftfunktionen (siehe Menu\>TestStuff)
  - Schriften
  - Grafik
    - Bereich löschen, füllen, Linie, Rechteck, Kreise etc

##### Hintergrundbeleuchtung

- Pin: [sck0/P0.4](LPC2220%20Pin-Belegung.md "LPC2220 Pin-Belegung")
- 64 Helligkeitsstufen (Software-PWM in SoundIRQ)
- Leuchtdauer einstellbar (n\*\[s\])
- Übergangsgeschwindigkeit einstellbar (n \* 5 ms / Helligkeitsstufe)

#### Tastatur

Q: 'keytest' im Menü 'TestStuff' zeigt Tastaturcodes, wie kommt man da wieder raus?

A: Batterien rein und raus! Bei dem Hintergedanken der Funktion allerdings völlig legitim.

#### Akkuzustand

Wird in oben rechts als Batteriesymbol angezeigt. 'bat debug' im Menü 'TestStuff' zeigt - was für Werte?

#### Audio

##### Hardware

P0.7/SSEL0/PWM2/EINT2 69 PWM\<br\\ P0.11/CTS1/CAP1.1 83 Shutdown\<br\\

Verstärker: LM4876

##### Software

Sounderzeugung (Menu\>TestStuff\>SID) und Wiedergabe von Samples (Menu\>Credits)

#### IR

Über Pin 4 (P0.21/PWM5/CAP1.3) kann die IR Diode zum Senden ein und ausgeschaltet werden.\<br\\ Der IR-Empfang wird über Pin 84 (P0.12/DSR1/MAT1.0) aktiviert/deaktiviert.\<br\\ Über Pin 32 (P0.29/AIN2/CAP0.3/MAT0.3) wird das empfangene Signal eingelesen.\<br\\

#### Funk

Transceiver [CC1100](CC1100.md "CC1100") Testweise als IR-Device eingebaut, überträgt Tastencodes an den [SCART Adapter](SCART%20Adapter.md "SCART Adapter") mit [betty_scart](Betty%20scart.md "Betty scart")

- Kommunikation Scartadapter [Forum](http://bettyhacks.com/forum/index.php?topic=114.msg826#msg826)
- Transceiver CC1100 Möglichkeiten [Forum](http://bettyhacks.com/forum/index.php?topic=121.msg850#msg850)

#### Uhr

I2C

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

