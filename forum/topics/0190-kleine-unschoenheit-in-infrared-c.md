---
title: "Kleine Unschönheit in infrared.c"
topic_id: 190
board: "Software"
board_id: 6
posts: 3
first_post: "05. Feb 2009, 22:33"
last_post: "06. Feb 2009, 14:01"
authors: ["Ge0rG", "JimBeam"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=190.0"
---

# Kleine Unschönheit in infrared.c

[← Software](../boards/06-software.md) · Thema 190 · 3 Beiträge · 05. Feb 2009, 22:33 – 06. Feb 2009, 14:01

Beteiligt: Ge0rG, JimBeam

---

<a id="msg1281"></a>

## 1. JimBeam · 05. Feb 2009, 22:33

Hallo Leute,

erst mal vielen Dank an alle, die hier mitarbeiten/mitgearbeitet haben !!!! Ist viel Arbeit reingeflossen... Und das Ergebnis kann sich sehen lassen! Bisher kann ich zwar nur das beurteilen was ich hier sehe ('ne eBay-Betty ist unterwegs), aber das ist schon ziemlich beeindruckend.

Wenn ich meine Betty habe, werde ich mich etwas mehr mit dem SCART Adapter beschäftigen - ich bin recht firm in der 8051 Programmierung. Mal sehen, was mir da so alles einfällt - falls jemand ne Idee hat: her damit! Erst mal werde ich aber mal mit der bestehenden Firmware rumspielen.

So, nun zu der "Unschönheit" - was ich hier habe ist eigentlich Makulatur, aber ich muß es einfach loswerden 

Die Makro-Aufrufe von doKey(_x, _y) in der Funktion getCode() enden alle mit einem Semikolon, d.h. in Zeile 193 wird aus

  doKey(KEY_A, 0);

dann nach der Expansion

  if(KEY_A) return keyMap[0]; else ;

Ja, ich weiß: Pedant... und es schadet so ja auch nicht... aber ich mag nun mal keine Redundanz... 
Na ja, also in meiner Version hier habe ich im Makro das Ende, also "; else" weggemacht...

Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=190.msg1281#msg1281)

---

<a id="msg1283"></a>

## 2. Ge0rG · 05. Feb 2009, 23:39

Es ist sogar noch viel schlimmer 

Die Funktion kopiert die Logik von getKeynum() und lässt sich unter deren Verwendung auf einen Vierzeiler reduzieren:
`unsigned long getCode(void)
{
 int keynum = getKeynum();
 if (keynum < 42)
  return keyMap[keynum];
 else
  return 0xFFFFFFFF;
}`

Das Makro kann dann auch vorzeitig entlassen werden

[Permalink](http://bettyhacks.com/forum/index.php?topic=190.msg1283#msg1283)

---

<a id="msg1285"></a>

## 3. JimBeam · 06. Feb 2009, 14:01

So weit bin ich noch nicht im Quellcode vorgedrungen - habe erst seit gestern überhaupt Kenntnis von dieser Site bzw. der Existenz von Boop...

Ich habe nur in diesem Teil der Software mal "rumgestöbert", um zu sehen ob man nicht mehr als 4 FB's reinbekommt. Sollte relativ einfach sein, wenn man z.B. die Taste 'D' zum Durchblättern mehrerer Seiten mit jeweils 3 Einträgen (auswählbar dann mit A..C) benutzen würde. Oder man nimmt nur die 'A' Taste zum Aufruf eines Menüs, in dem man mit den Cursortasten die gewünschte FB auswählt. Ist natürlich in beiden Fällen mindestens ein Tastendruck mehr als jetzt, dafür könnte man aber theoretisch beliebig viele FBs gleichzeitig haben - quasi eine "X in 1" Universalfernbedienung (wobei X durchaus groß wählbar ist...). Platz ist ja noch genug, sind ja erst 120k von 1MB verbraten.

Na ja, wenn meine Betty da ist, werde ich mal etwas daran rumspielen.

Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=190.msg1285#msg1285)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
