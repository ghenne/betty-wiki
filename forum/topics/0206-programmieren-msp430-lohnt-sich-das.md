---
title: "Programmieren MSP430 lohnt sich das?"
topic_id: 206
board: "Hardware"
board_id: 5
posts: 5
first_post: "05. Mai 2009, 17:36"
last_post: "15. Nov 2009, 14:04"
authors: ["D.Poics", "El_Barto", "Gonzo", "gerdi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=206.0"
---

# Programmieren MSP430 lohnt sich das?

[← Hardware](../boards/05-hardware.md) · Thema 206 · 5 Beiträge · 05. Mai 2009, 17:36 – 15. Nov 2009, 14:04

Beteiligt: D.Poics, El_Barto, Gonzo, gerdi

---

<a id="msg1403"></a>

## 1. gerdi · 05. Mai 2009, 17:36

Ich sehe gerade, dass das Rom der MSP430 sehr klein ist.
Da kann es doch nicht so viel zu programmieren geben.

Die Anbieter werben mit einer seriellen Programmierumgebung. Kann ich da meine bisherigen Kabel verwenden?

Kennt sich jemand aus, der mich unterstützen könnte?

Ist die MSP430 das einzige, was man programmieren muss im TAE?

Kriegt man das hin? Lohnt sich das?

Ist das in der Boopsy (so nenne ich die Betty Swisscom mit Boop) das selbe?

Ich möchte nur Daten von der Boopsy über einen Voip-Adapter an einen IP-Port senden.

[Permalink](http://bettyhacks.com/forum/index.php?topic=206.msg1403#msg1403)

---

<a id="msg1404"></a>

## 2. El_Barto · 05. Mai 2009, 17:57

Der MSP ist auf dem TAE-Adapter für die Verbindung des CC1100 mit dem ARM gedacht. Er steuert wohl die gesamte Funkanbindung und schaltet bei Bedarf den ARM ein. Der ARM fungiert als Softmodem und stellt dann eine Verbindung mit dem Provider her.

Auch wenn der MSP klein ist - die Implementierung des Funkmoduls (samt den "höheren" Layern) der Betty sollte sich auch für den MSP verwenden lassen. Dank Telekatz (ProgInterface für MSP) habe ich dafür nun etwas Motivation dafür gefunden. Eine AppNote von TI mit funktionierendem Code für einen MSP430 mit CC110x-Modul gibt es auch schon (TI: slaa325.zip).

Sobald mein Prüfungsstress rum ist setzte ich mich da mal dran. Bisher bin ich mit meinem JTAG an der Hardware-Hürde gescheitert, da OpenOCD leider keine MSP430 unterstützt.

Mich würde allerdings interessieren wie du dir das mit dem TAE vorstellst. Weil die Verbindung Betty-TAE-???VoIP???-???IP??? finde ich doch sehr seltsam. Da wirst du einige Protokolle zu implementieren haben.
Mein Vorschlag für dich: besorg dir irgendeine WebServer-Implementierung (z.B. Pollin uC-Webserver) und schicke deine Events seriell (ja, das wurde für den Scart-Adapter schon durch die Weisen des Forums programmiert) an den Webserver. Oder bastel dir ein PHY-Interface an den MSP, dann wirds aber aufwändiger.

*Last Edit : 05. Mai 2009, 18:04 by El_Barto*

[Permalink](http://bettyhacks.com/forum/index.php?topic=206.msg1404#msg1404)

---

<a id="msg1405"></a>

## 3. gerdi · 05. Mai 2009, 19:32

> **Zitat**
>
> und schicke deine Events seriell (ja, das wurde für den Scart-Adapter schon durch die Weisen des Forums programmiert) an den Webserver.

WOW!
Das wurde schon programmiert!!!!
Wusste ich nicht.
Ich glaube mein Asus Wl-500gp hat intern einen TTL-Low-Voltage-Anschluss!
Könnte ich da den Scart-Adapter direkt verbinden?

> **Zitat**
>
> Weil die Verbindung Betty-TAE-???VoIP???-???IP??? finde ich doch sehr seltsam. Da wirst du einige Protokolle zu implementieren haben.

Das sehe ich anders.
An den Voip-Adapter kann ich jedes billige Telefon anschliessen und das hat keine aufwändigen Protokolle.
Alle Voip- und IP-Protokolle werden vom Adapter geschachtelt. Die sind für das Telefon transparent.
Damit hat das Telefon NICHTS zu schaffen.

Da implementieren wir ein Nullmodem, mehr nicht!!!

Höchstens auf der Seite des Servers müsste ich Protokolle implementieren. Dafür ist der aber gerüstet. Sogar ein vollständiger Asterisk-Server steht als Optware in Mini-Packages zur Verfügung.

*Last Edit : 05. Mai 2009, 19:35 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=206.msg1405#msg1405)

---

<a id="msg1510"></a>

## 4. D.Poics · 14. Nov 2009, 09:18

Mal so ne frage meint ihr das sich der umbau heutzutage noch lohn vom aufwandt und preis fьr das alles? weil ich wьrde mich fьr sowas interessieren

[Permalink](http://bettyhacks.com/forum/index.php?topic=206.msg1510#msg1510)

---

<a id="msg1511"></a>

## 5. Gonzo · 15. Nov 2009, 14:04

Spamt wohl immer noch rum...

[Permalink](http://bettyhacks.com/forum/index.php?topic=206.msg1511#msg1511)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
