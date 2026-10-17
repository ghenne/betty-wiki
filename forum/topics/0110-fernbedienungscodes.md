---
title: "Fernbedienungscodes"
topic_id: 110
board: "Software"
board_id: 6
posts: 13
first_post: "10. Mär 2008, 13:11"
last_post: "04. Okt 2010, 11:45"
authors: ["Gonzo", "Telekatz", "eme", "vdrtux", "waldy", "wynn"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=110.0"
---

# Fernbedienungscodes

[← Software](../boards/06-software.md) · Thema 110 · 13 Beiträge · 10. Mär 2008, 13:11 – 04. Okt 2010, 11:45

Beteiligt: Gonzo, Telekatz, eme, vdrtux, waldy, wynn

---

<a id="msg794"></a>

## 1. wynn · 10. Mär 2008, 13:11

Hallo,

hier mal eine Frage an die Entwickler, Experten und andere Cracks 

Gibt es eigentlich eine Möglichkeit eigene Fernbedienungscodes in das Boop zu integrieren, evtl. in den Quellcode  um den dann neu zu kompilieren ?

Das Boop (der, die, das Boop ?) funktioniert bei mir schon 1a und das Flashen der Betty ist dank der umfassenden Dokumentation auch ein Kinderspiel. Allerdings nützt mir das Teil in diesem Stadium relativ wenig. Wenn es eine Möglichkeit gäbe jede beliebige Fernbedienung zu integrieren könnte man ja hier im Forum eine Datenbank einrichten wo jeder seine Codes einstellen kann. Das würde dem Projekt bestimmt sehr auf die Sprünge helfen.

Ich freue mich auf Eure Antworten
cu
wynn

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg794#msg794)

---

<a id="msg796"></a>

## 2. vdrtux · 10. Mär 2008, 18:36

Hi wynn,

> **Zitat**
>
> Gibt es eigentlich eine Möglichkeit eigene Fernbedienungscodes in das Boop zu integrieren, evtl. in den Quellcode  um den dann neu zu kompilieren ?

na sicher geht das

Schau dir mal die IR-Code-Tabellen auf [http://lirc.sourceforge.net/remotes/](https://web.archive.org/web/2012/http://lirc.sourceforge.net/remotes/) an und vergleiche diese mit denen die in "boop/infrared/ir_codes" liegen.
Wie du die dann einbaust sollte eigentlich selbsterklaerend sein, oder?
Entweder vorhandene Codes ersetzen (easy) oder einen komplett neuen FB-Typ anlegen (leicht aufwendiger) - alles ist da ohne viel Aufwand möglich.

cu
vdrtux

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg796#msg796)

---

<a id="msg797"></a>

## 3. wynn · 10. Mär 2008, 21:28

Ha !

Das scheint ja noch einfacher zu sein als ich zu träumen wagte. Ich habe meinen Problemfall sogar schon in der Datenbank gefunden.
Besten Dank !

cu
wynn

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg797#msg797)

---

<a id="msg892"></a>

## 4. eme · 29. Mär 2008, 20:18

Hi,

ich versuche gerade mich in die IR Routinen einzuarbeiten, um diese Fernbedienung einzubauen:

[http://lirc.sourceforge.net/remotes/olympus/RM-1](https://web.archive.org/web/2012/http://lirc.sourceforge.net/remotes/olympus/RM-1) (NEC-Protokoll)

Wenn ich das am Beispiel von "seleco 027" richtig nachvollziehen kann (leider nicht in der lirc datenbank) ist der ir_spaceenc für 16 Bit Daten ausgelegt, weswegen für "schneider_dtv3" der encoder um die SPACEENC2 Routinen und Defs erweitert worden ist, die die bestehenden Funktionen für mehr Daten aufbohren. Im der eigentlichen Codezuweisung steht dann nur der Verweis auf die Daten in schneider_dtv3_extra.

D.h. ich nehme an, dass ich für obige Fernbedienung ähnlich vorgehen muss?

Was ich noch nicht gefunden habe ist, wo SPACEENC_Init aufgerufen wird.

Wäre nett, wenn Ihr mir etwas Hilfestellung geben könntet!

--

Also ich rate mal dass setEncoder in infrared.c über die struct in encoders.c aufgerufen wird. Zeiger auf Funktion. Ein Grund mal richtig C zu lernen...
Aber wo ist festgelegt, ob der normale oder der erweiterte Encoder zum Einsatz kommt?

*Last Edit : 29. Mär 2008, 20:33 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg892#msg892)

---

<a id="msg1485"></a>

## 5. waldy · 06. Okt 2009, 15:58

Ich hab hier ein Bang & Olufsen Fernseher, den ich gerne mit meiner Betty bedienen würde.
Hab auch Lirc-Codes dafür gefunden:

[http://lirc.sourceforge.net/remotes/bang&olufsen/Beo4](https://web.archive.org/web/2012/http://lirc.sourceforge.net/remotes/bang&olufsen/Beo4)

...jedoch sind dieses leider raw-codes. Gibt es eine Möglichkeit diese in die Betty einzubinden und wenn ja wie?

thx

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1485#msg1485)

---

<a id="msg1486"></a>

## 6. Telekatz · 06. Okt 2009, 19:44

Sehe da keine Möglichkeit. Grund steht in der Lirc-Datei:

> **Zitat**
>
> #   For those who want to build a simple Serial IR receiver, I recommend
> #   sticking to the guide on [www.lirc.org/receivers.html](https://web.archive.org/web/2012/http://www.lirc.org/receivers.html) - however, note
> #   that Bang & Olufsen chose a carrier frequency of 455 kHz (>10x that
> #   of other manufacturers). Thus you need an IR device like Vishay
> #   TSOP7000. It is slightly more expensive, however you should be able
> #   to build a complete Serial IR reciver at around than 20 euros like I
> #   did.

Die Betty kann keinen 455kHz Carrier erzeugen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1486#msg1486)

---

<a id="msg1487"></a>

## 7. Gonzo · 09. Okt 2009, 14:14

Irgendwie hab ich mit dem Einbinden der lirc Codes auch Schwierigkeiten. Gibt es eine Anleitung oder kann mir jemand Tipps geben wie ich z.B. [http://lirc.sourceforge.net/remotes/toshiba/CT-90287](https://web.archive.org/web/2012/http://lirc.sourceforge.net/remotes/toshiba/CT-90287) ins richtige Format für boop bekomme?

Danke schon mal

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1487#msg1487)

---

<a id="msg1512"></a>

## 8. Telekatz · 16. Nov 2009, 12:14

Hallo Gonzo,

in Boop ist jetzt ein LIRC encoder enthalten, bei dem man die entsprechenden Parameter direkt aus dem LIRC config file übernehmen kann. Probier den mal aus.

Gruß

Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1512#msg1512)

---

<a id="msg1513"></a>

## 9. Gonzo · 17. Nov 2009, 00:35

Ok, werd ich bei Gelegenheit mal testen.
Bin z.Zt. am Umziehen und die Betty ist schon verpackt...

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1513#msg1513)

---

<a id="msg1577"></a>

## 10. eme · 31. Jan 2010, 18:01

Habe mich nochmal an [http://lirc.sourceforge.net/remotes/olympus/RM-1](https://web.archive.org/web/2012/http://lirc.sourceforge.net/remotes/olympus/RM-1) versucht:

`boopfirmware/boop/trunk$ svn diff
Index: boop_rom.bin
===================================================================
Cannot display: file marked as a binary type.
svn:mime-type = application/octet-stream
Index: infrared/codes.c
===================================================================
--- infrared/codes.c (revision 19)
+++ infrared/codes.c (working copy)
@@ -222,14 +222,14 @@

 const struct TABLES_L LIRC =
 {
- 5,
+ 6,
  {
   {
    #include "ir_codes/lirc/ufs922"
    "UFS 922"
   },
   {
-   #include "ir_codes/lirc/STR_DE545"
+   #include "ir_codes/lirc/str_de545"
    "STR-DE545"
   },
   {
@@ -243,6 +243,10 @@
   {
    #include "ir_codes/lirc/hx2262"
    "HX2262"
+  },
+  {
+   #include "ir_codes/lirc/olympus_rm-1"
+   "Olympus RM-1"
   }
  }
 };
Index: infrared/encoders.c
===================================================================
--- infrared/encoders.c (revision 19)
+++ infrared/encoders.c (working copy)
@@ -47,6 +47,6 @@
   { SPACEENC_Init,(void*)&SPACEENC, 0, "SPACEENC\0" },
   { IRRF_Init, (void*)&IRRF,  1, "RF\0" },
   { RAW_Init,  (void*)&RAW,  3, "learn" },
-  { LIRC_Init, (void*)&LIRC,  4, "LIRC" }
+  { LIRC_Init, (void*)&LIRC,  5, "LIRC" }
  }
 };`

Nun wird im Menu 06 tables for LIRC 6x "unknown" aufgelistet..
An welcher Stelle muss noch was geändert werden?

Edit: der Encoder funktioniert trotzdem, nur der neue Name aus "const struct TABLES_L LIRC" wird nicht gefunden..

*Last Edit : 31. Jan 2010, 18:23 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1577#msg1577)

---

<a id="msg1578"></a>

## 11. Telekatz · 31. Jan 2010, 20:03

`-  { LIRC_Init, (void*)&LIRC,  4, "LIRC" }
+  { LIRC_Init, (void*)&LIRC,  5, "LIRC" }`

Mach das rückgängig, dann geht's.

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1578#msg1578)

---

<a id="msg1579"></a>

## 12. eme · 31. Jan 2010, 20:16

Sehr gut, danke!

PS: eingecheckt, Apple remote auch hinzugefügt und eingecheckt (22).

*Last Edit : 31. Jan 2010, 22:12 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1579#msg1579)

---

<a id="msg1668"></a>

## 13. eme · 04. Okt 2010, 11:45

Apple remote neulich zum ersten mal getestet - geht einwandfrei :-)

[Permalink](http://bettyhacks.com/forum/index.php?topic=110.msg1668#msg1668)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
