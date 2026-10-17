---
title: "Diplomarbeit zu Sensornetzwerken. Hardware: 200 Bettys und boop"
topic_id: 181
board: "Software"
board_id: 6
posts: 12
first_post: "13. Jan 2009, 20:48"
last_post: "16. Jan 2009, 10:50"
authors: ["MrFX", "asgard", "eme", "pcsquirrel", "safti"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=181.0"
---

# Diplomarbeit zu Sensornetzwerken. Hardware: 200 Bettys und boop

[← Software](../boards/06-software.md) · Thema 181 · 12 Beiträge · 13. Jan 2009, 20:48 – 16. Jan 2009, 10:50

Beteiligt: MrFX, asgard, eme, pcsquirrel, safti

---

<a id="msg1224"></a>

## 1. eme · 13. Jan 2009, 20:48

Zitat aus [http://ces.univ-karlsruhe.de/~ebi/pdf/DA_Kobbe_Sensornetzwerk.pdf](https://web.archive.org/web/2012/http://ces.univ-karlsruhe.de/~ebi/pdf/DA_Kobbe_Sensornetzwerk.pdf) (5,5 MB)

Seite 17 bzw. 25 im PDF

3.3 Gegebenheiten

Bereits gegeben war die Hardware, ursprünglich einmal eine interaktive Fernbedienung
mit dem Namen Betty. Das Betty-Set war aus mehreren Teilkomponenten aufgebaut:
Ein Adapter zum Anschluss an den Fernseher um zu erkennen, welcher Sender
und welche Sendung gerade angesehen wird, ein Modem zum Anschluss an das Telefonnetz
um Verbindung zum Betty-Server aufbauen zu können und natürlich die Fernbedienung
selbst. Die Teilkomponenten standen per Funk miteinander in Verbindung.
In dieser Arbeit wird nur die Fernbedienung selbst (die sog. "Head Unit") eingesetzt,
da diese bereits fur den Betrieb mit Akkus vorbereitet war. Sie steht vielen kommerziell
angebotenen Sensorknotenplattformen in nichts nach und bietet "Features" - wie
beispielsweise ein leistungsfahiges LCD - welche uber das ublicherweise Vorhandene
hinausgehen.
Die Betty wurde von der Swisscom AG beworben als interaktive Fernbedienung. Die
Markteinfuhrung erfolgte 2006 (Schweiz) bzw. 2007 (Deutschland). Sie bot Quizspiele,
Abstimmungen, Umfragen, Informationen und Werbung begleitend zum Fernsehprogramm
einiger Fernsehsender. Leider verlief die Markteinfuhrung nicht mit dem
gewunschten Erfolg (nur etwa 100.000 verkaufte Exemplare statt den ¨uber 500.000
geplanten). Der Geschaftsbetrieb wurde Ende 2007 eingestellt.
Da die Betty Fernbedienung den gleichen Funkchip wie der am Institut entwickelte
Hyperion Sensorknoten verwendet, bot es sich an, die Fernbedienungen zur Erweiterung
des Hyperion-Netzes zu verwenden. Aufgrund einer Nachfrage beim (ehemaligen)
deutschen Betreiber konnte eine komplette Palette mit etwa 200 Betty-Sets zu akademischen
Zwecken zur Verfugung gestellt werden. Die Fernbedienung wurde zwar nicht
dazu entworfen, als Sensorknoten zu dienen, aufgrund der verbauten Komponenten
eignet sie sich hierfur jedoch gut. Details zur Hardware werden im Unterkapitel 3.3.1
naher beschrieben. Als Grundgerust fur die Software wurde die Open Source Firmware
"Boop" verwendet. Details hierzu folgen im Unterkapitel 3.3.4.

*Last Edit : 14. Jan 2009, 14:28 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1224#msg1224)

---

<a id="msg1225"></a>

## 2. MrFX · 14. Jan 2009, 08:01

Moin!

Interessant finde ich das Konzept mit den modularen Programmen, die austauschbar sind (ohne die eigentliche Firmware zu verändern); die Aktualisierung der Programme per Funk und die verschiedenen Möglichkeiten, den Stromverbrauch zu reglen...

Vielleicht kann das ja auch in boop einfließen... 

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1225#msg1225)

---

<a id="msg1226"></a>

## 3. pcsquirrel · 14. Jan 2009, 10:19

Hat sich einer von euch bereits nach dem source erkundigt?

lg
pcsquirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1226#msg1226)

---

<a id="msg1227"></a>

## 4. asgard · 14. Jan 2009, 13:58

ob der source public ist...

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1227#msg1227)

---

<a id="msg1228"></a>

## 5. MrFX · 14. Jan 2009, 14:29

Moin!

Nein, weil der Code GPL2 und 3 ist... aber er würde bei Interesse den benötigten Code rausgeben...

> **Zitat**
>
> Vom original boop ist jedoch nicht mehr viel
> übrig/kompatibel, die meisten Funktionen waren schon viel zu gut und
> speziell entwickelt und wurden durch sehr einfache ersetzt (z.B. die
> ganze Interrupt- und Timer Verwaltung, PWM, ...)

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1228#msg1228)

---

<a id="msg1229"></a>

## 6. eme · 14. Jan 2009, 14:33

Urheber ist Sebastian Kobbe, kobbe (a) informatik.uni-karlsruhe.de
[http://ces.univ-karlsruhe.de/i80_stud/site_4e-all-info.htm#Kobbe-S_DA](https://web.archive.org/web/2012/http://ces.univ-karlsruhe.de/i80_stud/site_4e-all-info.htm#Kobbe-S_DA)

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1229#msg1229)

---

<a id="msg1230"></a>

## 7. safti · 14. Jan 2009, 15:22

> **Zitat von: MrFX am 14. Jan 2009, 14:29**
>
> Moin!
> Nein, weil der Code GPL2 und 3 ist... aber er würde bei Interesse den benötigten Code rausgeben...

Hallo,

erlaubt mir, mich hier ebenfalls zu Wort zu melden und die gesamte Antwort zu zitieren.. 

> **Zitat**
>
> aufgrund von Problemen bei der Veröffentlichung von Mischungen aus GPL2
> und GPL3 Code habe ich den Code nicht veröffentlicht.. Prinzipiell
> müsste man nur eine crc32-Routine neu verfassen, dann wäre alles GPL3..
> Ich habe den ganzen Code noch auf meinem Notebook, vielleicht mache ich
> das mal, wenn ich etwas Zeit habe.. An welchen Teilen besteht denn
> besonderes Interesse? Die könnte ich dir wahrscheinlich problemlos
> zukommen lassen.. -- Vom original boop ist jedoch nicht mehr viel
> übrig/kompatibel, die meisten Funktionen waren schon viel zu gut und
> speziell entwickelt und wurden durch sehr einfache ersetzt (z.B. die
> ganze Interrupt- und Timer Verwaltung, PWM, ...) Ein "Rückportieren"
> wäre also extrem eklig  ;-)

Viele Grüße,

Sebastian

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1230#msg1230)

---

<a id="msg1233"></a>

## 8. pcsquirrel · 15. Jan 2009, 08:28

Hallo,

wie schon MrFX sagt, wäre jener Teil für die modularen Applikationen interessant. Vielleicht sollte man um diesen Teil des Codes bitten.

LG
pcsquirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1233#msg1233)

---

<a id="msg1237"></a>

## 9. eme · 15. Jan 2009, 13:04

@ pcsquirrel
evtl. safti = Sebastian = Sebastian Kobbe = Autor der Diplomarbeit ?

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1237#msg1237)

---

<a id="msg1238"></a>

## 10. asgard · 15. Jan 2009, 15:48

> **Zitat von: eme am 15. Jan 2009, 13:04**
>
> @ pcsquirrel
> evtl. safti = Sebastian = Sebastian Kobbe = Autor der Diplomarbeit ?

richtig(er) ist:
safti = Sebastian = Sebastian Kobbe = Autor der Diplomarbeit!

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1238#msg1238)

---

<a id="msg1239"></a>

## 11. pcsquirrel · 16. Jan 2009, 08:38

guten morgen,

erstmal entschuldigung, daß ich da tomaten auf den augen hatte.

hab mir die funktionsweise in der DA mal zu gemüte geführt. das ganze klingt ja gar nicht soo kompliziert, wenn man erstmal weiß wie es funktioniert :-). kompliment!

@sebastian
mich würde noch interessieren, wie die anwendung(en) von der Firmware gestartet werden bzw. die Firmware weiß welche Anwendungen es gibt.
könntest du das bitte kurz erklären oder hab ich das in der DA nur überlesen?

vielen dank
pcsquirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1239#msg1239)

---

<a id="msg1240"></a>

## 12. safti · 16. Jan 2009, 10:50

> **Zitat von: pcsquirrel am 16. Jan 2009, 08:38**
>
> @sebastian
> mich würde noch interessieren, wie die anwendung(en) von der Firmware gestartet werden bzw. die Firmware weiß welche Anwendungen es gibt.
> könntest du das bitte kurz erklären oder hab ich das in der DA nur überlesen?
> pcsquirrel

hi,

hier muss ich leider etwas von der Begeisterung nehmen.. es gibt bei mir immer nur genau eine Anwendung (weil das für meine Anforderungen gereicht hat) welche auf der festen "Firmware" läuft. Die Anwendung wird an eine feste Adresse ins Flash gelinkt (siehe "Speicheraufteilung"). Die Firmware schaut dann, ob an dieser Speicheradresse eine "magische" Bytefolge steht, wenn ja, wird einfach ein Sprung an die Adresse im Flash ausgeführt und voila. Es wäre überhaupt kein Problem, mehrerer solcher Anwendungen an jeweils verschiedene "Slots" zu linken und dann anzuspringen.. Ein kooperativer Scheduler wäre auch in wenigen Zeilen Code implementiert, damit mehrere Anwendungen gleichzeitig laufen können.. Das wäre aber überhaupt nicht kompatibel zum bisherigen boop und auch nicht zu meiner Art der Anwendungen (aka: mehrere Wochenenden Arbeit mit fraglichem Nutzen für eine Fernbedienung).

Das Skript zum erzeugen der Pointertabellen aus der Firmware kann ich gerne irgendwo hochladen.. Ist hässlicher, wüster Perlcode Die Linkerskripts um die Anwendung an eine andere Adr. ins Flash zu linken auch..

Viele Grüße,

Sebastian

[Permalink](http://bettyhacks.com/forum/index.php?topic=181.msg1240#msg1240)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
