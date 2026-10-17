---
title: "Scart - Terminalmode"
topic_id: 226
board: "Software"
board_id: 6
posts: 11
first_post: "12. Dez 2009, 20:55"
last_post: "13. Dez 2009, 20:44"
authors: ["Telekatz", "asgard"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=226.0"
---

# Scart - Terminalmode

[← Software](../boards/06-software.md) · Thema 226 · 11 Beiträge · 12. Dez 2009, 20:55 – 13. Dez 2009, 20:44

Beteiligt: Telekatz, asgard

---

<a id="msg1527"></a>

## 1. asgard · 12. Dez 2009, 20:55

hi,
hab jetzt mal den scartadapter auf die aktuelle version geflasht und seriell (über usb) an den rechner gehängt...nun versuchte ich die befehle aus der readme zu verwenden:

`Serial settings: 38400,n,8,1, no handshake

Commands:

Terminal Mode:
==============

t<data>                                 transmitt <data>
s                                       show cc1100 status bytes
c                                       show cc1100 configuration registers
b                                       switch to binary mode
w                                       send WOR packet`

Leider bekomme ich ausser einem Echo der Eingabe nichts zurück (wenn ich z.B. s oder c verwende)...
woran kann das denn liegen...

Viele Grüße
Asgard

*Last Edit : 12. Dez 2009, 21:07 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1527#msg1527)

---

<a id="msg1528"></a>

## 2. Telekatz · 13. Dez 2009, 10:41

Hi Asgard,

sendet dein Terminalprogramm vielleicht kein CR beim Zeilenende? Ansonsten kommt das Echo überhaupt vom Scart Adapter oder generiert das Terminalprogramm das Echo selber?

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1528#msg1528)

---

<a id="msg1530"></a>

## 3. asgard · 13. Dez 2009, 11:01

Hi Telekatz,
danke für deine Antwort!

Ich verwende Kitty (Putty + ein paar Verbesserungen/Erweiterungen) als Terminalprogramm...
wenn ich die Verbindung zum Scart trenne, bekomme ich keine Echos mehr...
Sofern gehe ich davon aus, dass die wirklich vom scart kommen.

Was ich aber zwischenzeitlich bemerkt habe...
Ich verwende zum flashen des Scartadapters die Betty...und in der aktuellen Boop ist noch das alte Scart-Image (#9 im SVN) drin...

Jetzt muss ich erstmal schauen, wie ich das aktualisiere

Viele Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1530#msg1530)

---

<a id="msg1532"></a>

## 4. asgard · 13. Dez 2009, 12:01

So,
anbei ein aktuelles Boop-Build mit der momentan aktuellen Scart Version (SVN #14) sowie passendem Sourcefile.
Vielleicht kann das jemand kurz ins SVN schieben..

Viele Grüße
Asgard

EDIT:
irgendwie kann ich immernoch nicht per rs232 und meinem Rechner mit dem Scartadapter kommunizieren.
Jedes mal wenn ich etwas sende, leuchtet kurz die grüne Scart-LED.
Aber auf "c" und/oder "s" bekomm ich halt nichts zurück

Der Port-Redirector scheint auch zu funktionieren.
Wenn ich die Verbindung zwischen Scart und Betty aufgebaut habe und dann per RS232 und Terminalprogramm
Daten an den Scart schicke, dann zählt auf der Betty der "Counter" hoch...

Jetzt würde ich halt gerne mal den Traffic sniffen...
nur ohne funktionierende RS232-Kommunikation ist das recht doof..
hat noch irgendwer ne idee?

*Last Edit : 13. Dez 2009, 12:38 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1532#msg1532)

---

<a id="msg1533"></a>

## 5. Telekatz · 13. Dez 2009, 12:48

Hast du schon überprüft, ob dein Terminalprogramm ein CR am Zeilenende sendet?

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1533#msg1533)

---

<a id="msg1534"></a>

## 6. asgard · 13. Dez 2009, 12:59

jein....ich hab jetzt ein anderes Terminaltool genommen...dort hab ich den CR (Cr+LF) eingeschaltet...
welches Terminaltool nimmst du denn Telekatz?

Ist das denn normal, dass man ein Echo bekommt?
Denn wenn ich RX/TX vertausche, funktioniert der Port-Redirector noch, aber die LED blinkt nicht mehr auf, wenn ich was vom Rechner absende...

EDIT:
Hab jetzt definitiv ein Terminal, das ein CR am ende sendet...[http://www.compuphase.com/software_termite.htm](https://web.archive.org/web/2012/http://www.compuphase.com/software_termite.htm)
(den CR kann man in den Settings einschalten)...
Nun sendet er z.B. ein S und ich bekomm als Echo auch wieder ein S ...aber eben nicht mehr

Ich hab 38400 8N1 None...neuste Scart-Version und neuste Boop...alles verbunden per USB-RS232-Adapter..

Was soll denn passieren, wenn ich auf der Betty im Port-Redirector auf Test drücke?

Und brauch ich eigentlich einen Level-Shifter für den TX-RX-Scart-Anschluss?
Momentan hab ich keinen dran...ist das evtl. der fehler?

*Last Edit : 13. Dez 2009, 13:22 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1534#msg1534)

---

<a id="msg1535"></a>

## 7. Telekatz · 13. Dez 2009, 13:28

Ich nehme HyperTerminal.  Das Echo ist gewollt und die LED blinkt immer auf wenn vom PC zum Scartadapter etwas gesendet wird.

> **Zitat**
>
> Nun sendet er z.B. ein S und ich bekomm als Echo auch wieder ein S ...aber eben nicht mehr

Ein S oder ein s? Und nur ein s oder ein s + Eingabetaste? Allerdings sollte er auch auf ein S (mit Eingabetaste) mit Syntax error antworten.

> **Zitat**
>
> Was soll denn passieren, wenn ich auf der Betty im Port-Redirector auf Test drücke?

Am PC erscheit im Terminal "abc".

> **Zitat**
>
> Und brauch ich eigentlich einen Level-Shifter für den TX-RX-Scart-Anschluss?
> Momentan hab ich keinen dran...ist das evtl. der fehler?

Ja, den braucht man. Eingang ist aber 5V tolerant, muss nicht umbedingt 3,3V Pegel haben.

*Last Edit : 13. Dez 2009, 13:49 by Telekatz*

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1535#msg1535)

---

<a id="msg1536"></a>

## 8. asgard · 13. Dez 2009, 13:48

> **Zitat von: Telekatz am 13. Dez 2009, 13:28**
>
> Ein S oder ein s? Und nur ein s oder ein s + Eingabetaste? Allerdings sollte er auch auf ein S (mit Eingabetaste) mit Syntax error antworten.

hab sowohl S als auch s probiert.
ein Syntax error bekomme ich nie zu sehen.

hab gerade mal text per seriell vom scart zur betty übertragen...das funktioniert per portredirector
Testbutton macht nichts...kein abc

Ist in der SCart-Firmware evtl grad ein Fehler drin?

*Last Edit : 13. Dez 2009, 13:51 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1536#msg1536)

---

<a id="msg1537"></a>

## 9. Telekatz · 13. Dez 2009, 13:58

> **Zitat**
>
> Ist in der SCart-Firmware evtl grad ein Fehler drin?

REV14 funktioniert bei mir so wie es soll.

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1537#msg1537)

---

<a id="msg1538"></a>

## 10. asgard · 13. Dez 2009, 18:48

> **Zitat von: Telekatz am 13. Dez 2009, 13:58**
>
> > **Zitat**
> >
> > Ist in der SCart-Firmware evtl grad ein Fehler drin?
>
>
> REV14 funktioniert bei mir so wie es soll.

kann es sein, dass im SVN eine kompilierte Version mit

main.c
 `terminal = 1;
 redirector = 1;
 len =0;

 while (1) {
  if(redirector) {`

oder

main.c
 `//terminal = 1;
 redirector = 1;
 len =0;

 while (1) {
  if(redirector) {
   if(inbuflen >= 58) {
   if(inbuflen >= 58) {`

liegt?
Würde das nicht erklären, dass ich nur ein Echo bekomme und ich sonst nichts machen kann?

@telekatz:
Da ich es irgendwie nicht kompiliert bekomme wäre es super, wenn du mir dein bin-file kurz hochladen könntest.

Meine Ausgabe:
`Z:\XXX\betty_scart\trunk>make
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 -c main.c
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 -c serial.c
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 -c cc1100.c
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 -c cmd.c
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 -c rf.c
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 -c timer.c

Linking main.rel serial.rel cc1100.rel cmd.rel rf.rel timer.rel
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 main.rel serial.rel cc1100.rel cmd.rel rf.rel timer.rel -o bett
y_scart.ihx
Multiple definition of _crlf
Multiple definition of _crlf
Multiple definition of _crlf
make: *** [betty_scart.ihx] Error 1`

Wenn ich danach nochmal make mache:

`Z:\XXX\betty_scart\trunk>make
C:/SDCC/bin/packihx betty_scart.ihx > betty_scart.hex
packihx: read 440 lines, wrote 239: OK.
cat betty_scart.hex | C:/SDCC/bin/makebin -s 8096 > betty_scart.bin`

Viele Grüße und vielen Dank!
Asgard

*Last Edit : 13. Dez 2009, 19:14 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1538#msg1538)

---

<a id="msg1539"></a>

## 11. Telekatz · 13. Dez 2009, 20:44

Habe sowohl die im SVN als auch die anhängende bin getestet. Beide funktionieren.

> **Zitat**
>
> Würde das nicht erklären, dass ich nur ein Echo bekomme und ich sonst nichts machen kann?

Nein, denn im Redirector Mode wird kein Echo augegeben.

`Linking main.rel serial.rel cc1100.rel cmd.rel rf.rel timer.rel
C:/SDCC/bin/sdcc --iram-size 0x100 --model-small --code-size 8096 -IC:/SDCC/incl
ude --std-sdcc99 main.rel serial.rel cc1100.rel cmd.rel rf.rel timer.rel -o bett
y_scart.ihx
Multiple definition of _crlf
Multiple definition of _crlf
Multiple definition of _crlf
make: *** [betty_scart.ihx] Error 1`
Probier mal alle im Sourcecode vorkommende crlf in irgendetwas anderes umzubenennen (Variable wird in serial.h definiert).

[Permalink](http://bettyhacks.com/forum/index.php?topic=226.msg1539#msg1539)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
