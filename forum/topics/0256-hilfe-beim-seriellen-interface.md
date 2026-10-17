---
title: "Hilfe beim seriellen Interface"
topic_id: 256
board: "Hardware"
board_id: 5
posts: 8
first_post: "25. März 2011, 10:18"
last_post: "29. März 2011, 07:58"
authors: ["Megabug", "Patrick", "RandD", "martin99"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=256.0"
---

# Hilfe beim seriellen Interface

[← Hardware](../boards/05-hardware.md) · Thema 256 · 8 Beiträge · 25. März 2011, 10:18 – 29. März 2011, 07:58

Beteiligt: Megabug, Patrick, RandD, martin99

---

<a id="msg1907"></a>

## 1. Megabug · 25. März 2011, 10:18

Moment, wenns ein serielles Kabel ist, dann braucht es noch VON der Betty eine Spannungsversorgung! (Für die Pegelwandler da drin)

Wenns ein USB Kabel ist, dürfen die 5V VOM Kabel nicht an die Betty angeschlossen werden!

Gruß
Megabug

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1907#msg1907)

---

<a id="msg1908"></a>

## 2. RandD · 25. März 2011, 10:49

Jap, VON der Betty 3,3V!!!

Der Pegelwandler des Siemenskabels braucht die Spannung damit er tut.

Bei USB Kabeln wird normalerweise die 5V der USB-Buchse für den Pegelwandler verwendet.

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1908#msg1908)

---

<a id="msg1909"></a>

## 3. Patrick · 25. März 2011, 11:04

Ah, ok, prima-Danke...

Wo die 3,3V auf der Betty liegen, weiß ich, aber wohin müssen die beim Kabel ([http://www.nobbi.com/steck_s25.html)?](https://web.archive.org/web/2012/http://www.nobbi.com/steck_s25.html)?)
Vermutlich an
4   BATT   Spannungsversorgung für Zubehör   U = 3,0V - 3,9V Umin = 2,6V Imax = 100mA   out
oder?

Danke!

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1909#msg1909)

---

<a id="msg1910"></a>

## 4. RandD · 25. März 2011, 12:03

Ja genau an 4 BATT...

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1910#msg1910)

---

<a id="msg1911"></a>

## 5. martin99 · 27. März 2011, 15:27

Hallo,
ich habe Problem meine Betty mit der seriellen Schnittstelle zu programmieren. Ich habe die Schaltungen von Colibri (Scart-Betty-Kombiinterface) und von K.Jacobs (simple Seriell Interface) aufgebaut und versucht mit Betty Heaven das Flash auszulesen. Es kommt immer die Fehlermeldung RX-Timeout.
Ich benutze eine normale RS232 Schnittstelle und kein USB Wandler. Wenn ich mit Putty RX und TX brücke sehe ich das der MAX 3232 arbeitet. Auch die Bootmeldungen der Betty bekomme ich angezeigt. Nur Betty-Heaven will nicht!
Was mich noch wundert, die Schaltung von Colibri benutzt zur Steuerung CTS (nur für Scart) und RTS und die Schaltung von K. Jakobs DTR und RTS. Wie soll Betty Heaven das denn unterscheiden?
Habt Ihr für mich einen Tip für das weitere Vorgehen? Auch finde ich nirgends das Programm LPCTool. Wo liegt denn das?

VG
Martin

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1911#msg1911)

---

<a id="msg1913"></a>

## 6. Megabug · 27. März 2011, 21:23

Versuch mal die Betty manuell im bootloader zu bringen und dann zu flashen.

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1913#msg1913)

---

<a id="msg1914"></a>

## 7. martin99 · 29. März 2011, 06:53

Hallo Megabug,
vielen Dank für den Tip! Mit der manuellen Steuerung hat es geklappt. Muss nur mal suchen warum das mit den Transistoren nicht klappt.

Aber wo finde ich das Programm LPCTool?

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1914#msg1914)

---

<a id="msg1915"></a>

## 8. RandD · 29. März 2011, 07:58

Hallo,

das  LPCTool findest du im SVN:  [http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware/lpctool/](https://web.archive.org/web/2012/http://boopfirmware.svn.sourceforge.net/viewvc/boopfirmware/lpctool/)

greetz

[Permalink](http://bettyhacks.com/forum/index.php?topic=256.msg1915#msg1915)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
