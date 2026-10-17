# IP Adapter Hardware

[<img src="../images/c/c1/Pinheader_ip_1.jpg" width="250" height="333" alt="Pinheader ip 1" />](Datei_Pinheader%20ip%201.jpg.md)

[<img src="../images/d/d2/Debug_header.jpg" width="250" height="193" alt="Debug header" />](Datei_Debug%20header.jpg.md)

  

## Bauteile

### \[1\] ASIX AX11005

[Uebersicht](http://www.asix.com.tw/products.php?op=pItemdetail&PItemID=90;72;103)  
[Datenblatt](http://www.asix.com.tw/FrootAttach/userguide/AX110xx_Product_Introduction_Rev14.pdf)

    Single Chip Microcontroller with TCP/IP and 10/100M Fast Ethernet MAC/PHY
    Features:
    512K Flash
    16GPIOs
    LQFP-80/TFBGA-80

### \[2\] CC1100 - DN4309.00 - 0641

[Datenblatt](http://focus.ti.com/docs/prod/folders/print/cc1100.html)  
wie in [SCART Adapter](SCART%20Adapter%20Hardware.md "SCART Adapter Hardware") und [TAE Adapter](TAE%20Adapter%20Hardware.md "TAE Adapter Hardware")

    5 Pins auf jeder seite = 20 pins
    Code:
    CC1100
    DN7452.00
    0705

### \[3\] Quarz AQ25.000

25MHz

### \[4\] Quarz AQ27.000

27MHz

## Anschlussbelegung

### Serieller Anschluss

    TxD0      1 2    RxD0
    xData4    3 4    Reset
    GND       5 6    VCC
    SDA       7 8    TM1GT / CEX2
    SCL       8 10   RxD2
    xData5   11 12   TxD2

### Debug Interface

              1 2    DB_DO (Pin 20)
              3 4    
    VCC       5 6    
    VCC       7 8    DB_DI (Pin 18)
    GND       8 10   RDB_CLKO

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

