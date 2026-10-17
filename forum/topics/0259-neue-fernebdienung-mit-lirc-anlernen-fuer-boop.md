---
title: "Neue Fernebdienung mit lirc anlernen für Boop"
topic_id: 259
board: "Software"
board_id: 6
posts: 2
first_post: "15. Feb 2011, 10:10"
last_post: "15. Feb 2011, 12:19"
authors: ["Telekatz", "teufel2k"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=259.0"
---

# Neue Fernebdienung mit lirc anlernen für Boop

[← Software](../boards/06-software.md) · Thema 259 · 2 Beiträge · 15. Feb 2011, 10:10 – 15. Feb 2011, 12:19

Beteiligt: Telekatz, teufel2k

---

<a id="msg1875"></a>

## 1. teufel2k · 15. Feb 2011, 10:10

Hallo,

da meine Fernebdienung für den Humax S HD 3 scheinbar ein Toggle Bit nutzt wollte ich nun die Fernbedienung über den PC per lirc einlesen. Leider finde ich dazu keine wiki-Seite und so wollte ich es auf eigene Faust probieren.

Man soll sich ja beim einlesen per irrecord an den namespace halten (z.B. KEY_3, KEY_4, KEY_5, KEY_RIGHT, KEY_LEFT)
Gibts es dafür schon einen vorgefertigten namespüace für Boop? Oder ist dieser Namespace völlig egal?
Momentan sieht die Datei auch noch völlig anders aus als die im svn repository! Muss ich meine per lirc eingelsene Fernbedienungs configuratioon noch konvertieren?

Merkwürdig ist auch, dass ich eigentlich einen Toggle-Bit benötige aber unter toggle_bit_mask 0x0 steht. Aber vielleicht bedeutet dies auch nix!

Danke für eure Hilfe,
teufel2k

So sieht bisher meine Datei aus:

`begin remote

  name  sky.conf
  bits           16
  flags RC6|CONST_LENGTH
  eps            30
  aeps          100

  header       2761   793
  one           507   380
  zero          507   380
  pre_data_bits   21
  pre_data       0x37FB7
  gap          107081
  toggle_bit_mask 0x0
  rc6_mask    0x100000000

      begin codes
          KEY_VOLUMEDOWN           0xD9EE
          KEY_VOLUMEUP             0xD9EF
          KEY_RIGHT                0xD9A4
          KEY_LEFT                 0x59A5
          KEY_UP                   0xD9A7
          KEY_DOWN                 0xD9A6
          KEY_OK                   0xD9A3
      end codes

end remote`

[Permalink](http://bettyhacks.com/forum/index.php?topic=259.msg1875#msg1875)

---

<a id="msg1876"></a>

## 2. Telekatz · 15. Feb 2011, 12:19

Hallo  teufel2k,

ja, die eingelesene LIRC Datei muss noch in das Format der Betty konvertiert werden. In Boop werden die Daten in einer Struct abgelegt und die Daten aus der LIRC Datei müssen in die entsprechenden Felder der Struct übernommen werden.

Das Protokoll deinem FB ist anscheinend das selbe wie für meine UFS922. Nimm die Datei für die UFS922 als Vorlage und ändere nur pre_data und deine Tastencodes ab.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=259.msg1876#msg1876)

---

## Verwandte Themen

- [Boop: Fernbedienung anlernen](0162-boop-fernbedienung-anlernen.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
