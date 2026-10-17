---
title: "Was ist besser? Handykabel oder Simple Seriell Interface?"
topic_id: 165
board: "Hardware"
board_id: 5
posts: 15
first_post: "01. Nov 2008, 16:09"
last_post: "08. Nov 2008, 20:51"
authors: ["Gentoo07", "TEN", "edison", "pupsi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=165.0"
---

# Was ist besser? Handykabel oder Simple Seriell Interface?

[← Hardware](../boards/05-hardware.md) · Thema 165 · 15 Beiträge · 01. Nov 2008, 16:09 – 08. Nov 2008, 20:51

Beteiligt: Gentoo07, TEN, edison, pupsi

---

<a id="msg1135"></a>

## 1. pupsi · 01. Nov 2008, 16:09

Hi,

hab mir vor kurtzem bei Ebay 4 Betty Fernbedienungen ersteigert, da diese sau günstig sind und als Universalverbedienung echt schick! (Hab hier schon eine als Geschenk von Prosieben). Heute sind diese bei mir Angekommen. Leider musste ich feststellen, dass noch keine Neue Software drauf ist und jetzt ständig bei Betty anrufen will. Drum will ich jetzt die Software von der Betty mit neuer Software kopieren und auf die anderen bringen. Dazu braucht man erst mal ne Verbindung zum PC. Allerdings weiß ich jetzt nicht was ich nehmen soll: Entweder das Simple Seriell Interface oder doch bloß ein einfaches Handykabel. Weil wie ich das im Wiki versteh, braucht man bloß ein einfaches Handykabel mit so nem Wandler drin und bei dem Kabel braucht man dann nur noch TX mit TX und RX mit RX Verbinden oder Verstehe ich das falsch. Oder ist doch das Simple Seriell Interface besser zum Programieren? Bitte um Hilfe

MfG

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1135#msg1135)

---

<a id="msg1136"></a>

## 2. Gentoo07 · 01. Nov 2008, 17:30

Moin,

ich und mehrere Andere Leute haben mehrfach erfolgreich ihre Betty mit einem solchen Handydatenkabel programmiert, daher habe ich das mal zu einem Wiki-Eintrag zusammengefasst.

In diesem Fall sähe ich bei dem "Simple Serial Interface" keine Vorteile, da es gegenüber einem (bei mir als Rest vorhandenem Handydatenkabel) doch etwas Aufwand ist.

Allerdings gibt es eben auch schon Berichte von Leuten (2 Stück die ich gelesen habe) die es mit diesem beschriebenen Kabel nicht geschafft haben zu programmieren, was diverse Ursachen haben könnte. Entweder liefert die PC-Schnittstelle zu wenig Pegel, oder ein USB-Seriell-Wandler ist zufällig nicht geeignet, oder es ist eins der Siemens-Datenkabel mit extra Stromversorgung etc. Ob es dann mit dem "SSI" funktioniert, ist fraglich.

Wenn du das Material schon hast bau dir doch das "SSI", ansonsten würde ich es erst mit nem alten seriellen Handykabel probieren...am besten noch ganz ohne USB, direkt mit RS232 am PC-Ende.

Viel Glück!

*Last Edit : 01. Nov 2008, 17:43 by Gentoo07*

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1136#msg1136)

---

<a id="msg1137"></a>

## 3. pupsi · 01. Nov 2008, 17:45

Also ist das eigentlich egal was man nimmt. Ich hab beides im moment nicht zur hand und müsste deshalb bestellen. Also ist das vollkommen egal ob ich handykabel oder SSI nehm (Beides von den Bauteilen her gleich teuer). Löten könnt ich scho aber was bringt mir das den Scart Adapter zu Flashen? Anwendungsvorschläge wärn nett. Ach und würde ein Nokia 3310 Datenkabel funktionieren? Mein Freund hätte eins das er nicht mehr braucht.

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1137#msg1137)

---

<a id="msg1138"></a>

## 4. Gentoo07 · 01. Nov 2008, 17:56

Hi nochmal...da warst ja schnell mit dem Lesen und antworten *g*

Bei dem Scart-Adapter hatte ich gerade selbst die Interfaces verwechselt, dabei an das Kombiinterface gedacht. Daher hab ich das gerade wieder wegeditiert. Bis jetzt gäbe es eine Möglichkeit an der Betty gedrückte Tasten am Scart-Interface über eine wiederum serielle Schnittstelle auszugeben, also eher ein recht "spezieller" Nutzen.

Solange für dich beides gleich teuer wäre, bestell ruhig die Teile fürs "SSI".

Aber das Nokia 3310-Kabel müsste tatsächlich ideal passen ohne extra Stromversorgung u.s.w. , probiere es doch erstmal damit. Ein solches habe ich ebenfalls schon erfolgreich verwendet.

Gruß
Gentoo

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1138#msg1138)

---

<a id="msg1139"></a>

## 5. pupsi · 01. Nov 2008, 18:11

Na dann werd ichs mal mit dem Handykabel Versuchen. Danke für die Antworten

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1139#msg1139)

---

<a id="msg1140"></a>

## 6. pupsi · 02. Nov 2008, 10:36

Schade, das Handykabel funktioniert anscheinend nicht ich bekomm immer "RX- Timeout". Muss dann wohl oder übel den SSI baun. Naja is ja nich schwer hab aber eine Frage: bei dem Anschluss an die Betty steht ja 1 = RTS = Eint1 und 2 = RX = TX von Betty. Also muss ich dann 1 an Eint1 Anschliesen und 2 An TX von Betty Anschliesen. Muss ich GND und VCC (Wo?) auch Anschliesen? Sorry dass ich so blöd frage aber will meine Bettys nicht zerstören durch falsches verbinden

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1140#msg1140)

---

<a id="msg1141"></a>

## 7. Gentoo07 · 02. Nov 2008, 20:17

Zu dem Handydatenkabel:
Hast du auch den "EINT"-Pin mit Masse/GND verbunden, um die Betty im Bootloader-Modus zu starten? Dann auch evtl. die Batterien nochmal herausnehmen, und nach dem wieder einlegen schnell auf "Start" im BettyHeaven klicken...ansonsten weiss ich da leider auch nix weiter hilfreiches.

Zum "SSI":
![](https://web.archive.org/web/2012/http://www.grautier.com/grautier/uploads/Elektronik/Betty/RIMG0001.JPG)

Hier sind die Pins der Betty zu sehen, vom Interface müssen hier angeschlossen werden:

Interface -> Betty
1 RTS/EINT1-> Bootloader(Eint1)
2 RX -> TX
3 DTR/Reset -> Reset
4 TX -> RX
5 GND -> GND
6 VCC -> 3,3V

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1141#msg1141)

---

<a id="msg1142"></a>

## 8. pupsi · 03. Nov 2008, 13:15

> **Zitat von: Gentoo07 am 02. Nov 2008, 20:17**
>
> Zu dem Handydatenkabel:
> Hast du auch den "EINT"-Pin mit Masse/GND verbunden, um die Betty im Bootloader-Modus zu starten? Dann auch evtl. die Batterien nochmal herausnehmen, und nach dem wieder einlegen schnell auf "Start" im BettyHeaven klicken...ansonsten weiss ich da leider auch nix weiter hilfreiches.

Ja hab ich auch schon versucht aber immer "RX-Timeout"

THX fürs Erklären der Verbindung hab grad bei Conrad die Sachen bestellt hoffentlich kommen die morgen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1142#msg1142)

---

<a id="msg1143"></a>

## 9. Gentoo07 · 03. Nov 2008, 23:22

Ich will dich nicht nerven, aber das "auch schon versucht" klingt für mich wie "mal drangehalten"...

Evtl. ist das "verbinden" etwas ungenau...der Bootloader-EINT1-Pin muss am Stecker der an die Betty kommt dauerhaft an GND angeklemmt werden, nicht angetippt.

Und dann die Batterien einlegen und schnell Start klicken.

Ansonsten...Viel Glück mit dem SSI

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1143#msg1143)

---

<a id="msg1144"></a>

## 10. TEN · 04. Nov 2008, 00:03

> **Zitat von: pupsi am 03. Nov 2008, 13:15**
>
> > **Zitat von: Gentoo07 am 02. Nov 2008, 20:17**
> >
> > Zu dem Handydatenkabel:
> > Hast du auch den "EINT"-Pin mit Masse/GND verbunden, um die Betty im Bootloader-Modus zu starten? Dann auch evtl. die Batterien nochmal herausnehmen, und nach dem wieder einlegen schnell auf "Start" im BettyHeaven klicken...ansonsten weiss ich da leider auch nix weiter hilfreiches.
>
> Ja hab ich auch schon versucht aber immer "RX-Timeout"

Schau mal unter [http://vdr-portal.de/board/thread.php?postid=762022#post762022](https://web.archive.org/web/2012/http://vdr-portal.de/board/thread.php?postid=762022#post762022) - wenn der *Gurkensalat* klappt ("Read, Neo, the answers are coming..."), solltest Du vielleicht eine andere Software probieren.

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1144#msg1144)

---

<a id="msg1148"></a>

## 11. pupsi · 05. Nov 2008, 17:40

Also jetz könnt ihc mir die Haare ausreißen. Heut früh ist mein Conrad Paket angekommen und hab mich natürlich sofort an die Arbeit gemacht, dass SSI zu Baun. Allerdings bekomm ich immer nur RX Timeout! Ich hab jetzt schon den ganzen Tag nach dem Fehler gesucht aber keinen Gefunden!

Wenn einer ein funktionierendes SSI hat, könnte er es mir Verkaufen? (Angebote Bitte per PN schicken)

MfG

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1148#msg1148)

---

<a id="msg1149"></a>

## 12. Gentoo07 · 06. Nov 2008, 14:08

"funktionierend" sind auch die Handydatenkabel...versuch doch erstmal einen oder mehrere andere Rechner
Bettyheaven mit Boop-rom auf nen USB-Stick und los geht die Reise *g*

Gut möglich, dass es da auf einmal mit beiden Varianten funktioniert.

Edit: Es könnte auch noch am seriellen Kabel zum SSI liegen, es gibt sogenannte "Nullmodem"-Kabel mit verdrehter Aderbelegung von Stecker zu Stecker.

*Last Edit : 06. Nov 2008, 14:14 by Gentoo07*

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1149#msg1149)

---

<a id="msg1150"></a>

## 13. edison · 06. Nov 2008, 19:19

Tief durchatmen, nen Tag warten - und nochmal nach dem Fehler suchen.
Hat bei mir auch geklappt - hatte einen Dreher im Bettystecker

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1150#msg1150)

---

<a id="msg1151"></a>

## 14. pupsi · 07. Nov 2008, 11:41

> **Zitat von: Gentoo07 am 06. Nov 2008, 14:08**
>
> "funktionierend" sind auch die Handydatenkabel...versuch doch erstmal einen oder mehrere andere Rechner

Also dass des am Computer liegen soll kann ich nicht nachvollziehen. Meine Rs232 Schnittstelle funktioniert (Sonst könnt ich ja auch nicht die Firmware von meinem Sat Reciver Flashen)

> **Zitat von: edison am 06. Nov 2008, 19:19**
>
> Hat bei mir auch geklappt - hatte einen Dreher im Bettystecker

Wenn des so einfach wär hätt ich meinen Fehler jetzt auch gefunden aber alle Verbindungen stimmen. Oder muss man doch RX mit RX Verbinden bei der Betty und nicht wie im Wiki beschrieben RX mit TX und TX mit RX?

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1151#msg1151)

---

<a id="msg1154"></a>

## 15. Gentoo07 · 08. Nov 2008, 20:51

> **Zitat von: pupsi am 07. Nov 2008, 11:41**
>
> > **Zitat von: Gentoo07 am 06. Nov 2008, 14:08**
> >
> > "funktionierend" sind auch die Handydatenkabel...versuch doch erstmal einen oder mehrere andere Rechner
>
>
>
> Also dass des am Computer liegen soll kann ich nicht nachvollziehen. Meine Rs232 Schnittstelle funktioniert (Sonst könnt ich ja auch nicht die Firmware von meinem Sat Reciver Flashen)

Gerade das muss nicht unbedingt so sein...es gibt erwiesenermaßen öfter mal sogenannte Timing-Probleme, die nicht nur abhängig vom Rechner , dem Betriebssystem und auch den nebenher laufenden Programmen sind sondern auch noch von der verwendeten Baudrate, eventuellem Hardware-Handshake und eben der verwendeten Gegenstelle mit einem evtl. vorhandenen eigenem Übertragungsprotokoll.

Daher führt bei solchen Spezialfällen wie der Betty und den nicht sehr großflächig getestenen Programmierwerkzeugen öfter mal probieren mit mehreren Rechnern zum Erfolg. Eben weil sich die Probleme kaum richtig nachvollziehen lassen aber immer mal wieder auftreten und woanders nicht.

[Permalink](http://bettyhacks.com/forum/index.php?topic=165.msg1154#msg1154)

---

## Verwandte Themen

- [Simple Seriell Interface zu Verkaufen](0171-simple-seriell-interface-zu-verkaufen.md)
- [Simple Seriell Interface zu Verkaufen (zum 2. mal)](0175-simple-seriell-interface-zu-verkaufen-zum-2-mal.md)
- [Frage zum Simple Serial Interface](0104-frage-zum-simple-serial-interface.md)
- [[Bilder] Simple Serial Interface V2](0108-bilder-simple-serial-interface-v2.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
