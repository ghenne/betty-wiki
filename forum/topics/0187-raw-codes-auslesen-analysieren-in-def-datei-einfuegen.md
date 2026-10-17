---
title: "RAW-Codes auslesen/analysieren/in def-Datei einfügen"
topic_id: 187
board: "Software"
board_id: 6
posts: 13
first_post: "22. Jan 2009, 06:51"
last_post: "26. Jan 2009, 09:32"
authors: ["El_Barto", "Telekatz", "damaltor", "eme", "pcsquirrel"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=187.0"
---

# RAW-Codes auslesen/analysieren/in def-Datei einfügen

[← Software](../boards/06-software.md) · Thema 187 · 13 Beiträge · 22. Jan 2009, 06:51 – 26. Jan 2009, 09:32

Beteiligt: El_Barto, Telekatz, damaltor, eme, pcsquirrel

---

<a id="msg1249"></a>

## 1. El_Barto · 22. Jan 2009, 06:51

Hi, ich würde gerne die per IR-Capture aufgenommenen RAW-Codes auslesen, so dass ich diese in eine eigene Fernbedienungsdefinition übernehmen kann.
Hintergrund ist folgender: Ich habe eine Philips RC5 Fernbedienung mit farbigen Sondertasten, welche sich mit LIRC nicht analysieren lässt. Die Betty erkennt die RAW-Codes aber problemlos und simuliert die Originalfunktion. In den Verschiendenen LIRC-Files auf der LIRC-Page ist zwar teilweise ein code vorhanden, jedoch wechseln dabei komischerweise immer die RC5-Adressbytes. Ich gehe also davon aus dass die Sonderfunktionen je nach TV einen anderen Adresscode haben. Und den für meinen TV habe ich leider noch nicht gefunden. Aus den RAW-Daten erhoffe ich mir nun mehr Infos zur verwendeten Codierung usw. Ich hoffe nur bei dem Code für meine FB handelt es sich nicht um eine Erweiterung des "klassischen" RC5.
Ohne mich nun zeitaufreibend durch die linkerscripts usw zu hangeln und dann die entsprechende Flash-Stelle auszulesen dachte ich mir ich frage bei euch einfach mal nach.
Kann diese Vorgehensweise so funktionieren? Wer weiß evtl wo diese Infos im Flash stehen? Gibts einfachere Möglichkeiten einen IR-Code in eine def zu übernehmen, vielleicht mit dem Test-IR-Capture woe die Pulszeiten usw angegeben werden?

Eine weitere Frage: Müssen die def-Dateien für die Fernbedienungen in einer speziellen Codierung vorliegen? Mit einer leicht erweiterten Kopie des generic-beispiels schmiert mir die Betty beim Auswählen des Profils immer ab und zeigt (fast blaue) Linien auf dem Display an. Nach einem Neustart frisst er das Profil aber und einige der Codes funktionieren. Die geänderte Datei wird dabei wie die Originaldatei (die problemlos läuft) im Unix-Format gespeichert.

So, das waren meine wichtigsten Fragen. Ich arbeite mich gerade erst in die Umgebung der Betty ein. Bin aber von dem bisherigen Softwaregerüst nach einem ersten vorsichtigen Kontakt damit ganz beeindruckt von der Arbeit der Urheber. Eine einheitliche Toolchain mit GCC ist prima. Also Hut ab davor! 
Ich hoffe in naher Zukunft auch einige dazu beisteuern zu können.
Danke
El_Barto

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1249#msg1249)

---

<a id="msg1250"></a>

## 2. damaltor · 22. Jan 2009, 11:07

hol dir mal per svn das letzte snapshot von boop, seit einigen versionen gibt es ein filesystem im flash #2 welches alle einstellungen und profile über die neustarts behalten sollte. für deine IR-Captures kann ich dir aber leider auch nicht helfen...

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1250#msg1250)

---

<a id="msg1252"></a>

## 3. Telekatz · 22. Jan 2009, 12:14

Die Informationen, die für die RAW Codes im Flash abgespeichert werden, sind im Grunde ähnlich denen, die mit der Test-IR-Capture Funktion angezeigt werden. Deshalb ist es am einfachsten wenn du diese Informationen nimmst. Analysieren, welches Protokoll das ist, musst du aber selber.

Die Daten sind wie bereits gesagt im zweiten Flash abgespeichert. Den Anfang findet man am leichtesten indem man nach RC01 gefolgt vom eingegebenen Namen sucht. Kann allerdings auch mehrfach im Flash vorkommen, da bei einer Änderung der Daten unter gewissen Umständen die alte Version als veralten markiert und neu im Flash abgespeichert wird. Die Daten sind in einer struct vom Typ "struct RAWset_" (Definition in ir_capture.h) abgelegt.

Die blaue Linien deuten darauf hin, dass versucht wird einen zu langen Text auf dem Display auszugeben. Eventuell Nullterminierung vergessen.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1252#msg1252)

---

<a id="msg1253"></a>

## 4. pcsquirrel · 22. Jan 2009, 12:37

Du kannst den Ouput der Test-IR-Capture Funktion hier mal posten. vielleicht kann ich dir dann beim herausfinden des codes helfen.

pcsquirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1253#msg1253)

---

<a id="msg1254"></a>

## 5. eme · 22. Jan 2009, 16:07

Falls eine weitergehende Untersuchung gewünscht ist, kann anstelle eines Oszilloskopes auch der Soundkarteneingang mit einer Fotodiode zur Aufnahme des Signals dienen.
Wenn die Trägerfrequenz gemessen werden soll, braucht es einen parallelen Widerstand oder besser eine kleine Operationsverstärkerschaltung als Transimpedanzwandler.
Ansonsten wird die Trägerfrequenz durch die Trägheit / Kapazitäten schon gefiltert.

Es gibt bestimmt auch Software, mit der man die gewonnenen Daten weiter analysieren kann.

[http://people.inf.ethz.ch/mringwal/lirc/](https://web.archive.org/web/2012/http://people.inf.ethz.ch/mringwal/lirc/)
[http://www.minidisc.org/contrib/oded.htm](https://web.archive.org/web/2012/http://www.minidisc.org/contrib/oded.htm)

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1254#msg1254)

---

<a id="msg1256"></a>

## 6. El_Barto · 22. Jan 2009, 21:19

Vielen Dank für die Tips. Ich werde diese heute mal testen und die Ergebnisse hier posten.

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1256#msg1256)

---

<a id="msg1258"></a>

## 7. El_Barto · 23. Jan 2009, 09:37

Also das Problem mit den blauen Linien konnte ich lösen. Es lag an einem zu langen String im Namen des Listeneintrags. Der angezeigte Name hat bei der Bestätigung des Profils den Bildschirm unten rechts "verlassen". Da in der Listenansicht (wo alle Codegruppen stehen) der Anzeigeplatz am kürzesten ist, löste die Anzeige des Namens den Fehler aus.
Mit dem analysieren des von mir benötigten FB.Codes kam ich leider noch nicht viel weiter. Ich vermute es hängt an dem 36kHz TSOP den ich am PC zum samplen benutze.

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1258#msg1258)

---

<a id="msg1260"></a>

## 8. Telekatz · 23. Jan 2009, 11:38

Mach mal ein Bild von dem was die Test-IR-Capture Funktion anzeigt und poste es hier mal.

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1260#msg1260)

---

<a id="msg1261"></a>

## 9. eme · 24. Jan 2009, 11:11

> **Zitat von: El_Barto am 23. Jan 2009, 09:37**
>
> Ich vermute es hängt an dem 36kHz TSOP den ich am PC zum samplen benutze.

Auch wenn ein 36 kHz Bandpass drinsteckt, je nach Signalstärke sollten nahe Frequenzen empfangen werden können. Im Datenblatt müsste dazu ein Diagramm sein.

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1261#msg1261)

---

<a id="msg1263"></a>

## 10. El_Barto · 25. Jan 2009, 07:08

So, übers Wochenende habe ich mal etwas mehr Zeit für die Betty gehabt. Anbei poste ich 4 IR-Samples. Dabei handelt es sich um 2 Samples für eine RC7574 (Philips TV) und 2 Samples von einer Philips SAT-Fernbedienung.
Falls ihr darauf eine Codierung (RC5, RC5e oder RC6) erkennt oder gar einen genauen Code ablesen könnt, würde mich das sehr voran bringen.

Auf der LIRC-Homepage ist zu der RC7574 ein Code zu finden, der ist aber nicht funktioniert.
Blau: 0x0000000000001176
Gelb: 0x0000000000001174

Ich habe das Gefühl dass beide FB eine RC5e oder RC6-Codierung verwenden, da mein RC5-IR-Decoder (TSOP1736 mit ATTiny) für den PC einen Code empfangen kann, welcher aber nicht korrekt ist...

Vielen Dank für eure bisherigen Tipps.

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1263#msg1263)

---

<a id="msg1265"></a>

## 11. Telekatz · 25. Jan 2009, 13:06

Das ist alles Extended RC-5.

Adresse bei den ersten beiden ist 0x00, bei den letzten beiden 0x08. Kommandos sind 0x6f, 0x6d, 0x56 und 0x55.

Mit dieser RC5 Codetabelle müssten diese Kommandos richtig gesendet werden:
`RC5_STD(0x0000), // A  ->
 RC5_STD(0x0000), // B  ->
 RC5_STD(0x0000), // C  ->
 RC5_STD(0x0000), // D  ->
 RC5_STD(0x0000), // Betty ->
 RC5_STD(0x0000), // Exit  ->
 RC5_STD(0x0812), // Up  -> Brightness+
 RC5_STD(0x0813), // Down  -> Brightness-
 RC5_STD(0x0000), // Left  ->
 RC5_STD(0x0000), // Right ->
 RC5_STD(0x0000), // OK  ->
 RC5X(0x0A16),    // Vol+  -> Vol+
 RC5X(0x0A15),    // Vol-  -> Vol-
 RC5_STD(0x080D), // Mute  -> Mute
 RC5_STD(0x0820), // Prog+ -> Prog+
 RC5_STD(0x0821), // Prog- -> Prog-
 RC5_STD(0x0801), // 1  -> 1
 RC5_STD(0x0802), // 2  -> 2
 RC5_STD(0x0803), // 3  -> 3
 RC5_STD(0x0804), // 4  -> 4
 RC5_STD(0x0805), // 5  -> 5
 RC5_STD(0x0806), // 6  -> 6
 RC5_STD(0x0807), // 7  -> 7
 RC5_STD(0x0808), // 8  -> 8
 RC5_STD(0x0809), // 9  -> 9
 RC5_STD(0x0800), // 0  -> 0
 RC5_STD(0x080A), // -/--  ->
 RC5_STD(0x0000), // AV  ->
 RC5_STD(0x0000), // Menu  ->
 RC5_STD(0x0000), // PiP  ->
 RC5_STD(0x0000), // A/B  ->
 RC5_STD(0x0000), // 16:9  ->
 RC5_STD(0x0000), // Info  ->
 RC5_STD(0x0000), // VTX1  ->
 RC5_STD(0x0000), // VTX2  ->
 RC5_STD(0x0000), // VTX3  ->
 RC5X(0x082F),    // Blue  ->
 RC5X(0x082D),    // Yello ->
 RC5_STD(0x0000), // Green ->
 RC5_STD(0x0000), // Red  ->
 RC5_STD(0x0000), // TV  ->
 RC5_STD(0x080C)  // Power -> Standby`

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1265#msg1265)

---

<a id="msg1269"></a>

## 12. El_Barto · 26. Jan 2009, 03:41

@Telekatz: Vielen vielen Dank! Die Codes funktionieren perfekt. Aber warum addierst du 7C0 auf die eigentlichen RC5e-Codes drauf? Komme da nicht ganz dahinter. Habe mich leider noch nicht weit genug in den Sourcecode eingearbeitet.
Beim Compilieren ist noch ein Fehler bei der RC5X-Def aufgetreten. Dort sind 2 Leerzeichen zu viel, so dass die Ersetzung nicht richtig funktioniert. Wie gesagt, sind nur 2 Zeichen, aber damit sich von euch keiner die Mühe machen muss: Anbei ein (2-Leerzeichen) Patch.
Eventuell benötigt ihn ja auch jemand der von C nicht viel versteht.

Gruß
El_Barto

*Last Edit : 26. Jan 2009, 05:59 by El_Barto*

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1269#msg1269)

---

<a id="msg1270"></a>

## 13. Telekatz · 26. Jan 2009, 09:32

> **Zitat**
>
> Aber warum addierst du 7C0 auf die eigentlichen RC5e-Codes drauf?

+0x800 für das Toggle Bit. Muss mann nicht machen, wird vom Encoder selbstständig gesetzt oder gelöscht. Ist bei diesem Code gemacht worden um auch die Taste "0" senden zu können. "0" währe sonst 0x0000 und damit nicht belegt.

-0x40 für das 7. Kommandobit. Ist bei RC5e das invertierte 2. Start Bit.

[Permalink](http://bettyhacks.com/forum/index.php?topic=187.msg1270#msg1270)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
