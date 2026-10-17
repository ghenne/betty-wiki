---
title: "LPC2220 Pin-Belegung"
topic_id: 140
board: "Hardware"
board_id: 5
posts: 6
first_post: "16. April 2008, 20:00"
last_post: "13. Mai 2008, 20:28"
authors: ["Gentoo07", "famos", "pcsquirrel"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=140.0"
---

# LPC2220 Pin-Belegung

[← Hardware](../boards/05-hardware.md) · Thema 140 · 6 Beiträge · 16. April 2008, 20:00 – 13. Mai 2008, 20:28

Beteiligt: Gentoo07, famos, pcsquirrel

---

<a id="msg981"></a>

## 1. pcsquirrel · 16. April 2008, 20:00

Hallo,

Anregungen, Fehlerkorrekturen und sonstiges bzgl.
[http://www.bettyhacks.com/wiki/index.php/LPC2220_Pin-Belegung](../../pages/LPC2220%20Pin-Belegung.md)

bitte hier diskutieren.

Ich erzeuge diese Tabelle aus einem XML File und kann Änderungswünsche gerne einarbeiten.

Weiß jemand, ob dir Anbindung vom Display und Flash so richtig ist, werden die BLs (BLs[3:0] Output Low-active Byte Lane Select signals.) Signale verwendet? Ich bin da noch nicht genz durchgestiegen.

Danke
pcsquirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=140.msg981#msg981)

---

<a id="msg983"></a>

## 2. famos · 18. April 2008, 20:49

Prima, vielen Dank pcsquirrel!

Dokumentation der Hardware und Software ist sicher einer der nächsten nötigen Schritte.
Habe gerade ein paar Sunden verbraten um rauszufinden wie das Einlesen der Tasten geht. Die vielen Maskier und Schift Operationen sind nicht so leicht zu durchschauen.

Bezüglich Deiner Tabelle hätte ich noch einen Vorschlag: Eine weiter Spalte mit dem Hinweis ob Output oder Input wäre auch noch informativ.

Ich schliesse mit dem Aufruf: Jetzt ran an die Doku!

famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=140.msg983#msg983)

---

<a id="msg1014"></a>

## 3. Gentoo07 · 01. Mai 2008, 17:55

-P0.01 hat falsche Beschreibung TxD
-P0.14 könnte noch die Beschrebung "Bootloader Enable" bekommen
-ich fände es gut die Bezeichnung "EN29LV800" vom Flash aus der Ziel-Spalte zu entfernen, da die Tabelle dadurch erheblich schlanker und übersichtlicher wird.

Aber davon abgesehen ist es super wie du die Tabelle verwaltet und bisher schon erweitert hast, Respekt!

[Permalink](http://bettyhacks.com/forum/index.php?topic=140.msg1014#msg1014)

---

<a id="msg1015"></a>

## 4. pcsquirrel · 01. Mai 2008, 19:13

@ famos:

Die Anregung bzgl. I/O hab ich aufgenommen und werd ich einarbeiten - hast du eine Aufstellung für die Tastaturmatrix?

@Gentoo07

Danke für die Korrekturvorschläge - sind schon eingearbeitet. Wegen der Spaltenbreite würde ich ehe vorschlagen die Spalte "Funktion" in einzelne Zeilen zu zerlegen und so Breite zu sparen.

Und natürlich an euch beide: Danke für die Blumen.

p.c.squirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=140.msg1015#msg1015)

---

<a id="msg1017"></a>

## 5. pcsquirrel · 03. Mai 2008, 11:52

@famos

So die I/O sind eingefügt. Bitte sepziell bei den Tasten mal kontrollieren.

Danke
 
p.c.squirrel

[Permalink](http://bettyhacks.com/forum/index.php?topic=140.msg1017#msg1017)

---

<a id="msg1024"></a>

## 6. famos · 13. Mai 2008, 20:28

> **Zitat**
>
> Zitat einfügen
> @ famos:
>
> Die Anregung bzgl. I/O hab ich aufgenommen und werd ich einarbeiten - hast du eine Aufstellung für die Tastaturmatrix?
>
>
> @Gentoo07
>
> Danke für die Korrekturvorschläge - sind schon eingearbeitet. Wegen der Spaltenbreite würde ich ehe vorschlagen die Spalte "Funktion" in einzelne Zeilen zu zerlegen und so Breite zu sparen.
>
> Und natürlich an euch beide: Danke für die Blumen.
>
> p.c.squirrel

Hier die Tastatur Matrix (ist im Wiki zu finden). Werde bei Gelegenheit mal ein Schema des Tastaturteils und eine Beschreibung der Tastaturroutine posten.
Scansignal ist auf P2.18..P2.24 gelesen wird P0.x und P3.x.

![](https://web.archive.org/web/2012/http://www.bettyhacks.com/wiki/images/a/af/Matrix_DE_Betty.jpg)
[http://bettyhacks.com/forum/index.php?action=dlattach;topic=128.0;attach=46](https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?action=dlattach;topic=128.0;attach=46)

Gruss famos

[Permalink](http://bettyhacks.com/forum/index.php?topic=140.msg1024#msg1024)

---

[← Zurück zu Hardware](../boards/05-hardware.md) · [Gesamtindex](../index.md)
