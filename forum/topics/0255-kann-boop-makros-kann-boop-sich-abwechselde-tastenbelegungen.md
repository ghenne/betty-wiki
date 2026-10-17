---
title: "Kann Boop Makros? Kann Boop sich abwechselde Tastenbelegungen?"
topic_id: 255
board: "Software"
board_id: 6
posts: 4
first_post: "31. Jan 2011, 10:49"
last_post: "19. Okt 2012, 22:44"
authors: ["RandD", "Telekatz", "eazee", "teufel2k"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=255.0"
---

# Kann Boop Makros? Kann Boop sich abwechselde Tastenbelegungen?

[← Software](../boards/06-software.md) · Thema 255 · 4 Beiträge · 31. Jan 2011, 10:49 – 19. Okt 2012, 22:44

Beteiligt: RandD, Telekatz, eazee, teufel2k

---

<a id="msg1840"></a>

## 1. teufel2k · 31. Jan 2011, 10:49

Hallo ihrs,

seit gestern habe ich endlich Boop drauf und es stellen sich mir gerade zwei Fragen:

1)
Kann ich mit Boop Tasten als Makros definieren? Z.B. mit der Einschalttaste 3 Codes lossenden, eines zum Fernseher einschalten, eines zum Receiver und eines zum Verstärker?

2)
Meine Fernebdienung vom "Humax S HD 3" ist scheinbar so intelligent, dass es beim Prog+ und Prog- zwischen zwei Codes immer hin und her wechselt. Wenn ich also meine Boop mit der Taste anlerne, dann funktioniert die Taste ein mal und danach nicht mehr. Wenn ich jetzt die Originalfernbedienung benutze, dann funktioniert sie genau einmal nicht und dann, beim nächsten tastendruck schaltet sie einmal hoch, daraufhin funktioniert auch die Boop wieder einmal.
Ich habe die Prog+ Taste einfachmal testweise auf zwei Boop tasten angelernt, abwechselnd funktionieren diese Tasten super.

Kann ich das irgendwie abbilden? Oder muss ich mich tiefer mit der Boop  programmierung auseinandersetzen?

Danke für euere Hilfe,
teufel2k

[Permalink](http://bettyhacks.com/forum/index.php?topic=255.msg1840#msg1840)

---

<a id="msg1841"></a>

## 2. RandD · 31. Jan 2011, 16:45

@teufel2k

ich bin auch neu auf die Betty umgestiegen und habe mir auch schon die gleiche Frage gestellt: Also ob Makros unterstützt werden.

Soweit ich die Programmierung eingesehen habe scheint das allerdings nicht der Fall zu sein.

Ich bin grade noch dabei die toolchain einzurichten...

[Permalink](http://bettyhacks.com/forum/index.php?topic=255.msg1841#msg1841)

---

<a id="msg1844"></a>

## 3. Telekatz · 31. Jan 2011, 21:21

zu 1)
Nein, kann man aktuell nicht.

zu 2)
Das liegt daran, dass die Anlernfunktion keine Togglebits unterstützt, deine Humax aber ein sich änderndes Togglebit erwartet und desshalb nicht darauf reagiert.  Hatte das gleiche Problem mit meiner Kathrein UFS922. Hab dann als "Lösung" den LIRC Encoder eingebaut und den dafür verwendet.

[Permalink](http://bettyhacks.com/forum/index.php?topic=255.msg1844#msg1844)

---

<a id="msg2051"></a>

## 4. eazee · 19. Okt 2012, 22:44

Muss den thread nochmal hochholen, sorry 

Ich möchte gerne, dass wenn ich die XBox oder die DBox2 anschalte, der TV gleich mit angeht. Deswegen das Hochholen des Makro-Threads.....

Ich blick bei den ganzen devices und tabs noch nicht ganz ducrch, aber ich denke ea wäre am einfachsten, dass in die main zu implementieren bei "keay_pressed"

Kann mir bitte jemand einen Tip geben oder sogar die Lösung verraten? Die Codes für die Aus- bzw. Einschalttaste sind alle schon im lirc-Modul enthalten.

Btw.: ich hasse arrays....

[Permalink](http://bettyhacks.com/forum/index.php?topic=255.msg2051#msg2051)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
