---
title: "Freie Pins, SPI, SD / MMC"
topic_id: 246
board: "Hardware"
board_id: 5
posts: 3
first_post: "11. November 2010, 15:50"
last_post: "11. November 2010, 22:00"
authors: ["Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=246.0"
---

# Freie Pins, SPI, SD / MMC

[← Hardware](../boards/05-hardware.md) · Thema 246 · 3 Beiträge · 11. November 2010, 15:50 – 11. November 2010, 22:00

Beteiligt: Telekatz, eme

---

<a id="msg1714"></a>

## 1. eme · 11. November 2010, 15:50

Erstmal nur zum Ideen sammeln..

PCSquirrel hatte sich ja freundlicherweise damals die Mühe gemacht, eine Tabelle mit den LPC-Pins anzulegen:
[http://bettyhacks.com/wiki/index.php/LPC2220_Pin-Belegung](../../pages/LPC2220%20Pin-Belegung.md)
[http://bettyhacks.com/forum/index.php?topic=140.0](0140-lpc2220-pin-belegung.md)

Hier nochmal das LPC2220 Datenblatt
[http://www.keil.com/dd/docs/datashts/philips/lpc2210_2220.pdf](https://web.archive.org/web/2012/http://www.keil.com/dd/docs/datashts/philips/lpc2210_2220.pdf)

AN10406
Accessing SD/MMC card using SPI on LPC2000
[http://ics.nxp.com/support/documents/microcontrollers/pdf/an10406.pdf](https://web.archive.org/web/2012/http://ics.nxp.com/support/documents/microcontrollers/pdf/an10406.pdf)

Basierend auf
FatFs Generic File System Module
[http://elm-chan.org/fsw/ff/00index_e.html](https://web.archive.org/web/2012/http://elm-chan.org/fsw/ff/00index_e.html)

hat Martin Thomas etwas für ARM gebastelt
ChaN's FAT-Module and NXP LPC2000 using SPI(SSP)
[http://www.siwawi.arubi.uni-kl.de/avr_projects/arm_projects/arm_memcards/index.html#chanfat_lpc2k_spi](https://web.archive.org/web/2012/http://www.siwawi.arubi.uni-kl.de/avr_projects/arm_projects/arm_memcards/index.html#chanfat_lpc2k_spi)

Man könnte die Hintergrundbeleuchtung evtl. auf einen anderen Pin legen und ggf. auf PWM verzichten, damit SCK0 für SPI0 frei wird. Die Pins MISO0 und MOSI0 sind laut Tabelle evtl. nicht belegt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=246.msg1714#msg1714)

---

<a id="msg1715"></a>

## 2. Telekatz · 11. November 2010, 18:07

Die Pins für SPI0 sind alle schon belegt. P0.5 (MISO0) für die Erkennung der Hardwareversion der Betty (unwichtig) und P0.6 (MOSI0) für SOUND ON.

Aber man könnte auch SPI1 dafür benutzen. Man braucht ja nur einen freien Pin für CS.

Wofür brauchst du denn so viel Speicherkapazität auf der Betty?

[Permalink](http://bettyhacks.com/forum/index.php?topic=246.msg1715#msg1715)

---

<a id="msg1716"></a>

## 3. eme · 11. November 2010, 22:00

Betty als Fernbedienung braucht natürlich keine SD Karte. Aber es gäbe einen Datenlogger ab. Insbesondere, wenn man ans SPI auch ein 868 MHz Funkmodul anklemmt.. ;-) Oder serielle Daten.

Ich habe die Tabelle im Wiki aktualisiert - weißt du noch mehr über die Belegung?

[Permalink](http://bettyhacks.com/forum/index.php?topic=246.msg1716#msg1716)

---

## Verwandte Themen

- [LPC2220 Pin-Belegung](0140-lpc2220-pin-belegung.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
