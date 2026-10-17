---
title: "NXP ISP (nachbau)"
topic_id: 13
board: "Hardware"
board_id: 5
posts: 8
first_post: "01. Aug 2007, 21:12"
last_post: "10. Aug 2007, 19:16"
authors: ["cheristi", "theborg", "vSaAmTp"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=13.0"
---

# NXP ISP (nachbau)

[← Hardware](../boards/05-hardware.md) · Thema 13 · 8 Beiträge · 01. Aug 2007, 21:12 – 10. Aug 2007, 19:16

Beteiligt: cheristi, theborg, vSaAmTp

---

<a id="msg44"></a>

## 1. theborg · 01. Aug 2007, 21:12

So ich habe mich mal dran gemacht das NXP ISP zu bauen leider habe ich dafür im Internet keine Schaltung gefunden b.z.w. die eine die ich gefunden habe ist etwas scheiße aufgebaut kein Spannungswandler für die Schnittstelle und viele sinnlose Bauteile leider läuft sie noch nicht ganz so wie sie soll.

Nach der Schaltung die ich gefunden habe von (Spark Fun) wird Bootenable und Reset gleichzeitig angesteuert da ist aber das Problem das beide gleichzeitig auch wieder auf High gesetzt wird also der Bootloader nicht Aktiviert wird da Reset und Bootenable gleichzeitig ausgeführt werden, dieses habe ich aber noch nicht geändert werde ich wahrscheinlich aber noch machen.

(Achtung !!! nicht nicht ganz fertig) [http://grautier.com/temp/betty/NXPisp.png](https://web.archive.org/web/2012/http://grautier.com/temp/betty/NXPisp.png)

Wer schon nen Schnittstellenwandler hat (Pollin/elv) kann einfach den teil mit den Transistoren an den RTS ausgang klemmen

Das NXP ISP Tool gibt es bei NXP.de oder Flash Magic das findet ihr irgendwo bei Google.

mfg tb

Mein Testaufbau
![](https://web.archive.org/web/2012/http://grautier.com/temp/betty/RIMG0003.JPG)

*Last Edit : 28. Sep 2007, 05:05 by theborg*

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg44#msg44)

---

<a id="msg45"></a>

## 2. vSaAmTp · 01. Aug 2007, 21:47

Glaub Du meinst [www.nxp.com](https://web.archive.org/web/2012/http://www.nxp.com) . Die DE Seite ist ne Werbeseite...

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg45#msg45)

---

<a id="msg75"></a>

## 3. cheristi · 02. Aug 2007, 17:53

Ist der ISP irgendwas besonderes?
Oder ist das ein ganz normaler ISP wie z.b. der von myavr.de
Den habe ich mal gekauft um ATMELs zu programmieren.

#grs

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg75#msg75)

---

<a id="msg76"></a>

## 4. theborg · 02. Aug 2007, 18:45

nein der ISP ist eigentlich recht simpel aufgebaut nen Standard ttl Wandler und dann eine Leitung um per SW Bootloader enable und reset zu schaltun das ding ist aber noch nicht ganz fertig.

Aber zum Amtel ISP wenn das der 20 polige ist kanste den als Jtag für die betty verwenden

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg76#msg76)

---

<a id="msg77"></a>

## 5. vSaAmTp · 02. Aug 2007, 19:46

Wie sieht es mit dem Teil aus ([SerCon](https://web.archive.org/web/2012/http://mikrocontroller.cco-ev.de/files/SerCon_Anleitung_V0_2.pdf))? Kann man das auch benutzen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg77#msg77)

---

<a id="msg137"></a>

## 6. theborg · 05. Aug 2007, 20:48

jup ist nen Standard rs232 Wandler den kanste auch so benutzen um die Konsole auszuwerten

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg137#msg137)

---

<a id="msg187"></a>

## 7. vSaAmTp · 10. Aug 2007, 19:00

Wenn es Fertig ist, werd ich ne nette Bauanleitung schreiben inkl. Reichelt Stückliste.

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg187#msg187)

---

<a id="msg188"></a>

## 8. theborg · 10. Aug 2007, 19:16

jo nen angefangen der Eintrag ist ja schon im wikki den kanste dann weiter machen ich bin dabei das faq für die fw zu schreiben

[Permalink](http://bettyhacks.com/forum/index.php?topic=13.msg188#msg188)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
