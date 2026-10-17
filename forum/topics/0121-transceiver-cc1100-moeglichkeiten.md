---
title: "Transceiver CC1100 Möglichkeiten"
topic_id: 121
board: "Hardware"
board_id: 5
posts: 1
first_post: "26. Mär 2008, 17:06"
last_post: "26. Mär 2008, 17:06"
authors: ["eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=121.0"
---

# Transceiver CC1100 Möglichkeiten

[← Hardware](../boards/05-hardware.md) · Thema 121 · 1 Beiträge · 26. Mär 2008, 17:06 – 26. Mär 2008, 17:06

Beteiligt: eme

---

<a id="msg850"></a>

## 1. eme · 26. Mär 2008, 17:06

Ich habe mal die Threads zum Transceiver CC1100 ( [http://focus.ti.com/docs/prod/folders/print/cc1100.html](https://web.archive.org/web/2012/http://focus.ti.com/docs/prod/folders/print/cc1100.html) ) zusammengesammelt.
Allerdings kann ich vorerst nichts Wesentliches zum Thema beitragen, außer vielleicht etwas Übersicht für Interessierte zu schaffen.

Der IC ist relativ mächtig und kann eine Reihe von Modulationsarten:
2-FSK, GFSK, and MSK supported as well as OOK and flexible ASK shaping

Außerdem:
Flexible support for packet oriented systems: On-chip support for sync word detection, address check, flexible packet length, and automatic CRC handling

Es ist natürlich am Besten, zwischen zwei oder mehreren gleichen Transceivern zu funken. Klappt wohl auch schon:

Kommunikation Scartadapter
[http://bettyhacks.com/forum/index.php?topic=114.0](0114-kommunikation-scartadapter.md)

VT Datenstrom zur Datenübertragung
[http://bettyhacks.com/forum/index.php?topic=82.0](0082-vt-datenstrom-zur-datenuebertragung.md)

Wenn andere Module mit ins Spiel kommen, bedeutet das natürlich mehr Arbeit:

Kommunikation zur Betty mit RFM12?
[http://bettyhacks.com/forum/index.php?topic=93.0](0093-kommunikation-zur-betty-mit-rfm12.md)

Das RFM-12 kann meines Wissens nach FSK, daher könnte ein Zusammenspiel (auf niedrigster Ebene) möglich sein.
Viel zu diesem Modul findet sich in [http://www.mikrocontroller.net/topic/65984](https://web.archive.org/web/2012/http://www.mikrocontroller.net/topic/65984)
Es gibt dort auch andere ausgereifte Programme für AVR und RFM-12, unter anderem eine transparente RS232-Verbindung (Luftkabel) mit einem einfachen, wirkungsvollen Protokoll.

Ein Protokoll müsste dann wahrscheinlich auch in Software auf der Betty unterstützt werden.

S.N.A.P.-Protokoll für die Funkübertragung?
[http://bettyhacks.com/forum/index.php?topic=95.0](0095-s-n-a-p-protokoll-fuer-die-funkuebertragung.md)

Da auf der anderen Seite schon verschiedene Verfahren existieren, hat man die Qual der Wahl.

Billige digitale Sender / Empfänger arbeiten meist mit Amplitudenmodulation (AM).

Funksteckdosen
[http://bettyhacks.com/forum/index.php?topic=86.0](0086-funksteckdosen.md)

Dazu gehören auch noch Außenthermometer, Funk-Klingeln, ..

Auf Seite 36 des Datenblatts unter "16.3 Amplitude Modulation" steht, dass der IC zwei AM-Modulationsarten beherrscht.

On-Off Keying (OOK)
Amplitude Shift Keying (ASK)

Dazu [http://de.wikipedia.org/wiki/On-Off_Keying](https://web.archive.org/web/2012/http://de.wikipedia.org/wiki/On-Off_Keying)

Ich kenne mich leider nicht gut genug aus, aber vermute, dass doch eine Möglichkeit besteht, das mit dem CC1100 zu realisieren. Die Geräte verwenden oft die gleichen bzw. ähnliche Encoder. Habe was von Pulslängen von 400µs-1.2ms gelesen. Fertigen Code gibt es jedenfalls, auch für Systeme wie FS20, X10

[http://www.mikrocontroller.net/search?query=Funksteckdose](https://web.archive.org/web/2012/http://www.mikrocontroller.net/search?query=Funksteckdose)

Hier noch ein PDF zum Thema ISM-Band, Anwendungen, Modulation, Kodierung:

[http://digital.ni.com/worldwide/germany.nsf/87e62f4c89ea9df9862564250075e6e4/314564a9c53c31f6862572e5004dab62/](https://web.archive.org/web/2012/http://digital.ni.com/worldwide/germany.nsf/87e62f4c89ea9df9862564250075e6e4/314564a9c53c31f6862572e5004dab62/)$FILE/Nachrichtentechnik%20Seminar%20-%20Testen%20von%20ISM-Band%20Applikationen.pdf

*Last Edit : 26. Mär 2008, 22:25 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?PHPSESSID=439881574cc52b3c4b5bcc9acd1ba162&topic=121.msg850#msg850)

---

## Verwandte Themen

- [Kommunikation Scartadapter](0114-kommunikation-scartadapter.md)
- [VT Datenstrom zur Datenübertragung](0082-vt-datenstrom-zur-datenuebertragung.md)
- [Funksteckdosen](0086-funksteckdosen.md)
- [Kommunikation zur Betty mit RFM12?](0093-kommunikation-zur-betty-mit-rfm12.md)
- [S.N.A.P.-Protokoll für die Funkübertragung?](0095-s-n-a-p-protokoll-fuer-die-funkuebertragung.md)

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
