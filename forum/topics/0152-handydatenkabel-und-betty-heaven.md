---
title: "Handydatenkabel und Betty Heaven"
topic_id: 152
board: "Hardware"
board_id: 5
posts: 7
first_post: "30. Jun 2008, 19:56"
last_post: "19. Feb 2009, 12:30"
authors: ["Gentoo07", "R-M-N", "Trekinfo", "nitpicker", "teufel2k"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=152.0"
---

# Handydatenkabel und Betty Heaven

[← Hardware](../boards/05-hardware.md) · Thema 152 · 7 Beiträge · 30. Jun 2008, 19:56 – 19. Feb 2009, 12:30

Beteiligt: Gentoo07, R-M-N, Trekinfo, nitpicker, teufel2k

---

<a id="msg1069"></a>

## 1. teufel2k · 30. Jun 2008, 19:56

Hallo Betty-Gemeinde!

Ich habe mir ein Datenkabel auf einem alten Ericsson T28 Datenkabel gebastelt. Leider bekomme ich es nicht hin damit die Betty Firmware zu Backupen oder zu flashen.

- Der Bootloader Modus scheint zu funktionieren! Wenn ich nur die Reset Leitung auf GND lege, dann startet die Betty neu und wenn ich davor schon die Bootloader leitung auf GND gelegt habe, dann erlischt der Bildschirm und ich hoffe die Betty ist im richtigen Modus.

- Wenn ich nur ein Backup ziehen will, muss die Betty dann auch im Bootloader Modus sein?

- Wenn ich allerdings Flashen oder Backupen will (egal ob mit oder ohne Bootloader) kommt von Betty Heaven nur ein:
> **Zitat**
>
> Starte Backup...
> RX: Timeout
> Synchronisation gescheitert.

- Die Kommunikation mit der Betty scheint aber zu stehen, denn wenn ich mir per putty die serielle Konsole anzeigen lasse und die Betty per Reset auf GND neustarte erscheinten dort einige Hyroglyphen:

> **Zitat**
>
> pOO±<Õÿaþ·ÿÿ¾s'ÏùÆÊþßâßÝßßßßû^âý

Wenn ich jetzt noch Tasten auf der Betty drücke, dann erscheinen noch weitere Hyroglyphen:
> **Zitat**
>
> ¥Ù±×ßý÷ßsqþ¥ÙÐÓÁÁþÊßÿWÐÓÁÁÿÊÖÍ'Ó

Edit: Nachdem ich im Putty die Datenrate von 9600 auf 115200 angehoben habe kann man nun auch den Bootlog in Klartext und Farbe lesen. Leider hilft das nicht beim Flashen! Auch nicht wenn ich die Datenrate im Gerätemanager anpasse! :-(

Eigentlich will ich aus meiner Betty hauptsächlich eine Uni-FB machen (und für die zukunft hoffen, dass das zusammenspiel zwischen Neutrino und Betty ausgebaut wird wie z.B. EPG & Co auf der Betty).

Vielleicht kann mir ja wer helfen!

Danke,
teufel2k

P.S. Ich benutze Vista x64, kompatibilitäts Modus brachte nichts und ein kurzer Test des Tools lpctool auch nicht. Als Admin habe ich Betty-Heaven auch schon gestartet!

*Last Edit : 30. Jun 2008, 23:16 by teufel2k*

[Permalink](http://bettyhacks.com/forum/index.php?topic=152.msg1069#msg1069)

---

<a id="msg1070"></a>

## 2. R-M-N · 05. Jul 2008, 11:33

Hi,

Ich habe grad ein ähnliches Problem. Mein Handydatenkabel scheint ein leicht verfälschtes echo zurückzugeben, was Betty Heaven nicht versteht.
Kannst du leicht rausfinden, indem du im terminal tasten auf der pc tastatur drückst, wenn dann zeichen kommen hast du eine echo vom pegelwandler. Am besten nur mit dem datenkabel ohne betty testen

> **Zitat**
>
> Starte Backup...
> Synchronisation gescheitert.

`Request: 05.07.2008 12:27:05.59364 (+9.7031 seconds)

 3F                                                ?               

Answer: 05.07.2008 12:27:05.59364 (+0.0000 seconds)

 BF 53 79 6E 63 68 72 6F 6E 69 7A 65 64 0D 0A      ¿Synchronized..`

*Last Edit : 05. Jul 2008, 11:48 by R-M-N*

[Permalink](http://bettyhacks.com/forum/index.php?topic=152.msg1070#msg1070)

---

<a id="msg1280"></a>

## 3. nitpicker · 03. Feb 2009, 01:07

Genau dieses Problem hatte ich mit meinem Siemens-Datenkabel auch. Es war ein no-name Kabel RS-232 auf Lumberg (alt). Ich vermute das Problem hängt damit zusammen dass in den Siemens Handys wohl noch Pullup-Widerstände an den Datenleitungen hängen - also wurden die in der Schaltung des Pegelwandlers eingespart, was dieses unangenehme Verhalten verursacht.

Lösung bei mir: ein 4.7 kOhm-Widerstand zwischen 3.3V und TX am Stecker. Damit war der Spuk verschwunden.

[Permalink](http://bettyhacks.com/forum/index.php?topic=152.msg1280#msg1280)

---

<a id="msg1306"></a>

## 4. Trekinfo · 18. Feb 2009, 14:28

Moin. the same procedure

Ich habe hier ein altes Siemens Datenkabel R232 benutzt. Das selbe Schema.
Im Hyperterminal bei 115k ist alles OK. Komunikation findet statt.
Mit Betty Heaven läuft gar nichts.

Ich habe sogar versucht den RS232 Adapter mit einem 5V Netzteil anstatt der 3.3V der Betty auf die Sprünge zu helfen aber pustekuchen es tut sich nichts.

Immer Timeout.

Mann, das kann doch nicht so schlimm sein diese (zensiert) Firmware aufzuspielen 

Gruß Trekinfo

[Permalink](http://bettyhacks.com/forum/index.php?topic=152.msg1306#msg1306)

---

<a id="msg1308"></a>

## 5. Gentoo07 · 19. Feb 2009, 00:16

@Trekinfo: Hast du denn auch den Lösungsansatz von nitpicker ausprobiert? (siehe posting über deinem)

Das klingt sehr plausibel als Lösung für die vereinzelt (und dann oft mit mehreren Kabeln) auftretenden Probleme da die Kabel ja von extrem verschiedenen Herstellern stammen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=152.msg1308#msg1308)

---

<a id="msg1309"></a>

## 6. Trekinfo · 19. Feb 2009, 08:40

@nitpicker:

Mann verleiht dem Mann einen Betty-Orden, es funzt !

THX

[Permalink](http://bettyhacks.com/forum/index.php?topic=152.msg1309#msg1309)

---

<a id="msg1310"></a>

## 7. Gentoo07 · 19. Feb 2009, 12:30

Siehst..war doch gar nicht so schlimm

[Permalink](http://bettyhacks.com/forum/index.php?topic=152.msg1310#msg1310)

---

## Verwandte Themen

- [Betty-Heaven.exe / Betty-Dumps.zip](0033-betty-heaven-exe-betty-dumps-zip.md)
- [Installation Betty Heaven](0107-installation-betty-heaven.md)
- [Betty-Heaven Problem: Keine Com-Ports](0180-betty-heaven-problem-keine-com-ports.md)
- [Betty-Heaven tot?](0296-betty-heaven-tot.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
