---
title: "Frage zum Simple Serial Interface"
topic_id: 104
board: "Hardware"
board_id: 5
posts: 30
first_post: "16. Februar 2008, 15:01"
last_post: "26. Apr 2008, 02:46"
authors: ["Gentoo07", "Telekatz", "bustler", "famos", "heugabel", "peter_silie", "thuxnder"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=104.0"
---

# Frage zum Simple Serial Interface

[← Hardware](../boards/05-hardware.md) · Thema 104 · 30 Beiträge · 16. Februar 2008, 15:01 – 26. Apr 2008, 02:46

Beteiligt: Gentoo07, Telekatz, bustler, famos, heugabel, peter_silie, thuxnder

---

<a id="msg775"></a>

## 1. peter_silie · 16. Februar 2008, 15:01

Hallo zusammen,

ich wollte Morgen das Simple Serial Interface zusammenlöten. Jetzt habe ich eine Frage zum Anschluß an die Betty. Wie habt ihr das mit dem Kabel gelöst ? Welche Stecher habt Ihr genommen. Ich bin am Überlegen alte Anschlußstecker von einem Gehäuse zu benutzen (für Reset, Sound, usw....).

Gruß
Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg775#msg775)

---

<a id="msg776"></a>

## 2. Gentoo07 · 17. Februar 2008, 19:43

Moin, ich habe für den Zweck einfach ein Stück von dem Reichelt-Artikel "BL 2X10G 2,54" abgeschnitten, auf ein Stückchen Lochraster gelötet, hier drauf noch 2 Jumper für Bootloader und Reset und eine 3polige Stiftleiste gelötet, worauf ich wiederum mein zerschnittenes Siemens C35-Datenkabel gesteckt hab. Funktioniert mit Betty-heaven hervorzüglich.

Aber mehrere der genannten PC-Gehäuse-Steckverbinder würden natürlich genauso gehen, ggf. mit sekundenkleber zusammengefügt. ![Zwinkernd](https://web.archive.org/web/2012/http://bettyhacks.com/forum/Smileys/default/wink.gif)

Viel Erfolg!

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg776#msg776)

---

<a id="msg798"></a>

## 3. bustler · 10. März 2008, 22:14

Hi,

bin hier neu, und hab auch schon ein paar Fragen, da meine Betty noch ungeflasht ist.
Mein Pegelwandler ist auch gebaut, nur Bettyheaven will nicht starten. Angeblich fehlen da ein paar DLLs, die in .NET dabei dein sollen.
Kann mir jemand sagen welche, und woher nehmen?

Ausserdem würd mich interessieren, wie Gentoo07 das mit dem C35 Datenkabel gemacht hat.
Ich hab eines vom S45 (ME45), das ich auch schonmal verwenden wollte, aber das wurde nix.

Danke!

Gruß
Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg798#msg798)

---

<a id="msg810"></a>

## 4. famos · 14. März 2008, 18:57

Hallo Peter,

Bettyheaven benötigt das File mfc80.dll danach habe ich auch rumgesucht und Zeugs installiert was nichts brachte. Gefunden habe ich es dann auf einem andern Computer. Damit es du einfacher hast, habe ich dir das File auf Rapidshare gelegt: [http://rapidshare.com/files/99525178/mfc80.dll](https://web.archive.org/web/2012/http://rapidshare.com/files/99525178/mfc80.dll) .
Als Interface Zur Betty habe ich Keyspan USB zu RS232 Adapter genommen und drei Drähte an den TI Chip gelötet, also den Pegelwandler überbrückt. Das geht sicher auch mit andern Fabrikaten. Das ist die billigste Lösung. Bei Pollin bekomt man ähnlich Adapter für 10 Euro.

Gruss famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg810#msg810)

---

<a id="msg814"></a>

## 5. Gentoo07 · 16. März 2008, 23:09

@ Bustler:

Mein verwendetes Datenkabel hat eine 3-adrige Leitung zum Handy. Welche Ader jeweils Masse, RX oder TX ist, habe ich aus dem Pinout des Siemens-Handysteckers entnommen. Die beiden Jumper für Bootloader und Reset sind nach Masse geschaltet, die anderen 3 Adern direkt zur Fernbedienung verbunden.

Um mit Betty-Heaven zu Flashen, muss man nun den Stecker an die Betty stecken, Jumper für Bootloader stecken, und den für Reset einmal kurz auf- dann wieder abstecken um die Betty in den Bootmodus zu bringen. Jetzt kann man mit Bettyheaven connecten...

Nach dem Flash Bootjumper ab, und wieder einmal kurz resetten, dann sollte boop starten.

Viel Erfolg!

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg814#msg814)

---

<a id="msg823"></a>

## 6. bustler · 21. März 2008, 08:31

Hallo famos,

Danke für den Tip, und das File; auch an Gentoo07 - werd dann nochmal mein Glück mit dem Datenkabel versuchen wenn Bettyheaven geht!
Ich habs mir heruntergeladen und in den BettyHeaven Ordner als auch auf Windows und System32 kopiert - nutzt leider nix :-(
Was könnte da noch fehlen?
Hab auch keine Ahnung, was ich damals alles auf dem Rechner drauf hatte, als es einmal lief.

Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg823#msg823)

---

<a id="msg824"></a>

## 7. famos · 21. März 2008, 12:58

Hoi Peter,

aus eigener Erfahrung kann ich bestätigen, dass nicht jedes Interface mit BettyHaven funktioniert, obwolt eigentlich alles richtig ist. Auch Pegelprobleme mit 5 / 3.3 Volt sind möglich. Ich würde empfehlen als erstes das Interface mit einem Terminalprogramm zu prüfen (RX und TX zusammenhalten). Als zweites ist eine Test mit einer Betty, die noch micht umgeflasht ist, hilfreich. Meine Betty sendet nach dem einlegen der Batterien jede Menge Information auf die serielle Schnittstelle. Wenn da was kommt ist schon mal eine Richtung in Ordnung.

Alternativ zu BettyHaven gibt es noch die NXP Flash Utility: [http://www.nxp.com/files/products/standard/microcontrollers/utilities/lpc2000_flash_utility.zip](https://web.archive.org/web/2012/http://www.nxp.com/files/products/standard/microcontrollers/utilities/lpc2000_flash_utility.zip)
 und das LPCTools_cygwin, das auch unter Windows läuft: [http://katanafans.idf-mod.de/cmde/betty_pub/lpctool-cygwin.zip](https://web.archive.org/web/2012/http://katanafans.idf-mod.de/cmde/betty_pub/lpctool-cygwin.zip)
Ich habe noch einen weiteren Schnittstellenwandler gefunden der sich einigermassen gut öffnen lässt und einen FTDI232BM, welcher auch geeignet ist, enthält. [http://www.amazon.de/Assmann-USB-2-0-Adapter-USB-seriell/dp/B000NPLDH6/ref=pd_sbs_pc_title_3](https://web.archive.org/web/2012/http://www.amazon.de/Assmann-USB-2-0-Adapter-USB-seriell/dp/B000NPLDH6/ref=pd_sbs_pc_title_3) . Wo welcher Draht anzulöten ist kann ich bei Bedarf mitteilen.

Viel Erfolg famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg824#msg824)

---

<a id="msg883"></a>

## 8. peter_silie · 29. März 2008, 14:14

So, nun habe ich alle Bauteile zusammen. Die Sachen habe ich bei Reichelt bestellt.
Nun habe ich die Polar Kondensatoren und mir ist nicht klar wie ich die an V+ und V- am IC anschließen soll (Polung V+ an Kondensator + Pol und V- an Kondensator - Pol).
Kann mir da jemand weiterhelfen, der auch schon die Bauteile vom Reichelt eingesetzt hat ?

Gruß
Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg883#msg883)

---

<a id="msg884"></a>

## 9. Gentoo07 · 29. März 2008, 14:36

@ Perter_Silie:

Der Minuspol ist an solchen Elektrolytkondensatoren mit einem großen durchgezogenen Strich am Gehäuse markiert, meist in heller Farbe.

Meintest du das, oder liegt dein Problem woanders?

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg884#msg884)

---

<a id="msg898"></a>

## 10. peter_silie · 29. März 2008, 23:00

Hi Gentoo07,

also wo das auf dem Kondensator ist kann ich auf dem Kondensator erkennen. Es geht um den Schaltplan.
V+ scheint ja für einen Pluspol gedacht zu sein. Kommt hier der Kondensator mit Plus oder Minus dran.
Und umgekehrt, kommt an V- des ICs an den Minus Pol vom Kondensator ?

Gruß
Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg898#msg898)

---

<a id="msg900"></a>

## 11. Gentoo07 · 30. März 2008, 03:58

@Peter_silie:

Da musst du tatsächlich einen Elko mit - an V-, und einen mit + an V+ anschließen. An diesen beiden Pins liegen im Betrieb Spannungen von ca. +-13V gegen GND an, V+ ist also positiver als VCC und V- negativer als GND da der MAX232/3232 eine integrierte Ladungspumpe hat um die 5V VCC auf RS232-Pegel +-12-15V umzusetzen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg900#msg900)

---

<a id="msg903"></a>

## 12. peter_silie · 30. März 2008, 15:46

Hi Gentoo07,

danke für die schnelle Antwort. Dann solltem dem Zusammenlöten nichts mehr im Weg stehen.

Gruß
Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg903#msg903)

---

<a id="msg962"></a>

## 13. peter_silie · 10. April 2008, 22:48

So der Adapter ist zusammengelötet aber irgendwie funktioniert nichts.
Wenn ich den Adapter an der Betty anschließe, passiert nichts. Sobald ich den Stecker mit dem PC verbinde, geht das Display aus.
Nach dem Abziehen der Stecker muß ich die Batterien entfernen damit die Betty durchstartet. Danach befinde ich mich in einem 'Emergency Menu'.

Auch Betty Heaven sagt immer "RX: Timeout"

Was kann das sein ? Sollte der Adapter denn nicht richtig sein ? Soll ich vielleicht mal ein Bild von dem Adapter hochladen ?

Gruß
Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg962#msg962)

---

<a id="msg963"></a>

## 14. thuxnder · 11. April 2008, 02:16

dass das display ausgeht ist normal, da die betty durch die schaltung resettet wird.

ein emergency menu kenn ich nicht, kann dazu nix sagen.

rx timeout, mhh. hast du ein osziloskop zur hand?
bei mir gibt es öfters probleme mit der masse wenn die serielle verbindung nicht will.

zum testen der schaltung kannst du mal tx und rx verbinden (am besten an der steckerseite zur betty hin, ohne angeschloßene betty) und was über die serielle schicken, unter windows gibts so nen tool, hyper terminal glaub ich, damit dann einfach mal was auf die serielle schicken, beachte local echo aus machen. wenn du nun was auf die serielle schickst solltest du das selbige sehen, wenn ja, dann glappt die schaltung soweit.

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg963#msg963)

---

<a id="msg964"></a>

## 15. peter_silie · 12. April 2008, 11:12

Hallo,

ein Osziloskop habe ich nicht. Leider. Vielleicht ist es auch nur eine Einstellung am COM Port von meinem PC. Welche Baudrate, usw. muß denn eingestellt sein ?

Das Hyper Termial habe ich gefunden. Kann ich jetzt einfach RX und TX brücken ohne das was passiert ? Was kann ich denn in dem Fenster eingeben um was zu empfanden ?

Gruß und Dank
Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=104.msg964#msg964)

---

<a id="msg965"></a>

## 16. thuxnder · 12. Apr 2008, 15:15

ja rx und tx kann ohne probleme ge brückt werden, und alles was du dann eingibst bekommst logischer weise ja dann auch wieder, weil ja rx und tx gebrückt ist.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg965#msg965)

---

<a id="msg966"></a>

## 17. peter_silie · 12. Apr 2008, 20:37

Hi  thuxnder,

was für eine Baudrate hast du für die Betty (nicht für den Hyperterminal Test) eingestellt (und vieleicht die Flußsteuerung)?

Gruß
Peter

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg966#msg966)

---

<a id="msg974"></a>

## 18. Gentoo07 · 15. Apr 2008, 20:39

Bei mir ist die Schnittstelle auf 9600 Baud und keine Flußsteuerung eingestellt. (Und funktioniert mit Bettyheaven)

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg974#msg974)

---

<a id="msg988"></a>

## 19. heugabel · 21. Apr 2008, 14:52

hallo,

ich habe ledier auch die Polaren elko´s von reichelt nur weis ich leider net wie rum die eingebaut werden müssen.

Schaltplan und Rasterlayout sind ja 2 völlig verschiedene pläne...

kann bitte wer schnell helfen, hab den drang betty zu bibby zu machen

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg988#msg988)

---

<a id="msg989"></a>

## 20. Gentoo07 · 21. Apr 2008, 16:24

@heugabel:
Guck mal auf [http://www.elektronik-magazin.de/page/der-pegelumsetzer-max232-15](https://web.archive.org/web/2012/http://www.elektronik-magazin.de/page/der-pegelumsetzer-max232-15)
da sind Pin-Numerierung und Polaritäten eingetragen. Die Elkos sind am Gehäuse auf der Seite des Minuspols mit einem weissen Streifen markiert.

Viel Erfolg!

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg989#msg989)

---

<a id="msg990"></a>

## 21. heugabel · 22. Apr 2008, 09:59

danke, dat half mir super

insoweit alles richtig nach gefühl aber geht nicht....

bei terminal proggs kommen alle befehle wieder zurück ohne das ich brücke....weis wer rat?

kann es evtl am elko liegen? weil zw. schaltplan und layout sind c1 und c5 vertauscht

*Last Edit : 22. Apr 2008, 10:15 by heugabel*

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg990#msg990)

---

<a id="msg991"></a>

## 22. Gentoo07 · 22. Apr 2008, 10:47

> **Zitat von: heugabel am 22. Apr 2008, 09:59**
>
> insoweit alles richtig nach gefühl aber geht nicht....
>
> bei terminal proggs kommen alle befehle wieder zurück ohne das ich brücke....weis wer rat?
>
> kann es evtl am elko liegen? weil zw. schaltplan und layout sind c1 und c5 vertauscht

Dass alles zurückkommt ist u.U. normal, die zuständige Einstellung heisst meistens "Lokales Echo aktivieren". Wenn das Aktiv ist, wird alles abgesendete auch pauschal wieder im Fenster ausgegeben. Wenn dann vom gebrückten Interface eine Antwort käme, würde sie zweimal auf dem Schirm stehen. Zum testen steck dein Interface doch mal ganz vom Rechner ab und guck ob immer noch was zurückgesendet wird. Wenn ja ist es eine Einstellungssache.

Aber der Schaltplan und das Layout sind in der Tat sehr unpassend, das könnte auch Probleme verursachen. Wenn du hast ersetz doch auch den 5. Kondensator durch 1µF, dann bist du auf der sicheren Seite und auch in den Beispielschaltungen von Maxim werden 5 gleiche Kondensatoren verwendet.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg991#msg991)

---

<a id="msg992"></a>

## 23. Telekatz · 22. Apr 2008, 11:02

> **Zitat**
>
> Aber der Schaltplan und das Layout sind in der Tat sehr unpassend, das könnte auch Probleme verursachen. Wenn du hast ersetz doch auch den 5. Kondensator durch 1µF, dann bist du auf der sicheren Seite und auch in den Beispielschaltungen von Maxim werden 5 gleiche Kondensatoren verwendet.

Alternativ kann man auch alle Kondensatoren durch 100nF Keramik ersetzen und hat dann auch kein Problem mit der Polatität mehr. Laut Datenblatt ist beim MAX3232 bei 3,3V Versorgungsspannung eine Mindestkapazität von nur 0,1µF gefordert.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg992#msg992)

---

<a id="msg993"></a>

## 24. heugabel · 22. Apr 2008, 12:56

also wenns abgesteckt ist kommt nix zurück...

wo finde ich denn die lokales echo funktion in vista?

bettyheaven sagt immer rx timeout :-(

edit: teste grad mit ner hyperterminal software, aslo leere verbindung ohne betty am ende kann ich tippen passiert nix...

brücke ich rx - tx dann hängt sich das programm auf

*Last Edit : 22. Apr 2008, 13:28 by heugabel*

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg993#msg993)

---

<a id="msg994"></a>

## 25. Gentoo07 · 23. Apr 2008, 14:32

Die Einstellung für das Lokale Echo findest du immer im jeweiligen Terminalprogramm, wo genau kann ich daher nicht sagen.
Aber da nichts durchkommt mit abgezogenem Stecker, funkt dir das schonmal nicht dazwischen.

Da musst du wohl die Schaltung, und vor allem die Steckerbelegungen noch 3x kontrollieren.
Bedenke auch, dass z.B. die SubD-Verbinder für die Serielle Schnittstelle an Buchse und Stecker eine unterschiedliche Numerierung aufweisen (so dass bei beiden zusammengesteckt Pin1 in Buchse1 steckt u.s.w.). Sonst könnte z.B. das IC falschherum eingesteckt oder irgendwo ein Kurzschluss vorhanden sein.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg994#msg994)

---

<a id="msg996"></a>

## 26. heugabel · 23. Apr 2008, 20:38

ich werds mal checken, im falle des nicht erfolgs werde ich mit kleinen zusatzteilchen ein nxpisp bauen da fahlen ja nur sehr wenige bauteile.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg996#msg996)

---

<a id="msg998"></a>

## 27. Gentoo07 · 23. Apr 2008, 23:56

Ich will nicht unhöflich erscheinen, aber ein Umbau macht keinen Sinn wenn die Basis schon kaputt ist.

Deine vorhandene Schaltung hat irgendwo einen dicken Fehler wenn sie ohne Betty schon alles eingegebene wieder ausgibt und der wird sich nicht auflösen indem Du einen anderen Schaltungsteil umbaust.

Der Unterschied liegt nur in der Invertierung des RTS-Signals bei der Simple-Schaltung, und hat mit Rx und Tx in dem Sinne nichts zu tun.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg998#msg998)

---

<a id="msg999"></a>

## 28. heugabel · 25. Apr 2008, 10:17

es waren wieder mal fehler in der schaltung

hab die pin belegung beim dsub nicht beachtet...

nun geht die betty nicht aus wenn ich sie anstecke....

aber auch gebrückt kommt nix mehr zurück :-(

die 3,3V kann ich auch nit mehr messen....

ich check weiter^^

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg999#msg999)

---

<a id="msg1000"></a>

## 29. Telekatz · 25. Apr 2008, 10:46

Wenn die Betty nicht angeschlossen ist kann auch nichts funktionieren. Die 3,3V kommen von der Betty und ohne die arbeitet der MAX3232 nicht.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg1000#msg1000)

---

<a id="msg1001"></a>

## 30. heugabel · 26. Apr 2008, 02:46

also ich check mich hier kaputt

wenn ich am ic pin 13 und 14 brücke kommt was zurück, wenn ich pin 11 und 12 brücke passiert nix mehr, auch nich wenn miss betty dran is.

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=53fb32962856752245e22e3b7adadfb9&topic=104.msg1001#msg1001)

---

## Verwandte Themen

- [[Bilder] Simple Serial Interface V2](0108-bilder-simple-serial-interface-v2.md)
- [Frage zum Betty Serial Log](0045-frage-zum-betty-serial-log.md)
- [Was ist besser? Handykabel oder Simple Seriell Interface?](0165-was-ist-besser-handykabel-oder-simple-seriell-interface.md)
- [Simple Seriell Interface zu Verkaufen](0171-simple-seriell-interface-zu-verkaufen.md)
- [Simple Seriell Interface zu Verkaufen (zum 2. mal)](0175-simple-seriell-interface-zu-verkaufen-zum-2-mal.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
