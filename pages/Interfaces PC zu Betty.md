# Interfaces PC zu Betty

Man braucht eine [serielle Schnittstelle](http://de.wikipedia.org/wiki/RS-232#Datenrahmen_und_Timing) mit 3V oder 5V-Pegel (Direkt oder über USB-Umweg), um mit den entsprechenden [Programmen](Tools.md "Tools") die Firmware auf die Betty ([Betty_Hardware#Anschlussbelegung](Betty%20Hardware.md "Betty Hardware")) zu übertragen .

## RS232-Schnittstellenwandler

Benutzen meist Pegelwandler-ICs wie MAX3232. Bettys Spannungsversorgung ist 3V. Daher kann man den Standard MAX232 nicht ohne zusätzliche Spannungsversorgung (5V) verwenden.

- Handy-Datenkabel  
  Zählen fast immer hierzu, siehe unten

<!-- -->

- [Int. USB und Laderegler](Int.%20USB%20und%20Laderegler.md "Int. USB und Laderegler")  
  USB2Serial Wandler zum einbauen in die Betty.

<!-- -->

- [Simple Serial Interface](Simple%20Serial%20Interface.md "Simple Serial Interface")  
  Funktional identisch zum NXP ISP, aber Aufbau auf Lochrasterplatine (Einfacher für den Hobbybastler)

<!-- -->

- [Very Simple Serial Interface](Very%20Simple%20Serial%20Interface.md "Very Simple Serial Interface")  
  Funktional identisch Simple Serial Interface, aber nur mit Transistoren, kein Pegelwandler-IC notwendig

<!-- -->

- [SCART-Betty-Kombiinterface](SCART-Betty-Kombiinterface.md "SCART-Betty-Kombiinterface")  
  Mit dem [SCART-Betty-Kombiinterface](SCART-Betty-Kombiinterface.md "SCART-Betty-Kombiinterface") können nicht nur wie bei den bisher verfügbaren Interfaces mit der Betty, sondern auch mit dem [SCART Adapter](SCART%20Adapter.md "SCART Adapter") Daten ausgetauscht werden.

<!-- -->

- NXP ISP  
  Der NXP ISP besteht aus einem Standard TTL Wandler der die RTS / CTS Leitungen zum Resetten/Boot Enable benutzt.  
  <http://www.grautier.com/grautier/index.php?/archives/51-Betty-Hardware-Teil-4-NXPisp-Adapter.html> (01:32 - 18.09.2007)  
  [Link zum Flash Magic](http://www.flashmagictool.com/)

<!-- -->

- [Stk500](Stk500.md "Stk500")  
  Mit dem STK500-Entwicklungsboard von Atmel könnt ihr eure Betty ohne jegliche Bastelarbeit flashen.

## USB-Seriell-Wandler

Man kann auch USB-seriell Wandler ohne RS232-Pegel benutzen. Im besten Fall unterstützen sie auch Handshake-Signale. Dazu eignen sich spezielle ICs (FT232R, ..), es geht auch mit einigen Handy-Datenkabeln.

***Achtung:*** Fertige Adapter mit USB und RS232-Steckern müssen geöffnet und Kabel direkt an den (FT232/PL2303-)Wandlerchip angelötet werden, da hier der Pegel anschließend wieder auf +-12V gewandelt wird. Handydatenkabel umgehen dies. Anschlusspunkte am Chip siehe z.B.: [FTDI FT232BM Datenblatt](http://www.ftdichip.com/Documents/DataSheets/DS_FT232BM.pdf) ; [PL2303 Datenblatt](http://user.chollian.net/~mines/pl2303.pdf)

  
Ein recht günstiges USB zu RS232 Interface als Bausatz mit per Jumper wählbarem 3,3V und 5V Pegel auf FT232RL Basis: [USB Uart Adapter](https://www.it-wns.de/themes/kategorie/detail.php?artikelid=168&kategorieid=1&source=1)

Herausgeführt auf eine Stiftleiste sind RXD und TXD, sowie die IO-Spannung (also 3,3 bzw. 5V), Masse und ein 12MHz Takt des FT232RL. Wer sich nicht scheut, SMD zu löten (was er ja sowieso muß, da es ein Bausatz ist...), kann auch die restlichen Signale vom FT232RL abnehmen, also RTS/CTS, DSR/DTR, DCD und RI.

Kleiner Tip für den Aufbau: Die Platine ist im HAL Verfahren verzinnt (Hot Air Leveling), d.h. das Zinn wird bei der Fertigung mit heißer Luft von der Platine "geblasen" - es bleibt aber noch reichlich davon drauf. Zum Verlöten (vor Allem des FT232) Löthonig auf die Pads bringen (***BITTE AUF KEINEN FALL LÖTFETT NEHMEN !!!***), den Chip auflegen und mit der gereinigten Spitze eines Lötkolbens einfach die Beinchen in das Lot drücken - das reicht in aller Regel für einen einwandfreien Kontakt aus, am Besten mit einer Lupe kontrollieren.

## Umbau von Handy-Datenkabeln

Hierzu sind alle Datenkabel (Seriell oder auch USB) geeignet, deren zugehörige Handys seriell mit 3,3V oder 5V-Pegel angesprochen werden. Erkennen lässt sich das an den Signalbezeichnungen RX und TX in der Pinbelegung des Handysteckers (Über Google zu finden). Das sind u.a. Siemens C25-S65, Nokia 3210, 3310, 5110, 8110, Motorola T191 und fast alle anderen die nicht per USB (Handyseitig) angebunden sind. USB-Kabel für Nokia's mit dem neueren "Pop-Port" gehen z.B. NICHT da hier 4 Adern zu einer USB-Schnittstelle direkt am Handy laufen, ohne Wandler! Die älteren Modelle (aus der Zeit als jedes Modell seine eigene Anschlussnorm bekam) funktionieren dagegen praktisch immer.

Ist ein Kabel gefunden, Stecker zerlegen und mit der Pinbelegung (Pinout) des Steckers feststellen welche Ader TX, RX und GND(Masse/Minus) ist. Im Falle eines Original Siemens-Datenkabels kommt noch eine Ader für die 3,3V aus der Betty dazu, andere Schaltungen versorgen sich aus dem PC. Zur Steckerbelegung siehe auch hier: [Siemens](http://www.nobbi.com/steck_s25.html) [Nokia](http://www.nobbi.com/steck_nok.html)

[\[1\]](http://www.grautier.com/grautier/uploads/Elektronik/Betty/RIMG0001.JPG) zeigt die Belegung des Betty-Programmiersteckers, als Kupplung ein Stück von dem Reichelt-Artikel "[BL 2X10G 2,54](http://www.reichelt.de/?;ACTION=3;LA=4;GROUP=C142;GROUPID=3221;ARTICLE=6074;)" abgeschnitten und er passt.

RX, TX, GND werden 1:1 durchverbunden, ggf. auch noch 3,3V. Die "Bootloader Enable"-Leitung von Betty (am Stecker) muss noch mit GND verbunden werden damit sie in den Softwareupdatemodus geht wenn unser Kabel dransteckt. Wird auch der Terminalmodus benötigt, muss ein Schalter in diese Verbindung eingefügt werden.

Dies ist die einfachste Version eines Betty Interfaces, zum Starten des Bootloaders wird der Stecker aufgesetzt und die Batterien eingelegt. Zum Starten der Software nach dem Update das Kabel abziehen, und kurz eine der Batterien entfernen.

## Problembehebung

Es kam bei einigen Usern mit verschiedenen Handykabelmodellen zu dem Problem dass im Hyperterminal problemlose Übertragung funktioniert, aber Betty-Heaven nur **"RX: Timeout"** meldet. Boardmember "nitpicker" fand eine Lösung:

Ein zusätzlicher PullUp-Widerstand von 4,7 kiloOhm zwischen "TX" und "3,3V" am Betty-Stecker hilft ihr auf die Sprünge.

Siehe auch [LPCTool#Lpctool-Probleme](LPCTool.md "LPCTool").

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

