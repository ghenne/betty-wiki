---
title: "boop, infrarot, etc ..."
topic_id: 65
board: "Software"
board_id: 6
posts: 19
first_post: "07. Okt 2007, 00:24"
last_post: "25. Nov 2007, 17:01"
authors: ["Colibri", "KiLLERHOLiC", "Megabug", "alterego", "asgard", "eme", "netguy", "starshiner"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=65.0"
---

# boop, infrarot, etc ...

[← Software](../boards/06-software.md) · Thema 65 · 19 Beiträge · 07. Okt 2007, 00:24 – 25. Nov 2007, 17:01

Beteiligt: Colibri, KiLLERHOLiC, Megabug, alterego, asgard, eme, netguy, starshiner

---

<a id="msg431"></a>

## 1. netguy · 07. Okt 2007, 00:24

hallo alle zusammen,

so, ich bin gerade dabei den infrarot-teil einzubauen. zunaechst wird es rc5 geben, andere systeme nach bedarf. im moment erzeugt die betty lediglich einen 37khz carrier auf der ir diode, es kann sein das dadurch die spannung zusammenbricht (die ir diode zieht halt zuviel saft im 50/50 dauerbetrieb).

ebenso sind die tasten nun integriert. alles laeuft in eigenen interrupts, also der sound, tasten & infrarot. diese sind so angelegt das sie aus dem internen sram des lpc laufen (der code ist dort platziert), da die ausfuehrung aus dem flash nur begrenzt moeglich waere (der flash speicher ist einfach zu langsam)

all das findet sich im svn, in dem repository fuer boop ist auch das .bin und das .hex dabei, jedoch laeuft das nur noch aus dem flash im moment.

nochmals wegen dem ir: die aktuelle version wird mit hooher wahrscheinlichkeit die betty im 1 sekunden takt resetten und nach 3-4 mal ganz schweigen, da die ir diode dauerhaft mit dem reinen carrier gepulst wird.
wer also di augenblickliche version testen will muss entweder die ir-diode kurzfristig abloeten an einem pin, oder den SET/CLR code in infrared.c -> irIRQ auskommentieren.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg431#msg431)

---

<a id="msg432"></a>

## 2. asgard · 07. Okt 2007, 16:24

Super!!

Langsam wirds ja

Allerdings konnte ich die Version nicht testen, da ich sie nicht auf die Betty bekommen habe (diese version muss ja in den Flash geschrieben werden...)
Irgendwie wollte das Betty-heaven nicht so machen....oder ich war einfach zu dumm.

Vielleicht kann sich Colibri mal dazu äussern ob das nur ein Fehler meinerseits war oder ob betty-heaven das (noch) nicht kann/richtig macht. Danke schon mal im vorraus

Grüße und ein schönes WE
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg432#msg432)

---

<a id="msg433"></a>

## 3. Colibri · 07. Okt 2007, 17:35

Ab der Version 1.04 von Betty-Heaven kann man auch kleinere Dateien ins Betty-Flash schreiben (Rest wird mit FFh aufgefüllt). Damit klappts jetzt z.B. auch mit boop_rom.bin (übrigens geiles Bild/Sound) im Flash.

Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg433#msg433)

---

<a id="msg434"></a>

## 4. asgard · 07. Okt 2007, 18:12

super! Danke für das schnelle Update!

Grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg434#msg434)

---

<a id="msg435"></a>

## 5. netguy · 07. Okt 2007, 18:44

hallo colibri,

> **Zitat von: Colibri am 07. Okt 2007, 17:35**
>
> Ab der Version 1.04 von Betty-Heaven kann man auch kleinere Dateien ins Betty-Flash schreiben (Rest wird mit FFh aufgefüllt). Damit klappts jetzt z.B. auch mit boop_rom.bin (übrigens geiles Bild/Sound) im Flash.
>
> Colibri

ah, das ist super!

ja, leider ist mir gestern mein scope gestorben, ausgerechnet als ich am infrarot implementieren bin .... ;(
jetzt heisst es erstmal im blindflug zu coden ....

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg435#msg435)

---

<a id="msg437"></a>

## 6. starshiner · 08. Okt 2007, 21:42

> **Zitat von: netguy am 07. Okt 2007, 00:24**
>
> ebenso sind die tasten nun integriert. alles laeuft in eigenen interrupts, also der sound, tasten & infrarot. diese sind so angelegt das sie aus dem internen sram des lpc laufen (der code ist dort platziert), da die ausfuehrung aus dem flash nur begrenzt moeglich waere (der flash speicher ist einfach zu langsam)

Frage dazu: nutzt du schon den PWM Ausgang  zur 37kHz Erzeugung?

Gruß
s.

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg437#msg437)

---

<a id="msg438"></a>

## 7. netguy · 08. Okt 2007, 22:33

hallo starshiner,

> **Zitat von: starshiner am 08. Okt 2007, 21:42**
>
> > **Zitat von: netguy am 07. Okt 2007, 00:24**
> >
> > ebenso sind die tasten nun integriert. alles laeuft in eigenen interrupts, also der sound, tasten & infrarot. diese sind so angelegt das sie aus dem internen sram des lpc laufen (der code ist dort platziert), da die ausfuehrung aus dem flash nur begrenzt moeglich waere (der flash speicher ist einfach zu langsam)
>
>
>
> Frage dazu: nutzt du schon den PWM Ausgang  zur 37kHz Erzeugung?
>
> Gruß
> s.

zur zeit ich beuntze timer1 zur carrier erzeugung, nicht den pwm. insgesamt laeuft die ganze ir uebetragung im interrupt.
es werden auch alle protokolle, die ich finden kann, als eigenstaendige encoder implementiert, wobei der irq dann den ausgewaehlten (ueber einen funktionspointer) encoder nach ablauf der mark/space time aufruft.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg438#msg438)

---

<a id="msg440"></a>

## 8. netguy · 09. Okt 2007, 08:59

hallo colibri,

> **Zitat von: Colibri am 07. Okt 2007, 17:35**
>
> Dateien ins Betty-Flash schreiben (Rest wird mit FFh aufgefüllt).

sag mal, ist das mit dem auffuellen woertlich gemeint? denn nach dem loeschen des flash/sektors ist naemlich alles bereits 0xFF ...

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg440#msg440)

---

<a id="msg441"></a>

## 9. netguy · 09. Okt 2007, 09:02

so,

ein neuer ir encoder funktioniert, naemlich fuer das rcmm protokoll das z.b. vom galaxis receiver genutzt wird.

standardmaessig ist der auch aktiv.

wenn man aber beim start von boop die A taste haelt, wird auf nrc17 fuer die nokia dbox2 umgeschaltet.
(ist ja alles nur zum testen)

gruesse,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg441#msg441)

---

<a id="msg444"></a>

## 10. netguy · 10. Okt 2007, 03:44

hallo allerseits,

so, bis jetzt sind in boop folgende ir protokolle integriert, mit ein paar codetabellen zum testen:

protokoll - vorhandene code tabelle

SIRC (Sony) - sony rm pp411 av2, tv
RCMM - galaxis sat receiver
NRC17 - dbox2
RC5 - tv

standardmaessig ist tv RC5 aktiv. man kann zum testen beim reset/start der betty die tasten a-d gedrueckt halten. A: dbox2 NCR17, B: galaxis RCMM, C: pp411 SIRC, D: tv SIRC

ich werde in den naechsten tagen weitere protokolle hinzufuegen.

wenn ihr mir beim testen helfen wollt, schreibt doch einfach hier rein was fuer geraete ihr habt/steuern wollt, mit einem link auf ein passendes lirc config file. evtl. ist das gewuenschte geraet bereits in lirc erfasst ( [http://lirc.sourceforge.net/remotes/](https://web.archive.org/web/2012/http://lirc.sourceforge.net/remotes/) ), wenn nicht bitte eines anlegen. dazu lirc installieren und ihm die fernbedienung beibringen. ( [http://www.lirc.org/](https://web.archive.org/web/2012/http://www.lirc.org/) und fuer windows [http://winlirc.sourceforge.net/de/](https://web.archive.org/web/2012/http://winlirc.sourceforge.net/de/) )

das alles ist im moment nur zu testzwecken, ich werde mich naechste woche daransetzen und eine universal-fb funktionalitaet in boop integrieren, die auch nutzbar ist, allerdings noch ohne anlernfunktion. mein ziel ist vorrangig mit implementierungen der einzelnen protokolle + kleine codetabllen zu arbeiten, und das anlernen als "notnagel" zu reservieren, wenn es halt eine unbekannte fb ist. aber auch dann ist das ziel dazu das entsprechende protokoll direkt zu implementieren.

auch sind sachen wie z.b. ir-makros geplant: man drueckt den power knopf und alles geht an/aus, oder feste abfolgen zum video-recorder programmieren, etc...

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg444#msg444)

---

<a id="msg445"></a>

## 11. KiLLERHOLiC · 10. Okt 2007, 08:37

Sorry für meine dumme Frage, aber funktionieren mit boop die Tasten auf der FB schon?
Oder wird die FB nur als IR Sender über den PC gesteuert?

Ich lese schon seit langem mit, und die fortschirtte bis jetzt sind schon super. Ich hab hier eine Betty die noch nicht aktiviert ist. Kann ich das boop Programm direkt in den Flash schreiben, oder muss ich die FB aktivieren? Komm nämlich aus Österreich und kann die Betty nicht aktivieren.

mfg
KiLLERHOLiC

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg445#msg445)

---

<a id="msg446"></a>

## 12. asgard · 10. Okt 2007, 09:09

Hi,

du kannst boop einfach so in den Flash schreiben,...da muss nichts aktiviert werden (afaik)!

Grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg446#msg446)

---

<a id="msg447"></a>

## 13. alterego · 11. Okt 2007, 08:14

korrekt, es muss nichts aktiviert werden. aber trotz allem kann es nicht schaden ein backup zu machen bevor man software != der originalen aufspielt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg447#msg447)

---

<a id="msg580"></a>

## 14. eme · 22. Nov 2007, 17:14

Es gibt auch noch das NEC Protokoll...

Kann man die zu sendenden Daten per Betty-Tastatur eingeben, oder ist das hard-coded?

MfG

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg580#msg580)

---

<a id="msg581"></a>

## 15. alterego · 23. Nov 2007, 18:31

nein kann man nicht, is alles im source bzw in header-files.

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg581#msg581)

---

<a id="msg583"></a>

## 16. KiLLERHOLiC · 24. Nov 2007, 08:58

So nachdem ich nach tagelanger Fehlersuche mein Simple Serial Interface fertig gebaut habe konnte ich endlich boop auf die Betty spielen.
Es ist tatsächlich egal ob die Betty aktiviert ist oder nicht, das flashen klappt einwandfrei.

Da ich die FB für den VDR benutze wäre ein Profil bei dem alle Tasten funktioniern super. Zurzeit läuft es mit dem RCMM Protokoll für Galaxy Geräte. Allerdings sind einige Tasten ohne funktion.
Wäre es möglich ein Profil zu erstellen bei dem alle Tasten ein Signal nach RCMM Standard senden?
Der Code der gesendet wird ist ziemlich egal, da die FB mit Lirc und für den VDR angelernt werden muss.
Ausserdem wäre es super wenn man die anordnung der Tasten ändern könnte.
Ich würde zB. die Position für die Farbtasten und ABCD gerne tauschen. Für den VDR braucht man die Farbtasten oft, die ABCD Tasten brauch ich dafür sogut wie nie.
Soweit ich es gesehen habe sind die Tasten gleich groß, ich müsste nur die Betreffenden Tasten ausschneiden und an meine gewünschte Position wieder einbauen.
Allerdings müsste dazu auch die belegung in Software geändert werden, damit die Betty weis wo die Tasten sind.

Vielen Dank für alle die so fleissig an der Betty arbeiten, vieleicht könnte man noch die änderungen einbauen die ich vorgeschlagen habe.

KiLLERHOLiC

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg583#msg583)

---

<a id="msg584"></a>

## 17. KiLLERHOLiC · 24. Nov 2007, 11:47

So, ich hab mir jetzt mal die Sourcen angesehen.
Genügt es eigentlich wenn ich in der keyboard.h die Einträge ändere.
z.B. KEY_A gegen KEY_Red und umgekehrt?
Bin noch in der Firma und kann es nicht austesten. Werd es sonnst am Abend mal probieren.

mfg
KiLLERHOLiC

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg584#msg584)

---

<a id="msg586"></a>

## 18. KiLLERHOLiC · 24. Nov 2007, 19:09

Hab es heute nachmittag probiert, und es funktioniert tatsächlich.
Wenn man in der keyboard.h die Einträge vertauscht und die Knöpfe ändert hat man die perfekte VDR Betty.
Wäre nur noch das Thema mit den ungenutzten Tasten....

mfg
KiLLERHOLiC

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg586#msg586)

---

<a id="msg590"></a>

## 19. Megabug · 25. Nov 2007, 17:01

Tasten bzw. codes selber definieren kannst du in den jeweiligen dateien... \ir-codes\rcmm\galaxis

Einfach was ausdenken.

[Permalink](http://bettyhacks.com/forum/index.php?topic=65.msg590#msg590)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
