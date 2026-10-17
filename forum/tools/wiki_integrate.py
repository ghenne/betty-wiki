#!/usr/bin/env python3
"""Integriert die Forum-Lückenliste in das Wiki.

Liest WIKI-LUECKEN.md, ordnet jeden Eintrag einer Zielseite zu und
erzeugt dort einen Abschnitt mit Forumslinks, Kurzbeschreibung und
kompakter Einordnung. Neue Oberthemen-Seiten werden nur angelegt, wenn
es die Seite noch nicht gibt.

Aufruf: python3 tools/wiki_integrate.py [--wiki ..] [--write]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WIKI = ROOT.parent
LIST = ROOT / "WIKI-LUECKEN.md"
FORUM_BASE = "../forum"
START = "<!-- forum-links:start -->"
END = "<!-- forum-links:end -->"

# Eintragstitel aus WIKI-LUECKEN.md -> Zielseite
PAGES: list[dict] = [
    {
        "page": "MPD", "new": True, "title": "MPD",
        "intro": (
            "MPD (Music Player Daemon) ist ein Musikserver, der über das Netzwerk "
            "gesteuert wird. Im Forum ist eine Firmware dokumentiert, mit der Betty "
            "als MPD-Client arbeitet: Sie zeigt Titel und Interpreten an und steuert "
            "Wiedergabe, Lautstärke und Playlist. Zusätzlich muss der Scart-Adapter "
            "geflasht und ein Hilfsprogramm auf dem MPD-Server installiert werden."
        ),
        "entries": ["MPD-Client"],
    },
    {
        "page": "Funksteckdosen", "new": True, "title": "Funksteckdosen und Funkprotokolle",
        "intro": (
            "Mit dem CC1100-Transceiver kann Betty Funksteckdosen im 433/434-MHz-Band "
            "schalten. Behandelt werden Intertechno- und Baumarkt-Steckdosen "
            "(OOK/ASK), FS20/HX2262 sowie S.N.A.P. als Rahmen für eigene Funkdaten. "
            "Die Threads enthalten Codes, Reichweiten und Schaltbeispiele; X10 blieb "
            "im Forum eine offene Frage."
        ),
        "entries": [
            "Funksteckdosen (Intertechno, 434 MHz)", "FS20 / HX2262",
            "S.N.A.P.-Protokoll für Funkdaten", "X10-Protokoll",
        ],
    },
    {
        "page": "IR-Codes", "new": True, "title": "IR-Codes und LIRC",
        "intro": (
            "Boop kann Infrarot-Codes senden und empfangen. Die folgenden Threads "
            "behandeln RC5/RC6, das RC5-Toggle-Bit, RAW-Codes, LIRC-Codecs "
            "(Xoro HRS3000, Harman Kardon) und das Anlernen fremder Fernbedienungen. "
            "Sie ergänzen die Feature-Liste in `Boop Features` um konkrete Codes und "
            "Vorgehensweisen."
        ),
        "entries": [
            "IR-Codes: RC5/RC6, RAW-Codes, LIRC",
            "LIRC-Sender/Empfänger und Funkfernbedienung",
        ],
        "exclude_ids": [162],
    },
    {
        "page": "Recovery", "new": True, "title": "Recovery und Fehlerbilder",
        "intro": (
            "Startet Betty nach einem fehlerhaften Flash, einem Flash-Erase oder einem "
            "Hardwaredefekt nicht mehr, helfen die hier gesammelten Fehlerbilder und "
            "Rettungswege. Dazu gehören der Fehlercode C20A0001, ein defekter "
            "Bootloader, JTAG/OpenOCD, J-Link und Fälle, in denen lpctool nicht mehr "
            "flashen kann."
        ),
        "entries": ["Betty tot: Error C20A0001 / Recovery", "J-Link anschließen"],
    },
    {
        "page": "Wiki", "new": True, "title": "Wiki und Webseite",
        "intro": (
            "Hinweise zum Wiki selbst: Backup und Sicherheit, Link-Updates, "
            "User-CSS und frühe Wiki-Threads. Die Seite sammelt die Meta-Informationen, "
            "die nicht zu Hardware oder Firmware gehören."
        ),
        "entries": ["Sicherheit/Backup des Wikis", "Wichtige Links"],
        "extra_links": [
            (5, "Frühe Wiki-Diskussion."),
            (71, "Wiki-Update-Ankündigung."),
            (78, "Wiki-Style und User-CSS."),
            (183, "Link zum Wiki."),
            (1055, "Wiki-Probleme."),
            (1056, "Wiki und Webseite allgemein."),
        ],
    },
    {
        "page": "Entwicklungsumgebungen", "new": False,
        "section": "Forumsdiskussionen: Toolchain und Build",
        "intro": (
            "Ergänzend zur Toolchain-Übersicht: konkrete Builds unter Linux, macOS "
            "und Windows (WinARM, Cygwin, CodeSourcery, Debian, arm-launchpad), "
            "Makefile-Anpassungen und typische Compiler-/Linkerfehler."
        ),
        "entries": [
            "Toolchain für Mac OS X / Linux", "McBetty/Toolchain einrichten",
            "GCC 4.5.2 CodeSourcery: Alignment-Warnings",
            "Debian Squeeze: passende Toolchain", "arm-launchpad-Compiler",
            "WinARM unter Windows 7 x64 / WinARM-Build",
            "Boop kompilieren: Fehler und Compilerfehler",
            "undefined reference: strncpy/strncat/strnlen",
            "Keil als alternative IDE", "Lokale Toolchain-Settings",
        ],
    },
    {
        "page": "LPCTool", "new": False,
        "section": "Forumsdiskussionen: Quellen, Programmer und Timing",
        "intro": (
            "Ergänzungen zum LPCTool: Quellcode und RAM-Programme, BusPirate als "
            "Programmer, Timingprobleme mit dem PL-2303 unter Ubuntu, Cygwin-Builds "
            "und der Soft-Reset nach dem Flashen."
        ),
        "entries": [
            "LPCTool-Quellen und RAM-Programm", "BusPirate als Programmer",
            "lpctool unter Ubuntu / PL-2303-Timing",
            "lpctool mit Cygwin unter Windows 7 bauen", "Soft-Reset nach dem Flashen",
        ],
    },
    {
        "page": "Firmware flashen", "new": False,
        "section": "Forumsdiskussionen: U-Boot, Update und Flashprobleme",
        "intro": (
            "Ergänzungen zum Flashen: U-Boot als alternativer Bootloader, das "
            "Mitschneiden des Original-Updates, Probleme nach dem Boop-Flash und das "
            "Flashen des SCART-Adapters."
        ),
        "entries": [
            "U-Boot als alternativer Bootloader", "Firmware-Update mitschneiden",
            "Boop-Flashprobleme", "SCART-Adapter flashen (Fehler und Ablauf)",
        ],
    },
    {
        "page": "SCART Adapter", "new": False,
        "section": "Forumsdiskussionen: Programmierung und Terminalmodus",
        "intro": (
            "Der SCART-Adapter lässt sich auch ohne Kombi-Interface programmieren; "
            "zusätzlich ist ein Terminalmodus mit seriellen Einstellungen dokumentiert."
        ),
        "entries": [
            "SCART programmieren ohne Kombi-Interface", "SCART-Terminalmode",
        ],
    },
    {
        "page": "Simple Serial Interface", "new": False,
        "section": "Forumsdiskussionen: Adapter, Sniffing und VT-Datenstrom",
        "intro": (
            "Ergänzungen zur seriellen Anbindung: TTL-Wandler, Handydatenkabel, "
            "TXD1- und Daten-Sniffing sowie die Übertragung per VT-Datenstrom."
        ),
        "entries": [
            "Daten sniffen", "TTL-Wandler", "TXD1 sniffen / Datenmüll",
            "Handydatenkabel vs. Simple Serial Interface",
            "VT-Datenstrom zur Datenübertragung",
        ],
    },
    {
        "page": "LOG", "new": False, "section": "Forumsdiskussionen: Bootlog",
        "intro": "Ergänzung zum Bootlog: Der Fall, dass er nur unter Windows 98 funktioniert.",
        "entries": ["Bootlog nur unter Windows 98"],
    },
    {
        "page": "Boop Features", "new": False,
        "section": "Forumsdiskussionen: Makros und Tastenbelegung",
        "intro": (
            "Ergänzung zu den Boop-Features: Makros (mehrere Codes pro Taste) und "
            "wechselnde Tastenbelegungen."
        ),
        "entries": [
            "Boop: Makros und wechselnde Tastenbelegungen",
            "Boop: Fernbedienung anlernen",
        ],
    },
    {
        "page": "Bmp2b", "new": False, "section": "Forumsdiskussionen: bmp2b",
        "intro": "Das bmp2b-Tool wandelt 128x160-BMP-Dateien in Betty-taugliche Logos um.",
        "entries": ["BMP-Logos und bmp2b-Tool"],
    },
    {
        "page": "Speicheraufteilung", "new": False,
        "section": "Forumsdiskussionen: freier Speicher in Boop",
        "intro": "Wie viel RAM und Flash in Boop für eigene Variablen und Programme frei bleibt.",
        "entries": ["Speicherplatz in Boop (RAM/Flash)"],
    },
    {
        "page": "Flash access", "new": False,
        "section": "Forumsdiskussionen: BFS_LoadFile und Flash1",
        "intro": "BFS_LoadFile, Flash1 und eine Kontrasteinstellung im Settingsmenü.",
        "entries": ["BFS_LoadFile / Flash1 und Kontrasteinstellung"],
    },
    {
        "page": "CC1100", "new": False,
        "section": "Forumsdiskussionen: Defines, RTC, 868 MHz und RFM12",
        "intro": (
            "Ergänzungen zum CC1100: mögliche falsche Defines in `cc1100/rf.h`, "
            "RTC-/RF-Ablauf, Umbau auf 868 MHz, RFM12 als Alternative und Betrieb "
            "mehrerer Bettys."
        ),
        "entries": [
            "RTC: send_time / ask_for_time und RF-Ablauf",
            "cc1100/rf.h: mögliche falsche Defines", "Umbau auf 868 MHz",
            "RFM12 als Funk-Alternative", "Mehrere Bettys / Funkverbindung",
        ],
    },
    {
        "page": "LPC2220", "new": False, "section": "Forumsdiskussionen: PLL und setSpeed",
        "intro": "Taktfrequenz des LPC2220 per setSpeed (30/60 MHz) und Grenzen beim Pin-Toggeln.",
        "entries": ["PLL umschalten / setSpeed"],
    },
    {
        "page": "SVN", "new": False, "section": "Forumsdiskussionen: Quellcode und SVN",
        "intro": "Bezug des Boop-Quellcodes, SVN-Ausfall und neuer Server, aufgeräumtes Repository.",
        "entries": ["Boop-Quellcode und SVN-Zugang"],
    },
    {
        "page": "Boop", "new": False, "section": "Forumsdiskussionen: Bugs und Patches",
        "intro": "Fehler und Patches aus der Community, u. a. in `infrared.c`.",
        "entries": ["Bugs/Patches: infrared.c und Boop-Firmware"],
    },
    {
        "page": "TAE Adapter", "new": False,
        "section": "Forumsdiskussionen: PCD80718HL",
        "intro": "Programmierung des PCD80718HL im Umfeld des TAE-Adapters.",
        "entries": ["PCD80718HL programmieren"],
    },
    {
        "page": "MSP430 Pin-Belegung", "new": False,
        "section": "Forumsdiskussionen: MSP430 über den TAE-Adapter",
        "intro": "Programmierung des MSP430 über den TAE-Adapter sowie Nutzen und Grenzen.",
        "entries": ["TAE-Adapter und MSP430-Programmierung"],
    },
    {
        "page": "SCART-Betty-Kombiinterface", "new": False,
        "section": "Forumsdiskussionen: Platine und Schaltplan",
        "intro": "Platine, Schaltplan und Aufbau des Kombiinterfaces.",
        "entries": ["Kombiinterface: Platine und Schaltplan"],
    },
    {
        "page": "Anschlussbelegungen", "new": False,
        "section": "Forumsdiskussionen: LCD-Controller und Anschluss",
        "intro": (
            "Der verbaute LCD-Controller (Epson S1D15710-Serie), seine Kommandos und "
            "der LCD-Anschluss."
        ),
        "entries": ["LCD-Treiberchip und LCD-Anschluss"],
    },
    {
        "page": "LPC2220 Pin-Belegung", "new": False,
        "section": "Forumsdiskussionen: freie Pins und Erweiterungen",
        "intro": "Unbelegte IOs, freie GPIOs sowie SPI- und SD/MMC-Nutzung.",
        "entries": ["Freie Pins, GPIOs, SPI, SD/MMC"],
    },
    {
        "page": "Betty Hardware", "new": False,
        "section": "Forumsdiskussionen: Schaltplan und Revisionen",
        "intro": "Schaltplan/Schematic und Unterschiede verschiedener Hardwarerevisionen.",
        "entries": ["Schaltplan und Hardwarerevisionen"],
    },
    {
        "page": "Betty TV", "new": False,
        "section": "Forumsdiskussionen: Swisscom und Betty-TV-Aus",
        "intro": (
            "Swisscom-Variante und Tastaturbelegung sowie die Abschaltung des "
            "interaktiven Betty-TV-Angebots und ihre Folgen."
        ),
        "entries": [
            "Swisscom-Tastatur", "Swisscom-Hardware", "Betty-TV-Aus und Folgen",
        ],
    },
    {
        "page": "Umbau auf LiIon Akku", "new": False,
        "section": "Forumsdiskussionen: Spannungsversorgung",
        "intro": "Spannungsversorgung und Stromverbrauch der Betty.",
        "entries": ["Spannungsversorgung"],
    },
    {
        "page": "Interfaces PC zu Betty", "new": False,
        "section": "Forumsdiskussionen: bidirektionale Kommunikation",
        "intro": "Bidirektionale Kommunikation zwischen PC und Betty und ihre Anwendungsfälle.",
        "entries": ["Bidirektionale Kommunikation mit dem PC"],
    },
    {
        "page": "Betty", "new": False,
        "section": "Forumsdiskussionen: Einstieg, Ziele und Bezugsquellen",
        "intro": (
            "Einordnung und Einstieg: Ziele und Nutzungsszenarien, Bezugsquellen "
            "(Pollin), Marktwert und Betrieb mit anderen Sendern."
        ),
        "entries": [
            "Welches Ziel mit der Betty?", "Betty, andere Sender?",
            "Bezugsquellen und Marktwert", "Einstieg: Betty von Pollin, Software woher?",
        ],
    },
    {
        "page": "Projekte", "new": False,
        "section": "Forumsdiskussionen: Oszilloskop und RCOS",
        "intro": "Projekte mit der Betty: Lowcost-Oszilloskop, bettycheck/RCOS und verwandte Anwendungen.",
        "entries": ["Betty als Oszilloskop / RCOS-Projekt"],
    },
    {
        "page": "Original Firmware", "new": False,
        "section": "Forumsdiskussionen: Universalfernbedienung",
        "intro": (
            "Original-Firmware und Universalfernbedienung: Aufspielen, Software-Reset "
            "und das Vergessen von Programmierungen."
        ),
        "entries": [
            "Universalfernbedienung / Original-Firmware",
            "Betty vergisst Programmierungen",
        ],
    },
]

# Manuelle Kurzbeschreibungen fuer wichtige Threads (ueberschreiben Automatik)
OVERRIDES = {
    220: "Firmware für Betty als MPD-Client: Titel/Interpret anzeigen, Wiedergabe und Playlist steuern.",
    223: "Intertechno-Funksteckdosen mit dem CC1100 ansteuern (434 MHz, OOK/ASK), inkl. Codes und Reichweite.",
    86: "Baumarkt-Funksteckdosen im 433-MHz-Band mit Betty schalten, Master-Schaltung.",
    232: "Funk-Steckdosen mit HX2262-Sender über den FS20-Code anbinden.",
    95: "S.N.A.P. als Protokollrahmen für die Funkübertragung.",
    262: "Frage, ob Betty mit einem X10-Funkempfänger betrieben werden kann; keine abschließende Lösung.",
    110: "Eigene Fernbedienungscodes in Boop einbinden bzw. den Quellcode anpassen.",
    141: "Betty mit Boop anlernen und den Code einer Sagem DBox2 einbinden.",
    145: "Von der Community geschriebener RC6-Encoder für Boop.",
    156: "Behandlung des RC5-Toggle-Bits im Generic-TV-Encoder.",
    187: "RAW-IR-Codes auslesen und in eine eigene Fernbedienungsdefinition übernehmen.",
    253: "LIRC-Codec für den Xoro HRS3000 SAT-Receiver.",
    259: "Fernbedienung des Humax S HD 3 per lirc für Boop anlernen.",
    162: "IR-Signale aufzeichnen/wiedergeben und fremde Fernbedienungen an Boop anlernen.",
    214: "Harman-Kardon-Verstärker anlernen (im Thread ohne Lösung).",
    148: "SCART-Adapter ohne Kombi-Interface programmieren; ICP-Routinen auf andere Mikrocontroller portiert.",
    226: "Terminalmodus des SCART-Adapters mit seriellen Einstellungen (38400,n,8,1).",
    258: "Umbau der Betty zum Lowcost-Oszilloskop mit Modellbau-Features.",
    242: "Betty als Backend für RCOS/bettycheck.",
    300: "Betty wieder zur Universalfernbedienung umprogrammieren.",
    154: "Neue Software auf eine Betty aufspielen.",
    89: "Neue Software von Betty-TV und Update über den LAN-Adapter.",
    90: "Software-Reset nach der Betty-TV-Abschaltung.",
    274: "Funkverbindung und Betrieb mehrerer Bettys.",
    255: "Makros und wechselnde Tastenbelegungen in Boop.",
    179: "bmp2b: 128x160-BMP-Logos für Betty konvertieren.",
    266: "Freien RAM/Flash in Boop für eigene Variablen und Programme ermitteln.",
    231: "BFS_LoadFile, Flash1 und eine Kontrasteinstellung im Settingsmenü.",
    243: "Ablauf der RF-Zeitabfrage (send_time/ask_for_time).",
    267: "PLL/setSpeed: Taktfrequenz erhöhen und Grenzen beim Pin-Toggeln.",
    1057: "Mögliche falsche Defines in cc1100/rf.h beim Bau mit arm-gcc 4.8.4.",
    190: "Kleinere Unschönheit in infrared.c.",
    229: "Bug-/Patch-Sammlung von Boop-Nutzern ohne SVN-Zugang.",
    207: "Boop-Quellcode beziehen (SVN).",
    210: "SVN-Server-Ausfall und neuer Server.",
    64: "Boop und lpctool im SVN.",
    83: "Aufgeräumtes Boop-SVN.",
    32: "U-Boot als Universal-Bootloader und Eignung für den LPC2220.",
    82: "Datenübertragung über den SCART-Adapter per VT-Datenstrom.",
    7: "Original-Firmware-Update mitschneiden/dumpen.",
    261: "Boop unter Mac OS X/Linux kompilieren und Toolchain bauen.",
    273: "McBetty aus GitHub-Quellen mit WinARM bauen.",
    269: "GCC 4.5.2 von CodeSourcery: Alignment-Warnungen und newlibc/uClibc.",
    1049: "Boop aus aktuellen Quellen unter Debian Squeeze bauen.",
    1050: "ARM-Launchpad-Compiler für Betty.",
    1046: "WinARM unter Windows 7 x64 einrichten und libgcc.a ersetzen.",
    295: "Boop mit WinARM 20060606 kompilieren.",
    106: "Typische Fehler beim Boop-Build.",
    289: "Compilerfehler beim Boop-Build.",
    227: "Linkerfehler bei strncpy/strncat/strnlen.",
    109: "Betty-Software mit Keil erstellen.",
    75: "Boop und lpctool mit GCC 4.1.1 bauen, lokale Settings.",
    215: "LPCTool-Quellcode und ein Beispielprogramm im RAM.",
    288: "BusPirate im UART-Modus als Programmer für Betty.",
    228: "Reset-/eINT1-Timingprobleme mit PL-2303 unter Ubuntu.",
    241: "lpctool mit Cygwin unter Windows 7 bauen.",
    189: "Soft-Reset über RX/TX/GND nach dem Flashen.",
    178: "Probleme beim Boop-Flash.",
    280: "Nach dem Boop-Flash startet nichts: typische Ursachen und Abhilfe.",
    186: "Fehler beim Flashen des SCART-Adapters mit BettyHeaven/Kombiinterface.",
    176: "Flashen des SCART-Adapters: Ablauf und Stolperfallen.",
    239: "Betty nach Flüssigkeitsschaden: Fehler C20A0001 und Rettungsversuche.",
    146: "Defekter Bootloader und Recovery.",
    293: "Cannot flash: lpctool/NXP/BettyHeaven.",
    291: "Nach Flash-Erase keine JTAG-Verbindung mehr.",
    294: "J-Link von Segger an Betty anschließen.",
    84: "Bootlog funktioniert nur unter Windows 98.",
    254: "Betty vergisst nach einiger Zeit Fernbedienungscodes.",
    1051: "Einstieg mit einer Pollin-Betty: welche Software, welche Toolchain.",
    279: "Bettys bei Pollin: Bezug und Erfahrungen.",
    225: "Datenverkehr mitschneiden und auswerten.",
    202: "Tastatur/Belegung der Swisscom-Variante.",
    29: "TTL-Pegelwandler für serielle Verbindungen.",
    22: "TTL-Wandler (kurzer Thread).",
    27: "TXD1 mitschneiden und Datenmüll analysieren.",
    165: "Handydatenkabel oder Simple Serial Interface: Vergleich.",
    152: "Handydatenkabel mit BettyHeaven nutzen.",
    182: "TAE-Adapter als MSP430-Programmer.",
    206: "Programmieren des MSP430 über den TAE-Adapter: Nutzen und Grenzen.",
    208: "TAE und serielle Verbindung.",
    248: "Schaltplan des Kombiinterfaces.",
    125: "Platine des Kombiinterfaces.",
    233: "PCD80718HL programmieren.",
    51: "Verwendeter LCD-Controller (Epson S1D15710-Serie) und Kommandos.",
    119: "LCD-Anschluss an der Betty.",
    122: "Pinbelegung und unbelegte IOs.",
    278: "Freie GPIOs der Betty für Erweiterungen.",
    246: "Freie Pins, SPI und SD/MMC.",
    286: "Schaltplan/Schematic der Betty.",
    1052: "Unterschiedliche Hardwarerevisionen.",
    128: "Swisscom-Variante der Betty.",
    205: "Swisscom-Betty im Betrieb.",
    191: "Spannungsversorgung und Stromverbrauch.",
    247: "Umbau der Funkstrecke auf 868 MHz.",
    93: "Kommunikation zur Betty mit RFM12.",
    216: "Betty als LIRC-Sender und -Empfänger.",
    218: "Betty als Funkfernbedienung.",
    14: "Grundsatzdiskussion zu Zielen und Nutzungsszenarien.",
    56: "Betty mit anderen Sendern/Quellen nutzen.",
    134: "Bidirektionale Kommunikation zwischen PC und Betty.",
    69: "Abschaltung des interaktiven Betty-TV-Angebots.",
    74: "Aus für Betty TV auch in Deutschland.",
    77: "Abspeckung der Betty-Firmware zum 31. November.",
    103: "Geht Betty noch? Status nach der Abschaltung.",
    149: "Infos zur Betty-TV-Abschaltung.",
    20: "Marktwert und Preise für Bettys.",
    123: "Backup- und Sicherheitsüberlegungen für Wiki/Webseite.",
    3: "Sammlung wichtiger externer Links aus der Frühphase.",
}


def parse_list() -> dict[str, dict]:
    text = LIST.read_text(encoding="utf-8")
    entries: dict[str, dict] = {}
    cur = None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = None
        elif line.startswith("### "):
            cur = line[4:]
        elif line.startswith("- [ ] **"):
            m = re.match(r"- \[ \] \*\*(.+?)\*\* — (.+)", line)
            if m:
                entries[m.group(1)] = {
                    "ids": [int(x) for x in re.findall(r"\[(\d+)\]", m.group(2))],
                    "cluster": cur,
                }
    return entries


def load_topics() -> dict[int, dict]:
    return {
        t["topic_id"]: t
        for t in json.loads((ROOT / "_meta" / "topics.json").read_text(encoding="utf-8"))["topics"]
    }


def clean_text(s: str) -> str:
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_>`#]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def auto_desc(topic_file: Path) -> str:
    text = topic_file.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^## 1\..*?\n\n(.*?)(?=\n\n<a id=|\Z)", text, re.S | re.M)
    body = clean_text(m.group(1) if m else "")
    body = re.sub(
        r"^(hallo|hi|moin|guten (abend|tag)|nabend|n'abend|aloha|hey|servus)[^.!?]*[.!?]\s*",
        "", body, flags=re.I,
    )
    body = re.sub(r"^(alle zusammen|zusammen|allerseits)[,.!]\s*", "", body, flags=re.I)
    if len(body) < 40:
        # zweiter Absatz / naechster sinnvoller Text
        parts = [p for p in re.split(r"(?<=[.!?])\s+", body) if len(p) > 30]
        body = " ".join(parts[:2]) if parts else body
    # auf zwei Saetze / 180 Zeichen kuerzen
    sentences = re.split(r"(?<=[.!?])\s+", body)
    out = ""
    for s in sentences:
        if len(out) + len(s) + 1 > 180:
            break
        out = (out + " " + s).strip()
    return (out or body)[:200].rstrip() + ("…" if len(body) > 200 else "")


def build_block(entry: dict, topics: dict[int, dict], exclude: set[int] | None = None) -> str:
    lines = []
    exclude = exclude or set()
    for tid in entry["ids"]:
        if tid in exclude:
            continue
        t = topics.get(tid)
        if not t:
            continue
        desc = OVERRIDES.get(tid) or auto_desc(ROOT / "topics" / t["file"])
        lines.append(
            f"- [{t['title']}]({FORUM_BASE}/topics/{t['file']}) — {desc}"
        )
    return "\n".join(lines)


def upsert_page(wiki: Path, spec: dict, entries: dict[str, dict], topics: dict[int, dict], write: bool) -> None:
    page = wiki / "pages" / f"{spec['page']}.md"
    blocks = []
    for title in spec["entries"]:
        e = entries.get(title)
        if not e:
            raise SystemExit(f"Eintrag nicht gefunden: {title!r}")
        block = build_block(e, topics, set(spec.get("exclude_ids", [])))
        if block:
            blocks.append(f"### {title}\n\n{block}")
    extra = []
    for tid, desc in spec.get("extra_links", []):
        t = topics.get(tid)
        if t:
            extra.append(
                f"- [{t['title']}]({FORUM_BASE}/topics/{t['file']}) — {desc}"
            )
    if extra:
        blocks.append("### Ergänzende Wiki-Threads\n\n" + "\n".join(extra))
    body = "\n\n".join(blocks)
    intro = spec.get("intro", "").strip()
    section = f"{intro}\n\n{body}".strip()

    if spec.get("new") and not page.exists():
        content = (
            f"# {spec['title']}\n\n{intro}\n\n"
            f"{START}\n## Forumsdiskussionen\n\n{body}\n{END}\n\n"
            "---\n\n"
            "[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)\n"
        )
    else:
        text = page.read_text(encoding="utf-8")
        heading = spec.get("section", "Forumsdiskussionen")
        block = f"{START}\n## {heading}\n\n{section}\n{END}\n"
        if START in text and END in text:
            text = re.sub(
                re.escape(START) + r".*?" + re.escape(END) + r"\n?",
                block, text, flags=re.S,
            )
        else:
            footer = "\n---\n\n[Startseite](Main%20Page.md)"
            idx = text.rfind(footer)
            if idx == -1:
                text = text.rstrip() + "\n\n" + block
            else:
                text = text[:idx] + "\n" + block + text[idx:]
        content = text

    if write:
        page.write_text(content, encoding="utf-8")
    print(f"{'neu ' if spec.get('new') and not page.exists() else 'aktualisiert'} pages/{spec['page']}.md")


def update_index(wiki: Path, new_pages: list[tuple[str, str]], write: bool) -> None:
    p = wiki / "index.md"
    text = p.read_text(encoding="utf-8")
    m = re.search(r"## Seiten \((\d+)\)\n\n(.*?)(?=\n## )", text, re.S)
    if not m:
        print("Index-Struktur nicht erkannt, übersprungen")
        return
    count = int(m.group(1))
    lines = [l for l in m.group(2).splitlines() if l.startswith("- [")]
    existing = {re.match(r"- \[([^\]]+)\]", l).group(1) for l in lines}
    from urllib.parse import quote
    for title, fname in new_pages:
        if title not in existing:
            lines.append(f"- [{title}](pages/{quote(fname, safe='')})")
    lines.sort(key=lambda l: re.match(r"- \[([^\]]+)\]", l).group(1).lower())
    new_count = len(lines)
    text = text[: m.start()] + f"## Seiten ({new_count})\n\n" + "\n".join(lines) + text[m.end():]
    if write:
        p.write_text(text, encoding="utf-8")
    print(f"index.md: {count} -> {new_count} Seiten")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", type=Path, default=DEFAULT_WIKI)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    entries = parse_list()
    topics = load_topics()
    assigned = [t for spec in PAGES for t in spec["entries"]]
    missing = sorted(set(entries) - set(assigned))
    extra = sorted(set(assigned) - set(entries))
    dupes = sorted({x for x in assigned if assigned.count(x) > 1})
    if missing:
        raise SystemExit(f"Nicht zugeordnete Einträge: {missing}")
    if extra:
        raise SystemExit(f"Unbekannte Einträge im Mapping: {extra}")
    if dupes:
        raise SystemExit(f"Doppelt zugeordnet: {dupes}")

    new_pages = []
    for spec in PAGES:
        is_new = spec.get("new") and not (args.wiki / "pages" / f"{spec['page']}.md").exists()
        if is_new:
            new_pages.append((spec["title"], f"{spec['page']}.md"))
        upsert_page(args.wiki, spec, entries, topics, args.write)
    update_index(args.wiki, new_pages, args.write)
    print(f"\n{len(PAGES)} Zielseiten, {len(new_pages)} neu, {len(entries)} Einträge zugeordnet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
