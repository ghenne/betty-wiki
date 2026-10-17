---
title: "boop - communicate with betty - by netguy"
topic_id: 41
board: "Software"
board_id: 6
posts: 17
first_post: "30. Aug 2007, 03:24"
last_post: "24. Jul 2008, 20:10"
authors: ["Robbi5", "Spessi", "Telekatz", "alterego", "kackhart", "netguy", "theborg"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=41.0"
---

# boop - communicate with betty - by netguy

[← Software](../boards/06-software.md) · Thema 41 · 17 Beiträge · 30. Aug 2007, 03:24 – 24. Jul 2008, 20:10

Beteiligt: Robbi5, Spessi, Telekatz, alterego, kackhart, netguy, theborg

---

<a id="msg260"></a>

## 1. alterego · 30. Aug 2007, 03:24

Hallo leute,

netguy hat vorhin ein schönes stück arbeit geleistet: boop.

eine software die vorerst im ram der betty läuft und 2 strings ausgibt und eingaben von der tastatur als ECHO zurückgibt.

nähere infos findet ihr hier:
[http://bettyhacks.com/wiki/index.php/Boop_-_communicate_with_betty](../../pages/Boop%20-%20communicate%20with%20betty.md)

kritik an meinem ersten wiki-eintrag is erwünscht (wenn begründet :>)

lieben gruss,
alterego

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg260#msg260)

---

<a id="msg261"></a>

## 2. netguy · 30. Aug 2007, 03:35

hallo alle zusammen,

danke auch an alterego fuer die doku und das makefile!

hatte gerade gesehen, das noch ein fehelr im boop-0.1.tgz war, sollte jetzt alles ok sein (falsches boot.s)

gute nacht,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg261#msg261)

---

<a id="msg264"></a>

## 3. Spessi · 31. Aug 2007, 18:18

Gute Arbeit! Geht ja vorwärts!! Wie wärs wenn du ein SVN/CVS-Server einrichtest?

Viel Spaß beim weiterhin programmieren & hacken Hoffentlich können wir bald komplett eigene Software programmieren, die alles unterstützen wird.

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg264#msg264)

---

<a id="msg265"></a>

## 4. theborg · 31. Aug 2007, 20:13

Sacht mal habt ihr die aktuelle SW auf eurer betty ? den da bekomme ich weder die sw drauf noch das flash ausgelesen

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg265#msg265)

---

<a id="msg266"></a>

## 5. netguy · 31. Aug 2007, 20:23

hallo allerseits,

unter [http://mamalala.org/boop-0.3.tgz](https://web.archive.org/web/2012/http://mamalala.org/boop-0.3.tgz) gibt es die aktuellste version der "fummelware"

nach dem upload mit dem aktuellsten lpcload wird mit 115200 baus kommuniziert.

wie bisher gibt die betty nach eingabe von ! den string "Hello Betty!" aus, mit * kommt "And another Hello"

mit 1 werden die ersten 8 32-bit worte des flash#0 ausgelesen

man kann das flash sektorenweise loeschen, in dem man E0a fuer den ersten sektor in flash0 bis E0s fuer den letzten sektor eingibt. das gleiche fuer E1a bis E1s, dann aber im zweiten flash

mit XF0 kann man erste flash komplett loeschen, mit XF1 das zweite

mit W werden die ersten 8 16-bit werte aus dem ram ab 0x40000200 in das flash0 ab 0x80000000 geschrieben, also die ersten 16 byte der boop.bin

gruesse,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg266#msg266)

---

<a id="msg267"></a>

## 6. netguy · 31. Aug 2007, 20:24

hallo theborg,

> **Zitat von: theborg am 31. Aug 2007, 20:13**
>
> Sacht mal habt ihr die aktuelle SW auf eurer betty ? den da bekomme ich weder die sw drauf noch das flash ausgelesen

du kommst nicht in den internen bootloader?

gruss,

chris

p.s.: ich habe mittlerweile garkeine soft mehr auf den betties ... endlich sind sie sauber ;-D

*Last Edit : 31. Aug 2007, 20:27 by netguy*

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg267#msg267)

---

<a id="msg268"></a>

## 7. theborg · 31. Aug 2007, 21:40

Doch in den bootloader komme ich aber ich bekomme kein OK mehr und die Synchronisierung geht auch nicht mehr.

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg268#msg268)

---

<a id="msg269"></a>

## 8. netguy · 31. Aug 2007, 21:45

hallo,

> **Zitat von: theborg am 31. Aug 2007, 21:40**
>
> Doch in den bootloader komme ich aber ich bekomme kein OK mehr und die Synchronisierung geht auch nicht mehr.

hmm, aber wie merkst du dann das du im bootloader bist? das "Synchronized" kommt also noch?

magst nicht in den chat kommen? ist glaube ich einfacher

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg269#msg269)

---

<a id="msg270"></a>

## 9. theborg · 31. Aug 2007, 23:08

würde ich machen hab nur kein java

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg270#msg270)

---

<a id="msg271"></a>

## 10. netguy · 31. Aug 2007, 23:45

> **Zitat von: theborg am 31. Aug 2007, 23:08**
>
> würde ich machen hab nur kein java

nimm einen irc lient deiner wahl, server ist irc.insiderz.de, port 6667, kanal #bettyhacks

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg271#msg271)

---

<a id="msg278"></a>

## 11. netguy · 01. Sep 2007, 15:59

hallo allerseits,

hatte einen fehler im flash loeschen, 1) top anstelle bottom boot adressen benutzt, dann einen shift vrgessen (wegen dem versatz der adressleitungen)

habe [http://mamalala.org/boop-0.3.tgz](https://web.archive.org/web/2012/http://mamalala.org/boop-0.3.tgz) gerade neu hochgeladen, loescht jetzt alles richtig

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg278#msg278)

---

<a id="msg371"></a>

## 12. netguy · 20. Sep 2007, 19:45

hallo allerseits,

unter [http://mamalala.org/boop-0.9.tgz](https://web.archive.org/web/2012/http://mamalala.org/boop-0.9.tgz) gibt es die aktuelle version.
sie macht nichts ausser ein nettes logo anzeigen und wenn man I eingibt, einen timer interrupt zu starten.
der gibt  dann ca. alle 3 sekunden einen fortlaufenden zaehler ueber die serielle aus.

achtung: das klappt nur wenn boop_rom.bin in das flash geschrieben wird ...

der befehl dazu (mit aktuellem lpctool von [http://mamalala.org/lpctool-0.8.tgz)](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.8.tgz)) lauetet:

lpctool -v -i -e -a boop_rom.bin

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg371#msg371)

---

<a id="msg372"></a>

## 13. kackhart · 20. Sep 2007, 23:01

> **Zitat von: netguy am 20. Sep 2007, 19:45**
>
> achtung: das klappt nur wenn boop_rom.bin in das flash geschrieben wird ...

damit dass auch im ram geht, muessen die vektoren noch an den ram anfang kopiert werden (memap natuerlich auch nicht vergessen!). dazu mach ich grob sowas im startup.s:

 `copy_exception_vectors:

        mov r0, #sram_addr
        ldr r1, =exception_vectors
        ldmia r1!, {r2-r9}
        stmia r0!, {r2-r9}
        ldmia r1!, {r2-r8}
        stmia r0!, {r2-r8}`

wobei sram_addr eben 0x40000000 und exception_vectors halt der anfang der vektoren ist. wenn du den ldr auf de pc vom VICVectAddr relativ (-0xff0) machst genuegen wahrscheinlich am schluss auch 6 bytes.

cheers,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg372#msg372)

---

<a id="msg373"></a>

## 14. netguy · 21. Sep 2007, 00:53

hallo nochmals,

so, habe jetzt mal den sound ans laufen gebracht und boop 0.9 aktualisiert. zu finden unter [http://mamalala.org/boop-0.9.tgz](https://web.archive.org/web/2012/http://mamalala.org/boop-0.9.tgz)

aufgrund der groesse ist es jetzt nicht mehr moeglich, boop aus dem ram zu benutzen, es _muss_ also in das flash geschrieben werden.

die soundausgabe laeuft mit 7500000 / 256 / 4 = 7324.21875 hz, also  nicht ganz 7.5 khz.
wenn man sounds konvertieren moechte ist es wichtig zuerst auf mono zusammenzumischen, dann tiefpassfiltern mit der halben samplefrequenz (also hier fo = 3750 hz), anschliessen resamplen auf 7.5 khz und zu gut der letzt noch in 8-bit umwandeln.

ein kleines script zum umwandeln mittels sox kommt spaeter noch ...

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg373#msg373)

---

<a id="msg1072"></a>

## 15. Robbi5 · 20. Jul 2008, 10:03

Hallo Netguy,
ich habe endlich meine Betty mit boop flashen können und gleich mal den Sound ausprobiert.

Du hattest in der Nachricht davor
> **Zitat von: netguy am 21. Sep 2007, 00:53**
>
> ein kleines script zum umwandeln mittels sox kommt spaeter noch ...

geschrieben.

Ich würde gerne mal die eingebauten Sounds durch eigene ersetzen, verstehe aber das Dateiformat nicht.
Könntest du bitte das Script veröffentlichen? 

Danke,
Robbi5

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg1072#msg1072)

---

<a id="msg1073"></a>

## 16. Telekatz · 23. Jul 2008, 21:30

Hallo Robbi5

das umwandeln des Soundile mit sox funktioniert mit folgendem Befehl:

sox.exe input.wav -c 1 -r 7500 -1 -u output.raw  lowpass 3750

Die erzeugte Datei mit WinBin umwandeln (gibt es hier [http://www.ulrichradig.de/home/index.php/projekte/winbin](https://web.archive.org/web/2012/http://www.ulrichradig.de/home/index.php/projekte/winbin)) und in die sounds.h kopieren.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg1073#msg1073)

---

<a id="msg1074"></a>

## 17. Robbi5 · 24. Jul 2008, 20:10

Hi,

danke, damit habe ich jetzt endlich wieder die original Betty-Sounds in Boop. 
(Leider klingen die aber verzerrt, nicht so wie bei der Originalfirmware - aber immer noch besser als gar kein Sound )

Dann noch eine Frage zu WinBin:
Ich arbeite hauptsächlich unter Linux (Ubuntu). Gibt es WinBin auch für Linux? Das wäre besser, als ständig wegen den Sounds das Dual-Boot-XP wieder hochzuholen.

Nochmals ein großes Danke,
Robbi5

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=41.msg1074#msg1074)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
