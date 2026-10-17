---
title: "Kommunikation Scartadapter"
topic_id: 114
board: "Software"
board_id: 6
posts: 3
first_post: "21. Mär 2008, 17:09"
last_post: "21. Mär 2008, 22:46"
authors: ["Telekatz", "edison"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=114.0"
---

# Kommunikation Scartadapter

[← Software](../boards/06-software.md) · Thema 114 · 3 Beiträge · 21. Mär 2008, 17:09 – 21. Mär 2008, 22:46

Beteiligt: Telekatz, edison

---

<a id="msg826"></a>

## 1. edison · 21. Mär 2008, 17:09

Vorgeschichte:

> **Zitat von: edison am 16. Mär 2008, 23:09**
>
> Toll wäre, wenn ich den Scartadapter via 232 an eine SPS koppeln könnte und so die Tastendrücke der Betty abfragen, sowie Texte auf das Display Schreiben könnte.
> Somit wär die Betty für Hausautomatisierungszwecke nutzbar 

> **Zitat von: Telekatz am 20. Mär 2008, 00:06**
>
> eine Übertragung der Tastendrücke an den Scartadapter ist jetzt möglich. Ich habe dafür einen neuen IR encoder hinzugefügt, der anstelle eines IR Signals ein Funkübertragung sendet. Dies ist mit dem Scartadapter im binary mode empfangbar.

Das ist ja klasse,
ich könnte dann quasi den Scartadapter an den Rechner anschließen und im Terminal die gedrückten Tasten sehen?
Gibt es hierzu eine spezielle Firmware für den Scartadapter?
Wie schnell ist dann die Kommunikation (9600,8,N,1 z.B.)?
Bekomme ich auch eine Information daüber, welches Gerät gegenwärtig angewählt ist?

[Permalink](http://bettyhacks.com/forum/index.php?topic=114.msg826#msg826)

---

<a id="msg827"></a>

## 2. Telekatz · 21. Mär 2008, 20:35

> **Zitat**
>
> ich könnte dann quasi den Scartadapter an den Rechner anschließen und im Terminal die gedrückten Tasten sehen?

Man kann die gedrückten Tasten empfangen, allerdings kann man sich das nicht mit einem Terminalprogramm ansehen. Dazu muss man ein Programm schreiben, das den Scartadapter in den Binary Mode schaltet und dann das empfangene decodiert.

> **Zitat**
>
> Gibt es hierzu eine spezielle Firmware für den Scartadapter?
> Wie schnell ist dann die Kommunikation (9600,8,N,1 z.B.)?

Die firmware für den Scartadapter gibt's hier [http://svn.mamalala.org/listing.php?repname=betty_scart&path=%2F&sc=0](https://web.archive.org/web/2012/http://svn.mamalala.org/listing.php?repname=betty_scart&path=%2F&sc=0)
In der readme.txt stehen die Einstellungen für die Serielle Schnittstelle sowie die Befehle zur Kommunikation mit dem Scart Adapter.

> **Zitat**
>
> Bekomme ich auch eine Information daüber, welches Gerät gegenwärtig angewählt ist?

Nein, denn die es funktioniert wie ein eigenes Gerät, das anstelle von Infrarot mit Funk sendet.

[Permalink](http://bettyhacks.com/forum/index.php?topic=114.msg827#msg827)

---

<a id="msg830"></a>

## 3. edison · 21. Mär 2008, 22:46

Danke für die schnelle Antwort,
ich glaub, ich werd mir mal einen Adapter für den Scartadapter löten und mir das Ganze einmal ansehen.

38400 baud schaffe ich so erstmal nich mit meiner SPS, da ist bei 19200 schluß.
Eigenes Gerät ist auch nicht schlecht, hauptsache ich kann umschalten ohne die Rolläden zu öffnen :-)

[Permalink](http://bettyhacks.com/forum/index.php?topic=114.msg830#msg830)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
