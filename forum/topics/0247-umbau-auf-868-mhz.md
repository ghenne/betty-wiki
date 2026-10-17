---
title: "Umbau auf 868 MHz"
topic_id: 247
board: "Hardware"
board_id: 5
posts: 5
first_post: "13. November 2010, 14:01"
last_post: "21. Februar 2012, 03:28"
authors: ["eme", "r00t"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=247.0"
---

# Umbau auf 868 MHz

[← Hardware](../boards/05-hardware.md) · Thema 247 · 5 Beiträge · 13. November 2010, 14:01 – 21. Februar 2012, 03:28

Beteiligt: eme, r00t

---

<a id="msg1717"></a>

## 1. eme · 13. November 2010, 14:01

Zur Ideensammlung, da mittlerweile viele Geräte auf 868 MHz ausgewichen sind (FS20, Funk-Wettersensoren, Heizungssteuerung.). Laut Telekatz lässt sich zwar auch mit der Beschaltung für 434 MHz etwas aus dem 868 Band Empfangen, aber es geht nur in unmittelbarer Umgebung  (5 m und Wand).

Alternativ zum Umbau könnte man auch ein zusätzliches Funkmodul an Betty/SCART/TAE anbringen.
Mir schwebt gerade vor, SCART oder TAE umzurüsten und mit der Betty zu verbinden.

Im Datenblatt des CC1100 Abschn. 7, "Application Circuit", sind Beispielbeschaltungen für 434 und 868 MHz.

Wie im Anhang zu erkennen, ist zumindest das Layout bei Betty, SCART und TAE fast identisch.

Die Schaltung für 868 MHz benötigt 6 Kondensatoren und 6 Induktivitäten (zwei Teile mehr, teils gleiche Werte), es lassen sich keine Komponenten wiederverwenden.

Dafür lassen sich aber einige Pads recyclen, Masseflächen sind ausreichend vorhanden.
Da Luftverdrahtung mit 0402 ziemlich fummelig ist, könnte man auch eine Leiterplatte huckepack auflöten, die an den CC1100, Masse, und die Antenne geht. Gerber-Daten (also das PCB Layout) sind im "CC1100EM 868 – 915 MHz Reference Design 2.0" enthalten und unter [http://www.ti.com/lit/zip/swrr038](https://web.archive.org/web/2012/http://www.ti.com/lit/zip/swrr038) zu bekommen.

Hier die benötigten Teile laut Datenblatt "Table 15: Bill Of Materials for the Application Circuit":

Murata GRM1555C series:
1x 1.0 pF ± 0.25 pF, 0402 NP0
2x 1.5 pF ± 0.25 pF, 0402 NP0
1x 3.3 pF ± 0.25 pF, 0402 NP0
2x 100 pF ± 5%, 0402 NP0

Murata LQG15HS series:
4x 12 nH ± 5%, 0402 monolithic
2x 18 nH ± 5%, 0402 monolithic

NPO = non-polarized (laut "What is "NPO" in Capacitor Spec?", [http://www.diystompboxes.com/smfforum/index.php?topic=30558.0](https://web.archive.org/web/2012/http://www.diystompboxes.com/smfforum/index.php?topic=30558.0))

Die Werte in 0402 gibt es bei RS-Components, wenn auch nicht alle entsprechend der vorgeschlagenen Produktserie:

20 x 701-6910
10 x 701-6926
50 x 624-2777
50 x 624-2193
50 x 624-2929
50 x 456-8588

16,25 + MwSt. für 5 + Umbauten

Spätestens durch diesen Umbau erlischt die Zulassung, und man funkt evtl. wild und gesetzesbrechend in der Gegend herum.

[Permalink](http://bettyhacks.com/forum/index.php?topic=247.msg1717#msg1717)

---

<a id="msg1725"></a>

## 2. eme · 17. November 2010, 14:31

> **Zitat von: eme am 13. November 2010, 14:01**
>
> NPO = non-polarized (laut "What is "NPO" in Capacitor Spec?", [http://www.diystompboxes.com/smfforum/index.php?topic=30558.0](https://web.archive.org/web/2012/http://www.diystompboxes.com/smfforum/index.php?topic=30558.0))

Eher NP0 (N P Null) als Kürzel für für Material bzw. Temperaturkoeffizient:
[http://de.wikipedia.org/wiki/Keramikkondensator#Klasse-1-Keramikkondensatoren](https://web.archive.org/web/2012/http://de.wikipedia.org/wiki/Keramikkondensator#Klasse-1-Keramikkondensatoren)

[Permalink](http://bettyhacks.com/forum/index.php?topic=247.msg1725#msg1725)

---

<a id="msg2000"></a>

## 3. r00t · 04. Januar 2012, 07:20

> **Zitat von: eme am 13. November 2010, 14:01**
>
> Alternativ zum Umbau könnte man auch ein zusätzliches Funkmodul an Betty/SCART/TAE anbringen.

> **Zitat von: eme am 13. November 2010, 14:01**
>
> Dafür lassen sich aber einige Pads recyclen, Masseflächen sind ausreichend vorhanden.
> Da Luftverdrahtung mit 0402 ziemlich fummelig ist, könnte man auch eine Leiterplatte huckepack auflöten, die an den CC1100, Masse, und die Antenne geht. Gerber-Daten (also das PCB Layout) sind im "CC1100EM 868 – 915 MHz Reference Design 2.0" enthalten und unter [http://www.ti.com/lit/zip/swrr038](https://web.archive.org/web/2012/http://www.ti.com/lit/zip/swrr038) zu bekommen.

ist der aufwand den vorhanden chip mit dem ganzen smd-huehnerfutter umzuruesten nicht arg hoch?
und ausserdem verliert man die moeglichkeit mit scart/tae/anderen bettys zu kommunizieren.

es erscheint interessanter, ein zweites funkmodul (zB RFM12) einzubauen.
der CC1100 ist per SPI angebunden, man koennte an den gleichen bus relativ einfach noch ein zusatzliches  anderes funkmodul mit spi anschliessen (zB das RFM12).

[Permalink](http://bettyhacks.com/forum/index.php?topic=247.msg2000#msg2000)

---

<a id="msg2005"></a>

## 4. eme · 20. Februar 2012, 22:32

Hallo,

ein weiteres Funkmodul zu nutzen ist natürlich eine Überlegung wert. Ich bin etwas aus dem Thema raus; gibt es denn noch freie Leitungen für den chip select?

PS: die Idee hatte ich ja auch schonmal: [http://bettyhacks.com/forum/index.php?topic=246.msg1716#msg1716](0246-freie-pins-spi-sd-mmc.md#msg1716) :-)

*« Letzte Änderung: 20. Februar 2012, 22:35 von eme »*

[Permalink](http://bettyhacks.com/forum/index.php?topic=247.msg2005#msg2005)

---

<a id="msg2007"></a>

## 5. r00t · 21. Februar 2012, 03:28

> **Zitat von: eme am 20. Februar 2012, 22:32**
>
> gibt es denn noch freie Leitungen für den chip select?

ich kenne mich da leider auch (noch) nicht genug aus,
daher hatte ich dazu einen extra thread angefangen:
[http://bettyhacks.com/forum/?topic=278.0](0278-erweiterung-der-betty-hardware-freie-gpios.md)
(auch da gab es vorher schon andere...)

[Permalink](http://bettyhacks.com/forum/index.php?topic=247.msg2007#msg2007)

---

## Verwandte Themen

- [Freie Pins, SPI, SD / MMC](0246-freie-pins-spi-sd-mmc.md)
- [erweiterung der betty hardware / freie GPIOs](0278-erweiterung-der-betty-hardware-freie-gpios.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
