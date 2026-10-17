---
title: "Source LCPTool und Beispielprogramm, das im Ram läuft"
topic_id: 215
board: "Software"
board_id: 6
posts: 11
first_post: "05. Juli 2009, 10:01"
last_post: "06. Juli 2009, 21:48"
authors: ["Telekatz", "asgard", "gunnar"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=215.0"
---

# Source LCPTool und Beispielprogramm, das im Ram läuft

[← Software](../boards/06-software.md) · Thema 215 · 11 Beiträge · 05. Juli 2009, 10:01 – 06. Juli 2009, 21:48

Beteiligt: Telekatz, asgard, gunnar

---

<a id="msg1448"></a>

## 1. gunnar · 05. Juli 2009, 10:01

Hallo,

wäre bitte jemand so nett mir den Source des LPCTool schicken, das SVN is ja down, so dass ich es nicht selbst auschecken kann. (G.Henne@combio.de)

Ich möchte in der Betty kleine Programme im RAM ausführen, hat jemand zufällig ein kleines Beispielprojekt das im Ram läuft und irgendwas tut, so dass man sehen kann dass es ausgeführt wird? (Ausgabe auf der seriellen Schnittstelle, Hintergrundlicht blinkt o.ä.) Ich bin neu in der ARM Programmierung und weiss noch nicht, wie man die Linker-Scripts so anpasst, dass ein Programm im Ram statt im Rom läuft. Ich habe nur gesehen, dass man mit LPCTool ein Programm ins Ram lädt, dass dann den Flash prorammiert. Prinzipiell müsste man also beliebige Programme im Ram laufen lassen können...

Ich möchte etwas mit dem Funkchip spielen und da ist es praktisch, wenn man erstmal was im Ram ausführen/testen kann, um es dann später in Betty zu integrieren und im Flash laufen zu lassen.

Vielen Dank schonmal!

Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1448#msg1448)

---

<a id="msg1449"></a>

## 2. Telekatz · 05. Juli 2009, 22:56

Hallo Gunnar,

anbei eine Boop Version die ich mal zum Testen des SID erstellt habe. Läuft im RAM, ist aber im Funktionsumfang stark reduziert worden.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1449#msg1449)

---

<a id="msg1450"></a>

## 3. gunnar · 05. Juli 2009, 23:56

Hallo Telekatz!

Super vielen Dank, dass ist mehr als ich erhofft hatte. :-)

Wie lautet denn die Befehlszeile fürs LPCtool um das Programm zu übertragen/starten? Bzw falls Du einen anderen Loader benutzt: Ab welcher Ram Adresse muss geladen werden und wo startet die Ausführung?

Viele Grüße
Gunnar

> **Zitat von: Telekatz am 05. Juli 2009, 22:56**
>
> anbei eine Boop Version die ich mal zum Testen des SID erstellt habe. Läuft im RAM, ist aber im Funktionsumfang stark reduziert worden.

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1450#msg1450)

---

<a id="msg1451"></a>

## 4. Telekatz · 06. Juli 2009, 10:52

Geladen und gestartet wir ab Adresse 0x40000200. Zum laden benutze ich Bettyheaven, dort ist diese Adresse fest eingestellt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1451#msg1451)

---

<a id="msg1453"></a>

## 5. gunnar · 06. Juli 2009, 20:30

Hallo Telekatz,

das klappt super. :-)
Ich kann das Testprogramm im RAM ausführen und das ROM bleibt unverändert. Einmal Reset und dann ist Boop aus dem Rom wieder da.
Ich habe mit dieser Kommandozeile den Transfer und den Start gemacht:

lpctool -r boop_rom.bin -d /dev/ttyUSB2

Den Quellcode von LPCTools habe ich aber immernoch nicht. Liest denn hier nur Telekatz mit?

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1453#msg1453)

---

<a id="msg1454"></a>

## 6. asgard · 06. Juli 2009, 20:38

> **Zitat von: gunnar am 06. Juli 2009, 20:30**
>
> Liest denn hier nur Telekatz mit?

nein

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1454#msg1454)

---

<a id="msg1455"></a>

## 7. gunnar · 06. Juli 2009, 20:58

Hallo Asgard und stille Mitleser,

> **Zitat von: asgard am 06. Juli 2009, 20:38**
>
> > **Zitat von: gunnar am 06. Juli 2009, 20:30**
> >
> > Liest denn hier nur Telekatz mit?
>
>
> nein 

Da Du ja offensichtlich mitliest kannst Du mir vielleicht sagen, wie ich an die die Sources komme? Gibt es da ein bestimmtes Ritual? Soll ich Dir oder jemand anderem eine Firmware schicken, die das Display voll "Bitte, bitte" schreibt, um mich als würdig zu erweisen, den LPCTool Source zu bekommen. ;-)

Ich kann auch anbieten auf meinem Server ein SVN für Boop und LPCTool aufsetzen, wenn es größere Schwierigkeiten mit der Neueinrichtung des ursprünglichen SVN Server gibt.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1455#msg1455)

---

<a id="msg1456"></a>

## 8. asgard · 06. Juli 2009, 21:04

> **Zitat von: gunnar am 06. Juli 2009, 20:58**
>
> Da Du ja offensichtlich mitliest kannst Du mir vielleicht sagen, wie ich an die die Sources komme? Gibt es da ein bestimmtes Ritual? Soll ich Dir oder jemand anderem eine Firmware schicken, die das Display voll "Bitte, bitte" schreibt, um mich als würdig zu erweisen, den LPCTool Source zu bekommen. ;-)

fänd ich auch geil...anbei alles was ich svn-mäßig hab....
Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1456#msg1456)

---

<a id="msg1457"></a>

## 9. gunnar · 06. Juli 2009, 21:38

Hallo Asgard,
> **Zitat von: asgard am 06. Juli 2009, 21:04**
>
> fänd ich auch geil...anbei alles was ich svn-mäßig hab....
> Grüße
> Asgard

Danke für den Upload. Im Archiv ist der komplette Quellcode von Boop, aber nicht der von lpctool...

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1457#msg1457)

---

<a id="msg1458"></a>

## 10. Telekatz · 06. Juli 2009, 21:42

Gefunden!

Das "Bitte,bitte" möchte ich aber trotzdem sehen!    (With a cherry on top.)

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1458#msg1458)

---

<a id="msg1459"></a>

## 11. gunnar · 06. Juli 2009, 21:48

Hallo Telekatz,

> **Zitat von: Telekatz am 06. Juli 2009, 21:42**
>
> Gefunden!
>
> Das "Bitte,bitte" möchte ich aber trotzdem sehen!    (With a cherry on top.)

Das kommt. Versprochen! Nur die Kirsche wird etwas schwer. ;-)

Danke
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=215.msg1459#msg1459)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
