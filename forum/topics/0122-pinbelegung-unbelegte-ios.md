---
title: "Pinbelegung / unbelegte IOs?"
topic_id: 122
board: "Hardware"
board_id: 5
posts: 15
first_post: "27. Mär 2008, 09:55"
last_post: "31. Mär 2008, 21:12"
authors: ["Gentoo07", "Telekatz", "eme", "famos", "pcsquirrel"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=122.0"
---

# Pinbelegung / unbelegte IOs?

[← Hardware](../boards/05-hardware.md) · Thema 122 · 15 Beiträge · 27. Mär 2008, 09:55 – 31. Mär 2008, 21:12

Beteiligt: Gentoo07, Telekatz, eme, famos, pcsquirrel

---

<a id="msg862"></a>

## 1. eme · 27. Mär 2008, 09:55

Gibt es eigentlich irgendwo eine komplette Pinbelegung des LPCs?

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg862#msg862)

---

<a id="msg864"></a>

## 2. pcsquirrel · 27. Mär 2008, 15:31

Diese Frage hab ich im Chat schon mal an telekatz gestellt und laut ihm gibt´s "nur" die im WIKI verstreuten Info´s.

Ich hab auch schon darüber nachgedacht eine derartige Aufstellung zu machen.
Vielleicht sollten wir beide uns da ein wenig koordinieren.
Aus einer solchen Aufstellung dann ein Blockdiagramm zuerstellen wäre sicher auch eine gute Idee.

p.c.squirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg864#msg864)

---

<a id="msg866"></a>

## 3. eme · 27. Mär 2008, 17:45

Aha, noch einer, der für Doku ist!

Ich will ja eigentlich nur rausfinden, was man elektronisch noch an der Betty machen kann.
Aus Programmierer-Sicht ist das mittlerweile uninteressant, weil das meiste bereits in Funktionen gekapselt ist. Was benutzt wird, kann man natürlich den Quelltexten entnehmen, nur ist das mühselig, wenn man sich da noch nicht auskennt.

Hier gibt es hier ein Dokument, leider schlecht lesbar: [http://hackdaworld.org/pics/betty/betty_buttons.jpg](https://web.archive.org/web/2012/http://hackdaworld.org/pics/betty/betty_buttons.jpg)
In einem andern Thread habe ich den vermeintlichen Urheber (hackbard = kackhart?) um größere Auflösung gebeten, ich kann's nicht lesen.

Ansonsten bleiben erstmal die boop-Quellen, aufwendiger ist nur das durchklingeln der Hardware. Es sei denn, es gibt Software, die mit guten Scans etwas anfangen kann, und auch Multilayer raten kann. Ein umgekehrter Auto-Router quasi..ich schweife ab.

Wenn am Ende eine Tabelle mit Pins und die Zuordnung zur Hardware steht, wär das gelegentlich bestimmt nützlich. Ein Schaltplan ist wohl zuviel des Guten.

Noch wichtiger als die Hardwarezuordnung halte ich aber eine kurze Einführung in den Aufbau von boop. Ich habe mit ARM noch nicht gearbeitet, aber auch für ARM-Profis
wäre es gut, ein bißchen Hilfe für den schnelleren Einstieg zu bekommen. Aber es scheint, als hätte sich die anfängliche Motivation und Aktivität der Entwickler gelegt (nach soviel Arbeit auch nachvollziehbar), und auch das Interesse an Mitstreitern ist eingeschlafen.

Wiki habe ich versucht etwas zu sortieren und zu ergänzen, ohne redundante Informationen zu erzeugen. Das ist stellenweise nicht leicht, weil alle Bereiche ineinander übergehen, und es auch nicht so toll ist, ständig hin- und herzuspringen. Meiner Meinung nach müsen jetzt noch die Lücken geschlossen werden.. ansonsten nicht zuviel Herzblut reinstecken -der Nächste kommt und sieht alles ganz anders .. bloß nicht wie z.B. die Wikipedialeute enden..

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg866#msg866)

---

<a id="msg870"></a>

## 4. pcsquirrel · 27. Mär 2008, 20:04

Werde mich dann die nächste Zeit mal dran machen das zusammen zu stellen oder willst du das machen?

Ich meinte ein Blockschaltbild und nicht einen kompletten Schaltplan. Werd vielleicht mal ein Beispiel machen.

p.c.squirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg870#msg870)

---

<a id="msg871"></a>

## 5. eme · 27. Mär 2008, 21:15

Habe erstmal genug im Wiki gemacht, möchte mir bei Gelegenheit mal die Software angucken. Ich hoffe aber noch, dass sich ein Qualifizierter findet, der dazu was schreibt.
Wenn Du eine neue Seite >>LPC2220 Pin-Belegung<< oder so anfangen willst, funke ich Dir nicht dazwischen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg871#msg871)

---

<a id="msg873"></a>

## 6. Telekatz · 27. Mär 2008, 21:45

Hallo,

hab mal in meine Notitzen nach Pinbelegungen geschaut

CC1100 <-> ARM
GDO2 <-> P0.24
GDO0 <-> P0.16
MISO <-> P0.18
MOSI <-> P0.19
SCK <-> P0.17
CS <-> P0.23

PCF8563 <-> ARM
INT <-> P0.15
SCL <-> P0.2
SDA <-> P0.3

Die Akkuspannung wird über P2.31 gemessen

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg873#msg873)

---

<a id="msg874"></a>

## 7. pcsquirrel · 27. Mär 2008, 22:14

@telekatz:

danke für die info, werd ich einarbeiten.

@eme:

gut dann werd ich das in den nächsten Tagen angehen.

p.c.squirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg874#msg874)

---

<a id="msg875"></a>

## 8. eme · 27. Mär 2008, 23:15

Klasse!

Aus dem Bild von oben stammt:

AUDIO
P0.7/SSEL0/PWM2/EINT2     69     PWM
P0.11/CTS1/CAP1.1            83     Shutdown

@Telekatz
IR Änderungen eingesehen. Wird also der Komparator LM393 über Pin 84 eingeschaltet und dann dessen Pulse über CAP0.3 gemessen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg875#msg875)

---

<a id="msg877"></a>

## 9. Telekatz · 28. Mär 2008, 20:39

> **Zitat**
>
> @Telekatz
> IR Änderungen eingesehen. Wird also der Komparator LM393 über Pin 84 eingeschaltet und dann dessen Pulse über CAP0.3 gemessen?

Richtig.

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg877#msg877)

---

<a id="msg907"></a>

## 10. Gentoo07 · 30. Mär 2008, 23:51

@eme:

Ich hab die Strichzeichnung der Buttons nun mal in lesbare Form übersetzt, und ins Wiki gestellt: [http://www.bettyhacks.com/wiki/index.php/Betty_Buttons](../../pages/Betty%20Buttons.md)

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg907#msg907)

---

<a id="msg908"></a>

## 11. eme · 31. Mär 2008, 07:47

Schick!
Aber sind die Dateien auf hackdaworld nicht als veraltet anzusehen? (keine Ahnung, von 'den Programmierern' sagt ja leider niemand, was sie machen / wie es steht). Und wie ist das mit dem Interrupt zu verstehen?

[http://bettyhacks.com/wiki/index.php/LPC2220_Pin-Belegung](../../pages/LPC2220%20Pin-Belegung.md) würde ich nach echten Pins sortieren, das nach Ports zu machen finde ich unübersichtlich.

Aber macht, was ihr wollt ;-)

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg908#msg908)

---

<a id="msg909"></a>

## 12. Telekatz · 31. Mär 2008, 08:36

Welcher Interrupt? EINT3 auf P0.30?
Der kann bei jedem Tastendruck ausgelöst werden. Aktuell wird der aber nur dazu genutzt, um wieder aus dem Power Down Modus aufzuwachen. Die Interruptroutine, die die Tasten auswertet ist im Timer0 Interrupt eingehängt

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg909#msg909)

---

<a id="msg910"></a>

## 13. pcsquirrel · 31. Mär 2008, 09:11

Die Sortierung ist Auffassungssache. Beim Programmieren macht die jetztige Sortierung Sinn, da mann ja immer Portweise zugreift.
Die Tabelle ist nun sortierbare.

Danke für´s eintragen auf der Startseite. Ich wollte damit warten bis ich die Aufstellung vollständig habe.

p.c.squirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg910#msg910)

---

<a id="msg911"></a>

## 14. eme · 31. Mär 2008, 13:19

> Die Tabelle ist nun sortierbare.

wow!

> Danke für´s eintragen auf der Startseite. Ich wollte damit warten bis ich die Aufstellung vollständig habe.

Ich dachte, dass dann auch andere eine Chance haben die Lücken zu füllen, wenn sie sie sehen..

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg911#msg911)

---

<a id="msg915"></a>

## 15. famos · 31. Mär 2008, 21:12

Kann mir jemand sagen was auf dem Pin P0.30 für ein Signal ist und woher es kommt? Ist es eine oder Verknüpfung der Keymatrix Signale P0.13, P0.22, P0.27, P0.28 u.s.w.
Wird in keyirq.c als Bedingung für den keyscan verwendet:

   if(!(FIOPIN0 & (1<<30))) { Keyscan ..... }

Gruss

[Permalink](http://bettyhacks.com/forum/index.php?topic=122.msg915#msg915)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
