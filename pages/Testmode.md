# Testmode

Wenn man die Betty-Fernbedienung ueber ein [Interface](Interfaces%20PC%20zu%20Betty.md "Interfaces PC zu Betty") mit dem PC verbindet, kann man in einen Terminalprogramm die Debugausgaben der Betty sehen. Die Einstellungen der seriellen Schnittstelle sind 115200 Baud, 8N1.

    BettyHHUbootloader 00003264 00B770ED 1MByte
    BIOS 000033A0 000233E0 81D8E589
    no new BIOS
    BIOS 000233E0 81D8E589
    starting BIOS...<25>
    <\0>
    Betty HHU BIOS 00B770ED 1MB
    INFO: 512 13216->13216
    search for new...
     MAINAPP
     GAMEAPP
     PRODAPP
     EPGAPP
     FONTs
     SOUNDs
     IRDB
     LOTTOAPP
    NVRAM Recovery:
     V6
     CRC CC38B9F3/41420B1A
     WARNING: NVRAM corrupted
     nothing to recover
    ???PCBA TEST???

    *** Main Cat4E49414D 13214
    Main started
    *** Game Cat454D4147 12900
    App EPG_ no V0 @0x80070000!
    *** FONT 12900 F
    *** WAVE 12900
    *** HW V3
    *** FLASH 1C5B
    *** ID 26C79E0B1F18
    RFHandler SCART Thread started
    *** FREQOFFSET 7
    *** SCARTID 246328
    *** SCART_CHANNEL 6
    *** CC 0003
    ~*** System up and running
    2006.02.16 16:16:17 (1140106577) : Containers 0%
    BIOSEPG - event 0x40000000
    BIOSEPG - msg 0x10020000
    BIOSEPG - REDRRAW
    <27>[45m MainApp got 08150000 <27>[0m
    IW msg 08150000 at state 6
    call home...
    Call@UTC: Time=1140106577, Prio=1, Reason=7
    New Call @1140106577 Reason=7
     erase_sector @0x82010000
     erase_sector @0x82020000
     erase_sector @0x82030000
     erase_sector @0x82040000
     erase_sector @0x82050000
    !2006.02.16 16:16:20 (1140106580) : search channel 6 for 246328
    *** FREQOFFSET 7
    *** SCARTID 246328
    *** SCART_CHANNEL 6
    *** CC 0003
    ~CRC SC VIRGIN !
    CRC NVM False !
    NVM: -1 9E3FCF89 FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF
     SC: 0 27D8BF0D 00000000 00000000 00000000 00000000
    Key 0 80000002
    Key 1 00000002
    Key 2 80000002
    Key 3 00000002
    Key 4 80000002
    Key 5 00000002
    Key 6 00000002
    Key 7 00000002
    Key 8 00000002
    Key 9 00000002
    Key 10 80000002
    Key 11 80000002
    2006.02.16 16:16:21 (1140106581) : CALL 7 Exec
    2006.02.16 16:16:22 (1140106582) : ** LS: ScartUpdate -> ScartStatusPoll TaeSearch 10 0 ==
    SCART_CTRL_SM: STA
    !RFHandler SCARTCTRL Thread started

    Channel RSSI:
     Chn0 -22 ===============>
     Chn1 -24 ==============>
     Chn2 -22 ===============>
     Chn3 -20 ===============>
     Chn4 -22 ===============>
     Chn5 -23 ===============>
    *Chn6 -25 ==============>
     Chn7 -23 ===============>

    Channel RSSI:
     Chn0 -22 ===============>
     Chn1 -24 ==============>
     Chn2 -22 ===============>
     Chn3 -20 ===============>
     Chn4 -22 ===============>
     Chn5 -23 ===============>
    *Chn6 -25 ==============>
     Chn7 -23 ===============>
    Choose RF Channel #6


    CTRL SCART 246328 on channel 6

    get SCART STATUS

Ein weiterer Mitschnitt: <http://betty.zentgraf-modding.de/index.php?s=info&p=1>

Um auch Befehle vom Terminal zur Betty schicken zu koennen, muss man erst einen geheimen mit einem Passwort geschuetzten Testmode aktivieren.

Durch den Testmode kann man die Betty vom PC aus fernsteuern. Ein Tastendruck im Terminal bewirkt einen Tastendruck auf der Fernbedienung und der Displaytext auf der Betty erscheint auch auf dem Terminal.

Die Aktivierung des Testmode funktioniert wie folgt:

- Den „Bootloader EN, Aktiv = LOW (EINT1)“ Pin am [Servicestecker](Betty%20Hardware.md "Betty Hardware") offen lassen und den Akku einlegen.
- Am Terminal sind jetzt die Ausgaben der Betty zu sehen.
- Jetzt den „Bootloader EN, Aktiv = LOW (EINT1)“ Pin mit Masse verbinden.
- Dann das Passwort „Gurkensalat“ im Terminal eingeben.
- „got secret key - accept serial input“ erscheit als Bestaetigung im Terminal.
- Jetzt "K" (Grossgeschrieben) druecken
- Ab jetzt erscheinen die Aenderungen im Display auch auf dem Terminal. Jede Displayzeile ist in die Tags \<LCD\> und \</LCD\> eingeschlossen um sie von den normalen Debugmeldungen unterscheiden zu koennen.
- Die Zuordnung der Terminaltasten zu den Bettytasten ist in der folgenden Tabelle dargestellt (z.B. entspricht die Klammer-Auf-Taste „(“ der OK-Taste auf der Betty).

  

|             |               |        |
|-------------|---------------|--------|
| Betty-Taste | PC-Taste      | IR-Key |
| A           | !             | 16     |
| B           | "             | 11     |
| C           | \#            | 12     |
| D           | \$            | 22     |
| Betty       | \<unbekannt\> | 26     |
| Exit        | \*            | 42     |
| Hoch        | %             | 21     |
| Runter      | ,             | 51     |
| Links       | ’             | 31     |
| Rechts      | )             | 32     |
| OK          | (             | 41     |
| VOL +       | \+            | 36     |
| VOL -       | \-            | 46     |
| Mute        | .             | 61     |
| PROG +      | \<unbekannt\> | 52     |
| PROG -      | /             | 62     |
| 1           | 0             | 15     |
| 2           | 1             | 71     |
| 3           | 2             | 72     |
| 4           | 3             | 25     |
| 5           | 4             | 14     |
| 6           | 5             | 13     |
| 7           | 6             | 35     |
| 8           | 7             | 24     |
| 9           | 8             | 23     |
| 0           | :             | 34     |
| -/--        | 9             | 45     |
| AV          | ;             | 33     |
| MENU        | \<            | 56     |
| PiP         | =             | 55     |
| A/B         | \>            | 44     |
| 16:9        | ?             | 43     |
| i           | @             | 66     |
| VT an       | A             | 65     |
| VT aus      | B             | 54     |
| VT Opak     | C             | 53     |
| Rot         | D             | 76     |
| Grün        | E             | 75     |
| Gelb        | F             | 64     |
| Blau        | G             | 63     |
| TV          | H             | 74     |
| Power/StdBy | I             | 73     |

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

