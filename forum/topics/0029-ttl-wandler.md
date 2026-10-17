---
title: "TTL-Wandler"
topic_id: 29
board: "Hardware"
board_id: 5
posts: 33
first_post: "08. Aug 2007, 15:46"
last_post: "12. Nov 2007, 23:31"
authors: ["Gentoo07", "Megabug", "Phönix", "Spessi", "TonyMahony", "alterego", "asgard", "theborg", "vSaAmTp"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=29.0"
---

# TTL-Wandler

[← Hardware](../boards/05-hardware.md) · Thema 29 · 33 Beiträge · 08. Aug 2007, 15:46 – 12. Nov 2007, 23:31

Beteiligt: Gentoo07, Megabug, Phönix, Spessi, TonyMahony, alterego, asgard, theborg …

---

<a id="msg167"></a>

## 1. Phönix · 08. Aug 2007, 15:46

Wie wärs mal eine schöne Umbauanleitung für den Pollin hier zu erstellen?

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg167#msg167)

---

<a id="msg168"></a>

## 2. asgard · 08. Aug 2007, 17:01

Hi,

Spessi wollte das machen,...er hatte ja auch damit angefangen   

Der kommt aber erst wieder am Samstag(?) aus dem "Urlaub",...ich denke er wird sich danach darum kümmern.

Vielleicht kann aber auch einer der Anderen, die sich etwas besser auskennen (z.b. hackbart, borg oder so ^^) was dazu sagen 

Grüße
Asgard

*Last Edit : 08. Aug 2007, 17:09 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg168#msg168)

---

<a id="msg171"></a>

## 3. theborg · 08. Aug 2007, 17:24

hi bei Spessi auf der seite ist eine Anleitung alternativ gibt es bei pollin nen c25 Datenkabel (USB) das kanste auch dafür nutzen ist im entefekt auch billiger

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg171#msg171)

---

<a id="msg172"></a>

## 4. asgard · 08. Aug 2007, 17:31

Hi,

> **Zitat von: theborg am 08. Aug 2007, 17:24**
>
> hi bei Spessi auf der seite ist eine Anleitung alternativ gibt es bei pollin nen c25 Datenkabel (USB) das kanste auch dafür nutzen ist im entefekt auch billiger

leider ist die anleitung auf der Seite von Spessi (noch) falsch und funktionsuntüchtig.
Auf pollin.de konnte ich kein passendes USB kabel entdecken, hast du mir vielleicht kurz die artikelnummer?

danke und grüße
asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg172#msg172)

---

<a id="msg174"></a>

## 5. theborg · 08. Aug 2007, 18:14

hm ok des hat sich wohl erledigt hab grade durchgesucht scheint net mehr vorhanden zu sein

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg174#msg174)

---

<a id="msg177"></a>

## 6. asgard · 09. Aug 2007, 07:32

Hi Zusammen, hi Borg,

würde das hier gehen?
[USB-Datenkabel - Ebay Nummer1](https://web.archive.org/web/2012/http://cgi.ebay.de/USB-DATENKABEL-SIEMENS-A35-C35-C45-S35-S45-SL45-C25-M50_W0QQitemZ190139234814QQihZ009QQcategoryZ13441QQssPageNameZWDVWQQrdZ1QQcmdZViewItem)

bzw. das
[USB-Datenkabel - Ebay Nummer2](https://web.archive.org/web/2012/http://cgi.ebay.de/SIEMENS-USB-DATENKABEL-C25-C28-C35-C35i-C45-C45i_W0QQitemZ180144799807QQihZ008QQcategoryZ111305QQssPageNameZWDVWQQrdZ1QQcmdZViewItem)

oder die Platine:
[RS232-TTL](https://web.archive.org/web/2012/http://cgi.ebay.de/Konverter-Mit-MAX232-RS232-TTL-fur-PIC-ATMEL-AVR_W0QQitemZ120149693735QQihZ002QQcategoryZ12949QQssPageNameZWDVWQQrdZ1QQcmdZViewItem)

Grüße
asgard

*Last Edit : 09. Aug 2007, 07:56 by asgard*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg177#msg177)

---

<a id="msg178"></a>

## 7. vSaAmTp · 09. Aug 2007, 10:21

[SerCon Datenblatt](https://web.archive.org/web/2012/http://mikrocontroller.cco-ev.de/files/SerCon_Anleitung_V0_2.pdf)

[Shop](https://web.archive.org/web/2012/https://cco-ev.de/mikrocontroller/index.php?main_page=product_info&cPath=69&products_id=195&zenid=b526a2555f31a4a22e8278c25a362351)

Der geht auch. Ich denk das bei anderen Projekten noch mehr so Wandler gibt.

Was pollin angeht: [810036](https://web.archive.org/web/2012/http://www.pollin.de/shop/shop.php?cf=detail.php&pg=NQ==&a=MzY5OTgxOTk=) in die Suche dort eingeben und Schwups findet man es dort.

Dazu von Herta aus dem IP-Phone Forum:
> **Zitat**
>
> Das IC ersetzte ich durch ein MAX3232 , da dieses auch mit 3,3V arbeitet. Ich benutzte einen MAX3232CPE. Wichtig ist vor allem
> die Bauform (DIL-16).
> Zusätzlich musste ich folgende Elkos wechseln (bezieht sich auf den
> Schaltplan und den Platinenaufdruck von dem Bausatz):
>
> C3 durch 0,1 microFarad
> C1,C2,C4 0,47 microFarad
>
>
> Die Orientierung der Elkos bleibt jeweils gleich.
> Es ist natürlich darauf zu achten das RXD und TXD zwischen zum Endgerät
> hin gekreuzt werden.

Was den Pegelumsetzer angeht:
[Infos drüber](https://web.archive.org/web/2012/http://www.elektronik-kompendium.de/public/riederer/max232.htm)
Wie ich da lese, ist ein 2ter Kanal noch verfügbar. Wenn man nun diesen Kanal als Schalter nutzt für die Betty?
Denk das ist auch das was theborg in seinem [NXP ISP Nachbau](0013-nxp-isp-nachbau.md) macht

> **Zitat**
>
> ...Standard ttl Wandler und dann eine Leitung um per SW Bootloader enable und reset zu schaltun...

Hab ein wenig gelesen. Pin 4 am RS232 wäre DTR und ein Ausgang. Den könnt man doch als Schalter nutzen.
[http://de.wikipedia.org/wiki/RS232](https://web.archive.org/web/2012/http://de.wikipedia.org/wiki/RS232)
> **Zitat**
>
> Über diese Leitung signalisiert der PC dem Gerät, dass er betriebsbereit ist. Damit kann ein Gerät eingeschaltet oder zurückgesetzt werden. (Üblicherweise schaltet ein Gerät z.B. Modem diese Leitung auf DSR durch, wenn es einsatzbereit ist)

Pin 6 (DSR) als bestätigung, das es auch geschalten ist
> **Zitat**
>
> Ein angeschlossenes Gerät signalisiert dem Computer, dass es einsatzbereit (nicht notwendigerweise empfangsbereit) ist, wenn eine logische Null auf dieser Leitung anliegt.

Progger sind ja im Board. Die Pins werden beim RS232-TTL Wandler auch nicht benutzt (z. B bei dem Pollin Teil ).

*Last Edit : 09. Aug 2007, 13:02 by vSaAmTp*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg178#msg178)

---

<a id="msg179"></a>

## 8. theborg · 09. Aug 2007, 17:53

Hi jup die beiden Ports sind frei wenn man Tools wie Flash magic oder das Philips flash Tool nutzen möchte kann man über DTR/RTS, CTS/RTD den RESET b.z.w. Bootloader Enable steuern da der MAX aber nur einen weiteren Eingang hat (der andere ist ein Ausgang) muss mann dann zusetzlich noch direkt eine ader vom pc auf einen Transistor legen. Schaltplan dafür ist ja hier im forum

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg179#msg179)

---

<a id="msg181"></a>

## 9. vSaAmTp · 09. Aug 2007, 18:49

[http://grautier.com/temp/betty/NXPisp.png](https://web.archive.org/web/2012/http://grautier.com/temp/betty/NXPisp.png)

Meinste die Schaltung?

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg181#msg181)

---

<a id="msg182"></a>

## 10. theborg · 09. Aug 2007, 19:29

jo die ist leider noch nicht ganz perfekt denke mal am we wird sie fertig

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg182#msg182)

---

<a id="msg183"></a>

## 11. vSaAmTp · 09. Aug 2007, 19:32

Welche Version von dem Philips Flash Tool nutzt Du? Die wo ich hab, unterstützt den LPC nicht.

[Flash Magic Homepage](https://web.archive.org/web/2012/http://www.flashmagictool.com/)
[Philips Flash Tools Homepage](https://web.archive.org/web/2012/http://www.standardics.nxp.com/products/lpc2000/all/~LPC2220/#LPC2220)

[Das Philips Flash Tool hab ich gesaugt](https://web.archive.org/web/2012/http://www.nxp.com/products/microcontrollers/support/development_tools/general/includes/arm7tdmi2200/isp_sw.html)

*Last Edit : 09. Aug 2007, 19:36 by vSaAmTp*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg183#msg183)

---

<a id="msg185"></a>

## 12. theborg · 10. Aug 2007, 18:20

jup aber das Magic Tool unterstützt es

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg185#msg185)

---

<a id="msg186"></a>

## 13. vSaAmTp · 10. Aug 2007, 18:59

Hab ich gesehen. Dachte das es mit dem Philips Tool eben auch geht, da Du das als Beispiel geschrieben hast.

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg186#msg186)

---

<a id="msg193"></a>

## 14. Spessi · 12. Aug 2007, 20:40

Okay, hab den Fehler gefunden - meine Bauteilliste auf der Seite ist richtig. Zusätzlich muss aber noch ein 10k Widerstand zugelegt werden, der zwischen RX und 3,3V geschaltet wird. Danke an theborg.

Edit: Mh, anscheinend klappts doch nich so - werde morgen nochmal berichten.
Ah ok. man muss nicht von RX auf 3,3V (wobei das wohl auch nicht schadet) sondern von TX auf 3,3V mit dem Widerstand. Dann klappts. Also die Teile auf meiner Seite PLUS 2 Widerstände (10k) für TX und RX (vermutlich reicht auch nur einer für TX)

*Last Edit : 12. Aug 2007, 23:41 by Spessi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg193#msg193)

---

<a id="msg478"></a>

## 15. TonyMahony · 07. Nov 2007, 22:24

Bevor ich mich völlig verrückt mache, mal n paar blöde Fragen zum Max3232CPE:

Ich würde das Kombiinterface gerne nachbauen, allerdings leicht modifiziert.
Daher wollte ich den Kram erstmal in Eagle hacken und etwas hin und her schieben.

Wenn ich da den MAX3232CPE einfüge, sieht der TTL allerdings wie bei grautier aus ([http://grautier.com/temp/betty/NXPisp.png),](https://web.archive.org/web/2012/http://grautier.com/temp/betty/NXPisp.png),) aber in dem Colibri-PDF zur Kombiplatine ([http://colibri.de.ms/Scart-Betty-Kombiinterface.pdf)](https://web.archive.org/web/2012/http://colibri.de.ms/Scart-Betty-Kombiinterface.pdf)) hat der noch VCC und GND.

Parallel hab ich dann mal den Burschen bei Reichelt rausgesucht ([http://www.reichelt.de/?;ACTION=6;LA=3;ARTICLE=9398;GROUPID=2914;GROUP=A217)](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=6;LA=3;ARTICLE=9398;GROUPID=2914;GROUP=A217)) und die beiden Datenblätter dort machen die Verwirrung für mich perfekt.

Was stimmt denn jetzt?
14 Pins, 16 Pins, 18 Pins und wie beschaltet?
Das wäre meines Erachtens schon nicht ganz unwichtig für ein geschicktes Platinenlayout, oder etwa nicht?

Steinigt mich bitte nicht, falls ich hier völligen Käse schreibe - ich stehe hier noch ziemlich am Anfang und hab zwar Löterfahrung, aber eher mit Bausätzen und da hat mich die Schaltung bisher nicht groß interessiert...

EDIT: Lasst mich raten - die Nummern an den Beinchen ham nen bestimmten Sinn... Ich schau mir das nochmal an!

EDIT2: Ok - der mit den 18 Beinchen ist scheinbar was anderes (3222 - lesen müsste man können!).
Die Reihenfolge wird dann wohl die sein wie bei Reichelt, also 1-8 und 9-16.
Bleiben zwei Fragen: Warum sind die Beinchen in Eagle in ner anderen Reihenfolge drangepinselt als sie wirklich vorkommen und warum gibt Eagle mir nur 14 Beinchen und Colibri bekommt 16? Das ist doch unfair...

*Last Edit : 07. Nov 2007, 22:49 by TonyMahony*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg478#msg478)

---

<a id="msg481"></a>

## 16. theborg · 08. Nov 2007, 05:47

[http://grautier.com/temp/betty/NXPisp.png](https://web.archive.org/web/2012/http://grautier.com/temp/betty/NXPisp.png) hi bei der schaltung ziht er sich vcc + gnd aus der betty siehe board da ist der pinheader 1:1 durchverdratet

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg481#msg481)

---

<a id="msg482"></a>

## 17. TonyMahony · 08. Nov 2007, 11:39

Arg - ich Idiot!
Auf dem Bild hat er ja Pin 15 und 16 oben noch extra abgebildet.
Hätte ich mal meine Augen aufgemacht!^^

Dann nehme ich jetzt mal die Grautier-Variante und versuche im Eagle, die zur Kombiplatine zu machen.

Mal ein paar Fragen am Rande:
Ist das Kombiinterface sinnvoll oder gibt es da einen besseren Stand der Technik?

Was mir vorschwebt ist ein Interface für Scart, IP-Adapter, Modem und Betty.
Könnt ihr schon Aussagen treffen, ob es möglich sein wird, auf seriellem Wege mit dem IP-Adapter und dem Modem Kontakt aufzunehmen?

Dann schließen sich direkt weitere Fragen an *nerv*:
Ich konnte im Datenblatt zum IP-Adapter nicht erkennen, welche Versorgungsspannung benötigt wird - passen da auch die 3,3V?
Reichen dann zum Ansprechen RxD0, TxD0, GND, Vcc und Reset?
Habt ihr irgendeine Ahnung, wofür der restliche Kram ist?
Habe ich es richtig verstanden, dass Reset mit + und nReset mit - geschaltet werden?

Beim Modem sind ja noch einige Pins nicht dokumentiert.
Mit GND, Vcc und nReset kommt man sicher noch nicht sehr weit. Ist der andere Kram brauchbar?
Ist es sinnvoll, einfach mal eine Modemschnittstelle vorzusehen, in der Annahme, dass sich zwei der Pins irgendwie als RxD und TxD oder sonstwie nutzbar entpuppen?

Entschuldigt bitte, dass ich Euch hier so bombardiere, aber ich muss erstmal irgendwie nen Einstieg ins Thema finden...

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg482#msg482)

---

<a id="msg484"></a>

## 18. alterego · 09. Nov 2007, 05:54

du kannst auch gern alternativ das simple serial interface nutzen, gibts schon länger in der version 2 die die gleiche funktionalität wie die von theborg bietet, gibts fertig als eagle-layout und mit lochmaster-layout. Vorteil: es wird etwas mehr wert auf sicherheit der schaltung und des com-port gelegt.

ich werds heut abend mal ins wiki packen.

*Last Edit : 09. Nov 2007, 07:43 by alterego*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg484#msg484)

---

<a id="msg485"></a>

## 19. alterego · 09. Nov 2007, 07:40

So!

Simple Serial Interface V2 ist im Wiki online, [hier](../../pages/Simple%20Serial%20Interface.md)

NEU:

- Hoffentlich Benutzerfreundliche Schaltpläne (Pin-Belegungen am Interface und an der Betty)

- Volle LPCTool-Unterstüzung für RESET und EINT1

- Sicherheit zum Schutz von Schaltung und COM-Port

viel vergnügen!

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg485#msg485)

---

<a id="msg487"></a>

## 20. TonyMahony · 09. Nov 2007, 10:07

Schonmal vielen Dank für die V2 und die praktischen Dateien!

Das SSIV2 kann aber "nur" mit der Betty und ist für den Scart-Adapter nicht vorgesehen, korrekt?

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg487#msg487)

---

<a id="msg488"></a>

## 21. alterego · 09. Nov 2007, 17:36

vom konzept her sehe ich keinen grund warum es nicht mit dem scart-adapter oder dem modem/ip adapter gehen soll... weil rs232 habe sie alle, nur bzgl reset und eint ist es halt mit lpctool an die betty gebunden... vorerst.

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg488#msg488)

---

<a id="msg491"></a>

## 22. TonyMahony · 10. Nov 2007, 00:24

Colibri nutzt in seinem Kombiinterface ja zusätzlich PDA und PCL. Warum er das tut, bekomme ich schon noch raus...
Vollen Durchblick habe ich noch nicht, aber ich lasse mir ab und an von nem Radio- und Fernsehtechniker mit E-Technik-Studium ein Stück von der Schaltung erklären.
Was ich mir vorstelle ist ne eierlegende Wollmilchsau:
Ich hätte gerne ein Interface, mit dem ich RS232 mit allen vier Geräten machen und zusätzlich per Jumper (bzw. Schiebeschalter) auf die spezifischen Eigenarten der Geräte eingehen kann. Natürlich soll das nicht gleichzeitig stattfinden.
Dafür muss ich aber erstmal verstehen, warum in den beiden Interfaces was wie gelöst ist und was IP Adapter und Modem ggf. noch so brauchen.
Ich muss also vorerst ne Menge Datenblätter und Anleitungen lesen, einiges lernen und viel fragen.

Mir ist klar, dass ich mich wahrscheinlich besser aufs Wesentliche konzentrieren sollte, aber der Gedanke hat sich jetzt so festgesetzt und wird dann auch erstmal weiterverfolgt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg491#msg491)

---

<a id="msg494"></a>

## 23. alterego · 10. Nov 2007, 03:53

klingt für mich sehr überflüssig und absolut bloated. aber tu was du nicht lassen kannst

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg494#msg494)

---

<a id="msg497"></a>

## 24. Megabug · 10. Nov 2007, 16:13

Also für den IP Adapter muss nur eint statt auf GND, auf VCC gelegt werden. Hab da jetzt ein kabel dran mit 3 Tastern was dies tut.

Aber ist auch nicht so schlimm derzeit, da der IP Adapter ein eigenes Flashtool hat was diese Leitungen nicht nutzt. (AFAIK!)

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg497#msg497)

---

<a id="msg502"></a>

## 25. TonyMahony · 11. Nov 2007, 04:13

> **Zitat von: Megabug am 10. Nov 2007, 16:13**
>
> Also für den IP Adapter muss nur eint statt auf GND, auf VCC gelegt werden. Hab da jetzt ein kabel dran mit 3 Tastern was dies tut.

Beim Modem wäre das für den Reset ja das gleiche Verfahren, wenn ich das richtig verstanden habe.

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg502#msg502)

---

<a id="msg507"></a>

## 26. theborg · 11. Nov 2007, 12:02

hi zu edit 2 bei eagle auf invoke und dann aufs bauteiel klikken und schon haste die beiden extra pins.

zur anordnung der pins die ist meist so da es leichter zu verdraten ist im schaltplaneditor.

mfg tb

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg507#msg507)

---

<a id="msg510"></a>

## 27. TonyMahony · 12. Nov 2007, 13:18

Okay - dann baue ich also erstmal das SSI V2.
Kann man ja später noch erweitern, aber ich will endlich die Betty brutzeln...

Ich suche grad die Bauteile bei Reichelt raus und hätte da mal wieder ne Frage. 

In der Stückliste steht ein 680Ohm-Widerstand, auf dem Plan steht 3K3, also 3300 Ohm. Was ist da richtig?   
Ich vermute mal, dass die 680 richtig ist und die 3K3 sich über die 3V3 von der Diode eingeschlichen hat...

EDIT:

Wäre nett, wenn da mal jemand nen Blick drauf werfen könnte:

Anzahl - Artikelnummer - Beschreibung

1 - [H25SR050 - Streifenrasterplatine, Hartpapier, 50x100mm](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=C932;GROUPID=3373;ARTICLE=8275;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,47€
1 - [MAX 3232 CPE - RS232, DIL-16](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=A217;GROUPID=2914;ARTICLE=9398;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 4,5€
4 - [TANTAL 1,0/35 - Tantal-Kondensator, Rm 2,5, 1,0µF/35V](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=B312;GROUPID=3143;ARTICLE=15094;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,15€
1 - [TANTAL 0,1/35 - Tantal-Kondensator, Rm 2,5, 0,1µF/35V](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=B312;GROUPID=3143;ARTICLE=15085;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,11€
2 - [BC 547C - TRANSISTOR](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=A121;GROUPID=2881;ARTICLE=5007;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,031€
1 - [1N 4148 - DIODE](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=A411;GROUPID=2987;ARTICLE=1730;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,02€
1 - [ZF 3,3 - Z-DIODE 0,5W](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=A421;GROUPID=2993;ARTICLE=23126;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,031€
1 - [1W 680 - Kohleschichtwiderstand 1W, 5%, 680 Ohm](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=B1121;GROUPID=3070;ARTICLE=1839;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,15€
1 - [GS 16 - IC-Sockel, 16-polig, doppelter Federkontakt](https://web.archive.org/web/2012/http://www.reichelt.de/?;ACTION=3;LA=5;GROUP=C131;GROUPID=3215;ARTICLE=8208;START=0;SORT=order_col_artnr_besch;OFFSET=16) - 0,041€

Gesamtkosten: 5,984€

*Last Edit : 12. Nov 2007, 14:55 by TonyMahony*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg510#msg510)

---

<a id="msg512"></a>

## 28. alterego · 12. Nov 2007, 16:23

hiho.

die 3k3 sind der vorwiderstand für die z-diode, allerdings von ner ganz ganz frühen version der schaltung und recht üppig bemessen, 680Ohm is der widerstand den du nehmen möchtest. ich nutze immer keramik kondensatoren (ich hab ehrlich gesagt noch nie tantals verwendet) aber kannst ja mal testen, sollte aber davon abgesehen funktionierne (16v tantals reichen aber). Bei dem widerstand reichen 1/4 watt.

dann willst du das ding vllt an die rs232 buchse deines pcs anschliessen... vllt willst du ja noch eine buchse zum anschluss eines 1:1 rs232 kabels mitbestellen? vllt auch noch ein rs232 kabel?

dann willst du ja die betty noch anschliessen? vllt noch eine buchsenleiste um die auf den pinheader der betty zu stecken?

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg512#msg512)

---

<a id="msg513"></a>

## 29. TonyMahony · 12. Nov 2007, 16:34

> **Zitat von: alterego am 12. Nov 2007, 16:23**
>
> hiho.
>
> die 3k3 sind der vorwiderstand für die z-diode, allerdings von ner ganz ganz frühen version der schaltung und recht üppig bemessen, 680Ohm is der widerstand den du nehmen möchtest. ich nutze immer keramik kondensatoren (ich hab ehrlich gesagt noch nie tantals verwendet) aber kannst ja mal testen, sollte aber davon abgesehen funktionierne (16v tantals reichen aber). Bei dem widerstand reichen 1/4 watt.

Waren die kleinsten Tantals, die ich gefunden habe - 16V gibt es die 1,0er als SMD, aber das wäre mir dann doch ein wenig zu klein.
Der Radio- und Fernsehtechniker meines Vertrauens meinte, Tantals könnte ich nehmen - ich melde dann hier, ob es geklappt hat...

> **Zitat von: alterego am 12. Nov 2007, 16:23**
>
> dann willst du das ding vllt an die rs232 buchse deines pcs anschliessen... vllt willst du ja noch eine buchse zum anschluss eines 1:1 rs232 kabels mitbestellen? vllt auch noch ein rs232 kabel?
> dann willst du ja die betty noch anschliessen? vllt noch eine buchsenleiste um die auf den pinheader der betty zu stecken?

Ich denke mal, dass ich dafür genügend Elektroschrott zuhause rumfliegen habe, um da ne Verbindung hinzubekommen, aber danke für den Hinweis!

Der angepasste Widerstand findet sich im öffentlichen Warenkorb für das SSIV2 bei Reichelt wieder:
[https://secure.reichelt.de/?;ACTION=20;LA=5000;AWKID=35284;PROVID=2084](https://web.archive.org/web/2012/https://secure.reichelt.de/?;ACTION=20;LA=5000;AWKID=35284;PROVID=2084)

EDIT:
Das einzig blöde ist, dass man damit nicht an die 10€ Mindestbestellwert rankommt, aber irgendwas braucht man ja immer noch zusätzlich...

*Last Edit : 12. Nov 2007, 16:37 by TonyMahony*

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg513#msg513)

---

<a id="msg514"></a>

## 30. alterego · 12. Nov 2007, 17:07

wie du vllt auf dem lochraster-layout gesehen hast gehe ich von horizontalen streifen auf der platine aus ( also über die vollen 10cm) die in deinem warenkorb sieht mir vertikal aus (aber muss ja nicht stimmen, bilder und kataloge sind immer so ne sache)... das würde es dir auf jeden fall etwas schwerer machen da du das ganze dann etwas kompakter machen musst. (is aber keine aktion)

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg514#msg514)

---

<a id="msg516"></a>

## 31. TonyMahony · 12. Nov 2007, 19:09

> **Zitat von: alterego am 12. Nov 2007, 17:07**
>
> wie du vllt auf dem lochraster-layout gesehen hast gehe ich von horizontalen streifen auf der platine aus ( also über die vollen 10cm) die in deinem warenkorb sieht mir vertikal aus (aber muss ja nicht stimmen, bilder und kataloge sind immer so ne sache)... das würde es dir auf jeden fall etwas schwerer machen da du das ganze dann etwas kompakter machen musst. (is aber keine aktion)

Danke für den Hinweis - hab ich auch schon gesehen und kam mir komisch vor, aber wie heißt es so schön:
Es gibt keine Probleme, sondern nur Herausforderungen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg516#msg516)

---

<a id="msg517"></a>

## 32. Gentoo07 · 12. Nov 2007, 20:43

@alterego:

Moin, und danke für die Veröffentlichung der Schaltung!

Nimm es mir bitte nicht böse, aber ist die Z-Diode nicht überflüssig?

Die Basis-Emitterstrecke von Q2 begrenzt die Spannung parallel zu der z-diode auf 0,7V , daher tritt die Z-Spannung von 3,3V nicht auf (solange Q2 intakt ist).

Grüße aus Ostfriesland

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg517#msg517)

---

<a id="msg518"></a>

## 33. alterego · 12. Nov 2007, 23:31

warum sollte ich deswegen böse sein? für verbesserungen oder optimierungen bin ich immer offen.

grundsätzlich könnte man die z-diode + vorwiderstand auch weglassen (der transistor wird nur ehr kurz mit der spannung belastet), aber was wenn der transitor mal beschädigt wird, oder es bereits ist vor dem ersten einschalten? oder durchs löten? ich weiss nicht wie realistisch das is (und bin auch für optimalere lösungen offen) will aber  nicht die angeschlossenen schaltungen mit spannungen >5v aussetzen sollte das ding mal so verrecken, das ich nen schluss zwischen basis und collector habe.

[Permalink](http://bettyhacks.com/forum/index.php?topic=29.msg518#msg518)

---

## Verwandte Themen

- [NXP ISP (nachbau)](0013-nxp-isp-nachbau.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
