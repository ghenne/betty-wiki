# Firmware flashen

## Bettys Bootloader

Betty enthält einen Bootloader, mit dem sich über eine serielle Schnittstelle (3V, nicht RS232) die Firmware ([Boop](Boop.md "Boop")) aufspielen lässt.

Man braucht dazu einen Adapter, der den PC mit der Betty verbindet. Siehe [Interfaces PC zu Betty](Interfaces%20PC%20zu%20Betty.md "Interfaces PC zu Betty")

Man braucht ein Programm, dass die Firmware über diese Adapter überträgt. Siehe [Tools](Tools.md "Tools"). Dort gibt es auch Beispiele, wie die Firmware übertragen wird.

Der Bootloader muss auf der Betty allerdings erst gestartet werden. Das passiert, wenn der eINT1 Pin beim Reset der Betty (Akkus rein, Reset Pin low) auf low liegt (s.u.).

Die Adapter und Programmiersoftware können das teilweise automatisch über zwei Leitungen. Es geht aber auch manuell.

Dieser [Thread](https://github.com/ghenne/betty-forum/blob/main/topics/0104-frage-zum-simple-serial-interface.md) enthält einige Tips zu Interface und Tools.

## Bootloader manuell starten

    EINT PIN auf GND bruecken
    RESET PIN auf GND bruecken
    RESET PIN wieder oeffnen
    EINT PIN wieder oeffnen

Pin-Belegung der Betty hier: [Betty_Hardware](Betty%20Hardware.md "Betty Hardware")

<!-- forum-links:start -->
## Forumsdiskussionen: U-Boot, Update und Flashprobleme

Ergänzungen zum Flashen: U-Boot als alternativer Bootloader, das Mitschneiden des Original-Updates, Probleme nach dem Boop-Flash und das Flashen des SCART-Adapters.

### U-Boot als alternativer Bootloader

- [Das U-Boot - Universal Bootloader](https://github.com/ghenne/betty-forum/blob/main/topics/0032-das-u-boot-universal-bootloader.md) — U-Boot als Universal-Bootloader und Eignung für den LPC2220.

### Firmware-Update mitschneiden

- [Mitschneiden des Updatevorgangs - allgemein](https://github.com/ghenne/betty-forum/blob/main/topics/0007-mitschneiden-des-updatevorgangs-allgemein.md) — Original-Firmware-Update mitschneiden/dumpen.

### Boop-Flashprobleme

- [Probleme beim boop flashen](https://github.com/ghenne/betty-forum/blob/main/topics/0178-probleme-beim-boop-flashen.md) — Probleme beim Boop-Flash.
- [Boop geflasht, nichts geht ?](https://github.com/ghenne/betty-forum/blob/main/topics/0280-boop-geflasht-nichts-geht.md) — Nach dem Boop-Flash startet nichts: typische Ursachen und Abhilfe.

### SCART-Adapter flashen (Fehler und Ablauf)

- [Fehler beim Flashen des SCART-Adapters](https://github.com/ghenne/betty-forum/blob/main/topics/0186-fehler-beim-flashen-des-scart-adapters.md) — Fehler beim Flashen des SCART-Adapters mit BettyHeaven/Kombiinterface.
- [Flashen des Scart Adapters ???  und einen guten Rutsch ins Jahr 2009 !!!](https://github.com/ghenne/betty-forum/blob/main/topics/0176-flashen-des-scart-adapters-und-einen-guten-rutsch-ins-jahr-2.md) — Flashen des SCART-Adapters: Ablauf und Stolperfallen.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

