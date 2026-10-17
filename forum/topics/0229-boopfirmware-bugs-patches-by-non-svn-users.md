---
title: "boopfirmware: bugs/patches by non svn users"
topic_id: 229
board: "Software"
board_id: 6
posts: 7
first_post: "31. Jan 2010, 11:05"
last_post: "07. Feb 2011, 17:45"
authors: ["Boregard", "Telekatz", "eme"]
source: "https://web.archive.org/web/2012/http://bettyhacks.com/forum/index.php?topic=229.0"
---

# boopfirmware: bugs/patches by non svn users

[← Software](../boards/06-software.md) · Thema 229 · 7 Beiträge · 31. Jan 2010, 11:05 – 07. Feb 2011, 17:45

Beteiligt: Boregard, Telekatz, eme

---

<a id="msg1570"></a>

## 1. eme · 31. Jan 2010, 11:05

Auf diesem Weg die Korrektur eines Fehlers:

`boopfirmware/boop/trunk/infrared$ svn diff codes.c
Index: codes.c
===================================================================
--- codes.c (revision 19)
+++ codes.c (working copy)
@@ -229,7 +229,7 @@
    "UFS 922"
   },
   {
-   #include "ir_codes/lirc/STR_DE545"
+   #include "ir_codes/lirc/str_de545"
    "STR-DE545"
   },
   {`

[Permalink](http://bettyhacks.com/forum/index.php?topic=229.msg1570#msg1570)

---

<a id="msg1571"></a>

## 2. eme · 31. Jan 2010, 12:35

Nochwas kleines..

`boopfirmware/lpctool/trunk$ svn diff lpctool_serial.h
Index: lpctool_serial.h
===================================================================
--- lpctool_serial.h (revision 19)
+++ lpctool_serial.h (working copy)
@@ -1,5 +1,5 @@
 #ifndef LPCTOOL_SERIAL_H
-#define LPCTOOL_DERIAL_H
+#define LPCTOOL_SERIAL_H

 #define TOOLBAUD 115200`

[Permalink](http://bettyhacks.com/forum/index.php?topic=229.msg1571#msg1571)

---

<a id="msg1573"></a>

## 3. eme · 31. Jan 2010, 14:03

Und wieder was..

`boopfirmware/lpctool/trunk$ svn diff lpctool_serial.c
Index: lpctool_serial.c
===================================================================
--- lpctool_serial.c (revision 19)
+++ lpctool_serial.c (working copy)
@@ -37,8 +37,8 @@
    cfsetospeed(&term,B9600);
    break;
   case 19200:
-   cfsetispeed(&term,B38400);
-   cfsetospeed(&term,B38400);
+   cfsetispeed(&term,B19200);
+   cfsetospeed(&term,B19200);
    break;
   case 38400:
    cfsetispeed(&term,B38400);`

[Permalink](http://bettyhacks.com/forum/index.php?topic=229.msg1573#msg1573)

---

<a id="msg1580"></a>

## 4. eme · 31. Jan 2010, 20:17

Habe jetzt Schreibrechte, werde ich bei Gelegenheit mal "committen".

[Permalink](http://bettyhacks.com/forum/index.php?topic=229.msg1580#msg1580)

---

<a id="msg1581"></a>

## 5. Telekatz · 31. Jan 2010, 20:36

Ist schon drin (REV 20).

[Permalink](http://bettyhacks.com/forum/index.php?topic=229.msg1581#msg1581)

---

<a id="msg1812"></a>

## 6. Boregard · 25. Jan 2011, 09:00

Ich hole den Thread jetzt mal hoch um einen kleinen Fehler zu reporten...

In codes.c ist die Makrodefinition für den erweiterten RX5 code falsch:
`#define RC5X   (cmd) cmd`
da darf kein Leerzeichen vor der öffnenten Klammer sein, richtig ist:
`#define RC5X(cmd) cmd`
dann funktionieren auch die erweiterten RC5 Codes.

[Permalink](http://bettyhacks.com/forum/index.php?topic=229.msg1812#msg1812)

---

<a id="msg1866"></a>

## 7. eme · 07. Feb 2011, 17:45

Habe ich geändert.

[Permalink](http://bettyhacks.com/forum/index.php?topic=229.msg1866#msg1866)

---

[← Zurück zu Software](../boards/06-software.md) · [Gesamtindex](../index.md)
