---
title: "erweiterung der betty hardware / freie GPIOs"
topic_id: 278
board: "Hardware"
board_id: 5
posts: 4
first_post: "04. Jan 2012, 07:02"
last_post: "21. Feb 2012, 03:36"
authors: ["Flunder", "famos", "r00t"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=278.0"
---

# erweiterung der betty hardware / freie GPIOs

[← Hardware](../boards/05-hardware.md) · Thema 278 · 4 Beiträge · 04. Jan 2012, 07:02 – 21. Feb 2012, 03:36

Beteiligt: Flunder, famos, r00t

---

<a id="msg1999"></a>

## 1. r00t · 04. Jan 2012, 07:02

(edit: es gibt hier schon einen thread zur sd-karten anbindung: [http://bettyhacks.com/forum/index.php?topic=246.0](0246-freie-pins-spi-sd-mmc.md) )
(edit: die idee mit dem ENC28J60 ist auch nicht neu: [http://bettyhacks.com/forum/index.php?topic=182.msg1236#msg1236](0182-tae-adapter-programmieradapter-fuer-msp430.md#msg1236) )

hat sich schonmal jemand damit beschaeftigt, zusaetzliche interne peripherie an die betty anzuschliessen?
bzw was fuer freie ports/GPIO-pins es dafuer gibt? (GPIO = general purpose input output).
und ggfs testpunkte, an denen man diese einfach abgreifen kann? (loeten an den pins des LPC2220 duerfte nicht jedermann's sache sein.)

ein paar ideen:
* ein i2c eeprom als datenspeicher, solange der zugriff auf den eigentlich verwendeten smartcard-chip wohl eh nicht klappt?
* was soll der geiz, gleich einen sd-karten (spi geraet) slot
* i2c port-expander um zusaetzliche IOs zu bekommen
* ein RFM12 funkmodul (spi-geraet) (ist denke ich einfacher einzubauen, als den vorhandenen funk-chip umzubauen, zB fuer funksteckdosen)
* ein ENC28J60 Ethernet controller (spi-geraet), wuede aus einer betty einen ethernet<->rf gateway machen! (fertige "netzwerkkarten" kosten 5eur bei ebay) das waehre eine gute altenative zum nicht verfuegbaren ip-adapter... (man koennte auch den scart oder tae adapter umbauen, aber ich denke der prozessor in der betty ist dafuer praktischer, da er bequem einen IP-stack ausfuehren koennen sollte.)
* ...

ich fand' es etwas erschreckend zu lesen, dass zB bettycheck einen teil der tastatur opfert, um einen eingang fuer das oszilloskop zu bekommen?! der LPC2220 hat soeviele pins, da sollte doch was besseres moeglich sein...

hier mal zu den moeglichkeiten die ich per blick auf das datenblatt ([http://bettyhacks.com/wiki/index.php/Betty-Hardware)](https://web.archive.org/web/2012/http://bettyhacks.com/wiki/index.php/Betty-Hardware)) und [http://bettyhacks.com/wiki/index.php/LPC2220_Pin-Belegung](../../pages/LPC2220%20Pin-Belegung.md) sehe:
* die jtag-leitungen sind sogar bequem am programmieranschluss verfuegbar - die sind lt. datenblatt wohl auch als GPIOs (teil von port 1) verwendbar?
* unter "Unbenutzte Pins / nicht erfasste Pins" finden sich auch noch etliche GPIOs, waehre zu klaren ob die wirklich frei/benutzbar sind.
* am i2c-bus haengt die RTC, man sollte problemlos weitere i2c-geraete anschliessen koennen
* der LPC2220 hat zwei uarts
  * der eine wird fuer die programmierung/konsole verwendet
  * am anderen haengt der eh nicht verwendete smartcard-controller?
* der LPC2220 hat zwei SPI interfaces.
  * das erste (MISO0/MOSI0/SCK0) ist von backlight/hardwareerkennung/sound belegt - die sollte man auch umlegen koennen
  * am zweiten (SCK1/MISO1/MOSI1) ist das funkmodul angeschlossen. man muesste nurnoch einen freien GPIO als chip-select findet, koennte man hier weitere SPI-geraete anschliessen.
* ...

*Last Edit : 04. Jan 2012, 07:40 by r00t*

[Permalink](http://bettyhacks.com/forum/index.php?topic=278.msg1999#msg1999)

---

<a id="msg2001"></a>

## 2. Flunder · 05. Jan 2012, 21:16

> **Zitat von: r00t am 04. Jan 2012, 07:02**
>
> * ein i2c eeprom als datenspeicher, solange der zugriff auf den eigentlich verwendeten smartcard-chip wohl eh nicht klappt?

Wie ich [hier](https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=39.msg1985#msg1985) geschrieben habe, habe ich die Kommunikation doch noch hinbekommen und konnte Daten speichern und auslesen. Nur sind halt die Zugriffszeiten deutlich länger als bei einer SPI/I2C-Schnittstelle.

Gruß Volkmar

[Permalink](http://bettyhacks.com/forum/index.php?topic=278.msg2001#msg2001)

---

<a id="msg2004"></a>

## 3. famos · 14. Feb 2012, 21:50

Hallo r00t,

der LPC 2220 hat schon viele Pins, aber der Grossteil davon geht für Speisung und den Daten-/Address BUS drauf. Freie I/O's sind da praktisch keine mehr. Ein analoges Signal kann auch nicht mit jedem Pin erfasst werden. Das ist der Grund warum man dafür Leitungen von der Tastatur abklemmen muss.

Was sicher interessant ist, wäre mal eine ISA Netzwerkkarte wie eine NE2000 oder eine 3C509 (ev. CS8900) an den Bus zu hängen. Genügend Addressspace wäre vorhanden. Beispiele für die NE2000 und 3C509 Karten gibt es auch: [http://jalethernet.sourceforge.net/soft.html](https://web.archive.org/web/2012/http://jalethernet.sourceforge.net/soft.html) resp. [http://www.hamradio.cz/aprs/dalsi/Pic3Com/index_en.htm.](https://web.archive.org/web/2012/http://www.hamradio.cz/aprs/dalsi/Pic3Com/index_en.htm.)

Gruss
famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=278.msg2004#msg2004)

---

<a id="msg2008"></a>

## 4. r00t · 21. Feb 2012, 03:36

> **Zitat von: famos am 14. Feb 2012, 21:50**
>
> der LPC 2220 hat schon viele Pins, aber der Grossteil davon geht für Speisung und den Daten-/Address BUS drauf. Freie I/O's sind da praktisch keine mehr.

naja, bei sovielen sollte irgendwo was freizuschaufeln sein,
wie erwaehnt bieten sich zB die jtag-pins an, wenn man jtag nicht benutzt. (muesste nochmal im datenblatt lesen, ob es da einschraenkungen gibt.)
und unter [http://bettyhacks.com/wiki/index.php/LPC2220_Pin-Belegung#Unbenutzte_Pins_.2F_nicht_erfasste_Pins](../../pages/LPC2220%20Pin-Belegung.md#unbenutzte-pins--nicht-erfasste-pins) stehen ja noch einige kandidaten, die man mal nachpruefen muesste/koennte.

> **Zitat von: famos am 14. Feb 2012, 21:50**
>
> Ein analoges Signal kann auch nicht mit jedem Pin erfasst werden. Das ist der Grund warum man dafür Leitungen von der Tastatur abklemmen muss.

das nicht jeder pin alle features bietet ist klar, aber man koennte die tastatur dann ja zB woanders anschliessen.

> **Zitat von: famos am 14. Feb 2012, 21:50**
>
> Was sicher interessant ist, wäre mal eine ISA Netzwerkkarte wie eine NE2000 oder eine 3C509 (ev. CS8900) an den Bus zu hängen.

sicher eine nette idee, aber zeige uns erstmal bitte wie du die ganzen dafuer benoetigten leitungen in einer betty verdrahtet hast, dann koennen wir das weiter diskutieren
(was schon eher realistisch waehre, waehre ein latch an den bus zu klemmen, um weitere IOs zu bekommen.)

[Permalink](http://bettyhacks.com/forum/index.php?topic=278.msg2008#msg2008)

---

## Verwandte Themen

- [Freie Pins, SPI, SD / MMC](0246-freie-pins-spi-sd-mmc.md)
- [TAE Adapter - Programmieradapter für MSP430](0182-tae-adapter-programmieradapter-fuer-msp430.md)
- [Umbau auf 868 MHz](0247-umbau-auf-868-mhz.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
