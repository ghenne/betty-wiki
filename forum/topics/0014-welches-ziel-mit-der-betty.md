---
title: "Welches Ziel mit der Betty???"
topic_id: 14
board: "Sonstiges"
board_id: 9
posts: 31
first_post: "02. Aug 2007, 10:24"
last_post: "21. Mär 2008, 17:00"
authors: ["DocKugelfisch", "Kay", "Megabug", "Robbi5", "Telekatz", "TonyMahony", "Zimi", "asgard", "chaospir8", "edison", "klitzer", "meinbier", "minipilot", "netguy", "pasquale5682", "theborg", "vSaAmTp"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=14.0"
---

# Welches Ziel mit der Betty???

[← Sonstiges](../boards/09-off-topic.md) · Thema 14 · 31 Beiträge · 02. Aug 2007, 10:24 – 21. Mär 2008, 17:00

Beteiligt: DocKugelfisch, Kay, Megabug, Robbi5, Telekatz, TonyMahony, Zimi, asgard …

---

<a id="msg55"></a>

## 1. vSaAmTp · 02. Aug 2007, 10:24

Welches ist euer Ziel?

[Meine Wiki-Page](../../pages/Benutzer_VSaAmTp.md)

Ich möcht Sie gern als Uni-Fernbedienung nutzen.
Da ich noch ne DBox (und XBox) hab, sollte Sie mit Ihr auch genutzt werden. EPG Infos auslesen und auf dem Display anzeigen. Steuern der DBox. Steuern von Irgendwelchen Geräten (Türöffner, Schalter, Screenshot via serieller Webcam, Messen von Temperatur, usw)
Scart Adapter per Serieller an Digital Receiver (Linux ist meist ja auf dem Receiver), so können Infos von dem Receiver abgerufen und hingesendet werden. Wenn GPios oder der I2C Bus genutzt werden kann, dann auch Ein-Ausgabe möglichkeiten.
TAE Adapter als Schaltzentrale (Ein-Ausgabe-Modul) und Anschluss an Router (USB-RS232)
Wenn mal der Netzwerkadapter kommen sollte, dann kann man eigentlich alles machen.

*Last Edit : 02. Aug 2007, 10:27 by vSaAmTp*

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg55#msg55)

---

<a id="msg90"></a>

## 2. Zimi · 03. Aug 2007, 09:27

Ich hätte gerne sowas:

[http://www.keyspan.com/products/tvi200c/homepage.spml](https://web.archive.org/web/2012/http://www.keyspan.com/products/tvi200c/homepage.spml)

Aber nicht für einen iPod, sondern für einen Linux-basierten Mediaplayer. Insbesondere beim Musikhören möchte ich keinen Fernseher oder Monitor laufen haben müssen. Leider sind TuneView und auch dieses Logitech-Ding proprietär, so dass man keine eigenen Anwendungen darauf implementieren kann.

Gruß,
       - Zimi

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg90#msg90)

---

<a id="msg93"></a>

## 3. Robbi5 · 03. Aug 2007, 10:37

Mein Ziel:

Die Firmware-Funktionen so lassen wie sie sind und die Betty dazu bringen, dass sie automatisch den Sofameilenstand auf meine Internetseite schubst 

Robbi5

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg93#msg93)

---

<a id="msg118"></a>

## 4. theborg · 04. Aug 2007, 14:05

> **Zitat von: Robbi5 am 03. Aug 2007, 10:37**
>
> Mein Ziel:
>
> Die Firmware-Funktionen so lassen wie sie sind und die Betty dazu bringen, dass sie automatisch den Sofameilenstand auf meine Internetseite schubst 
>
> Robbi5

jo des wehre klasse vileicht kann man bei betty.tv mal nach ner api anfragen

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg118#msg118)

---

<a id="msg119"></a>

## 5. Robbi5 · 04. Aug 2007, 15:24

> **Zitat von: theborg am 04. Aug 2007, 14:05**
>
> jo des wehre klasse vileicht kann man bei betty.tv mal nach ner api anfragen

Das werden die  nicht machen. Allein schon aus datenschutzrechtlichen gründen...

<sub>

![](https://web.archive.org/web/2012/http://i.bettytools.net/all/a/1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg119#msg119)

---

<a id="msg294"></a>

## 6. minipilot · 04. Sep 2007, 13:39

Mir würde es schon reichen, vernünftig meine dbox mit Neutrino zu bedienen und dabei das Display der Dbox auf der Betty angezeigt zu bekommen. Meine dbox ist nämlich etwas weit weg, und das Fernglas nicht immer erreichbar.

Die original Funktionen sollten v i e l l e i c h t erhalten bleiben.

Da die kommunikation vom Receiver zur Betty ja über Videotext läuft, müssten die Entwickler von [www.tuxtxt.net](https://web.archive.org/web/2012/http://www.tuxtxt.net) (der Videotext decoder für dbox und dreambox) mit ins boot genommen werden...Falls man das Teil nicht direkt an die serielle Schnittstelle der Box hängt (was für die meisten user ohne Lötkolben erfahrung praktisch wäre)

Und Sie sollte lirc-kommandos beherrschen. --> [http://www.lirc.org/](https://web.archive.org/web/2012/http://www.lirc.org/) Dann fiele der ganze anlern quatsch weg. Verstehe auch nicht, warum die Betty-Entwickler darauf nicht zurückgegriffen haben, denn die Lirc Tabellen sind über das Modem doch schnell geladen.

Fertig wäre die perfekte Fernbedienung.

Irgendwelche Hacks, um Sofis (ist das die "offizielle" Abkürzung für Sofameilen?) zu ergaunern, finde ich kriminell. Das umprogrammieren ist schon grenzwärtig. Man kann in diesem Fall nur hoffen, dass nicht allzuviele das machen, sonst geht Betty.tv ziemlich schnell den Bach runter, dann gibts keinen Hardware Nachschub mehr...

*Last Edit : 05. Sep 2007, 15:11 by minipilot*

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg294#msg294)

---

<a id="msg328"></a>

## 7. meinbier · 10. Sep 2007, 14:03

es währe optimal wenn man mehrere fernbedingungen programmieren könnte ( mehrfachbelegung der tasten).
auswahl über das display (tv, sat, audio, dvd etc) währe natürlich nett.

marcos auf der betty würden die bedienung natürlich vereinfachen (ein tastendruck => sat, tv und audio gehen aus/an)

den wünschen des epg, lcd anzeige der dbox, playlisten etc.  schlisse ich mich gern an 

gruss
meinbier

ps: ist schon geil wie die entwiklung voranrennt hätte das nicht erwartet.
nur weiter so

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg328#msg328)

---

<a id="msg330"></a>

## 8. Megabug · 11. Sep 2007, 14:03

Genau, eine "mächtige" universalfernbedienung währe der hammer. Also nur um einen Zweck zu nennen! Bei mir könnte ich die dann für Dolby Receiver, Dbox2, Xbox und TV nutzen. Meine Tevion Universalfernbedienung ist nicht so umbedingt nen renner... ^^

Für Dbox2 Sendungsinfos auf dem LCD anzeigen, etc... eine XBMC implementierung könnte man sicher auch mit Python schaffen. (Dann z.b. über den Betty Netzwerkadapter oder so)

Fernsehzeitung für vordefinierte Programme immer aktuell auf der Fernbedienung.

PC Steuerung per Funk. (inkl Winamp trackanzeige, etc)

Haussteuerung (Anschluss an andere Basteleien um halt im Haus Sachen zu schalten, etc... 433MHz Steckdosen z.b.)

Mailclient mit Audionotification.

ISDN Anruferanzeige für alle MSNs.

Anzeige der Anrufliste von FritzBoxen.

Kommunikation mit Linux Routern für Statusinfos, etc.

Puuhh das wars erstmal.

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg330#msg330)

---

<a id="msg332"></a>

## 9. chaospir8 · 12. Sep 2007, 07:19

Ich denke, zuerst sollte an der Funktionalität als Universal-FB gearbeitet werden. LIRC-Unterstützung wäre dabei von Vorteil.
Danach sollte einer der Sender (vorzugsweise der am Scart) "rangenommen" werden, damit wir beliebige Inhalte an die Betty schicken können (über Seriell oder Ethernet?). Was damit dann gemacht wird, hängt dann auch von anderen Communitys ab, z.B. von den "DBox2-Neutrino-Jüngern".

<sub>

Schöne Grüße!
chaospir8

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg332#msg332)

---

<a id="msg334"></a>

## 10. minipilot · 14. Sep 2007, 11:37

...den Audioplayer der d-Box bei ausgeschaltetem Fernseher komplett über das LCD bedienen...

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg334#msg334)

---

<a id="msg374"></a>

## 11. DocKugelfisch · 24. Sep 2007, 00:26

> **Zitat von: minipilot am 04. Sep 2007, 13:39**
>
> Mir würde es schon reichen, vernünftig meine dbox mit Neutrino zu bedienen und dabei das Display der Dbox auf der Betty angezeigt zu bekommen

> **Zitat von: minipilot am 14. Sep 2007, 11:37**
>
> ...den Audioplayer der d-Box bei ausgeschaltetem Fernseher komplett über das LCD bedienen...

Ich denke auch man sollte an einer dbox2 Loesung fuer das Display arbeiten und an der Uni-FB

<sub>

Was man lernen muß, um es zu tun, das lernt man, indem man es tut.
Zitat: Aristoteles (384-322), griechischer Philosoph

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg374#msg374)

---

<a id="msg380"></a>

## 12. pasquale5682 · 30. Sep 2007, 07:48

Da ich auch in besitz einer DBox2 bin, mit Linux natürlich, denke ich auch mal das es ganz cool wäre, sich die EPG daten auf das Betty Display anzeigen zu lassen. Aber vielleicht ist ja auch irgendwqann mal mehr mit der Betty möglich.

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg380#msg380)

---

<a id="msg472"></a>

## 13. chaospir8 · 06. Nov 2007, 10:23

Hallo liebe Mitboardies,

ich möchte meine oben stehende "Ich wünsche mir ..."-Aussage um die Kleinigkeit ergänzen, dass die Kommunikation mit der Betty (also Aufspielen alternativer Software, Informationen anzeigen ...) DAU-sicher über den IP-Adapter erfolgen soll.

<sub>

Schöne Grüße!
chaospir8

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg472#msg472)

---

<a id="msg473"></a>

## 14. theborg · 06. Nov 2007, 16:41

DAU-Sicher ? das geht nicht es gibt immer einen der trozdem kaput bekommt

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg473#msg473)

---

<a id="msg474"></a>

## 15. Kay · 06. Nov 2007, 16:44

Wir sind hier nicht bei "Wünsch dir was".

Immer die tollsten Sachen wünschen und alle 3 Wochen mal gucken ob es schon erfüllt wurde. 

Es heißt ja auch "Welches ist euer Ziel?"

Das heißt welches Ziel ihr für euch selber erarbeiten wollt und nicht welches Ziel soll für euch von anderen erarbeitet werden.

Mitmachen ist hier die Devise!

*Last Edit : 06. Nov 2007, 17:19 by Kay*

<sub>

![](https://web.archive.org/web/2012/http://bowp.netaction.de/ausrede/a1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg474#msg474)

---

<a id="msg475"></a>

## 16. klitzer · 06. Nov 2007, 18:51

@kay
kann ja nicht jeder so'n genie wie du sein. es gibt auch noch normalsterbliche ohne c++ und andere programmierkenntnisse..

g,k

<sub>

#!/bin/sh

if [ "${USER_READ}" -ne "" ] ; then
   echo -e "${GRUSS},\n${NICK}"
fi

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg475#msg475)

---

<a id="msg476"></a>

## 17. Kay · 06. Nov 2007, 19:34

Hab ich gesagt das ich ein Genie bin? Nein! Genauso wenig hab ich was von Programmierkenntnissen gesagt, man kann Projekte auch anders unterstützen z.B. durch Hardware-Spenden: Unsere Entwickler haben z.B. nicht mal einen IP-Adapter.

Also nicht immer sagen was zu tun ist sondern auch mal fragen was man tuen kann!

<sub>

![](https://web.archive.org/web/2012/http://bowp.netaction.de/ausrede/a1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg476#msg476)

---

<a id="msg477"></a>

## 18. klitzer · 07. Nov 2007, 08:59

hätte ich, wie so manch anderer hier 20 bettys wäre es kein problem. hab aber selbst nur eine betty und einen ip-adapter und die möchte ich nur ungern hergeben. nen ip-adapter habe ich mit folgender email erhalten:

> **Zitat**
>
> Von: xxxxxxxx@xxxx.de [mailto:xxxxxxx@xxx.de]
> Gesendet: Dienstag, 18. September 2007 15:39
> An: 'service@betty-tv.de'
> Betreff: AW: Betty TV - IP-Adapter
>
> Sehr geehrte Damen und Herren,
>
> vorab bedanke ich mich für die rasche Antwort. Ich besitze einen Router (AVM FRITZ!Box 7170) der über alle nötigen Voraussetzungen des Anschlusses eines solchen IP-Adapters und einer dauerhaften Onlineverbindung verfügt. Ich möchte Sie hiermit bitten, mich für den Versand eines IP-Adapters für die Betty vorzumerken.
>
> Mit freundlichen Grüßen,
> xxxxxxxx xxxxxxxxxxxx
>
>
> ________________________________________
> Von: service@betty-tv.de [mailto:service@betty-tv.de]
> Gesendet: Dienstag, 18. September 2007 10:55
> An: xxxxxxxxxx@xxxx.de
> Betreff: Betty TV - IP-Adapter
>
>
> Sehr geehrter Herr xxxxxxx,
>
> vielen Dank für Ihre E-Mail.
>
> Um den neuen IP-Adapter von Betty nutzen zu können, benötigen Sie in jedem Falle einen freier Steckplatz im DSL-Router, Kabelmodem oder WLAN-Router.
>
> Bei dem Betty IP-Adapter wird der drahtlose Telefonadapter gegen ein kleines IP-fähiges Modem ausgetauscht.
>
> Wenn diese Voraussetzung bei Ihnen erfüllt ist, sagen Sie uns bitte kurz bescheid, damit wir Sie für den Versand des IP-Adapters vormerken können.
>
> Für weitere Fragen stehen wir Ihnen gerne jederzeit zur Verfügung.
>
> Mit freundlichen Grüßen,
>
> Pia Sievers
> Betty Kundendienst
>
> PS: Nicht immer beantwortet derselbe Betty Mitarbeiter Ihre E-Mail. Damit wir Ihnen so rasch als möglich weiterhelfen können, senden Sie bitte immer auch Ihre ursprüngliche Anfrage und bereits erhaltene(n) Antwort(en) mit. Danke für Ihre Mithilfe!
> ___________________________________________________________________________
> Betty TV Servicerufnummer:
> 01805 045 045 (EUR 0,14/Min aus dem Festnetz der Deutschen Telekom AG)
>
> Betty TV Service Mail:
> service@betty-tv.de
>
> Betty TV Internet Adresse:
> [www.betty-tv.de](https://web.archive.org/web/2012/http://www.betty-tv.de)
>
> HRB:155 735, Amtsgericht München
>
> Vorstand: Matthias Zahn, Jens Gloede
> Vorsitzender des Aufsichtsrats: Ueli Dietiker
>
>
>
> Bereich: Support
> E-Mail: xxxxxx@xxxx.de
> Thema: netzwerkadapter für die betty
> Nachricht: Sehr geehrte Damen und Herren,
> ich habe meinen Festnetzanschluss bei der Telekom gekündigt und kann die Betty deshalb leider nicht mehr nutzen. Nun habe ich erfahren, dass die Möglichkeit besteht, sich mit einem entsprechenden Netzwerkadapter über das Internet zu verbinden. Ich wäre Ihnen sehr verbunden, wenn Sie mir einen Netzwerkadapter zusenden könnten, damit ich die Betty und Ihre Dienste weiterhin in Anspruch nehmen kann.
> Für Rückfragen erreichen Sie mich unter der VOIP-Rufnummer: xxxxxxxxxxx
>
> Mit freundlichen Grüßen,
> xxxxxxxx xxxxxxxxxxx
>
> -------------------------------------------
> Betty ID 1: xxxx
> Betty ID 2: xxxx
> Betty ID 3: xxxx
> Betty KDNr 1: 0000
> Betty KDNr 2: 00000000
> -------------------------------------------
> Vorname: xxxxxxxxx
> Name: xxxxxxx
> Strasse: xxxxxx
> Nr.: 8
> PLZ: xxxxxxx
> Ort: xxxxxxxx
> Telefon: xxxxxxxxx

vielleicht hilfts auch anderen..
sollte ich irgendwo vertrauliche daten nicht ausge-x haben, bitte ich um benachrichtigung/berichtigung..

g,k

<sub>

#!/bin/sh

if [ "${USER_READ}" -ne "" ] ; then
   echo -e "${GRUSS},\n${NICK}"
fi

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg477#msg477)

---

<a id="msg479"></a>

## 19. TonyMahony · 07. Nov 2007, 23:54

Welches Ziel ich mit der Betty verfolge?

Ich finde die Betty einfach sehr interessant - die Kombination aus Scart-Adapter, Fernbedienung, Modem und IP-Adapter ist schon recht spektakulär.
Und was ihr hier bisher geleistet habt, finde ich schon ganz erstaunlich!

Ich erhoffe mir auf jeden Fall, dieses Projekt wachsen zu sehen und hoffentlich in irgendeiner Form unterstützen zu können - sei es durch Testen, neue Ideen, Dokumentation oder Spenden.

Mit technischem Fachwissen kann ich leider nicht glänzen, bin aber durchaus lernfähig, hab nen Lötkolben und kann ihn halbwegs bedienen, probiere gerne neuen Kram aus und ich bin - wenn motiviert - durchaus hartnäckig am Thema.

Logisches Denken ist mir nicht fremd; C, C++ und Java (sowie COBOL ) hab ich vor 5-6 Jahren mal gelernt - müsste ich wohl mal auffrischen, um da hilfreich zu sein.
Ich hab ne DBox mit Linux und einfach Spaß an der damit verbundenen Frickelei - auch wenn ich sonst keine Geduld habe, bei sowas halte ich durch...

Um mal völlig zu phantasieren, was ich mir so vorstellen könnte - ohne eine Ahnung zu haben, ob das realisierbar ist:
-das Modem so umbauen, dass es über eine serielle Schnittstelle angeschlossen werden kann (PC, D-Box, wasauchimmer) und mit der Betty funken kann
-den IP-Adapter so umbauen, dass er über das Netzwerk von diversen Rechnern angesprochen werden kann, um über Funk mit der Betty zu kommunizieren
-den Scart-Adapter so umbauen, dass er Infos von der DBox verarbeiten kann und diese an die Betty schickt
-Funk-Steckdosen bauen, die mit der Betty bedient werden können
-die Betty via Funk und modifiziertem Modem oder IP-Adapter an einem PC als Chat-Client nutzen
...uns fällt da bestimmt noch was ein, oder?

Einfach mal schauen, was halt so geht und dabei möglichst viel lernen und eine nette Entwicklergemeinde kennenlernen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg479#msg479)

---

<a id="msg489"></a>

## 20. Kay · 09. Nov 2007, 20:48

Wow resekt das ist wirklich mal ein super Post mit konkreten Vorstellung und vorallem du foderst nicht nur sondern bietest auch an mitzumachen. Top!

<sub>

![](https://web.archive.org/web/2012/http://bowp.netaction.de/ausrede/a1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg489#msg489)

---

<a id="msg492"></a>

## 21. klitzer · 10. Nov 2007, 03:02

> **Zitat von: Kay am 09. Nov 2007, 20:48**
>
> Wow resekt das ist wirklich mal ein super Post mit konkreten Vorstellung und vorallem du foderst nicht nur sondern bietest auch an mitzumachen. Top!   

berichtige mich, wenn ich mich irre, aber du hast bisher auch noch nicht wirklich viel geboten, außer seitenhiebe an user zu verteilen, die einfach nur neugierig sind und fragen stellen und/oder wünsche äußern. das kanns doch neicht sein, oder? hab von dem untergrundbieber mehr erwartet..

was den respekt an user wie TonyMahony angeht, dem schließe ich mich an. solche projekte können nicht ohne leistungsträger (die namen brauch ich ja wohl net erwähnen) die zeit und schweiß investieren leben. doch gibt es auch jene, deren fähigkeiten eingeschränkt sind bzw sich auf anderen gebieten entfalten und trotzdem an den erfolgen teilhaben möchten. ich denke nicht, dass die zugpferde das alles nur für den eigengebrauch auf die beine stellen und die früchte ihrer arbeit nicht teilen wollen. also ich würde mich freuen, wenn möglichst viele die produkte meines schaffens in ihrem wohnzimmer nutzen.

*Last Edit : 10. Nov 2007, 03:12 by klitzer*

<sub>

#!/bin/sh

if [ "${USER_READ}" -ne "" ] ; then
   echo -e "${GRUSS},\n${NICK}"
fi

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg492#msg492)

---

<a id="msg493"></a>

## 22. netguy · 10. Nov 2007, 03:47

> **Zitat von: klitzer am 10. Nov 2007, 03:02**
>
> > **Zitat von: Kay am 09. Nov 2007, 20:48**
> >
> > Wow resekt das ist wirklich mal ein super Post mit konkreten Vorstellung und vorallem du foderst nicht nur sondern bietest auch an mitzumachen. Top!   
>
>
> berichtige mich, wenn ich mich irre, aber du hast bisher auch noch nicht wirklich viel geboten, außer seitenhiebe an user zu verteilen, die einfach nur neugierig sind und fragen stellen und/oder wünsche äußern. das kanns doch neicht sein, oder? hab von dem untergrundbieber mehr erwartet..

das ist ansichtssache. der ton macht die musik. wenn man reinrumpelt, nur sagt was man gerne will und die ausdrucksweise dann auch noch zu wuenschen uebriglaesst, dann darf man sich nicht wundern wenn entsprechend harsche reaktionen  zurueckkommen. oder wie in deinem fall:

> **Zitat**
>
> hey leute,
> das ist doch nicht euer ernst.. der kerl ist doch nicht echt.. is das nen pr-gag, damit sich nach 2,5 wochen ruhe wieder leben im board tummelt?

wie soll man auf solche unterstellungen reagieren? glaubst du wirklich wir haben nichts besseres zu tun als uns solchen unsinn auszudenken, hier zu posten unter anderem nick um dann darauf loszugehen? erst denken, dann posten! und das gilt fuer viele hier.

> **Zitat**
>
> was den respekt an user wie TonyMahony angeht, dem schließe ich mich an. solche projekte können nicht ohne leistungsträger (die namen brauch ich ja wohl net erwähnen) die zeit und schweiß investieren leben. doch gibt es auch jene, deren fähigkeiten eingeschränkt sind bzw sich auf anderen gebieten entfalten und trotzdem an den erfolgen teilhaben möchten. ich denke nicht, dass die zugpferde das alles nur für den eigengebrauch auf die beine stellen und die früchte ihrer arbeit nicht teilen wollen. also ich würde mich freuen, wenn möglichst viele die produkte meines schaffens in ihrem wohnzimmer nutzen.

dem respekt schliesse ich mich natuerlich auch an. allerdings verstehe ich deinen kommentar nicht wirklich.
> **Zitat**
>
> doch gibt es auch jene, deren fähigkeiten eingeschränkt sind bzw sich auf anderen gebieten...
> ...
> also ich würde mich freuen, wenn möglichst viele die produkte meines schaffens in ihrem wohnzimmer nutzen.

dann mach doch mal "butter bei die fische" und verrate uns, was du beitragen koenntest. zu tun gibt es viel, aber leider sind die meisten leute dann doch nur am endergebnis interresiert und nicht an der mitarbeit. was es zu tun gibt? nun, den wiki auf vordermann bringen, code testen und evtl. kleine howto's dazu machen, datenblaetter organisieren (manchmal nicht einfach), hardware fuer die entwickler besorgen (ip-adapter z.b.), wietrgehende info's zu den verwendeten bauteilen suchen (z.b. bestehenden code aufspueren, tools um die chips zu programmieren finden, etc).... es gibt wirklich genug zu tun, nur machen tut es keiner, und immer wieder hoert man nur "was kann es denn jetzt schon?" und "ich haette gerne das es x kann!"

schon mal auf die idee gekommen eine wiki-seite anzulegen mit wohldurchdachten ideen zur verwendbarkeit des systems? nein? tja, warum nur?

gruss,
chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg493#msg493)

---

<a id="msg495"></a>

## 23. Kay · 10. Nov 2007, 10:31

Full Ack, netguy 

> **Zitat von: klitzer am 10. Nov 2007, 03:02**
>
> > **Zitat von: Kay am 09. Nov 2007, 20:48**
> >
> > Wow resekt das ist wirklich mal ein super Post mit konkreten Vorstellung und vorallem du foderst nicht nur sondern bietest auch an mitzumachen. Top!   
>
>
> berichtige mich, wenn ich mich irre, aber du hast bisher auch noch nicht wirklich viel geboten, außer seitenhiebe an user zu verteilen, die einfach nur neugierig sind und fragen stellen und/oder wünsche äußern. das kanns doch neicht sein, oder? hab von dem untergrundbieber mehr erwartet..

Tja dann warst du wohl weder im Chat noch Wiki bis jetzt...

Uns was ist dein Auftrag hier?

*Last Edit : 10. Nov 2007, 10:47 by Kay*

<sub>

![](https://web.archive.org/web/2012/http://bowp.netaction.de/ausrede/a1.gif)

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg495#msg495)

---

<a id="msg496"></a>

## 24. klitzer · 10. Nov 2007, 13:49

> **Zitat von: Kay am 10. Nov 2007, 10:31**
>
> Uns was ist dein Auftrag hier?

ich bin die board-nervensäge - so einen habt ihr noch nicht, oder?

ihr solltet ein wenig geduldiger sein mit den neulingen. wer jetzt noch dumme fragen stellt, kann später, wenn er sich ein wenig mit dem thema befasst hat, seinen beitrag leisten. wenn hier jeder für seinen ersten post einen auf die mütze kriegt, schreibt er kein zweites mal.. die comunity muss erst wachsen, später wird sich schon herauskristallisieren, wer "nützlich" ist und euch unterstützt..

<sub>

#!/bin/sh

if [ "${USER_READ}" -ne "" ] ; then
   echo -e "${GRUSS},\n${NICK}"
fi

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg496#msg496)

---

<a id="msg498"></a>

## 25. netguy · 10. Nov 2007, 16:55

> **Zitat von: klitzer am 10. Nov 2007, 13:49**
>
> > **Zitat von: Kay am 10. Nov 2007, 10:31**
> >
> > Uns was ist dein Auftrag hier?
>
>
> ich bin die board-nervensäge - so einen habt ihr noch nicht, oder?

hab ichs mir doch gedacht. nur dumm schwaetzen aber nix dahinter. warum gehst du denn nicht auf meine punkte ein?

echt, auf so typen wie dich koennen wir hier gut verzichten. depp....

halte dich doch bittte an dieter nuhr: wenn man keine ahnung hat, einfach mal die fresse halten!

chris

*Last Edit : 10. Nov 2007, 18:09 by netguy*

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg498#msg498)

---

<a id="msg499"></a>

## 26. klitzer · 10. Nov 2007, 23:19

warum beleidigst du mich? du kennst mich doch gar nicht. soll ich mich jetzt auch auf das niveau (ist keine hautcreme) harablassen und dir sachen wie schwanzlutscher an den kopf schmeissen? mach ich aber nicht. deine punkte waren hauptsächlich vorwürfe - worauf soll ich mich da einlassen. wenn ihr unterstützung sucht, solltet ihr über die boardatmosphäre nachdenken und nicht jeden teeren und federn, der sich euch anschliessen will.

um auf deine "punkte" einzugehen:
> **Zitat**
>
> wie soll man auf solche unterstellungen reagieren? glaubst du wirklich wir haben nichts besseres zu tun als uns solchen unsinn auszudenken, hier zu posten unter anderem nick um dann darauf loszugehen? erst denken, dann posten! und das gilt fuer viele hier.

das war vielmehr ne frage als ne unterstellung und nicht ganz ernst gemeint. und wenn der echt ist, warum habt ihr ihn dann verarscht anstatt ihn aufzuklären?
vielmehr ging es mir um den zweiten abschnitt meines ersten posts:
> **Zitat**
>
> wie auch immer - will ja kein spielverderber sein, würde aber viel lieber wissen, ob und was sich rund um die betty getan hat... schau hier fast jeden tag lesend vorbei, weil ichs vor neugier kaum aushalten kann. wann in etwa ist denn das ganze einigermaßen end-user-tauglich und relativ dau-sicher?

ne ganz normale frage. ich, der gerade mal weiß wierum ich den lötkolben halten muss, wollte wissen, ob ichs riskieren kann, jetzt schon einzusteigen, ohne was kaputt zu machen. als antwort kam:
> **Zitat**
>
> jeden tag mitprogrammierend waere hilfreicher.
>
> wann es dau (klitzer) tauglich ist? keine ahnung, bezahl meine miete, strom, etc. und ich kann mich full time dransetzen.
>
> ansonsten einfach mal ausprobieren. wenn das aber auch schon zuviel verlangt ist, dann haste pech gehabt.

also auch gleich wieder vorwürfe und ne beleidigung. das hätte man doch anders schreiben können ... finde ich.
> **Zitat**
>
> allerdings verstehe ich deinen kommentar nicht wirklich.

das ist schade, aber nicht überraschend. wollte damit sagen, dass auch einsteiger dazulernen und irgendwann ne bereicherung seien können. das wird aber nix, wenn jeder weggeekelt wird.
> **Zitat**
>
> dann mach doch mal "butter bei die fische" und verrate uns, was du beitragen koenntest.

erwähnte ich schon im anderen thread. ich kann scripten - nur bringt das zurzeit nix. ich kann HOWTO's schreiben und anderen einsteigern support leisten - nur muss ich dazu selbst erstmal nen einstieg finden. das gleiche gilt für
> **Zitat**
>
> was es zu tun gibt? nun, den wiki auf vordermann bringen, code testen und evtl. kleine howto's dazu machen,

> **Zitat**
>
> hardware fuer die entwickler besorgen (ip-adapter z.b.)

würde ich gern machen, nur bezweifel ich, dass ich weitere ip-adapter/bettys zugeschickt bekäme. allerdings habe ich (weiter oben) den emailverkehr mit service@betty-tv.de gepostet, als "wegweiser" um den ip-adapter kostenlos zu erhalten. bei mir hats geklappt, versuchs doch einfach mal
> **Zitat**
>
> wietrgehende info's zu den verwendeten bauteilen suchen (z.b. bestehenden code aufspueren, tools um die chips zu programmieren finden, etc)....

dafür reicht mein fachwissen nicht aus, aber es gibt sicherlich etliche andere, die sich mit der mateirie auskennen. fragt doch einfach mal nach. mir, als aussenstehender kommt es vor, als säßen da ein paar eigenbrödler die im stillen kämmerlein ihr eigenes süppchen kochen. versucht doch etwas mehr die user (oder zumindest die, die es werden wollen) einzubeziehen. es gibt bestimmt sehr viele, die gern helfen würden, aber nicht wissen wie oder dass überhaupt hilfe erwünscht ist.
> **Zitat**
>
> und immer wieder hoert man nur "was kann es denn jetzt schon?" und "ich haette gerne das es x kann!"

ist doch in ordnung. auch wenn es vielleicht etwas ungeschickt verpackt ist, schadet es nicht die zukünftigen user zu informieren oder sich mal durchzulesen, welche "changerequest" eingehen. vielleicht sind ja paar gute ideen oder zumindest denkanstösse dabei. ich kann nicht verstehen, warum teilweise so agressiv auf neuankömmlinge reagiert wird. vielleicht klärt mich ja jemand auf.

so, auch wenn ich für diesen beitrag wahrscheinlich wieder prügel einstecke, hoffe ich meinen standpunkt verständlich dargelegt zu haben. wenn nicht, ists schade, aber für mich nicht weiter schlimm.

<sub>

#!/bin/sh

if [ "${USER_READ}" -ne "" ] ; then
   echo -e "${GRUSS},\n${NICK}"
fi

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg499#msg499)

---

<a id="msg505"></a>

## 27. asgard · 11. Nov 2007, 09:38

Hi zusammen,

pls....back to topic!

Einen Flame/bash/streit-thread ist hier völlig unnötig!

Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg505#msg505)

---

<a id="msg547"></a>

## 28. chaospir8 · 16. Nov 2007, 08:53

Hallo!
Gute Idee mit dem "Back to Topic". Danke!

Dann hier noch eine Anregung meinerseits: Betty soll (über den IP-Adapter) mit der FritzBox kommunizieren und das können, was mit der [FritzMini](https://web.archive.org/web/2012/http://www.fritzmini.de/start.html) auch machbar sein wird. Nur so eine verrückte Idee von mir.

<sub>

Schöne Grüße!
chaospir8

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg547#msg547)

---

<a id="msg815"></a>

## 29. edison · 16. Mär 2008, 23:09

Auch ich kann leider nicht bei der Softwareentwicklung der Betty helfen, hab aber Spaß an solchen Basteleien.
Bei mir steht ebenfalls eine Dbox2 mit Neutrino.

Toll wäre, wenn ich den Scartadapter via 232 an eine SPS koppeln könnte und so die Tastendrücke der Betty abfragen, sowie Texte auf das Display Schreiben könnte.
Somit wär die Betty für Hausautomatisierungszwecke nutzbar 

Nu Ja, erstmal sollte mein Schnittstellenadapter funktionieren

Aber wenn ich helfen kann...

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg815#msg815)

---

<a id="msg822"></a>

## 30. Telekatz · 20. Mär 2008, 00:06

Hallo edison,

eine Übertragung der Tastendrücke an den Scartadapter ist jetzt möglich. Ich habe dafür einen neuen IR encoder hinzugefügt, der anstelle eines IR Signals ein Funkübertragung sendet. Dies ist mit dem Scartadapter im binary mode empfangbar.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg822#msg822)

---

<a id="msg825"></a>

## 31. edison · 21. Mär 2008, 17:00

THX
Das ist ja klasse, habs mitlerweile mit meinem Interface hinbekommen.
Funzt prima :-)
Mache mal einen neuen Thread auf, ist hier doch ot.

[Permalink](http://bettyhacks.com/forum/index.php?topic=14.msg825#msg825)

---

[← Zurück zu Sonstiges](../boards/09-off-topic.md) · [Gesamtindex](../index.md)
