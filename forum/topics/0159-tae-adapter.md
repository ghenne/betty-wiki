---
title: "TAE Adapter"
topic_id: 159
board: "Hardware"
board_id: 5
posts: 18
first_post: "07. Sep 2008, 20:08"
last_post: "02. Oktober 2010, 11:53"
authors: ["Capt", "JimBeam", "Matschkeks", "Telekatz", "eme", "famos", "meinbier", "pcsquirrel", "phaidros"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=159.0"
---

# TAE Adapter

[← Hardware](../boards/05-hardware.md) · Thema 159 · 18 Beiträge · 07. Sep 2008, 20:08 – 02. Oktober 2010, 11:53

Beteiligt: Capt, JimBeam, Matschkeks, Telekatz, eme, famos, meinbier, pcsquirrel …

---

<a id="msg1101"></a>

## 1. famos · 07. Sep 2008, 20:08

Ich habe gerade überlegt für was man den TAE-Adaptor verwenden könnte.
Mit dem MSP430c1121 könnte man was machen, da habe ich Doku gefunden. Kennt jemand sich jemand mit diesem Processor aus?
Wer könnte ein Datenblatt vom PCD80703HL auftreiben? Im Wiki ([http://www.bettyhacks.com/wiki/index.php/Talk:TAE_Adapter)](https://web.archive.org/web/2012/http://www.bettyhacks.com/wiki/index.php/Talk:TAE_Adapter)) wurde erwähnt es wäre möglich ein Datenblatt zu bekommen. Mit genügend Infos könnte man mit dem Teil auch was machen.

Gruss famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1101#msg1101)

---

<a id="msg1102"></a>

## 2. eme · 08. Sep 2008, 08:20

Wenn man die Kommunikation zwischen den beiden Mikrocontrollern belauschen würde, wüßte man evtl. wer welche Aufgabe übernimmt. Ich vermute dass die Intelligenz im ARM sitzt und der MSP nur glue-logic spielt. Den großen controller nur als Modem zu benutzen ist wohl overkill.
Vielleicht gibt es bei NXP App Notes oder vielleicht ein eval board mit codebeispielen, dann könnte man das Ding als Anrufbeantworter nutzen ;-)
Es kann auch DTMF erkennen, theroetisch könnte man also den Fernseher über Betty über TAE-Adapter über Telefon bedienen...
Aber Nutzen/Aufwand ist wohl klein..

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1102#msg1102)

---

<a id="msg1106"></a>

## 3. famos · 11. Sep 2008, 21:54

Der Arm hat einige unbelegte Pins. Da könnte man einfach etwas anschliessen. Ein paar Teile könnte man ausschlachten und noch nutzen, die Teile ohne Datenblatt sind aber wertlos.

Gruss famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1106#msg1106)

---

<a id="msg1107"></a>

## 4. Telekatz · 15. Sep 2008, 10:47

Ich habe bei NXP mal nach einem Datenblatt für den PCD80718HL nachgefragt. Hier die Antwort:

> **Zitat**
>
> Thank you for contacting NXP Semiconductors.
>
> The PCD80718HL/D has been discontinued. I do not have any information on the component other than it is a sole source component. Contact Lansdale Semiconductor who is a Supply Source of Certain Previously Discontinued NXP's Products and Replacement Part Information.
>
>
>
> Lansdale Semiconductor, Inc., is an aftermarket manufacturer that supports some of NXP's discontinued product lines.
>
>
>
> For additional information on the availability of certain discontinued NXP's or Signetics' products, as well as replacements for other discontinued products, contact Lansdale Semiconductor, Inc., at 2412 West Huntington Drive, Tempe, Arizona 85252, U.S.A.; phone number 602-438-0123; fax number 602-438-0138, or at [http://www.lansdale.com](https://web.archive.org/web/2012/http://www.lansdale.com).
>
>
>
> NXP Semiconductors has a long-standing licensing agreement with Lansdale Semiconductor, Inc. This agreement covers a large number of both NXP and Signetics obsolete commercial and military integrated circuits that Lansdale either has in inventory, or can manufacture and independently sell under Lansdale's tradename.

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1107#msg1107)

---

<a id="msg1108"></a>

## 5. pcsquirrel · 15. Sep 2008, 14:24

Hallo,

vor einiger Zeit hab ich zufällig dem Chat gelauscht und da hatte einer ( ich glaube es war mamalala) links zu den Datenblättern gepostet.
Ich hab sie mir damals gespeichert und müsste Sie mal suchen. Es stellen sich allerdings 2 Fragen:

1.) die Datanblätter sind "confidential", gibt´s für uns/mich/mamalala dadruch irgendwelche Probleme?
2.) wohin damit, ich glaube Sie hatten einige MB und sind damit als Anhang im Forum eher ungeeignet.

p.c.squirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1108#msg1108)

---

<a id="msg1109"></a>

## 6. Telekatz · 16. Sep 2008, 11:21

Kannst du mir die Datenblätter mal zukommen lassen?

Allgemein zugänglich würde ich die Datenblätter angesichts der confidential Kennzeichnung nicht machen. Eventuell die Datenblätter in ein Passwortgeschütztes Archiv packen und irgendwo hochladen. PW und Link über PN an Interessierte verteilen.

Gruß
Telekatz

*Last Edit : 16. Sep 2008, 18:00 by Telekatz*

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1109#msg1109)

---

<a id="msg1110"></a>

## 7. pcsquirrel · 16. Sep 2008, 15:13

PN am Weg.

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1110#msg1110)

---

<a id="msg1111"></a>

## 8. Telekatz · 16. Sep 2008, 19:37

Danke für das Datenblatt.

Zu deiner Frage über die verbauten Controller: Ich habe hier einen TAE Adapter REV 1.8 in dem der PCD80718HL verbaut ist und 4 TAE Adapter REV 1.9 in denen der PCD80703HL verbaut ist.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1111#msg1111)

---

<a id="msg1112"></a>

## 9. pcsquirrel · 17. Sep 2008, 07:27

Danke

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1112#msg1112)

---

<a id="msg1114"></a>

## 10. famos · 21. Sep 2008, 18:05

> **Zitat**
>
> vor einiger Zeit hab ich zufällig dem Chat gelauscht und da hatte einer ( ich glaube es war mamalala) links zu den Datenblättern gepostet.
> Ich hab sie mir damals gespeichert und müsste Sie mal suchen.

Für welche Bausteine sind die Datenblätter und wem werden Sie zugänglich gemacht? Falls es sich um ein "discontinued product" handelt ist das Confidential wohl überholt.

Gruss famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1114#msg1114)

---

<a id="msg1115"></a>

## 11. Telekatz · 21. Sep 2008, 18:39

Das Datenblatt ist für PCD80715/16/18HL PCD8013/14/15/16/18HL. Auch auf den PCD80703HL sind Teile davon anwendbar.

Nicht alle davon sind abgekündigt. [http://www.nxp.com/acrobat_download/other/eol/dn59_a.pdf](https://web.archive.org/web/2012/http://www.nxp.com/acrobat_download/other/eol/dn59_a.pdf)

Wer will denn alles das Datenblatt?

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1115#msg1115)

---

<a id="msg1127"></a>

## 12. Capt · 22. Okt 2008, 16:57

Hallo an alle!

Ich hätte auch Interesse am Datenblatt, falls das möglich ist.
Die Verwendung des MSPs macht echt überhaupt keinen Sinn. Naja, solange nicht die Fuse gebrannt wurde, sollten wir uns einfach über den zusätzlichen Chip freuen - zumal die Teile einfach nur rocken ("Das Beste was der MSP430 kann ist nichts (tun)"), und ablöten kann man immer noch alles
Falls man den DSP-Teil nicht nutzen kann bleiben vielleicht ja immer noch einige interessante Einsatzzwecke. Ich würde einfach mal probieren, mit einem j-link Code auf das Teil zu flashen, wenn ich mehr Informationen zum ARM7-Core hätte (Flash-Adressen usw.)...

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1127#msg1127)

---

<a id="msg1128"></a>

## 13. Telekatz · 22. Okt 2008, 21:22

Die Verwendung des MSP macht dahingehend Sinn, das er sehr stromsparend sein kann.

Der ARM wird wohl wirklich nur als Modem verwendet. Wenn keine Verbindung zur Bettyzentrale verlangt wird, ist die Stromversorgung zum ARM abgeschaltet.

Nur der PCD80718HL hat einen DSP.

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1128#msg1128)

---

<a id="msg1130"></a>

## 14. Capt · 23. Okt 2008, 08:17

> **Zitat von: Telekatz am 22. Okt 2008, 21:22**
>
> Die Verwendung des MSP macht dahingehend Sinn, das er sehr stromsparend sein kann.
>
> Der ARM wird wohl wirklich nur als Modem verwendet. Wenn keine Verbindung zur Bettyzentrale verlangt wird, ist die Stromversorgung zum ARM abgeschaltet.

Das mit dem MSP ist mir klar, daher das Zitat mit nichts tun
Ich werde mich mal ein wenig mit der Platine beschäftigen. Es wundert mich aber schon ein bisschen, wenn auf einmal Stromverbrauch zum Thema wird - soviel ziehen die Baseband-Chips sonst ja auch nicht und beim Ladeteil hats auch keinen interessiert...

> **Zitat**
>
> Nur der PCD80718HL hat einen DSP.

Ich habe hier nur 80718er, ändert aber nichts an der Sache. Der DSP wäre eh sekundär.

P.S.: Danke.

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1130#msg1130)

---

<a id="msg1131"></a>

## 15. Matschkeks · 23. Okt 2008, 21:03

Hallo,
würdest du mir die Datenblätter auch zukommen lassen?

Ich hab meine Betty noch nicht, aber ab Montag wird gespielt
Ich wollte versuchen den TAE Adapter zur "Alround-Schnittstelle" umzubauen. RS232, RS485, Funkerei, CAN (, USB?) usw. dranbasteln und den Modem-Teil dafür wegkloppen. Mal schauen, inwieweit man das lösen kann.
Mit soner Betty kann man ne Studentenbude wahrscheinlich schon recht gut zentral "Bedienen"

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1131#msg1131)

---

<a id="msg1209"></a>

## 16. phaidros · 05. Januar 2009, 07:49

Hallo auch von mir.
Die Datenblätter würden mich auch sehr interessieren. Ist es noch möglich, die per PN zu bekommen?
Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1209#msg1209)

---

<a id="msg1286"></a>

## 17. JimBeam · 06. Februar 2009, 20:09

Hallo,

da ich von den Dingen, die ich so habe - also auch von Betty - gerne immer alles über deren "Innereien" haben möchte: kann ich das Datenblatt bitte auch bekommen?

Andreas

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1286#msg1286)

---

<a id="msg1664"></a>

## 18. meinbier · 02. Oktober 2010, 11:53

Hallo
ich hät da mal ne Idee was man mit dem TEA Adapter anfangen könnte.
kann man den TEA sich als ein "normales" Telefon ausgeben lassen, Ihn an eine Telefonanlage z.B. Fritzbox hängen und die Ankommenden Gespräche auf dem Betty Bildschirm ausgeben.
Ich weiss ist nichts weiter als ein Callmonitor aber zumindest etwas.

und bevor wieder auf mir rumgehackt wird ja meine Programierkenntnisse sind weniger als bescheiden deshalb nur eine Idee und kein Lösungansatz oder ähnliches.

Mit freundlichem Gruss

meinbier

PS: freue mich schon auf ne Diskussion (auser über Sinn und Unsinn)

[Permalink](http://bettyhacks.com/forum/index.php?topic=159.msg1664#msg1664)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
