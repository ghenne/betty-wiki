# Boop Features

Hier eine Übersicht über die Funktionen von Boop. Siehe auch [Boop#Das_System](Boop.md "Boop").

Boop 0.91 rev 19 2009-12-16 (siehe SVN).

### Fernbedienung

#### Infrarot

Unterstützt 4 Fernbedienungsprofile (A,B,C,D), die mit vielen IR-Codes und Geräten belegt werden können.

##### Codes

Die unterstützten Codes und Geräte sind unter <http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware/boop/trunk/infrared/ir_codes/> einzusehen.

Es ist relativ einfach möglich, [LIRC](http://www.lirc.org/)-kompatible Geräte in den Quellcode mit einzufügen:

    boop/infrared/ir_codes

[Fernbedienungscodes](https://github.com/ghenne/betty-forum/blob/main/topics/0110-fernbedienungscodes.md#msg796)

Mit dem Encoder LIRC ist es noch einfacher, Codes aus der [LIRC-Datenbank](http://lirc.sourceforge.net/remotes/) in Boop zu integrieren.

##### Anlernen

Es ist auch möglich, vier IR-Signale aufzuzeichnen (Settings\>IR learn) und wieder abzuspielen (Zuordnung: Settings\>RC codes\>04 remotes in learn).

##### Empfangen/Senden

(TestStuff\>receive IR)

Bedeutung der Werte: <http://bettyhacks.com/forum/index.php?topic=144.0>

#### Funk

##### Funksteckdosen

Der "LIRC" Encoder kann Pulse auch über den RF-IC senden. Funksteckdosen benutzen AM im 433 MHz ISM Band mit häufig trinären Encodern. Die drei Zustände lassen sich durch zwei Symbole codieren. Die "LIRC" Struktur wurde so erweitert, dass die Sendedaten als o.g. Symbole interpretiert und in entsprechende Pulsfolgen umgesetzt werden ([Funksteckdose](https://github.com/ghenne/betty-forum/blob/main/topics/0223-funksteckdose.md#msg1542)). Das Senden erfolgt durch ... des RF-ICs.

Auch wenn die Systeme ähnliche Encoder verwenden, entscheidet die Beschaltung über die gesendeten Codes.

###### Unterstützung

Encoder PT2262 ≙ HX2262 ≙ LP801B (≙ ARC M3EA ?):

- Datenblatt: <http://www.princeton.com.tw/downloadprocess/downloadfile.asp?mydownload=PT2262.pdf>
- Protokoll: <http://avr.börke.de/Funksteckdosen.htm> und <http://www.mikrocontroller.net/topic/63171> (Unitec)

Geräte:

- "Funkfernschalter" Unitec
  - Innenleben, Encoder-IC: <http://thomaskropf.at/index.php?option=com_content&task=view&id=19&Itemid=28>
  - IC: LP801B oder HX2262

<!-- -->

- REV Telecontrol ( 008340 )
  - HS2260A-R4 ≙ PT2260RC4
  - Innenleben, Encoder-IC: <http://mitglied.multimania.de/madmax3333/>

  

###### Unterstützung nicht bekannt

- [ARCTECH](http://www.arctech.com.tw/products/allproud.htm) aka Intertechno
  - Bez. Sender / Empfänger: YCT-100 / YCR-3500
  - IC: ARC M3EA? (man müsste die Protokolle vergleichen)
  - Protokoll: <http://www.mikrocontroller.net/topic/124084>

##### FS20

FS20:

- [Hausautomationssystem von ELV-Elektronik](http://www.elv.de/FS20-Haussteuerungs-System/x.aspx/cid_74/detail_1/detail2_313)
- <http://fhz4linux.info/tiki-index.php?page=FS20>

868 MHz ISM-Band. Der [CC1100](CC1100.md "CC1100") ist für 434 MHz beschaltet, entsprechend schlechter ist die Sende/Empfangsleistung in diesem Band.

Mit dem LIRC Encoder. [Funksteckdose](https://github.com/ghenne/betty-forum/blob/main/topics/0223-funksteckdose.md#msg1542)

Protokoll:

- <http://fhz4linux.info/tiki-index.php?page=FS20+Protocol>
- <http://www.mikrocontroller.net/topic/45762>

##### RF Test

Sendet und empfängt (Ping) Daten. Mit zwei Bettys:

- Settings\>RF: denselben Kanal, unterschiedliche IDs einstellen
- TestStuff\>RF Test: die jeweils andere ID einstellen

Ist nicht 100% zuverlässig, mehrmals probieren:

- - OK sendet ping, empfängt Antwort
  - TV sendet "TV"
  - POWER sendet "PW"

##### RSSI Monitor

Stellt die Feldstärke grafisch dar.

##### RF Viewer

Plottet die Daten asynchron, 1 px entspricht 50 µs. Alternativ Ausgabe über serielle Schnittstelle. [FS20/HX2262 Howto](https://github.com/ghenne/betty-forum/blob/main/topics/0232-fs20-hx2262-howto.md#msg1600)

##### Redirector

Leitet serielle Schnittstelle auf Funk um.

#### Grafik

(in Menu\>Teststuff) Diverse Grafikroutinen (Kreise, Schrift etc.) testen.

#### SID

[source](http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware/boop/trunk/audio/) (in Menu\>Teststuff) Sound Interface Device (siehe: <http://de.wikipedia.org/wiki/MOS_Technology_SID>).

- n polyphon
- 4 Wellenformen rot, grün, gelb, blau
- 4 Hüllkurven A,B,C,D
- 7 Töne über Zifferntasten 1..7
- ein "Lied" OK

Ausser beim Abspielen des Liedes ist die Tonerzeugung auch während einer Note beeinflussbar.

### Werkzeuge

(in Menu\>Tools)

#### SCART ICP

Flashen des [SCART Adapters](SCART%20Adapter.md "SCART Adapter") mit [Betty](Betty.md "Betty") und [boop](Boop.md "Boop") (für [betty_scart](Betty-scart.md "Betty-scart")).

#### Serial redirector

Funkübertragung der Daten der seriellen Schnittstelle. Von Betty zu (Betty/SCART Adapter)?

  

### Spiele

(in Menu\>Games)

Es gibt 3 Spiele:

- TicTacToe  
  In 3x3 Felder wird abwechselnd ein Symbol eingetragen. Ziel: 3 in einer Reihe.
- Sokoban  
  Objekte durch ein Labyrinth schieben.
- Connect4  
  4 Gewinnt

### Serielle Schnittstelle

    9.11.2007:

    - serial console:
    115200 baud, 8N1, no handshake

    - serial commands:
    0 - backlight off
    1 - dimmed backlight
    2 - full backlight
    . - prints "HELO"
    S - prints RCA_Encode status (hex value)
    I - prints irIRQ status (hex value)
    K - prints keyIRQ status (hex value)
    all other inputs are echoed

<!-- forum-links:start -->
## Forumsdiskussionen: Makros und Tastenbelegung

Ergänzung zu den Boop-Features: Makros (mehrere Codes pro Taste) und wechselnde Tastenbelegungen.

### Boop: Makros und wechselnde Tastenbelegungen

- [Kann Boop Makros? Kann Boop sich abwechselde Tastenbelegungen?](https://github.com/ghenne/betty-forum/blob/main/topics/0255-kann-boop-makros-kann-boop-sich-abwechselde-tastenbelegungen.md) — Makros und wechselnde Tastenbelegungen in Boop.

### Boop: Fernbedienung anlernen

- [Boop: Fernbedienung anlernen](https://github.com/ghenne/betty-forum/blob/main/topics/0162-boop-fernbedienung-anlernen.md) — IR-Signale aufzeichnen/wiedergeben und fremde Fernbedienungen an Boop anlernen.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

