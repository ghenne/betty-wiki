# Simple Serial Interface

## Simple Serial Interface **V2**

Es gibt eine Neuauflage des Simple Serial Interface als **V2**, welche das [LPCTool](LPCTool.md "LPCTool") komplett unterstüzt (automatisches Setzen von EINT und RESET) in bekannter simpler Art und Weise. Jedoch habe ich in der Schaltung Wert darauf gelegt, dass weder der COM-Port, noch die angeschlossene Schaltung geschädigt werden kann. Zusätzlich zu den 2 Transistoren braucht man daher noch 2 Dioden und einen Widerstand. Ich empfehle euch in eurem eigenem Interesse die paar Cent mehr auszugeben.

BITTE BEACHTET DIE DISKUSSIONSSEITE. Bei diesem Interface fehlen Basisvorwiderstände für die Transistoren, ausserdem passt das Betty-Interface nicht mit der Pinleiste.

Im \[[Forum](https://github.com/ghenne/betty-forum)\] gibt es \[[Fotos](https://github.com/ghenne/betty-forum/blob/main/topics/0108-bilder-simple-serial-interface-v2.md#msg828)\]

  

### Stückliste

|  |  |  |  |
|----|----|----|----|
| Stück | Bezeichnung | Conrad | Reichelt.de |
| 1 | Euro-Platine 50x90mm Streifenraster | 527629 | H25SR050 |
| 1 | Maxim MAX 3232 CPE | 167108 | MAX 3232 CPE |
| 4 | Kondensator 1µF (Kondensatoren **C1-C4** - z.B. Keramik, bipolar) | 453382 | RAD 1/63 \*\* |
| 1 | Kondensator 100nF (0,1µF) (Kondensator **C5** - z.B. Keramik, bipolar) | 453099 | X7R-5 100N |
| 2 | Transistor BC 547C | 154989 | BC 547C |
| 1 | Diode 1N4148 (**D3**) | 162280 | 1N 4148 |
| 1 | Z-Diode 3,3V (**D4**) | 180041 | ZF 3,3 |
| 1 | Widerstand 680 Ohm (**R1**) | 403237 | 1/4W 680 |
| 1 | SUB-D9 Fermale |  | D-SUB BU 09FB |
| 1 | Flachbandkabel |  | AWG 28-10G 3M |
| 1 | IC-Sockel 16 Polig (2x8) |  | GS 16 |

  

|  |  |
|----|----|
| [<img src="../images/c/c2/Ueberarbeiten-Gross.png" width="50" height="50" alt="Ueberarbeiten-Gross" />](Datei_Ueberarbeiten-Gross.png.md) | **Dieser Artikel oder Abschnitt muss überarbeitet werden, da der Reichelt-Warenkorb fehlerhaft ist.** |

  
Den kompletten Einkaufskorb könnt ihr bei Reichelt direkt unter folgendem Link adden. Es ist alles drinnen, was in der oberen Liste dteht: <https://secure.reichelt.de/?;ACTION=20;LA=5000;AWKID=48846;PROVID=2084> Die Kosten belaufen sich auf 8,26€.

- Die Kondensatoren von Reichelt sind POLAR also auf die Polung achten!

optional:

- 1 x Flachbandkabel 10 Polig (es reicht auch wenn man ein altes IDE kabel hat und sich da die 10 Adern herausschneidet) (Rechelt: AWG 28-10G 3M)
- 1 x IC-Sockel 16-polig, (Bitte nicht die mit eingebautem Kondensator, der sitzt immer zwischen Pin 8 und 16, was hier nicht passen würde) (Reichelt: GS16)
- 1 x SUBD Buchse, 9-polig (Reichelt: D-SUB BU 09FB (Für Flachbandkabel))

### Schaltplan und Layout

Der Schaltplan:

[<img src="../images/8/8e/Betty-Serial-V2-EAGLE.jpg" width="771" height="580" alt="Betty-Serial-V2-EAGLE" />](Datei_Betty-Serial-V2-EAGLE.jpg.md)

Das Layout für Lochstreifenraster:

[<img src="../images/7/7d/Betty-Serial-V2-Lochmaster.jpg" width="998" height="556" alt="Betty-Serial-V2-Lochmaster" />](Datei_Betty-Serial-V2-Lochmaster.jpg.md)

### Eagle Files

Die Eagle und Lochmaster-Dateien könnt ihr hier downloaden: [Simple-Serial-Interface V2 - Schaltplan und Lochraster-Layout](http://alterego.mamalala.org/tmp/betty-simple-serial-interface-v2.rar)

  

### Software

Simple Serial Interface funktioniert mit jeder gängigen Software.  

- ob es nun Terminal-Programme wie \[[TeraTerm](http://hp.vector.co.jp/authors/VA002416/ttermp23.zip)\], realterm oder minicom sind oder
- die Software die für die Betty erstellt wurden, von Netguy(mamalala), von hackbard oder von Colibri.
- wenn die Software [LPCTool](LPCTool.md "LPCTool") genutzt wird, auch mit automatischem Schalten von EINT und RESET

### Danke

Mein Dank geht an dakaos für die Liste von Conrad Bestellnummern.

  
--[Alterego](Benutzer_Alterego.md "Benutzer:Alterego") 07:26, 9 November 2007 (CET)

<!-- forum-links:start -->
## Forumsdiskussionen: Adapter, Sniffing und VT-Datenstrom

Ergänzungen zur seriellen Anbindung: TTL-Wandler, Handydatenkabel, TXD1- und Daten-Sniffing sowie die Übertragung per VT-Datenstrom.

### Daten sniffen

- [Daten Sniffen](https://github.com/ghenne/betty-forum/blob/main/topics/0225-daten-sniffen.md) — Datenverkehr mitschneiden und auswerten.

### TTL-Wandler

- [TTL-Wandler](https://github.com/ghenne/betty-forum/blob/main/topics/0029-ttl-wandler.md) — TTL-Pegelwandler für serielle Verbindungen.
- [TTL-Wandler](https://github.com/ghenne/betty-forum/blob/main/topics/0022-ttl-wandler.md) — TTL-Wandler (kurzer Thread).

### TXD1 sniffen / Datenmüll

- [TXD1 sniffen! Datenmüll ?!](https://github.com/ghenne/betty-forum/blob/main/topics/0027-txd1-sniffen-datenmuell.md) — TXD1 mitschneiden und Datenmüll analysieren.

### Handydatenkabel vs. Simple Serial Interface

- [Was ist besser? Handykabel oder Simple Seriell Interface?](https://github.com/ghenne/betty-forum/blob/main/topics/0165-was-ist-besser-handykabel-oder-simple-seriell-interface.md) — Handydatenkabel oder Simple Serial Interface: Vergleich.
- [Handydatenkabel und Betty Heaven](https://github.com/ghenne/betty-forum/blob/main/topics/0152-handydatenkabel-und-betty-heaven.md) — Handydatenkabel mit BettyHeaven nutzen.

### VT-Datenstrom zur Datenübertragung

- [VT Datenstrom zur Datenübertragung](https://github.com/ghenne/betty-forum/blob/main/topics/0082-vt-datenstrom-zur-datenuebertragung.md) — Datenübertragung über den SCART-Adapter per VT-Datenstrom.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

