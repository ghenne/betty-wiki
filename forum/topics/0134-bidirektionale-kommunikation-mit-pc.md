---
title: "Bidirektionale Kommunikation mit PC"
topic_id: 134
board: "Sonstiges"
board_id: 7
posts: 7
first_post: "07. Apr 2008, 10:14"
last_post: "28. Feb 2009, 21:08"
authors: ["Telekatz", "bn", "eme", "markusk", "thuxnder"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=134.0"
---

# Bidirektionale Kommunikation mit PC

[← Sonstiges](../boards/07-sonstiges.md) · Thema 134 · 7 Beiträge · 07. Apr 2008, 10:14 – 28. Feb 2009, 21:08

Beteiligt: Telekatz, bn, eme, markusk, thuxnder

---

<a id="msg951"></a>

## 1. markusk · 07. Apr 2008, 10:14

Hallo,

ich suche für eine Heizungssteuerung mittels FHZ ein Bedienteil. Die angebotene Zentrale und Bedienteil (FZH 1000) bietet nicht die Funktionen die ich benötige. Zum alternativen PC-Interface gibt es Projekte die ein Perl-Interface zur Verfügung stellen. Jedoch fehlt mir ein Bedienteil. Mittels LCDproc könnte man so etwas realisieren, jedoch muß dies mittels Kabel am PC hängen. Die Betty wäre optimal für diesen Zweck. Ich könnte die akutelle Temperatur und das Heiz-Programm auf dem Display anzeigen lassen und ggf. auch Regeln. Zusätzlich könnte ich eine Programmierung Remote vornehmen (z.B. wenn ich aus dem Haus gehe).

Betty müßte die darzustellenden Zeichen gesendet bekommen und Tastendrücke senden (praktisch als "dummes" Terminal ). Senden ist ja jetzt Ansatzweise möglich, aber Empfangen über Scart? Wie weit könnte das Betty-Projekt sich dem Nähern. Leider bin ich kein C-Programmierer, kenne mich jedoch mit Perl, Shell etc. recht gut aus.

Existieren denn andere halbwegs bezahlbare Lösungen (<200 Euro)? Ich möchte wenn möglich auf einen Pocket-PC als Fernbedienung verzichten?

Gruß
Markus

[Permalink](http://bettyhacks.com/forum/index.php?topic=134.msg951#msg951)

---

<a id="msg953"></a>

## 2. eme · 07. Apr 2008, 11:09

Und was ist jetzt die Frage?
Du wirst hier vermutlich keinen finden, der Deine Probleme löst oder Dir C beibringt. Das "Betty-Projekt" sind ein bis zwei Leute, die aber nicht mehr besonders aktiv an der Entwicklung arbeiten. Selbst ist der Mann.

[Permalink](http://bettyhacks.com/forum/index.php?topic=134.msg953#msg953)

---

<a id="msg954"></a>

## 3. markusk · 07. Apr 2008, 11:42

Meine Frage war, ob es evtl. käuflich erwerbbare und auch bezahlbare Fernbedienungen mit gibt, die eine bidirektionale Kommunikation mit Linux erlauben. Ich habe zumindest nichts gefunden. Evtl. gibt es ja jemand mit alternativen Ideen.

Als zweites würde mich interessieren, ob es überhaupt noch Ambitionen bezügl. Betty/Boop gibt, die ich für mein Vorhaben nutzen könnte. Dies wäre in meinem Fall, dass ich die Betty als Terminal missbrauchen könnte.

Niemand hat was von C beibringen gesagt.

Gruß
Markus

[Permalink](http://bettyhacks.com/forum/index.php?topic=134.msg954#msg954)

---

<a id="msg955"></a>

## 4. thuxnder · 07. Apr 2008, 12:55

Die Betty Hardware sollte das im grunde hergeben, sowohl Scart, als auch Die Fernbediehung selbst haben den cc1100 drine, der den funk macht und damit ist die bidirektionalität gegeben.

Software seitig ist, wie du ja schon gelesen hast, das senden möglich, d.h. es müsste noch auf den scart adapter portiert werden und ggf ein bisl protokoll drüber gestülpt werden um vernüftige bidirekte Komm. hinzubekommen.

Mit mässig viel aufwand bei der software sollte das also möglich sein.
Der Source ist eigentlich recht übersichtlich geschrieben, also mit vorhanden programmierkenntnissen  sollte es machbar sein die fehlenden funktioen zu bauen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=134.msg955#msg955)

---

<a id="msg956"></a>

## 5. Telekatz · 07. Apr 2008, 18:20

Softwareseitig ist senden und empfangen bereits möglich. Sowohl auf der Betty als auch auf dem Scart Adapter.

Es fehlen halt noch die darüberliegenden Schichten auf der Betty und auf dem PC, die die Daten sinnvoll verarbeiten / zur verfügung stellen / anzeigen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=134.msg956#msg956)

---

<a id="msg957"></a>

## 6. markusk · 08. Apr 2008, 10:25

Hallo Telekaz,

so hab ich das auch verstanden, wobei ich mir beim Senden zur Betty nicht 100%ig sicher war. Ob das implementieren eines (einfachen) Terminals nun aufwändig oder nicht ist, kann ich nun nicht beurteilen. Sicherlich sind auch einige Dinge zu beachten, wie Stromverbrauch etc.

Mich würde auch interessieren, ob ich mich weiter um anderweitige Lösungen umschauen sollte oder ob die Entwicklung rund um die Betty noch vorwärts geht.

Gruß
Markus

[Permalink](http://bettyhacks.com/forum/index.php?topic=134.msg957#msg957)

---

<a id="msg1322"></a>

## 7. bn · 28. Feb 2009, 21:08

Hallo markusk,

ich bin aktiver FHEM-Benutzer und -Entwickler und habe mir just Bettys zugelegt, um meine Hausautomation fernzusteuern. Wenn Du noch mitliest würde ich mich freuen, von Dir zu hören.

Grüße,
bn

[Permalink](http://bettyhacks.com/forum/index.php?topic=134.msg1322#msg1322)

---

[← Zurück zu Sonstiges](../boards/07-sonstiges.md) · [Gesamtindex](../index.md)
