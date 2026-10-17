---
title: "Mitschneiden des Updatevorgangs - allgemein"
topic_id: 7
board: "Software"
board_id: 6
posts: 15
first_post: "29. Jul 2007, 16:41"
last_post: "05. Aug 2007, 12:45"
authors: ["MrFX", "Zimi", "asgard", "theborg", "vSaAmTp"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=7.0"
---

# Mitschneiden des Updatevorgangs - allgemein

[← Software](../boards/06-software.md) · Thema 7 · 15 Beiträge · 29. Jul 2007, 16:41 – 05. Aug 2007, 12:45

Beteiligt: MrFX, Zimi, asgard, theborg, vSaAmTp

---

<a id="msg19"></a>

## 1. asgard · 29. Jul 2007, 16:41

Hi,

hat sich jetzt schon einer mit dem mitschneiden/dumpen des Firmwareupdates beschäftigt?

@Stinki: hast du schon erfolg mit der Fritz!Box?

Vielleicht könnten wir uns dann per BruteForce-Angriff über die Firmware hermachen

Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg19#msg19)

---

<a id="msg23"></a>

## 2. Zimi · 30. Jul 2007, 12:58

Ahauahauaha! Freunde, ihr seid ja total im Tal der Ahnungslosen! Das weiße Ding ist ein analoges Modem. Damit hat man früher, als IT noch EDV hieß, Computer über das Telefon miteinander verbunden. Klar hört sich das an wie ein Fax, denn die benutzen auch Modems.

Das Zeug mitzuschneiden hat nun wieder gar keinen Sinn. Geheimdienste haben bestimmt noch Software sowas wieder in Daten zu wandeln, aber das will man gar nicht! Wenn das Modem über den Analog-VOIP-Channel redet, so kann man da doch auch nur die Audiodaten mitschneiden. Etherreal oder sonst irgendein Packet-Sniffer kann da gar nix mit anfangen!

Ich denke es gibt zwei Möglichkeiten Betty mit neuer Firmware zu versorgen:

1 - Firmware komplett neu flashen, dann muß man nichts mehr über jetzige Firmware herausfinden, kein Bootlog, keine Modemkommunikation, keine MD5-Verschlüsselung, denn das kommt ja sowieso dann alles neu. Das wäre m.E. der beste Weg oder

2 - den eingebauten Updatemechanismus verwenden. Hierzu muß man in der Tat die Kommunikation reengeneeren. Aber doch nicht über Modem-Audio! Ich würde vorschlagen, man baut einen Betty-Funk-Adapter (den benötigt man sowieso, wenn man später mit dem PC mit Betty sprechen möchte). Also irgendwie seriell oder USB auf 433MHz Datenfunk, den Betty ja augenscheinlich verwendet. Man bringt Betty und das Funkmodem soweit auseinander, bis sie sich nicht mehr sehen können. Dann nimmt man einen Funkadapter und bringt ihn in die Nähe des Modems und einen zweiten in die Nähe von Betty. Ein PC in der Mitte mit einer Software, die von beiden Adaptern liest und das Gelesene jeweils auf dem anderen wieder ausgibt, spielt dann the man in the middle. Betty denkt sie spricht mit dem Modem und das Modem denkt es spricht mit Betty. Hier kann man jetzt mitlesen und bei einer Verschlüsselung ggf. versuchen zu entschlüsseln. Der PC kann, wenn man es raus hat, dann mit nur einem Adapter Betty-Zentrale spielen und eigene Updates hochladen. Das scheint wir aufwendiger als Plan 1

Anregung zum Funkadpter kann man sich bestimmt aus dem SCART-Adapter (BTW, welche Spinner haben sich eigentlich solch dämliche Stecker ausgedacht?)

Egal welchen Weg man wählt, man wird genaue Informationen zur Betty Hardware benötigen, sonst kann man keine eigenen Treiber für Tasten, Display, Funk und IR schreiben. Ein Blockschaltbild wäre mal eine gute Idee, ein Schaltplan wäre ideal.

Ich würde gerne einen Betty-Hack sehen, habe aber leider im Moment überhaupt keine Zeit. Macht weiter - aber nicht so :-)

Gruß,
Zimi

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg23#msg23)

---

<a id="msg24"></a>

## 3. asgard · 30. Jul 2007, 13:12

Hi Zimi,

> **Zitat von: Zimi am 30. Jul 2007, 12:58**
>
> Ahauahauaha! Freunde, ihr seid ja total im Tal der Ahnungslosen! Das weiße Ding ist ein analoges Modem. Damit hat man früher, als IT noch EDV hieß, Computer über das Telefon miteinander verbunden. Klar hört sich das an wie ein Fax, denn die benutzen auch Modems.

danke für den Hinweis! Das ist mir klar

> **Zitat von: Zimi am 30. Jul 2007, 12:58**
>
> Das Zeug mitzuschneiden hat nun wieder gar keinen Sinn. Geheimdienste haben bestimmt noch Software sowas wieder in Daten zu wandeln, aber das will man gar nicht! Wenn das Modem über den Analog-VOIP-Channel redet, so kann man da doch auch nur die Audiodaten mitschneiden. Etherreal oder sonst irgendein Packet-Sniffer kann da gar nix mit anfangen!

Ich bin der Meinung, dass es doch einen Sinn hat. Denn die Betty holt sich nun mal Firmware-updates etc. über die Schnittstelle. Wenn man nun die Daten konvertieren könnte, dann hätte man evtl. die Firmware als File zur Verfügung....alles recht umständlich und aufwendig - das muss ich zugeben.

> **Zitat von: Zimi am 30. Jul 2007, 12:58**
>
> 2 - den eingebauten Updatemechanismus verwenden. Hierzu muß man in der Tat die Kommunikation reengeneeren. Aber doch nicht über Modem-Audio! Ich würde vorschlagen, man baut einen Betty-Funk-Adapter (den benötigt man sowieso, wenn man später mit dem PC mit Betty sprechen möchte). Also irgendwie seriell oder USB auf 433MHz Datenfunk, den Betty ja augenscheinlich verwendet. Man bringt Betty und das Funkmodem soweit auseinander, bis sie sich nicht mehr sehen können. Dann nimmt man einen Funkadapter und bringt ihn in die Nähe des Modems und einen zweiten in die Nähe von Betty. Ein PC in der Mitte mit einer Software, die von beiden Adaptern liest und das Gelesene jeweils auf dem anderen wieder ausgibt, spielt dann the man in the middle. Betty denkt sie spricht mit dem Modem und das Modem denkt es spricht mit Betty. Hier kann man jetzt mitlesen und bei einer Verschlüsselung ggf. versuchen zu entschlüsseln. Der PC kann, wenn man es raus hat, dann mit nur einem Adapter Betty-Zentrale spielen und eigene Updates hochladen. Das scheint wir aufwendiger als Plan 1

Dieser Ansatz gefällt mir sehr gut!!
Leider bin ich nur im Besitz einer Betty....vielleicht kann das jemand mal probieren der zwei hat. Ich werde mir wohl noch eine besorgen müssen!

> **Zitat von: Zimi am 30. Jul 2007, 12:58**
>
> Ich würde gerne einen Betty-Hack sehen, habe aber leider im Moment überhaupt keine Zeit. Macht weiter - aber nicht so :-)

Vielen dank für deine Ideen ...freu mich über weiter konstruktive kritik 

Grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg24#msg24)

---

<a id="msg25"></a>

## 4. theborg · 30. Jul 2007, 16:36

> **Zitat von: Zimi am 30. Jul 2007, 12:58**
>
> 1 - Firmware komplett neu flashen, dann muß man nichts mehr über jetzige Firmware herausfinden, kein Bootlog, keine Modemkommunikation, keine MD5-Verschlüsselung, denn das kommt ja sowieso dann alles neu. Das wäre m.E. der beste Weg oder

Das geht nicht der ARM hat einen eingebauten JTAG Scrambler also geht es nur über die Firmware oder über den Bootloader also und das per funk mitschneiden ist wohl zu aufwendig dann kanapper ich mich lieber durch den I2C BUS der die Signale an den Funkchip überträgt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg25#msg25)

---

<a id="msg30"></a>

## 5. Zimi · 30. Jul 2007, 21:37

Und der Scrambler wird wie initialisiert? Ist der Bestandteil der CPU? Sind das dann Custom-Chips? Oder ist der außerhalb der CPU? Dann wäre es doch der gleiche Aufwand den Scrambler zu umgehen wie den I2C-Bus abzugreifen oder? Hat den Scrambler schon mal jemand "erlebt" oder ist das die Information von der Herstellerseite?

Also einen Funk-Adapter braucht man sowieso, wenn man mit einem PC mit Betty sprechen möchte. Wäre sogar ein erster Meilenstein, wenn man der Betty z.B. eingehende Mail ohne weiteren Eingriff pushen könnte...

Wer's kann könnte ja mal auf Basis dieses CC1100-Chips einen Adapter basteln, dann könnte man weitersehen. Ggf. gibt es sowas ja schon, habe noch nicht recherchiert, aber so externe Thermometer verwenden ja auch einen 433MHz Datenfunk, da hat doch bestimmt schon mal wer was für den PC gebaut.

Ansonsten ist natürlich die Möglichkeit die Daten am I2C-Bus abzugreifen ziemlich gut. Nur nicht für jeden geeignet, da invasiv...

Gruß,
       - Zimi

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg30#msg30)

---

<a id="msg31"></a>

## 6. asgard · 30. Jul 2007, 21:57

Hi,

> **Zitat von: Zimi am 30. Jul 2007, 21:37**
>
> Und der Scrambler wird wie initialisiert? Ist der Bestandteil der CPU? Sind das dann Custom-Chips? Oder ist der außerhalb der CPU? Dann wäre es doch der gleiche Aufwand den Scrambler zu umgehen wie den I2C-Bus abzugreifen oder? Hat den Scrambler schon mal jemand "erlebt" oder ist das die Information von der Herstellerseite?

hier wird der scrambler angesprochen...aber nicht direkt im zusammenhang mit der betty...
[http://www.sysoc.de/page1/page1.html](https://web.archive.org/web/2012/http://www.sysoc.de/page1/page1.html)
relativ weit unten (fast ganz unten)!

Grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg31#msg31)

---

<a id="msg32"></a>

## 7. MrFX · 31. Jul 2007, 09:04

Moin!

Ich denke mal, der Scrambler ist im Betty-Bootloader, damit man, wenn man das Teil per eingebautem seriellen Bootloader (was ja per JTAG möglich ist) bootet, nicht auslesen kann.
Möglicherweise läßt er sich aber neu beschreiben.

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg32#msg32)

---

<a id="msg35"></a>

## 8. theborg · 31. Jul 2007, 18:57

Jo hm ich werde mich am we nochmal mit dem JTAG Auseinandersetzen und denn mal schauen ob ich das irgendwie hin bekomme auch mit dem Bootloader.

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg35#msg35)

---

<a id="msg47"></a>

## 9. Zimi · 01. Aug 2007, 21:53

Also klar ist der Scrambler für den Zweck, damit niemand andere Software aufbringen kann. Aber ist er in der Betty wirklich drin? SysOC hat Betty entwickelt und SysOC hat eine ARM-Referenzimplementierung für einen JTAG-Scrambler gemacht. Daraus ergibt sich ja nicht automatisch, dass in der Betty auch der Scrambler drin ist - wenngleich es natürlich naheliegend ist. Man bekommt nur spärliche Informationen zu dem Scrambler und ich kann nicht sehen, dass man bei Philips eine CPU mit integriertem Scrambler bekommen könnte.

Ich denke man sollte diesen Weg nicht aufgrund eines Gerüchts oder einer Vermutung aufgeben.

Gruß,
      - Zimi

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg47#msg47)

---

<a id="msg86"></a>

## 10. vSaAmTp · 02. Aug 2007, 22:08

Hab mich das auch schon gefragt. Wird überall geschrieben, mit dem Scrambler, mit Hinweis auf die Homepage. Aber ne bestätigung gab es noch keine.

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg86#msg86)

---

<a id="msg124"></a>

## 11. asgard · 05. Aug 2007, 07:14

Wollte mal fragen, woher ihr wisst, dass zur datenübertragung zum Funkchip der i2c-bus eingesetzt wird?

Denn meine bescheidenen Kenntnisse sagen mir, dass ich für den i2c-Bus doch SDA und SCL-Leitungen benötige (oder hab ich da womöglich was falsch verstanden?  ).

Aber ich find irgendwie keine auf dem Schaltbild...

Auszug aus dem CC1100-Datasheet
 `4-wire Serial Configuration and Data Interface
CC1100 is configured via a simple 4-wire SPIcompatible
interface (SI, SO, SCLK and CSn)
where CC1100 is the slave. This interface is
also used to read and write buffered data. All
address and data transfer on the SPI interface
is done most significant bit first.`

Also müsste es ja eine Art SPI-Bus sein ([http://de.wikipedia.org/wiki/Serial_Peripheral_Interface](https://web.archive.org/web/2012/http://de.wikipedia.org/wiki/Serial_Peripheral_Interface))

Grüße
Asgard

*Last Edit : 05. Aug 2007, 07:45 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg124#msg124)

---

<a id="msg126"></a>

## 12. Zimi · 05. Aug 2007, 08:21

Hatte theBorg gesagt, dass er das vor hat mit i2c-Bus - Petz petz!

Gruß,
       - Zimi

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg126#msg126)

---

<a id="msg127"></a>

## 13. asgard · 05. Aug 2007, 08:30

Hi Zimi,

> **Zitat von: Zimi am 05. Aug 2007, 08:21**
>
> Hatte theBorg gesagt, dass er das vor hat mit i2c-Bus - Petz petz!

ja weiß ich 

Wollte es nur mal so in den Raum werfen....weil ich mir selber nicht ganz sicher bin

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg127#msg127)

---

<a id="msg129"></a>

## 14. theborg · 05. Aug 2007, 10:20

> **Zitat von: asgard am 05. Aug 2007, 08:30**
>
> Hi Zimi,
>
> > **Zitat von: Zimi am 05. Aug 2007, 08:21**
> >
> > Hatte theBorg gesagt, dass er das vor hat mit i2c-Bus - Petz petz!
>
>
>
> ja weiß ich 
>
> Wollte es nur mal so in den Raum werfen....weil ich mir selber nicht ganz sicher bin

sorry meinte spi nicht i2c

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg129#msg129)

---

<a id="msg130"></a>

## 15. asgard · 05. Aug 2007, 12:45

Borg und natürlich auch alle Anderen,

hast du/habt ihr mir da vielleicht einen tipp wie ich den Abhören/sniffen kann, ohne direkt 300€ für eine fertige Lösung auszugeben 

Kann ich das mit dem LPT realisieren?

EDIT:
würde das hier funktionieren?
[http://www.xs4all.nl/~jwasys/old/diy2.html](https://web.archive.org/web/2012/http://www.xs4all.nl/~jwasys/old/diy2.html)

Grüße
asgard

*Last Edit : 05. Aug 2007, 12:46 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=7.msg130#msg130)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
