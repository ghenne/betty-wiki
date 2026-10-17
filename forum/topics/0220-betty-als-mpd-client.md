---
title: "Betty als MPD client"
topic_id: 220
board: "Software"
board_id: 6
posts: 132
first_post: "13. Oktober 2009, 03:36"
last_post: "24. Nov 2011, 20:31"
authors: ["Fux", "MrFX", "Telekatz", "antonia", "asgard", "frode", "gerdigerdi", "glotzi", "gunnar", "ino", "jannis", "phaidros", "stevie101", "t0bit0bsen"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=220.0"
---

# Betty als MPD client

[← Software](../boards/06-software.md) · Thema 220 · 132 Beiträge · 13. Oktober 2009, 03:36 – 24. Nov 2011, 20:31

Beteiligt: Fux, MrFX, Telekatz, antonia, asgard, frode, gerdigerdi, glotzi …

---

<a id="msg1488"></a>

## 1. phaidros · 13. Oktober 2009, 03:36

Ich habe auf meiner Homepage eine neue Firmware für Betty abgelegt, mit der man Betty als Client für den Musik-Server MPD nutzen kann.
Betty zeigt einem den gerade gespielten Titel samt Interpreten. Man kann mit Betty den MPD bedienen, also laut/leise, Titel vor/zurück, Pause, Play, Stop,
10 Sekunden vor/zurück, Mute.
Außerdem kann man sich die aktuelle Playliste anzeigen lassen und einen Titel daraus aussuchen.
Ebenso funktioniert die Auswahl der Playliste selber aus allen MPD verfügbaren Playlisten.

Die Installation ist etwas kompliziert, da man sowohl Betty als auch den Scart-Adapter flashen muss und noch ein Zusatzprogramm auf dem MPD-Server (oder einem anderen Rechner mit TCP/IP Verbindung zum MPD) installieren muss.
Läuft bei mir aber schon ganz gut.

Link zur Homepage mit Download-Möglichkeit:
[http://www.ewetel.net/~horst.raap](https://web.archive.org/web/2012/http://www.ewetel.net/~horst.raap)

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1488#msg1488)

---

<a id="msg1489"></a>

## 2. asgard · 13. Oktober 2009, 06:58

Hey,
sieht super aus,...schöner Anwendungszweck.
Ich setz das mal als Sticky!

Viele Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1489#msg1489)

---

<a id="msg1490"></a>

## 3. MrFX · 13. Oktober 2009, 07:47

Moin!

Sehr schön... wollte da auch schon mal was in die Richtung machen, kam aber aus Zeitmangel nie dazu.

Ist die betty_scart.bin gegenüber der letzten Version von Telekatz verändert? Weil ich die schon drauf habe.

MfG
MrFX

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1490#msg1490)

---

<a id="msg1491"></a>

## 4. phaidros · 13. Oktober 2009, 13:07

Ja, die betty_scart.bin ist verändert. Sie nimmt jetzt Befehle von der Betty über Funk auf und sendet sie über die serielle Schnittstelle an den dranhängenden Rechner weiter. Dann wartet sie auf Antwort und sendet diese zurück zur Betty. Muss also leider definitiv neu geflasht werden.

*« Letzte Änderung: 13. Oktober 2009, 18:49 von phaidros »*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1491#msg1491)

---

<a id="msg1492"></a>

## 5. Telekatz · 14. Oktober 2009, 10:51

Mahlzeit,

hab mir mal den Sourcecode angeschaut. Sieht irgendwie nicht so aus, dass man das in Boop einfach integrieren kann. Wie viel vom Boop Sourcecode steckt da eigentlich noch drin?

Trotzdem gute Arbeit.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1492#msg1492)

---

<a id="msg1493"></a>

## 6. phaidros · 14. Oktober 2009, 12:26

Ebenfalls Mahlzeit,

also das Ganze hat mal als Boop angefangen mit einer Schicht drauf zum Handling der Kommunikation mit dem MPD Server. Dann hab' ich Boop ein bißchen umstrukturiert, um besseres Echtzeitverhalten hinzukiregen. Viele Teile von Boop sind auch momentan noch draußen, da der Client sie nicht nutzt. Wirklich übrig von Boop sind nur noch ein paar hardwarenahe Sachen. War ja auch nicht das Ziel, Boop Konkurrenz zu machen. Soll einfach als eigenständiges Programm dienen.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1493#msg1493)

---

<a id="msg1704"></a>

## 7. stevie101 · 27. Okt 2010, 21:49

Edit: Hab's gerade so probiert, LED ist jetzt aus, leider nach wie vor kein Com.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1704#msg1704)

---

<a id="msg1705"></a>

## 8. jannis · 30. Okt 2010, 19:39

Kannst ja mal ohne das mpdtool horchen ob ueberhaupt etwas bei tx raus kommt. Beim einschalten wird immer kurz was gesendet.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1705#msg1705)

---

<a id="msg1706"></a>

## 9. t0bit0bsen · 02. Nov 2010, 15:28

Hallo zusammen,

ich habe seit einigen Tagen mpd auf der Seagate Dockstar mit eine USB Soundkarte laufen. Das funktioniert soweit auch super. Wenn jetzt noch die Betty wollen würde...

Das Flashen der Betty hat schon geklappt. Ich habe das Boop Image aus dem SVN gebaut und in die scart_image_data.h den Hex-Code der betty_scart.bin einkopiert. Leider bricht das Flashen des Scart-Adapters immer mit Fehler 8F ab. Was auch immer das sein mag...

Gibt es jemanden, der den Scart-Adapter über die Betty erfolgreich programmiert hat? Wenn ja, dann wäre es schön, wenn derjenige sein Image uppen könnte.

Viele Grüße

Tobi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1706#msg1706)

---

<a id="msg1707"></a>

## 10. jannis · 03. Nov 2010, 01:19

Ich hoffe das ist die richtige. Bei mir klappts ganz gut eigentlich.
Manchmal entstehen bei der Uebertragung grosse Verzoegerungen. Batterien kurz raus und wieder rein hilft dann manchmal...

[http://ul.to/q1zz8m](https://web.archive.org/web/2012/http://ul.to/q1zz8m)

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1707#msg1707)

---

<a id="msg1708"></a>

## 11. t0bit0bsen · 03. Nov 2010, 09:50

Hi,

danke für die schnelle Antwort. Ich habe es nun doch selbst hin bekommen, Python für Windows installiert und mit dem Skript die scart_image_data.h Datei erstellt, neu kompiliert  und dann lief es. Ich habe das Image als zip angehängt.

Die Betty funktioniert. Auch wenn das Display sich manchmal aufhängt, wenn ich von einer recht langen Playlist zurück auf den Wiedergabeschirm wechsle.

Sind eigentlich noch Erweiterungen geplant, um auf das Musikarchiv ohne Playlisten zuzugreifen?

Gibt es irgendwo eine Tastenbelegung?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1708#msg1708)

---

<a id="msg1709"></a>

## 12. gerdigerdi · 03. Nov 2010, 20:53

Hi,

Ich habe versucht MCbetty um einige Kleinigkeiten zu erweitern.
Seitenweises Scrollen in der Playlist und Anzeige von Dateinamen falls das Lied keinen Tilel hat.

Leider zählt die Playtime nun nicht mehr hoch wobei ich da nichts geändert habe.
Wäre schön wenn sich das mal einer anschauen würde der Ahnung hat. Achtung bad code!
Mir scheint auch das die betty "etwas" wenig Ram hat. Erhöhen vom "Playlist Buffers" hat interessante Ergebnisse geliefert ;/

Gibt es ein svn, phaidros?

*Last Edit : 04. Nov 2010, 17:00 by gerdigerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1709#msg1709)

---

<a id="msg1710"></a>

## 13. Fux · 08. Nov 2010, 14:46

Wenn ich McBetty-0.7.tar.bz2 runterlade bekomme ich immer eine Fehlermeldung:
`bzip2: (stdin) is not a bzip2 file.`
Kann das bitte mal jemand gegenprüfen, bzw. die Datei irgendwo neu raufladen. Danke!

@t0bit0bsen:
Deine Firmware-Datei "boop_rom_mitMCBetty_scart_python.bin" wird in die Betty Fernbedienung geladen und dann damit der Scart-Adapter geflasht. Anschließend lade ich dann die McBetty Firmware in die Betty Fernbedienung. Ist das richtig so?

Noch zwei allgemeine Fragen:
Wie schnell geht denn der Verbindungsaufbau bei McBetty, bzw. wie flüssig läuft das ganze (bei überschaubarer Playlist <= 100 Titel)?
Reicht für die Verbindung von Scart-Adapter zu PC ein USB-Handykabel aus, wie unter [http://bettyhacks.com/wiki/index.php/Interfaces_PC_zu_Betty](../../pages/Interfaces%20PC%20zu%20Betty.md) beschrieben?

Grüße
Fux

*Last Edit : 08. Nov 2010, 14:52 by Fux*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1710#msg1710)

---

<a id="msg1711"></a>

## 14. t0bit0bsen · 08. Nov 2010, 16:26

> **Zitat**
>
> @t0bit0bsen:
> Deine Firmware-Datei "boop_rom_mitMCBetty_scart_python.bin" wird in die Betty Fernbedienung geladen und dann damit der Scart-Adapter geflasht. Anschließend lade ich dann die McBetty Firmware in die Betty Fernbedienung. Ist das richtig so?

Ja. Genau.

> **Zitat**
>
> Reicht für die Verbindung von Scart-Adapter zu PC ein USB-Handykabel aus

Ja. Ich habe eins aus der Bucht fürs Siemens C45. Damit habe ich programmiert und nun ist es zwischen Scart-Adapter und PC.

Die Übertragungsgeschwindigkeit ist in Ordnung. Allerdings ist das Handling z.B. übers Smartphone (Android) schon um Klassen besser. Die Betty ist nur "Backup", um mal schnell Musik machen zu können, ohne Rechner oder Handy zu bemühen.

Grüße

Tobi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1711#msg1711)

---

<a id="msg1712"></a>

## 15. Fux · 08. Nov 2010, 18:26

> **Zitat**
>
> Die Übertragungsgeschwindigkeit ist in Ordnung. Allerdings ist das Handling z.B. übers Smartphone (Android) schon um Klassen besser. Die Betty ist nur "Backup", um mal schnell Musik machen zu können, ohne Rechner oder Handy zu bemühen.

Hört sich gut an, d.h. man muß nicht ewig auf irgendeine Verbindung warten, sondern Betty an und los gehts?
Für die Couch hab ich auch einen alten ipod Touch, die Betty ist fürs Bad gedacht. Da ist es nicht so schlimm, wenn die mal untertaucht ;-). Für den Sound hab ich einen USB FM-Transmitter, kann ich sehr empfehlen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1712#msg1712)

---

<a id="msg1713"></a>

## 16. phaidros · 09. Nov 2010, 02:44

Hallo,
habe leider länger nicht hier reingeschaut.
Im Moment liegt das Projekt bei mir etwas auf Eis. Das heißt in diesem Jahr wird es von mir wohl keine neue Version geben.
SVN habe ich auch nicht. Also selbst verbessern und irgendwo hosten oder warten bis ich wieder dazu komme, wohl Anfang nächsten Jahres.

Gruß Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1713#msg1713)

---

<a id="msg1718"></a>

## 17. frode · 14. Nov 2010, 03:39

> **Zitat von: jannis am 03. Nov 2010, 01:19**
>
> Ich hoffe das ist die richtige. Bei mir klappts ganz gut eigentlich.
> Manchmal entstehen bei der Uebertragung grosse Verzoegerungen. Batterien kurz raus und wieder rein hilft dann manchmal...
>
> [http://ul.to/q1zz8m](https://web.archive.org/web/2012/http://ul.to/q1zz8m)

Weiß vielleicht jemand, ob das das richtige Image ist?
Ich habe es geflasht, rx,tx,gnd angeschlossen, bekomme aber ein timeout (und das Messgerät sag auch nichts außergewöhnliches).
Wollte also nur wissen, ob das Image passt um die Fehlerquellen eingrenzen zu können.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1718#msg1718)

---

<a id="msg1719"></a>

## 18. jannis · 14. Nov 2010, 14:41

Timeout an sich ist nicht umbedingt falsch. Horch doch einfach mal mit einem Terminal Programm ob etwas beim einschalten des Scartsteckers gesendet wird.
Auch wenn alles klappt kommen immer noch regelmaessig timeouts solange man auf der betty nichts eingibt...

Wenns wirklich nicht klappt werd ich einfach noch mal mein eigenes image testen. Aber eigentlich sollte es funzen...

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1719#msg1719)

---

<a id="msg1722"></a>

## 19. jannis · 17. Nov 2010, 01:24

Ich komm grad gar nicht klar mit dem code...

In der cc1100.c steht: "GDO0 from cc1100 is connected with P0.6 from 89LPC31 !"

Im Datenblatt steht P0.6 ist an Pin 20. Aber mit der Lupe sehe ich am Pin20 ueberhaupt nix angeschlossen!
Wie kann das sein?
Hab ich ein falsches Datenblatt? (oben steht P89LPC930/931)

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1722#msg1722)

---

<a id="msg1724"></a>

## 20. Telekatz · 17. Nov 2010, 11:37

Nimm statt der Lupe ein Röntgengerät, dann siehst du vielleicht, dass der Pin unter dem 89LPC31 angeschlossen ist.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1724#msg1724)

---

<a id="msg1726"></a>

## 21. jannis · 17. Nov 2010, 16:41

Haha, hier mal ein Roentgenfoto fuer alle andern Nichtsnutze wie mich.
Seh ich das richtig, dass die LED an pin 3 anliegt? Ich will diesen Ausgang fuer was anderes verwenden.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1726#msg1726)

---

<a id="msg1727"></a>

## 22. Fux · 20. Nov 2010, 00:27

Wenn ich die mcbetty.bin auf die Betty flashe geht nur die Hintergrundbeleuchtung an, ansonsten passiert gar nichts. Kennt jemand diesen Effekt?
Die Boop-Firmware funktioniert im Gegensatz einwandfrei.
EDIT: Hab zwei Fernbedienungen, bei der zweiten läuft McBetty jetzt. Die erste hat jedoch immer noch obiges Phänomen.

Wenn ich woanders als auf der Betty z.B. einen anderen Titel aktualisiere, dann wird die Betty leider nicht aktualisiert. Ist das ein Bug oder fehlt dieses Feature noch?
Title-Skip funktioniert sehr gut, jedoch lassen sich die Playlisten nur hin und wieder auswählen, meistens passiert einfach keine Reaktion, ist das jemanden bekannt?

Gruß
Fux

*Last Edit : 20. Nov 2010, 02:21 by Fux*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1727#msg1727)

---

<a id="msg1728"></a>

## 23. jannis · 22. Nov 2010, 01:41

Dass das Ding n par Bugs hat seh ich auch so. Bei mir funzt es immer wieder nach ein par resets. Aber frag mich nicht warum...

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1728#msg1728)

---

<a id="msg1729"></a>

## 24. gerdigerdi · 24. Nov 2010, 20:12

So meine Betty ist im Wirkbetrieb
Meine Frau ist happy .. endlich keinen TV mehr anschalten um die Titel auszuwählen.

Auch wenn die Version etwas buggy ist (keinen Plan ob es an meinen Änderungen liegt (siehe oben) langt bei mir für einen schnellen Reset ein leichtes "Aufdotzen" mit der Unterkante auf den Tisch. Ob das aufgrund der Akkuaufnahme so gewollt ist ?

Hoffe ich finde mal wieder Zeit an dem klasse Projekt mit zu helfen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1729#msg1729)

---

<a id="msg1737"></a>

## 25. phaidros · 17. Dez 2010, 02:34

Es gibt eine neue Version von McBetty auf [http://www.ewetel.net/~horst.raap](https://web.archive.org/web/2012/http://www.ewetel.net/~horst.raap)

Version 0.8.1. enthält hauptsächlich Bugfixes.

Außerdem ist jetzt Random, Repat und Single Mode (siehe MPD) möglich.

Enjoy the music!

Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1737#msg1737)

---

<a id="msg1738"></a>

## 26. Fux · 21. Dez 2010, 00:38

Wow, danke für das vorweihnachtliche Geschenk 

Muss alles aktualisiert werden, auch das Scart-Interface? Könnte jemand ggf. wieder ein "boop_rom_mitMCBetty" Image hochladen.

Danke!

Gruß
Fux

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1738#msg1738)

---

<a id="msg1739"></a>

## 27. phaidros · 21. Dez 2010, 00:54

Ja, leider muss alles aktualisiert werden.

Wenn bereits einmal die McBetty Firmware auf den Scart Adapter geflasht wurde, lässt er sich
(vielleicht) über die serielle Schnittstelle flashen. Im README von scart_image steht was dazu.
Geht meistens. Wenn man den Scart Adapter einmal power-cycelt sogar eigentlich immer.
Ich empfehle die aktuelle Version aus dem git-hub, da ist noch eine kleine Verbesserung gegenüber
Version 0.8.1 drin.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1739#msg1739)

---

<a id="msg1740"></a>

## 28. Fux · 22. Dez 2010, 21:29

Bei mir lässt sich das Scart-Interface leider nicht direkt mit dem flashtool flashen (McBetty 0.7 ist aktuell drauf).
Version ist die aktuelle aus dem Git.
`:/usr/src/mpd/mcbetty/git/McBetty/scart_image$ ./flashtool /dev/ttyUSB0
Sending break
Read 0 characters:

Read 0 characters:

buffer[0] = 00
Error: Could not negotiate baud rate!`

Es kommt eine Fehlermeldung beim kompilieren, vielleicht liegt es daran?
`:/usr/src/mpd/mcbetty/git/McBetty/scart_image$ make
gcc bin2c.c -o bin2c
gcc makebin.c -o makebin
/usr/bin/sdcc --iram-size 0x100 --model-small --code-size 8192 -I/include -c main.c
/usr/bin/sdcc --iram-size 0x100 --model-small --code-size 8192 -I/include -c serial.c
/usr/bin/sdcc --iram-size 0x100 --model-small --code-size 8192 -I/include -c cc1100.c
cc1100.c:53:1: warning: "SMARTRF_SETTING_PKTCTRL1" redefined
In file included from cc1100.c:21:
smartrf_CC1100.h:73:1: warning: this is the location of the previous definition
cc1100.c:54:1: warning: "SMARTRF_SETTING_IOCFG0D" redefined
smartrf_CC1100.h:72:1: warning: this is the location of the previous definition
cc1100.c:55:1: warning: "SMARTRF_SETTING_IOCFG2" redefined
smartrf_CC1100.h:71:1: warning: this is the location of the previous definition
cc1100.c:56:1: warning: "SMARTRF_SETTING_FIFOTHR" redefined
smartrf_CC1100.h:70:1: warning: this is the location of the previous definition
/usr/bin/sdcc --iram-size 0x100 --model-small --code-size 8192 -I/include main.rel  serial.rel cc1100.rel  -o betty_scart.ihx
./makebin -s 7680 <betty_scart.ihx >betty_scart.bin
./bin2c scart_image 7680 <betty_scart.bin >scart_image.h
gcc flashtool.c -o flashtool
asx8051 -losg isp.asm
/usr/bin/sdcc --iram-size 0x100 --model-small --code-size 8192 -I/include main.rel  serial.rel cc1100.rel isp.rel -o betty_scart_boot.ihx
./makebin -s 8192  <betty_scart_boot.ihx >betty_scart_boot.bin
./bin2c scart_image 8192 <betty_scart_boot.bin >scart_image_boot.h
cp scart_image_boot.h boop.orig/tools/scart_image.h
cd boop.orig && make clean && make
make[1]: Betrete Verzeichnis '/usr/src/mpd/mcbetty/git/McBetty/scart_image/boop.orig'
rm -Rf .deps adc/.deps audio/.deps cc1100/.deps display/.deps flash/.deps games/.deps gui/.deps infrared/.deps interrupt/.deps keyboard/.deps rtc/.deps serial/.deps timer/.deps tools/.deps
rm -f crt.o main.o global.o audio/soundirq.o infrared/infraredirq.o interrupt/irq.o keyboard/keyirq.o timer/timerirq.o adc/adc.thumb.o adc/adcirq.thumb.o audio/sound.thumb.o audio/sid.thumb.o cc1100/cc1100.thumb.o cc1100/rf.thumb.o display/lcd.thumb.o display/fonty.thumb.o display/backlight.thumb.o flash/flash.thumb.o flash/bfs.thumb.o games/gamesmenu.thumb.o games/tic_tac_toe.thumb.o games/sokoban.thumb.o games/connect4.thumb.o gui/menu.thumb.o gui/mainmenu.thumb.o gui/testmenu.thumb.o gui/settingsmenu.thumb.o gui/controls.thumb.o infrared/infrared.thumb.o infrared/codes.thumb.o infrared/encoders.thumb.o infrared/ir_capture.thumb.o infrared/ir_selector.thumb.o keyboard/keyboard.thumb.o rtc/rtc.thumb.o rtc/i2c.thumb.o serial/serial.thumb.o timer/timerfuncs.thumb.o tools/toolsmenu.thumb.o tools/scart_icp.thumb.o infrared/ir_itt.thumbunopt.o infrared/ir_nrc17.thumbunopt.o infrared/ir_raw.thumbunopt.o infrared/ir_rc5.thumbunopt.o infrared/ir_rc6.thumbunopt.o infrared/ir_rca.thumbunopt.o infrared/ir_rcmm.thumbunopt.o infrared/ir_rec80.thumbunopt.o infrared/ir_recs80.thumbunopt.o infrared/ir_rf.thumbunopt.o infrared/ir_sirc.thumbunopt.o infrared/ir_spaceenc.thumbunopt.o *.elf *.bin *.hex *~
make[1]: Verlasse Verzeichnis '/usr/src/mpd/mcbetty/git/McBetty/scart_image/boop.orig'
make[1]: Betrete Verzeichnis '/usr/src/mpd/mcbetty/git/McBetty/scart_image/boop.orig'
mkdir -p .deps
mkdir -p adc/.deps
mkdir -p audio/.deps
mkdir -p cc1100/.deps
mkdir -p display/.deps
mkdir -p flash/.deps
mkdir -p games/.deps
mkdir -p gui/.deps
mkdir -p infrared/.deps
mkdir -p interrupt/.deps
mkdir -p keyboard/.deps
mkdir -p rtc/.deps
mkdir -p serial/.deps
mkdir -p timer/.deps
mkdir -p tools/.deps
/home/raap/CodeSourcery/Sourcery_G++_Lite/bin/arm-uclinuxeabi-as -mcpu=arm7tdmi-s -D --gstabs -mthumb-interwork -mfpu=softfpa -o crt.o crt.s
make[1]: /home/raap/CodeSourcery/Sourcery_G++_Lite/bin/arm-uclinuxeabi-as: Kommando nicht gefunden
make[1]: *** [crt.o] Fehler 127
make[1]: Verlasse Verzeichnis '/usr/src/mpd/mcbetty/git/McBetty/scart_image/boop.orig'
make: *** [betty_flasher] Fehler 2`

EDIT:
Ich habe zwei Betty Fernbedienungen. Das Flashen hatte bei einer mit der Version 0.7 partout trotz mehrmaliger Versuche nicht geklappt. Konnte eben beide auf die git-Version der McBetty flashen. Nur als positive Rückmeldung :-).
Flashen des Scart-Interfaces klappt weiterhin nicht.

Gruß
Fux

*Last Edit : 22. Dez 2010, 22:05 by Fux*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1740#msg1740)

---

<a id="msg1741"></a>

## 29. phaidros · 23. Dez 2010, 00:48

> **Zitat**
>
> make[1]: /home/raap/CodeSourcery/Sourcery_G++_Lite/bin/arm-uclinuxeabi-as: Kommando nicht gefunden

Oh, da habe ich meinen Pfad zu der CodeSourcery Toolchain im Makefile.
Das müsstest du ändern.

Also wenn das Flashen mit dem flashtool nicht geht:
(passiert bei mir auch manchmal, obwohl ein-und wieder ausstöpseln des Netzsteckers vom Scart-Adapter und dann nochmal flashstool probieren bei mit immer geht)
Bitte auch checken, ob /dev/ttyUSB0 das richtige Device ist, an dem der Scart Adapter hängt!
 
Unter scart_image/boop.orig sollte eine Datei boop_rom.bin liegen, Diese auf die Betty flashen, dann kann mithilfe der Betty der  Scart-Adapter geflasht werden.
Wenn man die Datei selber erzeugen will:
cd scart_image
make betty_flasher

Die Pfade zu den Tools (Codesourcery und sdcc) müssen in den Makefiles angepasst werden wenn man selbst kompiliert.

Ich hoffe es klappt.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1741#msg1741)

---

<a id="msg1742"></a>

## 30. gerdigerdi · 23. Dez 2010, 16:26

Wenn ich das richtig verstanden habe, sollte flashen des scart_adapters per seriell mit dem flashtool funktionieren, wenn bereits eine MCBetty-scart-version geflasht war. Langt da die 7.X?

Muss neben rx/tx/gnd/vcc noch etwas anderes angeschlossen sein zum seriellen flashen? So wie es aussieht ignoriert mein scart adapter (mit bettyscart 7.X) den BREAK. (es kommt weiterhin "Status" von der betty rein.)

Compilieren hat fast perfekt geklappt. nur u_int16_t ist bei meiner toolchain nicht defined.

Werde die tage dann wohl den scart wieder per betty flashen. Würde mich nur interessieren wiso das bei mir (uns) nicht klappt. (Ich benutze einen cp210x converter).

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1742#msg1742)

---

<a id="msg1743"></a>

## 31. phaidros · 23. Dez 2010, 23:13

> **Zitat**
>
> Langt da die 7.X?

Weiß ich leider auch nicht mehr so genau. Da gab es zwei Versionen der Scart-Adapter Firmware. Eine mit Bootloader, eine ohne.
Außerdem musste noch was an den Config-Bytes geflasht werden, was bisher nur Betty(Boop) konnte. Jetzt kann das aber auch Flashtool.

> **Zitat**
>
> Muss neben rx/tx/gnd/vcc noch etwas anderes angeschlossen sein zum seriellen flashen?

Definitiv nein.

> **Zitat**
>
> Ich benutze einen cp210x converter.

Vielleicht kann der kein BREAK senden? Ich habe den Scart-Adapter an einem echten seriellen Anschluss dran.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1743#msg1743)

---

<a id="msg1744"></a>

## 32. gerdigerdi · 24. Dez 2010, 10:06

Wird sich ja klären wenn die neue scart-version geflashed ist.

Hab erstmal die neue Version auf die Betty geflashed. Sieht wirklich gut aus:
- Seitenweises Blättern (hast du wirklich eleganter implementiert als ich)
in Play- und Tracklist! genial!
- Random mode usw. durchaus funktional

ABER wiso aktualisiert die Betty die Lautstärke auch wenn sie nicht geändert wurde? (bzw. von ausserhalb geändert wurde).
Das ist ein fatales Problem für mich. Ich pausiere die Wiedergabe immer nur und switche dann zum TV-modus. Wenn ich da nun die Lautstärke ändere wird sie nach kurzer Zeit wieder zurückgesetzt. Betty sollte die von aussen gesetzte Lautstärke eher übernehmen, oder?

Schön das wieder Leben in das Projekt kommt

MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1744#msg1744)

---

<a id="msg1745"></a>

## 33. jannis · 24. Dez 2010, 14:15

Betty geht immer davon aus, dass sie alleiniger Client ist. Den Lautstaerkepegel speichert sie auf der Fernbedienung ab, und der wird dann spaeter erneut so von mpd angefordert. Nur wundere ich mich, dass betty ueberhaupt eine Lautstaerkeanfrage macht ohne dass man die Tasten dafuer drueckt. Hatte ich anders verstanden als ich damals den code lass.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1745#msg1745)

---

<a id="msg1746"></a>

## 34. Fux · 24. Dez 2010, 21:03

> **Zitat von: phaidros am 23. Dez 2010, 00:48**
>
> Die Pfade zu den Tools (Codesourcery und sdcc) müssen in den Makefiles angepasst werden wenn man selbst kompiliert.

Ok, ich hab mir der einfachheit halber auch einen /home/raap Ordner erstellt und dorthin die Codesourcery installiert.
Make läuft eine Weile und bringt dann einen Fehler, mit dem ich leider nichts anfangen kann:
`/home/raap/CodeSourcery/Sourcery_G++_Lite/bin/arm-uclinuxeabi-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float -I/home/raap/CodeSourcery/Sourcery_G++_Lite/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinfrared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm -Impd -O2 -c  -MMD -MF serial/.deps/serial.o -o serial/serial.o serial/serial.c
/home/raap/CodeSourcery/Sourcery_G++_Lite/bin/arm-uclinuxeabi-ld -Tlpc2220_rom.ld -Map boop.map -L/home/raap/CodeSourcery/Sourcery_G++_Lite/lib/gcc/arm-uclinuxeabi/4.3.2 -o muc_rom.elf crt.o isr.o arm_exc.o global.o main.o cc1100/cc1100.o cc1100/rf.o display/lcd.o display/fonty.o display/window.o display/screen.o display/screen_playing.o display/screen_tracklist.o display/screen_playlist.o display/screen_info.o interrupt/irq.o pwm/pwmirq.o keyboard/keyboard.o kernel/kernel.o timer/timerirq.o mpd/model.o mpd/mpd.o serial/serial.o -lgcc
/home/raap/CodeSourcery/Sourcery_G++_Lite/bin/arm-uclinuxeabi-ld.real: cannot find -lgcc
make: *** [muc_rom.elf] Fehler 1`EDIT: Habs jetzt über folgenden Workaround in den Griff bekommen:

- libgcc.a aus dem CodeSourcery lib Verzeichnis (CodeSourcery/Sourcery_G++_Lite/lib/gcc/arm-uclinuxeabi/4.5.1) in das muc Source-Verzeichnis kopieren (McBetty/muc)

- statt dem angehängten -lgcc ein "libgcc.a" anhängen

Da ich viele Alben höre, habe ich mir ein Bash-Skript geschrieben, welches in der Playliste zum ersten Titel des aktuellen bzw. vorherigen Album springt (siehe [http://mpd.wikia.com/wiki/Hack:mpdNextAlbum).](https://web.archive.org/web/2012/http://mpd.wikia.com/wiki/Hack:mpdNextAlbum).)
D.h ich möchte mit dem "PROG+/PROG-" Button auf der Fernbedienung dieses Skript aufrufen. Kannst Du mir grob sagen, an welchen Stellen (Button-Abfrage der FB und wo Aufruf des Skripts im mpdtool) ich im Code dies mir einbauen kann? Bzw. muß ich dem mpdtool hierzu einen bestimmten Befehl schicken? Ich kenn mich leider mit C nur rudimentär aus.

Danke!

EDIT: Noch eine andere Frage, auf der Betty Webseite ist auf den Screenshots der Playliste zu sehen: "100 Lastest Tracks" bzw. "500 Random Tracks", wie werden denn diese Tracks "erzeugt", ist das im Code enthalten oder extern per Skript?

Grüße
Fux

*Last Edit : 24. Dez 2010, 22:38 by Fux*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1746#msg1746)

---

<a id="msg1747"></a>

## 35. phaidros · 26. Dez 2010, 15:06

> **Zitat**
>
> Betty sollte die von aussen gesetzte Lautstärke eher übernehmen, oder?

Ja, ist in der neuesten Version auf git-hub geändert. Ich benutze tatsächlich Betty im Moment als einzigen Client.
Jetzt wird die Lautstärke nur auf Tastendruck von Betty geändert und ansonsten die extern eingestellte Lautstärke
akzeptiert.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1747#msg1747)

---

<a id="msg1748"></a>

## 36. phaidros · 26. Dez 2010, 15:15

> **Zitat**
>
> Da ich viele Alben höre, habe ich mir ein Bash-Skript geschrieben, welches in der Playliste zum ersten Titel des aktuellen bzw. vorherigen Album springt (siehe [http://mpd.wikia.com/wiki/Hack:mpdNextAlbum).](https://web.archive.org/web/2012/http://mpd.wikia.com/wiki/Hack:mpdNextAlbum).)
> D.h ich möchte mit dem "PROG+/PROG-" Button auf der Fernbedienung dieses Skript aufrufen. Kannst Du mir grob sagen, an welchen Stellen (Button-Abfrage der FB und wo Aufruf des Skripts im mpdtool) ich im Code dies mir einbauen kann? Bzw. muß ich dem mpdtool hierzu einen bestimmten Befehl schicken? Ich kenn mich leider mit C nur rudimentär aus.

In der neuesten Version auf git-hub ist das testweise drin. Wenn man im Playing-Screen (da wo Titel und Spieldauer und so angezeigt werden) auf "A" drückt, wird das Script
"script_1.sh" im aktuellen Verzeichnis von mpdtool aufgerufen. Taste "B" ruft "script_2.sh" auf. Ist aber noch nicht ausführlich geteste!

> **Zitat**
>
> Noch eine andere Frage, auf der Betty Webseite ist auf den Screenshots der Playliste zu sehen: "100 Lastest Tracks" bzw. "500 Random Tracks", wie werden denn diese Tracks "erzeugt", ist das im Code enthalten oder extern per Skript?

Extern per Script. So eine Funktion auf der Betty wäre noch schön, so etwas wie Smart-Playlists bei Amarok. Ist aber schwierig. Mal schauen.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1748#msg1748)

---

<a id="msg1749"></a>

## 37. Fux · 29. Dez 2010, 12:20

> **Zitat von: phaidros am 26. Dez 2010, 15:15**
>
> In der neuesten Version auf git-hub ist das testweise drin. Wenn man im Playing-Screen (da wo Titel und Spieldauer und so angezeigt werden) auf "A" drückt, wird das Script
> "script_1.sh" im aktuellen Verzeichnis von mpdtool aufgerufen. Taste "B" ruft "script_2.sh" auf. Ist aber noch nicht ausführlich geteste!

Wow, genial! Werde ich mir anschauen.

> **Zitat von: phaidros am 26. Dez 2010, 15:15**
>
> Extern per Script. So eine Funktion auf der Betty wäre noch schön, so etwas wie Smart-Playlists bei Amarok. Ist aber schwierig. Mal schauen.

Wie speichertst Du denn die letzten 100 Songs ab, mit mpdcron?

Ich habe gestern im MPD-Mantis eine ähnliche Anfrage zu Smart-Playlists reingestellt (-> [http://musicpd.org/mantis/view.php?id=3134).](https://web.archive.org/web/2012/http://musicpd.org/mantis/view.php?id=3134).) In der neuesten MPD git werden ja jetzt auch Audio CDs unterstützt. Ich finde nur das Handling mit den verschiedenen Soundquellen unpraktisch. Deshalb hab ich Playlists vorgeschlagen, die "Audio CD", "Streams", "Recordings" und "Default" enthalten und sich somit mit einem Klick aufrufen lassen sollten. Mal sehen was der Entwickler dazu meint. Wenn das noch jemand gut findet, bitte auch im Mantis eintragen.
Aktuell löse ich den Wechsel von Radio- auf Default-Playlist mit einem Umschaltskript, aber das funktioniert natürlich nur, wenn ich mit der Fernbedienung schalte und nicht mit einem GUI-Client. Wie löst Du denn das?

Grüße
Fux

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1749#msg1749)

---

<a id="msg1750"></a>

## 38. phaidros · 29. Dez 2010, 14:03

> **Zitat**
>
> Wie speichertst Du denn die letzten 100 Songs ab, mit mpdcron?

Das kenne ich noch gar nicht.

Eigentlich benutze ich Amarok (Verseion 1.4) als Musik-Verwalter. Ich erzeuge dann in Amarok die entsprechende Playlist neu und speichere sie in dem Playlisten-Verzeichnis von MPD ab.
Das ist alles noch ein ziemliches Gewurschtel. Ich verstehe auch das Konzept von MPD bezüglich Playlisten nicht wirklich. Warum haben Playlisten Versionsnummern, aber keinen numerischen Index, mit denen man sie aufrufen kann
Und muss ich wirklich für alles Playlisten haben? Ich will doch bestimmte Alben hören, meist sogar nur bestimmte Titel. Muss ich für jedes Album eine Playliste erstellen?

> **Zitat**
>
> Aktuell löse ich den Wechsel von Radio- auf Default-Playlist mit einem Umschaltskript, aber das funktioniert natürlich nur, wenn ich mit der Fernbedienung schalte und nicht mit einem GUI-Client. Wie löst Du denn das?

Oh, sowas kompliziertes mache ich gar nicht. Ich habe ein normales Radio, nix mit diesem bösen Internet :-)
OK, eigentlich hätte ich sowas auch gern, aber im Moment dienen  Betty und MPD nur dazu, mir im Wohnzimmer gelegentlich mal Musik über 'ne richtig gute Anlage anzuhören,
ohne dass ich da einen riesen Rechner mit Amarok drauf stehen haben muss und ohne den Fernseher einschalten zu müssen.

Meine MPD Version ist auch schon recht alt (0.12.1), muss ich dringend mal aktualisieren.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1750#msg1750)

---

<a id="msg1751"></a>

## 39. jannis · 29. Dez 2010, 14:53

Also ich benutze hier gmpc und ncmpc als clients fuer mpd. Besonders gmpc ist sehr einfach und intuitiv bedienbar.

mpd erlaubt allen clients ueber das Protokoll die Datenbank zu durchsuchen, entweder in der Folder-ansicht oder z.B. nach Artist, Album, Titel getrennt. Auch eine echte Suchfunktion ist vorhanden.
Ich fuege mit all diesem Hilfsmitteln Ordner, Alben und einzelne Titel der current playlist hinzu. Diese selbst speichere ich dann aber nur sehr selten ab.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1751#msg1751)

---

<a id="msg1752"></a>

## 40. phaidros · 29. Dez 2010, 16:07

> **Zitat**
>
> mpd erlaubt allen clients ueber das Protokoll die Datenbank zu durchsuchen, entweder in der Folder-ansicht oder z.B. nach Artist, Album, Titel getrennt. Auch eine echte Suchfunktion ist vorhanden.
> Ich fuege mit all diesem Hilfsmitteln Ordner, Alben und einzelne Titel der current playlist hinzu. Diese selbst speichere ich dann aber nur sehr selten ab.

Ok. Das klingt gut. Mal sehen ob eine elementare Suchfunktion in Betty machbar ist.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1752#msg1752)

---

<a id="msg1753"></a>

## 41. Fux · 29. Dez 2010, 20:00

> **Zitat von: jannis am 29. Dez 2010, 14:53**
>
> Also ich benutze hier gmpc und ncmpc als clients fuer mpd. Besonders gmpc ist sehr einfach und intuitiv bedienbar.

GMPC verwende ich auch. Wenn man MPD verwendet, kommt man da wohl kaum dran vorbei.
@phaidros: Schau Dir mal die aktuelle MPD/GMPC Version an, da hat sich einiges getan. Vielleicht gefällts Dir besser als Amarok.

> **Zitat**
>
> Das ist alles noch ein ziemliches Gewurschtel. Ich verstehe auch das Konzept von MPD bezüglich Playlisten nicht wirklich. Warum haben Playlisten Versionsnummern, aber keinen numerischen Index, mit denen man sie aufrufen kann

Geht einfacher als mit Index, Du kannst eine Playlist direkt mit ihren Namen aufrufen. Gegebenfalls kann man sich die vorhandenen Playlisten mit mpc anzeigen lassen.
`mpc load playlistname
mpc lsplaylists`

> **Zitat**
>
> Zitat
> Wie speichertst Du denn die letzten 100 Songs ab, mit mpdcron?
> Das kenne ich noch gar nicht.

Ist sehr praktisch, damit schalte ich zum Beispiel je nach MPD-Wiedergabe meine Stereo-Anlage vollautomatisch über eine Funksteckdose an und aus. Das geht über einen USB-Funkstick namens Tellstick, sehr zu empfehlen.

Das ist mein Umschalteskript zwischen Default-Playlist und Radio-Playlist. Es speichert sogar den zuletzt gespielten Titel (inkl. Abspielzeit) bzw. Stream. Aber wär halt viel eleganter, wenn das ganze in MPD integriert wäre.
`` #!/bin/bash

# FX, 2010-08-06
# Switch between radio (stream) and normal playing

# Requirements: A MPD-playlist called "Radio" with your radio streams
# Fit your $USER and make sure that $USER have respective rights at /home/$USER/.mpd/

# PARAMETER
USER=markus
TEMPMODE=/home/$USER/.mpd/tempMode
TEMPNR=/home/$USER/.mpd/tempNr
TEMPSTATE=/home/$USER/.mpd/tempState
TEMPTIME=/home/$USER/.mpd/tempTime
TEMPRADIONR=/home/$USER/.mpd/tempRadioNr
TEMPRADIOSTATE=/home/$USER/.mpd/tempRadioState

if [ ! -e "$TEMPMODE" ]; then
 echo "Mode nicht angelegt"
 echo "normal" > "$TEMPMODE"
fi

if [ "$1" == "$(cat "$TEMPMODE")" ]; then
 echo "Modus bereits aufgerufen"
 case "$1" in
  radio)
  # /usr/local/skripte/lircLcd.py -f "     RADIO" &
  ;;
  normal)
  # /usr/local/skripte/lircLcd.py -f "     MUSIK" &
  ;;
 esac
 exit
fi

echo "Übergabeparameter: $1"
case "$1" in
 radio)
  # Switch to radio playlist
  echo "Switch to radio"
  echo "radio" > "$TEMPMODE"
  ACTNR=$(mpc --format "%position%"  | head -n 1)
  echo "Active Nr: $ACTNR"
  echo $ACTNR > "$TEMPNR"
  # Status einlesen
  if [ `/usr/bin/mpc | wc -l` -gt "1" ]; then
   if [ `/usr/bin/mpc | grep playing | wc -l` -eq "1" ]; then
    echo "Status: play"
    echo play > "$TEMPSTATE"
   else
    echo "Status: pause"
    echo pause > "$TEMPSTATE"
   fi
   echo "$(/usr/bin/mpc | head -n 2 | tail -n 1 | cut -d' ' -f5 | cut -d'/' -f1)" > "$TEMPTIME"
  else
   echo "Status: stop"
   echo stop > "$TEMPSTATE"
  fi

  mpc rm temp
  mpc save temp
  mpc clear
  mpc load Radio
  if [ -e "$TEMPRADIONR" ]; then
   ACTNR=$(cat "$TEMPRADIONR")
   mpc play
   mpc play $ACTNR
  else
   mpc play
  fi
  ;;
 normal)
  # Switch back to normal playlist (saved as temp)
  echo "Switch to normal"
  #/usr/local/skripte/lircLcd.py -f "     MUSIK" &
  echo "normal" > "$TEMPMODE"
  ACTNR=$(mpc --format "%position%"  | head -n 1)
  echo "Radio Active Nr: $ACTNR"
  echo $ACTNR > "$TEMPRADIONR"

  # Status einlesen
  if [ `/usr/bin/mpc | wc -l` -gt "1" ]; then
   if [ `/usr/bin/mpc | grep playing | wc -l` -eq "1" ]; then
    echo "Radio State: play"
    echo play > "$TEMPRADIOSTATE"
   else
    echo "Radio State: pause"
    echo pause > "$TEMPRADIOSTATE"
   fi
  else
   echo "Radio State: stop"
   echo stop > "$TEMPRADIOSTATE"
  fi

  # Normal Playlist einlesen
  mpc clear
  mpc load temp
  if [ -e "$TEMPNR" ]; then
   ACTNR=$(cat "$TEMPNR")
   echo "Old State: Play #$ACTNR"
   mpc play
   mpc play $ACTNR
   if [ -e "$TEMPTIME" ]; then
   echo "Old State: Play #$ACTNR - $(cat "$TEMPTIME")"
       mpc seek "$(cat "$TEMPTIME")"
      fi
  else
   mpc play
  fi
  ;;
  *)
  echo "Usage: $0 {radio|normal}"
esac ``

Grüße
Fux

*Last Edit : 29. Dez 2010, 20:13 by Fux*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1753#msg1753)

---

<a id="msg1755"></a>

## 42. gerdigerdi · 31. Dez 2010, 11:47

Ich habe jetzt alles auf die neuste svn-version upgedatet. Funktioniert anfangs super. Jedoch nach einigen Stunden inaktivität scheint der scart-adapter sich aufzuhängen. Da hilft dann nurnoch ein reconnecten des adapters. Habt ihr das auch oder ist meine Hardware defekt? Das problem hatte ich mit allen versionen!

Ich habe viele mp3's ohne id3-tag. Die werden von der Betty dann nur mit "-" betittelt. Ich hatte mal provisorisch implementiert, dass dann der dateiname angezeigt wird. Sollte nicht der grosse Aufwand sein das an die neue Version anzupassen (Würde ich nach absprache auch übernehmen). Oder gibt es ein tool, was automatisiert die id3-tags nach dem datenamen betittelt falls nicht vorhanden? Per hand mache ich das nicht !

Weiter so - saubere Arbeit! Bin gespannt was alles noch so in die betty passt
MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1755#msg1755)

---

<a id="msg1756"></a>

## 43. phaidros · 31. Dez 2010, 12:19

> **Zitat**
>
> Jedoch nach einigen Stunden inaktivität scheint der scart-adapter sich aufzuhängen.

Ja, das Problem habe ich auch. Da ist irgendwo noch der Wurm drin.
Ich arbeite dran. Es ist  nur so schwierig, den Fehler gezielt zu produzieren.

> **Zitat**
>
> Ich habe viele mp3's ohne id3-tag. Die werden von der Betty dann nur mit "-" betittelt. Ich hatte mal provisorisch implementiert, dass dann der dateiname angezeigt wird. Sollte nicht der grosse Aufwand sein das an die neue Version anzupassen (Würde ich nach absprache auch übernehmen).

Ja gerne. Implementiere das doch bei dir und schicke mir einen Pull-Request (ich glaube so geht das bei git).

Gruß (und frohes neues Jahr)
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1756#msg1756)

---

<a id="msg1757"></a>

## 44. gerdigerdi · 31. Dez 2010, 13:41

Die reproduktion ist einfach: abends per rote taste stoppen und am nächsten morgen hängt der adapter 100%ig ;/ leider scheint es stunden zu dauern.

Im neuen jahr werde ich mich dranmachen. Evtl könen wir uns ja für detailabsprachen im IRC-Chat z.B. #bettyhacks (freenode) treffen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1757#msg1757)

---

<a id="msg1760"></a>

## 45. gerdigerdi · 03. Jan 2011, 10:01

Wollte nur positive Rückmeldung geben, dass mit dem letzten Scart-Update der morgendliche Hänger behoben scheint!

Besten Dank an Phaidros!

PS: Updaten des Scart-Adapters per seriell (USB2ser cp21xx) hat auch traumhaft funktioniert

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1760#msg1760)

---

<a id="msg1761"></a>

## 46. Fux · 03. Jan 2011, 10:47

Bekomme leider kein aktuelles (Neuanlage) git mehr drauf:
`$ git clone https://github.com/HerrSchrader/McBetty
Initialized empty Git repository in /usr/src/mpd/mcbetty/git2/McBetty/.git/
fatal: https://github.com/HerrSchrader/McBetty/info/refs not found: did you run git update-server-info on the server?`

"USB2ser cp21xx" sagt mir jetzt nichts, ist das neu?

Gruß
Fux

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1761#msg1761)

---

<a id="msg1762"></a>

## 47. gerdigerdi · 03. Jan 2011, 12:05

Ich clone immer per:
git clone git://github.com/HerrSchrader/McBetty McBetty
Gestern hats bei mir noch geklappt - sollte also jetzt auch noch gehen

Bitte zu Entschuldigen, dass ich mich nicht klar ausgedrückt habe bezüglich des "USB2ser cp21xx". Mein Scart-Adapter hängt an einen USB-Serielwandler mit einem cp2102-chip drauf. Wir hatten die Theorie, dass das serielle flashen des Scart-Adapters eventuell wegen mangelnder "Break"-Funktionalität des cp2102-chips nicht funktionierte - Lag dann wohl eher an dem falschen Image im Scart-Adapter ohne Bootloader.

Mit dem passenden Image im Scart-Adapter funktioniert das Flashen über die serielle Schnittstelle perfekt!

Ich habe durch Zufall mal die Blaue Taste betätigt. Es erscheint eine Suchmaske. Eingabe wie beim Handy. Gefällt mir gut auch wenn es anscheinend noch ohne Funktion ist. Evtl könnte man da dann später auch per Timeout auf die nächste Stelle springen. Aber das ist Finetuning ) Weiter so!
Phaidros: Hast du Urlaub oder arbeitest du auf dem Amt ? Oder wie hat man so viel zeit für ein Projekt?! (Hab Frau+Kind(er)+Hunde - da geht quasi nichts nebenbei)

MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1762#msg1762)

---

<a id="msg1763"></a>

## 48. phaidros · 03. Jan 2011, 19:53

> **Zitat**
>
> Phaidros: Hast du Urlaub oder arbeitest du auf dem Amt

Lehrer! Sind gerade noch Schulferien. Leider bald vorbei 

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1763#msg1763)

---

<a id="msg1764"></a>

## 49. jannis · 03. Jan 2011, 22:38

Und kannst du mit den Schülern auch gemeinsam weiter an der betty programmieren?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1764#msg1764)

---

<a id="msg1765"></a>

## 50. phaidros · 04. Jan 2011, 00:53

> **Zitat**
>
> Und kannst du mit den Schülern auch gemeinsam weiter an der betty programmieren?

Wird schwierig. Sind Sonderschüler!

> **Zitat**
>
> Wollte nur positive Rückmeldung geben, dass mit dem letzten Scart-Update der morgendliche Hänger behoben scheint!

Sieht bei mir auch so aus. Scart läuft problemlos durch. Hoffen wir, dass es so bleibt.
Dieser blöde drahtlose Kram ist echt schwer in den Griff zu kriegen.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1765#msg1765)

---

<a id="msg1766"></a>

## 51. gerdigerdi · 07. Jan 2011, 21:25

Echt traumhaft wie stabil die Betty nun rennt!

Ich hätte da noch ne Idee. Leider ist die betty ja nicht wirklich mit reichlich RAM bestückt (64KB), aber es gibt soweit ich weiß noch einen unbenutzten Flash-Speicherchip (1MB NOR).
Könnte man den nicht für die Speicherung der Titelnamen verwenden. Dann müssten nur bei Bedarf noch Titelinfos über die doch manchmal arg langsame Funkverbindung gesendet werden. Ist nur mal ins Unreine gedacht. Aber eine Tittelnummer+Prüfsumme ist immer weniger als manchmal bis zu 300Bytes pro Lied (bei langen Dateipfaden+viele lange id3taginfos). Dann wäre bei einem MB für 5000 Titel immerhin jeweils etwa 200Bytes da. Sollte theoretisch machbar sein. Vergibt der mpd jedem Lied ne eindeutige id? Wie seht ihr das?

Evtl ists auch der falsche Ansatz. Manchmal ist der aufbau der Trackliste rasend schnell und kurz drauf dümpeln die Tracks alle 5 Sekunden einzelnd ein. Ist das denn noch optimierbar oder einfach aufgrund der störungsanfälligen Funkübertragung so gegeben?

MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1766#msg1766)

---

<a id="msg1767"></a>

## 52. phaidros · 07. Jan 2011, 21:59

> **Zitat**
>
> Echt traumhaft wie stabil die Betty nun rennt!

Gut zu hören.

Zu deiner Idee:
Die Funkschnittstelle an sich ist nicht langsam. Die läuft mit 38kBaud, das sind ungefähr 4000 Bytes pro Sekunde. Also bei 300 Bytes pro Titel sollten mindestens 10 Titel pro Sekunde reinkommen.
Langsamer wird es, wenn die Funkverbindung gestört ist (vielleicht durch andere Sender auf der Frequenz). Dann warten sowohl Betty als auch mpdtool ein paar Sekunden auf einen Time-Out, bevor die Übertragung erneut versucht wird. Kommt bei mir selten vor (recht störungsfreie Umgebung).
Das mit dem Titelspeichern könnte eventuell gehen (ich weiß auch nicht genau, wie der NOR-Speicher anzusprechen ist, kann man aber ja rauskriegen).
ABER:
Was nützen mir 5000 Titel? Meine Sammlung ist deutlich größer. Ich hätte dann doch immer nur einen Teil im NOR, vielleicht gerade den, den ich nicht so oft brauche.
Da wären also ausgeklügelte Cache-Strategien nötig, weil man das NOR ja auch nicht beliebig oft überschreiben kann. Scheint mir recht aufwändig zu werden.
Alternative Möglichkeit.
Betty nutzt im Moment sowieso nur Titel und Interpret bei der Tracklist. Man könnte mpdtool beibringen, alles andere an Infos schon vor dem Senden rauszufiltern.
Vielleicht bringt das was. Ist schnell zu machen. (Infrastruktur für sowas ist in mpdtool schon vorhanden). Werde ich bei Gelegenheit mal austesten.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1767#msg1767)

---

<a id="msg1768"></a>

## 53. jannis · 07. Jan 2011, 22:26

Also ich komm mit dem flashen net klar. ich hab auch nen cp210x und mpd klappt ja auch wie man sieht:
 `./mpdtool /dev/ttyUSB0  192.168.178.23 6600
Checking scart adapter
Scart adapter firmware V1.0
 MPD: OK MPD 0.15.0

(MPD): OK
(MPD): OK
MPD: Available Playlists = 11`
Aber warum klappt das hier nicht?!
 `make resident
./flashtool /dev/ttyUSB0
Sending break
Read 0 characters:
       
Read 0 characters:
       
buffer[0] = 00
Error: Could not negotiate baud rate!
make: *** [resident] Error 20`

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1768#msg1768)

---

<a id="msg1769"></a>

## 54. gerdigerdi · 07. Jan 2011, 23:14

Das Flashen des Scart-Adapters per flashtool hat bei mir erst nach dem einmaligen Einspielen des richtigen Images mit bootloader UND restarten (stromlos machen) des Scartadapters, funktioniert.
Es schien jedoch einen Bug im Linuxkerneltreiber für den cp210x gegeben zu haben. Ich nutze erfolgreich den gentookernel 2.6.35-gentoo-r5 zum Flashen.
Bei mir war es das falsche Image im Scart-Adapter.
Eigendlich sollte es ja klappen wenn der Kontakt zum mpdtool klappt.

Anderes Thema
> **Zitat**
>
> Die Funkschnittstelle an sich ist nicht langsam. Die läuft mit 38kBaud, das sind ungefähr 4000 Bytes pro Sekunde. Also bei 300 Bytes pro Titel sollten mindestens 10 Titel pro Sekunde reinkommen.
> Langsamer wird es, wenn die Funkverbindung gestört ist (vielleicht durch andere Sender auf der Frequenz). Dann warten sowohl Betty als auch mpdtool ein paar Sekunden auf einen Time-Out, bevor die Übertragung erneut versucht wird.

Evtl langts ja schon die Time-Outs beidseitig zu verkürzen. In dem Frequenzband wird meines Wissens oft eh nur kurzzeitig gesendet (z.B. Außenthermometer).
Wird die Übertragung eigendlich Hard-oder Softwareseitig irgendwie fehlerkorigiert?

MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1769#msg1769)

---

<a id="msg1770"></a>

## 55. phaidros · 08. Jan 2011, 12:32

> **Zitat**
>
> Wird die Übertragung eigendlich Hard-oder Softwareseitig irgendwie fehlerkorigiert?

Nein. Es gibt eine CRC-Checksumme, die hardwareseitig erzeugt und auch überprüft wird. Die dient nur der Fehlererkennung.
Eine Fehlerkorrektur wird bei drahtloser Übertragung eher selten gemacht, weil die häufigsten Fehler sind dabei sogenannte
Burst-Fehler, d.h. in einem Paket sind gleich ganz viele Bytes hintereinander gestört. Da bringt dann eine Fehlerkorrektur nicht
mehr viel.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1770#msg1770)

---

<a id="msg1774"></a>

## 56. jannis · 11. Jan 2011, 01:08

muss man die 3,3v anschliessen beim flashen des scart adapters? ich hab im mom nur folgende kabel angeschlossen: cp210x: rx/tx/gnd -> scart: tx/rx/gnd
Wenn es mit dem mpdtool klappt, kann das dann sein, dass es mit dem lpctool nicht klappt?! Oder kann mein cp210x dann tatsaechlich keinen break senden?!

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1774#msg1774)

---

<a id="msg1775"></a>

## 57. gerdigerdi · 11. Jan 2011, 20:22

Der Scartadapter muss zum Flashen per Bootloader genauso angeschlossen sein wie er es zum Betrieb auch ist (Versorgungsspannung wie auch immer + rx/tx/gnd).
Zum Flashen natürlich das "flashtool" aus dem scart_image Verzeichnis - lpctool war nen Vertipper, oder

Das habe ich zum "break-bug" des cp210x gefunden:
(falls Links nicht erlaubt sind bitte löschen) ;)https://patchwork.kernel.org/patch/129491/
Schließe daraus das der bug bis zum 2.6.34 er Kernel überlebt hat.

phaidros: Hab ich das richtig gesehen, dass du mit nem 2-Zeiler die Titelvergabe per Dateinamen gelöst hast? (hab die neuste noch nicht geflashed) 

MfG
Gerdi

*Last Edit : 11. Jan 2011, 20:27 by gerdigerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1775#msg1775)

---

<a id="msg1776"></a>

## 58. jannis · 11. Jan 2011, 21:33

Argh, ok, ich kompiliere meinen 2.6.33 dann jetzt zum 5. mal neu

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1776#msg1776)

---

<a id="msg1779"></a>

## 59. phaidros · 12. Jan 2011, 01:44

> **Zitat**
>
> phaidros: Hab ich das richtig gesehen, dass du mit nem 2-Zeiler die Titelvergabe per Dateinamen gelöst hast? (hab die neuste noch nicht geflashed) 

Im Prinzip ja. Ich habe das Problem einfach von Betty auf mpdtool verlagert. Da habe ich die schöne basename() Funktion schon, die ich sonst für Betty hätte schreiben mössen.
Vorher waren aber noch ein paar Aufräumarbeiten in Bettys Code nötig.
Ich habe auch gemerkt, dass ich viel mehr Stücke ohne richtigen Titel-Tag habe als gedacht.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1779#msg1779)

---

<a id="msg1780"></a>

## 60. gerdigerdi · 12. Jan 2011, 12:57

Hab das noch bissel erweitert. Nun sollts auch in der Playlistansicht helfen

Hatte noch keinen Nerv mit mit dem Git auseinander zu setzen, daher die Änderungen als File. Hab die Datein nochmal hochgeladen.

Leider scheints noch einen Bug in der Playansicht zu geben. Es wird nicht immer der Artist angezeigt zumindest nachdem ich meine Änderungen gemacht habe.
Es werden alle Artists angezeigt die als id3-tag existieren. Wird dann auf einen Tittel mit FakeArtist(ohne ide-Tag) ungeschaltet, wird der Erste Fehlerfrei angezeigt. alle weiteren danach nicht mehr (Siw werden aber zur betty gesendet!). Es scheint aber an meinen "Fuschcode" zu liegen. Wenn du zeit hast schaus dir mal an. 
MfG
Gerdi

*Last Edit : 13. Jan 2011, 09:35 by gerdigerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1780#msg1780)

---

<a id="msg1782"></a>

## 61. phaidros · 13. Jan 2011, 01:06

> **Zitat**
>
> Hatte noch keinen Nerv mit mit dem Git auseinander zu setzen, daher die Änderungen als File.

Das hat bei mir nicht funktioniert. Das tar Archiv enthält keine C-Datei?

> **Zitat**
>
> Leider scheints noch einen Bug in der Playansicht zu geben. Es wird nicht immer der Artist angezeigt.

Oha! Lässt sich das reproduzieren? Wenn ja, wie ?

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1782#msg1782)

---

<a id="msg1784"></a>

## 62. gerdigerdi · 13. Jan 2011, 09:35

Ich hab die Datei nochmal hochgeladen - nun sollts klappen - sorry!
Der Aufbau der Playlist funktionierte mit der Filterung übrigends flüssigst. Wie kann man im mpdtool filtern ob schon ein Titel/Artist Tag vorhanden ist, oder ob die Fake-Tags gesendet werden müssen? Mit doppelten Tags in der Tracklist (meine Änderung) wirds wieder langsam. Irgendwie steige ich noch nicht 100%ig durch deinen Code durch :/

Wie soll das eigentlich mit der Suche funktionieren (blaue Taste). Ergebnisse werden angezeigt aber nicht gespielt oder ist das noch nicht funktional?
MfG
Gerdi

*Last Edit : 13. Jan 2011, 09:41 by gerdigerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1784#msg1784)

---

<a id="msg1787"></a>

## 63. phaidros · 13. Jan 2011, 19:38

> **Zitat**
>
> Wie soll das eigentlich mit der Suche funktionieren (blaue Taste). Ergebnisse werden angezeigt aber nicht gespielt oder ist das noch nicht funktional?

Ein paar Buchstaben eingeben (wie auf Handy-Tastatur). Es erscheint eine Liste mit möglichen Kandidaten.
Mit dem Steuerkreuz hoch- und runterscrollen, bis man beim gewünschten Künstler ist. Dann OK drücken.
Alle Titel dieses Künstlers sollten dann in die laufende Playliste übernommen werden. Geht bei mir.

> **Zitat**
>
> Ich hab die Datei nochmal hochgeladen - nun sollts klappen - sorry!

Werde ich mir gleich mal anschauen.

Gruß

Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1787#msg1787)

---

<a id="msg1788"></a>

## 64. phaidros · 13. Jan 2011, 20:19

Ich habe nur ganz kurz auf deinen Code geschaut. Du includest am Anfang die libgen. Das ist nicht gut. Die basename() Funktion in libgen garantiert nicht, dass der Original-String unverändert bleibt. Die GNU basename() verändert nichts am übergebenen string.

Wenn ich deinen Code richtig verstehe, möchtest du den Ordner-Namen als Namen des Künstlers übergeben. Das geht zwar, macht aber doch nur bei den Leuten Sinn, die ihre Dateien entsprechend gespeichert haben. Bei mir ist der Ordner-Name meistens (aber auch nicht immer) der Album-Titel. Und bei Compilations taucht der Künstler wahrscheinlich gar nicht im Dateinamen auf. Die Lösung ist also wohl nur selten wirklich gut. Ich finde es besser, dann einfach nichts (oder "?") anzuzeigen. Das erhöht den Leidensdruck auf den Anwender, endlich seine mp3s richtig zu taggen!

> **Zitat**
>
> Wie kann man im mpdtool filtern ob schon ein Titel/Artist Tag vorhanden ist, oder ob die Fake-Tags gesendet werden müssen?

Das kann man erst erkennen, wenn "OK" gesendet werden soll. Erst dann weiß man, dass nichts mehr kommt. Man mus vorher alle Antworten interpretieren und speichern,
wenn "Artist: " oder "Title: " erkannt wird.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1788#msg1788)

---

<a id="msg1789"></a>

## 65. gerdigerdi · 13. Jan 2011, 20:43

Das der Original-String verändert wird ist mir auch schon aufgefallen .. manchmal kommen da seltsame Ergebnisse zustande. Dann lieber wie gehabt.
Klappt das so mit der Tracklistansicht wie ich mir das gedacht habe? Du hast die Dateinamen ja nur in der Play-Ansicht übernommen.

Apropos Leidensdruck: Ich habe mich mal mit Kid3 drangemacht und meine MP3s nachgetagt.  Geht recht gut - mit quasi automatisierter suche im i-net.

> **Zitat**
>
> Alle Titel dieses Künstlers sollten dann in die laufende Playliste übernommen werden.

Da muss ich ja mal schauen wie lange nun meine playlist ist. Der hängt das dann ans Ende nehme ich mal an. Ich dachte er spielt das dann direkt. O.K. das erklärt einiges!
Da fehlt dann evtl. noch eine Taste zum direkt nach der suche abspielen. Die Suche klappt übrigends super!
Thx.
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1789#msg1789)

---

<a id="msg1790"></a>

## 66. phaidros · 13. Jan 2011, 21:27

> **Zitat**
>
> Klappt das so mit der Tracklistansicht wie ich mir das gedacht habe? Du hast die Dateinamen ja nur in der Play-Ansicht übernommen.

Muss ich mir noch mal anschauen. Aber im Prinzip schon.

> **Zitat**
>
> Da fehlt dann evtl. noch eine Taste zum direkt nach der suche abspielen.

Genau! Das ist noch irgendwie unausgegoren. Er hängt sie wirklich hinten dran. Ist verwirrend. Ich lösche immer vorher die Playlist, um dann die Ergebnisse
der Suche besser sehen zu können. Vielleicht die grüne Taste (die ja sonst auch PLAY bedeutet) zum direkt abspielen nehmen?
Oder nach Druck auf OK ein extra Menü einblenden, wo der Anwender wählen kann:

<<< 42 Titel gefunden. >>>

 A = an aktuelle Playliste anhängen
 B = als neue Playliste übernehmen
 Exit = cancel

Was meinst du  ?

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1790#msg1790)

---

<a id="msg1793"></a>

## 67. gerdigerdi · 13. Jan 2011, 23:40

> **Zitat**
>
> Vielleicht die grüne Taste (die ja sonst auch PLAY bedeutet) zum direkt abspielen nehmen?
> Oder nach Druck auf OK ein extra Menü einblenden, wo der Anwender wählen kann:

Am praktikabelsten wäre meiner Meinung nach quasi beides. Wobei die OK-Taste das von dir beschriebene "Hilfe-Menü" öffnet, was die Direktwahltasten beschreibt oder auswählbar macht. Also ohne Menü, für die die wissen wie es geht und mit, intuitiv menügeleitet per OK-Taste und Auswahl per Menüpunkt. Denke eine simple Hilfeseite mit den Tastenkürzeln ("Grün" als neue Playliste übernehmen ...) ist einfacher zu implementieren.

Nett wärs wenn die Suchmaske offen bleiben würde mit "Popup" "Wurden Hinzugefügt" oder so.
Evtl noch nen button für "neue Suche" (Maske löschen). Aber das ist Finetuningschnickschnack - würde aber die Zusammenstellung neuer Playlists per betty beschleunigen.
Vor der Implementierung der neuen Suchfunktion hätte ich nie gedacht, dass eine Playlisterstellung per betty praktikabel/machbar wäre! 
MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1793#msg1793)

---

<a id="msg1795"></a>

## 68. phaidros · 14. Jan 2011, 12:06

Ja. Klingt gut. Ich werde mal kucken, wie weit ich am Wochenende komme.
Die neueste Version auf github sollte jetzt auch fehlende Titel in der Playlisten-Ansicht ergänzen.
Wurde allerdings einiges umstrukturiert, so dass ich noch nicht alles testen konnte.
Vor lauter Programmieren kommt man ja gar nicht mehr zum Musikhören

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1795#msg1795)

---

<a id="msg1796"></a>

## 69. jannis · 14. Jan 2011, 12:52

> Vor lauter Programmieren kommt man ja gar nicht mehr zum Musikhören

Das stimmt, meine Lautsprecher haben jetzt nicht mal mehr das Kabel angeschlossen...
Das war ja eigentlich nicht der Sinn der Sache *g*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1796#msg1796)

---

<a id="msg1797"></a>

## 70. gerdigerdi · 14. Jan 2011, 18:30

Ich komme auch zu nichts .. Meine Tochter Malea ist heute nacht gekommen!

51cm , 3,2kg .. alles O.K.
MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1797#msg1797)

---

<a id="msg1798"></a>

## 71. glotzi · 14. Jan 2011, 18:32

> **Zitat von: gerdigerdi am 14. Jan 2011, 18:30**
>
> Ich komme auch zu nichts .. Meine Tochter Malea ist heute nacht gekommen!
>
> 51cm , 3,2kg .. alles O.K.
> MfG
> Gerdi

Glückwunsch, dann wirst du nun zu gar nichts mehr kommen und schon gar nicht zum musikhören.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1798#msg1798)

---

<a id="msg1799"></a>

## 72. phaidros · 14. Jan 2011, 19:24

Auch von mir herzlichen Glückwunsch !

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1799#msg1799)

---

<a id="msg1800"></a>

## 73. gerdigerdi · 14. Jan 2011, 20:37

Dank euch! Meine erste ist schon fast 3. Hoffe ich finde trotzdem noch Zeit!

MfG
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1800#msg1800)

---

<a id="msg1803"></a>

## 74. asgard · 15. Jan 2011, 19:55

Wünsche euch auch alles Gute!

Liebe Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1803#msg1803)

---

<a id="msg1804"></a>

## 75. gerdigerdi · 18. Jan 2011, 22:58

Zurück zum Thema!
> **Zitat**
>
> Die neueste Version auf github sollte jetzt auch fehlende Titel in der Playlisten-Ansicht ergänzen.
> Wurde allerdings einiges umstrukturiert, so dass ich noch nicht alles testen konnte.

Bin beeindruckt! Ersten Tests nach, ist die Playlisten-Ansicht super flüssig auch beim seitenweisen Blättern. Dateinamen werden richtig gesetzt bei fehlender Betitelung

Hab aber noch einen Schönheitsfehler entdeckt - sorry - wird mir langsam peinlich
Bei manchen  langen einzeiligen Titeln wird in der Playansicht der erste Buchstabe abgeschnitten (Der Name wird korrekt übertragen - Nur nicht komplett angezeigt - Wäre außerhalb des Sichtbereichs). Ist mir erst nach der Umstellung des Trennzeichens aufgefallen. Keinen Plan ob es damit irgendwie zusammenhängt.

Aber wie immer saubere Arbeit. Hoffe der Urlaub war trotzt des Programmier-Marathons erholsam!

MfG
Gerdi

*Last Edit : 18. Jan 2011, 23:03 by gerdigerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1804#msg1804)

---

<a id="msg1806"></a>

## 76. phaidros · 22. Jan 2011, 03:00

> **Zitat**
>
> Hab aber noch einen Schönheitsfehler entdeckt - sorry - wird mir langsam peinlich

Nicht doch, dafür sind doch Tester da!
Konnte den Fehler noch nicht reproduzieren. Wie lang muss der Name denn ungefähr sein?

Auf github gibt es jetzt eine erste Version mit Menü-Führung. Betty-Taste und Info-Taste zeigen Optionen.
Die Script-Aufruftasten musste ich dazu leider verlegen auf die Video-Text Tasten.

Bei der Suche gibt "OK" jetzt ein Popup mit den Optionen.

Achtung: Viele interne Umstrukturierungen und noch nicht sehr ausführlich getestet. Bugs bitte melden.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1806#msg1806)

---

<a id="msg1807"></a>

## 77. gerdigerdi · 23. Jan 2011, 21:36

Seltsamer weise habe ich den Fehler auch nicht mehr reproduzieren können also vergess es einfach erstmal - Fehlalarm

Du hast dich ja mit dem letzten Update richtig ins Zeug gelegt!
Zahlreiche info und Help Popups - Gefällt mir sehr gut! Nur der letzte Punkt im "Suchmenu" (irgendwas mit play (hab die betty nicht hier)) ist etwas zweideutig. Dacht damit geht direkt abspielen - scheint aber quasi Abbruch zu sein, oder war das nicht so geplant?

Für mich wünschenswert wäre (falls problemlos möglich), wenn nach einer Suche und neuer Playlisterstellung gleich die Wiedergabe beginnen würde. Aber das ist "Luxusschnickschnack". Genauso wie das Abbspeichern der zusammengestellten Playlist
Die Suche hat manchmal auch noch einen kleinen Schönheitsfehler. Die ersten 1-2 Zeichen können dann nicht gelöscht werden (der cursor bleibt an 2. stelle). Bei erneuter eingabe springt der Cursor dann jedoch an die richtige 1. Position. Passiert manchmal, wenn man von der Suche direkt in die playlist und zurück zur Suche hüpft.

Noch was .. beim Wechsel von Playansicht zur Playlist springt der Cursor nicht zum aktuellen Track, war das nicht mal implementiert? Ist besonders bei Randomplay in langen Playlists interessant.

Langsam muss ich mir ne 2. Betty zulegen. Immer wenn ich sie updaten will flucht meine Frau weil sie 10 Minuten drauf verzichten muss

Zum Glück erfreut sich meine Kleine auch an guter Musik - So bleibt mir wenigstens dazu etwas zeit.

Grüße
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1807#msg1807)

---

<a id="msg1808"></a>

## 78. jannis · 25. Jan 2011, 01:56

Hi, ich habe ein kleines Problem. Ich versuche mich an der Stelle im Scart-Adapter einzuklinken, wo mit send_byte(x) die Kommandos an die serielle Schnittstelle weitergeleitet werden. Dort teste ich ob ein bestimmter string empfangen wurde. Aus irgendeinem Grund funktioniert das aber nicht. Vielleicht koennt ihr das Brett vor meinem Kopf finden

Als einfaches Beispiel in check_radio_input():
Betty wurde angepasst, dass sie z.B. 0x10 sendet...
 `x = cc1100_read_fifo();
switch(x){
case 0x10: KB7=0; break;
case 0x11: KB7=1; break;
}`
Funktioniert nicht. Ich hab auch mal gegen einen String der mit Sicherheit auch von betty ankommt getestet:
`unsigned char cs=0;
unsigned char volstring[]="setvol";
x = cc1100_read_fifo();
if(x==volstring[cs])
  cs++;
else
  cs=0;
if(cs>5)
  KB7=0;`

Hat jemand ne Idee?
Oder wie debugged ihr sowas? Ist echt anstrengend immer wieder meine betty zu flashen um damit den scart adapter zu flashen usw...
Vielleicht sollt ich zuerst endlich mal diesen Kernel mit funktionierendem usb-serial kompilieren...

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1808#msg1808)

---

<a id="msg1809"></a>

## 79. phaidros · 25. Jan 2011, 05:56

> **Zitat**
>
> Nur der letzte Punkt im "Suchmenu" (irgendwas mit play (hab die betty nicht hier)) ist etwas zweideutig. Dacht damit geht direkt abspielen - scheint aber quasi Abbruch zu sein, oder war das nicht so geplant?

Ist jetzt umbenannt in "Main Screen". Sollte einfach wieder auf den "Playing" Bildschirm umschalten. War aber wirklich sehr missverständlich.

> **Zitat**
>
> Für mich wünschenswert wäre (falls problemlos möglich), wenn nach einer Suche und neuer Playlisterstellung gleich die Wiedergabe beginnen würde.

Das geht in der neuesten Version mit der "C" Taste (Add & Play). Das Löschen des Eingabefeldes wurde deswegen verlegt auf die AV-Taste.

> **Zitat**
>
> Aber das ist "Luxusschnickschnack". Genauso wie das Abbspeichern der zusammengestellten Playlist

Das ist ja wohl ein Wink mit dem Zaunpfahl. Aber dazu brauchen wir wieder einen eigenen Bildschirm mit einer Eingabemaske für den Dateinamen.
Meine bisherige Maske gibt aber nicht mehr als 15 Zeichen her. Alles andere ist schwerer zu implementieren.
Andere Möglichkeit wäre eine automatische Dateinamengenerierung. Ist deutlich einfacher zu machen. Vielleicht als "Save01.m3u" oder mit Datum und Uhrzeit im Namen?

> **Zitat**
>
> Die Suche hat manchmal auch noch einen kleinen Schönheitsfehler.

Ja. War ein ganz blöder Fehler. Habe jetzt die entsprechenden Routinen noch mal überarbeitet. Hoffe es klappt jetzt besser. Bin noch nicht richtig zum Testen gekommen.

> **Zitat**
>
> Noch was .. beim Wechsel von Playansicht zur Playlist springt der Cursor nicht zum aktuellen Track, war das nicht mal implementiert? Ist besonders bei Randomplay in langen Playlists interessant.

Macht er jetzt wieder. Hatte ich rausgenommen, weil der Code so unelegant war. Ist jetzt besser.
> **Zitat**
>
> Langsam muss ich mir ne 2. Betty zulegen.

Wie? Du hast nur eine?  :)I

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1809#msg1809)

---

<a id="msg1810"></a>

## 80. phaidros · 25. Jan 2011, 06:13

> **Zitat von: jannis am 25. Jan 2011, 01:56**
>
> `x = cc1100_read_fifo();
> switch(x){
> case 0x10: KB7=0; break;
> case 0x11: KB7=1; break;
> }`
> Funktioniert nicht.

Hast du auch KB7 auf Output gesetzt? Ist der Pin wirklich frei? Probier mal statt dessen einfach X auf ein anderes Zeichen zu setzen, z.B "a" oder "b".
Das sollte man dann im output von mpdtool sehen können.

> **Zitat**
>
> Oder wie debugged ihr sowas? Ist echt anstrengend immer wieder meine betty zu flashen um damit den scart adapter zu flashen usw...
> Vielleicht sollt ich zuerst endlich mal diesen Kernel mit funktionierendem usb-serial kompilieren...

Ja, nur so kommt man voran. Das Flashen über Betty ist einfach zu umständlich.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1810#msg1810)

---

<a id="msg1811"></a>

## 81. glotzi · 25. Jan 2011, 08:12

> **Zitat von: jannis am 25. Jan 2011, 01:56**
>
> Vielleicht sollt ich zuerst endlich mal diesen Kernel mit funktionierendem usb-serial kompilieren...

Für welchen Kernel brauchst Du das? Für die VIP1710? Die habe ich.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1811#msg1811)

---

<a id="msg1813"></a>

## 82. jannis · 25. Jan 2011, 12:46

Ja fuer die VIP brauch ich auch noch so ein Modul. Das kann auch noch was warten, aber ich denke, dass ich darauf zurueckkommen werde

Der KB7 port funktioniert auf jeden Fall, denn wenn ich den in der main toggle seh ich das auch.
Vorher hab ich da noch son SMD kram abgeloetet von dem ich nicht wusste wofuer der da war...

Also, ich werd jetzt auf jeden Fall mal mein Kernel Modul fuer meinen PC zum flashen des Scart adapters in Ordnung bringen. Aber ich weiss noch nicht wie's dann weiter gehen soll. Mir gehen die Ideen aus  :'(

Also es wird alles was mit send_byte verschickt wird von mpdtool angezeigt?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1813#msg1813)

---

<a id="msg1814"></a>

## 83. phaidros · 25. Jan 2011, 18:17

> **Zitat**
>
> Also es wird alles was mit send_byte verschickt wird von mpdtool angezeigt?

Ja, alles größer als 0x20.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1814#msg1814)

---

<a id="msg1815"></a>

## 84. jannis · 26. Jan 2011, 17:36

> **Zitat von: gerdigerdi am 11. Jan 2011, 20:22**
>
> Das habe ich zum "break-bug" des cp210x gefunden:
> (falls Links nicht erlaubt sind bitte löschen) ;)https://patchwork.kernel.org/patch/129491/
> Schließe daraus das der bug bis zum 2.6.34 er Kernel überlebt hat.

Also, ich bin nun endlich dazu gekommen dieses Kernel modul mit dem integrierten patch neu zu kompilieren.
Geaendert hat sich allerdings gar nix

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1815#msg1815)

---

<a id="msg1816"></a>

## 85. jannis · 26. Jan 2011, 18:58

Oops. doch, inzwischen ist was passiert, jetzt klappt gar nix mehr
Nicht mal die betty kann den adapter jetzt noch ansprechen.

Vielleicht war der Schalter von der Steckdosenleiste schuld an dieser Misere.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1816#msg1816)

---

<a id="msg1817"></a>

## 86. glotzi · 27. Jan 2011, 22:56

Hallo,

ich habe inzwischen McBetty endlich auch am rennen, das flashen des ScartAdapters war doch ziemlich fumlig. Der ScartAdapter läuft nun an einer Motorola Vip1710 via Usb2Serial Kabel. Folgende Probleme sind mir aufgefallen:

- mpdtool startet manchmal nicht, wenn es aber mehrfach hintereinader gehts dann auf einmal. Ich habe den Code so geändert, dass scart_alive in main() mehrfach aufgerufen wird, beim zweiten Aufruf klappts dann. So sieht das dann aus:

 `int t=0;
 while (1) {
   /* Check that the scart adapter is connected and responding */
   if (!scart_alive()){
  fprintf(stderr,"Error. Scart adapter not responding.\n");
  fprintf(stderr,"Is scart adapter connected to %s ?\n", serial_device );
  fprintf(stderr,"Maybe powercycling the scart adapter could help.\n");
  if (t==5) {
    exit(20);
  } else {
    t++;
  }
   } else {
     break;
   }
 }`

- Ich kann scheinbar keine MPD Playlisten laden. Hat das Problem noch jemand?

- Die Suchmaske wird manchmal zu Einbahnstrasse, ich musste einmal die Batterien rausnehmen, weil ich nicht mehr rauskam

- Wenn man Shoutcast Streams abspielt, werden ständig die Infos auf der Betty akualisiert, was zu dazu führt, dass das Display flackert. Es wäre sinnvoll die Track/Stream Infos nur zu aktualisieren, wenn sie sich ändern

Nochmal Danke für dieses tolle Projekt, ich finde es wirklich super.

Edit: letzen Punkt auf der Liste eingefügt

*Last Edit : 27. Jan 2011, 23:05 by glotzi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1817#msg1817)

---

<a id="msg1818"></a>

## 87. stevie101 · 28. Jan 2011, 11:09

Hallo zusammen,

hab mittlerweile auch McBetty im Zusammenhang mit der vip1710 laufen.
Scart Adapter war sehr fummelig - kann ich nur bestätigen, allerdings flashe ich alles über serielle Verbindung, da gab es einige nicht reproduzierbare Probleme.
Der Scart Adapter ist bei mir über serielle Schnittstelle an der vip. Arbeiten beide mit 3.3 V Pegel, daher kann man direkt anschliessen. Allerdings ist bei der vip, /dev/tts/0 mit einer console per default belegt - hat ne Weile gedauert, bis ich geblickt hatte, dass das die Kommunikation stört.

Bezüglich Suchfunktion hab ich folgendes festgestellt (latest git) :
- insgesamt scheint mpdtool doch etwas sehr ungeduldig, wenn Suche aktiv. Die CPU Auslastung durch mpdtool allein liegt schon um die 30-40% (nur bei Suche).  Hab das Gefühl, MPD kommt gar nicht zum Antworten (Communication broken).
Beispiel: Artist
Suche: New
MPD liegt 60%, mpdtool bei 30%, irgendwann hab ich ein Resultat
gleiche Suche mit NCMPC++ ---> 536 Songs in ca. 6sec
Ähnliches passiert übrigens, wenn ich eine Playlist mit ca. 5500 Songs lade. mpdtool scheint MPD nicht genügend Zeit zu geben

- die Resultate haben manchmal nichts mit dem Suchbegriff zu tun. Suche nach "ORD" - ja ich suche immernoch New Order -, ergibt unter anderem "Morrissey" :-)

- hab die max. Ergebnisse nicht gezählt, aber es scheinen keine 50 angezeigt zu werden (wenn >=50 gefunden)
Was passiert mit den anderen Ergebnissen, wenn >50 gefunden werden ?

- Wird eine Suche gelöscht, schickt die Betty Suche:"" Richtung MPD, was die Kommunikation blockiert. Kann man hier, wenn AV gedrückt wird, die Suche nicht umgehend stoppen ?

Playlistanzeige und laden funktioniert hier gut.

Das Projekt ist einfach klasse - endlich kann ich meine MP3's verwalten ohne TV, vielen Dank dafür.

Gruss
Stefan

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1818#msg1818)

---

<a id="msg1819"></a>

## 88. glotzi · 28. Jan 2011, 11:30

> **Zitat von: stevie101 am 28. Jan 2011, 11:09**
>
> ... allerdings flashe ich alles über serielle Verbindung, da gab es einige nicht reproduzierbare Probleme.
> Der Scart Adapter ist bei mir über serielle Schnittstelle an der vip. Arbeiten beide mit 3.3 V Pegel, daher kann man direkt anschliessen. Allerdings ist bei der vip, /dev/tts/0 mit einer console per default belegt - hat ne Weile gedauert, bis ich geblickt hatte, dass das die Kommunikation stört.

Das mit der Onboard Serial hatte ich mir auch schon überlegt. Mir ist aber nichts eingefallen, wie ich dem Kernel abgewöhnen kann tty0 als console zu benutzen. Dazu müsste man eigentlich die Kernel Commandline ändern und die ist in den Bootloader gebacken.

Du flashst auf der Vip? Wie hast Du das mit der Console gelöst?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1819#msg1819)

---

<a id="msg1820"></a>

## 89. stevie101 · 28. Jan 2011, 11:55

> **Zitat**
>
> Das mit der Onboard Serial hatte ich mir auch schon überlegt. Mir ist aber nichts eingefallen, wie ich dem Kernel abgewöhnen kann tty0 als console zu benutzen. Dazu müsste man eigentlich die Kernel Commandline ändern und die ist in den Bootloader gebacken.
>
> Du flashst auf der Vip? Wie hast Du das mit der Console gelöst?

Die inittab wird modifiziert, initialisiere diese mit "init -q" und kille dann /bin/sh.  Funktioniert noch nicht ganz automatisiert, irgendwie wird "init -q" innerhalb eines Skriptes nicht durchgeführt, händisch geht es.
Geflashed hab ich auf der VIP noch nicht, sollte aber problemlos funktionieren.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1820#msg1820)

---

<a id="msg1821"></a>

## 90. glotzi · 28. Jan 2011, 12:08

> **Zitat von: stevie101 am 28. Jan 2011, 11:55**
>
> Die inittab wird modifiziert ...

Hmm,

meine inittab sieht so aus:
 `# IP-STB inittab

::respawn:/bin/sh
::sysinit:/etc/rc.sysinit
::wait:/usr/sbin/telnetd
::once:/usr/bin/start_platform.sh`

Was müsste ich da modifzieren? Sorry, das ich so blöde Frage.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1821#msg1821)

---

<a id="msg1823"></a>

## 91. stevie101 · 28. Jan 2011, 12:17

> **Zitat**
>
> Was müsste ich da modifzieren? Sorry, das ich so blöde Frage.

Kein Problem,  lösche folgendes:

`::respawn:/bin/sh`

dann init -q, kill -9 PID (/bin/sh). Damit ist tts/0 frei.
Wenn Du das automatisiert machen willst, kann es sein, dass start_platform.sh und damit der halserver beendet wird (restart). Bin leider kein toller skripter, daher lasse ich start_platform.sh und die runvdr.sh mit /bin/bash starten. Dann könnte man auch alle sh's killen.
Der scart adapter sollte beim booten der vip am besten stromlos sein. Der bekommt soviel Krempel von der vip beim booten mit, dass mpdtool ihn nicht initialisieren kann.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1823#msg1823)

---

<a id="msg1824"></a>

## 92. phaidros · 28. Jan 2011, 13:03

> **Zitat von: stevie101 am 28. Jan 2011, 11:09**
>
> Hallo zusammen,
>
>
> Bezüglich Suchfunktion hab ich folgendes festgestellt (latest git) :
> - insgesamt scheint mpdtool doch etwas sehr ungeduldig, wenn Suche aktiv. Die CPU Auslastung durch mpdtool allein liegt schon um die 30-40% (nur bei Suche).  Hab das Gefühl, MPD kommt gar nicht zum Antworten (Communication broken).
> Beispiel: Artist
> Suche: New
> MPD liegt 60%, mpdtool bei 30%, irgendwann hab ich ein Resultat
> gleiche Suche mit NCMPC++ ---> 536 Songs in ca. 6sec
> Ähnliches passiert übrigens, wenn ich eine Playlist mit ca. 5500 Songs lade. mpdtool scheint MPD nicht genügend Zeit zu geben

Das stimmt. Die Zeit ist sehr knapp eingestellt (2 Sekunden).

> **Zitat**
>
> - die Resultate haben manchmal nichts mit dem Suchbegriff zu tun. Suche nach "ORD" - ja ich suche immernoch New Order -, ergibt unter anderem "Morrissey" :-)

Das ist merkwürdig.

> **Zitat**
>
> - hab die max. Ergebnisse nicht gezählt, aber es scheinen keine 50 angezeigt zu werden (wenn >=50 gefunden)
> Was passiert mit den anderen Ergebnissen, wenn >50 gefunden werden ?

Die werden einfach weggeworfen. Zur Zeit werden nur ca. 30 angezeigt. Ich dachte, keiner will durch 50 Ergebnisse scrollen. Lieber noch einen Buchstaben
mehr eintippen um die Suche einzischränken ?
> **Zitat**
>
> - Wird eine Suche gelöscht, schickt die Betty Suche:"" Richtung MPD, was die Kommunikation blockiert. Kann man hier, wenn AV gedrückt wird, die Suche nicht umgehend stoppen ?

Mal schauen.

> **Zitat**
>
> Playlistanzeige und laden funktioniert hier gut.
> Das Projekt ist einfach klasse - endlich kann ich meine MP3's verwalten ohne TV, vielen Dank dafür.

Das freut zu hören. Die Probleme sind registriert. Mal sehen, ob sich was machen lässt.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1824#msg1824)

---

<a id="msg1825"></a>

## 93. glotzi · 28. Jan 2011, 13:04

> **Zitat von: stevie101 am 28. Jan 2011, 12:17**
>
> Kein Problem,  lösche folgendes:
>
> `::respawn:/bin/sh`
>
> dann init -q, kill -9 PID (/bin/sh). Damit ist tts/0 frei.

Ahh, die shell.

> **Zitat von: stevie101 am 28. Jan 2011, 12:17**
>
> Wenn Du das automatisiert machen willst, kann es sein, dass start_platform.sh und damit der halserver beendet wird (restart). Bin leider kein toller skripter, daher lasse ich start_platform.sh und die runvdr.sh mit /bin/bash starten. Dann könnte man auch alle sh's killen.
> Der scart adapter sollte beim booten der vip am besten stromlos sein. Der bekommt soviel Krempel von der vip beim booten mit, dass mpdtool ihn nicht initialisieren kann.

Das ist alles ziemlich gruselig. Ich wollt den ScartAdap eigentlich fest in die vip einbauen. Das ist mir zuviel Gewurschtel, da nehme ich lieber nen Handy-Datenkabel für 1 EUR aus der Bucht. Trotzdem danke für die Infos.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1825#msg1825)

---

<a id="msg1826"></a>

## 94. glotzi · 28. Jan 2011, 13:10

> **Zitat von: phaidros am 28. Jan 2011, 13:03**
>
> Das freut zu hören. Die Probleme sind registriert. Mal sehen, ob sich was machen lässt.

Ähm , meinen Beitrag obe haste gesehen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1826#msg1826)

---

<a id="msg1827"></a>

## 95. stevie101 · 28. Jan 2011, 14:33

@glotzi

Du verwendest aber schon die Version aus dem git, oder ?
Bei den alten release Versionen hatte ich auch Probleme beim laden der Playlisten....

@phaidros

> **Zitat**
>
> Die werden einfach weggeworfen. Zur Zeit werden nur ca. 30 angezeigt. Ich dachte, keiner will durch 50 Ergebnisse scrollen. Lieber noch einen Buchstaben
> mehr eintippen um die Suche einzischränken ?

Das Problem ist, wenn mehr als 3 Buchstaben eingegeben werden, die Chance auf Resultate recht gering, oft gegen Null, wird. Möglicherweise liegt es an den 2sec, da die vip1710 nicht wirklich Power hat.

Gruss
Stefan

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1827#msg1827)

---

<a id="msg1828"></a>

## 96. glotzi · 28. Jan 2011, 14:35

> **Zitat von: stevie101 am 28. Jan 2011, 14:33**
>
> @glotzi
> Du verwendest aber schon die Version aus dem git, oder ?

jop

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1828#msg1828)

---

<a id="msg1829"></a>

## 97. phaidros · 29. Jan 2011, 01:48

> **Zitat von: glotzi am 28. Jan 2011, 13:10**
>
> > **Zitat von: phaidros am 28. Jan 2011, 13:03**
> >
> > Das freut zu hören. Die Probleme sind registriert. Mal sehen, ob sich was machen lässt.
>
>
>
> Ähm , meinen Beitrag obe haste gesehen?

Ja, habe ich. Ich benutze gar keine Shoutcasts (was isn das fürn neumodischer Kram?).
Kannst du mir mal eine ganz kurze Anleitung für Dummies geben, wie ich in MPD einen Shoutcast einrichte und wenn ja einen, wo das Problem auftritt?
Dann werde ich es mal testen.

Auch über die anderen Probleme muss ich erst mal nachdenken.
Bisher war ich davon ausgegangen, dass mpdtool auf halbwegs leistungsfähiger Hardware läuft und deshalb Resourcen ohne Ende nutzen kann.
Ist bei mir eine S100 und die hat keine Probleme. Die Vip1710 ist das 1 Euro Teil von Pollin, oder?
Ich weiß noch nicht, was sich da machen lässt. Irgendeiner muss die Arbeit des Aussortierens der Dateinamen und so ja machen. Entweder Betty oder mpdtool.
Und Betty ist nun wirklich nicht so leistungsfähig.
Das eigentliche Problem ist aber, dass MPD auf Suchanfragen unglaublich viel Rümpel schickt, den man gar nicht haben
will. Ich hätte am liebsten 2 Zusatz-Kommandos: count-find liefert nur die Anzahl der gefundenen Ergebnisse zurück, nicht die Ergebnisse selbst und
find-max liefert nur die ersten n Ergebnisse. Das wäre schön praktisch. Da es das nicht gibt., muss man basteln.

Ich könnte einfach bei den Suchbefehlen die Wartezeit der Betty auf 5 Sekunden (oder 10) hochsetzen, möchte das aber nicht.
Betty kann keine weiteren Befehle senden, solange sie auf Antworten des alten Befehls wartet.
Wenn also die Wartezeit zu hoch ist, wird das ganze Ding träge.
Das muss man irgendwie sauber anders lösen.

Das dauert ein Weilchen.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1829#msg1829)

---

<a id="msg1830"></a>

## 98. stevie101 · 29. Jan 2011, 10:21

Hab mal mit der Wartezeit auf Betty und mpdtool Seite herumgespielt (aktuell bei 15sec), jetzt kommen vernünftige Ergebnisse. Muss ich aber noch weiter testen.
Ich denke, wenn man vermeidet, dass nach einer Suche und Suchmaske leer, nach "" gesucht wird,  MPD nicht unnütz belastet ist.
Eigentlich müsste dafür doch nur user_model.search_string = NULL gesetzt werden, nachdem AV gedrückt wurde (wie bei Initialisierung). Wo ist nur die Stelle im Code der Betty ?

Gruss
Stefan

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1830#msg1830)

---

<a id="msg1832"></a>

## 99. phaidros · 29. Jan 2011, 13:01

> **Zitat**
>
> Eigentlich müsste dafür doch nur user_model.search_string = NULL gesetzt werden, nachdem AV gedrückt wurde (wie bei Initialisierung). Wo ist nur die Stelle im Code der Betty ?

Ich würde das an folgender Stelle machen:
File model.c, Funktion model_needs_action()

   /* Something to search ? */
   if (user_model.search_string != NULL){
      req->str = mpd_get_search_string();
      return SEARCH_CMD;
   };

erstzen durch

   /* Something to search ? */
   if ( (user_model.search_string != NULL) && (*user_model.search_string != '\0') ){
      req->str = mpd_get_search_string();
      return SEARCH_CMD;
   };

Dann sucht Betty nie nach leeren Strings.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1832#msg1832)

---

<a id="msg1833"></a>

## 100. glotzi · 29. Jan 2011, 13:57

> **Zitat von: phaidros am 29. Jan 2011, 01:48**
>
> Ja, habe ich. Ich benutze gar keine Shoutcasts (was isn das fürn neumodischer Kram?).
> Kannst du mir mal eine ganz kurze Anleitung für Dummies geben, wie ich in MPD einen Shoutcast einrichte und wenn ja einen, wo das Problem auftritt?
> Dann werde ich es mal testen.

Ich meine ganz normales Internetradio. Das Problem tritt bei allen Radiostreams auf, da der mpd ständig die Track-Infos neu schickt. Man kann das schön beim mpdtool sehen. Ich hab mal eine Playlist angehängt. Internet-radio geht beim mpd nur via Playlist.

> **Zitat von: phaidros am 29. Jan 2011, 01:48**
>
> Ich hätte am liebsten 2 Zusatz-Kommandos: count-find liefert nur die Anzahl der gefundenen Ergebnisse zurück, nicht die Ergebnisse selbst und
> find-max liefert nur die ersten n Ergebnisse. Das wäre schön praktisch. Da es das nicht gibt., muss man basteln.

MPD patchen und einen Feature Request einreichen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1833#msg1833)

---

<a id="msg1834"></a>

## 101. phaidros · 29. Jan 2011, 14:19

> **Zitat**
>
> Ich hab mal eine Playlist angehängt.

Ja, danke. Jetzt kann ich es nachvollziehen. Das Problem ist, dass MPD eine Gesamtlänge von 0 schickt. Das soll wohl soviel heißen wie unbekannt.
Außerdem werden Titel und Artist nicht getrennt geschickt. Sehr seltsam. Statt dessen gibt es einen "Name:" Eintrag, der wohl der Radiosender ist.
Bei einer Gesamtlänge von 0 denkt Betty immer, der Song ist gleich zu Ende und es kommt ein neuer. Da werden dann ständig Anfragen hin- und hergeschickt und der
Bildschirmtext wird aktualisiert. Das werde ich bei Gelegenheit ändern!

> **Zitat**
>
> MPD patchen und einen Feature Request einreichen?

Im Prinzip völlig richtig. Ich habe nur etwas Schiss, da eine neue Baustelle aufzumachen. Bei MPD gäbe es meiner Meinung nach einiges zu patchen (damit es eben auf so
schwachen Clients wie Betty rund läuft), das könnte ein Fass ohne Boden werden. Vielleicht macht es ja jemand anders?

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1834#msg1834)

---

<a id="msg1835"></a>

## 102. stevie101 · 29. Jan 2011, 14:52

`if ( (user_model.search_string != NULL) && (*user_model.search_string != '\0') ){`

Danke, hatte es ohne "*" vor user_model... implementiert - jetzt geht's.

Übrigens sehr cool, dass der code so schön kommentiert ist. Selbst jemand wie ich, der nicht C programmieren kann, bekommt ne Idee.

Gruss
Stefan

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1835#msg1835)

---

<a id="msg1836"></a>

## 103. phaidros · 29. Jan 2011, 15:41

> **Zitat**
>
> Danke, hatte es ohne "*" vor user_model... implementiert - jetzt geht's.

Ist jetzt auch in der neuesten git-hub Version drin. Es macht ja wirklich nur selten Sinn, nach gar nichts (bzw. allem) zu suchen.
Hatte das nur so reingenommen, weil Amarok das auch so macht und es da wirklich funktioniert. Wenn man die Suchmaske löscht,
bekommt man einfach die komplette Musiksammlung zu sehen und kann darin rumscrollen. Nur Betty wird es nie schaffen, die ganze Sammlung anzuzeigen.
Ich hatte ursprünglich mal über eine Art "browse" Modus nachgedacht, wo man Ordner sieht, die man öffnen kann, aber letztendlich ist das Suchen doch
schneller zu implementieren. Und wenn man nur irgendwie Teile des Gesuchten kennt, findet man es ja auch ganz gut.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1836#msg1836)

---

<a id="msg1842"></a>

## 104. glotzi · 31. Jan 2011, 17:28

> **Zitat von: phaidros am 29. Jan 2011, 15:41**
>
> Ist jetzt auch in der neuesten git-hub Version drin.

Danke für die neue Version, der Refresh des Displays ist nun auch bei RadioStreams ok.

Ich habe aber immer noch das Problem, dass die OK Taste nicht funktioniert. Ich habe sogar die Betty gewechselt, um einen Hardware Defekt auszuschliessen.
Wenn ich in Ansicht Nr 1. "Current Playlists" zu einer Playlist navigiere und dort OK drücke, sollte doch der laufende Song abgebrochen, die aktuelle Playlist gelöscht, die ausgewählte geladen und Play ausgeführt werden. So stehts zumindest im Sourcecode.

Bei mir passiert nichts. 

Zum Thema Performance an der Vip 1710: mpdtool hat normalerweise ein Sysload von 8-10%, bei Suchen max. 30%, also eigentlich ausreichend. Bei mir läuft aber der mpd nicht auf der Vip, sondern auf meinem Debian-Server und der liefert den Sound via EsoundD an die VIP. Evtl. ist das für den ein oder anderen auch eine Option.

@phaidros: wieso hast du eigentlich nicht die libmpdclient benutzt für die Kommunikation mit dem mpd?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1842#msg1842)

---

<a id="msg1843"></a>

## 105. phaidros · 31. Jan 2011, 20:34

> **Zitat**
>
> @phaidros: wieso hast du eigentlich nicht die libmpdclient benutzt für die Kommunikation mit dem mpd?

Die kannte ich nicht. 
Werde ich mir gleich mal anschauen. Ist aber jetzt vielleicht schon zu spät.

> **Zitat**
>
> Bei mir läuft aber der mpd nicht auf der Vip, sondern auf meinem Debian-Server und der liefert den Sound via EsoundD an die VIP.

Bin erleichtert das zu hören. Weil mpd auch noch auf der Kiste könnte knapp werden. Bei mir läuft MPD auf einem NAS-Server, wodurch sich manchmal
arge Verzögerungen ergeben, weil das NAS erst seine Platten hochfahren muss um Anfragen zu beantworten. MPD hält wohl seine Datenbank nicht im RAM.
Überhaupt, wieso braucht MPD ein paar Sekunden um seine Datenbank nach einem einfachen String zu durchsuchen ? Ein paar Millisekunden vielleicht, aber mehr nicht.
Na ja, es ist wie es ist.
Ich werde mal kucken, ob man noch an der Kommunikation etwas drehen kann, so dass die Last von mpdtool etwas zurück geht.

> **Zitat**
>
> Wenn ich in Ansicht Nr 1. "Current Playlists" zu einer Playlist navigiere und dort OK drücke, sollte doch der laufende Song abgebrochen, die aktuelle Playlist gelöscht, die ausgewählte geladen und Play ausgeführt werden. So stehts zumindest im Sourcecode.

"Current Playlists" gibt es nicht. Entweder "Current Playlist" oder "All playlists".
Das von dir beschriebene Verhalten sollte bei "All Playlists" gegeben sein. Bei mir tut es das auch. Das könnte auch ein Timing-Problem sein. Kannst du mal die Ausgabe von Betty auf der seriellen Schnittstelle mitlesen, während das passiert? Sendet Betty überhaupt irgendwas?
Und vielleicht parallel auch die Ausgabe von mpdtool (via stderr auf der Konsole) anschauen.

Die Bezeichnung der beiden Ansichten ist sicherlich noch zu ähnlich. Vielleicht "Current Playlist" in "Current Tracks" oder so ändern ?

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1843#msg1843)

---

<a id="msg1845"></a>

## 106. glotzi · 31. Jan 2011, 22:50

> **Zitat von: phaidros am 31. Jan 2011, 20:34**
>
> Die kannte ich nicht. 
> Werde ich mir gleich mal anschauen. Ist aber jetzt vielleicht schon zu spät.

Evtl. macht es die Wartung aber einfacher. Man muss ja nicht geleich alles umstellen, evtl nach und nach.

> **Zitat von: phaidros am 31. Jan 2011, 20:34**
>
> "Current Playlists" gibt es nicht. Entweder "Current Playlist" oder "All playlists".
> Das von dir beschriebene Verhalten sollte bei "All Playlists" gegeben sein. Bei mir tut es das auch. Das könnte auch ein Timing-Problem sein.

Sorry hatte die Namen der Screens nicht so genau im Kopf: ich meinte All playlists.

Was meinst Du mit Timing Problem? Das die Vip zu langsam ist? Ich habe den Scart auch mal an den Debian-Server gehangen, keine Veränderung.

> **Zitat von: phaidros am 31. Jan 2011, 20:34**
>
> Kannst du mal die Ausgabe von Betty auf der seriellen Schnittstelle mitlesen, während das passiert? Sendet Betty überhaupt irgendwas?
> Und vielleicht parallel auch die Ausgabe von mpdtool (via stderr auf der Konsole) anschauen.

Ich wusste gar nicht, dass auf seriellen Schnittstelle was rausgeschrieben wird. Guter Hinweis. Mit welchen Paramtern muss die konfiguriert werden? Mit 115200 8N1 sehe ich nur Müll.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1845#msg1845)

---

<a id="msg1846"></a>

## 107. jannis · 01. Feb 2011, 01:19

> **Zitat von: phaidros am 31. Jan 2011, 20:34**
>
> Bin erleichtert das zu hören. Weil mpd auch noch auf der Kiste könnte knapp werden. Bei mir läuft MPD auf einem NAS-Server, wodurch sich manchmal
> arge Verzögerungen ergeben, weil das NAS erst seine Platten hochfahren muss um Anfragen zu beantworten. MPD hält wohl seine Datenbank nicht im RAM.
> Überhaupt, wieso braucht MPD ein paar Sekunden um seine Datenbank nach einem einfachen String zu durchsuchen ? Ein paar Millisekunden vielleicht, aber mehr nicht.

MPD muss die Datenbank nicht cachen, das macht schon der linux kernel in seinem filesystem cache. Aber so groß ist diese Datei ja eh nicht.

Auch bei mir läuft mpd momentan auf ner S100, da ich den spdif ausgang von der vip immer noch nicht ans laufen bekommen hab. Ist wohl noch Neuland.

Obwohl ich über das Netzwerk auf meine Datenbank zugreife wird jegliche Operation nahezu ohne spürbare Verzögerung ausgeführt.
Auf dem Server (Dockstar mit USB platte) sind ca 150GB Musik und die Suchergebnisse kommen trotzdem immer sofort.

Wie siehts mit deinem RAM aus, biste vielleicht schon am swappen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1846#msg1846)

---

<a id="msg1847"></a>

## 108. phaidros · 01. Feb 2011, 05:55

> **Zitat**
>
> Ich wusste gar nicht, dass auf seriellen Schnittstelle was rausgeschrieben wird. Guter Hinweis. Mit welchen Paramtern muss die konfiguriert werden? Mit 115200 8N1 sehe ich nur Müll.

38400 8N1
Bei mir brauche ich nichts machen. Im Makefile gibt es das Target "resident". Ich rufe make resident auf, das flasht die Betty, macht einen Betty-Reset und zeigt anschließend die
Ausgaben der seriellen Schnittstelle an. Also nach dem Flashen Betty einfach am Programmer dran lassen.
Früher gab es tatsächlich keine Ausgaben auf der Seriellen, da ist ein Flag drin was die Ausgaben bei Release-Versionen unterdrückt,
aber ich habe es schon länger ausgeschaltet. Jetzt sollte jede Menge auf der Seriellen zu sehen sein.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1847#msg1847)

---

<a id="msg1848"></a>

## 109. glotzi · 01. Feb 2011, 09:03

> **Zitat von: jannis**
>
> Auch bei mir läuft mpd momentan auf ner S100, da ich den spdif ausgang von der vip immer noch nicht ans laufen bekommen hab. Ist wohl noch Neuland.

Nee, kein Neuland guck mal hier
[http://meta-lab.de/index.php/Musik_im_bytewerk](https://web.archive.org/web/2012/http://meta-lab.de/index.php/Musik_im_bytewerk)

> **Zitat von: phaidros am 01. Feb 2011, 05:55**
>
> 38400 8N1
> Bei mir brauche ich nichts machen. Im Makefile gibt es das Target "resident". Ich rufe make resident auf, das flasht die Betty, macht einen Betty-Reset und zeigt anschließend die
> Ausgaben der seriellen Schnittstelle an. Also nach dem Flashen Betty einfach am Programmer dran lassen.

Danke für den Hinweis, ich habe die Kabel nach dem flashen immer abgezogen. Wann öffnest Du dann EINT wieder?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1848#msg1848)

---

<a id="msg1852"></a>

## 110. stevie101 · 01. Feb 2011, 11:18

Zum Thema vip1710.
Aktuell läuft bei mir mpd, mpdtool, vdr und pyload auf dem Teil. Der Speicher ist mehr als am Anschlag, daher wird auf USB HD geswapped. Bezüglich CPU Auslastung sieht es gar nicht so dramatisch aus, da entweder nur MPD oder VDR etwas aktiv ausgeben. Dockstar als Server wäre eine Alternative, habe ich aber noch nicht, daher läuft die VIP 24hrs/d. MPD hat ca. 500 GB an Daten zu verwalten.

Alles in allem läuft das Ganze relativ gut, auf Suchanfragen muss man halt etwas warten. Um die Anfragen etwas gezielter auszulösen, hab ich versucht die Betty sw dahingehend zu modifizieren, erst nach dem dritten Zeichen die Anfrage an MPD zu schicken. Ist wohl nicht korrekt umgesetzt (Anfragen werden geschickt, allerdings inkorrekte bis zum 4ten Zeichen), hilft aber. Für low power Systeme wäre es aus meiner Sicht am besten, die Suchfunktion so zu ändern, dass erst auf "OK" die Suche Richtung MPD geschickt würde ("D" könnte die add Funktion übernehmen). Hatte jetzt häufiger den Fall, dass die Suche bereits ausgeführt wurde, obwohl die Eingabe noch nicht vollständig war (bin kein SMS Tipper). Workaround : raus dem Suchmenu, wieder rein, dann wurde umgehend der vollständige String geschickt.
Wenn die aktuelle Implementierung bei euch zuverlässlich und schnell funktioniert, muss ich selbst schauen, wie das umzusetzen wäre.

Desweiteren fiel mir auf, wenn sehr viele Resultate zurückgegeben werden (MPD schickt auch immer "OK"), die Suchanfrage ständig erneut herausgeschickt wird (kein timeout), trotzdem keine Resultate übernommen werden.

Gruss

Stefan

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1852#msg1852)

---

<a id="msg1860"></a>

## 111. glotzi · 01. Feb 2011, 21:41

> **Zitat von: glotzi am 31. Jan 2011, 17:28**
>
> Ich habe aber immer noch das Problem, dass die OK Taste nicht funktioniert. Ich habe sogar die Betty gewechselt, um einen Hardware Defekt auszuschliessen.
> Wenn ich in Ansicht Nr 1. "Current Playlists" zu einer Playlist navigiere und dort OK drücke, sollte doch der laufende Song abgebrochen, die aktuelle Playlist gelöscht, die ausgewählte geladen und Play ausgeführt werden. So stehts zumindest im Sourcecode.
>
> Bei mir passiert nichts. 

So, habe das Problem gefunden: es liegt an der Toolchain. Ich habe die ganze Zeit CodeSourcery Fall2010 Lite benutzt (gcc 4.5.1). Mit boop hatte ich auch ganz komische Probleme. Daher hatte ich die hier probiert:

[https://github.com/esden/summon-arm-toolchain](https://web.archive.org/web/2012/https://github.com/esden/summon-arm-toolchain)

Seitdem sind die Probleme mit der OK Taste weg.

Nur der Build klappt nicht mehr out-of-the-box. In fonty.c wird wohl types.h nicht gefunden und dann fehlt u_int16_t. Habe den typedef als Workaround dann selber gemacht. Dann läuft er durch.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1860#msg1860)

---

<a id="msg1861"></a>

## 112. phaidros · 02. Feb 2011, 00:41

> **Zitat**
>
> In fonty.c wird wohl types.h nicht gefunden und dann fehlt u_int16_t.

Ja, den Blödsinn habe ich verzapft. Das muss natürlich uint16_t heißen.
Ist korrigiert. Keine Ahnung warum das bei mir überhaupt kompiliert hat!

Gruß
Phaidros

P.S.:
> **Zitat**
>
> Wann öffnest Du dann EINT wieder?

Keine Ahnung. Ich habe wohl vor einiger Zeit mal lpctool modifiziert, aber jetzt schon wieder komplett vergessen.
Hier nahe dem Ende von meinem lpctool:
   
   `setBaud(38400);
 setRTS(0); // Release boot loader enable line, needed for normal start.
 setDTR(1); // Issue a RESET
 usleep(500000);
 setDTR(0);

 Terminal();
end:
  . . .`

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1861#msg1861)

---

<a id="msg1862"></a>

## 113. phaidros · 02. Feb 2011, 01:12

> **Zitat**
>
> Für low power Systeme wäre es aus meiner Sicht am besten, die Suchfunktion so zu ändern, dass erst auf "OK" die Suche Richtung MPD geschickt würde

Ich möchte die Tastenbelegung nicht unnötig ändern. Version 1.2.3 auf github hat die blaue Taste definiert als "Jetzt suchen".
Und für low power Systeme sollte man in muc/Makefile die Zeile "EXTRAFLAGS = -D SLOW_HOST" reinnehmen (Kommentarzeichen entfernen).
Dann make clean und make. Jetzt macht Betty keine automatische Suche mehr, sondern wartet auf die blaue Taste.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1862#msg1862)

---

<a id="msg1863"></a>

## 114. stevie101 · 02. Feb 2011, 09:36

> **Zitat**
>
> Und für low power Systeme sollte man in muc/Makefile die Zeile "EXTRAFLAGS = -D SLOW_HOST" reinnehmen (Kommentarzeichen entfernen).

Vielen Dank dafür, werde ich heute abend sofort probieren.

Gruss
Stefan

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1863#msg1863)

---

<a id="msg1864"></a>

## 115. glotzi · 02. Feb 2011, 17:32

> **Zitat von: phaidros am 02. Feb 2011, 00:41**
>
> > **Zitat**
> >
> > In fonty.c wird wohl types.h nicht gefunden und dann fehlt u_int16_t.
>
>
> Ja, den Blödsinn habe ich verzapft. Das muss natürlich uint16_t heißen.
> Ist korrigiert. Keine Ahnung warum das bei mir überhaupt kompiliert hat!

Du hast nicht alle Stellen erwischt. In
 `/muc/display/fonts/misc_font.h
/muc/display/fonts/pearl_font.h
/muc/display/fonts/smooth_font.h`
sind auch noch u_int16_t. Wenn ich die durch uint16_t ersetze läuft der Build durch.

Ich habe aber noch ein ganz anderes Problem entdeckt: Ich habe gestern abend die Betty nicht in die Ladeschale gesteckt, heute morgen waren dann die Akkus leer, obwohl die ganz sicher gestern Abend voll waren.

Der Scart-Adapter ist nicht den ganzen Tag an, sondern nur dann wenn ich Musik hören will. Kann es sein das McBetty die ganze Zeit versucht den Adapter zu erreichen und dabei den Akku leer lutscht? In boop gibt es einen Powersave Mode, sowas habe ich der Source von McBetty nicht gefunden.

Es wäre schön, wenn man mit einem Druck auf den Power-Knopf die Betty schlafen legen könnte: Display aus, keine Zugriffe auf den Scart-Adapter, Cpu in den Halt schicken (wie bei Boop).

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1864#msg1864)

---

<a id="msg1865"></a>

## 116. phaidros · 03. Feb 2011, 04:51

> **Zitat**
>
> Du hast nicht alle Stellen erwischt.

Die "...font.h" Dateien werden automatisch neu generiert, wenn man die Fonts ändert. Jetzt werden sie allerdings mit dem richtigen uint16_t generiert.
Das Problem ist eher, dass make clean die Dinger nicht löscht. Das Makefile ist aber aus altem Boop-Code übernommen und ich verstehe nur die
Hälfte von dem, was da passiert. Rekursives Make ist böse!! Sollte ich auch noch mal ändern.

> **Zitat**
>
> Kann es sein das McBetty die ganze Zeit versucht den Adapter zu erreichen und dabei den Akku leer lutscht?

Definitiv ja!

> **Zitat**
>
> Es wäre schön, wenn man mit einem Druck auf den Power-Knopf die Betty schlafen legen könnte: Display aus, keine Zugriffe auf den Scart-Adapter, Cpu in den Halt schicken (wie bei Boop).

Das wäre doch zu einfach. 

Na gut, ernsthafte Antwort: Ist geplant. Allerdings würde ich gerne Betty selber entscheiden lassen, dass nichts mehr zu tun ist. Nur bei Tastendruck wacht sie wieder auf.
Das ermöglicht viel mehr Schlafphasen. Dazu muss ich aber noch einiges an dem Micro-Kernel umstrukturieren. Kann also noch dauern.
Bis dahin wäre die Power-Taste ganz gut.
Bei Gelegenheit schaue ich mal wie Boop das macht.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1865#msg1865)

---

<a id="msg1872"></a>

## 117. gerdigerdi · 13. Feb 2011, 15:15

hallöchen,
ich hätte da noch 2 kleine Anregungen.
wenn die Wiedergabe pausiert oder gestoppt, die Batterie alle ist und das Kind endlich schäft, passiert regelmäßig ein Unglück wenn die Betty in der Ladeschale landet:
Die Wiedergabe wird wie durch Geisterhand gestartet. Hat besonders in diesem Fall unangenehme Nebenwirkungen ;/

Wäre es ein großer Aufwand, auch in den Suchergebnissen Seitenweise Blattern zu können?
Und hast du Einfluss auch die Reihenfolge der Ergebnisse? Z.B. Suche "air" ergibt zahlreiche Ergebnisse, das was 100%ig übereinstimmt ("Air")  ist bei mir erst auf der 2. Seite.

Du merkst schon an den Wünschen, dass eigentlich alles geht und nur noch Luxusschnickschnack vermisst wird
Apropos Luxusschnickschnack eine Batterieanzeige könnte auch nicht schaden

Lass dich nicht hetzen! Alles nur Anregungen falls dir mal langweilig sein sollte

Grüße
Gerdi

PS: Ich hatte schon ewig keine Abstürze mehr Löft superstabil!

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1872#msg1872)

---

<a id="msg1873"></a>

## 118. glotzi · 13. Feb 2011, 21:07

Hallo zusammen,

das Problem mit den Geisterstarts kann ich bestätigen, ist mir auch schon unangenehm aufgefallen.  Ansonsten läuft alles ohne Probleme, Abstürze hatte ich noch keine. Auch der Betrieb an der Motorola VIP funktioniert gut.   

Batteriesysmbol und Powermanagement wären halt noch schön, aber das hatte ich ja oben auch schon mal geschrieben.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1873#msg1873)

---

<a id="msg1874"></a>

## 119. phaidros · 14. Feb 2011, 01:27

> **Zitat**
>
> ... passiert regelmäßig ein Unglück wenn die Betty in der Ladeschale landet:

Betty macht einen RESET. Ob das so gewollt ist oder nicht kann ich nicht sagen. Passiert auch nicht immer.
Dass dann die Musik spielt, kann man schnell ändern:
in Datei model.c ganz unten Funktion model_init():   user_model.state = PLAY;
ändern in user_model.state = STOP;
Die Idee war irgendwie, wenn es zu einem unbeabsichtigten RESET kommt, soll die Musik nicht aufhören.
Aber das mit dem Baby überzeugt. Werde ich demnächst mal einchecken.

> **Zitat**
>
> Wäre es ein großer Aufwand, auch in den Suchergebnissen Seitenweise Blattern zu können?

Eigentlich überhaupt nicht, ABER die dafür sonst immer benutzten Cursor-Tasten (links/rechts) sind schon belegt, da sie in der Suchmaske den Cursor bewegen.
Wie macht man das konsistent durch alle Bildschirme ?

> **Zitat**
>
> eine Batterieanzeige könnte auch nicht schaden

Ja, ist in Arbeit. Dauert aber noch ein Weilchen (auch die PowerOff Sache), da ich gerade ein anderes Projekt fertig stellen will.

> **Zitat**
>
> hast du Einfluss auch die Reihenfolge der Ergebnisse?

Nur begrenzt. MPD liefert die in irgendeiner Reihenfolge.  mpdtool speichert die zwischen und könnte sie auch sortiert ausgeben, aber wie / wonach sollte ich die sortieren? 

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1874#msg1874)

---

<a id="msg1883"></a>

## 120. gerdigerdi · 04. Mär 2011, 09:44

> **Zitat**
>
> Wäre es ein großer Aufwand, auch in den Suchergebnissen Seitenweise Blattern zu können?
> Eigentlich überhaupt nicht, ABER die dafür sonst immer benutzten Cursor-Tasten (links/rechts) sind schon belegt, da sie in der Suchmaske den Cursor bewegen.
> Wie macht man das konsistent durch alle Bildschirme ?

Wenn die Ergebnisse der Suche vorliegen könnte durch einmaliges drücken nach unten (Selektierung des ersten Suchergebnisses) die Seitenweise-Blättern Steuerung aktiviert werden - durch Selektierung der Suchmaske könnte diese wieder deaktiviert werden. Das wäre zumindest für mich intuitiv bedienbar

> **Zitat**
>
> ... passiert regelmäßig ein Unglück wenn die Betty in der Ladeschale landet:

Könnte der Status vom MPD nicht eingelesen/übernommen werden?

Gruß
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1883#msg1883)

---

<a id="msg1906"></a>

## 121. phaidros · 21. Mär 2011, 03:04

> **Zitat**
>
> Wenn die Ergebnisse der Suche vorliegen könnte durch einmaliges drücken nach unten (Selektierung des ersten Suchergebnisses) die Seitenweise-Blättern Steuerung aktiviert werden - durch Selektierung der Suchmaske könnte diese wieder deaktiviert werden. Das wäre zumindest für mich intuitiv bedienbar

Ja, das könnte gehen.
Ich habe eigentlich keine Ahnung wie man ein User-Interface gestaltet und bin mir noch nicht sicher. Die Logik bei deiner Lösung ist ein bißchen anders als vorher. Man braucht einen Tastendruck mehr als vorher, um die Suchmaske zu verlassen.
Eigentlich war die Idee, die Anzahl der Suchergebnisse durch Eingabe weiterer Buchstaben so weit zu verringern, dass nur noch wenige Titel angezeigt werden. Deswegen sträube ich mich innerlich ein bißchen gegen ein seitenweises Blättern. Ist einfach irrational, ich weiß.

Im Moment ist für McBetty sowieso keine Zeit, brauche noch ca. 2 Wochen für was anderes. Nächste Version also vorraussichtlich erst im April.

Gruß
Phaidros

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1906#msg1906)

---

<a id="msg1912"></a>

## 122. gerdigerdi · 27. Mär 2011, 19:53

> **Zitat**
>
> Eigentlich war die Idee, die Anzahl der Suchergebnisse durch Eingabe weiterer Buchstaben so weit zu verringern, dass nur noch wenige Titel angezeigt werden.

Funktionier auch fast immer. Erkannt habe ich die vorhandene Problematik erst nach der ersten Suche nach "air". Obwohl der volle Name eingegeben ist erscheint das gewünschte Suchergebnis ("Air" und nichts mehr) erst auf der 2. Seite. Deshalb auch die Anfrage nach der Möglichkeit der Sortierung der Suchergebnisse. Bei mir erscheinen zahlreiche Ergebnisse , die zwar "air" enthalten vor dem 100%igen Treffer "Air". So blieben für mich nur die Lösungen: Sortieren oder seitenweise Blättern.
Perfekt wäre es, wenn die Sortierung der Suchergebnisse bereist optimiert vom mpd geliefert würden. Wer regt das mal an?
Eventuell gibt es ja noch ne Möglichkeit

> **Zitat**
>
> Im Moment ist für McBetty sowieso keine Zeit, brauche noch ca. 2 Wochen für was anderes. Nächste Version also vorraussichtlich erst im April.

Nimm dir nur die Zeit, die du brauchst. So wie ich das mitbekommen habe legst du, wenn du loslegst, immer gleich einen Programmiermarathon hin
Aber schön zu hören das weitere Updates geplant sind.

Gruß
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1912#msg1912)

---

<a id="msg1922"></a>

## 123. antonia · 11. Mai 2011, 19:55

Hallo
ich bin absoluter Anfänger und würde auch gern die Betty zur Steuerung der vip verwenden. Ich kann leider nirgends ein scartadapter kaufen. Deshab meine Frage, ob man eine zweite betty als Scartadapter missbrauchen kann ?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1922#msg1922)

---

<a id="msg1923"></a>

## 124. gerdigerdi · 14. Mai 2011, 12:22

Normalerweise sind die Scartadapter bei der Betty dabei!
Der IP-Adapter ist Mangelware - wird zur Steuerung des MPD aber auch nicht gebraucht.
Ein Freund von mir hat noch Bettys mit Scartadapter (denk Größenordnung 10e) - Ich könnte Kontakt herstellen - Bitte PM an mich.

Gruß
Gerdi

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1923#msg1923)

---

<a id="msg1924"></a>

## 125. ino · 19. Mai 2011, 18:11

Hallo Forum Gemeinde

Habe bei Pollin.de die  MOTOROLA VIP1710 Box für 5€ gesehen. Damit wäre ja ein super preiswerter MPD
realiesierbar. Wäre dieser nicht eine optimale Ergänzung für die Betty als MDP Client ?

Es läuft auch schon ein Internetradio darauf und als VDR Client wird auch gebastelt!

Wäre nett mal eure Meinungen zu hören bzw. zu lesen!

Grüße Ino

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1924#msg1924)

---

<a id="msg1925"></a>

## 126. glotzi · 19. Mai 2011, 19:40

> **Zitat von: ino am 19. Mai 2011, 18:11**
>
> Habe bei Pollin.de die  MOTOROLA VIP1710 Box für 5€ gesehen. Damit wäre ja ein super preiswerter MPD
> realiesierbar. Wäre dieser nicht eine optimale Ergänzung für die Betty als MDP Client ?

Das ist jetzt doch aber wirklich ne olle Kamelle. In dem Beitrag hier steht doch auch schon was zu dem Thema. Tante Google hätte denn diesen:

[http://www.open7x0.org/arena/showthread.php?tid=2594&pid=22167#pid22167](https://web.archive.org/web/2012/http://www.open7x0.org/arena/showthread.php?tid=2594&pid=22167#pid22167)

Link hervorgebracht. 

Was genau ist nun deine Frage? BTW solltest du dich beeilen der Bestand bei Pollin schrumpft rapide.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1925#msg1925)

---

<a id="msg1952"></a>

## 127. gunnar · 16. Aug 2011, 06:58

Hallo zusammen,

ich habe versucht, mit dem in McBetty enthaltenen Boop die SCART Firmware zu flashen. Das scheitere aber schon daran, dass dieses Boop auf meiner Betty (und auch auf anderen) nicht läuft. Beim Einlegen der Batterien geht die Hintergrundbeleuchtung an und dann geht gar nichts mehr. Ich habe von dem Problem in diesem Thread gelesen, aber bei mir geht es auch trotz mehrmaligen Versuchens nicht.
Das normale Boop funktioniert aber. Und so habe ich scart_image.h aus dem McBetty Archiv ins tools Verzeichnis des Original-Boop kopiert. Damit konnte ich dann flashen... genau bis zur Adresse 0xe800. Ein kurzer Blick ins Datenblatt verriet mir, das diese Adresse im Booloader Bereich liegt. Das original-boop löscht diesen Bereich aber vor der Programmierung absichtlich nicht um den Bootloader zu erhalten. Das McBetty Boop löscht aber das ganze Flash, da der Bootloader im McBetty Scart-Image enthalten ist.
Um das original-Boop zum flashen des McBetty Scart-Images nehmen zu können muss man diese kleine Änderung an scart-icp.c machen:
 `-            /* only erase first 7 sectors, not all! */
-            for (i=0; i<7; i++)
+            /* erase all 8 sectors, including custom boot loader! */
+            for (i=0; i<8; i++)`

Der patch dazu hängt an. Vielleicht hilft dieser Hinweis ja dem einen oder anderen, der das gleiche Problem hat.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1952#msg1952)

---

<a id="msg1954"></a>

## 128. glotzi · 16. Aug 2011, 07:40

Über das Problem bin ich auch gestolpert. Ich habe dann einfach das Boop benutzt das bei McBetty dabei war. Damit gehts auch.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1954#msg1954)

---

<a id="msg1955"></a>

## 129. antonia · 19. Aug 2011, 23:46

Ich habe auch versucht das in mcBetty enthaltene boop zu flashen. Das hat auch nicht funktioniert. Nach dem Einlegen der Batterien hat auch wie schon beschrieben nur das Display kurz geleuchtet.
Ich habe als Toolchain Codesourcery Version 4.5.2 verwendet. Dann habe ich die Version 4.4.1 verwendet. Zusätzlich habe ich im makefile die Zeile
OPTFLAGS = -Os
durch
OPTFLAGS = -O2
ersetzt.
Das damit kompilierte boop funktioniert. Ich konnte damit sogar das scart-Adapter programmieren.

Grüße antonia

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1955#msg1955)

---

<a id="msg1967"></a>

## 130. gunnar · 07. Nov 2011, 14:04

Hallo Horst,

das, was momentan in Git eingecheckt ist, lässt sich nicht kompilieren. Ich habe hier einen kleinen Patch dafür.
Wäre nett wenn Du den einbaust.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1967#msg1967)

---

<a id="msg1973"></a>

## 131. glotzi · 24. Nov 2011, 09:12

Moin,

ich habe 2 Futro's S300 mit jeweils 1 Scart Adapter und McBetty im DG und EG stehen. Dummerweise ist der Empfang der Betty's so gut, dass er durch 2 Etagen geht, was in diesem Fall aber gar nicht gewünscht ist.

Weiß jemand, ob man den Kanal oder die Frequenz, mit dem der Scartadapter mit der Betty kommuniziert, konfiguriert werden kann? Oder gibts evtl. eine andere Möglichkeit eine Betty einem bestimmten Scartadapter zuzuordnen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1973#msg1973)

---

<a id="msg1974"></a>

## 132. glotzi · 24. Nov 2011, 20:31

Ok, ich antworte mir mal selbst: man kann den Channel auf dem der CC1100 sendet/emfängt ändern. Dazu editiert man jeweils im Verzeichnis muc und scart_image die Datei smartrf_CC1100.h und editiert:

#define SMARTRF_SETTING_CHANNR     0x06

Dann 2x neu flashen und alles wird gut.

[Permalink](http://bettyhacks.com/forum/index.php?topic=220.msg1974#msg1974)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
