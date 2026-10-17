---
title: "BFS_LoadFile, Flash1"
topic_id: 231
board: "Software"
board_id: 6
posts: 4
first_post: "03. Feb 2010, 19:28"
last_post: "03. Feb 2010, 23:38"
authors: ["Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=231.0"
---

# BFS_LoadFile, Flash1

[← Software](../boards/06-software.md) · Thema 231 · 4 Beiträge · 03. Feb 2010, 19:28 – 03. Feb 2010, 23:38

Beteiligt: Telekatz, eme

---

<a id="msg1588"></a>

## 1. eme · 03. Feb 2010, 19:28

N'Abend. Ich habe settingsmenu um eine Kontrasteinstellung erweitert:
[http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware/boop/trunk/gui/settingsmenu.c?revision=28&view=markup#l_140](https://web.archive.org/web/2012/http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware/boop/trunk/gui/settingsmenu.c?revision=28&view=markup#l_140)

Es gibt jedoch einen unschönen Bug: Es wird nach dem Flashen ein falscher Wert geladen, deswegen ist nichts auf dem Display zu sehen.
Genau das sollte jedoch nach meinem Verständnis in Zeile 140 unterbunden werden:
`if(BFS_LoadFile(BFS_ID_settings, sizeof(struct settings_), (unsigned char*) &settings) != sizeof(struct settings_))`

Diese Bedingung sollte True ergeben, da struct settings_ ein Byte größer ist, als die alte Struktur im Flash. Sehe ich das richtig?

Workaround: per lpctool mit Option -E oder per TestStuff "Erase Flash1" die alten Settings löschen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=231.msg1588#msg1588)

---

<a id="msg1589"></a>

## 2. Telekatz · 03. Feb 2010, 21:14

> **Zitat**
>
> Diese Bedingung sollte True ergeben, da struct settings_ ein Byte größer ist, als die alte Struktur im Flash. Sehe ich das richtig?

Ja, so hab ich mir das damals gedacht. Würde auf einem 8Bit µC wohl auch funktionieren. Aber nicht unbedingt auf einem ARM.

Die struct settings_ war vorher 12 Byte groß und ist mit mit dem Kontrastwert immernoch 12 Byte groß. Liegt an der Speicherausrichtung. Eine ungepackte struct hat hier immer eine vielfache größe von 4 und ein int liegt auf einer Adresse die restlos durch 4 teilbar ist.

Ich werd das mal etwas umprogrammieren.

[Permalink](http://bettyhacks.com/forum/index.php?topic=231.msg1589#msg1589)

---

<a id="msg1590"></a>

## 3. eme · 03. Feb 2010, 22:53

Klingt kompliziert :-)
Unabhängig davon: die Kontrasteinstellung bringt nicht so wahnsinnig viel; bei meinen Bettys sind die Graustufen bei gleichen Parametern ziemlich verschieden.
Ich werde mal ein paar Originale auslesen, ich vermute, sie bekommen bei der Herstellung einen Kalibrierwert. Vielleicht gibt's vom Displayhersteller für jedes Display gleich die optimalen Parameter mit dazu?

[Permalink](http://bettyhacks.com/forum/index.php?topic=231.msg1590#msg1590)

---

<a id="msg1592"></a>

## 4. eme · 03. Feb 2010, 23:38

Fixed durch Versionierung: [http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware?view=rev&revision=31](https://web.archive.org/web/2012/http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware?view=rev&revision=31)

[Permalink](http://bettyhacks.com/forum/index.php?topic=231.msg1592#msg1592)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
