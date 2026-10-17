---
title: "BMP-Logodateien Betty-Tauglich machen - neues tool"
topic_id: 179
board: "Software"
board_id: 6
posts: 13
first_post: "12. Jan 2009, 21:34"
last_post: "20. Mai 2010, 13:44"
authors: ["DJTouch", "El_Barto", "JimBeam", "LeoTheLoewe", "Telekatz", "asgard", "bustler", "damaltor", "theborg"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=179.0"
---

# BMP-Logodateien Betty-Tauglich machen - neues tool

[← Software](../boards/06-software.md) · Thema 179 · 13 Beiträge · 12. Jan 2009, 21:34 – 20. Mai 2010, 13:44

Beteiligt: DJTouch, El_Barto, JimBeam, LeoTheLoewe, Telekatz, asgard, bustler, damaltor …

---

<a id="msg1216"></a>

## 1. damaltor · 12. Jan 2009, 21:34

Moin,

Ich habe im SVN ein neues tool eingecheckt. der neue snapshot von boop enthält ein unterverzeichnis "bmp2b", da drin ist ein tool was (nach dem compilieren) eine bmp-datei welche genau 128x160 pixel hat und im 24bit-farbraum ist (!) in eine datei umformt, welche direkt nach gui/boop_logo kopiert werden kann. neu kompilieren, und schon ist das logo neu.

BITTE BEACHTET DIE READMEDATEI, sie enthält wichtige hinweise zum compilen und zu den voraussetzungen, die das originalbild erfüllen muss.

viel spaß damit...

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1216#msg1216)

---

<a id="msg1272"></a>

## 2. bustler · 26. Jan 2009, 10:32

Das bringt mich auf eine idee:
wärs möglich abhängig von den tasten a-d ein separates logo anzuzeigen, welches zb. ein geräte-logo oder
beispielsweise auch eine spezielle tastenbelegung des aktuellen gerätes anzeigt?

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1272#msg1272)

---

<a id="msg1273"></a>

## 3. El_Barto · 26. Jan 2009, 12:44

Sollte einfach umzusetzen sein. Die Funkt. drawmainscreen(void) müsste um einen Parameter (z.B. einen Pointer auf die Bildadresse) erweitert werden. Dann kannst du in der drawmainscreen mit einem If-Branch zwischen den verschiedenen Logos umschalten. DrawLogo müsste dann auch um deo o.g. Pointer erweitert werden und voila...

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1273#msg1273)

---

<a id="msg1317"></a>

## 4. DJTouch · 24. Feb 2009, 16:23

Hallo zusammen!
Kennt jemand eine Möglichkeit, dasselbe auch unter Windows zu machen?

Habe keine so große Lust, wegen einem Bild extra eine Linux Distribution zu installieren. Aber wenns sein muss, muss es halt sein

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1317#msg1317)

---

<a id="msg1318"></a>

## 5. asgard · 24. Feb 2009, 17:49

> **Zitat von: DJTouch am 24. Feb 2009, 16:23**
>
> Hallo zusammen!
> Kennt jemand eine Möglichkeit, dasselbe auch unter Windows zu machen?
>
> Habe keine so große Lust, wegen einem Bild extra eine Linux Distribution zu installieren. Aber wenns sein muss, muss es halt sein 

nehm halt ne vmware oder virtualbox... dann ist es auch unter windows

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1318#msg1318)

---

<a id="msg1319"></a>

## 6. theborg · 24. Feb 2009, 18:39

kannst auch cgywin nehmen sollte gehen damit

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1319#msg1319)

---

<a id="msg1320"></a>

## 7. JimBeam · 24. Feb 2009, 21:46

Hab's mal als Konsolen-App für Windows compiliert

Sourcen sind leicht modifiziert um farbige Vorlagen besser zu konvertieren:
Die Berechnung der Helligkeit war im Original

```
Y=(R+G+B)/3
```

also alle drei Farbkomponenten gehen zu gleichen Teilen ins Resultat ein - das ist ungünstig, da z.B. Grün viel heller erscheint als Blau. In der Fernsehtechnik wird folgende Berechnung durchgeführt:

```
Y=0.3*R + 0.59*G + 0.11*B
```

somit geht Grün am stärksten und Blau am wenigsten in die Helligkeit ein.
Außerdem habe ich ein paar "kosmetische" Änderungen vorgenommen, damit BORLAND C++5.5 das frisst...

JimBeam

Anhang: ZIP mit geänderten sourcen und EXE

*Last Edit : 24. Feb 2009, 21:49 by JimBeam*

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1320#msg1320)

---

<a id="msg1321"></a>

## 8. DJTouch · 25. Feb 2009, 14:07

@JimBeam:

Super, Danke!

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1321#msg1321)

---

<a id="msg1651"></a>

## 9. LeoTheLoewe · 17. Mai 2010, 08:12

Hallo liebe Betty-Gemeinde,
ich habe gestern Abend (heute Früh) ein neues Feature eingecheckt.

Icons (kleine [gern auch größere] Bitmaps)

Dazu habe ich im Test Stuff einen neuen Demo-Dialog hinzugefügt.
Oft benötigt man weniger Bytes für ein kleines Icon als für den Code,
das ganze mit der Grafikbibliothek zu zeichnen.

Icons werden in 4 Formaten unterstützt:
 - Monochrom  (1 Bit per Pixel)
 - 4 Graustufen (2 Bit per Pixel)
 - Monochrom mit Transparenz  (2 Bit per Pixel)
 - 4 Graustufen mit Transparenz (3 Bit per Pixel)
Meistens wird man die Transparenz nicht brauchen, wenn man mit DRAW_PUT
auf weißen Untergrund zeichnet.
Der Unterschied (Vorteil) von Tranzparenz auf gerauem Untergrund ist in dem Dialog
mit der Eieruhr demonstriert.

Für das ganze habe ich auch ein neues Tool mit eingecheckt.
Es läuft nur auf Windows (XP und Win7 getestet) - Sorry liebe Linux-Gemeinde,
ich verwende die MFC.

display/GrayScaler.exe

konvertiert interaktiv BMP und JPEG Bilder in die genannten Formate und
erstellt ein File, das man in das C Programm includiern muß.
Wie das ganze verwendet wird erkennt man in dem Demo-Code am besten.

Das Datenformat ist auch kompatibel zum betty-logo.
Bei der Gelegenheit habe ich das Logo neu konvertiert. Es hat jetzt Graustufen,
die dem Original viel ähnlicher sind.

<sub>

"Menschen nehmen nur dann die klügste Lösung, wenn alle anderen Möglichkeiten ausgeschöpft sind."
Harald L.

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1651#msg1651)

---

<a id="msg1652"></a>

## 10. Telekatz · 18. Mai 2010, 11:00

Hallo LeoTheLoewe,

hab mir mal deinen Code angeschaut:

icon.h
`///////////////////////////////////////////////////////////////////
// ICON can be defined in the appropriate C file before
// including that header or the related icon files to define the
// actual type of the icon structure:
//
// >> #define ICON   iconElement_t
//
///////////////////////////////////////////////////////////////////
#ifndef ICON
#define ICON   icon_t
#endif

///////////////////////////////////////////////////////////////////
// ICON_INFO can be defined in the appropriate C file before
// including that header to save one byte in the icon structure:
//
// >> #define ICON_INFO(i)
//
///////////////////////////////////////////////////////////////////
#ifndef ICON_INFO
#define ICON_INFO(i)        /* info    = */ i,
#define ICON_INFO_ELEMENT   unsigned char info;   // additional one byte (iconType_t might be larger)
#endif

#ifndef ICON_INFO_ELEMENT
#define ICON_INFO_ELEMENT
//#define ICON_IS_GRAY(i)   0
#define ICON_IS_GRAY(i) (sizeof(i.data) > (i.height/8 + (i.height%8 ? 1 : 0)) * i.width + 2);
#else
#define ICON_IS_GRAY(i)   ((i)->info >= ICON_GRAY)
#endif`

testmenu.c
`//-----------------------------------------------------------------------------
#undef  ICON_INFO
#define ICON_INFO(i)

#undef  ICON_INFO_ELEMENT
#define ICON_INFO_ELEMENT

#undef  ICON
#define ICON   iconElement_t

#include "iconFr.h"
#include "iconPlay.h"
#include "iconPause.h"
#include "iconStop.h"
#include "iconFf.h"`

Ist das nicht irgendwie viel zu kompliziert gedacht, mit den vielen defines zwei verschiedene Icon Structs zu definieren, nur um eventuell ein Byte in der Struct zu sparen? Das macht den Code nicht gerade übersichtlich.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1652#msg1652)

---

<a id="msg1653"></a>

## 11. LeoTheLoewe · 18. Mai 2010, 21:45

Naja, da hast Du völlig recht, ich bin nun mal ein sparsamer Mensch und
wollte für den sehr häufigen Fall, das die Icons in ein Array kommen, auf das man anaschließend indiziert zugreift (siehe Test Dialog, die kleinen Bildchen und die könnte man ja auch noch 1bpp
machen, dann sind sie nur noch halb so groß) so sparsam wie möglich sein.
Ansonsten hätte mir wieder ein Anderer vorgeworfen, das gerade bei so winzigen Icons das
Verhältnis von Header zu Nutzdaten beschämend ist.
Naja und eigentlich finde ich es zwar aufwendig aber nicht unübersichtlich.
So ein Macro kostet nix und erklärt sich mit seinem Namen einigermaßen.

<sub>

"Menschen nehmen nur dann die klügste Lösung, wenn alle anderen Möglichkeiten ausgeschöpft sind."
Harald L.

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1653#msg1653)

---

<a id="msg1654"></a>

## 12. Telekatz · 19. Mai 2010, 11:14

Die zwei verschiedenen Structs kann man ja beibehalten. Allerdings weiß man ja bereits von vornherein, ob man ein Icon vom Typ icon_t oder iconElement_t verwenden möchte. Und da macht es bezüglich der Übersichtlichkeit des Codes keinen Sinn, den Typ mit einem Makro zu definieren. In der entsprechenden .h Icondatei ist es nicht ersichtlich, welchen Typ das Icon denn hat.

Das du sparsam mit den Ressourcen umgehen möchtest, dagegen ist ja nicht einzuwenden. Allerdings hat dir hier der Compiler beim Testdialog einen Strich durch die Rechnung gemacht.
Bei einem dieser Bilder vom Typ iconElement_t währe die theoretische Größe der Struct 54 Bytes. Da die Structs allerdings immer auf einer Adresse eines vielfachen von 32Bit abgelegt werden, ist die tatsächliche Größe aufgrund von Füllbytes 56Bytes. Ein icon_t währe hier auch nicht größer.

Da zudem der Aufruf für ein iconElement_t
`drawIconExt (ix, LCD_SIZE_Y-1 - h,
         iconList [i]->data,
         iconList [i]->width, iconList [i]->height, ICON_GRAY,
         LCD_COLOR_B, DRAW_NORCU);`
aufgrund von mehr übergebenen Parametern länger ist als der entsprechende icon_t Aufruf
`drawIcon (ix, LCD_SIZE_Y-1 - h, iconList [i], LCD_COLOR_B, DRAW_NORCU);`
wird der Code im Endeffekt um 12 Bytes größer.

Wohlgemerkt, in diesem speziellen Fall. Wären die Bilder nur 1bpp bei gleichen Abmessungen,  sähe die Sache wieder anders aus.

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1654#msg1654)

---

<a id="msg1655"></a>

## 13. LeoTheLoewe · 20. Mai 2010, 13:44

Das Icon Header File wird ja vom GrayScaler generiert und
eigentlich wollte ich mich zu diesem Zeitpunkt noch nicht festlegen,
ob das Icon später in einem Array verwendet wird oder "standallone".
Das Problem mit den Allignments ist in der Tat ärgerlich.
Dann müßte ich wohl versuchen, das ganze Array zu generiern und damit das
Padding verhindern, denn es sind ja alles Characters.
Damit spart man sich dann auch noch das Array der Icon-Pointer.

Wichtig ist mir, das zwar die Icons im Array den gleichen Typ haben müssen, aber durchaus
verschiedene Größen haben dürfen.

Das muß man vielleich mal ein bischen probieren.

Wem der Typ iconElement_t nicht gefällt, der kann ihn ja auch einfach ignorieren,
wenn man nix tut und einfach das Icon Header-File includiert benutzt automatisch icon_t,
so wie man das auch im Testdialog sieht. Man muß ja nur etwas tun, wenn man ausdrücklich
das eine Byte versucht zu sparen.

Appropos: Man denke sich ein Array von 8 Icons mit 8x8 Größe 1bpp so wie die in unserer
Kopfzeile, dann könnte man eines "geschenkt" bekommen, wenn man den Typ nicht jedes mal
mitspeichert.  - vorausgesetzt wir bekommen das nun noch dem Allignment verklickert.

*Last Edit : 20. Mai 2010, 14:16 by LeoTheLoewe*

<sub>

"Menschen nehmen nur dann die klügste Lösung, wenn alle anderen Möglichkeiten ausgeschöpft sind."
Harald L.

</sub>

[Permalink](http://bettyhacks.com/forum/index.php?topic=179.msg1655#msg1655)

---

## Verwandte Themen

- [Logo-Contest](0016-logo-contest.md)
- [Was kann man mit betty alles machen???](0068-was-kann-man-mit-betty-alles-machen.md)

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
