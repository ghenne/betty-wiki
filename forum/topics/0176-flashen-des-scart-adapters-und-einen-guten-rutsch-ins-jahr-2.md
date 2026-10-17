---
title: "Flashen des Scart Adapters ???  und einen guten Rutsch ins Jahr 2009 !!!"
topic_id: 176
board: "Hardware"
board_id: 5
posts: 14
first_post: "14. Februar 2009, 11:55"
last_post: "02. Juni 2009, 19:57"
authors: ["Gentoo07", "JimBeam", "Megabug", "MrFX", "Telekatz", "ino", "phaidros"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=176.0"
---

# Flashen des Scart Adapters ???  und einen guten Rutsch ins Jahr 2009 !!!

[← Hardware](../boards/05-hardware.md) · Thema 176 · 14 Beiträge · 14. Februar 2009, 11:55 – 02. Juni 2009, 19:57

Beteiligt: Gentoo07, JimBeam, Megabug, MrFX, Telekatz, ino, phaidros

---

<a id="msg1298"></a>

## 1. JimBeam · 14. Februar 2009, 11:55

Ich habe noch eine bessere Idee (finde ich jedenfalls...):

Es gibt dieses Projekt: [http://www.recursion.jp/avrcdc/](https://web.archive.org/web/2012/http://www.recursion.jp/avrcdc/), das ist ein auf einem AVR basierendes rein in Software implementiertes USB-Device. Wenn man da ein wenig zusätzliche Software einbringt, die das "Wackeln" am Reset des dahinter befindlichen SCART-Moduls macht, wäre das doch perfekt... Und man spart sich sogar noch den USB-Wandler! Man könnte einen minimalen AT-Befehlssatz einbauen, bei dem ein Befehl das SCART Modul in den ISP-Zustand bringt. Ich werde heute mal ein wenig daran arbeitet - so please stay tuned... 

Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1298#msg1298)

---

<a id="msg1299"></a>

## 2. Gentoo07 · 15. Februar 2009, 01:37

Hallo JimBeam, eine Anregung zum Thema:

Unter [http://www.obdev.at/products/avrusb/index.html](https://web.archive.org/web/2012/http://www.obdev.at/products/avrusb/index.html) findest du eine ähnliche, noch etwas umfangreichere AVR-USB-Lib die m.E. etwas verbreiteter ist und wohl auch besser supportet wird. Ob hier tatsächliche Vorteile bestehen kann ich natürlich nicht garantieren, aber unter dem Punkt "Community Projects" kannst du dir schon eine große Menge an Beispielimplementierungen anschauen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1299#msg1299)

---

<a id="msg1300"></a>

## 3. JimBeam · 15. Februar 2009, 04:44

Jau, und das von mir genannte basiert darauf... 

Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1300#msg1300)

---

<a id="msg1301"></a>

## 4. JimBeam · 15. Februar 2009, 21:29

Zwischenbericht:

Es geht und geht auch nicht...

1.) Die ISP Routinen, die PHILIPS im Auslieferungszustand im FLASH des LPC931 hinterlässt, wurden beim Fertigen des Betty SCART Adapters offenbar gelöscht - das sind die Routinen zum Programmieren über die serielle Schnittstelle (Pin1 und 2, RX/TX, dreimal "Wackeln" am Reset) und NICHT die ICP Routinen, die über Pin3 und 4 (PDA/PCL, 8x Wackeln...) arbeiten! Letztere sind im ROM unlöschbar drin und werden zum Flashen über die Betty und auch beim Kombiinterface benutzt.
2.) Die 5V vom USB sind seeeehr knapp zur Versorgung des Moduls! Laut USB-Spezifikation können da durchaus auch nur 4,5V anliegen. Auf dem SCART Modul macht ein LM317 daraus die 3,3V für die Chips, und der will laut Datenblatt je nach Temperatur und Laststrom zwischen 1,5 und 2V mehr am Eingang als am Ausgang - reicht also gerade so oder auch nicht... Außerdem ist eine minimale Eingangsspannung von 4,3V angegeben - also auch knapp. Dann müsste man die Versorgungsspannung des Moduls auch noch softwaremäßig schaltbar machen, da ist also ein Längstransistor fällig, der auch noch mal ein paar Millivolt schluckt.
3.) Der ATtiny2313 hat mit der genannten Firmware (egal ob von obdev direkt oder dem recursion Derivat) nur noch ein paar zig Worte frei - das reicht nicht für einen AT-Kommando Dekoder, sondern nur für eine Taste, die beim Power-On gecheckt wird und dann entweder in den ISP Mode geht oder nicht.

Also habe ich das aufgegeben, und werde weiter mit dem Kombiinterface arbeiten... 

Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1301#msg1301)

---

<a id="msg1305"></a>

## 5. phaidros · 18. Februar 2009, 02:05

Es gibt noch eine dritte Möglichkeit, bei der man nicht an der Reset-Leitung wackeln muss. Dazu müssen allerdings einmalig die oben erwähnten Philips-ISP-Routinen wieder ins Flash gebracht werden. Dann noch in der Software beim Register AUXR1 Bit 6 setzen.
Dann erkennt der Scart-Adapter ein Break-Signal auf der seriellen Schnittstelle und spring automatisch in die ISP Routinen.
Funktioniert bei mir ziemlich gut.

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1305#msg1305)

---

<a id="msg1323"></a>

## 6. MrFX · 09. März 2009, 10:12

Moin!

Was ich mir noch vorstellen könnte:

Übertragung des Hexfiles an die Betty per Funk in RAM/Flash und dann Flashen per ICP.

So könnte man ein wenig effektiver mit dem Scartadapter arbeiten und hätte außerdem einen billigen ICP-Programmer für alle kompatiblen LPCs.

Noch 'ne andere Frage: hat schon mal jemand was mit I2C am Scartadapter gemacht? Könnte mir das mit 'nem PCF8574 und einigen Relais als Funk-Schalteinheit oder mit LM75 als Funkthermometer-Sender vorstellen.

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1323#msg1323)

---

<a id="msg1324"></a>

## 7. Telekatz · 12. März 2009, 22:52

Hab jetzt mal das Interface mit dem FT232RL gebaut. Serielle Kommunikation und Flashen des Scartadapters funktionieren damit.

Werd das ganze sobald ich die Programmiersoftware dazu fertig habe hier mal veröffentlichen.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1324#msg1324)

---

<a id="msg1325"></a>

## 8. MrFX · 13. März 2009, 09:54

Moin!

Hehe, danke, das klingt doch mal gut...
Hoffentlich eine Linux-Software, die auch unter OSX läuft 

MfG
MrFX

*« Letzte Änderung: 13. März 2009, 10:05 von MrFX »*

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1325#msg1325)

---

<a id="msg1326"></a>

## 9. Telekatz · 13. März 2009, 11:53

> **Zitat**
>
> Hoffentlich eine Linux-Software, die auch unter OSX unter OSX läuft

Linux läuft bei mir nur auf SAT Receivern.   
Freiwillige vor.

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1326#msg1326)

---

<a id="msg1327"></a>

## 10. ino · 17. März 2009, 11:39

Hallo Telekatz

Kannst du mal den Schaltplan vom Interface einstellen???
Dann würde ich mir auch mal einen FT232RL besorgen und deine Schaltung nachbauen.

Viele Dank,Grüße ino

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1327#msg1327)

---

<a id="msg1328"></a>

## 11. Telekatz · 17. März 2009, 18:22

Hallo,

anbei Schaltplan, PCB und Bestückungsplan der Schaltung.

Angeschlossen wird das Interface nur über den 7polingen Pinheader, die beiden Versorgungsleitungen vom Netzteil werden entfernt.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1328#msg1328)

---

<a id="msg1329"></a>

## 12. Telekatz · 17. März 2009, 23:07

Und hier noch die passende (Windows) Software dazu. Erstellt mit Visual C++ 2008 Express Edition.

Vielleicht findet sich ja noch jemand, der das auch für Linux erstell. Sourcecode ist dabei.

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1329#msg1329)

---

<a id="msg1424"></a>

## 13. Megabug · 02. Juni 2009, 00:18

Hi!

Gibts eigentlich was neuen mit dem Scart Adapter?

Bestelle mir jetzt bei Reichelt den FT232 mit und bastel mir ne Platine . Will auch etwas mit dem Scart Adapter spielen!

Gruß
Megabug

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1424#msg1424)

---

<a id="msg1425"></a>

## 14. Telekatz · 02. Juni 2009, 19:57

Nein, was neues zum Scart Adapter gibt's momentan nicht.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=176.msg1425#msg1425)

---

## Verwandte Themen

- [Fehler beim Flashen des SCART-Adapters](0186-fehler-beim-flashen-des-scart-adapters.md)
- [Frohe Weihnachten und einen guten Start ins Jahr 2008](0092-frohe-weihnachten-und-einen-guten-start-ins-jahr-2008.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
