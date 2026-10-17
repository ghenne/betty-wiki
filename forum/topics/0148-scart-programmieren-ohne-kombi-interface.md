---
title: "Scart programmieren, ohne Kombi-Interface!!"
topic_id: 148
board: "Software"
board_id: 6
posts: 12
first_post: "05. Juni 2008, 22:16"
last_post: "01. Februar 2010, 12:09"
authors: ["El_Barto", "Gentoo07", "MrFX", "TEN", "Telekatz", "bettyuser", "damaltor", "eme", "gunnar", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=148.0"
---

# Scart programmieren, ohne Kombi-Interface!!

[← Software](../boards/06-software.md) · Thema 148 · 12 Beiträge · 05. Juni 2008, 22:16 – 01. Februar 2010, 12:09

Beteiligt: El_Barto, Gentoo07, MrFX, TEN, Telekatz, bettyuser, damaltor, eme …

---

<a id="msg1055"></a>

## 1. bettyuser · 05. Juni 2008, 22:16

Hallo,

für alle die sich kein Kombi-Interface o.ä. zum Programmieren des Scart-Adapters basteln wollen, gibt es eine einfachere Möglichkeit.
Ich habe die ICP-Routinen auf einen für alle verfügbaren Mikrocontroller portiert - die Betty!
Anbei eine Version der Boop-Software, die ein betty_scart SW-Image und die entsprechenden Routinen zum Programmieren des Scart-Adapters enthält.

Es ist keine weitere Elektronik notwendig, einfach den Stecker der Betty mit dem des Scart verbinden.
Die Verbindung ist dabei wie folgt:
**Betty:                        Scart:**
GND             <--->  GND
EINT1/P0.14  <--->  Reset
TX/P0.0        <--->  PCL/P0.5
RX/P0.1        <--->  PDA/P0.4

Es ist kein Pegelwandler notwendig, da beide mit 3,3V arbeiten,
VCC darf zwischen Betty und Scart jedoch NICHT verbunden werden!
Um Betty und Scart nicht zu beschädigen, sollte entsprechend der auf dem Betty-Display angegebenen Reihenfolge vorgegangen werden.

Viel Spass!!

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1055#msg1055)

---

<a id="msg1056"></a>

## 2. eme · 06. Juni 2008, 22:02

Nette Idee!

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1056#msg1056)

---

<a id="msg1061"></a>

## 3. Gentoo07 · 15. Juni 2008, 23:59

Vielen dank!

Das Programm erspart mir mit meinem einfachen Handydatenkabel für die Betty einiges an Bastelarbeit, und das Programm auf dem Adapter werd ich wohl weniger häufig als daß der Betty updaten.

Ich habe es gerade ausprobiert und es funktioniert wunderprächtig!

Interessehalber: Wie wandelt man den denn die kompilierte .bin oder .hex-datei für den Scart-Adapter in die Textform für dein Tool um?

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1061#msg1061)

---

<a id="msg1064"></a>

## 4. MrFX · 16. Juni 2008, 14:57

Moin!

Mit WinBin geht das z. B.:

[http://www.ulrichradig.de/home/index.php/projekte/winbin](https://web.archive.org/web/2012/http://www.ulrichradig.de/home/index.php/projekte/winbin)

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1064#msg1064)

---

<a id="msg1066"></a>

## 5. Telekatz · 20. Juni 2008, 18:49

Hallo bettyuser,

gute Arbeit. Hab die Änderung ins SVN Repository eingecheckt.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1066#msg1066)

---

<a id="msg1145"></a>

## 6. TEN · 04. November 2008, 00:13

> **Zitat von: bettyuser am 05. Juni 2008, 22:16**
>
> für alle die sich kein Kombi-Interface o.ä. zum Programmieren des Scart-Adapters basteln wollen, gibt es eine einfachere Möglichkeit.
> Ich habe die ICP-Routinen auf einen für alle verfügbaren Mikrocontroller portiert - die Betty!
> Anbei eine Version der Boop-Software, die ein betty_scart SW-Image und die entsprechenden Routinen zum Programmieren des Scart-Adapters enthält.

Bietet sich doch eigentlich an, diese ICP-Routinen auch zum Programmieren anderer Betties zu nutzen, und damit die Verbreitung von boop ganz ohne Interface-Basteleien wesentlich zu erleichtern?

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1145#msg1145)

---

<a id="msg1146"></a>

## 7. netguy · 04. November 2008, 02:55

Hallo TEN,

das sinnvollste wird es langfristig sein das ganze über Funk zu machen. Demnächst werde ich mich wieder an Boop setzen und u.A. einen ordentlichen Bootloader integrieren. Der sollte dann idealerweise sowohl seriell als auch über Funk ansprechbar sein.

Grüße,

Chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1146#msg1146)

---

<a id="msg1215"></a>

## 8. damaltor · 12. Januar 2009, 21:31

könnte man das mal zusammenfassen?

man baut das image für den scart, soweit versteh ich das... dann lädt man das ganze in winbin (gibts da eigentlich ein linux tool?) und formatiert es um (welche einstellungen werden benötigt?). wie bekommt man das dann in die betty? das mit dem kabel ist mir klar, aber erstmal muss die betty doch drauf vorbereitet werden...

danke,

Malte

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1215#msg1215)

---

<a id="msg1218"></a>

## 9. Telekatz · 12. Januar 2009, 22:00

Man wandle das Image vom Scartadapter in Hexcode um, schreibe diesen in die tools/scart_image.h hinein, kompiliere Boop und flashe dieses, theoretisch gesprochen.

Hab's aber noch nicht selbst gemacht.

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1218#msg1218)

---

<a id="msg1257"></a>

## 10. El_Barto · 23. Januar 2009, 09:01

Hallo,

ich habe das Tool auch gerade erfolgreich getestet. Hat etwas gedauert, aber nun tut es. Was mir jedoch noch aufgefallen ist: Die Config-Bytes werden nicht geändert, so dass nach dem Flashen noch immer die alte Config aktiv ist.
Deshalb habe ich das Menü erweitert und die trivialen Funktionsaufrufe für eine Änderung der ConfigBytes eingebaut.
Anbei ein patch mit den änderungen

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1257#msg1257)

---

<a id="msg1259"></a>

## 11. Telekatz · 23. Januar 2009, 09:47

Die beiden UCFG Bytes müssen nicht unbedingt geändert werden, das läuft auch mit der vorhandenen Einstellung.

Boot Vector und Status Byte wird bereits passend geändert.

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1259#msg1259)

---

<a id="msg1584"></a>

## 12. gunnar · 01. Februar 2010, 12:09

> **Zitat von: El_Barto am 23. Januar 2009, 09:01**
>
> Deshalb habe ich das Menü erweitert und die trivialen Funktionsaufrufe für eine Änderung der ConfigBytes eingebaut.
> Anbei ein patch mit den änderungen

Hallo El_Barto,

ich war so frei Deinen Patch einzuchecken.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=148.msg1584#msg1584)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
