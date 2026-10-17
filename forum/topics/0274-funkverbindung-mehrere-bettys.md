---
title: "Funkverbindung / mehrere Bettys"
topic_id: 274
board: "Sonstiges"
board_id: 7
posts: 3
first_post: "11. Nov 2011, 21:50"
last_post: "15. Nov 2011, 23:52"
authors: ["Flunder", "gunnar"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=274.0"
---

# Funkverbindung / mehrere Bettys

[← Sonstiges](../boards/07-sonstiges.md) · Thema 274 · 3 Beiträge · 11. Nov 2011, 21:50 – 15. Nov 2011, 23:52

Beteiligt: Flunder, gunnar

---

<a id="msg1968"></a>

## 1. Flunder · 11. Nov 2011, 21:50

Hallo,

ich bin leider erst jetzt über Betty gestolpert, es hört sich soweit gut an, ich kann aber noch nicht beurteilen inwieweit sie für mein Vorhaben passen würde. Vielleicht könnt Ihr mir weiterhelfen?

Folgende Infos bräuchte ich zur Funkverbindung:
- Welche Datenübertragungsrate kann erzielt werden?
- Ist die Übertragung bidirektional im Vollduplex oder Halbduplex?
- Können mehrere Bettys auf gleichzeitig im Funk aktiv sein und sich die Funkverbindung teilen?

Danke für Eure Antworten im voraus.

[Permalink](http://bettyhacks.com/forum/index.php?topic=274.msg1968#msg1968)

---

<a id="msg1969"></a>

## 2. gunnar · 15. Nov 2011, 08:56

Hallo Flunder,

im Wiki von Bettyhacks findest Du das Datenblatt des Chips [http://bettyhacks.com/wiki/index.php/CC1100](../../pages/CC1100.md) der für die Funk-Kommunikation zuständig ist. Das ist allerdings etwas komplexer als Zeichen über eine serielle Schnittstelle zu schicken. Der CC1100 kann nicht gleichzeitig senden und empfangen, es geht also nur halbduplex. Mit dem richtigen Protokoll können sich auch mehrere Bettys auf einem Funkkanal befinden, es muss nur geregelt sein, dass immer nur einer sendet.

Wenn Du Dich damit beschäftigen möchtest musst Du an Boop selbst herumprogrammieren. Hier ist ein schönes Beispiel für die Funk-Kommunikation: [http://bettyhacks.com/forum/index.php?topic=220.0](0220-betty-als-mpd-client.md)

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=274.msg1969#msg1969)

---

<a id="msg1970"></a>

## 3. Flunder · 15. Nov 2011, 23:52

Hallo Gunnar,

vielen Dank für Deine Antwort.

> **Zitat von: gunnar am 15. Nov 2011, 08:56**
>
> im Wiki von Bettyhacks findest Du das Datenblatt des Chips [http://bettyhacks.com/wiki/index.php/CC1100](../../pages/CC1100.md) der für die Funk-Kommunikation zuständig ist. Das ist allerdings etwas komplexer als Zeichen über eine serielle Schnittstelle zu schicken. Der CC1100 kann nicht gleichzeitig senden und empfangen, es geht also nur halbduplex.

Halbduplex sollte kein Problem sein, ich werde einen Master haben der dann die einzelnen Clients/Bettys abfragen kann. So zumindest meine derzeitige Vorstellung Und Danke auch für den Hinweis auf das Datenblatt.

> **Zitat von: gunnar am 15. Nov 2011, 08:56**
>
> Wenn Du Dich damit beschäftigen möchtest musst Du an Boop selbst herumprogrammieren. Hier ist ein schönes Beispiel für die Funk-Kommunikation: [http://bettyhacks.com/forum/index.php?topic=220.0](0220-betty-als-mpd-client.md)

Das ich die Funktionen selber programmieren muß, ist mir klar. Der Hinweis auf die existierende Implementierung einer Funk-Kommunikation ist da schon sehr hilfreich.

Ich wollte erst mal grob klären, was die Möglichkeiten der Betty und der Adapter sind, bevor ich das Thema dann nach und nach angehe. Heute habe ich meine erste Betty erhalten und kann mich dann erst mal um die Programmierumgebung und die Flash-Tools inkl. SW/HW kümmern. Sie hat auch noch die Original-Betty-SW drauf und nicht die Universal-FB. Also brauche ich die Tools sowieso um überhaupt mal was ausprobieren zu können.

Vielen Dank

[Permalink](http://bettyhacks.com/forum/index.php?topic=274.msg1970#msg1970)

---

## Verwandte Themen

- [Betty als MPD client](0220-betty-als-mpd-client.md)

[← Zurück zu Sonstiges](../boards/07-sonstiges.md) · [Gesamtindex](../index.md)
