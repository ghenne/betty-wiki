# Speicheraufteilung

# Flash1

Der Inhalt des ersten Flashbausteins der Betty ist modular aufgebaut. Jedem Modul ist ein fester Adressbeich zugewiesen. Bei einer jungfräulichen Betty ist das EPG- und LOTTO-Modul noch nicht vorhanden.

## BOOT

- Adressbereich: 80000000h - 8000FFFFh
- Modul-Offset 0-1Fh: Exception Vector Locations
- Modul-Offset 40h: Modullänge ab Offset 40h
- Modul-Offset 44h: ReferenzCRC

CRC-Wert wird von Offset 48h bis zum Offset der sich aus der Modullänge berechnen lässt gebildet.

## FONT

- Adressbereich: 80010000h - 8001FFFFh
- Modul-Offset 10h: ReferenzCRC
- Modul-Offset 14h: Modullänge ab Offset 0

CRC-Wert wird von Offset 14h bis zum Offset der sich aus der Modullänge berechnen lässt gebildet.

## BIOS

- Adressbereich: 80020000h - 8005FFFFh
- Modul-Offset 10h: ReferenzCRC
- Modul-Offset 14h: Modullänge ab Offset 0

CRC-Wert wird von Offset 14h bis zum Offset der sich aus der Modullänge berechnen lässt gebildet.

## PROD

- Adressbereich: 80060000h - 8006FFFFh
- Modul-Offset 10h: ReferenzCRC
- Modul-Offset 14h: Modullänge ab Offset 0

CRC-Wert wird von Offset 14h bis zum Offset der sich aus der Modullänge berechnen lässt gebildet.

## EPG

- Adressbereich: 80070000h - 8007FFFFh

Dieses Modul ist bei einer jungfräulichen Betty noch nicht vorhanden.

## MAIN

- Adressbereich: 80080000h - 8009FFFFh
- Modul-Offset 10h: ReferenzCRC
- Modul-Offset 14h: Modullänge ab Offset 0

CRC-Wert wird von Offset 14h bis zum Offset der sich aus der Modullänge berechnen lässt gebildet.

## GAME

- Adressbereich: 800A0000h - 800AFFFFh
- Modul-Offset 10h: ReferenzCRC
- Modul-Offset 14h: Modullänge ab Offset 0

CRC-Wert wird von Offset 14h bis zum Offset der sich aus der Modullänge berechnen lässt gebildet.

## WAVE

- Adressbereich: 800B0000h - 800CFFFFh
- Modul-Offset 10h: ReferenzCRC
- Modul-Offset 14h: Modullänge ab Offset 0

CRC-Wert wird von Offset 14h bis zum Offset der sich aus der Modullänge berechnen lässt gebildet.

## LOTTO

- Adressbereich: 800D0000h - 800FFFFFh

Dieses Modul ist bei einer jungfräulichen Betty noch nicht vorhanden.

# Flash2

Im zweiten Flashbaustein werden die mitgeloggten Aktionen sowie die über den TAE-Adapter empfangenen Updates zwischengespeichert.

# Smartcard-Chip

Der Chip enthält u.a. zwei Speicherbereich (SC_MEM & SC_Sec_MEM) die ausgelesen werden können. Die passenden Kommanos sind im Artikel [Smartcardchip](Smartcardchip.md "Smartcardchip") dokumentiert.

## SC_MEM

Dieser Speicherbereich enhält E3h Register (0 .. E2h). Ein Register kann ein DWORD (4 Bytes) aufnehmen.

|          |           |
|----------|-----------|
| Register | Bedeutung |
| 0        | ?         |
| ..       | ?         |
| E2h      | ?         |

## SC_Sec_MEM

Dieser Speicherbereich enhält 96h Register (0 .. 95h). Ein Register kann ein DWORD (4 Bytes) aufnehmen.

|          |           |
|----------|-----------|
| Register | Bedeutung |
| 0        | ?         |
| ..       | ?         |
| 95h      | ?         |

<!-- forum-links:start -->
## Forumsdiskussionen: freier Speicher in Boop

Wie viel RAM und Flash in Boop für eigene Variablen und Programme frei bleibt.

### Speicherplatz in Boop (RAM/Flash)

- [Wieviel Speicher bleibt in Boop für weitere Variablen](https://github.com/ghenne/betty-forum/blob/main/topics/0266-wieviel-speicher-bleibt-in-boop-fuer-weitere-variablen.md) — Freien RAM/Flash in Boop für eigene Variablen und Programme ermitteln.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

