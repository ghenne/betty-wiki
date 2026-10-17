# Baudraten

Bei einer Peripherie-Frequenz von 7.5 MHz (Standard in der Betty) kann man folgende Tabelle zur Baudratenfestlegung nutzen:

    Baudrate      DLL        DLM      MulVal    DivAddVal    Tats.Baud Fehler %
    115200          3        0        14         5           115131    0.06
     57600          6        0        14         5            57565    0.06
     38400          5        0         9        13            38352    0.12
     19200         11        0         9        11            19176    0.25
      9600         23        0         8         9             9590    0.10
      4800         90        0        12         1             4807    0.14
      2400        180        0        12         1             2403    0.12
      1200        130        0         7        14             1201    0.08
       600        156        0         1         4              600    0
       300        184        0         2        15              299    0.02
       150        195        0         1        15              150    0
        75        161        1         1        14               75    0

Die Originalfirmware verwendet 115200 baud.

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

