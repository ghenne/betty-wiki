---
title: "SVN Server Offline->Neuer Online"
topic_id: 210
board: "Software"
board_id: 6
posts: 10
first_post: "09. Jun 2009, 09:10"
last_post: "16. Apr 2013, 21:33"
authors: ["Telekatz", "asgard", "eme", "gunnar"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=210.0"
---

# SVN Server Offline->Neuer Online

[← Software](../boards/06-software.md) · Thema 210 · 10 Beiträge · 09. Jun 2009, 09:10 – 16. Apr 2013, 21:33

Beteiligt: Telekatz, asgard, eme, gunnar

---

<a id="msg1426"></a>

## 1. gunnar · 09. Jun 2009, 09:10

Hallo zusammen!

Ich wollte mir Boop mal ansehen, aber der SVN Server antwortet mir nicht, kann jemand den mal wieder in Gang setzen?

Viele Grüße
Gunnar

*Last Edit : 25. Dez 2009, 23:12 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1426#msg1426)

---

<a id="msg1427"></a>

## 2. Telekatz · 09. Jun 2009, 22:07

Hallo,

Server ist momentan wegen Providerwechsel down. An einer Übergangslösung bis der Server wieder am Netz hängt wird aber gearbeitet.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1427#msg1427)

---

<a id="msg1428"></a>

## 3. gunnar · 10. Jun 2009, 07:44

Hallo,

könnte mir den in der Zwischenzeit jemand den ausgecheckten Quellcode von Boop und der Programmiersoftware als Archiv irgendwo ablegen?

Vielen Dank im Voraus,

Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1428#msg1428)

---

<a id="msg1465"></a>

## 4. eme · 23. Jul 2009, 09:45

Wie wär's mit sourceforge.com, code.google.com, github.com, ... [http://en.wikipedia.org/wiki/Comparison_of_open_source_software_hosting_facilities](https://web.archive.org/web/2012/http://en.wikipedia.org/wiki/Comparison_of_open_source_software_hosting_facilities)
Dann hast Du keine Arbeit damit, und der Code ist für 'immer' zugänglich..

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1465#msg1465)

---

<a id="msg1466"></a>

## 5. gunnar · 23. Jul 2009, 09:55

Hallo,
> **Zitat von: eme am 23. Jul 2009, 09:45**
>
> Wie wär's mit sourceforge.com, code.google.com, github.com, ...

Das halte ich auch für eine gute Idee! Wenn es niemand sonst tun möchte würde ich die Sources bei sourceforge einspielen. Ich warte aber erstmal Rückmeldungen zum Vorschlag ab.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1466#msg1466)

---

<a id="msg1467"></a>

## 6. asgard · 23. Jul 2009, 18:08

hau rein

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1467#msg1467)

---

<a id="msg1468"></a>

## 7. gunnar · 23. Jul 2009, 23:07

Hallo,
> **Zitat von: asgard am 23. Jul 2009, 18:08**
>
> hau rein

Ihr könnt ab jetzt hier auschecken:
svn co [https://boopfirmware.svn.sourceforge.net/svnroot/boopfirmware](https://web.archive.org/web/2012/https://boopfirmware.svn.sourceforge.net/svnroot/boopfirmware) boopfirmware

Die Projektseite:
[http://boopfirmware.sourceforge.net/](https://web.archive.org/web/2012/http://boopfirmware.sourceforge.net/)

Nur boop als Name ging irgendwie nicht, deshalb boopfirmware. Die von Telekatz erhaltene Mini-RAM Version zum Testen neuer Features werde ich später auch noch einchecken.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1468#msg1468)

---

<a id="msg1475"></a>

## 8. eme · 04. Sep 2009, 17:15

Danke.
Code "browsen" und "downloaden" geht hier:
[http://sourceforge.net/projects/boopfirmware/develop](https://web.archive.org/web/2012/http://sourceforge.net/projects/boopfirmware/develop)

Es ist auch das lpctool mit dabei.

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1475#msg1475)

---

<a id="msg1476"></a>

## 9. Telekatz · 08. Sep 2009, 19:30

Fehlt nur noch Code "uploaden".

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg1476#msg1476)

---

<a id="msg2116"></a>

## 10. gunnar · 16. Apr 2013, 21:33

Hallo,
ich habe das Projekt auf die neue Sourceforge Software umgestellt. Auf der alten Repository URL kann man nur noch auchecken, aber nicht mehr einchecken.

Zum späteren Einchecken müsst Ihr diese URL nehmen:
svn checkout --username=mein_login svn+ssh://mein_login@svn.code.sf.net/p/boopfirmware/code/ boopfirmware-code

mein_login bitte durch das Sourceforge-Login ersetzen.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=210.msg2116#msg2116)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
