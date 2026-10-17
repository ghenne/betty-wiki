---
title: "lpctool - schneller upload"
topic_id: 54
board: "Software"
board_id: 6
posts: 32
first_post: "10. Sep 2007, 20:22"
last_post: "10. Jul 2008, 14:05"
authors: ["Megabug", "MrFX", "Ronin", "eme", "localhosthack0r", "netguy", "pcsquirrel", "theborg"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=54.0"
---

# lpctool - schneller upload

[← Software](../boards/06-software.md) · Thema 54 · 32 Beiträge · 10. Sep 2007, 20:22 – 10. Jul 2008, 14:05

Beteiligt: Megabug, MrFX, Ronin, eme, localhosthack0r, netguy, pcsquirrel, theborg

---

<a id="msg329"></a>

## 1. netguy · 10. Sep 2007, 20:22

hallo zusammen,

unter [http://mamalala.org/lpctool-0.1.tgz](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.1.tgz) ist ein neues tool zu finden, um code in den lpc2220 zu laden.

zur zeit wird nur der upload in das ram unterstuetzt, am flash arbeite ich gerade (75% fertig)

das tool ist ca. 10 mal schneller als lpcload von hackbard beim upload ins ram unter benutzung des lpc internen bootloaders.

mit "lpctool -?" bekommt man hilfe.

gruss,

chris

edit:

zum vergleich mal die zeiten, zuerst mit lpcload:

root@desk:~/bettystuff/boop-0.7# time ./lpcload -d /dev/ttyS0 -f boop.hex
boot loader init ...
write firmware to ram ...
unlock go command ...
go ...
flushing lpc tx buffer: 30 0d 0a

real    1m0.380s
user    0m0.000s
sys     0m0.000s

und hier mit lpctool:
root@desk:~/bettystuff/boop-0.7# time ./lpctool -r boop.bin
This Software is free Software under GNU GPL 3 or later
(c) 2007 Ch. Klippel <ck@mamalala.net>

using ram image boop.bin
wrote 228 bytes @ 40003A00

real    0m6.331s
user    0m0.004s
sys     0m0.000s

wobei code-maessig die .bin und die .hex gleich sind, lediglich das dateiformat ist anders.

*Last Edit : 10. Sep 2007, 20:30 by netguy*

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg329#msg329)

---

<a id="msg331"></a>

## 2. netguy · 11. Sep 2007, 14:13

so, flash schreiben geht jetzt auch:

[http://mamalala.org/lpctool-0.2.tgz](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.2.tgz)

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg331#msg331)

---

<a id="msg338"></a>

## 3. netguy · 14. Sep 2007, 18:07

hallo alle zusammen,

unter [http://mamalala.org/lpctool-0.4.tgz](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.4.tgz) gibt es die neueste version des schnellen upload tools.

mit -V werden infomeldungen ausgegeben, auch gibt es jetzt fehlermeldungen wenn was schief geht, ebenso ist mit -? eine hilfe da.
das loeschen von sektoren "on demand" fehlt noch, genauso wie das auslesen des flash/ram.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg338#msg338)

---

<a id="msg340"></a>

## 4. Megabug · 15. Sep 2007, 17:26

Was genau muss vom µClinux installiert sein damit ich das compilen kann? Binutils?

mh wahrscheinlich das: [http://opensrc.sec.samsung.com/download/arm-uclinux-tools-base-gcc3.4.0-20040713.sh](https://web.archive.org/web/2012/http://opensrc.sec.samsung.com/download/arm-uclinux-tools-base-gcc3.4.0-20040713.sh)  ?

*Last Edit : 15. Sep 2007, 17:37 by Megabug*

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg340#msg340)

---

<a id="msg341"></a>

## 5. netguy · 15. Sep 2007, 17:54

> **Zitat von: Megabug am 15. Sep 2007, 17:26**
>
> Was genau muss vom µClinux installiert sein damit ich das compilen kann? Binutils?
>
>
> mh wahrscheinlich das: [http://opensrc.sec.samsung.com/download/arm-uclinux-tools-base-gcc3.4.0-20040713.sh](https://web.archive.org/web/2012/http://opensrc.sec.samsung.com/download/arm-uclinux-tools-base-gcc3.4.0-20040713.sh)  ?

100 punkte

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg341#msg341)

---

<a id="msg342"></a>

## 6. Megabug · 15. Sep 2007, 17:59

zenega:/home/megabug/betty# sh arm-uclinux-tools-base-gcc3.4.0-20040713.sh
tail: Warning: "+number" syntax is deprecated, please use "-n +number"
arm-uclinux-tools-base-gcc3.4.0-20040713.sh: line 42: bunzip2: command not found
zenega:/home/megabug/betty#

Ahja, debian...  2.6.18-5-686

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg342#msg342)

---

<a id="msg343"></a>

## 7. netguy · 15. Sep 2007, 18:52

> **Zitat von: Megabug am 15. Sep 2007, 17:59**
>
> zenega:/home/megabug/betty# sh arm-uclinux-tools-base-gcc3.4.0-20040713.sh
> tail: Warning: "+number" syntax is deprecated, please use "-n +number"
> arm-uclinux-tools-base-gcc3.4.0-20040713.sh: line 42: bunzip2: command not found
> zenega:/home/megabug/betty#

apt-get install bzip2

sollte man aber eigentlich haben .... was haste denn gemacht, das es nicht da ist?

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg343#msg343)

---

<a id="msg344"></a>

## 8. Megabug · 15. Sep 2007, 19:29

Öhm keine Ahnung.

./lpctool -r boop.bin -s /dev/ttyUSB1   <- so richtig?

ttyUSB1 ist mein datenkabel an der betty. USB0 ist mein Adapter wo meine USV dranhängt.

EDIT:

Solltest die hilfe ändern... ist nicht -s sondern -d...

> **Zitat**
>
> to do the same, but using serial device /dev/ttyS1 instead :
> lpcload -r -s /dev/ttyS1

`zenega:/home/megabug/betty/lpctool-0.4# ./lpctool -r boop.bin -d /dev/ttyUSB1

Welcome to lpctool V0.4

This Software is free Software under GNU GPL 3 or later
(c) 2007 Ch. Klippel <ck@mamalala.net>

ERROR: autobaud detection failed
ERROR: Error opening BootLoader
zenega:/home/megabug/betty/lpctool-0.4#`

*Last Edit : 15. Sep 2007, 19:36 by Megabug*

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg344#msg344)

---

<a id="msg345"></a>

## 9. netguy · 15. Sep 2007, 22:37

moin megabug,

jo, das mit dem -s habe ich jetzt mal geaendert ...

wegen dem fehler kann ich im moment auch nichts sagen. ich habe das hier auch oefter mal, auf einem regulaeren rs232 port (also kein usb adapter). auch wenn man in dem moment mal mit einem terminal draufgeht, sieht man das die kommunikation fehelerhaft ist (bei "Synchronized" kommen muellzeichen mit)

bisher hat es immer geholfen enweder, wenn eint geschlossen ist, mehrmals reset zu druecken ... oder einmal reset ohne eint, dann tool starten (was natuerlich einen fehler bringt), danach wieder mit eint & reset in den bootloader und erneut versuchen. damit klappt das bei mir immer.

ich hoffe das ich den bug irgendwann mal wegbekomme, aber ich _vermute_ das es u.u. mit kontaktprellen auf der reset & eint leitung zu tun hat, wenn man dort einfach nur taster anschliesst (so wie ich).

evtl. muss man die autobaud auch einfach mit niedrigerer geschwindigkeit machen, und dann "hochschalten" .... in den naechsten tagen weiss ich mehr ...

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg345#msg345)

---

<a id="msg346"></a>

## 10. netguy · 16. Sep 2007, 01:36

hallo,

habe jetzt den fehler beseitigt, der dafuer sorgte das am anfang die kommunikation schiefgeht.

aktuelle version ist jetzt unter [http://mamalala.org/lpctool-0.5.tgz](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.5.tgz) zu finden.
zwei parameter haben sich geaendert, -V gibt jetzt nur die version aus, und -v schaltet die info-meldungen an.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg346#msg346)

---

<a id="msg348"></a>

## 11. Megabug · 16. Sep 2007, 12:48

jetzt tut es bei mir nichts mehr.

bei opening bootloader bleibts stehen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg348#msg348)

---

<a id="msg349"></a>

## 12. netguy · 16. Sep 2007, 12:57

> **Zitat von: Megabug am 16. Sep 2007, 12:48**
>
> jetzt tut es bei mir nichts mehr.
>
> bei opening bootloader bleibts stehen.

hmm, sicher das du waehrend des reset die eint leitung haelst? hier bleibt er eigentlich nur stehen wenn er garnicht mit der gegenseite sprechen kann, also wenn nichts zurueckkommt. wenn eine kommunikation moeglich, aber fehlerhaft ist, bricht er ab.

allerdings habe ich gestern nacht noch kleinere aenderungen gemacht, irgendwann war auch ein  fehler drin, den ich dann beseitigt habe.
lade das archiv doch einfach nochmal runter....

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg349#msg349)

---

<a id="msg350"></a>

## 13. Megabug · 16. Sep 2007, 15:42

Endweder sofort fehler oder bleibt hängen bei
Info : opening serial device /dev/ttyUSB1
Info : opening ram image boop.bin
Info : opening bootloader

Wenn er mal sofort nen Fehler ausgibt:

ERROR: autobaud detection failed
ERROR: Error opening BootLoader

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg350#msg350)

---

<a id="msg352"></a>

## 14. netguy · 16. Sep 2007, 16:31

hallo megabug,

hmm, dann weiss ich im moment auch nicht weiter. ich habe keinen usb<->seriell adapter hier, daher kann ich es auch nicht testen.
ich habe jetzt nochmal eine geaenderte version hochgeladen, gleicher name, die ein paar mehr fehlermeldungen ausgibt, allerdings wird das in deinem fall auch nicht mehr anzeigen.

bleibt eigentlich nur noch der adapter als ursache, ueber usb ist die kommunikation ja etwas anders als direkt mit einer seriellen leitung wegen der usb paketgroesse und dem polling intervall. wenn du kannst, schau dir mal die routine openSerial() in lpctool_serial.c, ab zeile 79 an. dor wird der port geoeffnet und eingestellt. wahrscheinlich ist dort der fehler zu suchen, kann sein das der port in einen modus gesetzt wird mit dem der adapter nicht klarkommt. aber da ich es ja selber hier nicht testen kann, muessen dort andere einspringen, oder mir einen usb<->seriell adapter schicken.

bist du auf den adapter angewiesen, oder hast du auch eine regulaere rs232 schnittstelle?

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg352#msg352)

---

<a id="msg354"></a>

## 15. Megabug · 17. Sep 2007, 11:10

Hi, gib mir deine Adresse dann schick ich dir einen. Hab 3 davon hier. Siemens Datenkabel.

Bin leider drauf angewiesen. Mein normaler PC hat keine seriell ports mehr und bei meiner S100 box (t-online vision, da hab ich auch das debian laufen) wollen die seriellen ports nicht so recht.

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg354#msg354)

---

<a id="msg359"></a>

## 16. netguy · 17. Sep 2007, 12:54

> **Zitat von: Megabug am 17. Sep 2007, 11:10**
>
> Hi, gib mir deine Adresse dann schick ich dir einen. Hab 3 davon hier. Siemens Datenkabel.
>
> Bin leider drauf angewiesen. Mein normaler PC hat keine seriell ports mehr und bei meiner S100 box (t-online vision, da hab ich auch das debian laufen) wollen die seriellen ports nicht so recht.

ok, ahbe die eine email geschickt.

es ist wirklich eine schande das ganz normale, und vor allem sehr nuetzliche schnittstellen verschwinden. gerade seriell und parport sollte wirklich jeder rechner haben. und wenn es am platz liegt, es spricht ja nichts dagegen mini-buchsen anstelle der normalen zu verwenden ...

bis denne,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg359#msg359)

---

<a id="msg364"></a>

## 17. netguy · 18. Sep 2007, 00:12

hallo zusammen,

unter [http://mamalala.org/lpctool-0.6.tgz](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.6.tgz) gibt es eine neue version.

wenn man zwei n-kanal mosfets (z.b. bs170) und zwei 1 kohm widerstaende hat, kann die betty nun automatisch resettet werden und ebenfalls in den internen bootloader gebracht werden.

die mosfets mit den source pins auf gnd legen, die drain pins gehen dann je einer auf die reset, der andere auf die eint leitung. nun loetet man je einen widerstand von dem gate eines fet's zu gnd. das gate des reset fet's geht auf pin 4 des seriellen kabels (dtr leitung), das gate des eint fet's geht auf pin 7 (rts). die nummern beziehen sich auf einen 9-poligen seriellen stecker. wer mag kann noch je eine 1n4148 diode zwische dtr/rts und des gates schalten (der ring zum gate hin) anstelle eine direkte verbindung zu machen. aber normalerweise machen dem fet die -12 volt nix aus.

wenn nun etwas ins ram geladen wird, wird automatisch ein reset gemacht und in den internen bootloader gestartet (eint). wenn man etwas in's flash geladen hat, wird automatisch ein reset gemacht. diesen reset-nach-flash kann man mit -N verhindern.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg364#msg364)

---

<a id="msg365"></a>

## 18. Megabug · 18. Sep 2007, 00:24

*gg* da kann jemand wohl nicht schlafen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg365#msg365)

---

<a id="msg366"></a>

## 19. theborg · 18. Sep 2007, 00:30

das ist meine schaltung hab sie so abgeendert das es gehen solte mit sicherheit kann ich das aber erst morgen sagen

*Last Edit : 18. Sep 2007, 11:14 by theborg*

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg366#msg366)

---

<a id="msg369"></a>

## 20. netguy · 19. Sep 2007, 19:52

hallo alle zusammen,

unter [http://mamalala.org/lpctool-0.7.tgz](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.7.tgz) gibt es die neueste version.

hinzugekommen sind die parameter -c (erstes flash) bzw. -C (zweites flash).
diese bewirken das groessere ansammlungen von 0xFFFFFFFF uebersprungen werden.

das resultat: der upload der original-firmware, inklusive loeaschen der beiden flash und upload des tools, betraegt nun zwischen 2 und 3 minuten.

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg369#msg369)

---

<a id="msg370"></a>

## 21. netguy · 20. Sep 2007, 03:43

hallo,

unter [http://mamalala.org/lpctool-0.8.tgz](https://web.archive.org/web/2012/http://mamalala.org/lpctool-0.8.tgz) gibts wieder mal eine neue version.

das flash-utility fuer das ram ist nun integriert und kann mit -i ausgewaehlt werden. natuerlich kann nachwievor mit -r [name] ein externes file verwendet werden.
der vortiel ist das man nun nicht immer das ramtool.bin im gleichen verzeichnis haben muss. beispiel-kommadozeile um ein backup der flash's wieder einzuspielen:

lpctool -i -e -E -c -a Flash1.bin -b Flash2.bin

-i: internes image fuer das flashtool verwenden, -e und -E: erstes und zweites flash komplett loeschen, -a und -b geben die .bin dateien fuer die beiden flash's an, und durch -c werden groessere ansammlungen von 0xFFFFFFFF uebersprungen um den transfer zu beschleunigen.

jetzt fehlt nur noch das auslesen, dann kommt eine nette gui dazu....

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg370#msg370)

---

<a id="msg739"></a>

## 22. localhosthack0r · 30. Jan 2008, 21:26

> **Zitat von: netguy am 20. Sep 2007, 03:43**
>
> jetzt fehlt nur noch das auslesen, dann kommt eine nette gui dazu....

Wird das noch weiterentwickelt? Kann man jetzt scho auslesen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg739#msg739)

---

<a id="msg833"></a>

## 23. eme · 25. Mär 2008, 00:40

hallo, ich versuche gerade mit einem ft232rl und lpctool-cygwin 0.9 das aktuelle boop_rom.bin zu flashen.

ich sehe auch eine sequenz auf eint1 und reset

`EINT PIN auf GND bruecken
RESET PIN auf GND bruecken
RESET PIN wieder oeffnen
EINT PIN wieder oeffnen`

aber es scheint mir vom timing eher andersherum. ich hoffe, ich habe da nicht die leitungen vertauscht..

jedenfalls sagt lpctool:

 `lpctool-cygwin>lpctool -d /dev/com4
-i -v -e -a boop_rom.bin

lpctool V0.9

This Software is free Software under GNU GPL 3 or later
(c) 2007 Ch. Klippel

Info : erasing flash #0 before write
Info : using flash #0 image boop_rom.bin
Info : opening serial device /dev/com4
Info : reset into bootmode
Info : opening bootloader
Info : initiating auto-baud
Info : awaiting autobaud response
Info : got response, answering
Info : setting frequency
Info : switching baudrate
Info : disabling echo

....Abbruch...`

Da bleibt es dann stehen. Bettys LCD ist leer, nach einem power-on bootet sie wie gehabt.

mit der option -V

 `\lpctool-cygwin>lpctool -d /dev/com4
-i -v -e -a -V boop_rom.bin

lpctool V0.9

This Software is free Software under GNU GPL 3 or later
(c) 2007 Ch. Klippel

Info : erasing flash #0 before write
Info : closing file descriptor
Info : closing serial device /dev/com4

...Ende...`

Liegt es an meinem 'Interface' oder an lpctool-cygwin?

*Last Edit : 29. Mär 2008, 18:30 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg833#msg833)

---

<a id="msg834"></a>

## 24. eme · 25. Mär 2008, 01:02

ich glaube, es liegt daran, dass der rechner nix empfangen kann. der ft232rl ist im ssop, da ist wohl bei einer korrektur eben was schiefgegangen...so, jetzt vorerst letzter versuch für heute..

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg834#msg834)

---

<a id="msg835"></a>

## 25. eme · 25. Mär 2008, 01:13

so jetzt kann ich auch empfangen, aber mittlerweile sagt die betty nix mehr. lpctool-cygwin bleibt an derselben stelle hängen.

auf

> **Zitat**
>
> Info : initiating auto-baud
> Info : awaiting autobaud response
> Info : got response, answering

ist dann aber wohl nicht verlass! :-)

gute nacht

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg835#msg835)

---

<a id="msg836"></a>

## 26. eme · 25. Mär 2008, 10:22

Jetzt habe ich gerade im Wiki einen Hinweis zu Problemen mit lpctool entdeckt:
[http://bettyhacks.com/wiki/index.php/LPCTool#Lpctool-Probleme](../../pages/LPCTool.md#lpctool-probleme)

" .. Da "tcsetattr" beim Baud-Wechsel (38.400->115.200) den reset-Pin toggelt. (Linux, CentOS 5, USB-Seriell-Kabel, Windows mit FT232R).."

Das kann ich auf dem Oszi sehen (jetzt sieht auch das Timing der Sequenz einwandfrei aus).

Hat jemand zufällig ein auf 38.400 baud gebremstes lpctool-cygwin für mich?

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg836#msg836)

---

<a id="msg838"></a>

## 27. eme · 25. Mär 2008, 14:04

So, mit Ubuntu 7.04 geht's:

Boop runterladen:
[http://svn.mamalala.org/filedetails.php?repname=boop&path=%2Ftrunk%2Fboop_rom.bin&rev=0&sc=0](https://web.archive.org/web/2012/http://svn.mamalala.org/filedetails.php?repname=boop&path=%2Ftrunk%2Fboop_rom.bin&rev=0&sc=0)

lpctool .deb installieren:
[http://www.grautier.com/grautier/index.php?/plugin/dlfile_108](https://web.archive.org/web/2012/http://www.grautier.com/grautier/index.php?/plugin/dlfile_108)

lpctool -d /dev/ttyUSB0 -i -v -e -a boop_rom.bin

Getestet mit ft232RL (USB).

Leider konnte ich lpctool nicht kompilieren, auch nach Installation von [http://opensrc.sec.samsung.com/download/arm-uclinux-tools-base-gcc3.4.0-20040713.sh](https://web.archive.org/web/2012/http://opensrc.sec.samsung.com/download/arm-uclinux-tools-base-gcc3.4.0-20040713.sh) und Anpassen des Makefiles war ein arm Befehl unbekannt.
Wenn ich bei Gelegenheit mal mit Boop rumspielen kann, werde ich da nochmal nachhaken und Infos posten.

Dann hat lpctool-cygwin oder der fdtdi-treiber ne Macke.

Ich hoffe, ich kann euch Entwicklern in Zukunft auch was beisteuern.

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg838#msg838)

---

<a id="msg842"></a>

## 28. pcsquirrel · 25. Mär 2008, 19:34

Hallo,

ich hab ein lpctool-cygwin ohne baudrate wechsel für dich. Hab´s angehängt - Ich hoffe die Forenregeln erlauben es.

Was noch zu beachten ist: Der Original Flashadapter für die RS232 invertiert die Signale DTR und RTS. Ich nehme an, du hast diese Signale beim FT232R direkt an die Betty gelegt. Ich glaub, daß da auch dein Problem liegt.
Man sollte diese Signale mit dem MProg von FTDI invertieren. Das funktioniert bei mir aber nicht.
Darum hab ich diese Invertierung beim LPCTool rausgenommen.

Du kannst es also verwenden, wenn du RTS und DTR direkt angeschloßen hast.

pcs

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg842#msg842)

---

<a id="msg843"></a>

## 29. eme · 25. Mär 2008, 19:44

Vielen Dank, ich werde das mal bei Gelegenheit ausprobieren.

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg843#msg843)

---

<a id="msg889"></a>

## 30. eme · 29. Mär 2008, 18:11

Funktioniert leider nicht, mit und ohne (scheinbar) invertierte Pegel. Die Hintergrundbeleuchtung der Betty blitzt kurz auf. Ich habe aber nicht die Signale / Pegel nachgemessen.

\lpctool-cygwin>lpctool -d /dev
/com4 -i -v -e -a boop_rom.bin

lpctool V0.9

This Software is free Software under GNU GPL 3 or later
(c) 2007 Ch. Klippel

Info : erasing flash #0 before write
Info : using flash #0 image boop_rom.bin
Info : opening serial device /dev/com4
Info : reset into bootmode
Info : opening bootloader
Info : initiating auto-baud
Info : awaiting autobaud response

*Last Edit : 29. Mär 2008, 18:29 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg889#msg889)

---

<a id="msg921"></a>

## 31. MrFX · 01. Apr 2008, 11:55

Moin!

Kann man das lpctool auch so nutzen, daß man den BL und Reset mit Jumper steuert? So wie bei Betty Heaven?

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg921#msg921)

---

<a id="msg1071"></a>

## 32. Ronin · 10. Jul 2008, 14:05

Also, bei mir funktioniert das lpctool unter Windows genauso wenig wie bei eme.

[Permalink](http://bettyhacks.com/forum/index.php?topic=54.msg1071#msg1071)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
