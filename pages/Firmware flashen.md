# Firmware flashen

## Bettys Bootloader

Betty enthält einen Bootloader, mit dem sich über eine serielle Schnittstelle (3V, nicht RS232) die Firmware ([Boop](Boop.md "Boop")) aufspielen lässt.

Man braucht dazu einen Adapter, der den PC mit der Betty verbindet. Siehe [Interfaces PC zu Betty](Interfaces%20PC%20zu%20Betty.md "Interfaces PC zu Betty")

Man braucht ein Programm, dass die Firmware über diese Adapter überträgt. Siehe [Tools](Tools.md "Tools"). Dort gibt es auch Beispiele, wie die Firmware übertragen wird.

Der Bootloader muss auf der Betty allerdings erst gestartet werden. Das passiert, wenn der eINT1 Pin beim Reset der Betty (Akkus rein, Reset Pin low) auf low liegt (s.u.).

Die Adapter und Programmiersoftware können das teilweise automatisch über zwei Leitungen. Es geht aber auch manuell.

Dieser [Thread](http://bettyhacks.com/forum/index.php?topic=104.0) enthält einige Tips zu Interface und Tools.

## Bootloader manuell starten

    EINT PIN auf GND bruecken
    RESET PIN auf GND bruecken
    RESET PIN wieder oeffnen
    EINT PIN wieder oeffnen

Pin-Belegung der Betty hier: [Betty_Hardware](Betty%20Hardware.md "Betty Hardware")

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

