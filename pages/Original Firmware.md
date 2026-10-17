# Original Firmware

Die ursprüngliche Firmware von Betty und SCART-Adapter findet sich [hier](http://free.pages.at/colibri_dvb/Betty-Dumps.zip).

Informationen zur ursprünglichen Firmware gibt es hier:

- [Betty_init](Betty%20init.md "Betty init") - [<img src="../images/b/bf/Wichtig.16px.png" width="16" height="13" alt="Wichtig.16px" />](Datei_Wichtig.16px.png.md) **veraltet**
- [Flash_access](Flash%20access.md "Flash access") - [<img src="../images/b/bf/Wichtig.16px.png" width="16" height="13" alt="Wichtig.16px" />](Datei_Wichtig.16px.png.md) **veraltet**
- [Testmode](Testmode.md "Testmode") - Debugausgaben und Befehle über die serielle Schnittstelle
- [Speicheraufteilung](Speicheraufteilung.md "Speicheraufteilung") - Bereiche der Flash-Speicher
- [CRC-Check](CRC-Check.md "CRC-Check") - Prüfsumme für den Speicherinhalt / die Firmware
- [Baudraten](Baudraten.md "Baudraten")

# Debugausgaben

Siehe [Testmode](Testmode.md "Testmode").

# Update über Telefon

Betty \<\> Funk \<\> [SCART Adapter](SCART%20Adapter.md "SCART Adapter") \<\> Telefon \<\> Betty-Zentrale

- Log eines Updates: <http://www.grautier.com/grautier/uploads/Elektronik/Betty/bettyneu.txt>

# Universalfernbedienung

Nach Einstellen der Geschäftstätigkeit von betty-tv konnte man Betty über ein telefonisches Firmwareupdate zu einer einfachen Universalfernbedienung machen. Diese Firmware gibt es [hier](../forum/topics/0089-neue-software-von-betty-tv.md#msg807).

## Features

- Infrarotfernbedienung für vier Geräte (zugeordnet zu den Tasten A,B,C,D)
  - Tasten anlernbar
  - Gerätenamen einstellbar
  - Lautstärke einstellbar (CradleBeep, ..?)

## Default

- A: TV (RC5, Ziffern funktionieren nicht?)
- B: LinVDR
- C: AC3
- D: Video

## Debugausgaben

Ausgabe über die serielle Schnittstelle (115200 baud, 8N1) nach Reset:

    BettyHHUbootloader 00003264 00B770ED 1MByte
    BIOS 00006420 000179B4 617EE0AD
    no new BIOS
    BIOS 000179B4 617EE0AD
    starting BIOS...<25>
    <\0>
    Betty HHU BIOS 00B770ED 1MB
    Current build 25632, last build 25632
    *** FONT 25632 F
    *** WAVE 12900
    *** HW V3
    This is the final firmware for Betty. There will be no further updates.
    *** FLASH 1C5B
    *** System up and running

- In die Ladeschale einsetzen: tüt,tüt:

<!-- -->

    Charge: CradleBeep

## Firmware aufspielen

Wie kommt diese Firmware in die Betty? Siehe [Firmware_flashen](Firmware%20flashen.md "Firmware flashen").

Mit einem zweckentfremdeten [Handy-Datenkabel](Interfaces%20PC%20zu%20Betty.md "Interfaces PC zu Betty") und dem Programm [LPCTool](LPCTool.md "LPCTool") unter Linux z.B. so:

    ./lpctool -d /dev/ttyUSB0 -i -v -e -a Flash1_UniFB.bin -E -b Flash2_UniFB.bin

<!-- forum-links:start -->
## Forumsdiskussionen: Universalfernbedienung

Original-Firmware und Universalfernbedienung: Aufspielen, Software-Reset und das Vergessen von Programmierungen.

### Universalfernbedienung / Original-Firmware

- [Betty zur Universalfernbedienung umprogrammieren](../forum/topics/0300-betty-zur-universalfernbedienung-umprogrammieren.md) — Betty wieder zur Universalfernbedienung umprogrammieren.
- [Aufspielen der neuen Software](../forum/topics/0154-aufspielen-der-neuen-software.md) — Neue Software auf eine Betty aufspielen.
- [Neue Software von Betty-tv](../forum/topics/0089-neue-software-von-betty-tv.md) — Neue Software von Betty-TV und Update über den LAN-Adapter.
- [Software Reset Betty-TV](../forum/topics/0090-software-reset-betty-tv.md) — Software-Reset nach der Betty-TV-Abschaltung.

### Betty vergisst Programmierungen

- ["Vergisst" die Betty manche Programmierungen mit der Zeit?](../forum/topics/0254-vergisst-die-betty-manche-programmierungen-mit-der-zeit.md) — Betty vergisst nach einiger Zeit Fernbedienungscodes.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

