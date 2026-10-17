---
title: "betty initialisierung"
topic_id: 36
board: "Software"
board_id: 6
posts: 4
first_post: "22. Aug 2007, 22:29"
last_post: "23. Aug 2007, 18:31"
authors: ["Colibri", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=36.0"
---

# betty initialisierung

[← Software](../boards/06-software.md) · Thema 36 · 4 Beiträge · 22. Aug 2007, 22:29 – 23. Aug 2007, 18:31

Beteiligt: Colibri, netguy

---

<a id="msg230"></a>

## 1. netguy · 22. Aug 2007, 22:29

hallo alle zusammen,

um die wartezeit, bis meine betties ankommen, zu ueberbruecken,
habe ich mich mal ein wenig mit der original firmware beschaeftigt.

es geht mir dabei nicht darum, das teil zum betrug zu gebrauchen,
sondern die hardware anzusprechen, z.b. das lc-display.

wie sieht das hier mit dem posten von langen disassembler-listings aus?

bisher habe ich die lcd-init routine gefunden (benutzt bank#1, adressen
0x81000000 fuer command, 0x81000001 fuer daten), das setup der pll
und der speicherbaenke.

das naechste was ich enteckt habe scheint die i/o port initialisierung der
tasten und des i/r interfaces zu sein, bin aber noch nicht ganz sicher.

im grundzustand ist flash#2 leer, es wird lediglich als datenspeicher
benutzt, z.b. fuer benutzerdaten, software-updates, etc....

ein smartcard chip haengt an uart#1, das wird sicher noch interresant.

wuerde die assembler-ausschnitte hier gerne posten, wenn moeglich.

schoene gruesse,

netguy

[Permalink](http://bettyhacks.com/forum/index.php?topic=36.msg230#msg230)

---

<a id="msg231"></a>

## 2. netguy · 23. Aug 2007, 11:32

hallo,

hier mal der zusammengesammelte init-code der betty:

[http://bettyhacks.com/wiki/index.php/Betty_init](../../pages/Betty%20init.md)

er enthaelt die pll initialisierung (40 mhz, bei 10mhz ext. quarz),
speicherbank-konfiguration (bank0, 1 und 2) sowie den init
fuer das dsiplay incl. loeschen des displays.

es ist wol _kein_ uc1610, zumindest passen die init codes nicht
wirklich zum datenblatt des chips.....

viel spass, happy hacking,

netguy

[Permalink](http://bettyhacks.com/forum/index.php?topic=36.msg231#msg231)

---

<a id="msg232"></a>

## 3. Colibri · 23. Aug 2007, 17:49

@netguy

Ich habe mal drübergeschaut. Ich komme auf eine CPU-Freq von 30 MHz (statt 40 MHz).
Table 30: PLL Multiplier values:
MSEL Bits (PLLCFG bits [4:0]) = 00010 => Value of M = 3
FOSC (10 MHz) * M (3) = CCLK (30 MHz)

Die Peripheral-Freq ist dann laut dem Defaultwert in Tabelle 35 (VPBDIV), der in der init Funktion nicht geändert wird, ein Viertel der CPU-Freq also 7,5 MHz.

U0DLL wird bei 800006C8 mit 4 initialisiert, die Baudrate ist demnach 115200 Bit/s (Formel auf Seite 115). Ein Gegencheck mit dem Hyperterminal war erfolgreich.

Die Befehl in der Pause Funktion bei 80000C1C multipliziert mit 2 statt mit 8 (R3 enthält 1)
`CS0:80000C1C                 MOV     R0, R0,LSL R3  -> 24000*8 = 192000`

Insgesammt wird R0 mit 750 multipliziert. Bei der Peripheral-Freq von 7,5 MHz ergibt sich z.B. bei dem Übergabewert 0x64 (=100 dez.) eine Wartezeit von 10 mS.

Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=36.msg232#msg232)

---

<a id="msg233"></a>

## 4. netguy · 23. Aug 2007, 18:31

hallo colibri,

> **Zitat von: Colibri am 23. Aug 2007, 17:49**
>
> @netguy
>
> Ich habe mal drübergeschaut. Ich komme auf eine CPU-Freq von 30 MHz (statt 40 MHz).
> Table 30: PLL Multiplier values:
> MSEL Bits (PLLCFG bits [4:0]) = 00010 => Value of M = 3
> FOSC (10 MHz) * M (3) = CCLK (30 MHz)
>
> <...snip...>

stimmt, mein fehler muss mich ja auch erst mal in den chip einarbeiten ....
danke fuer die richtigstellung!

> **Zitat von: Colibri am 23. Aug 2007, 17:49**
>
> Die Befehl in der Pause Funktion bei 80000C1C multipliziert mit 2 statt mit 8 (R3 enthält 1)
> `CS0:80000C1C                 MOV     R0, R0,LSL R3  -> 24000*8 = 192000`
>
> Insgesammt wird R0 mit 750 multipliziert. Bei der Peripheral-Freq von 7,5 MHz ergibt sich z.B. bei dem Übergabewert 0x64 (=100 dez.) eine Wartezeit von 10 mS.
>
> Colibri

haha, auch richtig, ich habe irgendwie #3 anstelle R3 gelesen .... naja, was will man nach 3 tagen assembler listings auch erwarten 8-}

gruss,

netguy

[Permalink](http://bettyhacks.com/forum/index.php?topic=36.msg233#msg233)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
