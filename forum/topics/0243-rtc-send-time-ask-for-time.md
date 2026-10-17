---
title: "rtc send_time / ask_for_time?"
topic_id: 243
board: "Software"
board_id: 6
posts: 5
first_post: "07. Okt 2010, 17:42"
last_post: "08. Okt 2010, 10:07"
authors: ["Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=243.0"
---

# rtc send_time / ask_for_time?

[← Software](../boards/06-software.md) · Thema 243 · 5 Beiträge · 07. Okt 2010, 17:42 – 08. Okt 2010, 10:07

Beteiligt: Telekatz, eme

---

<a id="msg1680"></a>

## 1. eme · 07. Okt 2010, 17:42

Hallo Telekatz,

was machen diese Funktionen?

Evtl. könntest Du kurz den Ablauf einer RF Verbingung erklären?

Danke.

[Permalink](http://bettyhacks.com/forum/index.php?topic=243.msg1680#msg1680)

---

<a id="msg1681"></a>

## 2. Telekatz · 07. Okt 2010, 19:35

Die machen das, nach dem die auch benannt sind.

"ask_for_time" veranlasst alle Bettys, die diese Nachricht empfangen und eine aktuelle Zeit haben, diese der anfragenden Betty mittels "send_time" zu übermitteln.

Die Beantwortung von "ask_for_time" und die Üernahme der empfangenen Zeit von "send_time" erfolgt im cc1100IRQ.

"send_time" wird auch nach dem Einstellen des Datums/Uhrzeit im Settingsmenue aufgerufen und übermittelt die Zeit an alle in Reichweite befindlichen Bettys.

[Permalink](http://bettyhacks.com/forum/index.php?topic=243.msg1681#msg1681)

---

<a id="msg1682"></a>

## 3. eme · 07. Okt 2010, 20:17

Das hatte ich vermutet, aber es funktioniert bei mir nicht. Ich sehe zwar mit dem RSSI Monitor etwa -30dBm aber eine Verbindung bekommen sie nicht hin (weder mit RF Test noch die Synchronisation der Uhren).
Channel 1 und IDs 0/1

[Permalink](http://bettyhacks.com/forum/index.php?topic=243.msg1682#msg1682)

---

<a id="msg1683"></a>

## 4. Telekatz · 07. Okt 2010, 20:57

Has du einen Reset gemacht, nachdem du Channel und Device Address an der Betty eingestellt hast. Hab gerade gemerkt, das da irgendwo ein Bug sein muss. Nach dem Einstellen ist  der Empfang deaktiviert.

> **Zitat**
>
> Channel 1 und IDs 0/1

Sicher, dass du Device Address und Channel nicht vertauscht hast? Device Address lässt sich nicht auf 0 einstellen, das ist die Broadcast address.
Channel muss auf beiden Bettys gleich sein.

[Permalink](http://bettyhacks.com/forum/index.php?topic=243.msg1683#msg1683)

---

<a id="msg1684"></a>

## 5. eme · 08. Okt 2010, 10:07

Ich hatte wohl noch alte Settings im Flash und nur eine von den Bettys nach den RF-Einstellungen neu gestartet. RF-Test klappt jetzt mit ID 1,2 und Channel 1.
Danke für die Unterstützung!

PS: Cool, die Zeit-Synchronisation :-)

[Permalink](http://bettyhacks.com/forum/index.php?topic=243.msg1684#msg1684)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
