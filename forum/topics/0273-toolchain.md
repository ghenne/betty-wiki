---
title: "Toolchain"
topic_id: 273
board: "Software"
board_id: 6
posts: 7
first_post: "31. Okt 2011, 18:04"
last_post: "16. Apr 2013, 21:41"
authors: ["Josch", "gunnar"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=273.0"
---

# Toolchain

[← Software](../boards/06-software.md) · Thema 273 · 7 Beiträge · 31. Okt 2011, 18:04 – 16. Apr 2013, 21:41

Beteiligt: Josch, gunnar

---

<a id="msg1960"></a>

## 1. Josch · 31. Okt 2011, 18:04

Hallo,

ich versuche jetzt schon seit einiger Zeit, McBetty aus den github-Sourcen zu kompilieren.
Ich habe das Zip-Paeckchen nach C:\Betty\McBetty\github entpackt, WinARM laut Wiki-Beitrag eingerichtet, "Makefile.local" in ....\muc durch die Datei im Wiki ersetzt und damm "make" ausgefuehrt.

Das Ergebnis war nicht das, was ich mir gewuenscht habe:

 `c:\Betty\McBetty\github\muc>make

mkdir -p .deps
mkdir -p cc1100/.deps
mkdir -p display/.deps
mkdir -p display/fonts/.deps
mkdir -p interrupt/.deps
mkdir -p pwm/.deps
mkdir -p keyboard/.deps
mkdir -p kernel/.deps
mkdir -p timer/.deps
mkdir -p mpd/.deps
mkdir -p serial/.deps
c:/WinARM/bin/arm-elf-as -mcpu=arm7tdmi-s -D --gstabs -mthumb-interwork -mfpu=so
ftfpa -o crt.o crt.s
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float
 -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinf
rared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm
 -Impd -O2 -c  -MMD -MF ./.deps/isr.o -o isr.o isr.c
c:/WinARM/bin/arm-elf-as -mcpu=arm7tdmi-s -D --gstabs -mthumb-interwork -mfpu=so
ftfpa -o arm_exc.o arm_exc.s
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float
 -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinf
rared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm
 -Impd -O2 -c  -MMD -MF ./.deps/global.o -o global.o global.c
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float
 -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinf
rared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm
 -Impd -O2 -c  -MMD -MF ./.deps/main.o -o main.o main.c
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float
 -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinf
rared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm
 -Impd -O2 -c  -MMD -MF cc1100/.deps/cc1100.o -o cc1100/cc1100.o cc1100/cc1100.c

cc1100/cc1100.c:56:1: warning: "SMARTRF_SETTING_PKTCTRL0" redefined
In file included from cc1100/cc1100.c:28:
cc1100/smartrf_CC1100.h:74:1: warning: this is the location of the previous defi
nition
cc1100/cc1100.c: In function 'cc1100_read_status_reg_otf':
cc1100/cc1100.c:347: warning: comparison is always false due to limited range of
 data type
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float
 -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinf
rared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm
 -Impd -O2 -c  -MMD -MF cc1100/.deps/rf.o -o cc1100/rf.o cc1100/rf.c
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float
 -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinf
rared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm
 -Impd -O2 -c  -MMD -MF display/.deps/lcd.o -o display/lcd.o display/lcd.c
display/lcd.c: In function 'draw_progressbar':
display/lcd.c:495: warning: comparison is always false due to limited range of d
ata type
display/lcd.c:496: warning: comparison is always false due to limited range of d
ata type
display/lcd.c: In function 'draw_trianglebar':
display/lcd.c:537: warning: comparison is always false due to limited range of d
ata type
c:/WinARM/bin/arm-elf-gcc -mcpu=arm7tdmi-s -Wall -mthumb-interwork -msoft-float
 -Ic:/WinARM/include -I. -Iinterrupt -Idisplay -Ikeyboard -Ikernel -Iaudio -Iinf
rared -Iserial -Iflash -Icc1100 -Igui -Itimer -Igames -Iadc -Irtc  -Itools -Ipwm
 -Impd -O2 -c  -MMD -MF display/.deps/fonty.o -o display/fonty.o display/fonty.c

In file included from display/fonty.c:27:
display/fonts/pearl_font.h:166: error: expected '=', ',', ';', 'asm' or '__attri
bute__' before 'pearl_font_cpos'
In file included from display/fonty.c:28:
display/fonts/smooth_font.h:215: error: expected '=', ',', ';', 'asm' or '__attr
ibute__' before 'smooth_font_cpos'
In file included from display/fonty.c:29:
display/fonts/misc_font.h:215: error: expected '=', ',', ';', 'asm' or '__attrib
ute__' before 'misc_font_cpos'
display/fonty.c: In function 'set_font':
display/fonty.c:66: error: 'misc_font_cpos' undeclared (first use in this functi
on)
display/fonty.c:66: error: (Each undeclared identifier is reported only once
display/fonty.c:66: error: for each function it appears in.)
display/fonty.c:77: error: 'smooth_font_cpos' undeclared (first use in this func
tion)
display/fonty.c:90: error: 'pearl_font_cpos' undeclared (first use in this funct
ion)
make: *** [display/fonty.o] Error 1`

Meine Linuxversuche sahen auch nicht besser aus.

Was mache ich denn falsch? so schwer kann das doch garnicht sein.

[Permalink](http://bettyhacks.com/forum/index.php?topic=273.msg1960#msg1960)

---

<a id="msg1961"></a>

## 2. gunnar · 02. Nov 2011, 10:47

Hallo Josch,

welche Toolchain hast Du denn genommen?

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=273.msg1961#msg1961)

---

<a id="msg1962"></a>

## 3. Josch · 02. Nov 2011, 11:41

Hallo Gunnar,

obige Fehlermeldung habe ich mit WinARM (20060606) generiert. Brauche ich ausserdem noch etwas?

Meine Linuxversuche habe ich mit der aktuellen "Sourcery CodeBench Lite Edition" gestartet. Da Linux nicht so ganz meine Welt ist, kann es sein, dass ich da was entscheidendes uebersehen habe.

(Mir wuerden im Moment ja auch die aktuellen Binaries reichen.)

Guss,

  Joh

[Permalink](http://bettyhacks.com/forum/index.php?topic=273.msg1962#msg1962)

---

<a id="msg1963"></a>

## 4. gunnar · 03. Nov 2011, 08:46

Hallo Josh,

ich habe auf meinem System (Linux) auch die Codesourcery Version der Toolchain. Die Versionsnummer ist 4.5.2.
[https://sourcery.mentor.com/sgpp/lite/arm/portal/package8744/public/arm-uclinuxeabi/arm-2011.03-46-arm-uclinuxeabi-i686-pc-linux-gnu.tar.bz2](https://web.archive.org/web/2012/https://sourcery.mentor.com/sgpp/lite/arm/portal/package8744/public/arm-uclinuxeabi/arm-2011.03-46-arm-uclinuxeabi-i686-pc-linux-gnu.tar.bz2)
Entpackt als /opt/arm-uclinuxeabi-codesourcery-gcc
Damit es baut musste ich die Makefiles etwas anpassen, damit die libc.a gelinkt wird. Ohne die Libc kommt es zu nicht aufgelösten Verweisen auf memcpy. Der Patch hängt an.
Das kompilierte bin File habe ich auch angehangen, probier mal ob es läuft.

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=273.msg1963#msg1963)

---

<a id="msg1964"></a>

## 5. Josch · 04. Nov 2011, 01:22

Hallo Gunnar,

Linux ist echt nicht meine Welt. Kann sich ja noch mal aendern, aber im Moment ist meine Frustrationsgrenze weit ueberschritten. Ich bin wohl ay#uch zu dusselig zum patchen.

Kannst Du mich bitte auch noch mit dem bin-File versorgen, das ich brauche, um den Scart-Apapter per Betty zu flashen?
Kompilieren kaoennte ich dann ja mal ueben, waehrend ich Musik per McBetty hoere. Geht dann bestimmt besser   .

Danke uebrigens fuer Deine Muehen.

 Gruss
  Joh

[Permalink](http://bettyhacks.com/forum/index.php?topic=273.msg1964#msg1964)

---

<a id="msg1966"></a>

## 6. gunnar · 07. Nov 2011, 12:26

Hallo Josh,

ich habe Dir hier ein boop kompiliert, mit dem Du den Scart Adapter flashen kannst. Dazu musste ich allerdings die ronetix newlib 4.1.1 Toolchain, die im Boop Wiki verlinkt ist, nehmen. Mit der Code-Sourcery 4.5.2 Toolchain flackerte beim Start nur kurz die Hintergrundbeleuchtung auf und dann bleibt der Screen leer.

Viel Spaß mit McBetty,

Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=273.msg1966#msg1966)

---

<a id="msg2118"></a>

## 7. gunnar · 16. Apr 2013, 21:41

Hallo,

ich habe die aktuelle summon Toolchain mit dem GCC 4.7.3 vom Linaro Projekt gebaut. Das Build Script gibt es hier:
[https://github.com/esden/summon-arm-toolchain](https://web.archive.org/web/2012/https://github.com/esden/summon-arm-toolchain)
Ich habe kleine Änderungen für diese Toolchain gemacht, u.A. auch das Alignment fest auf 4 Bytes eingestellt.

Jetzt kommen die Warnungen nicht mehr und das Binary läuft. :-)

Viele Grüße
Gunnar

[Permalink](http://bettyhacks.com/forum/index.php?topic=273.msg2118#msg2118)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
