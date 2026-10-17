---
title: "Log auslesen. (Was muss ich tun?)"
topic_id: 19
board: "Software"
board_id: 6
posts: 11
first_post: "03. Aug 2007, 10:34"
last_post: "06. Okt 2007, 14:52"
authors: ["DocKugelfisch", "Robbi5", "Spessi", "asgard", "netguy", "theborg"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=19.0"
---

# Log auslesen. (Was muss ich tun?)

[← Software](../boards/06-software.md) · Thema 19 · 11 Beiträge · 03. Aug 2007, 10:34 – 06. Okt 2007, 14:52

Beteiligt: DocKugelfisch, Robbi5, Spessi, asgard, netguy, theborg

---

<a id="msg92"></a>

## 1. Robbi5 · 03. Aug 2007, 10:34

Hallo,

was muss ich jetzt eigentlich basteln/tun, damit ich auch so ein schönes Betty-Log auslesen kann?

Robbi5

p.s.: Denn vielleicht steht ja die Sofameilen-Anzahl drin => *Neues Tool für BettyTools.net überleg...*

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg92#msg92)

---

<a id="msg96"></a>

## 2. Spessi · 03. Aug 2007, 12:09

Erstmal brauchste nen RS232-TTL-Wandler, gibts bei Pollin.de

Hier eine Anleitung, die dir erklärt wie du ihn Betty-tauglich machst
[http://betty.zentgraf-modding.de/index.php?s=howto&p=1](https://web.archive.org/web/2012/http://betty.zentgraf-modding.de/index.php?s=howto&p=1)

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg96#msg96)

---

<a id="msg161"></a>

## 3. DocKugelfisch · 07. Aug 2007, 17:04

Zu der Anleitung eine Frage:
Du hast dort darauf verwiesen, daß Du einen Fehler entdeckt hast.
Ist es der, daß Du Elkos anstelle von Transistoren verwendet hast?
Oder schon wieder ein neuer?

<sub>

Was man lernen muß, um es zu tun, das lernt man, indem man es tut.
Zitat: Aristoteles (384-322), griechischer Philosoph

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg161#msg161)

---

<a id="msg189"></a>

## 4. Spessi · 12. Aug 2007, 10:34

Falsch, ich vermute, dass es daran liegt, dass ich Transistoren anstatt Elkos verwendet hab... Kannst ja mal ausprobieren, bin gestern erst aus Urlaub zurückgekommen und hatte noch keine Zeit zu probieren.

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg189#msg189)

---

<a id="msg190"></a>

## 5. theborg · 12. Aug 2007, 11:35

Hi ich hab mich mal dran gemacht und einen wandler von elv (gibs da nicht mehr) umgebaut die Schaltung ist ja die gleiche ich hab 5x 0,1µF drinne damit geht des hervoragend als chip hab ich einen MAX3232cpe verwendet.

komisch erweise hat mein usb Wandler immer zikken gemacht per seriell geht es einwandfrei.

*Last Edit : 12. Aug 2007, 11:37 by theborg*

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg190#msg190)

---

<a id="msg423"></a>

## 6. Robbi5 · 05. Okt 2007, 20:24

So, hab jetzt gerade ein SimpleSerialInterface gebastelt.
Ich hab jetzt auf der Platine 4 Pins.
Was muss ich jetzt wohin verbinden, dass ich dann mit minicomm den 'Gurkensalat' eingeben kann?? 

Robbi5

EDIT Admin: er meint das Interface:
[http://bettyhacks.com/wiki/index.php/Simple_Serial_Interface](../../pages/Simple%20Serial%20Interface.md)

*Last Edit : 06. Okt 2007, 09:56 by asgard*

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg423#msg423)

---

<a id="msg425"></a>

## 7. asgard · 06. Okt 2007, 06:43

Hi,
schau mal ins wiki, da steht alles drin
[http://www.bettyhacks.com/wiki/index.php/Testmode](../../pages/Testmode.md)

Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg425#msg425)

---

<a id="msg426"></a>

## 8. Robbi5 · 06. Okt 2007, 07:18

Dass ich den "Bootloader EN, Aktiv = LOW (EINT1)" mit GND verbinden muss, ist mir klar. 

Nur "Am Terminal sind jetzt die Ausgaben der Betty zu sehen." geht bei mir nicht, weil ich keine Ahnung habe welche Pins von der Platine wohin auf die Betty müssen 

Robbi5

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg426#msg426)

---

<a id="msg427"></a>

## 9. asgard · 06. Okt 2007, 09:54

Hi,

also, ich hoffe ich sag nichts falsches,....
Du musst von JP1_Pin 1 (TX) an den RX der Betty.
Du musst von JP1_Pin 2 (RX) an den TX der Betty.
Du musst von JP1_Pin 3 (3,3V) an den 3,3V der Betty (siehe
[http://www.bettyhacks.com/wiki/index.php/Anschlussbelegungen)](https://web.archive.org/web/2012/http://www.bettyhacks.com/wiki/index.php/Anschlussbelegungen))
Du musst von JP1_Pin 4 (GND) an den GND der Betty.

Wenn das nicht funktioniert, dann tausch mal JP1_1 und JP1_2.

Grüße
Asgard

*Last Edit : 06. Okt 2007, 09:57 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg427#msg427)

---

<a id="msg429"></a>

## 10. Robbi5 · 06. Okt 2007, 13:28

Danke

So, ich habs jetzt fertig gebastelt, auf nem anderem PC ubuntu aufgesetzt, bekomme aber leider keine (boot)-logs von Betty.
Habe auch schon RX/TX vertauscht.
Was muss ich noch machen?

Robbi5

*Last Edit : 06. Okt 2007, 13:45 by Robbi5*

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg429#msg429)

---

<a id="msg430"></a>

## 11. netguy · 06. Okt 2007, 14:52

also, wenn du das log der betty firmware sehen willst, muss eint beim reset natuerlich offen bleiben ... dann mit 115200,n,8,1 dran ...

wenn du aber mit dem chipinternen bootloader reden willst, muss eint beim reset geschlossen (auf gnd) sein, und die baudrate 19200 oder 38400 baud sein (langsamer ginge auch noch...). dann im lpc manual nachschauen was man mit dem bootloader machen kann....

ich nehme mal an das du auch einen max3232 hast? achte darauf das nicht unbedingt 3.3 volt aus dem header kommen, ich habe bei meinen hier ueberall nur 3 volt. das _kann_ unter umstaenden zu wenig sein, um die ladungspumpe im max sauber zu betreiben. evtl. hilft es dann, die kondensatoren zu vergroessern (einfach mal in das datenblatt des max3232 schauen)

wenn du aber einen max232 hast, also den normalen, dann klappt das mit der spannung von der betty eh nicht, da das ein 5volt bauteil ist. in dem fall kannst du dir aber die 5 volt vom usb bus des rachners "klauen". auf jeden fall dann aber einaml 10µF und und einmal 0.01µF zwischen +5volt und gnd bauen, damit die spannung einigermassen suaber wird.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=19.msg430#msg430)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
