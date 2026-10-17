---
title: "soft-reset nach dem flashen mit lpctool"
topic_id: 189
board: "Software"
board_id: 6
posts: 5
first_post: "31. Jan 2009, 02:28"
last_post: "07. Okt 2010, 14:37"
authors: ["Ge0rG", "Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=189.0"
---

# soft-reset nach dem flashen mit lpctool

[← Software](../boards/06-software.md) · Thema 189 · 5 Beiträge · 31. Jan 2009, 02:28 – 07. Okt 2010, 14:37

Beteiligt: Ge0rG, Telekatz, eme

---

<a id="msg1277"></a>

## 1. Ge0rG · 31. Jan 2009, 02:28

Hi!

Nachdem ich vor kurzem über bettyhacks.com gestolpert bin und meine Betty wieder aus der Kramkiste geholt habe, wollte ich gleich eine Kleinigkeit beitragen.

Ich habe lediglich ein Handy-Kabel mit RX, TX und GND; Reset und EINT1 habe ich als Taster am Adapter. Daher geht das Resetten der Betty nicht automatisch mit dem lpctool, wenn der Flashvorgang beendet ist. Um das dennoch zu ermöglichen, habe ich lpctool und ramtool so gepatcht, dass ein neues Reset-Kommando ('*') gesendet wird, und das ramtool den Reset-Vektor im ROM anspringt.

Die Code-Änderungen sind überschauber, ein unified diff gegen lpctool svn-r11 findet sich hier:
[http://op-co.de/betty/lpctool_softreset.diff](https://web.archive.org/web/2012/http://op-co.de/betty/lpctool_softreset.diff) (GPLv3 und der Integration ins SVN stimme ich natürlich zu)

Wer nicht einen Taster sondern einen Jumper für EINT1 (Bootloader enable) verwendet, müsste diesen allerdings während des Flash-Vorganges abziehen, damit er nicht beim Reset wieder im Bootloader landet.

[Permalink](http://bettyhacks.com/forum/index.php?topic=189.msg1277#msg1277)

---

<a id="msg1284"></a>

## 2. Ge0rG · 06. Feb 2009, 01:33

Bei der Gelegenheit fiel mir auf: das Compiler-Flag für "Größe minimieren" -Os wird beim Linken und nicht beim Compilieren übergeben. Wenn man das repariert, hat es gravierende Folgen auf die Dateigröße:

ohne -Os:
`19284 2009-02-06 01:04 ramtool.bin
19284 2009-02-06 01:04 romtool.bin`

mit -Os in den CFLAGS:
`10796 2009-02-06 01:05 ramtool.bin
10796 2009-02-06 01:05 romtool.bin`

Damit ist dann auch noch ein Kilobytechen frei um einen schicken Fortschrittsbalken im LCD zu implementieren ;-)
[http://op-co.de/betty/lpctool_progress_lcd.diff](https://web.archive.org/web/2012/http://op-co.de/betty/lpctool_progress_lcd.diff)

[Permalink](http://bettyhacks.com/forum/index.php?topic=189.msg1284#msg1284)

---

<a id="msg1677"></a>

## 3. eme · 06. Okt 2010, 20:36

Die diffs sind verschoben worden nach [http://op-co.de/betty/attic/](https://web.archive.org/web/2012/http://op-co.de/betty/attic/) also

[http://op-co.de/betty/attic/lpctool_softreset.diff](https://web.archive.org/web/2012/http://op-co.de/betty/attic/lpctool_softreset.diff)
[http://op-co.de/betty/attic/lpctool_progress_lcd.diff](https://web.archive.org/web/2012/http://op-co.de/betty/attic/lpctool_progress_lcd.diff)

Wenn mir jemand sagt, wie das Makefile angepasst werden kann, um die Mathe-Routinen aus libgcc.a plattformübergreifend zu linken, gibt es Georgs Statusbalken bald im SVN..

[Permalink](http://bettyhacks.com/forum/index.php?topic=189.msg1677#msg1677)

---

<a id="msg1678"></a>

## 4. Telekatz · 07. Okt 2010, 09:03

Genauso wie bei Boop.

libpath im makefile.local definieren z.B.
`LIBPATH = $(ARMBASE)/lib/gcc/arm-elf/4.1.1/interwork`

LD den libpath mitteilen und mit "-lgcc" libgcc.a hinzufügen:
`$(LD) $(ROMLDFLAGS) -L$(LIBPATH) -o.... -lgcc`

[Permalink](http://bettyhacks.com/forum/index.php?topic=189.msg1678#msg1678)

---

<a id="msg1679"></a>

## 5. eme · 07. Okt 2010, 14:37

Danke.

[Permalink](http://bettyhacks.com/forum/index.php?topic=189.msg1679#msg1679)

---

## Verwandte Themen

- [lpctool, ubuntu linux, Reset/eINT1-Timingprobleme mit PL-2303](0228-lpctool-ubuntu-linux-reset-eint1-timingprobleme-mit-pl-2303.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
