---
title: "VT Datenstrom zur Datenübertragung"
topic_id: 82
board: "Software"
board_id: 6
posts: 15
first_post: "04. Dez 2007, 21:55"
last_post: "09. Dez 2007, 23:10"
authors: ["KiLLERHOLiC", "Megabug", "Telekatz", "Zimi", "alterego", "asgard", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=82.0"
---

# VT Datenstrom zur Datenübertragung

[← Software](../boards/06-software.md) · Thema 82 · 15 Beiträge · 04. Dez 2007, 21:55 – 09. Dez 2007, 23:10

Beteiligt: KiLLERHOLiC, Megabug, Telekatz, Zimi, alterego, asgard, netguy

---

<a id="msg600"></a>

## 1. Zimi · 04. Dez 2007, 21:55

Hallo,
da ja nicht alle mit IP-Adaptern versorgt werden konnten, fänd ich es spannend Daten über den SCART-Adapter zu senden. Eine neue Firmware zu machen ist ja nict notwendig, wenn man weiß, wie man die Daten rausschicken muß, damit sie gesendet werden. Hat sich damit schon jemand beschäftigt?

Gruß,
       - Zimi

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg600#msg600)

---

<a id="msg601"></a>

## 2. Telekatz · 04. Dez 2007, 22:51

Hallo,

ich beschäftige mich gerade mit der Datenübertragung vom Scart Adapter zur Betty. Hab für den Scart Adapter eine eigene Firmware geschrieben die Daten von seiner Seriellen Schnittstelle entgegennimmt und an die Betty weitersendet. Testweise funktioniert die Übertragung auch schon.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg601#msg601)

---

<a id="msg602"></a>

## 3. asgard · 05. Dez 2007, 07:19

Hi,

na dann...

Ab damit ins Wiki ...also deine Fortschritte 

Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg602#msg602)

---

<a id="msg603"></a>

## 4. alterego · 05. Dez 2007, 14:19

also wiki-wertes seh ich hier noch nicht. source? genaue infos? garnichts.

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg603#msg603)

---

<a id="msg604"></a>

## 5. Telekatz · 05. Dez 2007, 23:37

Wer die Datenübertragung vom Scartadapter zur Betty ausprobieren möchte, kann meinen Sourcecode hier herunterladen:
[http://telekatz.das-hosting.de/Betty/Rev115_CC1100test.rar](https://web.archive.org/web/2012/http://telekatz.das-hosting.de/Betty/Rev115_CC1100test.rar)

Die Firmware für den Scartadapter wurde mit dem Keil C51 Evaluation Kit V8.09a kompiliert.

Befehle kann man mit einem Terminalprogramm an den Adapter schicken, die Einstellungen dafür sind 9600,8,N,1. Folgende Befehle sind aktuell implementiert:

c                Zeigt den Inhalt der Konfigurationsregister des CC1100 an
t<daten>     Sendet <daten>

Auf der Betty wird der Empfang mit der Taste B aktiviert/deaktiviert (erkennbar an einem kleinen Antennesymbol rechts oben im Display).

Da die Sendeleistung des Scartadapters momentan noch nicht sehr hoch eingestellt ist, muss zum testen die Betty in die Nähe des Scartadapters gehalten werden.

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg604#msg604)

---

<a id="msg605"></a>

## 6. netguy · 06. Dez 2007, 00:40

hallo telekatz,

super arbeit!

wenn du magst, schau dir doch bitte mal den sdcc compiler an: [http://sdcc.sourceforge.net/](https://web.archive.org/web/2012/http://sdcc.sourceforge.net/)
der ist open-source und cross-platform. waere schoen wenn man den benutzt, um eine offene toolchain zu erhalten.

wenn du magst kann ich dir schreibzugriff auf das boop svn geben.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg605#msg605)

---

<a id="msg606"></a>

## 7. Megabug · 06. Dez 2007, 01:30

Sieht schonmal sehr interessant aus!

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg606#msg606)

---

<a id="msg607"></a>

## 8. alterego · 06. Dez 2007, 02:13

ok. DAS ist wiki-würdig!

Respekt und super Arbeit!

Allerdings wäre es in der tat schön, wenn man eine einheitliche toolchain hätte, was a) das erweitern und mit-entwickeln erleichtern und b) eine gemeinsame grundlage zur folge hätte. Vorallem sollten Win und Linux-Nutzer gleichermassen bedacht werden.

Soweit erstmal besten Dank für das einbringen und veröffentlichen deiner Arbeit.

*Last Edit : 06. Dez 2007, 05:44 by alterego*

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg607#msg607)

---

<a id="msg609"></a>

## 9. KiLLERHOLiC · 06. Dez 2007, 15:36

Klingt ja sehr gut was du gemacht hast, wie kann ich mir das Vorstellen?
Werden die gesendeten Daten direkt am Display der Betty angezeigt?
Ich hätte gerne eine Uhr auf dem Display, hab es aber nicht geschafft eine zu Programieren. Das kompilieren funktioniert, aber beim linken gibts Probleme mit der gettimeofday funktion.
Da ich sowieso einen VDR zum Fernsehen verwende wäre es kein Problem den Scart Adapter über die Serielle damit zu verbinden und die Uhrzeit wegzuschicken.

mfg
KiLLERHOLiC

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg609#msg609)

---

<a id="msg610"></a>

## 10. Telekatz · 06. Dez 2007, 23:52

Werde es am Wochenende mal probieren die Firmware für den Scartadapter mit dem sdcc zu erstellen.

Die Daten werden direkt auf dem Display angezeigt. Allerdings ist die Übertagung so wie sie momentan ist noch nicht wirklich sinnvoll einsetzbar, da gibt es noch einiges zu optimieren.

@netguy
Das mit dem Schreibzugriff auf das boop svn würde ich gerne annehmen.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg610#msg610)

---

<a id="msg611"></a>

## 11. netguy · 07. Dez 2007, 00:21

hallo,

so, habe dir den zugriff eingerichtet, daten haste in einer pm.

das mit dem cc1100 will bei mir nicht so wirklich klappen, allerdings zwischen zwei betties, nicht zwischen scart/betty.

wie du evtl. auch schon in meiner letzten nachricht im neuen thread gelesen hast, die verzeichnisstrucktur habe ich mal ein wenig aufgeraeumt.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg611#msg611)

---

<a id="msg613"></a>

## 12. Telekatz · 07. Dez 2007, 18:55

Hallo,

der Grund warum die Übertragung zwischen den beiden Betty nicht funktioniert ist der, dass der Sendepuffer leerläuft. Das erste Byte das in den Sendepuffer geschrieben wird gibt die Anzahl der zu übertragenen Bytes an, zählt aber selbst nicht dazu. Habs entsprechend geändert.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg613#msg613)

---

<a id="msg614"></a>

## 13. netguy · 07. Dez 2007, 19:37

hallo telekatz,

ahh, super. hab das irgendwie wohl uebersehen

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg614#msg614)

---

<a id="msg624"></a>

## 14. Telekatz · 09. Dez 2007, 23:00

Hallo,

habs nun geschafft die Firmware für des Scart Adapter mit dem sdcc zu erstellen. Damit hätten wir auch dafür eine offene toolchain.

Netguy, hättest du eventuell auf deinem Server noch Platz für ein zusätzliches SVN für den Scart Adapter?

Gruß,

Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg624#msg624)

---

<a id="msg625"></a>

## 15. netguy · 09. Dez 2007, 23:10

hallo telekatz,

> **Zitat von: Telekatz am 09. Dez 2007, 23:00**
>
> Hallo,
>
> habs nun geschafft die Firmware für des Scart Adapter mit dem sdcc zu erstellen. Damit hätten wir auch dafür eine offene toolchain.

hey, super! zum thema cc1100 haette ich dann eh eon paar fragen an dich

> **Zitat von: Telekatz am 09. Dez 2007, 23:00**
>
> Netguy, hättest du eventuell auf deinem Server noch Platz für ein zusätzliches SVN für den Scart Adapter?
>
> Gruß,
>
> Telekatz

ja, klar ... ist angelegt, repo name ist betty_scart, user & pw fuer dich das gleiche wie bei boop.

waere schoen wenn du uns mal im irc besuchen koenntest, server ist irc.freenode.net, kanal ist #bettyhacks.
besonders spannend ist natuerlich die frage wie es nun mit dem rf kram weitergeht, da der ja jetzt funktioniert. z.b. habe ich jetzt timer callbacks eingebaut (min. aufloesung 5 ms). auch haengt der chip wohl sobald ein paket nicht korrekt empfangen wurde, man muss den empfang dann wieder starten.

weisst du welche irq moeglichkeiten des cc1100 genutzt werden koennen? also welche von den gpio's zu irq tauglichen eingaengen des lpc gehen? dann sollte man naemlich evtl. ein kleines message-handling einbauen als irq routine (auch das irw-handling hat sich jetzt in boop geaendert und funktioniert einwandfrei), die dann entsprechend auf status-fehler des cc's reagiert und das behandelt. man koennte ja 1kb vom ram fest als buffer vergeben.

ach ja, und noch so vieles mehr ...  
wie gesagt, komm doch mal in den chat ...

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=82.msg625#msg625)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
