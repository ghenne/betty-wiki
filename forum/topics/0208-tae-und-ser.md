---
title: "TAE und SER"
topic_id: 208
board: "Hardware"
board_id: 5
posts: 1
first_post: "08. Mai 2009, 19:03"
last_post: "08. Mai 2009, 19:03"
authors: ["gerdi"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=208.0"
---

# TAE und SER

[← Hardware](../boards/05-hardware.md) · Thema 208 · 1 Beiträge · 08. Mai 2009, 19:03 – 08. Mai 2009, 19:03

Beteiligt: gerdi

---

<a id="msg1416"></a>

## 1. gerdi · 08. Mai 2009, 19:03

Zu meinem grossen Erstaunen habe ich festgestellt, dass VOIP in Linux (und Win) schon sehr gut erschlossen ist.

Ich habe gerade in Lenny einen sehr kompakten VOIP-Server heruntergeladen (ser).
Dieses packages gibt es sogar als optware für den wl500gp!!! (Und auch openSer resp. opensipp).

Der Server lief gleich.

Dazu gibt es Perl-Skripte von CPAN für VOIP-Clients. (Net-Sip).

Der Server meldete "Success!" bei der Anmeldung meines VOIP-Adapters. (Das heisst nicht, dass es zu einer Telefon-Verbindung kam, sondern nur, dass der Server und der Adapter bereit sind Telefon-Verbindungen entgegen zu nehmen. Die Authentifikation [Telefonnummer und Passwort] habe ich ausgeschaltet.)
Der Voip-Client lief zum Test das Programm "listening.pl".
(Leider waren beide Programme sehr wortkarg. Vielleicht habe ich etwas falsch konfiguriert.)

Es bleibt also nur eines:
Den TAE so zu programmieren, dass der Voip-Client auf der anderen Seite im Testprogramm "listening.pl" die Tasteninformationen der Betty ausgibt und umgekehrt durch das Testprogramm "call.pl" Informationen an die Betty schickt.

Ist jemand bereit mir bei der Programmierung des TAE zu helfen, so dass dieses sehr einfache Problem gelöst ist?

(Mit einem Linmodem bekomme ich Echo vom TAE in einem seriellen Terminal. Sicher kann man auf diese Weise Firmware uploaden, wenn einmal eine bessere Firmware vorhanden ist.)

*Last Edit : 09. Mai 2009, 00:25 by gerdi*

[Permalink](http://bettyhacks.com/forum/index.php?topic=208.msg1416#msg1416)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
