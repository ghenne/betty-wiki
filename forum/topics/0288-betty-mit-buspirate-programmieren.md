---
title: "Betty mit BusPirate programmieren"
topic_id: 288
board: "Software"
board_id: 6
posts: 5
first_post: "09. Dez 2012, 15:56"
last_post: "21. Feb 2013, 12:21"
authors: ["OCMoe", "brainwash", "koppi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=288.0"
---

# Betty mit BusPirate programmieren

[← Software](../boards/06-software.md) · Thema 288 · 5 Beiträge · 09. Dez 2012, 15:56 – 21. Feb 2013, 12:21

Beteiligt: OCMoe, brainwash, koppi

---

<a id="msg2092"></a>

## 1. OCMoe · 09. Dez 2012, 15:56

Aloha!

Da ich einen BusPirate meine Eigen nenne, dachte ich mir ich nutz dessen UART-Modus zum Programmieren. Da das aber mit den wechselnden Baudraten usw. über den Umweg nicht ganz einfach ist, habe ich das lpctool etwas modifiziert, so dass es (bei korrekter Verkabelung) die Initialisierung des BusPirate erledigt und auch Reset/Bootloader über die BP-Befehle ausführt. Derzeit beschränke ich mich dabei auf 19200 bps, weil das erstmal einfacher war. Dafür klappt aber alles vollautomatisch, dauert halt nur 30sec. länger.

Wenn's wen interessiert, sagt bescheid, dann bring ich den Code in eine veröffentlichbare Form

[Permalink](http://bettyhacks.com/forum/index.php?topic=288.msg2092#msg2092)

---

<a id="msg2101"></a>

## 2. koppi · 28. Dez 2012, 23:00

>Wenn's wen interessiert, sagt bescheid, dann bring ich den Code in eine veröffentlichbare Form

Ja, schieb' mal rüber. Danke!

Ich habe es auch mit dem BP versucht, bisher erfolglos. UART Bridge Mode mit
allen möglichen Baudraten (BP-Kommando: m 3 7 1 1 1 2 (1) y).

Bei 38400:
Wenn ich "?\r\n" schicke antwortet die Betty mit "Synchronized\r\n", auf ein "Synchronized\r\n" vom
Host nur mit einem "Synchron" (Rest fehlt).

Irgendeine Idee? Habe auch, wie hier in irgendeinem Beitrag vorgeschlagen, einen Pull-Up zwischen
3.3V und TX geklemmt - keine Verbesserung.

Dagegen hat es mit dem UART IF des Raspberry mit 38400 geklappt.

[Permalink](http://bettyhacks.com/forum/index.php?topic=288.msg2101#msg2101)

---

<a id="msg2104"></a>

## 3. OCMoe · 14. Jan 2013, 19:58

Hier sind meine Änderungen am lpctool als diff. Ich hoffe die Standard-Tools diff und patch sind soweit bekannt

lpctool wechselt zweimal die Bitrate (19200->38400->115200). Da der BusPirate das im Bridge-Modus nicht kann, wird mit diesem Patch alles bei 19200 bit/s gemacht, was dann halt ein paar Sekunden länger dauert.

MOSI/MISO sind RX/TX bei der Betty. CLK ist /RESET. CS ist eint. Aber ich glaube das lief noch nicht ganz sauber, zur Not musst du per Hand resetten. Ich hab damit vier Bettys programmiert bekommen, musste es aber für eine Weile weglegen. Ab März kümmer ich mich wieder drum.

Da man den Bridge-Modus nicht verlassen kann, muss man den BusPirate allerdings nach jedem Programmieren herausziehen und wieder einstecken. Eine bessere Lösung wäre ein spezielles Bridge-Skript für den BusPirate, aber damit hab ich mich noch nicht befasst.

[Permalink](http://bettyhacks.com/forum/index.php?topic=288.msg2104#msg2104)

---

<a id="msg2108"></a>

## 4. brainwash · 16. Feb 2013, 14:28

Sorry for hijacking this thread in English, please feel free to respond in German, I will try to understand.

I'm trying to program the remote using the Bus Pirate and cannot get anywhere. What I've tried so far:
- UART bridge in 38400 baud using the recompiled lpctool. It gets stuck at "awaiting autobaud response"
- avrdude with "buspirate" device configuration and ATTiny13 (as shown in wiki). It receives a 0x000000 chip signature
- avrdude with STK500 clone firmware on the bus pirate (communication error)
- a standard USB-UART cable I had lying around (I think it requires a level inverter)

I'm putting the remote in BL mode as described in the Wiki: put batteries into remote, it boots into normal mode, connect BL to GND, connect RST to GND, wait two seconds, disconnect RST, disconnect BL. The remote is showing a blank screen and in the UART terminal (38400 baud) I see that upon pressing the enter key I get some kind of echo (but it does not look like \r\n) and another character like "Ü".

For the avrdude I connected CS to RST and CLK to BL, everything else normal. The RX and TX are not reversed because I see the boot traces.

Can someone advise me how to proceed with this? I have ordered a USB-TTL transceiver but it will take a while until I receive it.

[Permalink](http://bettyhacks.com/forum/index.php?topic=288.msg2108#msg2108)

---

<a id="msg2112"></a>

## 5. brainwash · 21. Feb 2013, 12:21

Ok, maybe someone can edit the wiki and add the entries (I don't have the rights) to add BusPirate to supported hardware. The only thing that needed change was the base communication baudrate from the default 115200.

Cookbook:
- connections: GND to GND, Betty TX to MISO, Betty RX to MOSI. I also connected the 3.3V lines together, but it might not be needed
- open the terminal to BusPirate, press 'b' (baudrate), '7' (38400), close the terminal
- open a new terminal but with the baudrate set to 38400, press space
- to enter the UART transparent bridge macro type: 'm' '3' '7' '1' '1' '1' '2' '(1)' 'y' (everything should be default except last item which is 2)
- download the lpctool version with the fixed 38400 baud rate ( [http://bettyhacks.com/forum/index.php?topic=241.msg1667#msg1667](0241-geloest-lpctool-mit-cygwin-unter-windows-7-bauen.md#msg1667) )
- flash as usual: lpctool -d /dev/com4 -e -i -a boop_rom.bin

[Permalink](http://bettyhacks.com/forum/index.php?topic=288.msg2112#msg2112)

---

## Verwandte Themen

- [[gelöst] lpctool mit Cygwin unter Windows 7 bauen?](0241-geloest-lpctool-mit-cygwin-unter-windows-7-bauen.md)
- [Wer kann meine Betty (03.09. gekauft) auf 'nur Fernbedienung' programmieren?](0195-wer-kann-meine-betty-03-09-gekauft-auf-nur-fernbedienung-pro.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
