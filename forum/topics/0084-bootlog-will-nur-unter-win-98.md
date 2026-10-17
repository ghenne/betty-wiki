---
title: "Bootlog will nur unter WIN 98 ???"
topic_id: 84
board: "Hardware"
board_id: 5
posts: 9
first_post: "07. Dez 2007, 09:13"
last_post: "10. Dez 2007, 13:58"
authors: ["Megabug", "asgard", "mcgyver100", "netguy"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=84.0"
---

# Bootlog will nur unter WIN 98 ???

[← Hardware](../boards/05-hardware.md) · Thema 84 · 9 Beiträge · 07. Dez 2007, 09:13 – 10. Dez 2007, 13:58

Beteiligt: Megabug, asgard, mcgyver100, netguy

---

<a id="msg612"></a>

## 1. mcgyver100 · 07. Dez 2007, 09:13

Hi

Habe mir das Interface gebaut und bekomme nur unter WIN 98 ne Verbindung ( kann im Terminal den Bootlog sehen )
Unter WINXP kommt nix .

Also sollte der Adapter ja OK sein .

Wäre auch ned so schlimm wenn Bettyheaven bei mir mit WIN98 laufen würde, will aber ned .

Hat wer noch nen TIP für mich ?

Ach , noch was. Wenn ich RST und eint1 mit anschließe klappt gar nix ( Die Betty macht dann kein Display) oder iss das normal ?
Sehe dann unter WIN98 auch keinen Log .

Danke schon mal .

Habs mit 3 XP Rechnern probiert , geht auf allen nicht

cu mcgyver100

*Last Edit : 07. Dez 2007, 13:57 by mcgyver100*

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg612#msg612)

---

<a id="msg615"></a>

## 2. Megabug · 08. Dez 2007, 22:46

Ja das ist normal. (Mit dem eint und reset)

Die Betty geht dann in den Bootloader wo man halt nichts sieht. Mit lpctool kannst du die betty dann flashen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg615#msg615)

---

<a id="msg616"></a>

## 3. mcgyver100 · 09. Dez 2007, 13:54

Hi

Kann es sein das das Ipctool nur für Linux iss ?

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg616#msg616)

---

<a id="msg617"></a>

## 4. asgard · 09. Dez 2007, 16:58

ja,

dann nehm bettyheaven...am besten du schaust mal ins wiki...

grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg617#msg617)

---

<a id="msg621"></a>

## 5. Megabug · 09. Dez 2007, 19:14

> **Zitat von: mcgyver100 am 09. Dez 2007, 13:54**
>
> Hi
>
> Kann es sein das das Ipctool nur für Linux iss ?

Öhm joa, eigentlich ja.

Gibt auch ne Windows Version, keine Ahnung gerade warum die noch net im Wiki ist. Ich frag mal rum!
EDIT:

Windows Version ist nun im Wiki drin.

Benutzung wie Linux version. Das Device ist das normale, also /dev/ttyS0

*Last Edit : 09. Dez 2007, 19:24 by Megabug*

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg621#msg621)

---

<a id="msg629"></a>

## 6. mcgyver100 · 10. Dez 2007, 10:50

> **Zitat von: asgard am 09. Dez 2007, 16:58**
>
> ja,
>
> dann nehm bettyheaven...am besten du schaust mal ins wiki...
>
> grüße
> asgard

Bettyhaven will unter WIN98 ned ( weiß auch nicht warum )
Und unter WIN XP bekomme ich keine Verbindung zur Betty ( Siehe ganz oben , hatte ich geschrieben )

@megabug

So , mit dem WIN Lpctool komme ich soweit bis er anzeigt :" awaiting autobaud response "
und dann hängt er

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg629#msg629)

---

<a id="msg632"></a>

## 7. asgard · 10. Dez 2007, 12:33

Hi,

kannst du bettyheaven unter winxp nicht einfach mal im kompatibilitätsmodus (Verknüfung erstellen dann rechtsklick  auf verknüpfung->eigenschaften->reiter kompatibilität) laufen lassen?

Vielleicht funzt es dann.

Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg632#msg632)

---

<a id="msg635"></a>

## 8. mcgyver100 · 10. Dez 2007, 13:49

> **Zitat von: asgard am 10. Dez 2007, 12:33**
>
> Hi,
>
> kannst du bettyheaven unter winxp nicht einfach mal im kompatibilitätsmodus (Verknüfung erstellen dann rechtsklick  auf verknüpfung->eigenschaften->reiter kompatibilität) laufen lassen?
>
> Vielleicht funzt es dann.
>
> Grüße
> Asgard

Hi

Also unter WIN 98 kann ich den Bootlog sehen aber nicht unter WINXP

Bettyheaven startet bei mir mit WIN 98 gar nicht unter XP startet es aber ich bekomme einen RX timeout .

Mit dem LPCTool bleibt es unter WIN XP und 98 bei "awaiting autobaud response " hängen .

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg635#msg635)

---

<a id="msg637"></a>

## 9. netguy · 10. Dez 2007, 13:58

> **Zitat von: mcgyver100 am 10. Dez 2007, 13:49**
>
> Hi
>
> Also unter WIN 98 kann ich den Bootlog sehen aber nicht unter WINXP
>
> Bettyheaven startet bei mir mit WIN 98 gar nicht unter XP startet es aber ich bekomme einen RX timeout .
>
> Mit dem LPCTool bleibt es unter WIN XP und 98 bei "awaiting autobaud response " hängen .

dann kommt keine verbindung zustande. nochmal zur sicherheit: reset auf gnd, danach eint auf gnd, danach reset wieder oeffnen und zum schluss eint wieder oeffnen, dann mit lpctool flashen.

lpctool kann auch zwei transistoren ansteuern die das schalten der reset & eint leitung uebernehmen.

ueberpruefe doch nochmal alles ob es auch richtig verbunden ist, und nicht evtl. irgendwo rx/tx vertauscht.
welchen ttl/rs232 wandler nimmst du, und von wo wird er mit strom versorgt? versuche es auch zuerst einmal mit manuellem betaetigen der reset & eint leitungen, koennte ja sein das einer der transistoren defekt ist (sofern du ueberhaupt welche benutzt)

und ueberpruefe auf jeden fall ob der stecker hinten an der betty richtig drauf ist. da ist genug platz um den pinheader herum, so das man leicht einen fehler machen kann und es um eine reihe versetzt aufsteckt.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=84.msg637#msg637)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
