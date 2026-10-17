---
title: "Funksteckdosen"
topic_id: 86
board: "Software"
board_id: 6
posts: 11
first_post: "10. Dez 2007, 08:50"
last_post: "20. Feb 2012, 22:46"
authors: ["Megabug", "MrFX", "asgard", "eme", "mcgyver100", "minipilot", "netguy", "tmuehlha"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=86.0"
---

# Funksteckdosen

[← Software](../boards/06-software.md) · Thema 86 · 11 Beiträge · 10. Dez 2007, 08:50 – 20. Feb 2012, 22:46

Beteiligt: Megabug, MrFX, asgard, eme, mcgyver100, minipilot, netguy, tmuehlha

---

<a id="msg627"></a>

## 1. minipilot · 10. Dez 2007, 08:50

Hallo,

es gibt doch diese Baumarkt Funksteckdosen. Wäre es möglich, diese Steckdosen mit der Betty zu schalten. Die Steckdosen benutzen auch den 433 MHz Funkbereich wie die Betty.

Man könnte so eine Master-schaltung für Glotze Receiver Verstärker DVD realisieren oder auch nur die Christbaum Beleuchtung schalten...

Gruß Minipilot

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg627#msg627)

---

<a id="msg630"></a>

## 2. MrFX · 10. Dez 2007, 11:39

Moin!

Glaube ich nicht, denn die benutzen einen speziellen Chip: PT2262.

Man könnte natürlich die Funksteckdosen auf CC1100 "umrüsten"...

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg630#msg630)

---

<a id="msg633"></a>

## 3. asgard · 10. Dez 2007, 12:34

Hi,
> **Zitat von: minipilot am 10. Dez 2007, 08:50**
>
> Man könnte so eine Master-schaltung für Glotze Receiver Verstärker DVD realisieren oder auch nur die Christbaum Beleuchtung schalten...

Christbaumbeleuchtung?....da gehören "echte" Kerzen hin 

Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg633#msg633)

---

<a id="msg638"></a>

## 4. minipilot · 10. Dez 2007, 14:51

@asgard
Hatte noch nie was anderes als Wachskerzen am Baum. Aber ich muss mich jedes Jahr gegen meine Holde durchsetzen...

@MrFX
Pflücke heute Abend mal eine Steckdose auseinander

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg638#msg638)

---

<a id="msg657"></a>

## 5. minipilot · 14. Dez 2007, 21:22

So, hat ein wenig länger gedauert. Bei meinem Sender ist ein Chip mit der Bezeichnung LP801B verbaut.

Das spuckt Gooooogle so aus:

[http://avr.b](https://web.archive.org/web/2012/http://avr.b)örke.de/Funksteckdosen.htm
[http://thomaskropf.at/index.php?option=com_content&task=view&id=19&Itemid=28](https://web.archive.org/web/2012/http://thomaskropf.at/index.php?option=com_content&task=view&id=19&Itemid=28)

Und das Datenblatt:

[http://www.princeton.com.tw/webSite/downloadprocess/downloadfile.asp?mydownload=PT2272_1.pdf](https://web.archive.org/web/2012/http://www.princeton.com.tw/webSite/downloadprocess/downloadfile.asp?mydownload=PT2272_1.pdf)

Gruß minipilot

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg657#msg657)

---

<a id="msg658"></a>

## 6. MrFX · 14. Dez 2007, 22:05

Moin!

Wie ich schon schrieb... die Kombi aus PT2262 und 2272.

Haben leider 2 Probleme: benötigen 12 V (weniger geht nicht, dann funktioniert die HF-Einheit nicht) und stören die meisten Geräte auf dem 433 MHz-Band; meine Funk-Temperatursensoren werden, seitdem ich diese Schalter in Betrieb habe, nicht mehr empfangen!

Das einfachste wäre, selbst etwas entsprechendes zu bauen, also ein kleines Platinchen mit uC, CC1100 und Relais oder FET (für Dimmer).

Oder die Teile "simulieren", was ich aber kaum für möglich halte...

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg658#msg658)

---

<a id="msg659"></a>

## 7. netguy · 15. Dez 2007, 01:17

hallo,

wie ich es mir gedacht habe, das ist mit nix wirklich kompatibel. der eigentlliche code-empfaenger ist ein ic wie z.b. fuer ir fernbedienungen, und der eigentlich hf sender/empfaenger ist nichts weiter als ein traeger der dann davon angesteuert wird bzw. das in den chip fuettert.

das ist auf keinen fall mit dem cc1100 oder den pollin modulen zu verbinden (funkmaessig). apropos pollin-modul: das sollte sich theoretisch mit den cc1100 der betty verstehen.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg659#msg659)

---

<a id="msg661"></a>

## 8. mcgyver100 · 15. Dez 2007, 09:47

Hi

Hier mal ne andere Idee

Es gibt IR Verlängerungen die über Funk senden .

Ich z.B. habe diese : [http://www.elv.de/output/controller.aspx?cid=74&detail=10&detail2=7495](https://web.archive.org/web/2012/http://www.elv.de/output/controller.aspx?cid=74&detail=10&detail2=7495)
![](https://web.archive.org/web/2012/http://www.elv-downloads.de/bilder/artikel/45369.jpg)

Ich benutze ihn mit meiner Philips Pronto .

Zum Anlernen nur den Funk-IR Wandler anschließen und die Funk FB auf die IR FB anlernen .
Zum benutzen den Funk-IR Wandler abklemmen und nur den IR- Funk Wandler anschließen und siehe da es werde Licht .

Klappt bei mir wunderbar mit Schaltern ( Billigteile von OBI für 15 € 3er Set ) und auch Dimmern und ist ned so teuer ca. 25 €

cu mcgyver100

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg661#msg661)

---

<a id="msg663"></a>

## 9. Megabug · 16. Dez 2007, 18:05

Also ich versorge meine Fernbedienung mit 5V statt den 12V und klappt auch gut. [http://katanafans.idf-mod.de/web/include.php?path=content/content.php&contentid=26](https://web.archive.org/web/2012/http://katanafans.idf-mod.de/web/include.php?path=content/content.php&contentid=26)

Ich weiss, sieht schrecklich aus. Aber macht nichts!

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg663#msg663)

---

<a id="msg1971"></a>

## 10. tmuehlha · 20. Nov 2011, 11:33

Funksteckdosen sind recht einfach anzusprechen, ist eigentlich wie ein "Morsecode". Das CC1100 müsste man dafür aber in einen AM Modus bekommen, das geht doch oder? Sollte ein Betty Programmierer dann einfach schaffen können.
Ich kann nicht gut programmieren, daher bekomme das ich das nur mit einem Arduino hin, wenn ich fertige Libraries nutzte.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg1971#msg1971)

---

<a id="msg2006"></a>

## 11. eme · 20. Feb 2012, 22:46

Nichts neues, nur eine Umleitung dieses alten Threads auf: [http://bettyhacks.com/forum/index.php?topic=223.0](0223-funksteckdose.md) (Boop 'kann' Funksteckdosen)!

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=749500db2d024952ffa89938d6b2d015&topic=86.msg2006#msg2006)

---

## Verwandte Themen

- [Funksteckdose](0223-funksteckdose.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
