---
title: "undefined reference to 'strncpy'/'strncat'/'strnlen'"
topic_id: 227
board: "Software"
board_id: 6
posts: 4
first_post: "31. Dez 2009, 10:08"
last_post: "31. Dez 2009, 20:02"
authors: ["Telekatz", "asgard"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=227.0"
---

# undefined reference to 'strncpy'/'strncat'/'strnlen'

[← Software](../boards/06-software.md) · Thema 227 · 4 Beiträge · 31. Dez 2009, 10:08 – 31. Dez 2009, 20:02

Beteiligt: Telekatz, asgard

---

<a id="msg1555"></a>

## 1. asgard · 31. Dez 2009, 10:08

Hi,

irgendwie kann ich die Befehle 'strncpy'/'strncat'/'strnlen' nicht nutzen.

`` testmenu.c:(.text+0xff4): undefined reference to `strncpy'
testmenu.c:(.text+0x1018): undefined reference to `strncat'
testmenu.c:(.text+0x1046): undefined reference to `strnlen' ``

Die String.h hab ich auch eingebunden (#include "string.h").

Der Code sieht an der Stelle folgendermaßen aus (hab vorher noch nie C-programmiert...daher evtl. total unbrauchbarer/umständlich/falscher Code)....

> **Zitat**
>
> while (strncmp(serial_getc(),".",1)==1)
> {
>    strncpy(replay, serial_getc(), 1);
> }

Ich möchte eigentlich nur meine gesnifften Daten vom Rechner an die Betty schicken (über RS232).
Dort sollen die Daten (0-en und 1-er) so lange gesammelt werden (quasi in der variable replay) bis ein "." kommt.
Der "." signalisiert der Betty das Ende der Daten. Danach soll Sie dann die Daten entsprechende rausfunken.

> **Zitat**
>
>    while(KEY_Exit) {};
>    
>    for (i=1;i=strlen(replay);i++)
>    {
>    strncat(act_char, replay+i, 1);
>       
>       waitus(50); //Daten wurden mit 50µs Abtastung aufgenommen
>       //waitus(50);
>          
>       if(act_char=0)
>       {
>          FIOCLR0 = GDO0;  //Kein Signal wird gesendet - Low
>       } else {
>          FIOSET0 = GDO0;  //Signal wird gesendet - High
>       }

Komischerweise kann ich aber strncmp nutzen....da gibt es keinen Fehler.
Was muss ich denn beachten?
Muss ich die "string.h" ausser in der testmenu.c noch wo anders einbinden?

Viele Grüße, vielen Dank und einen guten Rutsch ins neue Jahr 2010
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=227.msg1555#msg1555)

---

<a id="msg1556"></a>

## 2. Telekatz · 31. Dez 2009, 14:30

Hallo Asgard,

> **Zitat**
>
> Die String.h hab ich auch eingebunden (#include "string.h").

Standardbibliotheken werden nicht mit Anführungszeichen eingebunden. Richtig ist:
#include <string.h>

`while (strncmp(serial_getc(),".",1)==1)
{
   strncpy(replay, serial_getc(), 1);
}`
Du liest hier zwei mal ein Zeichen ein. Das Zeichen, das du auf das Übertragungsende hin überprüfst ist ein anderes als das, was du in replay abspeicherst.

> **Zitat**
>
> Dort sollen die Daten (0-en und 1-er) so lange gesammelt werden (quasi in der variable replay) bis ein "." kommt.

Kommt da (unsigned char) 0 und 1 oder (ASCII) '0' und '1'? Wenn da 0 und 1 kommt wird das mit Stringfunktionen sowieso nicht funktionieren. (wegen der Nullterminierung von Strings)
Versuch das ganze mal ohne Stringfunktionen zu schreiben. Die sind für dieses Problem nicht notwendig.

Gruß
Telekatz

[Permalink](http://bettyhacks.com/forum/index.php?topic=227.msg1556#msg1556)

---

<a id="msg1557"></a>

## 3. asgard · 31. Dez 2009, 16:34

Hi Telekatz,

> **Zitat**
>
> Standardbibliotheken werden nicht mit Anführungszeichen eingebunden. Richtig ist:
> #include <string.h>

das habe ich jetzt probiert, da bekomme ich leider die selben Fehlermeldungen:
 `` testmenu.c:(.text+0xff4): undefined reference to `strncpy'
testmenu.c:(.text+0x1018): undefined reference to `strncat'
testmenu.c:(.text+0x1044): undefined reference to `strlen' ``

> **Zitat**
>
> Kommt da (unsigned char) 0 und 1 oder (ASCII) '0' und '1'? Wenn da 0 und 1 kommt wird das mit Stringfunktionen sowieso nicht funktionieren. (wegen der Nullterminierung von Strings)

du frägst sachen   
ka...ich wollte die Daten einfach als String per rs232 rübersenden...also gehe ich von ASCII aus....

> **Zitat**
>
> Versuch das ganze mal ohne Stringfunktionen zu schreiben. Die sind für dieses Problem nicht notwendig.

Hast du mir da mal nen Tipp...ich hab keine Ahnung wie ich das lösen könnte...

Viele Grüße und vielen Dank für deine Mühe und Zeit!
Asgard

[Permalink](http://bettyhacks.com/forum/index.php?topic=227.msg1557#msg1557)

---

<a id="msg1558"></a>

## 4. Telekatz · 31. Dez 2009, 20:02

> **Zitat**
>
> das habe ich jetzt probiert, da bekomme ich leider die selben Fehlermeldungen:
> Code:
>
> `` testmenu.c:(.text+0xff4): undefined reference to `strncpy'
> testmenu.c:(.text+0x1018): undefined reference to `strncat'
> testmenu.c:(.text+0x1044): undefined reference to `strlen ``'

Die libc.a muss noch im makefile hinzugefügt werden (-lc):
`LIBS = -lgcc -lc`
Wenn GCC jetzt beim kompilieren meckert, dass die libc.a nur hardware FB unterstützt, die libc.a im verzeichnis \WinARM\arm-elf\lib\interwork durch die beiliegende ersetzen.

> **Zitat**
>
> Hast du mir da mal nen Tipp...ich hab keine Ahnung wie ich das lösen könnte...

`for (i=1;i=strlen(replay);i++)`
z.B.:
`i=0;
while(replay[i] != '.') {
  <Irgendwas machen>
  i++;
  }`

`strncat(act_char, replay+i, 1);`
kann ersetzt werden durch
`act_char = replay[i];`

> **Zitat**
>
> ka...ich wollte die Daten einfach als String per rs232 rübersenden...also gehe ich von ASCII aus....

`if(act_char=0)`
Dann muss das eine '0' sein.

[Permalink](http://bettyhacks.com/forum/index.php?topic=227.msg1558#msg1558)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
