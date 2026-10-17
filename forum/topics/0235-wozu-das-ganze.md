---
title: "Wozu das Ganze?"
topic_id: 235
board: "Allgemeines"
board_id: 8
posts: 15
first_post: "04. Mär 2010, 15:04"
last_post: "01. Apr 2010, 19:00"
authors: ["Megabug", "Minze", "Telekatz", "famos", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=235.0"
---

# Wozu das Ganze?

[← Allgemeines](../boards/08-allgemeines.md) · Thema 235 · 15 Beiträge · 04. Mär 2010, 15:04 – 01. Apr 2010, 19:00

Beteiligt: Megabug, Minze, Telekatz, famos, netguy

---

<a id="msg1609"></a>

## 1. Minze · 04. Mär 2010, 15:04

Schönen guten Tag!

Scheinbar ist hier im Forum nicht allzuviel los, aber manchmal scheint sich ja noch jemand hierher zu verirren.
Ein Bekannter hat mir eine [Bettyfernbedienung](https://web.archive.org/web/2012/http://www.netzwelt.de/images/articles/betty-set_1170420654.jpg) gegeben und gefragt, ob ich ihm so einen Adapter löten kann.

Ich habe mich auf der Wiki-Seite umgesehen und finde diesen hier ganz sympathisch: [Simple Serial V2](../../pages/Simple%20Serial%20Interface.md).
Da der im Prinzip auch nix anderes macht, als ein Adapter, mit dem man einen Atmega über die RS232 mit dem Rechner "sprechen" lässt, sollte das nicht schwer aufzubauen sein.
Sicher wäre das in einer Stunde fertig aufgebaut, allerdings frage ich mich, wozu das Ganze?

Ich habe von diesem Menschen, der mir das Ding gegeben hat, erfahren, dass man da irgendwas per Telefondose machen können soll. Das war alles ganz schön vage.
Nun, also ich wüsste gern, was man denn mit dieser Fernbedienung nun genau anfängt? Wenn ich den Adapter gebaut habe und die Verbindung mit dem Rechner funktioniert, wie geht es dann weiter?
Ich habe weder auf der Wiki-Seite noch hier im Forum was lesen können, was mir das befriedigend benatwortet hätte.
Scheinbar bauen sich die meisten daraus eine Fernbedienung für IPod, Steckdosen und Mediaplayer.

Außerdem wüsste ich noch gern, ob an die Schaltung noch was rangehört? Da steht ja, dass den Transistoren die Basisiwiderstände fehlen. Da sind jeweils 10k sicher ok, es geht ja nur darum, die Pegel zu heben, bzw. zu senken.
Ich hab vor Wochen, als ich die Fernbedienung bekommen habe, eine Seite gefunden auf der stand, dass zunächst EINT und dann RESET angehoben werden müssen oder so ähnlich. Ich kann diese Seite aber nicht mehr finden (Hatte in der Zwischenzeit Prüfungen und deswegen alles wieder vergessen).
Also wenn ich diesen SimpleSerialV2 nachbaue und den über die 9polige mit dem Rechner verbinde, dann kann ich da mit AVRTerm was auslesen, oder wie ist das?

Klingt ja eigentlich sehr interessant die ganze Sache, wenn's nur soviel gäbe, was man wirklich fernsteuern müsste...

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1609#msg1609)

---

<a id="msg1616"></a>

## 2. Minze · 07. Mär 2010, 20:18

Es weiß also niemand, warum er das macht?

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1616#msg1616)

---

<a id="msg1619"></a>

## 3. famos · 08. Mär 2010, 21:44

Hallo Minze,

 *Ich habe mich auf der Wiki-Seite umgesehen und finde diesen hier ganz sympathisch: Simple Serial V2.
Da der im Prinzip auch nix anderes macht, als ein Adapter, mit dem man einen Atmega über die RS232 mit dem Rechner "sprechen" lässt, sollte das nicht schwer aufzubauen sein.
Sicher wäre das in einer Stunde fertig aufgebaut, allerdings frage ich mich, wozu das Ganze?*

Ein Adapter ist nötig um die Pegel der RS232- und Betty Schnittstelle anzupassen. RS232 arbeitet mit +/-12V Pegeln und die Betty mit 0/3.3Volt.

*Ich habe von diesem Menschen, der mir das Ding gegeben hat, erfahren, dass man da irgendwas per Telefondose machen können soll. Das war alles ganz schön vage.
Nun, also ich wüsste gern, was man denn mit dieser Fernbedienung nun genau anfängt? Wenn ich den Adapter gebaut habe und die Verbindung mit dem Rechner funktioniert, wie geht es dann weiter?
Ich habe weder auf der Wiki-Seite noch hier im Forum was lesen können, was mir das befriedigend benatwortet hätte.
Scheinbar bauen sich die meisten daraus eine Fernbedienung für IPod, Steckdosen und Mediaplayer.*

Das mit dem Anschliessen an die Telefondose ist überholt. Das war mal als es BettyTV noch gab.
Was man mit der Fernsteuerung letztendlich macht ist jedem selbst überlassen. Weil man die Funktionen selbst programmieren kann ist sehr vieles möglich. Ausser als TV Fernbedienung wäre es auch möglich sie als Ersatz für die Fernsteuerung des Garagentoröffners zu gebrauchen.

 *Außerdem wüsste ich noch gern, ob an die Schaltung noch was rangehört? Da steht ja, dass den Transistoren die Basisiwiderstände fehlen. Da sind jeweils 10k sicher ok, es geht ja nur darum, die Pegel zu heben, bzw. zu senken.
Ich hab vor Wochen, als ich die Fernbedienung bekommen habe, eine Seite gefunden auf der stand, dass zunächst EINT und dann RESET angehoben werden müssen oder so ähnlich. Ich kann diese Seite aber nicht mehr finden (Hatte in der Zwischenzeit Prüfungen und deswegen alles wieder vergessen).
Also wenn ich diesen SimpleSerialV2 nachbaue und den über die 9polige mit dem Rechner verbinde, dann kann ich da mit AVRTerm was auslesen, oder wie ist das?*

Die Schaltung des simpe serial Interface müsste eigentlich funktionieren, so wie sie gezeichnet ist.

 *Klingt ja eigentlich sehr interessant die ganze Sache, wenn's nur soviel gäbe, was man wirklich fernsteuern müsste*

Du kannst auch was anderes daraus machen. Wenn Du noch ein Mikrophon anschliesst, kannst Du die Betty auch als audio Spectrometer brauchen.
Oder Du kannst damit die Signale des Funkthermometer empfangen, vorausgesetzt es gelingt dir das Protokoll zu entschlüsseln.
Auch wenn Du all die Ideen aus dem Forum nimmst sind die Möglichkeiten noch lange nicht ausgeschöpft.
Also her mit deinen Ideen, umsetzen und im Forum posten.

Viel Erfolg
famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1619#msg1619)

---

<a id="msg1627"></a>

## 4. Minze · 15. Mär 2010, 15:11

Hey,
ich hatte deinen Beitrag gelesen, aber versäumt, darauf zu antworten.
Ich werde dem das einfach zusammenlöten und gut.
Als ich mir das "Datenblatt" angesehen habe, hab ich mich geärgert, dass das Display scheinabr über hundert Anschlüsse hat!
Nokia-Displays lassen sich ja auch mit weit weniger Datenleitungen pixelgenau ansteuern.
Solche Fernbedienungen zu kaufen und das Display auszubauen scheint also nicht so sinnvoll zu sein...

Wie dem auch sei,
ich danke dir für deine Antwort!

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1627#msg1627)

---

<a id="msg1628"></a>

## 5. netguy · 18. Mär 2010, 12:35

"Als ich mir das "Datenblatt" angesehen habe, hab ich mich geärgert, dass das Display scheinabr über hundert Anschlüsse hat!"

Darf man erfahren in welches Datenblatt du da geschaut hast? Tatsächlich hat das Display in der Betty eine ziemliche Standard-Schnittstelle: 8 Datenleitungen, Register-Select, Read/Write, etc... Alles in allem weniger als 20 Leitungen.

Falls du dich fragst was man mit der Betty noch so anstellen kann: Nun, es ist quasi eine komplette, kleine ARM7 basierte Plattform. Damit kann man doch recht viel machen. Hängt halt davin ab was für Ideen Du hast

Grüße,

Chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1628#msg1628)

---

<a id="msg1629"></a>

## 6. Minze · 18. Mär 2010, 16:50

Hehe, da habe ich wohl LPC mit LCD verwechselt :-D
Wahrscheinlich habe ich mir [das hier](../../pages/LPC2220%20Pin-Belegung.md) angesehen.

Ich habe aber noch eine Frage:
Im Plan zum [Simple Serial Interface](../../pages/Simple%20Serial%20Interface.md) gehen 4 Leitungen zur Fernbedienung (TxD, RxD, Reset und EInt). Pin 5 & 6 der "Schnittstelle" werden einfach mit VCC und GND bezeichnet.
Muss ich also zusätzlich zum Festspannungsregler (5V) für den Max232 noch einen 3,3V für die Ferbedienung einbauen?

Ich wunder mich, weil die Spannungsversorgung des Max232 links neben dem Stecker ohne jeden Spannungsunterschied eingezeichnet ist.
Aber der Max232 wird ja wohl nicht mit nur 3,3V laufen und die Fernbedienung nicht besonders lang mit 5V. Ist das einfach nur Bequemlichkeit des Zeichners gewesen oder hab ich was nicht verstanden?

Und kann mir jemand sagen, wie ich testen kann, ob die Schaltung funktioniert
Ich möchte da nix neues draufspielen, dass soll der selber machen. Ich möchte nur mal fix testen, ob die Schaltung so passt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1629#msg1629)

---

<a id="msg1630"></a>

## 7. Telekatz · 18. Mär 2010, 18:43

> **Zitat**
>
> Muss ich also zusätzlich zum Festspannungsregler (5V) für den Max232 noch einen 3,3V für die Ferbedienung einbauen?

Du musst überhaupt keinen Spannungsregler einbauen, die Schaltung wird von der Fernbedienung mit 3,3V versorgt.

> **Zitat**
>
> Aber der Max232 wird ja wohl nicht mit nur 3,3V laufen

Darum nimmt man ja auch einen MAX3232.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1630#msg1630)

---

<a id="msg1631"></a>

## 8. Minze · 18. Mär 2010, 21:21

Da muss ich den ja wieder auslöten. Hab sogar einen Gleichrichter davorgesetzt, damit er das nicht falsch anschließen kann.
Aber da bin ich ja froh, dass ihr hier so kompetent seid, vielleicht sollte ich mich doch mal mit diesem Projekt auseinandersetzen.

Einen schönen Abend wünsche ich noch!

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1631#msg1631)

---

<a id="msg1632"></a>

## 9. Megabug · 22. Mär 2010, 10:33

> **Zitat von: Minze am 18. Mär 2010, 21:21**
>
> vielleicht sollte ich mich doch mal mit diesem Projekt auseinandersetzen.

Keine schlechte Idee.

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1632#msg1632)

---

<a id="msg1633"></a>

## 10. Minze · 28. Mär 2010, 22:30

Ich muss mich leider nochmal melden:
Nachdem ich Gleichrichter, Regler und Glättungselkos wieder abgelötet habe, bleiben ja nur noch wenige Teile auf dem Brett übrig.
Wenn ich die Fernbedienung nun anschließe, bekomme ich folgende Meldung beim Sichern des Flash-Inhaltes:
RX: Timeout
Synchronisation gescheitert

- Ich habe [den Hinweis](0152-handydatenkabel-und-betty-heaven.md#msg1280) gefunden, zwischen Tx und Masse 4,7k-Ohm zu legen. Da ging es zwar um Handykabel, hab es trotzdem probiert, bringt nix

- Schaltung kontrolliert. Wie gesagt, viel bleibt ja nicht übrig, das scheint aber zu stimmen

- [Kabel getauscht](https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=188.msg1275#msg1275)

- Schnittstelle kontrolliert: Habe über diese Schnittstelle den Inhalt eines Atmega ohne Probleme ausgelesen.

- Anzeige der Betty: Wenn ich die Batterien einlege, kommt eine Meldun, dass Kontakt aufgenommen wird. Wenn ich die Stecker des Adapters einstecke, geht das Display aus. So soll's ja auch sein, wenn ich das richtig verstanden habe.

Was mir noch einfällt:

- Habe den "BC547C" benutzt. Aber entspricht die Pinbelegung wirklich [dieser hier](https://web.archive.org/web/2012/http://www.datasheetcatalog.org/datasheet/SGSThomsonMicroelectronics/mXytvtz.pdf)?

- richtige Kondensatoren genommen? Auf den 1µF müsste 150 stehen, auf dem mit 100µF müsste 107 stehen. Sind diese Werte kritisch? Hab sie nah an den MAX gelötet

Sofern jemand einen Tipp hat, wär ich dankbar!
Gute Nacht,
Martin

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1633#msg1633)

---

<a id="msg1634"></a>

## 11. Telekatz · 29. Mär 2010, 08:47

> **Zitat**
>
> richtige Kondensatoren genommen? Auf den 1µF müsste 150 stehen, auf dem mit 100µF müsste 107 stehen. Sind diese Werte kritisch? Hab sie nah an den MAX gelötet

Laut Datenblatt des MAX3232 reichen 100nF. Probier es mal damit.

Häng die Schaltung (ohne Betty) zum testen mal an ein Netzteil mit 3,3V und schließ TX und RX am Stecker zur Betty kurz.  Starte ein Terminalprogramm und prüfe ob eingegebene Zeichen wieder zurück gesendet werden.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1634#msg1634)

---

<a id="msg1635"></a>

## 12. Minze · 29. Mär 2010, 14:12

Bevor ich vergesse, was ich alles gemacht habe, poste ich das besser mal:

Habe zunächst einfach TxD & RxD über einen Pfostenstecker und einen Jumper kurzgeschlossen, 3,3V über einen Regler angelegt.
AVRTerm zeigt absolut nichts an, wenn ich sende. Von Echo keine Spur.

Dann hab ich einen normalen MAX232 reingesteckt, 5V angelegt, auch hier wird nichts angezeigt.

Hab dann die Grundbeschaltung eines Max232 (in beiden Varianten) auf einem Steckbrett aufgebaut (nur die Kondensatoren un die Spannungsversorgung). Bei Kurzschluss von TxD & RxD wird wieder nichts angezeigt. Die 3,3V, bzw. 5V lagen an Pin 2 & 16 an, so wie's sein soll.

Zwischendurch habe ich nach, bzw. vor jedem Schritt einen Atmega beschrieben, um die Funktion der Schnittstelle zu testen.

Sonderbarerweise bekommt der Rechner also keinerlei Input über die RS232. Ob er überhaupt was sendet, müsste ich mal mit einem Oszilloskop messen, aber das steht in der anderen Ecke des Raumes, eingebaut in einen Haufen Krempel...
Im Moment bin ich ratlos und es ärgert mich irgendwie, dass mir dieser winzige Adapter so viele Nerven kostet.

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1635#msg1635)

---

<a id="msg1636"></a>

## 13. Minze · 31. Mär 2010, 11:40

Schönen guten Morgen!

Ich konnte das Problem nun lösen:
Der Fehler war, dass die Pinbelegung der RS232 im Plan "falsch" aufgezeichnet ist.
Ich habe nur die Nummern beachtet, die direkt auf dem Stecker im Schaltplan stehen, nicht aber die dahinter.
Auf die Lösung bin ich gekommen, als ich systematisch vorgegangen bin:
Das Echo kam nicht einmal, als ich Tx und Rx direkt am Schnittstellenkabel verbunden habe.
Also musste was an der Belegung falsch sein, da das Kabel an sich ja funktioniert (hab ja die Atmegas gelesen/beschrieben).
Dann bin ich schnell drauf gekommen, dass Rx und Tx eben woanders sein müssen.

Naja, ich schieb den Fehler mal jetzt weit weg von mir. Es wär ja durchaus möglich gewesen, die Steckerbelegung gleich richtig einzuzeichnen, die Kabel kreuzen sich ja sowieso.

Ich danke für eure Hilfe!

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1636#msg1636)

---

<a id="msg1637"></a>

## 14. Telekatz · 31. Mär 2010, 19:18

"Falsch" ist die Steckerbelegung nicht.

Die Belegung an JP6 wurde so gewählt, dass man ein Flachbandkabel mit aufgequetschten D-Sub Stecker kreuzungsfrei anlöten kann.  Sie entspricht der Pinreihenfolge von der eine Seite des D-Sub Steckers zur anderen Seite.

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1637#msg1637)

---

<a id="msg1638"></a>

## 15. Minze · 01. Apr 2010, 19:00

Hm, ich hätt ja auch besser aufpassen können/müssen. Deswegen hab ich das falsch in Anführungszeichen gesetzt.
Ich glaub, ich hab mich hier in diesem Thread erfolgreich als weltgrößten Noob zur Schau gestellt 
Wahrscheinlich bin ich der einzige Nutzer, dessen Status da links unter dem Namen sich nicht ändert 
Es läuft eben nicht immer alles wie's soll...

[Permalink](http://bettyhacks.com/forum/index.php?topic=235.msg1638#msg1638)

---

## Verwandte Themen

- [Handydatenkabel und Betty Heaven](0152-handydatenkabel-und-betty-heaven.md)

[← Zurück zu Allgemeines](../boards/08-allgemeines.md) · [Gesamtindex](../index.md)
