---
title: "Toggle-Bit RC-5 Encoder (Generic TV) in boop"
topic_id: 156
board: "Software"
board_id: 6
posts: 5
first_post: "19. Aug 2008, 21:13"
last_post: "21. Aug 2008, 15:50"
authors: ["Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=156.0"
---

# Toggle-Bit RC-5 Encoder (Generic TV) in boop

[← Software](../boards/06-software.md) · Thema 156 · 5 Beiträge · 19. Aug 2008, 21:13 – 21. Aug 2008, 15:50

Beteiligt: Telekatz, eme

---

<a id="msg1086"></a>

## 1. eme · 19. Aug 2008, 21:13

Hallo,

kann es sein, daß das Toggle-Bit beim RC5 Encoder (Generic TV) nicht richtig behandelt wird?
Laut [http://www.sbprojects.com/knowledge/ir/rc5.htm](https://web.archive.org/web/2012/http://www.sbprojects.com/knowledge/ir/rc5.htm) wechselt es bei jedem echten Tastendruck, nicht bei den Wiederholungen bei gedrückter Taste.

Ich habe einen RC5-Dekoder, der bei gedrückter Betty-Taste ein wechselndes Toggle-Bit ausgibt.

Leider habe ich noch nicht die Zeit gefunden, mich in den boop-code einzuarbeiten, sonst würde ich selber mal nachsehen... :-(

PS:
Ich glaube, der Code wird generell zweimal hintereinander ausgegeben, da ist das Toggle-Bit anscheinend in Ordnung.
Vielleicht wird der Encoder von einer Tastatur-Routine regelmäßig neu gestartet?

*Last Edit : 19. Aug 2008, 21:18 by eme*

[Permalink](http://bettyhacks.com/forum/index.php?topic=156.msg1086#msg1086)

---

<a id="msg1087"></a>

## 2. Telekatz · 20. Aug 2008, 11:11

> **Zitat**
>
> PS:
> Ich glaube, der Code wird generell zweimal hintereinander ausgegeben, da ist das Toggle-Bit anscheinend in Ordnung.
> Vielleicht wird der Encoder von einer Tastatur-Routine regelmäßig neu gestartet?

So ist es. Bei länger gedrückt gehaltener Taste simuliert der keyscanner einzelne kurze Tastendrücke, die das toggeln verursachen.

Für den RCA_decoder habe ich desshalb kürzlich eine Funktion eingebaut, um diese Wiederholfunktion auszuschalten.

`sysInfo |= 0x20;`
Schaltet die Wiederholfunktion aus. Einzufügen in RC5_Send()

`sysInfo &= ~0x20;`
Schaltet die Wiederholfunktion wieder an. Einzufügen in RC5_Stop()

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=156.msg1087#msg1087)

---

<a id="msg1088"></a>

## 3. eme · 20. Aug 2008, 14:20

Also hast du dem keyscanner selbst quasi einen toggle-status hinzugefügt?
Leider leider werde ich weiterhin keine Gelegenheit haben, mich näher mit C, ARM, und boop zu beschäftigten, so dass ich das mal einpflegen könnte. Ich brauche das aber auch gar nicht, ist mir nur aufgefallen.

mfg

[Permalink](http://bettyhacks.com/forum/index.php?topic=156.msg1088#msg1088)

---

<a id="msg1089"></a>

## 4. eme · 20. Aug 2008, 16:32

Es sind anscheinend auch 0 (0x00) und -/-- (0x0A) vertauscht!

[Permalink](http://bettyhacks.com/forum/index.php?topic=156.msg1089#msg1089)

---

<a id="msg1090"></a>

## 5. eme · 21. Aug 2008, 15:50

anbei eine korrigierte \boop\infrared\ir_codes\rc5\tv

bei einem code war noch ein höherwertiges bit gesetzt, ich weiss nicht, ob das ein fehler ist.

[Permalink](http://bettyhacks.com/forum/index.php?topic=156.msg1090#msg1090)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
