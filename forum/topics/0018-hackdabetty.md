---
title: "hackdabetty"
topic_id: 18
board: "Hardware"
board_id: 5
posts: 35
first_post: "02. Aug 2007, 11:59"
last_post: "27. Mär 2008, 10:15"
authors: ["Colibri", "Spessi", "alterego", "cheristi", "eme", "kackhart", "netguy", "theborg"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=18.0"
---

# hackdabetty

[← Hardware](../boards/05-hardware.md) · Thema 18 · 35 Beiträge · 02. Aug 2007, 11:59 – 27. Mär 2008, 10:15

Beteiligt: Colibri, Spessi, alterego, cheristi, eme, kackhart, netguy, theborg

---

<a id="msg63"></a>

## 1. cheristi · 02. Aug 2007, 11:59

Die englischsprachigen Kollegen von hackdaworld haben sich auch schon ein bisschen ans auseinanderschrauben gemacht.

[http://www.hackdaworld.org/cgi-bin/awki.cgi?edit=true&page=BettyTV](https://web.archive.org/web/2012/http://www.hackdaworld.org/cgi-bin/awki.cgi?edit=true&page=BettyTV)

Da is zwar die gleiche Nummer wie auf meinem Display angegeben, aber ansonsten finde ich dazu nix im Netz.

Hat jmd dazu schon was rausgefunden?

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg63#msg63)

---

<a id="msg64"></a>

## 2. cheristi · 02. Aug 2007, 12:11

Nachdem das mit dem bearbeiten bei mir nich tut,
hier der echte link
[http://www.hackdaworld.org/cgi-bin/awki.cgi/BettyTV](https://web.archive.org/web/2012/http://www.hackdaworld.org/cgi-bin/awki.cgi/BettyTV)

#grs

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg64#msg64)

---

<a id="msg65"></a>

## 3. Spessi · 02. Aug 2007, 13:10

Hab ich das richtig verstanden? Er kann jetzt Firmware über den TX und RX Pin in den RAM der Fernbedienung laden, wenn er den Bootloader-Pin kurzschließt?
Jetzt müssen die nurnoch das Format der Firmware rauskriegen und können dann 'ne eigene Firmware schreiben? Na dann..!

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg65#msg65)

---

<a id="msg69"></a>

## 4. theborg · 02. Aug 2007, 16:34

Hi das Format der Firmware ist das standad intel HEX Format welches für jeden protzi benutzt wird.

Hab mir die Tools mal runter geladen und compiliert 3 Dateien davon sind fast lehr nur das Programm zum Flaschen läuft ich werde mir mal von NXP nen testcode runter laden und versuchen den zu flaschen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg69#msg69)

---

<a id="msg70"></a>

## 5. cheristi · 02. Aug 2007, 17:22

Ähm, ich glaube die Dateien sind nur Platzhalter.

Man bekommt die compilierten Datein ja im Moment gar nich auf die Betty, dank dem Bootloader..

#grs

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg70#msg70)

---

<a id="msg71"></a>

## 6. theborg · 02. Aug 2007, 17:30

jo leider ich denke ich werde mir nochmal nen usb-JTAG bauen und versuchen den direkt an den prozi anschlissen mal sehn ob das wenigstens klapt

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg71#msg71)

---

<a id="msg143"></a>

## 7. kackhart · 06. Aug 2007, 14:23

hallo!

> **Zitat von: cheristi am 02. Aug 2007, 17:22**
>
> Ähm, ich glaube die Dateien sind nur Platzhalter.

ja genau! die werden schon noch gefuellt ... hoffentlich.

> **Zitat von: cheristi am 02. Aug 2007, 17:22**
>
> Man bekommt die compilierten Datein ja im Moment gar nich auf die Betty, dank dem Bootloader..

also mit dem lpcload.c kann ich nun (seit gestern!) in den ram schreiben. hatte noch ein paar probleme mit dem uuencoden. man sollte nicht nur einfach schnell den algo aus wikipedia nach c uebersetzen, sondern mal genauer lesen .

man haette es sich sicher auch einfacher machen koennen. selbst fuer linux gibt es ja schon einige firmware loader ...

das lpcload tool liest nur intel hex files.

ich moechte nun doch erstmal die original fw auslesen. die fwbc firmware soll dies tun. leider schaffe ich es zz nichtmal dass sie mir einfach immer 0x23 bei 9600 baud 8n1 via uart0 ausgibt. sollte das problem in naechster zeit mal bewaeltigt sein, muss man hoffentlich nur noch einen init() fuer das externe memory interface schreiben und kann dann anfangen auszulesen (das geht ja im gegensatz zum schreiben wahrscheinlich noch sehr einfach) und das zeug via uart raushauen. fwdump soll den kram dann in ein file auf den pc schreiben. (die leeren files ersetzen einfach nur meine todo :p)

wer ideen hat warum der arm code (fwbc.c) nicht tut ... bin sehr dankbar!

gru3,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg143#msg143)

---

<a id="msg144"></a>

## 8. kackhart · 06. Aug 2007, 14:37

> **Zitat von: Spessi am 02. Aug 2007, 13:10**
>
> Hab ich das richtig verstanden? Er kann jetzt Firmware über den TX und RX Pin in den RAM der Fernbedienung laden, wenn er den Bootloader-Pin kurzschließt?

ja genau. aber wieso so verwundert? steht ja auch so in der lpc2220 doku, oder?

habe noch nicht so viel lesen koennen, aber generell wird hier ein bisschen viel panik gemacht.

ist doch alles wohldefiniert! auch wie man mit dem bootloader reden muss steht da drin!

gru3,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg144#msg144)

---

<a id="msg145"></a>

## 9. kackhart · 06. Aug 2007, 14:42

> **Zitat von: theborg am 02. Aug 2007, 16:34**
>
> 3 Dateien davon sind fast lehr nur das Programm zum Flaschen läuft ich werde mir mal von NXP nen testcode runter laden und versuchen den zu flaschen.

also in den flash schreiben kann der bootloader nicht. du kannst eine firmware in den ram hauen, diese kann dann den flash schreiben oder lesen. steht auch in der doku.

wenn ihr windows habt, solltet ihr einfach mal diesen keil kram ausprobieren. damit sollte das egtl funktionieren. selbst fuer linux gibt es wie gesagt auch schon schoenere tools die man wahrscheinlich nur minimal umhacken muss (part id hinzufuegen). ich bin mir sicher, die keil software hat bestimmt auch schon firmware dabei, die dann den code ins flash schreiben kann.

wie oben schon gesagt, die leeren files werden hoffentlich bald voller.

gru3,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg145#msg145)

---

<a id="msg149"></a>

## 10. Spessi · 06. Aug 2007, 17:15

Hab deine Datei lpcload.c eben mal unter Cygwin compiliert und die Exe ausgeführt - allerdings bekomm ich
`boot loader init ...
  >> ? | 3f | (1)
txrx read: bad return byte '3f'`
zurückgeliefert. Liegt es daran, dass mein TTL-Wandler ab und zu mal rumspinnt oder liegt es einfach daran, dass das Programm unter Windows garnicht gehen KANN?

gruß

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg149#msg149)

---

<a id="msg150"></a>

## 11. kackhart · 06. Aug 2007, 17:42

hi

> **Zitat von: Spessi am 06. Aug 2007, 17:15**
>
> Hab deine Datei lpcload.c eben mal unter Cygwin compiliert und die Exe ausgeführt - allerdings bekomm ich
> `boot loader init ...
>   >> ? | 3f | (1)
> txrx read: bad return byte '3f'`
> zurückgeliefert. Liegt es daran, dass mein TTL-Wandler ab und zu mal rumspinnt oder liegt es einfach daran, dass das Programm unter Windows garnicht gehen KANN?

komisch. er scheint das '?' zu echo'en. das sollte er nicht tun. er muesste mit "Synchronized" antworten. kann es sein, dass du eint1 nicht mit gnd verbunden hast?

tx und rx an max232, gnd von max232 an gnd und eint1 vom arm, dann batterien rein. danach das lpcload starten. sollte dann sowas kommen:

 `$ sudo ./lpcload -d /dev/ttyS0 -f fwbc.hex -v
boot loader init ...
  >> ? | 3f | (1)
  << Synchronized.. | 53 79 6e 63 68 72 6f 6e 69 7a 65 64 0d 0a | (14)
  >> Synchronized.. | 53 79 6e 63 68 72 6f 6e 69 7a 65 64 0d 0a | (14)
  << OK.. | 4f 4b 0d 0a | (4)
  >> 10000.. | 31 30 30 30 30 0d 0a | (7)
  << OK.. | 4f 4b 0d 0a | (4)
write firmware to ram ...
writing 0x10 bytes to 0x40000200
  >> W 1073742336 16.. | 57 20 31 30 37 33 37 34 32 33 33 36 20 31 36 0d 0a | (17)
  << 0.. | 30 0d 0a | (3)
  >> ##<"@.. | 23 23 3c 22 40 0d 0a | (7)
  >> #X0#8.. | 23 58 30 23 38 0d 0a | (7)
  >> #+>D$.. | 23 2b 3e 44 24 0d 0a | (7)
  >> #L$SB.. | 23 4c 24 53 42 0d 0a | (7)
  >> #!-!-.. | 23 21 2d 21 2d 0d 0a | (7)
  >> !X@  .. | 21 58 40 20 20 0d 0a | (7)
  >> 2081.. | 32 30 38 31 0d 0a | (6)
usw ...`

ausserdem natuerlich schauen das lpcload aktuell ist. wurde ja gestern noch gefixed (fast, aber wenigstens sowas wie hier solltest du sehen*). ob windoes probleme macht kann ich leider nicht sagen ...

*) wer schon weiter gekommen ist und spaeter probleme beim daten schreiben bekommt, moege die note in meinem wiki beachten:

> **Zitat**
>
> note: funnily enough (sometimes) the tool just works properly after having started minicom ... (maybe some serial port config issue, dunno!)

dann geht es aber! ja ich weiss, alles sehr unsauber. war aber nie fuer enduser gedacht.

gru3

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg150#msg150)

---

<a id="msg151"></a>

## 12. Spessi · 06. Aug 2007, 17:56

Du arbeitest mit dem Max232? Ist der nicht nur für 5V ausgelegt?

PS: du hast ne PN

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg151#msg151)

---

<a id="msg154"></a>

## 13. theborg · 06. Aug 2007, 18:49

mal ne blöde frage das makefile geht bei mir nicht wie kommt ihr zum hex file ?

ah habs jetzt fehlt mir nur die blöde header datei finde die mit googel net

EDIT: habs

*Last Edit : 06. Aug 2007, 19:10 by theborg*

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg154#msg154)

---

<a id="msg155"></a>

## 14. kackhart · 06. Aug 2007, 19:20

> **Zitat von: Spessi am 06. Aug 2007, 17:56**
>
> Du arbeitest mit dem Max232? Ist der nicht nur für 5V ausgelegt?

die 3v(?) von tx genuegen anscheinend. rx scheint auch 5v auszuhalten. an vcc des max232 selbst lege ich 5v an. gnd von der 5v spannungsquelle und vom arm muss man natuerlich kurz schliessen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg155#msg155)

---

<a id="msg157"></a>

## 15. kackhart · 06. Aug 2007, 19:37

hi theborg!

> **Zitat von: theborg am 06. Aug 2007, 18:49**
>
> EDIT: habs

hast evtl schon eine idee was ich bei dem fwbc verbockt habe, dass da nur muell vom uart kommt?

muell = Àøøøxüx usw.

wenn man von dem 10mhz quarz ausgeht sollte die baudrate mit 65 als divisor doch 9k6 baud sein ...

mfg, frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg157#msg157)

---

<a id="msg158"></a>

## 16. theborg · 06. Aug 2007, 19:53

kommen bei dir die Signale von der Konsole sauber rüber ?

wenn nicht versuch es mal mit nem pullup an rx

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg158#msg158)

---

<a id="msg159"></a>

## 17. theborg · 06. Aug 2007, 19:55

jo seit binn ich net hab mal wieder mein ttl wandler zerschossen gestern als ich meine fon neu geflasht habe werde mal am we platinen auf vorat dafür ätzen

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg159#msg159)

---

<a id="msg166"></a>

## 18. theborg · 08. Aug 2007, 12:06

So nen teiel erfolg mit lpcflash bekomme ich folgendes

 `> Synchronized
> SynchronizedOK
> 10000OK
< A 0
> 0
Ok
< U 23130
> 0
Ok
< B 38400 1
> 0
Ok
Schnittstelle schliessen...`

das andedre tool sag bei mir ganichts

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg166#msg166)

---

<a id="msg170"></a>

## 19. theborg · 08. Aug 2007, 17:05

noch nen Nachtrag ich komme mittlerweile ziemlich weit allerdings meckert es beim auslesen.

 `theborg@TBM:~/Desktop/betty$ ./lpcload -d /dev/ttyUSB0 -v -f fwbc.hex
boot loader init ...
  >> ? | 3f | (1)
  << Synchronized.. | 53 79 6e 63 68 72 6f 6e 69 7a 65 64 0d 0a | (14)
  >> Synchronized.. | 53 79 6e 63 68 72 6f 6e 69 7a 65 64 0d 0a | (14)
  << OK.. | 4f 4b 0d 0a | (4)
  >> 10000.. | 31 30 30 30 30 0d 0a | (7)
  << OK.. | 4f 4b 0d 0a | (4)
write firmware to ram ...
writing 0x10 bytes to 0x40000200
  >> W 1073742336 16.. | 57 20 31 30 37 33 37 34 32 33 33 36 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> ##<"@.. | 23 23 3c 22 40 0d 0a | (7)
  >> #X0#8.. | 23 58 30 23 38 0d 0a | (7)
  >> #+>D$.. | 23 2b 3e 44 24 0d 0a | (7)
  >> #L$SB.. | 23 4c 24 53 42 0d 0a | (7)
  >> #!-!-.. | 23 21 2d 21 2d 0d 0a | (7)
  >> !X@  .. | 21 58 40 20 20 0d 0a | (7)
  >> 2081.. | 32 30 38 31 0d 0a | (6)
  << OK.. | 4f 4b 0d 0a | (4)
writing 0x10 bytes to 0x40000210
  >> W 1073742352 16.. | 57 20 31 30 37 33 37 34 32 33 35 32 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> # #"@.. | 23 20 23 22 40 0d 0a | (7)
  >> #X1 P.. | 23 58 31 20 50 0d 0a | (7)
  >> #2^4... | 23 32 5e 34 2e 0d 0a | (7)
  >> #,J#C.. | 23 2c 4a 23 43 0d 0a | (7)
  >> #?SF#.. | 23 3f 53 46 23 0d 0a | (7)
  >> !X@  .. | 21 58 40 20 20 0d 0a | (7)
  >> 1793.. | 31 37 39 33 0d 0a | (6)
  << OK.. | 4f 4b 0d 0a | (4)
writing 0x10 bytes to 0x40000220
  >> W 1073742368 16.. | 57 20 31 30 37 33 37 34 32 33 36 38 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> #0#"#.. | 23 30 23 22 23 0d 0a | (7)
  >> #XA @.. | 23 58 41 20 40 0d 0a | (7)
  >> #6^4 .. | 23 36 5e 34 20 0d 0a | (7)
  >> #((/E.. | 23 28 28 2f 45 0d 0a | (7)
  >> #"*B=.. | 23 22 2a 42 3d 0d 0a | (7)
  >> !Z   .. | 21 5a 20 20 20 0d 0a | (7)
  >> 1794.. | 31 37 39 34 0d 0a | (6)
  << OK.. | 4f 4b 0d 0a | (4)
writing 0x10 bytes to 0x40000230
  >> W 1073742384 16.. | 57 20 31 30 37 33 37 34 32 33 38 34 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> ##<"@.. | 23 23 3c 22 40 0d 0a | (7)
  >> #X0#8.. | 23 58 30 23 38 0d 0a | (7)
  >> #+>D$.. | 23 2b 3e 44 24 0d 0a | (7)
  >> #L$SB.. | 23 4c 24 53 42 0d 0a | (7)
  >> ##C*@.. | 23 23 43 2a 40 0d 0a | (7)
  >> !XP  .. | 21 58 50 20 20 0d 0a | (7)
  >> 2017.. | 32 30 31 37 0d 0a | (6)
  << OK.. | 4f 4b 0d 0a | (4)
writing 0x10 bytes to 0x40000240
  >> W 1073742400 16.. | 57 20 31 30 37 33 37 34 32 34 30 30 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> #"SF#.. | 23 22 53 46 23 0d 0a | (7)
  >> #X@4@.. | 23 58 40 34 40 0d 0a | (7)
  >> #H., .. | 23 48 2e 2c 20 0d 0a | (7)
  >> #((/E.. | 23 28 28 2f 45 0d 0a | (7)
  >> # SF@.. | 23 20 53 46 40 0d 0a | (7)
  >> !XP  .. | 21 58 50 20 20 0d 0a | (7)
  >> 1688.. | 31 36 38 38 0d 0a | (6)
txrx read: bad return byte '0a'
  << . | 0a | (1)
ram write: bad response
writing 0x10 bytes to 0x40000250
  >> W 1073742416 16.. | 57 20 31 30 37 33 37 34 32 34 31 36 20 31 36 0d 0a | (17)
txrx read: bad return byte '31'
  << 1 | 31 | (1)
txrx bad return code!
  >> #CC*#.. | 23 43 43 2a 23 0d 0a | (7)
  >> #X@<@.. | 23 58 40 3c 40 0d 0a | (7)
  >> #H., .. | 23 48 2e 2c 20 0d 0a | (7)
  >> #((/E.. | 23 28 28 2f 45 0d 0a | (7)
  >> # SF@.. | 23 20 53 46 40 0d 0a | (7)
  >> !XP  .. | 21 58 50 20 20 0d 0a | (7)
  >> 1814.. | 31 38 31 34 0d 0a | (6)
txrx read: bad return byte '31'
  << 1 | 31 | (1)
ram write: bad response
writing 0x10 bytes to 0x40000260
  >> W 1073742432 16.. | 57 20 31 30 37 33 37 34 32 34 33 32 20 31 36 0d 0a | (17)
txrx read: bad return byte '20'
  <<   | 20 | (1)
txrx bad return code!
  >> #SC*#.. | 23 53 43 2a 23 0d 0a | (7)
  >> #XH,@.. | 23 58 48 2c 40 0d 0a | (7)
  >> #H., .. | 23 48 2e 2c 20 0d 0a | (7)
  >> #((/E.. | 23 28 28 2f 45 0d 0a | (7)
  >> ##C*@.. | 23 23 43 2a 40 0d 0a | (7)
  >> !XP  .. | 21 58 50 20 20 0d 0a | (7)
  >> 2006.. | 32 30 30 36 0d 0a | (6)
txrx read: bad return byte '0a'
  << . | 0a | (1)
ram write: bad response
writing 0x10 bytes to 0x40000270
  >> W 1073742448 16.. | 57 20 31 30 37 33 37 34 32 34 34 38 20 31 36 0d 0a | (17)
txrx read: bad return byte '31'
  << 1 | 31 | (1)
txrx bad return code!
  >> # SF#.. | 23 20 53 46 23 0d 0a | (7)
  >> #XA @.. | 23 58 41 20 40 0d 0a | (7)
  >> #H., .. | 23 48 2e 2c 20 0d 0a | (7)
  >> #((/E.. | 23 28 28 2f 45 0d 0a | (7)
  >> # SF@.. | 23 20 53 46 40 0d 0a | (7)
  >> !XP  .. | 21 58 50 20 20 0d 0a | (7)
  >> 1691.. | 31 36 39 31 0d 0a | (6)
txrx read: bad return byte '28'
  << ( | 28 | (1)
ram write: bad response
writing 0x10 bytes to 0x40000280
  >> W 1073742464 16.. | 57 20 31 30 37 33 37 34 32 34 36 34 20 31 36 0d 0a | (17)
txrx read: bad return byte '50'
  << P | 50 | (1)
txrx bad return code!
  >> #3C*#.. | 23 33 43 2a 23 0d 0a | (7)
  >> #X@ @.. | 23 58 40 20 40 0d 0a | (7)
  >> #H., .. | 23 48 2e 2c 20 0d 0a | (7)
  >> #((/E.. | 23 28 28 2f 45 0d 0a | (7)
  >> # SF@.. | 23 20 53 46 40 0d 0a | (7)
  >> !XP  .. | 21 58 50 20 20 0d 0a | (7)
  >> 1743.. | 31 37 34 33 0d 0a | (6)
txrx read: bad return byte '0a'
  << . | 0a | (1)
ram write: bad response
writing 0x10 bytes to 0x40000290
  >> W 1073742480 16.. | 57 20 31 30 37 33 37 34 32 34 38 30 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> #SC*#.. | 23 53 43 2a 23 0d 0a | (7)
  >> #X@,@.. | 23 58 40 2c 40 0d 0a | (7)
  >> #H., .. | 23 48 2e 2c 20 0d 0a | (7)
  >> #((/E.. | 23 28 28 2f 45 0d 0a | (7)
  >> # *B=.. | 23 20 2a 42 3d 0d 0a | (7)
  >> !Z   .. | 21 5a 20 20 20 0d 0a | (7)
  >> 1984.. | 31 39 38 34 0d 0a | (6)
txrx read: bad return byte '0d'
  << . | 0d | (1)
ram write: bad response
writing 0x10 bytes to 0x400002a0
  >> W 1073742496 16.. | 57 20 31 30 37 33 37 34 32 34 39 36 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> ##<"@.. | 23 23 3c 22 40 0d 0a | (7)
  >> #X0#8.. | 23 58 30 23 38 0d 0a | (7)
  >> #+>D$.. | 23 2b 3e 44 24 0d 0a | (7)
  >> #L$SB.. | 23 4c 24 53 42 0d 0a | (7)
  >> #"-!-.. | 23 22 2d 21 2d 0d 0a | (7)
  >> !X@  .. | 21 58 40 20 20 0d 0a | (7)
  >> 2085.. | 32 30 38 35 0d 0a | (6)
txrx read: bad return byte '0d'
  << . | 0d | (1)
ram write: bad response
writing 0x10 bytes to 0x400002b0
  >> W 1073742512 16.. | 57 20 31 30 37 33 37 34 32 35 31 32 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> #%  +.. | 23 25 20 20 2b 0d 0a | (7)
  >> #Y0 P.. | 23 59 30 20 50 0d 0a | (7)
  >> #H.,0.. | 23 48 2e 2c 30 0d 0a | (7)
  >> #, OE.. | 23 2c 20 4f 45 0d 0a | (7)
  >> #.0  .. | 23 2e 30 20 20 0d 0a | (7)
  >> !Z@  .. | 21 5a 40 20 20 0d 0a | (7)
  >> 1290.. | 31 32 39 30 0d 0a | (6)
  << 0.. | 30 0d 0a | (3)
ram write: bad response
writing 0x10 bytes to 0x400002c0
  >> W 1073742528 16.. | 57 20 31 30 37 33 37 34 32 35 32 38 20 31 36 0d 0a | (17)
txrx read: bad return byte '40'
  << @ | 40 | (1)
txrx bad return code!
  >> ##B*@.. | 23 23 42 2a 40 0d 0a | (7)
  >> #XP,I.. | 23 58 50 2c 49 0d 0a | (7)
  >> #@N(0.. | 23 40 4e 28 30 0d 0a | (7)
  >> #,!OE.. | 23 2c 21 4f 45 0d 0a | (7)
  >> # Q"@.. | 23 20 51 22 40 0d 0a | (7)
  >> !X0  .. | 21 58 30 20 20 0d 0a | (7)
  >> 1559.. | 31 35 35 39 0d 0a | (6)
txrx read: bad return byte '0a'
  << . | 0a | (1)
ram write: bad response
writing 0x10 bytes to 0x400002d0
  >> W 1073742544 16.. | 57 20 31 30 37 33 37 34 32 35 34 34 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> #%# ;.. | 23 25 23 20 3b 0d 0a | (7)
  >> #Y0,P.. | 23 59 30 2c 50 0d 0a | (7)
  >> #@>  .. | 23 40 3e 20 20 0d 0a | (7)
  >> #,-/E.. | 23 2c 2d 2f 45 0d 0a | (7)
  >> # #"".. | 23 20 23 22 22 0d 0a | (7)
  >> !Y0  .. | 21 59 30 20 20 0d 0a | (7)
  >> 1623.. | 31 36 32 33 0d 0a | (6)
txrx read: bad return byte '0d'
  << . | 0d | (1)
ram write: bad response
writing 0x10 bytes to 0x400002e0
  >> W 1073742560 16.. | 57 20 31 30 37 33 37 34 32 35 36 30 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> #$# ;.. | 23 24 23 20 3b 0d 0a | (7)
  >> #Y0$P.. | 23 59 30 24 50 0d 0a | (7)
  >> #@^(0.. | 23 40 5e 28 30 0d 0a | (7)
  >> #, OE.. | 23 2c 20 4f 45 0d 0a | (7)
  >> #$# ;.. | 23 24 23 20 3b 0d 0a | (7)
  >> !Y0  .. | 21 59 30 20 20 0d 0a | (7)
  >> 1350.. | 31 33 35 30 0d 0a | (6)
txrx read: bad return byte '0d'
  << . | 0d | (1)
ram write: bad response
writing 0x10 bytes to 0x400002f0
  >> W 1073742576 16.. | 57 20 31 30 37 33 37 34 32 35 37 36 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> # R"@.. | 23 20 52 22 40 0d 0a | (7)
  >> #X10P.. | 23 58 31 30 50 0d 0a | (7)
  >> #&^4#.. | 23 26 5e 34 23 0d 0a | (7)
  >> #,(+@.. | 23 2c 28 2b 40 0d 0a | (7)
  >> # ##3.. | 23 20 23 23 33 0d 0a | (7)
  >> !Y0  .. | 21 59 30 20 20 0d 0a | (7)
  >> 1637.. | 31 36 33 37 0d 0a | (6)
txrx read: bad return byte '0d'
  << . | 0d | (1)
ram write: bad response
writing 0x10 bytes to 0x40000300
  >> W 1073742592 16.. | 57 20 31 30 37 33 37 34 32 35 39 32 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> #  !3.. | 23 20 20 21 33 0d 0a | (7)
  >> #XRX .. | 23 58 52 58 20 0d 0a | (7)
  >> # !H... | 23 20 21 48 2e 0d 0a | (7)
  >> #,J#C.. | 23 2c 4a 23 43 0d 0a | (7)
  >> # SF#.. | 23 20 53 46 23 0d 0a | (7)
  >> !X@  .. | 21 58 40 20 20 0d 0a | (7)
  >> 1250.. | 31 32 35 30 0d 0a | (6)
txrx read: bad return byte '2e'
  << . | 2e | (1)
ram write: bad response
writing 0x10 bytes to 0x40000310
  >> W 1073742608 16.. | 57 20 31 30 37 33 37 34 32 36 30 38 20 31 36 0d 0a | (17)
txrx read: bad return byte '35'
  << 5 | 35 | (1)
txrx bad return code!
  >> #"B"@.. | 23 22 42 22 40 0d 0a | (7)
  >> #XP @.. | 23 58 50 20 40 0d 0a | (7)
  >> #@^4... | 23 40 5e 34 2e 0d 0a | (7)
  >> #,J#C.. | 23 2c 4a 23 43 0d 0a | (7)
  >> # SF#.. | 23 20 53 46 23 0d 0a | (7)
  >> !X@  .. | 21 58 40 20 20 0d 0a | (7)
  >> 1689.. | 31 36 38 39 0d 0a | (6)
txrx read: bad return byte '0d'
  << . | 0d | (1)
ram write: bad response
writing 0x10 bytes to 0x40000320
  >> W 1073742624 16.. | 57 20 31 30 37 33 37 34 32 36 32 34 20 31 36 0d 0a | (17)
txrx read: bad return byte '31'
  << 1 | 31 | (1)
txrx bad return code!
  >> ##2"@.. | 23 23 32 22 40 0d 0a | (7)
  >> #XP @.. | 23 58 50 20 40 0d 0a | (7)
  >> #@^4... | 23 40 5e 34 2e 0d 0a | (7)
  >> #,J#C.. | 23 2c 4a 23 43 0d 0a | (7)
  >> # SF#.. | 23 20 53 46 23 0d 0a | (7)
  >> !X@  .. | 21 58 40 20 20 0d 0a | (7)
  >> 1692.. | 31 36 39 32 0d 0a | (6)
txrx read: bad return byte '34'
  << 4 | 34 | (1)
ram write: bad response
writing 0x10 bytes to 0x40000330
  >> W 1073742640 16.. | 57 20 31 30 37 33 37 34 32 36 34 30 20 31 36 0d 0a | (17)
txrx read: bad return byte '32'
  << 2 | 32 | (1)
txrx bad return code!
  >> #%#"#.. | 23 25 23 22 23 0d 0a | (7)
  >> #X@ P.. | 23 58 40 20 50 0d 0a | (7)
  >> #D^5 .. | 23 44 5e 35 20 0d 0a | (7)
  >> #, /B.. | 23 2c 20 2f 42 0d 0a | (7)
  >> #  !3.. | 23 20 20 21 33 0d 0a | (7)
  >> !XP  .. | 21 58 50 20 20 0d 0a | (7)
  >> 1500.. | 31 35 30 30 0d 0a | (6)
txrx read: bad return byte '35'
  << 5 | 35 | (1)
ram write: bad response
writing 0x10 bytes to 0x40000340
  >> W 1073742656 16.. | 57 20 31 30 37 33 37 34 32 36 35 36 20 31 36 0d 0a | (17)
txrx read: bad return byte '31'
  << 1 | 31 | (1)
txrx bad return code!
  >> #2   .. | 23 32 20 20 20 0d 0a | (7)
  >> #"@S0.. | 23 22 40 53 30 0d 0a | (7)
  >> #2^( .. | 23 32 5e 28 20 0d 0a | (7)
  >> #J)WH.. | 23 4a 29 57 48 0d 0a | (7)
  >> ##<"@.. | 23 23 3c 22 40 0d 0a | (7)
  >> !X0  .. | 21 58 30 20 20 0d 0a | (7)
  >> 1750.. | 31 37 35 30 0d 0a | (6)
txrx read: bad return byte '5e'
  << ^ | 5e | (1)
ram write: bad response
writing 0x10 bytes to 0x40000350
  >> W 1073742672 16.. | 57 20 31 30 37 33 37 34 32 36 37 32 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> # -@M.. | 23 20 2d 40 4d 0d 0a | (7)
  >> #Z02P.. | 23 5a 30 32 50 0d 0a | (7)
  >> #3.(0.. | 23 33 2e 28 30 0d 0a | (7)
  >> #T$WB.. | 23 54 24 57 42 0d 0a | (7)
  >> #,#"?.. | 23 2c 23 22 3f 0d 0a | (7)
  >> !Y0  .. | 21 59 30 20 20 0d 0a | (7)
  >> 1987.. | 31 39 38 37 0d 0a | (6)
txrx read: bad return byte '2e'
  << . | 2e | (1)
ram write: bad response
writing 0x10 bytes to 0x40000360
  >> W 1073742688 16.. | 57 20 31 30 37 33 37 34 32 36 38 38 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> #&B!+.. | 23 26 42 21 2b 0d 0a | (7)
  >> #X@[ .. | 23 58 40 5b 20 0d 0a | (7)
  >> #H.,".. | 23 48 2e 2c 22 0d 0a | (7)
  >> # *#A.. | 23 20 2a 23 41 0d 0a | (7)
  >> # Q"@.. | 23 20 51 22 40 0d 0a | (7)
  >> !X0  .. | 21 58 30 20 20 0d 0a | (7)
  >> 1743.. | 31 37 34 33 0d 0a | (6)
txrx read: bad return byte '2e'
  << . | 2e | (1)
ram write: bad response
writing 0x10 bytes to 0x40000370
  >> W 1073742704 16.. | 57 20 31 30 37 33 37 34 32 37 30 34 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> ##""@.. | 23 23 22 22 40 0d 0a | (7)
  >> #X?[_.. | 23 58 3f 5b 5f 0d 0a | (7)
  >> #_^L".. | 23 5f 5e 4c 22 0d 0a | (7)
  >> # *#C.. | 23 20 2a 23 43 0d 0a | (7)
  >> #_O__.. | 23 5f 4f 5f 5f 0d 0a | (7)
  >> !ZP  .. | 21 5a 50 20 20 0d 0a | (7)
  >> 2816.. | 32 38 31 36 0d 0a | (6)
txrx read: bad return byte '5f'
  << _ | 5f | (1)
ram write: bad response
writing 0x10 bytes to 0x40000380
  >> W 1073742720 16.. | 57 20 31 30 37 33 37 34 32 37 32 30 20 31 36 0d 0a | (17)
txrx read: bad return byte '0d'
  << . | 0d | (1)
txrx bad return code!
  >> #_O__.. | 23 5f 4f 5f 5f 0d 0a | (7)
  >> #ZQHP.. | 23 5a 51 48 50 0d 0a | (7)
  >> #2^(#.. | 23 32 5e 28 23 0d 0a | (7)
  >> # *#A.. | 23 20 2a 23 41 0d 0a | (7)
  >> #_O__.. | 23 5f 4f 5f 5f 0d 0a | (7)
  >> !ZP  .. | 21 5a 50 20 20 0d 0a | (7)
  >> 2761.. | 32 37 36 31 0d 0a | (6)
txrx read: bad return byte '32'
  << 2 | 32 | (1)
ram write: bad response
writing 0x08 bytes to 0x40000390
  >> W 1073742736 8.. | 57 20 31 30 37 33 37 34 32 37 33 36 20 38 0d 0a | (16)
txrx read: bad return byte '5f'
  << _ | 5f | (1)
txrx bad return code!
  >> #7P  .. | 23 37 50 20 20 0d 0a | (7)
  >> #Z@  .. | 23 5a 40 20 20 0d 0a | (7)
  >> "    .. | 22 20 20 20 20 0d 0a | (7)
  >> 329.. | 33 32 39 0d 0a | (5)
txrx read: bad return byte '36'
  << 6 | 36 | (1)
ram write: bad response
writing 0x10 bytes to 0x40000200
  >> W 1073742336 16.. | 57 20 31 30 37 33 37 34 32 33 33 36 20 31 36 0d 0a | (17)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!
  >> #=6%R.. | 23 3d 36 25 52 0d 0a | (7)
  >> #=# @.. | 23 3d 23 20 40 0d 0a | (7)
  >> #=V]R.. | 23 3d 56 5d 52 0d 0a | (7)
  >> #:VEN.. | 23 3a 56 45 4e 0d 0a | (7)
  >> #9P  .. | 23 39 50 20 20 0d 0a | (7)
  >> !    .. | 21 20 20 20 20 0d 0a | (7)
  >> 1293.. | 31 32 39 33 0d 0a | (6)
txrx read: bad return byte '3d'
  << = | 3d | (1)
ram write: bad response
unlock go command ...
  >> U 23130.. | 55 20 32 33 31 33 30 0d 0a | (9)
txrx read: bad return byte '4e'
  << N | 4e | (1)
txrx bad return code!
go ...
  >> G 1073742336 A.. | 47 20 31 30 37 33 37 34 32 33 33 36 20 41 0d 0a | (16)
txrx read: bad return byte '0a'
  << . | 0a | (1)
txrx bad return code!

the above error might be due to the jump!

continue listening on serial port? (ctrl+c to quit) [y|n]: y

read 31 bytes: 31 0d 0a 33 0d 0a 31 0d 0a 32 33 31 33 0d 0a 31 0d 0a 31 30 37 37 34 33 33 20 41 0a 31 0d 0a
read 0 bytes:
theborg@TBM:~/Desktop/betty$`

@ kackhart

sach mal mit Flaschmagic kann ich wunderbar die Datei übertragen alerdinks finde ich die passende startadresse nicht kanste mir da mal helfen

*Last Edit : 08. Aug 2007, 17:34 by theborg*

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg170#msg170)

---

<a id="msg173"></a>

## 20. kackhart · 08. Aug 2007, 18:11

> **Zitat von: theborg am 08. Aug 2007, 17:05**
>
> noch nen Nachtrag ich komme mittlerweile ziemlich weit allerdings meckert es beim auslesen.

wie oben gesagt, minicom kurz starten und beenden hat da bei mir geholfen. allerdings habe ich den init des seriellen ports jetzt glaube ich gefixed. also bei mir geht es zumindest ohne. ka ob das in deiner version schon geaendert ist.

> **Zitat**
>
> sach mal mit Flaschmagic kann ich wunderbar die Datei übertragen alerdinks finde ich die passende startadresse nicht kanste mir da mal helfen

0x40000200

nachtrag:
0x23 transmitten funzt mit der jetzigen fwbc firmware auch. aber alles noch sehr seltsam. werde mich nun mal dran versuchen den flash auszulesen ...

gru3

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg173#msg173)

---

<a id="msg175"></a>

## 21. theborg · 08. Aug 2007, 18:17

hi jo den trik mit minicom hab ich schon versucht setseriel geht dafür auch

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg175#msg175)

---

<a id="msg176"></a>

## 22. kackhart · 09. Aug 2007, 01:52

> **Zitat von: kackhart am 08. Aug 2007, 18:11**
>
> > **Zitat**
> >
> > sach mal mit Flaschmagic kann ich wunderbar die Datei übertragen alerdinks finde ich die passende startadresse nicht kanste mir da mal helfen
>
>
> 0x40000200

das ist natuerlich nicht ganz richtig und erklaert evtl auch einige meiner probleme die ich hatte. wenn dein arm code nicht mit der main funktion beginnt hast du natuerlich einen anderen entry point. komischerweise erzeugt objcopy beim konvertieren nach intel hex keine '03' oder '05' record types. wenn ich die mal bekomme pass ich lpcload dementsprechend an, ist nicht schwer. ich weiss nicht was ich falsch mache, koennte mir aber gut vorstellen dass man objcopy anderst verwenden muss! alternativ koennte man die fw mit objdump -S nach der main funktion parsen und den addr-wert auf 0x40000200 addieren.

seltsam ist, auch wenn der main code als erstes kommt - funktionen kann ich nicht verwenden. evtl nimmt er da direkte spruenge und dann landet der pc irgendwo. ist aber nur eine vermutung.

naja, bis das geklaert ist hacke ich alles einfach nur in einer main funktion .

gru3,

frank

ps: den flash an bank0 habe ich mal ausgelesen, so vertrauenswuerdig schaut das allerdings bei mir nicht aus. anleitung und tools auf meiner wiki seite.

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg176#msg176)

---

<a id="msg281"></a>

## 23. kackhart · 02. Sep 2007, 14:42

> **Zitat von: kackhart am 09. Aug 2007, 01:52**
>
> seltsam ist, auch wenn der main code als erstes kommt - funktionen kann ich nicht verwenden. evtl nimmt er da direkte spruenge und dann landet der pc irgendwo. ist aber nur eine vermutung.

> **Zitat**
>
> ps: den flash an bank0 habe ich mal ausgelesen, so vertrauenswuerdig schaut das allerdings bei mir nicht aus. 

das alles hat sich jetzt dank netguy und dem tip von colibri mit dem bank init geaendert. man kann seine firmware mit hilfe von lpcload und fwflash nun in den flash an bank0 schreiben. die beispiel firmware betty.c laeuft super vom flash und announced sich stolz ueber uart nach eingabe eines beliebigen buchstabens mit 115200 baud.

gru3

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg281#msg281)

---

<a id="msg282"></a>

## 24. Colibri · 02. Sep 2007, 22:51

![](https://web.archive.org/web/2012/http://free.pages.at/colibri_dvb/Betty-FW-Patch.jpg)

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg282#msg282)

---

<a id="msg283"></a>

## 25. netguy · 03. Sep 2007, 00:23

> **Zitat von: Colibri am 02. Sep 2007, 22:51**
>
> ![](https://web.archive.org/web/2012/http://free.pages.at/colibri_dvb/Betty-FW-Patch.jpg)

information wants to be free!

magst du sie befreien? ;-)

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg283#msg283)

---

<a id="msg284"></a>

## 26. alterego · 03. Sep 2007, 00:24

colibri:

wie können wir dich dazu bringen dein wissen mit uns zu teilen? leider bist du bei keinem deiner projekte wirklich gesprächig... oder machst du das nur für dich und um uns hier die nase lang zu machen ?

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg284#msg284)

---

<a id="msg285"></a>

## 27. kackhart · 03. Sep 2007, 00:32

schoen! aber ...

./colibri -vvv

gru3,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg285#msg285)

---

<a id="msg286"></a>

## 28. Colibri · 03. Sep 2007, 19:44

Ihr müsst schon auch auf die Uhrzeit von meinem letzten Post schauen.
Ich habe es erst um Mitternacht geschafft eigenen Text auf dem Display darzustellen.
Für Doku im Wiki schreiben und Hochladen der Version 1.01 von Betty-Heaven das neben Backup, jetzt auch Restore mit CRC-Berichtigung beherrscht hatte ich gestern wirklich keine Lust mehr.
Dennoch wollte ich euch das Beweisfoto von unserem Erfolg die Orginalfirmware zu patchen natürlich nicht vorenthalten.

Die folgenden Wiki-Einträge habe ich jetzt upgedatet bzw. neu angelegt:
[http://www.bettyhacks.com/wiki/index.php/Software_von_Colibri](../../pages/Software%20von%20Colibri.md)
[http://www.bettyhacks.com/wiki/index.php/Speicheraufteilung](../../pages/Speicheraufteilung.md)
[http://www.bettyhacks.com/wiki/index.php/CRC-Check](../../pages/CRC-Check.md)

Schreibt man das Flash1 von Betty-Dumps.zip in die Betty erscheint ein AGB-Text auf dem Display.
Ich habe diesen Text einfach mit einem Hexeditor im Flash1 gesucht und durch den "[http://bettyhacks.com](https://web.archive.org/web/2012/http://bettyhacks.com)"-Text ersetzt. Den restlichen AGB-Text (sowie z.B. den Text "Einverstanden" oder den Titel "AGB") einfach mit Leerzeichen überschreiben.

Viel Spass beim Patchen
Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg286#msg286)

---

<a id="msg287"></a>

## 29. netguy · 03. Sep 2007, 21:14

> **Zitat von: Colibri am 03. Sep 2007, 19:44**
>
> Ich habe diesen Text einfach mit einem Hexeditor im Flash1 gesucht und durch den "[http://bettyhacks.com](https://web.archive.org/web/2012/http://bettyhacks.com)"-Text ersetzt. Den restlichen AGB-Text (sowie z.B. den Text "Einverstanden" oder den Titel "AGB") einfach mit Leerzeichen überschreiben.
>
> Viel Spass beim Patchen
> Colibri

ahch so, und ich dachte schon du haettest etwas ueber serielle eingaben erreicht ....
oder gar das lcd direkt angesteuert (dafuer waren aber die striche und das batt-symbol zu auffaellig)

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg287#msg287)

---

<a id="msg288"></a>

## 30. kackhart · 03. Sep 2007, 21:27

hi colibri,

du darfst das da oben nicht falsch verstehen. wir hiengen alle drei im #bettyhacks chat ab bis einer deinen post bemerkte. wir haben uns alle draufgestuerzt un jeder hat wohl ohne wissen dass der andere nach mehr info fragt replied . also zumindest ich haette mir meinen beitrag gespart, haette ich von den vorherigen zweien gewusst.

das mit dem flash habe ich mir dann auch gedacht (andere vermuteten auch irgendwas a la gurkensalat). ich habe mich dann nach deinem post auch dran gemacht die fw zu patchen.

![](https://web.archive.org/web/2012/http://hackdaworld.org/pics/betty/betty_fw_hacked.jpg)

allerdings wusste ich natuerlich nichts von dem speicherlayout und der crc. zudem dauert bei meinem tool ein kompletter flashwrite so schaetzungsweise 20-30 min.

die neue und alte crc hatte durch den bootloader herausgefunden:

BIOS 000233E0 6D6D3572 - should be 81D8E589

ich musste also mind. 3 mal schreiben und 2mal editieren. (drum muss ich dieses bild jetzt einfach zeigen auch wenn es ja nun ein alter schuh ist :p)

wegen dem flash schreiben haette ich deswegen auch gleich noch eine frage. ich denke mal bei dir geht das bestimmt wieder viel viel schneller, oder? ich wuerde das hier zumindest gern etwas beschleunigen.

ich schreibe ein word mit

 `int flash_write(u32 addr,u16 data) {

        u16 check;

        if(data==0xffff)
                return 0;

        *((unsigned volatile short *)addr)=0xa0;
        *((unsigned volatile short *)addr)=data;
        while(1) {
                check=*((unsigned short *)addr);
                if((data&0x80)==(check&0x80))
                        break;
        }
        if(data!=check)
                return -1;

        return 0;
}`

in einer anderen routine receive ich immer jeweils 2 byte ueber uart und schreibe die dann mit der oberen fkt. weil das teilweise nicht funktionierte habe ich zur kontrolle die erhaltenen bytes einfach mal wieder zurueckgeschickt an den host. dann ging es ploetzlich reibungslos. daher vermute ich ein timing problem. ich dachte egtl dass man mit  dem "if((data&0x80)==(check&0x80)) break;" teil egtl genuegend lange vor dem naechsten write wartet. hast du ne idee? bzw allgemein tips waeren toll .

auf alle faelle nochmal danke fuer die infos im wiki!

gru3,

frank

ps: nichts desto trotz waere es fuer die alternativ fw wichtig zu wissen wie man das lcd anspricht! ein glueck will sich netguy darum kuemmern!

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg288#msg288)

---

<a id="msg289"></a>

## 31. Colibri · 03. Sep 2007, 22:18

`BOOL CmdPrgFlash(DWORD DstAddress, int WordLen, BYTE *SrcBuffer)
{

 int i;
 int k;
 BOOL Error;
 DWORD dwPrgAddress;
 WORD wPrgData;
 int Retries;
 DWORD Address;
 int FlashNr;
 DWORD FlashBase;
 DWORD wData;

 if(DstAddress < FLASH_1_ADDRESS)
 {
  return false;//Error
 }

 FlashNr = (DstAddress < FLASH_2_ADDRESS) ? 1 : 2;
 FlashBase = (FlashNr == 1) ? FLASH_1_ADDRESS : FLASH_2_ADDRESS;

 for(i=0; i<WordLen; i++)
 {
  dwPrgAddress = DstAddress + (i * 2);
  wPrgData = GetWord(&SrcBuffer[i * 2], true);//LSB first

  Retries = 3;
  do
  {
   Error = false;

   Address = 0x555 << 1;
   Address |= FlashBase;
   wData = 0xAA;
   ((WORD*)Address)[0] = wData;

   Address = 0x2AA << 1;
   Address |= FlashBase;
   wData = 0x55;
   ((WORD*)Address)[0] = wData;

   Address = 0x555 << 1;
   Address |= FlashBase;
   wData = 0xA0;
   ((WORD*)Address)[0] = wData;

   Address = dwPrgAddress;
   Address |= FlashBase;
   wData = wPrgData;
   ((WORD*)Address)[0] = wData;

   BOOL DataOk;
   DataOk = false;

   for(k=0; (k<1000) & !DataOk ; k++)
   {
    if( (((WORD*)Address)[0] & 0x80) == (wData & 0x80) )
    {
     DataOk = true;
    }
   }
   if(!DataOk)
   {
    Error = true;
   }

   Address = 0 << 1;
   Address |= FlashBase;
   wData = 0xF0;//Reset
   ((WORD*)Address)[0] = wData;
  }while(Error & (Retries-- > 0));
 }

 return true;//OK
}`

Ich verwende zu flashen obige Routine.

Ich habe gerade mitgestoppt:
- Ausgangssituation Flash1 von Betty-Dumps.zip ist auf der Betty
- Zeit start
- Power on der Betty
- Flash1 mit gepatchten AGB-Text flashen (incl. CRC korrektur). Flash2 ist deaktiviert.
- Flashen beendet
- Zeit stop

Hat ca. 35 Sekunden (nicht Minuten) gedauert.

Die Tricks:
- Nicht das Brennen ist der Engpass sondern die serielle Schnittstelle -> Also nicht unnötig Daten übertragen.
- Ein kleines Tool wird über ISP-Bootloader mit 38400 Bit/s geladen.
- Das Tool setzt dann die typische Betty PLL-Frequenz und läd den Rest des Tool mit 115200 Bit/s nach.
- Vor dem Flashen lasse ich vom Tool die SHA-1 Hashwerte der 19 Sektoren ermitteln und zum PC schicken (geht schnell - nur wenig Daten über RS232).
- Von Quellfile werden am PC auch die SHA-1 Hashwerte der 19 Sektoren ermittelt.
- Dann werden nur die Sektoren mit unterschiedlichem Hashwert gelöscht und programmiert (das ist bei AGB-Patch nur ein Sektor - deshalb nur 35 Sekunden Gesamtzeit).

Colibri

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg289#msg289)

---

<a id="msg290"></a>

## 32. kackhart · 04. Sep 2007, 00:00

> **Zitat von: Colibri am 03. Sep 2007, 22:18**
>
> Die Tricks:
> - Nicht das Brennen ist der Engpass sondern die serielle Schnittstelle -> Also nicht unnötig Daten übertragen.

deswegen ist es ja so schade, dass er das hier ohne den uart0_send bei mir nicht ordentlich macht (denke aber das prob dafuer gerade erkannt zu haben und hoffe das weglassen zu koennen).

> **Zitat**
>
> - Ein kleines Tool wird über ISP-Bootloader mit 38400 Bit/s geladen.
> - Das Tool setzt dann die typische Betty PLL-Frequenz und läd den Rest des Tool mit 115200 Bit/s nach.

gut, das mache ich ja genau so ...

> **Zitat**
>
> - Vor dem Flashen lasse ich vom Tool die SHA-1 Hashwerte der 19 Sektoren ermitteln und zum PC schicken (geht schnell - nur wenig Daten über RS232).
> - Von Quellfile werden am PC auch die SHA-1 Hashwerte der 19 Sektoren ermittelt.
> - Dann werden nur die Sektoren mit unterschiedlichem Hashwert gelöscht und programmiert (das ist bei AGB-Patch nur ein Sektor - deshalb nur 35 Sekunden Gesamtzeit).

ok, sektor support muss bei mir sicher noch rein! zieht man mal 10 sec fuer ram write und crc ab, bleiben 25 sec. grob gepeilt (auf wohl sektoren ja unterschiedlich gross sind) brauchst du dann fuer den kompletten flash (btw, du koenntest noch checken ob data 0xffff ist und einfach abbrechen. habe gerade ausprobiert, so 15 bis 17 der while(1) durchlaeufe braucht hier ein word write) grob 8 min. da ich ja quasi doppelt daten via uart sende koennte ich 16 min verkraften, fehlen noch knapp 10.

und da faellt mir gerade ein, fuer den hash liest du ja auch noch den sektor aus, dafuer muesste man auch noch zeit abziehen .

ich muss wohl noch ein wenig lernen!

danke fuer input!

gru3,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg290#msg290)

---

<a id="msg291"></a>

## 33. kackhart · 04. Sep 2007, 01:18

> **Zitat von: kackhart am 04. Sep 2007, 00:00**
>
> deswegen ist es ja so schade, dass er das hier ohne den uart0_send bei mir nicht ordentlich macht (denke aber das prob dafuer gerade erkannt zu haben und hoffe das weglassen zu koennen).

was ein tcflush und ordentliches warten auf chip erase bewirkt (kann nun die byte replies lassen!) ...

hackbard@staubsauger:~/projects/arm/betty$ time sudo ./lpcload -d /dev/ttyS0 -f fwflash.hex -b -w hacked.bin
boot loader init ...
write firmware to ram ...
unlock go command ...
go ...
flushing lpc tx buffer: 30 f7
writing firmware to flash ...
D'OH ...ffff0

real    1m49.532s
user    0m0.132s
sys     0m0.192s
hackbard@staubsauger:~/projects/arm/betty$

das einzige was fwflash wie gesagt macht ist keine 0xffff words schreiben und lpcload (uebertraget immer 16 byte grosse bloecke) sendet erst garkeine schreibkommandos wenn alle davon den wert 0xff haben.

ich glaube ich verzichte auf sektor support, da ich die alternativ fw eh erstmal immer nur ins ram laden werde zum testen.

gru3,

frank

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg291#msg291)

---

<a id="msg292"></a>

## 34. netguy · 04. Sep 2007, 02:03

uebrigens,

bei 0x8002309C ist eine routine, die die sc infos ausgibt. fuer jedes feld wird R1 und R0 geladen, dann 0x800359AC aufgerufen, dort findet wohl dann das auslesen der einzelnen felder aus dem sc chip statt. der aufruf nach 0x80034D64 is lediglich fuer die ausgabe der strings ueber einen bios callback da (callback kommando 0x26C in R12).

die font sektion ist in etwa so strukturiert (basis ist 80010000, ich gebe ab hier nur die offsets an):

0x04 -> anzahl der fonts (3)
0x10 -> wahrscheinlich pruefsumme
0x28 -> info-struktur ueber die fonts, array mit 3 tabellen:
 0. font typ?
 1. start-adresse der fon-bitmaps
 2. adresse der character map, die auf entsprechende eintraege in der indextabelle verweist
 3. tabbelle der zeichenbreiten
 4. tabelle der inizies zu den einzelnen zeichen
 5. weitere hints, wir startzeile des zeichens
 6. immer 0x0

fuer die waves ab basis 0x800B0000:

0x04 -> anzahl der waves
0x2C wave info, array mit 9 tabellen zu je drei eintraegen:
 0. typ des waves? immer 0x1F40
 1. laenge des waves
 2. startadresse des waves im flash

gruss,

chris

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg292#msg292)

---

<a id="msg863"></a>

## 35. eme · 27. Mär 2008, 10:15

@ kackhart ?
hast du das foto der tastaturbelegung ([http://hackdaworld.org/pics/betty/betty_buttons.jpg)](https://web.archive.org/web/2012/http://hackdaworld.org/pics/betty/betty_buttons.jpg)) auch in groß?

[Permalink](http://bettyhacks.com/forum/index.php?topic=18.msg863#msg863)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
