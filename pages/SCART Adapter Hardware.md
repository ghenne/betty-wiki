# SCART Adapter Hardware

[<img src="../images/d/dd/Scart_bauteile_anschluesse.jpg" width="300" height="781" alt="Scart bauteile anschluesse" />](Datei_Scart%20bauteile%20anschluesse.jpg.md)

## Allgemeines

- SCART Adapter\|V1.4.1 - BSC
- UHF Sender
- Antenne
- Netzteilmodul 230V 1 Spannung DC
- SCARTAnschluss Male Female

## Netzteil

Das Netzteil der [Ladestation](Ladestation.md "Ladestation") ist aus ähnlichen Komponenten aufgebaut.

[Schaltnetzteil](http://de.wikipedia.org/wiki/Schaltnetzteil), 230 V Netzspannung! Lebensgefahr!

- Ausgangsspannung: 5 V ?
- Ausgangsleistung: (FSD200 -\> 5 W, hängt aber von den Übertragern etc. ab)

<!-- -->

- Schaltregler IC
  - Bezeichnung: FSD200 / DVG18
  - Bauform: DIP 7
  - Hersteller: fairchild
  - Status: discontinued
  - Datenblatt: <http://pdf1.alldatasheet.com/datasheet-pdf/view/83059/FAIRCHILD/FSD200.html>

<!-- -->

- Optokoppler
  - Bezeichnung: AC641 / EL817 / EVERLIGHT
  - Hersteller: everlight
  - Produktseite: <http://www.everlight.com/product_view2.php?item=180&cate_index=175&set_lang=en>
  - Datenblatt: <http://www.everlight.com/upload/product_pdf/EL817.pdf>

## Bauteile

### \[1\] PLD: Altera EPM3064A

[Datenblatt](http://www.altera.com/literature/ds/m3000a.pdf)

    max3046A Programmable Logic Device (PLD)

    Usable gates          1,250
    Macrocells            64
    Logic array blocks     4
    Maximum user I/O pins 34

    1cm x 1cm
    11 pins auf jeder seite (=44pins)

    Beschriftung
    Code:
    ALTERA
    M3064A
    44-10N
    BCB77
    0701A

### \[2\] Philips P89LPC931

[Produktseite](http://www.standardics.nxp.com/products/lpc900/all/~P89LPC931/)  
[Datenblatt](http://ics.nxp.com/products/lpc900/datasheet/p89lpc930.p89lpc931.pdf)  
[Errata](http://ics.nxp.com/support/documents/?scope=P89LPC931&type=errata)  
[User Manual](http://ics.nxp.com/support/documents/?scope=P89LPC931&type=user)  

    8-bit Microcontroller mit 80C51 Kern / 8KB 3V flash, 256-byte data RAM, I2C and SPI and UART interfaces
    Hersteller: www.nxp.com (ehem. Philips)

    1cm x 0,4 cm
    15pins auf den gegenueberliegenden seiten = 30 pins

    Beschriftung
    Code:
    P89LPC931F
    A1036600 03
    YuG0650A

Firmware: [Betty_scart](Betty%20scart.md "Betty scart")

### \[3\] Atmel626 - 24C64AN - SU27 A

[Datenblatt](http://www.alldatasheet.com/datasheet-pdf/pdf/83215/ATMEL/AT24C64AN-10SU-2.7.html)

    Serielles EEProm
    4 pins auf den gegenueberliegenden seiten = 8 pins insg.
    Code:
    ATMEL626
    24C64AN
    - SU27    A

### \[4\] LM317 -POTBL

[Datenblatt](http://www.ortodoxism.ro/datasheets/nationalsemiconductor/DS009063.PDF)

    Spannungsregler
    4 pins auf den gegenueberliegenden seiten = 8 pins insg.
    Code:
    LM317
    PNJAL

### \[5\] CC1100 - DN4309.00 - 0641

[Datenblatt](http://focus.ti.com/docs/prod/folders/print/cc1100.html)  
wie in [TAE Adapter](TAE%20Adapter%20Hardware.md "TAE Adapter Hardware") und [IP Adapter](IP%20Adapter%20Hardware.md "IP Adapter Hardware")

    5 Pins auf jeder seite = 20 pins
    Code:
    CC1100
    DN7452.00
    0705

### \[6\] Quarz AQ55.500-3

### \[7\] Quarz AQ27.000

27MHz

  

## Anschlussbelegung

### P89LPC931F

Der Anschluss ist rechts neben dem Quarz bei der Antenne

    1  RX (Der eckige Anschluss)
    2  TX
    3  P0.4 - PDA : ICP Daten (ICP = In Circuit Programming)
    4  P0.5 - PCL : ICP Takt
    5  GND
    6  nReset : ICP mode entry
    7  3,3V

### EPM3064A

    1  TDI (Der eckige Anschluss)
    2  TDO
    3  TCK
    4  TMS
    5  3,3V
    6  GND

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

