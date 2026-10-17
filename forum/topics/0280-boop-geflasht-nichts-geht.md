---
title: "Boop geflasht, nichts geht ?"
topic_id: 280
board: "Software"
board_id: 6
posts: 41
first_post: "02. Okt 2012, 08:55"
last_post: "30. Mär 2013, 10:24"
authors: ["0xDEAD", "Axel", "OCMoe", "Telekatz", "Torsten", "bastler", "chcatz", "chefpro", "eazee", "femto", "gunnar", "maselx", "mx", "swausd"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=280.0"
---

# Boop geflasht, nichts geht ?

[← Software](../boards/06-software.md) · Thema 280 · 41 Beiträge · 02. Okt 2012, 08:55 – 30. Mär 2013, 10:24

Beteiligt: 0xDEAD, Axel, OCMoe, Telekatz, Torsten, bastler, chcatz, chefpro …

---

<a id="msg2011"></a>

## 1. maselx · 02. Okt 2012, 08:55

Hallo,
ich hoffe das hier nochmal wer vorbeikommt und mir helfen kann.

Ich hab mir bei Pollin mal eben 5 Bettys bestellt, ich fand das doch sehr interessant was so möglich ist.
Wir haben 2xDbox2-mit linux und eine fritzbox 7170.
Leider hab ich nicht beachtet das es keine anleitungen zur Boob firmware gibt.

Also das Flashen Kabel basteln war ok. Ich brauchte nen 4,7k Wiederstand, im Wiki steht das der auf 3,3V - TX soll, im forum fand ich aber dann die lösung das der an 3,3V-RX gehört, das war die richtige lösung.

Nun ich kann endlich flashen, ich hab verschiedene Boop.bin gefunden und ausprobiert, nur  geht außer ein schönes Bootlogo nichts.

Was muss ich nun machen?
 Ich hoff das mir noch wer helfen kann.

MfG Marcel

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2011#msg2011)

---

<a id="msg2012"></a>

## 2. gunnar · 02. Okt 2012, 09:00

Hi Marcel,

in einem anderen jüngeren Forumsbeitrag steht, dass die Bettys von Pollin wohl aus der Schweiz sind. Such mal im Forum nach Problemen mit Schweizer Bettys, ich meine beim Stöbern mal etwas in dieser Richtung gelesen zu haben.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2012#msg2012)

---

<a id="msg2014"></a>

## 3. maselx · 02. Okt 2012, 10:26

Ich  hab den beitrag gefunden, der dort probleme hatte hatt eine HW03 Betty.
Hab nachgeschaut und es sind HW02 die von Pollin kommen.
Könntest du vieleicht eine Funktionierende Boop version Flash1und2 aus einer Betty auslesen, die ich mal testhalber flashen kann.

Das Logo geht ja nur reagiert die Betty auf keine Taste.
Oder giebt es eine art tastensperre wie bei Handys ?
Oder muss ich selbst noch irgendwie funktionen einfügen und dann flashen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2014#msg2014)

---

<a id="msg2016"></a>

## 4. gunnar · 02. Okt 2012, 11:08

Hallo Marcel,

eigentlich sollte nach dem Startbild schon das normale Menü kommen. Da muss man nichts spezielles machen. Ich habe meinen Betty Kram momentan verstaut, ich versuche aber zeitnah mal eine Betty zu flashen und Dir dann das Image zukommen zu lassen. Ich meine, dass die eingecheckten Images bei mir funktioniert haben, das überprüfe ich aber noch.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2016#msg2016)

---

<a id="msg2017"></a>

## 5. maselx · 02. Okt 2012, 12:10

Supi ist echt nett von dir.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2017#msg2017)

---

<a id="msg2018"></a>

## 6. maselx · 02. Okt 2012, 12:23

also wenn ich einen COM TerminalEmulator benutze die Betty resette kommt beim starten:

Erasing Sector: 0x820D0000 +> OK

als ausgabe hat das was zu bedeuten ?

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2018#msg2018)

---

<a id="msg2020"></a>

## 7. maselx · 02. Okt 2012, 16:31

Hab da noch nen bissl gesucht  :'(

Pollin Bettys sind Swisscom Bettys mit HW V2 Boop geht nicht da wohl
die Tastaturmatrix anders ist.

[http://bettyhacks.com/forum/index.php?topic=128.0](0128-swisscom-betty.md)

[http://www.mikrocontroller.net/topic/199655](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/199655) so ab der mitte.

wer weiss wies geht ?

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2020#msg2020)

---

<a id="msg2022"></a>

## 8. femto · 06. Okt 2012, 20:57

Hab mir gerade selbst eine Boop-Version für meine Swisscom-Betty von Pollin gebaut, kannst es ja mal damit versuchen!

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2022#msg2022)

---

<a id="msg2023"></a>

## 9. gunnar · 06. Okt 2012, 21:28

Hallo,

wenn der Test mit der Swisscom Betty erfolgreich ist, kann ich die Änderungen in einem eigenen Branch einchecken. Später kann man dann durch defines dafür sorgen, dass man einen Source hat der für beide Hardware-Varianten kompilierbar ist.

BTW. Hat es eigentlich schon jemand geschafft, mit einer aktuellen Toolchain ein funktionierendes Boop zu bauen? Die im Wiki empfohlene ist ja mittlerweile recht angestaubt...

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2023#msg2023)

---

<a id="msg2024"></a>

## 10. femto · 06. Okt 2012, 22:28

> **Zitat von: gunnar am 06. Okt 2012, 21:28**
>
> Hallo,
>
> wenn der Test mit der Swisscom Betty erfolgreich ist, kann ich die Änderungen in einem eigenen Branch einchecken. Später kann man dann durch defines dafür sorgen, dass man einen Source hat der für beide Hardware-Varianten kompilierbar ist.

Ähm, das entsprechende Define ist doch schon in den Quellen enthalten ...

> **Zitat von: gunnar am 06. Okt 2012, 21:28**
>
> BTW. Hat es eigentlich schon jemand geschafft, mit einer aktuellen Toolchain ein funktionierendes Boop zu bauen? Die im Wiki empfohlene ist ja mittlerweile recht angestaubt...

Für meinen Build habe ich auch noch die alte Toolchain genommen, ich kann mich aber durchaus auch mal an einer neueren versuchen ...

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2024#msg2024)

---

<a id="msg2025"></a>

## 11. maselx · 06. Okt 2012, 23:17

Hi,
habs gleich mal getestet und ist Top !!!     
Ist es den möglich das sich Boop selbst ensprechend konfiguriert beim starten? Bei Info steht auch
HW 02 also erkennen tut es ja schon.

Ich hatte auch schon die woche mich versucht, ist aber schon daran gescheitert was in Linux zu installieren. Ich bin halt absolut Windows eingstellt, also hatte ich mir ne live CD von ubuntu desktop besorgt aber wie gesagt es scheitert schon am instalieren.

Könnt mir wer  vieleicht ein fertig installierte entwicklungsumgebung als .iso machen die ich mit VMware oder als LifeCD/USB starten kann. Darf auch alte software sein hauptsache funktionabel.

Die Wiki ist halt für einen Window gesteuerten zu mager. Ich hab lang gesucht aber kein "make" gefunden. Verzeichnisse sind geschützt mann braucht root rechte "wie"? usw.
Hab großes interesse an projekte wie oszi, servo steuerung, funksteckdosen usw.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2025#msg2025)

---

<a id="msg2030"></a>

## 12. mx · 09. Okt 2012, 09:52

> **Zitat von: maselx am 06. Okt 2012, 23:17**
>
> Ist es den möglich das sich Boop selbst ensprechend konfiguriert beim starten? Bei Info steht auch HW 02 also erkennen tut es ja schon.

Ja, das sollte kein großes Problem sein.

Momentan wird die Tastaturmatrix per #define in keyboard/keyboard.h beim Compilieren festgelegt. Wenn man das so umbaut, daß beide Varianten eincompiliert werden, kann man zur Laufzeit anhand des Rückgabewerts von GetHWversion() entscheiden, welche davon verwendet werden soll.

Ich werde mir das anschauen, sobald ich überhaupt mal dazu komme, etwas mit boop zu machen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2030#msg2030)

---

<a id="msg2031"></a>

## 13. femto · 09. Okt 2012, 12:08

> **Zitat von: mx am 09. Okt 2012, 09:52**
>
> Momentan wird die Tastaturmatrix per #define in keyboard/keyboard.h beim Compilieren festgelegt. Wenn man das so umbaut, daß beide Varianten eincompiliert werden, kann man zur Laufzeit anhand des Rückgabewerts von GetHWversion() entscheiden, welche davon verwendet werden soll.
>
> Ich werde mir das anschauen, sobald ich überhaupt mal dazu komme, etwas mit boop zu machen.

Ich kann das gerne übernehmen, ist kein Problem für mich!

Ist denn sichergestellt, dass alle Bettys mit HW Version 02 automatisch von der Swisscom sind? Was ist mit der HW Version 01, welche Tastaturmatrix soll hier verwendet werden?

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2031#msg2031)

---

<a id="msg2032"></a>

## 14. mx · 09. Okt 2012, 12:45

> **Zitat von: femto am 09. Okt 2012, 12:08**
>
> Ich kann das gerne übernehmen, ist kein Problem für mich!

Super! Ich hatte mir vorgestellt, das Ergebnis von GetHWversion() am Anfang in einer globalen Variablen zu cachen, damit die Bitshifterei nicht jedes Mal wiederholt werden muß. Die kann dann überall verwendet werden, wo die Hardwareversion im Code berücksichtigt werden muß.

> **Zitat**
>
> Ist denn sichergestellt, dass alle Bettys mit HW Version 02 automatisch von der Swisscom sind?

Die Frage ist doch nicht, wer welche Version vertrieben hat, sondern ob die Tastaturen bei allen 02er und 03er Boards jeweils gleich verschaltet sind, und ich denke, davon können wir ausgehen. Deshalb sollte im Code auch der Begriff Swisscom besser nicht mehr auftauchen, sondern nur auf die jeweilige Hardwareversion Bezug genommen werden.

> **Zitat**
>
> Was ist mit der HW Version 01, welche Tastaturmatrix soll hier verwendet werden?

Gibt es diese Hardware denn überhaupt in der freien Wildbahn? Gelesen habe ich noch nichts darüber, deshalb denke ich, daß das wohl eher ein Prototyp war, den wir nicht weiter berücksichtigen müssen.

Generell sehe ich zwei Wege: entweder wir verwenden die eine Matrix für alle Versionen unter 3 und die andere für alle ab 3 oder wir zeigen bei allen Versionen außer 02 und 03 eine entsprechende Meldung an. Letzteres würde dem "principle of least surprise" entsprechen, weil jemand, der Boop auf eine andere HW-Version flasht (falls es solche wirklich gibt), eine klare Ansage bekommt, vorausgesetzt, die Display-Ansteuerung ist gleich, aber man könnte die Meldung ja auch zusätzlich noch seriell ausgeben.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2032#msg2032)

---

<a id="msg2033"></a>

## 15. femto · 09. Okt 2012, 14:59

> **Zitat von: mx am 09. Okt 2012, 12:45**
>
> Generell sehe ich zwei Wege: entweder wir verwenden die eine Matrix für alle Versionen unter 3 und die andere für alle ab 3 oder wir zeigen bei allen Versionen außer 02 und 03 eine entsprechende Meldung an. Letzteres würde dem "principle of least surprise" entsprechen, weil jemand, der Boop auf eine andere HW-Version flasht (falls es solche wirklich gibt), eine klare Ansage bekommt, vorausgesetzt, die Display-Ansteuerung ist gleich, aber man könnte die Meldung ja auch zusätzlich noch seriell ausgeben.

Ich würde es ebenfalls bevorzugen wenn die Betty eine Meldung ausgibt (Display falls möglich & über die serielle Schnittstelle), falls ihr eine unbekannte HW-Version unterkommt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2033#msg2033)

---

<a id="msg2036"></a>

## 16. chefpro · 11. Okt 2012, 19:34

Hallo femto,

hast du mal eine gebaute Version zum testen.
Der Source wäre auch gut.

Ich würde gerne die Oszi Software anpassen und mit Deiner Vorarbeit sollte ich das am Wochenende schaffen.

Danke, Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2036#msg2036)

---

<a id="msg2037"></a>

## 17. chefpro · 12. Okt 2012, 08:56

Hallo femto,

hab gesehen, dass da schon eine gebaute Version ist von Dir.

Ich war nicht eingeloggt und konnte das nicht sehen.

Der Source wäre trotzdem schön.

Vielen Dank, Peter

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2037#msg2037)

---

<a id="msg2038"></a>

## 18. femto · 12. Okt 2012, 17:55

Hi Peter,

sorry. hatte diese Woche tierisch viel zu tun, aber ich schau mal das ich heute Abend die automatische Umschaltung eingebaut bekomme ...

Gruss,

~ Hans-Dieter ~

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2038#msg2038)

---

<a id="msg2039"></a>

## 19. Telekatz · 12. Okt 2012, 18:21

> **Zitat von: mx am 09. Okt 2012, 12:45**
>
> Generell sehe ich zwei Wege: entweder wir verwenden die eine Matrix für alle Versionen unter 3 und die andere für alle ab 3 oder wir zeigen bei allen Versionen außer 02 und 03 eine entsprechende Meldung an. Letzteres würde dem "principle of least surprise" entsprechen, weil jemand, der Boop auf eine andere HW-Version flasht (falls es solche wirklich gibt), eine klare Ansage bekommt, vorausgesetzt, die Display-Ansteuerung ist gleich, aber man könnte die Meldung ja auch zusätzlich noch seriell ausgeben.

Du kannst davon ausgehen, dass bei Hardwareversion <=2 die Swisscom Matrix und bei Hardwareversion >=3 die andere Matrix verwendet wird.

Es scheint so, als ob es noch mindestens eine Hardwareversion 4 geben müsste. Die hat aber einen anderen Displaycontroller. Eine Ausgabe auf dem Display würde da nicht funktionieren. Diese Version war aber vermutlich nie im Umlauf.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2039#msg2039)

---

<a id="msg2040"></a>

## 20. femto · 12. Okt 2012, 20:05

> **Zitat von: Telekatz am 12. Okt 2012, 18:21**
>
> Du kannst davon ausgehen, dass bei Hardwareversion <=2 die Swisscom Matrix und bei Hardwareversion >=3 die andere Matrix verwendet wird.

Ok, soll ich das so einbauen?

Und wie sieht es im Fehlerfall aus, soll ich trotzdem versuchen eine Warnung auf dem Display auszugeben?

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2040#msg2040)

---

<a id="msg2041"></a>

## 21. Telekatz · 12. Okt 2012, 22:09

Bau das so ein und lass die Warnung auf dem Display weg. Die ist unnötig.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2041#msg2041)

---

<a id="msg2057"></a>

## 22. Torsten · 17. Nov 2012, 14:52

Hi,

ich habe meine Pollin-Betty jetzt mit dem hier angehängten ROM geflasht. Leider funktioniert bei mir das Tasten-Kreuz (um den OK-Button) nicht sauber. Hoch und Runter werden teilweise nicht angenommen oder als Links/Rechts interpretiert.
Tritt das nur bei mir auf oder ist das ein bekannter Fehler?

Gruß
  Torsten

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2057#msg2057)

---

<a id="msg2058"></a>

## 23. swausd · 18. Nov 2012, 13:41

Hallo Torsten,

dieses Verhalten habe ich auch beobachtet. Bei mir tritt es auf, wenn ich die Tasten fest durchdrūcke. Wenn nur leicht gedrückt wird, funktionieren sie zuverlässiger.

Gruß

Siegfried

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2058#msg2058)

---

<a id="msg2060"></a>

## 24. Torsten · 18. Nov 2012, 13:46

Hi,

ein bischen besser geht es dann, aber eine Lösung ist das nicht. Die Frage ist jetzt, ob das ein HW-Problem ist, oder ob man das per SW lösen kann.
Habe die original-FW leider nicht genug ausprobiert, deswegen weiß ich nicht, ob das Problem schon vor dem Flashen vorhanden war.

Gruß
  Torsten

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2060#msg2060)

---

<a id="msg2062"></a>

## 25. Axel · 20. Nov 2012, 23:23

Hallo,

hier mal mein erster Beitrag.

Es gibt m. Meinung nach einen Fehler im keyirq.c

Es muss heissen:
#ifdef SWISSCOM
        IOSET2= (126<<18);   // Alle Port 2 Ausgaenge physikalisch auf 1 setzen
        IO2_P = (1<<18);      // In IO2_P ist jeweils ein Bit gesetzt  (erstmal das auf pin 18)
        IO2_0=0;           // Wird zum shiften von keys[0] verwendet
        IO2_1=0;
        keys[0]=0;
        keys[1]=0;
        for(IO2_PC=18;IO2_PC<=24;IO2_PC++)     // Durch alle P2 durch jeweils ein P2 bit loeschen, Wert abfragen und wieder setzen
        {
                        IOCLR2 = IO2_P;       // Physikalisch clearen eine Leitung wird gelöscht
                        keys[0] |= ((IOPIN1>>16) & 0xF)<<IO2_0;     // Resultat an Pin1 abfragen default is all one (no key pressed)
                        keys[1] |= ((IOPIN1>>21) & 0x3)<<IO2_1;     // Resultat an Pin1 abfragen (obere hälfte)
                        IO2_0 +=4;     // nun das Resultat schiften
                        IO2_1 +=2;     // nun das Resultat schiften
                        IOSET2 = IO2_P;        // Nun wieder setzen, alle P2 sind wieder 1
                        IO2_P = (IO2_P<<1);
        }
        IOCLR2 = (127<<18);     // P2 Ausgaenge wieder alle löschen
        keys[0]= (~keys[0]) & 0x0fffffff;       // Resultat ist jetzt invertiert
        keys[1]= (~keys[1]) & 0x00003fff;
#else

d. h. die letzten beiden Zeilen vor dem #else waren falsch. So wie es vorher war, (also mit   keys[0]= (~keys[0]); ) konnte keys niemals 0 werden, so dass die Tastaturentprellung in den späteren Zeilen nicht vernünftig funktioniert hat.

So scheint es bei mir jetzt zu gehen (zumindest das Kreuz, Rest muss ich noch mal testen).

Gruss
Axel

*Last Edit : 21. Nov 2012, 23:26 by Axel*

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2062#msg2062)

---

<a id="msg2066"></a>

## 26. 0xDEAD · 22. Nov 2012, 13:19

Hallo Axel,

wäre es möglich dass Du dein Rom-Image zur Verfügung stellst, ich habe nämlich genau das selbe Problem.

Gruß,
0xDEAD

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2066#msg2066)

---

<a id="msg2068"></a>

## 27. maselx · 22. Nov 2012, 17:38

Ich hatte das mit den tasten als normal abgestellt 
Es wäre natürlich schöner wenn es besser geht.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2068#msg2068)

---

<a id="msg2071"></a>

## 28. Axel · 22. Nov 2012, 20:05

Bitte schön.

Allerdings habe ich festgestellt, dass das das Problem nicht löst. Dafür löst es das Problem, dass die IR Signale nicht stoppen. Ich hatte bei einigen beide Probleme.

Das Problem mit dem Kreuz kann man lösen, indem man den Ausschnitt in der schwarzen Abdeckung mit einem Messer etwas (also so 1/4 mm) vergrössert, so dass das "Kreuzteil" der Gummiplatte mehr Platz hat. 

Übrigens findet man unter LIRC neue Fernbedienungen für x10  (das ist eine Fernbedienung, die über Funk und USB Empfänger an den PC geht ) sowie Tevion (Aldi Funksteckdosen). Bei der Tevion kann man über Lautstärke  und Programm jeweils Steckdosen für A und B steuern. 

Sources stelle ich zur Verfügung, sobald die ausreichend getestet sind.

Gruss
Axel

*Last Edit : 22. Nov 2012, 22:54 by Axel*

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2071#msg2071)

---

<a id="msg2072"></a>

## 29. 0xDEAD · 23. Nov 2012, 13:01

Hallo Alex,

erstmal Danke! - mit der X10 Funktion hast Du einen Wunsch erfüllt, den ich noch gar nicht geäusert hatte!

aber leider funktioniert das mit den Tasten bei meinen beiden Bettys noch nicht zuverlässig - ab und zu werden immer noch Menüeinträge übersprungen, oder der Tastendruck wird gar nicht erkannt.

Gruß, 57005

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2072#msg2072)

---

<a id="msg2073"></a>

## 30. Axel · 23. Nov 2012, 22:06

Wie ich schon schrieb, gibt es zwei Probleme.

1. Die Führung der Wippe/Kreuz ist zu eng. Dadurch kippt der Ring nicht und drückt nur einen der vier Knöpfe, sondern man drückt mit dem "Unten" Knopf praktisch diesen ganzen Ring runter, so dass die anderen Knöpfe auch Kontakt bekommen. Bei mir habe ich das gelöst, indem ich mit einem Messer die Öffnung für den Ring, der das Kreuz bildet, etwas vergrössert habe, so dass der tatsächlich kippt und nur den einen Knopf aktiviert, auf den man drückt. Ich habe vier Bettys, das Problem trat bisher bei zweien auf, bei einer nicht. 

2. Die Software hat den oben erwähnten Bug, der dazu führt, dass die Erfassung der Knöpfe nicht richtig funktioniert. Bei mir hat das teilweise dazu geführt, dass die Sendesequenz nie gestoppt hat. Ob das auftritt, hängt aber anscheinend auch vom verwendeten IR-Code ab.

Gruss
Axel

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2073#msg2073)

---

<a id="msg2074"></a>

## 31. bastler · 26. Nov 2012, 19:28

Kann es sein das mit der letzten Version Boob_rom von Axel sich die Betty nicht mehr Flashen lässt?
Der Flashspeicher lässt sich mit Betty Haeven auch nicht mehr auslesen. Bei meiner anderen Betty geht es problemlos.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2074#msg2074)

---

<a id="msg2075"></a>

## 32. Axel · 27. Nov 2012, 22:06

Ich verwende nur lpctool, kann Bettyheaven daher nicht beurteilen.

Aber mit lpctool (Linux) habe ich es gerade noch mal probiert, geht einwandfrei.

Gruss
Axel

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2075#msg2075)

---

<a id="msg2077"></a>

## 33. bastler · 28. Nov 2012, 18:53

Hallo Axel,
danke für die schnelle Antwort. Linux hab ich im Moment nicht, also wird das wohl länger dauern das ich es damit ausprobieren kann. Vieleicht hat sich ja auch die Betty gerade da verabschiedet.
Drauf ist ja die neue Firmware, und die Tasten funktionieren in jedem Fall besser. Sogar unter TestStuff das Sound Testprogramm geht erstmals mit der Swisscom.
Danke.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2077#msg2077)

---

<a id="msg2088"></a>

## 34. OCMoe · 09. Dez 2012, 09:36

Moin!

> **Zitat von: Axel am 22. Nov 2012, 20:05**
>
> Das Problem mit dem Kreuz kann man lösen, indem man den Ausschnitt in der schwarzen Abdeckung mit einem Messer etwas (also so 1/4 mm) vergrössert, so dass das "Kreuzteil" der Gummiplatte mehr Platz hat. 

Ich habe auch ein Paar Pollin-Bettys bestellt und dieses Problem. Dank deines Hinweises ist es besser, aber nicht wirklich gut. Ich habe übrigens 400er-Schleifpapier genommen, damit wird es absolut sauber und gratfrei, so dass man keinerlei Nachbearbeitung sieht.

Da wir noch ein größeres Projekt vor haben, hab ich mir noch 2 16er-Kartons von asgard bestellt und konnte so direkt HW2 und HW3 vergleichen. Bei HW3 ist in der Gummimatte im Steuerkreuz zwischen je zwei "Tasten" noch ein Noppen als Abstandhalter. Die verhindern, dass angrenzende Tasten fälschlich mit gedrückt werden. Es handelt sich also eindeutig um einen Hardwarefehler, der nicht vollständig behebbar ist. Dafür ist das HW3-Steuerkreuz aber auch schwergängiger.

> **Zitat von: Axel am 22. Nov 2012, 20:05**
>
> Sources stelle ich zur Verfügung, sobald die ausreichend getestet sind.

Also ich hätte da großes Interesse dran, denn ich würde gerne eine Idee ausprobieren, um das Steuerkreuz zuverlässiger zu machen: Wenn man das Steuerkreuz softwaremäßig speziell entprellt, so dass immer nur der erste Tastendruck des Steuerkreuzes zählt und als "durchgehend gedrückt" gewertet wird, solange noch *irgendeine* Steuerkreuztaste aktiv ist. Eine andere Steuerkreuz-Taste zählt erst wieder, wenn eine gewisse Zeitspanne gar keine Steuerkreuz-Taste gedrückt war. Das müsste eigentlich ganz solide funktionieren, denn ich vermute/hoffe mal, dass die tatsächlich gedrückte Richtung immer als erstes Ereignis auftritt und erst danach die falschen Tastendrücke kommen. Als praktiablen Workaround eignet sich das bestimmt, besonders da das HW2-Tastengefühl wirklich angenehmer ist.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2088#msg2088)

---

<a id="msg2089"></a>

## 35. Axel · 09. Dez 2012, 13:33

Den Teil mit der Steuerkreuzansteuerung hatte ich hier schon gepostet, steht in der ersten Seite des Threads.

Alleridings habe ich mit den unterschiedlichen Ansteuerungen auch schon experimentiert. Aber die Reihenfolge der Kontakte hat leider keinen echten Bezug zur gedrückten Richtung. Es kann sein, dass man "Runter" drückt und der "Rechts" die ganze Zeit kontaktiert bleibt. Leider kann das auch umgekehrt passieren.

Beim Originalprogramm ist das anscheinend kein Problem, da wird das Kreuz kaum genutzt.

Gruss
Axel

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2089#msg2089)

---

<a id="msg2090"></a>

## 36. OCMoe · 09. Dez 2012, 15:48

Ärgerlich. Wie hast du das Diagnostiziert? Hast du mal über einen längeren Zeitraum alle Tasten-Events Protokolliert? Vielleicht gibt es ja doch noch ein brauchbares Muster, das man erkennen kann. Selbst wenn es nicht perfekt wird, wäre eine Verbesserung des Verhaltens wünschenswert.

Wie wäre es damit: Bei meinen zwei bisher getesteten Swisscom-Bettys ist "Links" völlig sauber, nur "Rechts" macht Probleme, d.h. Bei Hoch/Runter kommt fälschlicherweise auch Rechts mit, und bei Rechts kommen Hoch oder Runter mit. Angenommen, man wartet mit dem Erzeugen eines Tastenevents etwas, vielleicht 10ms. Wenn in der Zeit "hoch/rechts" kommt, wird "Runter" gewertet, bei "hoch/rechts" wird "Hoch" genommen, und bei "hoch/runter/rechts" ist es eben "Rechts".

Ich befürchte, dass das auch nicht ganz sauber ist, daher die Frage nach der Protokollierung.  Existieren da bereits Daten? Es kann ja einfach über Seriell ausgegeben werden zur Auswertung auf dem PC.  Mit Swisscom-Quelltext *hint, hint* würd ich ja selber mal experimentieren

Alternativ kann man sich fragen, ob es irgendeine andere Hardware-Maßnahme gibt, mit der man die Abstandsnoppen ersetzten/nachahmen kann. Irgendwas einzukleben scheint mir nicht stabil genug, aber irgendwas muss doch gehen. Wenn nur der 3D-Drucker schon fertig gebaut wäre

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2090#msg2090)

---

<a id="msg2093"></a>

## 37. eazee · 09. Dez 2012, 22:26

Hallo Axel,

würde es dir was ausmachen, mal die X10 "config" hier zu veröffentlichen?
Hab das gerade mal ausprobiert, bei mir gehen nur 2 Tasten, hätte gerne mal die hex-codes gesehen...

Danke im Voraus,
eazee

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2093#msg2093)

---

<a id="msg2094"></a>

## 38. OCMoe · 10. Dez 2012, 01:27

So, nochmal zum Tastenkreuz: Das Problem hat mich nicht losgelassen. Ich habe etwas experimentiert und habe eine gescheite Lösung gefunden.

Das Tastenkreuz der Swisscom-Betty lässt sich mit einer einfachen Modifikation vollständig in Ordnung bringen:

Aus einem Kabelbinder (eine schmale Sorte, 2,5mm Breite) schneide man 4 Stücke zu je ca. 15mm ab und legt diese hintereinander auf einen Streifen Tesafilm (auf die klebende Seite natürlich). Danach wickelt man das Tesafilm eng um die Kabelbinder-Stücke und schneidet an den Enden das überstehende Tesafilm ab. Das Resultat sieht dann wie ein Stück Kabelbinder mit 3 Tesafilm-Scharnieren aus. Dieses formt man zum Quadrat und legt es um den OK-Knopf unter das Tastenkreuz. Das verhindert, dass benachbarte Tasten fälschlicherweise mit gedrückt werden.

Streng genommen sollten schon 3 Segmente ausreichen, ich hab es jedenfalls nur mit 3 gemacht und diese zu einem eckigen "U" geformt. Wenn das Steuerkreuz danach zu schwer geht bzw. einige Tasten gar nicht oder immer gedrückt sind, dann ist entweder der Kabelbinder zu breit oder man hat beim Tesafilm-Wickeln nicht eng genug gewickelt. Ich habe nun keine Fehlbetätigungen mehr.

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2094#msg2094)

---

<a id="msg2095"></a>

## 39. Axel · 10. Dez 2012, 19:03

Hier die X10 Config

/*
    infrared codes for X10 remote control
    Copyright (C) 2009  <telekatz@gmx.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

/*pre_data*/            0x00000000,
/*post_data*/           0x00000000,
/*toggle_bit_mask*/     0x80800000,
/*gap*/                         4500,
/*repeat_gap*/          0,
/*bits*/                        16,
/*pre_data_bits*/       0,
/*post_data_bits*/      5,
/*rc6_bit*/                     0,
/*frequency*/           0x00101234,             // 433,9198 MHz
/*flags*/                       LIRC_RF,
/*header*/                      2600,1600,
/*three*/                       0,0,
/*two*/                         0,0,
/*one*/                         500,1600,
/*zero*/                        500,500,
/*plead*/                       0,
/*ptrail*/                      0,
/*foot*/                        0,0,
/*pre*/                 0,0,
/*post*/                        0,0,
/*repeat*/                      0,0,
/*min_repeat*/          0,
/*duty cycle*/          0,

{
        0x0000, // A            ->
        0x0000, // B            ->
        0x0000, // C            ->
        0x0000, // D            ->
        0x0000, // Betty        ->
        0xF520, // Exit         ->      Back
        0x6F9A, // Up           ->      UP
        0xF722, // Down         ->      Down
        0x729D, // Left         ->      Left
        0xF41F, // Right        ->      Right
        0x739E, // OK           ->      OK
        0x5E89, // Vol+         ->      Vol+
        0xDD08, // Vol-         ->      Vol-
        0xD500, // Mute         ->      Mute
        0x608B, // Prog+        ->      Prog+
        0xE10C, // Prog-        ->      Prog-
        0x628D, // 1            ->      1
        0xE30E, // 2            ->      2
        0x648F, // 3            ->      3
        0xE510, // 4            ->      4
        0x6691, // 5            ->      5
        0xE712, // 6            ->      6   
        0x6893, // 7            ->      7
        0xE914, // 8            ->      8
        0x6A95, // 9            ->      9
        0xEC17, // 0            ->      0
        0xF520, // -/--         ->      back   
        0x6D98, // AV           ->      Rec TV   
        0xD904, // Menu         ->      DVD-Menue
        0x88B3, // PiP          ->      subtitle 
        0xD0F2, // A/B          ->      Input     TBD
        0x0934, // 16:9         ->      Angle   
        0x84AF, // Info         ->      Info 
        0x86B1, // VTX1         ->      Guide
        0x58A7, // VTX2         ->    q.view    TBD
        0x8AB5, // VTX3         ->      Title
        0xFD28, // Blue         ->      STOP 
        0x7EA9, // Yello        ->      Pause 
        0x7AA5, // Green        ->      Play 
        0x7CA7, // Red          ->      Record
        0xF11C, // TV           ->      LifeTV
        0xD702  // Power        ->      Power
},

Gruss
Axel

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2095#msg2095)

---

<a id="msg2096"></a>

## 40. eazee · 10. Dez 2012, 19:51

Hallo Axel,

tausend Dank. Werde ich gleich mal ausprobieren bei mir.
Das sind die codes vom MD8800, richtig?

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2096#msg2096)

---

<a id="msg2113"></a>

## 41. chcatz · 30. Mär 2013, 10:24

Hallo Axel,

deine Swisscom Version funktioniert super.
Hatte bei mir die lirc xbox360 config eingebaut, das funktioniert auch,
nur ist die Betty jetzt mit den .svn Sourcen sehr träge und der "Sound Test " hängt sich auf.
Kannst Du vielleicht deine Änderungen für die Swisscom hier zur Verfügung stellen ?

Danke
chcatz

... hier die config für die xbox360

[Permalink](http://bettyhacks.com/forum/index.php?topic=280.msg2113#msg2113)

---

## Verwandte Themen

- [Swisscom Betty](0128-swisscom-betty.md)
- [Bettys bei Pollin](0279-bettys-bei-pollin.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
