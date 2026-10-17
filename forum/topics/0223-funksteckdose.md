---
title: "Funksteckdose"
topic_id: 223
board: "Software"
board_id: 6
posts: 13
first_post: "05. Dez 2009, 01:53"
last_post: "11. Jul 2011, 07:49"
authors: ["RandD", "Telekatz", "eme", "jannis", "tugstugi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=223.0"
---

# Funksteckdose

[← Software](../boards/06-software.md) · Thema 223 · 13 Beiträge · 05. Dez 2009, 01:53 – 11. Jul 2011, 07:49

Beteiligt: RandD, Telekatz, eme, jannis, tugstugi

---

<a id="msg1515"></a>

## 1. tugstugi · 05. Dez 2009, 01:53

Hi alle,

ich habe vor ein Paar Tagen ein Intertechno Funksteckdosenset gekauft. Da die meisten Funksteckdosen mit 434 Mhz funken, wollte ich mit Betty meine Funksteckdose steuern. CC1100 soll ja laut Datenblatt OOK/ASK unterstützen.

Hat jemand das ausprobiert? Im Internet finde ich leider keine Informationen zu diesem Thema. Bis jetzt habe ich einbischen mit CC1100 Konfigurationen rumgespielt und Betty so konfiguriert, dass man auf GDO0 High (carrier sense) bekommt, wenn die Funksteckdosen-Fernbedienung was sendet. GDO2 habe ich als "serial transparent data output" konfiguriert, aber lese da nur Rauschen.

Hier ist meine CC1100 Konfiguration (habe mit TI SmartRF Studio erzeugt):
 `const unsigned char conf[0x2F] = {
  0x0D, //IOCFG2 ---- GDO2 als serial transparent data output
  0x2E, //IOCFG1 ---- default
  0x0E, //IOCFG0 ---- GDO0 als carrier sense (Frage: sollte man nicht irgendwo ein Threshold konfigurieren?)
  0x07, //FIFOTHR ---- nicht benutzt
  0xD3, //SYNC1 ---- nicht benutzt
  0x91, //SYNC0 ---- nicht benutzt
  0x3E, //PKTLEN ---- nicht benutzt
  0x04, //PKTCTRL1 ---- ?
  0x32, //PKTCTRL0 ---- asynchronous transparent mode
  0x00, //ADDR ---- nicht benutzt
  0x00, //CHANNR ---- nicht benutzt
  0x06, //FSCTRL1
  0x00, //FSCTRL0
  0x10, //FREQ2
  0x12, //FREQ1
  0xF6, //FREQ0
  0xF5, //MDMCFG4
  0x75, //MDMCFG3
  0x30, //MDMCFG2 ---- ASK/OOK,  no preamble/sync, carrier sense
  0x22, //MDMCFG1
  0xF8, //MDMCFG0
  0x14, //DEVIATN  ---- nicht benutzt
  0x07, //MCSM2
  0x30, //MCSM1
  0x18, //MCSM0
  0x14, //FOCCFG
  0x6C, //BSCFG
  0x03, //AGCCTRL2 // siehe Design Note DN022
  0x00, //AGCCTRL1 // siehe Design Note DN022
  0x91, //AGCCTRL0 // siehe Design Note DN022
  0x46, //WOREVT1
  0x50, //WOREVT0
  0x78, //WORCTRL
  0x56, //FREND1 // siehe Design Note DN022
  0x11, //FREND0
  0xE9, //FSCAL3
  0x2A, //FSCAL2
  0x00, //FSCAL1
  0x1F, //FSCAL0
  0x41, //RCCTRL1
  0x00, //RCCTRL0
  0x59, //FSTEST
  0x7F, //PTEST
  0x3F, //AGCTEST
  0x81, //TEST2
  0x35, //TEST1 // siehe Design Note DN022
  0x09 //TEST0
  };`

Kennt jemand mit der CC1100 Konfiguration aus?

Gruß
Tuguldur

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1515#msg1515)

---

<a id="msg1517"></a>

## 2. Telekatz · 07. Dez 2009, 09:39

Ausprobiert hab ich das noch nicht, hab's aber noch vor der Betty das FS20 Protokoll beizubringen. Im Prinzip ähnlich deinem Problem.

Informationen zum Protokoll deine Funksteckdose findest du hier [http://www.mikrocontroller.net/topic/124084](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/124084)

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1517#msg1517)

---

<a id="msg1518"></a>

## 3. tugstugi · 07. Dez 2009, 10:54

> **Zitat von: Telekatz am 07. Dez 2009, 09:39**
>
> Ausprobiert hab ich das noch nicht, hab's aber noch vor der Betty das FS20 Protokoll beizubringen. Im Prinzip ähnlich deinem Problem.
>
> Informationen zum Protokoll deine Funksteckdose findest du hier [http://www.mikrocontroller.net/topic/124084](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/124084)

Hallo Telekatz,

Ich kenn den Link, danke trotzdem.

Ich habe jetzt die Baudrate auf 2,4Kbaud erhöht und die Filterbandwidth auch einbischen hochgeschraubt. Mittlerweile kann ich die Bits einigermassen richtig empfangen. Aber es gibt immer wieder Ausreißer ->  Pulsen mit mehr als 3*360 Mikrosekunden Länge.

Hier ist meine aktuelle Konfiguration:
 `unsigned char patable[8] = {0x00, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

const unsigned char conf[0x2F] = {
  0x0D, //IOCFG2
  0x2E, //IOCFG1
  0x0E, //IOCFG0
  0x07, //FIFOTHR
  0xD3, //SYNC1
  0x91, //SYNC0
  0x3E, //PKTLEN
  0x04, //PKTCTRL1
  0x32, //PKTCTRL0
  0x00, //ADDR
  0x00, //CHANNR
  0x06, //FSCTRL1
  0x00, //FSCTRL0
  0x10, //FREQ2
  0x12, //FREQ1
  0xF6, //FREQ0
  0xC6, //MDMCFG4
  0x75, //MDMCFG3
  0x30, //MDMCFG2
  0x22, //MDMCFG1
  0xF8, //MDMCFG0
  0x14, //DEVIATN
  0x07, //MCSM2
  0x30, //MCSM1
  0x18, //MCSM0
  0x14, //FOCCFG
  0x6C, //BSCFG
  0x03, //AGCCTRL2
  0x00, //AGCCTRL1
  0x91, //AGCCTRL0
  0x46, //WOREVT1
  0x50, //WOREVT0
  0x78, //WORCTRL
  0x56, //FREND1
  0x11, //FREND0
  0xE9, //FSCAL3
  0x2A, //FSCAL2
  0x00, //FSCAL1
  0x1F, //FSCAL0
  0x41, //RCCTRL1
  0x00, //RCCTRL0
  0x59, //FSTEST
  0x7F, //PTEST
  0x3F, //AGCTEST
  0x81, //TEST2
  0x35, //TEST1
  0x09 //TEST0
  };`

Weiss jemand, woran diese Ausreißer liegen könnten?

Gruß
Tuguldur

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1518#msg1518)

---

<a id="msg1519"></a>

## 4. Telekatz · 07. Dez 2009, 11:54

Stell die Baudrate auf 2,778kBaud ein (entspricht 360µs).

Wie liest du das Signal aus?

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1519#msg1519)

---

<a id="msg1521"></a>

## 5. tugstugi · 07. Dez 2009, 15:02

> **Zitat von: Telekatz am 07. Dez 2009, 11:54**
>
> Stell die Baudrate auf 2,778kBaud ein (entspricht 360µs).
>
> Wie liest du das Signal aus?

Wenn der Pin GDO0 High (carrier sense) ist, prüfe ich den Pin GD02 mit 50 mikrosekunden periodisch, ob der Pin High oder Low ist. Ich war einbischen faul, mit Interrupt zu arbeiten.

Gruß
Tuguldur

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1521#msg1521)

---

<a id="msg1523"></a>

## 6. tugstugi · 08. Dez 2009, 02:02

Empfangen funktioniert jetzt.

Für ASK/OOK muss man laut Design Note DN022 ([http://focus.ti.com/lit/an/swra215b/swra215b.pdf)](https://web.archive.org/web/2012/http://focus.ti.com/lit/an/swra215b/swra215b.pdf)) alle möglichen Kombinationen von AGCCTRL2 und AGCCTRL0 ausprobien. Mit AGCCTRL2=0x03 und AGCCTRL2=0x92 funktioniert das Empfangen einigermassen gut.

Gruß
Tuguldur

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1523#msg1523)

---

<a id="msg1542"></a>

## 7. Telekatz · 16. Dez 2009, 23:02

Funksteckdosen können jetzt auch bedient werden. Hab dazu den LIRC Encoder entsprechend erweitert.

Im Code ist ein Beispiel für FS20 und für die von dir verwendeten Funksteckdosen enthalten.
Die Reichweite ist allerdings bei FS20 aufgrund der dafür ungeeigneten Antennenbeschaltung stark eingeschränkt.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1542#msg1542)

---

<a id="msg1543"></a>

## 8. tugstugi · 16. Dez 2009, 23:40

> **Zitat von: Telekatz am 16. Dez 2009, 23:02**
>
> Im Code ist ein Beispiel für FS20 und für die von dir verwendeten Funksteckdosen enthalten.

Hi,

ich sehe in SVN nur fs20.c und fs20.h.

Gruß
Tuguldur

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1543#msg1543)

---

<a id="msg1545"></a>

## 9. Telekatz · 17. Dez 2009, 09:25

Das Senden geht über den LIRC Encoder. Für die Funksteckdosen gibt es desshalb ein entsprechendes LIRC Confi File im Ordner  boopfirmware/boop/trunk/infrared/ir_codes/lirc.

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1545#msg1545)

---

<a id="msg1672"></a>

## 10. eme · 04. Okt 2010, 22:14

Hallo Telekatz,

ich versuche gerade eine "LIRC" Config für die REV 008340 Fernbedienung mit HS2260A-R4 zu erstellen.
Leider reagiert die Steckdose nicht..
`/*
    RF codes for REV 008340 remote control HS2260A-R4
    based on hx2262 by telekatz
    2010-10-04 by eme

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

// Bit translation:
// HX2262     LIRC_RF
// 0       00
// F (floating)  01
// 1       11

// "channel" (A0-A3)
// A: 1FFF -> 11010101 -> 0xD5
// B: F1FF -> 01110101 -> 0x75
// C: FF1F -> 01011101 -> 0x5D
// D: FFF1 -> 01010111 -> 0x57

// "device" (A4-A7)
// 1: 1FF0 -> 11010100 -> 0xD4
// 2: F1F0 -> 01110100 -> 0x74
// 3: FFF1 -> 01010111 -> 0x57

// "action" (D3-D0)
// 1: 0010 (on/+)  -> 00001100 -> 0x0C
// 0: 0001 (off/-) -> 00000011 -> 0x03

/*pre_data*/    0xD5,      // A0-A3
/*post_data*/    0x00,
/*toggle_bit_mask*/ 0x00,
/*gap*/       58280,
/*repeat_gap*/   58280,     // gap after min_repeats
/*bits*/      16,       // data bits
/*pre_data_bits*/  8,
/*post_data_bits*/ 0,
/*rc6_bit*/     0,
/*frequency*/    0x00101234,   // 433,919861MHz
/*flags*/      LIRC_RF,
/*header*/     0,0,
/*three*/      0,0,
/*two*/       0,0,
/*one*/       1410,470,
/*zero*/      470,1410,
/*plead*/      0,
/*ptrail*/     470,      // sync pulse
/*foot*/      0,0,
/*pre*/       0,0,
/*post*/      0,0,
/*repeat*/     0,0,
/*min_repeat*/   10,
/*duty cycle*/   0,

{
 0x0000, // A   ->
 0x0000, // B   ->
 0x0000, // C   ->
 0x0000, // D   ->
 0x0000, // Betty ->
 0x0000, // Exit  ->
 0x0000, // Up   ->
 0x0000, // Down  ->
 0x0000, // Left  ->
 0x0000, // Right ->
 0x0000, // OK   ->
 0x0000, // Vol+  ->
 0x0000, // Vol-  ->
 0x0000, // Mute  ->
 0x0000, // Prog+ ->
 0x0000, // Prog- ->
 0xD40C, // 1   -> 1 on
 0xD403, // 2   -> 1 off
 0x0000, // 3   ->
 0x740C, // 4   -> dim2 +
 0x7403, // 5   -> dim2 -
 0x0000, // 6   ->
 0x570C, // 7   -> dim3 +
 0x5703, // 8   -> dim3 -
 0x0000, // 9   ->
 0x0000, // 0   ->
 0x0000, // -/--  ->
 0x0000, // AV   ->
 0x0000, // Menu  ->
 0x0000, // PiP  ->
 0x0000, // A/B  ->
 0x0000, // 16:9  ->
 0x0000, // Info  ->
 0x0000, // VTX1  ->
 0x0000, // VTX2  ->
 0x0000, // VTX3  ->
 0x0000, // Blue  ->
 0x0000, // Yello ->
 0x0000, // Green ->
 0x0000, // Red  ->
 0x0000, // TV   ->
 0x0000  // Power ->
},`

Ein Puls hat beim Original 470 µs. Es werden 12 Bits plus Synch am Ende gesendet.
Leider hat die Steckdose anscheinend keinen Ausgang für das demodulierte Signal und auch sonst fällt mir nicht ein, wie ich das Gesendete prüfen kann. Vielleicht fällt dir ja so schon auf, wo das Problem liegen könnte. Danke.

*Last Edit : 04. Okt 2010, 23:07 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1672#msg1672)

---

<a id="msg1673"></a>

## 11. eme · 04. Okt 2010, 22:51

Ah, hab's. Check ich bei Gelegenheit mal ein..

.. und danke für die Funktionalität!

*Last Edit : 04. Okt 2010, 22:58 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1673#msg1673)

---

<a id="msg1937"></a>

## 12. jannis · 06. Jul 2011, 17:14

Welche Funksteckdosen soll ich mir kaufen, damit das hier möglichst gut unterstützt wird? Bei Pollin sehe ich z.B. Funk-Steckdosen-Set 2605[1] und Funksteckdosen/Funkdimmer-Set GT-FSI [2].

Würde dimmen auch funktionieren?

Wäre es einfach diese codecs auch außerhalb von lirc zu verwenden? Ich würde das gerne in die McBetty[3] integrieren. Was haltet ihr davon?

[1] [http://www.pollin.de/shop/dt/MzMzOTQ0OTk-/Haustechnik/Installationsmaterial/Schalter_Steckdosen/Funk_Steckdosen_Set_2605.html](https://web.archive.org/web/2012/http://www.pollin.de/shop/dt/MzMzOTQ0OTk-/Haustechnik/Installationsmaterial/Schalter_Steckdosen/Funk_Steckdosen_Set_2605.html)
[2] [http://www.pollin.de/shop/dt/MTgxOTQ0OTk-/Haustechnik/Installationsmaterial/Schalter_Steckdosen/Funksteckdosen_Funkdimmer_Set_GT_FSI.html](https://web.archive.org/web/2012/http://www.pollin.de/shop/dt/MTgxOTQ0OTk-/Haustechnik/Installationsmaterial/Schalter_Steckdosen/Funksteckdosen_Funkdimmer_Set_GT_FSI.html)
[3]http://www.ewetel.net/~horst.raap/

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1937#msg1937)

---

<a id="msg1938"></a>

## 13. RandD · 11. Jul 2011, 07:49

Hallo,

also das Dimmerset ist ausverkauft

Dann wohl das andere, ich habe für den gleichen Preis (9,95 €) beim nächsten Toom Baumarkt 4 Funksteckdosen erstanden.

Gleichen denen auf dem Produktbild von Pollin bis ins kleinste Detail.

Grüßle

[Permalink](http://bettyhacks.com/forum/index.php?topic=223.msg1938#msg1938)

---

## Verwandte Themen

- [Funksteckdosen](0086-funksteckdosen.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
