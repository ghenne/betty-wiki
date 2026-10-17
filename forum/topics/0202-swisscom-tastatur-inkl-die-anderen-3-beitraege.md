---
title: "Swisscom: Tastatur (inkl die anderen 3 Beiträge)"
topic_id: 202
board: "Software"
board_id: 6
posts: 13
first_post: "02. Mai 2009, 00:24"
last_post: "05. Mai 2009, 07:41"
authors: ["JimBeam", "Telekatz", "bn", "famos", "gerdi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=202.0"
---

# Swisscom: Tastatur (inkl die anderen 3 Beiträge)

[← Software](../boards/06-software.md) · Thema 202 · 13 Beiträge · 02. Mai 2009, 00:24 – 05. Mai 2009, 07:41

Beteiligt: JimBeam, Telekatz, bn, famos, gerdi

---

<a id="msg1376"></a>

## 1. gerdi · 02. Mai 2009, 00:24

Die Tastatur der Swisscom reagiert auf Bit 30 von FIOPIN0.
Die Tastatur der Swisscom reagiert auf IOPIN1 statt IOPIN3!!!

Diese beiden muss man vertauschen!!!! (In keyirq.c)

*Last Edit : 02. Mai 2009, 00:27 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1376#msg1376)

---

<a id="msg1377"></a>

## 2. famos · 02. Mai 2009, 14:17

Da bei der DE Betty die Keymatrix auf Port P3 und P0 verteilt ist und bei der Swisscom Betty nicht, da ist alles auf P1, kannst Du den
 `keys[0] |= FIOPIN0>> 5;
keys[0] |= (IOPIN3 & MASK3) >> 18;`
vereinfachen, da kommen alle Rows auf IOPIN1 rein. Die Positionen und Belegung ist aber anderst.
Die Mask und Shift Operationen haben den Zweck die 42 Tasten auf zwei Wörter zu verteilen. Jeder Taste ist also ein Bit im keys[0] oder keys[1] zugeordnet.
Übrigens die Mask Funktion wird bei FIOPIN0 über die Hardware gemacht. Das geht aber, soweit ich mich noch erinnern kann, mit Port 1 nicht. Ich suche bei Gelegenheit mal das was ich habe zusammen. Überigens nicht vergessen die Port Initialisierungen anzupassen.

Gruss famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1377#msg1377)

---

<a id="msg1379"></a>

## 3. gerdi · 02. Mai 2009, 15:17

Famose Informationen!

Bisher bekomme ich auf IOPIN1 nur die Spalten der Tastenmatrix aus einem anderen Beitrag.

Vielleicht hat das mit der Port-Initialisierung zu tun.
Was soll ich da tun?
Einfach 0 nach IODIR1 schreiben? (Alles Eingabe)
Wo soll ich das tun? (In main.c vor der Eingabeschleife?)

(Übrigens:
In
lpc2220.h steht bei FIODIR0   0x3FFFC000
Stimmt die Adresse?
Ich würde eher 0x3FFFC020 erwarten.)

IOPIN2 habe ich nicht so recht verstanden.
Was soll das, dass in regelmässigen Abständen ein einzelnes Bit verschoben wird?
Wer fragt danach?

> **Zitat**
>
> Die Mask und Shift Operationen haben den Zweck die 42 Tasten auf zwei Wörter zu verteilen. Jeder Taste ist also ein Bit im keys[0] oder keys[1] zugeordnet.

Das habe ich aus dem Quelltext bereits verstanden. Die Tastenbelegung ist in keyboard.h.

*Last Edit : 02. Mai 2009, 15:23 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1379#msg1379)

---

<a id="msg1380"></a>

## 4. gerdi · 02. Mai 2009, 18:44

Ich glaube, dass ich kurz davor stehe, die Tastatur von Swisscom mit Boop zum laufen zu bringen.

Ich kann bereits:
- überprüfen, ob eine Taste gedrückt ist (FIOPIN0 Bit 30)
- die Spalte der Tastenmatrix angeben (IOPIN1), zu einer gedückten Taste.

Nun möchte ich die Zeile der Matrix der gedrückten Taste.
Stimmt es, dass diese Zeilen bei der Swisscom ebenfalls in IOPIN1 gespeichert sind?
Warum erscheinen sie nicht bei mir?

Muss ich eine PINSEL-Einstellung einfügen?

Danke für jede Hilfe.

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1380#msg1380)

---

<a id="msg1381"></a>

## 5. Telekatz · 02. Mai 2009, 21:35

P2.18-24 werden als Ausgang konfiguriert (Zeile), P1.16,17,18,19,21 und 22 als Eingang (Spalte).

Um herauszufinden welche Taste gedrückt ist wird eine der Zeilen auf Low Pegel gelassen und die anderen Zeilen auf High Pegel gelegt. Anhand des Bitmusters der Spalten kannst du nun sehen, welche Taste dieser Zeile gedrückt ist.

Dasselbe wiederholst du nun mit den Restlichen Zeilen. Zum Schluss des Tastaturscanns nicht vergessen alle Zeilen wieder auf Low zu legen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1381#msg1381)

---

<a id="msg1384"></a>

## 6. gerdi · 02. Mai 2009, 23:22

Wow!
Vielen Dank!

Jetzt glaube ich habe ich es verstanden.

Das ist also der Grund warum IOPIN2 bitweise von 18-24 läuft!

Oder?

Am Montag werde ich es gleich ausprobieren.

Ich bin voller Hoffnung!!!

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1384#msg1384)

---

<a id="msg1385"></a>

## 7. bn · 03. Mai 2009, 10:32

Hallo Gerdi,

Du moechtest Betty fuer Hausautomatisierung via LAN einsetzen? Das will ich auch.

Ich arbeite derzeit an einem Empfaenger auf Basis von CUL ([http://busware.de](https://web.archive.org/web/2012/http://busware.de)), der als Ethernet-Adapter fungiert, und von der Betty via CC1101 empfangene Ethernet-Frames weiterleitet (Software: CULeth, siehe [http://developer.berlios.de/projects/culeth/).](https://web.archive.org/web/2012/http://developer.berlios.de/projects/culeth/).)

Grundidee: auf dem PC laeuft ein Server, der via CULeth per UDP oder TCP/IP mit den Bettys kommuniziert. Kommandos von der Betty werden vom Server angenommen und an die Hausautomatisierungskomponenten weitergereicht. Die Zustaende des Hauses koennen vom Server abgefragt und auf der Betty visualisiert werden.

Gesucht wird jemand, der Adam Dunkels' IP-Stack auf der Betty implementiert, damit man eine Kommunikationsschicht zwischen PC und Betty hat.

Gruesse,
bn

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1385#msg1385)

---

<a id="msg1388"></a>

## 8. gerdi · 03. Mai 2009, 22:32

Du jagst mir hier einen grossen Schrecken ein!!!

Ich hoffe, dass es nicht notwendig wird auf der kleinen, armen Betty Swisscom einen IP Stack zu implementieren, um mit dem Netzwerk zu kommunizieren.

Ich dachte an eine Art Funk-Null-Modem Lösung.

Die Betty schickt per Funk über ein serielles Protokoll Daten an den TAE-Adapter.
Ich habe einen Voip-Telefon-Adapter (Zyxel 2002L AOL, legal gecrackt zum Debranding).
Den habe ich vor Jahren für 4 Euro ersteigert. Seitdem ersetzt das Internet meinen Telefonanschluss zuverlässig.

Dieser Voip-Adapter hat noch einen Anschluss frei.
Dort kommt der TAE hinein (eigentlich RJ-xx bei der Swisscom).

Der Voip-Adapter übernimmt selbständig den Lan Verbindungsufbau.
Der Voip-Adapter bestimmt die IP-Adresse.
Der Voip-Adapter bestimmt den Port.
Der Voip-Adapter bestimmt die IP-Adresse des VOIP-Anbieters (Das werde ich kurzschliessen auf meinen eigenen Domainnamen.)

Ich hoffe, dass die Funkverbindung zwischen Betty und TAE programmtechnisch eine gewöhnliche serielle Verbindung ist.
Hoffentlich erhalte ich von Dir oder Famos oder Telekatz weitere Details.

Um die Ethernet/Lan-Verbindung soll sich meine Betty nicht kümmern.

Den Browser möchte ich nicht direkt auf der Betty laufen lassen, sondern auf dem Server. Die Betty soll nur seriell Eingaben und Ausgaben des Servers auf einfache Weise steuern und anzeigen.

*Last Edit : 04. Mai 2009, 09:09 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1388#msg1388)

---

<a id="msg1389"></a>

## 9. bn · 04. Mai 2009, 16:32

Hallo,

an irgendeiner Stelle muss die Verpackung der von/an Betty gesendeten applikationsspezifischen Daten in ein Netzwerkprotokoll (TCP oder UDP) ja erfolgen. Ich lese heraus, dass Du das via TAE-Adapter in Deinem VOIP-Adapter machen willst. Um das hinzubekommen, musst Du wahrscheinlich mindestens noch ein Reverse Engineering des TAE-Adapters angehen - weiss nicht, ob das schon jemand gemacht hat.

Ich habe mich aus mehreren Gruenden fuer IP entschieden:
- TCP/IP oder UDP stellen paketorientierte Standardprotokolle dar, ueber die jegliche Applikation auf der Betty mit jeglicher Applikation auf jedem beliebigen PC in meinem Heimnetzwerk sprechen kann.
- Ich habe drei Bettys (fuer jedes Stockwerk eine), die so gesondert angesprochen werden koennen (jede Betty eine IP-Adresse in derselben Collision Domain on air).
- Es gibt einen fertigen freien IP-Stack fuer ARM (von Adam Dunkels), den man nur auf eine geeignete Implementierung des OSI Layer 2 (Data Link-Schicht) aufsetzen muss. Die Data Link-Schicht waere hierbei die Paketkommunikation "on air" des CC1101.

Die Implementierung der Gegenseite im CUL habe ich bis auf die Funkverbindung fertig.

Bettyseitig wuerde dann z.B. ein kleines Menue genuegen (z.B. eine Liste der Funkschaltsteckdosen mit an/aus-Knopf). Die Befehle des Menues wuerden in das anwendungsspezifische Protokoll verpackt und dann via UDP oder TCP/IP an die IP-Adresse des Heimservers geschickt. Der wertet sie aus und initiiert dann die jeweiligen Aktionen bzgl. Funkschaltsteckdosen. Ist die IP-Verbindung ersteinmal implementiert, sind der Fantasie keine Grenzen mehr gesetzt.

Gruesse,
bn

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1389#msg1389)

---

<a id="msg1391"></a>

## 10. gerdi · 04. Mai 2009, 19:09

Ich hatte eigentlich vor den TAE-Adapter im Orginal zu lassen.
Er sendet Daten an eine Telefonnummer.

Ich bin selber der Telefonserver.
Wenn die Daten bei mir ankommen werfe ich die Telefonnummer weg und nehme nur die Daten.

Auf der Serverseite werde ich nur ein Telnet ansetzen. Dann werde ich schon sehen, was ankommt.

Das einzige Problem ist die Kommunikation zwischen der Betty und dem TAE.

Kannst du mir einen Tip geben,wie ich mit dem TAE von der Betty aus kommuniziere?
Vielleicht könnten mir Telekatz oder Famos helfen?

*Last Edit : 04. Mai 2009, 19:20 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1391#msg1391)

---

<a id="msg1395"></a>

## 11. JimBeam · 04. Mai 2009, 20:36

Ich fürchte, so einfach wird das nicht sein... Die Betty hat sich ja ursprünglich mit dem TAE Adapter über ein (meines Wissens) nicht bekanntes Protokoll unterhalten - dort wurden Daten bzgl. irgendwelcher Spielstände, Quizzes etc. übermittelt. Der TAE Adapter hat dann eine Verbindung zu einem Server aufgebaut und wieder mittels eines "Geheimcodes" mit diesem kommuniziert. Das letztgenannte Protokoll könntest Du Dir in der Tat über Deinen Telefonserver anschauen - vorausgesetzt, Du kennst das erstgenannte Protokoll zwischen Betty und TAE um diesen Vorgang anzustoßen...!
Ich fürchte noch viel weniger wird es Dir ohne Kenntnis dieses Protokolls gelingen, den TAE Adapter dazu zu bewegen einfach *irgendwelche* von Betty geschickten Daten auf die Telefonleitung zu schicken - wenn das überhaupt vorgesehen ist!
Das meinte bn damit, daß es wohl nötig sei, den TAE Adapter oder die entsprechenden Routinen in der Original-Betty-Software "reverse-zu-engineeren" .

Allerdings soll Dich das nicht abhalten, es trotzdem zu versuchen - denn die Idee dahinter finde ich durchaus gut!

JimBeam

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1395#msg1395)

---

<a id="msg1396"></a>

## 12. gerdi · 04. Mai 2009, 20:56

War die RF-Kommunikation verschlüsselt?
Hatte jedes Gerät einen eigenen Schlüssel?(Kann man einen TAE nur für eine feste Betty verwenden?)

Ich dachte, Grundlage würde ein serielles Protokoll wie SLIP oder PPP sein? Ist das falsch?
Auf diesem Protokoll muss noch ein höheres liegen.

Ist jemand hier im Forum hardwaremässig in der Lage die RF-Kommunikation zwischen einer Standard-Betty und dem TAE-Adapter zu belauschen?

("Seriell" habe ich korrigiert, als ich meinen Fehler in einem Zitat entdeckte.)

*Last Edit : 05. Mai 2009, 17:03 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1396#msg1396)

---

<a id="msg1399"></a>

## 13. JimBeam · 05. Mai 2009, 07:41

> **Zitat von: gerdi am 04. Mai 2009, 20:56**
>
> War die RF-Kommunikation verschlüsselt?

Nein, für die Übertragung selbst bietet der CC1100 ein paketorientiertes Protokoll.
> **Zitat von: gerdi am 04. Mai 2009, 20:56**
>
> Hatte jedes Gerät einen eigenen Schlüssel?(Kann man einen TAE nur für eine feste Betty verwenden?)

Ich denke schon, denn es wäre ja denkbar, daß in der Nachbarwohnung ebenfalls jemand eine Betty hat - und die dürfen sich ja schließlich nicht gegenseitig beeinflussen.
> **Zitat von: gerdi am 04. Mai 2009, 20:56**
>
> Ich dachte, Grundlage würde ein Netzwerkprotokoll wie SLIP oder PPP sein? Ist das falsch?

Ich fürchte ja...
> **Zitat von: gerdi am 04. Mai 2009, 20:56**
>
> Auf diesem Protokoll muss noch ein höheres liegen.

Oder das Ganze ist rund um ein komplett anderes aufgebaut - was sehr wahrscheinlich ist, denn es ging ja bei den Betty-Games auch um Geld! Da hat man sicher Vorkehrungen getroffen, daß nicht jeder die Daten lesen/manipulieren kann.
> **Zitat von: gerdi am 04. Mai 2009, 20:56**
>
> Ist jemand hier im Forum hardwaremässig in der Lage die RF-Kommunikation zwischen einer Standard-Betty und dem TAE-Adapter zu belauschen?

Wie gesagt - es ist nicht das Problem, die RF-Kommunikation zu belauschen, das wurde meines Wissens bereits getan. Zum heutigen Stand ist nicht mal das mehr möglich, denn der Betty-Server existiert ja nicht mehr, also wird das Protokoll (bis auf den Versuch eines Verbindungsaufbaus) auch nicht aktiv werden.

Nochmal: das Problem ist, entweder
a) auf der Betty eine Software zu implementieren, die die bestehende Software im TAE Adapter dazu zu bewegt, Deine - wie auch immer gearteten - Daten über die Telefonleitung zu jagen...
oder
b) eine Software für den TAE Adapters zu schreiben, die das tut.

JimBeam

[Permalink](http://bettyhacks.com/forum/index.php?topic=202.msg1399#msg1399)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
