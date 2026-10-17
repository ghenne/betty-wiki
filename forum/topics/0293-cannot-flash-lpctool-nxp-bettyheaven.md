---
title: "Cannot flash - lpctool / nxp / BettyHeaven"
topic_id: 293
board: "Hardware"
board_id: 5
posts: 3
first_post: "19. Feb 2013, 11:20"
last_post: "20. Feb 2013, 10:27"
authors: ["brainwash"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=293.0"
---

# Cannot flash - lpctool / nxp / BettyHeaven

[← Hardware](../boards/05-hardware.md) · Thema 293 · 3 Beiträge · 19. Feb 2013, 11:20 – 20. Feb 2013, 10:27

Beteiligt: brainwash

---

<a id="msg2109"></a>

## 1. brainwash · 19. Feb 2013, 11:20

I took apart a USB-Serial cable based on Prolific PL2303HX and manually soldered the RX, TX, RTS, DTR signals to the chipset.
In RealTerm I can trigger the RTS and DTR pins to bring the device into bootloader mode, if I press "?" I get back "Synchronized". However, lpctool gets stuck at "awaiting autobaud response", NXP tool cannot open the port, BettyHeaven does not list the serial port at all. Under a WinXP Virtual Machine lpctool behaves the same, NXP times out, BettyHeaven again does not list the port, RealTerm works.

I can see that lpctool pulls the DTR line low, so reset works. I manually bridge the BL pin to ground before running the tool. I tried both the normal version of lpctool and the one limited to 38400 baud.

Is there any other way to flash the chip? I will download a Linux VM and try with that but I assume the Prolific chip is not properly supported by any of these tools.

Maybe I have a different bootloader?

`BettyHHUbootloader 00006420 00B770ED 1MByte
                                   
BIOS 00006420 000179B4 617EE0AD
                                               
no new BIOS
                                                                   
BIOS 000179B4 617EE0AD
                                                       
starting BIOS...

                                                           
                                                                               
Betty HHU BIOS 00B770ED 1MB
                                                   
Current build 25632, last build 25632
                                         
*** FONT 25632 F
                                                             
*** WAVE 12900
                                                               
*** HW V2
                                                                     
This is the final firmware for Betty. There will be no further updates.
       
*** FLASH 1C5B
                                                               
*** System up and running`

[Permalink](http://bettyhacks.com/forum/index.php?topic=293.msg2109#msg2109)

---

<a id="msg2110"></a>

## 2. brainwash · 19. Feb 2013, 11:46

I think I've traced at least one problem to the chipset & software combination.

   printInfoS(2,"initiating auto-baud",0);
   sendBuf(sprintf(buf, "?\r\n"), buf);

   printInfoS(2,"awaiting autobaud response",0);

On my scope I can see that braking the program with Ctrl+C during this waiting loop the characters get transmitted, but not before. This means that the PL 2303 [fake?] chipset buffers the TX characters and does not flush them.

[Permalink](http://bettyhacks.com/forum/index.php?topic=293.msg2110#msg2110)

---

<a id="msg2111"></a>

## 3. brainwash · 20. Feb 2013, 10:27

I'm sorry to be answering to my own messages (in English nonetheless) but this is a problem that's very common and not properly described anywhere on the Internet.

During 2007-2010 a lot of USB-RS232 cables based on a FAKE Prolific PL2303HX chip circulated around. It seems that I am also the unhappy owner of one.
The syndrome is that you cannot get it to work in Windows 7/8 with the official drivers, it just shows an Error 10 in the device manager and something with 'insufficient virtual memory'. The solution for this is to search for something like Prolific AllInOne GPS driver from 2008.

Under normal operation everything works fine but in some cases (like lpctool) software compiled with cygwin libraries and not the .NET ones from Microsoft exhibit a flushing problem. This manifests itself as the application missing the last one or sixteen characters on RX or not transmitting the last ones on TX. There is a discussion thread somewhere with Prolific acknowledging the problem and fixing it in later driver revisions. The serial libraries from .NET have also been updated (as far as I know) to flush earlier or after a time-out. Don't quote me on that.

However, the fake chips cannot be updated to any driver after 2008 because it causes the error 10 "device cannot start" in Device Manager. So you are pretty much stuck and having to buy another cable if you depend on this flushing functionality.

Again, under normal use - serial println debugging, flashing firmwares for routers and oscilloscopes, null-modem - you shouldn't see this problem. I have been using the cable for the past 5 years and haven't noticed any problems until now.

[Permalink](http://bettyhacks.com/forum/index.php?topic=293.msg2111#msg2111)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
