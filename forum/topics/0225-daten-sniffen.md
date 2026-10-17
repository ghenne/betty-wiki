---
title: "Daten Sniffen"
topic_id: 225
board: "Software"
board_id: 6
posts: 15
first_post: "12. Dezember 2009, 16:14"
last_post: "06. Januar 2010, 17:31"
authors: ["Telekatz", "asgard"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=225.0"
---

# Daten Sniffen

[← Software](../boards/06-software.md) · Thema 225 · 15 Beiträge · 12. Dezember 2009, 16:14 – 06. Januar 2010, 17:31

Beteiligt: Telekatz, asgard

---

<a id="msg1526"></a>

## 1. asgard · 12. Dezember 2009, 16:14

Hi,
nach dem ich endlich seit langem mal wieder Zeit für meine Betty habe, wollte ich mal kurz fragen, ob und ggf. wie ich den Datentransfer zwischen 2 Geräten belauschen kann.
Das ganze findet auf 434 MHz statt. Bei dem verbauten Chip handelt es sich um den PT4316-s (Datenblatt im Anhang).
Was ich sicher weiß, ist das der Datentransfer nur in eine Richtung abläuft und vollkommen unverschlüsselt ist.

Ich würde nun gerne Dauerhaft den Datenverkehr abfangen/mitlesen und ihn am Rechner auswerten.
Was würdet ihr mir empfehlen....den Scart oder besser den TAE-Adapter...ich brauch nur die Rohdaten...die Verarbeitung kann ich dann hoffentlich am Rechner erledigen...
Würde mich über ein paar Tipps sehr freuen...

Viele Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1526#msg1526)

---

<a id="msg1529"></a>

## 2. Telekatz · 13. Dezember 2009, 10:53

Hallo Asgard,

ich würde den Scart Adapter nehmen. Ist Firmwaretechnisch besser erschlossen und hat seine eigene Stomversorgung.

Für den CC1100 kannst du ja mal die Einstellungen von tugstugi [http://bettyhacks.com/forum/index.php?topic=223.0](0223-funksteckdose.md) zum sniffen probieren.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1529#msg1529)

---

<a id="msg1531"></a>

## 3. asgard · 13. Dezember 2009, 11:02

Danke!
Sobald mein Scart wieder läuft werde ich das mal probieren

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1531#msg1531)

---

<a id="msg1540"></a>

## 4. asgard · 16. Dezember 2009, 20:21

> **Zitat von: Telekatz am 13. Dezember 2009, 10:53**
>
> Für den CC1100 kannst du ja mal die Einstellungen von tugstugi [http://bettyhacks.com/forum/index.php?topic=223.0](0223-funksteckdose.md) zum sniffen probieren.

Vielleicht kannst du mir kurz erklären, wie ich genau vorgehen muss, wenn ich die Einstellungen für den CC1100 in die Firmware übernommen habe...wie komme ich denn dann an die Rohdaten?
Werden die direkt über RX/TX ausgegeben?
Oder muss ich die Firmware noch erweitern/umschreiben um eine Art Sniffer zu bekommen?

Hab da leider (noch) keinen Plan von....

Viele Grüße
Asgard

*« Letzte Änderung: 16. Dezember 2009, 20:27 von asgard »*

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1540#msg1540)

---

<a id="msg1541"></a>

## 5. Telekatz · 16. Dezember 2009, 22:45

Mit diesen Einstellungen wird das Packet Handling des CC1100 ausgeschaltet. Beim Empfangen werden die Daten dann über einen der GDO Pins (konfigurierbar) ausgegeben.

Schau dir mal in der aktuellen Boop die Funktion RF_viewer im Testmenue an. Dort wird demonstriert, wie man die Rohdaten auslesen kann. 

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1541#msg1541)

---

<a id="msg1544"></a>

## 6. asgard · 17. Dezember 2009, 07:59

Hi Telekatz,
erst mal vielen Dank für das neue Release und die darin enthaltenen neuen Funktionen.

Ich hab mir jetzt mal die Funktion "RF viewer" in der Betty angeschaut.
Da ich in der näheren Umgebung scheinbar viele 433 bzw. 434 MHz Sender habe,
sehe ich dort gaaaaanz viele Daten...

Wie kann ich denn erkennen, welche Daten von welchem Gerät gesendet wurden?
Irgendwie müssen die Geräte ja wissen, welche Daten für sie selber interessant/relevant sind.

Kann man die Daten irgendwie filtern?

Viele Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1544#msg1544)

---

<a id="msg1546"></a>

## 7. Telekatz · 17. Dezember 2009, 12:01

Wie tugstugi im anderen Thread geschrieben hat, etwas mit den AGCCTRL Registern herumprobieren . Das Gerät das du belauschen möchtest sollte das stärkste Signal sein das die Betty empfängt. Bei entsprechend eingestellten AGCCTRL Registern sollte dan hauptsächlich dieses Signal durchkommen.

Versuche herauszufinden ob das Gerät vor den Daten ein Syncwort sendet und wie das aussieht. Untersuche per software den Datenstrom auf das Syncwort und triggere darauf den Empfang. Siehe dazu auch das Beispiel vom FS20 Decoder.  Dort wird auf mindestens 10 hintereinanderfolgende Pulse von 600-1000µs Länge gewartet. Folgt darauf ein Puls von 1000-1400µs wird der Datenempfang gestartet.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1546#msg1546)

---

<a id="msg1547"></a>

## 8. asgard · 24. Dezember 2009, 15:00

Hi Telekatz,
danke für die Hilfe.

Ich bin zwischenzeitlich soweit, dass ich wirklich nur noch die Daten, die ich brauche, empfange.
Das ganze mach ich mit der Betty.
Ich lass mir die Daten dann über den RS232-Port der Betty an den Rechner ausgeben und zeichne sie dort auf (über den RFViewer).

Nun wollte ich fragen, ob bzw. wie ich diese aufgenommenen Daten per Betty "versenden"/"simulieren" kann.

Viele Grüße und frohe Weihnachten
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1547#msg1547)

---

<a id="msg1548"></a>

## 9. Telekatz · 25. Dezember 2009, 11:21

Hi Asgard,

Die Daten senden geht so ähnlich wie Daten einlesen. Gleiche Konfiguration des CC1100 und mit cc1100_strobe(STX); auf Senden schalten.  Dann die Daten im zeitlich richtigen Abstand auf den GDO0 Pin ausgeben. Dabei bedeuten GDO0=0 Signal wird gesendet, GDO0=1 kein Signal wird gesendet. Beispiel dazu siehe lirc.c und infraredirq.c.

Wenn deine Daten nicht zu komplex und zu lang sind, kannst du auch ein entsprechendes LIRC Confi File dafür erstellen und sie damit senden.

Gruß und frohe Weihnachten
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1548#msg1548)

---

<a id="msg1553"></a>

## 10. asgard · 28. Dezember 2009, 21:18

Hi Telekatz,
danke für die ausführliche Hilfe!

Jetzt hab ich alles entsprechend angepasst, bekommen aber folgende Fehlermeldung beim kompilieren:

error: invalid lvalue in assignment

In der Zeile steht:
GDO0=1;  //Kein Signal wird gesendet - Low

Wie muss ich das denn korrekt angeben?

VIele Grüße und nochmal vielen Dank für deine Geduld!
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1553#msg1553)

---

<a id="msg1554"></a>

## 11. Telekatz · 28. Dezember 2009, 23:59

Ausgang auf Low:
FIOCLR0 = GDO0;

Ausgang auf High:
FIOSET0 = GDO0;

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1554#msg1554)

---

<a id="msg1560"></a>

## 12. asgard · 06. Januar 2010, 11:29

Hi,

zwischenzeitlich habe ich einige Tests mit den gesnifften Daten gemacht.
Leider funktioniert das ganze noch nicht.

Ich vermute, dass ich ein Timing-Problem habe.

Mein Aufbau sieht momentan folgendermaßen aus:

2 Bettys
-> eine sendet die gesnifften Daten (die ich analysieren möchte und ganz zu Anfang aufgezeichnet habe)
-> zweite snifft die Daten, die Betty 1 verschickt, mit

Damit kann ich prüfen, ob die Daten korrekt gesendet wurden.

Nun ist es aber leider so, dass die Daten, die Betty 1 sendet, komplett anders aussehen als die ursprünglich zu analysierenden Daten.

Hier mal mein Code für den Versand der Daten per Funk:

`void RF_viewer_6_10_senden(void) {

 unsigned int i=1;
 char replay[]="000000000000000000000000000000000000001111000011111000011000000001100000000011111110000001111111110000000001111110000000111111100000011111111100000000011111110000111001111100001111111111100000000000111111111110000000000011111110000000011111110000000111111100000011111111100000000000111111111000000000111111111000000001111111110000000001111111110000000011110000111111111001";
//Die Daten der Variable replay wurden hier stark gekürzt. Bei mir sind es insgesamt 19700 Nullen und Einsen

 lcd_fill(0);
 set_font(BOLDFONT);
 draw_string(0, 0, "RF viewer-senden", 3, DRAW_PUT);
 draw_block(0,10,128,2,3,DRAW_PUT);
 set_font(SMALLFONT);

 RFasyncmode_6(true);

 cc1100_write1(AGCCTRL2,0x03);
 cc1100_write1(AGCCTRL1,0x00);
 cc1100_write1(AGCCTRL0,0x92);

 cc1100_strobe(STX);

 serial_init();  //baud 230400

 while(KEY_Exit) {};

  for (i=1;i<19700;i++)
  {
   waitus(10);

   if(replay[i]=='0')
   {
    FIOCLR0 = GDO0;  //Kein Signal wird gesendet - Low
   } else {
    FIOSET0 = GDO0;  //Signal wird gesendet - High
   }
  }

 RFasyncmode_6(false);
}`

Hier mal mein Code für das sniffen der Daten:

`void RF_viewer_6_10(void) {
 unsigned char row = 0;
 unsigned char col = 16;

 lcd_fill(0);
 set_font(BOLDFONT);
 draw_string(0, 0, "RF viewer-sniffen", 3, DRAW_PUT);
 draw_block(0,10,128,2,3,DRAW_PUT);
 set_font(SMALLFONT);

 RFasyncmode_6(true);

 cc1100_write1(AGCCTRL2,0x03);
 cc1100_write1(AGCCTRL1,0x00);
 cc1100_write1(AGCCTRL0,0x92);

 cc1100_strobe(SFRX);
 cc1100_strobe(SRX);

 serial_init();  //baud 230400

 while(KEY_Exit) {};
 while(!KEY_Exit)
 {

  waitus(10);

  if((FIOPIN0 & GDO2))
  {
   serial_putc('0'); //Low
  } else {
   serial_putc('1'); //High
  }

 }

 RFasyncmode_6(false);
}`
Hat jemand eine Idee, warum das ganze nicht korrekt funktioniert?

Viele Grüße
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1560#msg1560)

---

<a id="msg1561"></a>

## 13. Telekatz · 06. Januar 2010, 16:13

`serial_init();  //baud 230400`
Bei einer Baudrate von 230400 dauert die Übertragung eines Zeichens etwa 43 µs. Eine Abtastung des Signals alle 10µs funktioniert desshalb nicht.

Ausserdem sollte man, um die Abtastrate auch wirklich genau einzuhalten, die IRQs deaktivieren. Die Tastaturabfrage und waitus() funktionieren dann allerdings nicht mehr.

Was ist das eigentlich für ein Gerät, dessen Daten du aufzeichnen möchtest?

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1561#msg1561)

---

<a id="msg1562"></a>

## 14. asgard · 06. Januar 2010, 16:49

Hi,

> **Zitat von: Telekatz am 06. Januar 2010, 16:13**
>
> Bei einer Baudrate von 230400 dauert die Übertragung eines Zeichens etwa 43 µs. Eine Abtastung des Signals alle 10µs funktioniert desshalb nicht.

kann man die Übertragung irgendwie beschleunigen?
Oder die Daten intern zwischenspeichern und sie nach und nach an den PC per RS232 übertragen.

> **Zitat von: Telekatz am 06. Januar 2010, 16:13**
>
> Ausserdem sollte man, um die Abtastrate auch wirklich genau einzuhalten, die IRQs deaktivieren. Die Tastaturabfrage und waitus() funktionieren dann allerdings nicht mehr.

wie kann ich die IRQs  denn deaktivieren und trotzdem das timing einhalten (also waitus nutzen) ?

Viele Grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1562#msg1562)

---

<a id="msg1563"></a>

## 15. Telekatz · 06. Januar 2010, 17:31

Übertrag die Daten nicht Bitweise sondern Byteweise. Dann musst du nur noch alle 80µs ein Byte übertragen.

Folgende Version von waitus() sollte bei ausgeschalteten IRQs funktionieren:
`void waitus(unsigned long d) {

 unsigned long x;

 x=(T0TC+d)%5000;

 if(x<T0TC)
  while(x<T0TC);
 while(x>T0TC);

}`

[Permalink](http://bettyhacks.com/forum/index.php?topic=225.msg1563#msg1563)

---

## Verwandte Themen

- [Funksteckdose](0223-funksteckdose.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
