---
title: "Betty Hardwareauflistung"
topic_id: 53
board: "Hardware"
board_id: 5
posts: 6
first_post: "08. Sep 2007, 23:01"
last_post: "30. Apr 2008, 21:33"
authors: ["Spessi", "Telekatz", "bettyuser", "starshiner"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=53.0"
---

# Betty Hardwareauflistung

[← Hardware](../boards/05-hardware.md) · Thema 53 · 6 Beiträge · 08. Sep 2007, 23:01 – 30. Apr 2008, 21:33

Beteiligt: Spessi, Telekatz, bettyuser, starshiner

---

<a id="msg323"></a>

## 1. Spessi · 08. Sep 2007, 23:01

Habe im Wiki mal ein Bild + Beschreibung der Betty Einzelteile gemacht. Ich werde heute Abend noch größtenteils Links zu den Datasheets dazu machen, darum bitte ich, dass keiner bis 1-2 Uhr editiert. Danke

Ansonsten seid ihr herzlich eingeladen euer Wissen im Wiki kundzugeben und die Liste auszufüllen

[http://www.bettyhacks.com/wiki/index.php/Betty_Hardware](../../pages/Betty%20Hardware.md)

[Permalink](http://bettyhacks.com/forum/index.php?topic=53.msg323#msg323)

---

<a id="msg326"></a>

## 2. starshiner · 09. Sep 2007, 11:39

Oben die Sicherheit zu haben, es gleich ins Wiki schreiben zu können:

Bei den Punkten 5 und 6 dürfte es sich um einen MosFet und ein Schaltregler IC handeln. Beides nicht so interessant, das man da jetzt einen Aufstand für machen müsste...

[Permalink](http://bettyhacks.com/forum/index.php?topic=53.msg326#msg326)

---

<a id="msg753"></a>

## 3. bettyuser · 08. Feb 2008, 00:10

Hallo,

habe mal ne Frage zu dieser Hardwareauflistung, insbesondere zur IR-Diode.
Wie darf man die Auflistung IR senden, IR an/aus und IR empfangen verstehen?
Wie ist der genaue Anschluss zum LPC? IR senden und IR an/aus ist doch eigentlich das gleiche.
Ist also Pin 4 und Pin 84 mit einem UND-Gater verknüpft und zur IR-Diode geführt?
Die Info wäre interessant um das IR senden weiter zu entwickeln und die Betty lernfähig zu machen, also auch IR-Empfang zu ermöglichen.
Oder gibt es eigentlich schon Bestrebungen den IR-Empfang zu ermöglichen?

Danke.

[Permalink](http://bettyhacks.com/forum/index.php?topic=53.msg753#msg753)

---

<a id="msg758"></a>

## 4. Telekatz · 08. Feb 2008, 21:56

Hallo,

mit IR an/aus schaltest du zwischen senden und empfangen um.

Zum Senden muss Pin 84 auf High sein. Dann kann man über Pin 4 etwas senden.
Zum Empfangen schaltet man Pin 84 auf Low. Die Daten werden dann über Pin 32 eingelesen.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=53.msg758#msg758)

---

<a id="msg1009"></a>

## 5. bettyuser · 30. Apr 2008, 20:35

Hallo telekatz,

ich habe mal wieder eine Frage zu diesem Thema.
Seit einiger Zeit ist ja nun IR-Empfang in Boop implementiert, wenn auch leider nur testweise.
Bei der Durchsicht der Sourcen habe ich aber nirgendwo entdeckt, dass der Pin 84, also Port P0.12, bedient werden würde. Also stelle ich mir die Frage wie denn nun zwischen IR-Transmit und IR-Receive umgeschaltet wird.
Woher hast Du eigentlich Dein Wissen, kannst Du denn hierzu mal einen kleinen Schaltplanausschnitt zur Verfügung stellen?

Ich würde die Betty auch mal gerne soweit bringen, dass sie lernfähig ist.
Aber mir ist leider die Verdrahtung nicht ganz klar und ich finde auch die völlig unkommentierte Datei ir_decoder.c ziemlich unverständlich.

Gruss
bettyuser

Edit:
Sorry, war wohl eine alte Version von boop, in der aktuellen Version scheint P0.12 doch verwendet zu werden.
Trotzdem die Frage nach dem Schaltplanausschnitt?!

*Last Edit : 30. Apr 2008, 20:54 by bettyuser*

[Permalink](http://bettyhacks.com/forum/index.php?topic=53.msg1009#msg1009)

---

<a id="msg1010"></a>

## 6. Telekatz · 30. Apr 2008, 21:33

Hallo bettyuser,

nach meinen neusten Erkenntnissen dient P0.12 zu ein und ausschalten des IR empfangs (nicht zum umschalten zwischen senden und empfangen).

Einen Schaltplan habe ich nicht, die Infos hab ich aus dem WIKI und durch ausprobieren herausgefunden.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=53.msg1010#msg1010)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
