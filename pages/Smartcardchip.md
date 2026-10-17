# Smartcardchip

# Hardware

[<img src="../images/1/18/SmartcardChip1.jpg" width="172" height="258" alt="SmartcardChip1" />](Datei_SmartcardChip1.jpg.md)

Der Smartcard-Chip ist rot umrandet

In der Betty-Fernbedienung ist folgender Smartcard-Chip eingebaut:

    Security & Chip Card ICs
    SLE 66C24PE
    8/16-Bit Security Controller
    68-Kbytes ROM, 2304 Bytes RAM, 2-Kbytes EEPROM
    Dual Key Triple DES

Neben dem sehr kurzen 8 seitigen [PDF](http://www.infineon.com/cms/en/services/download.html?filename=%2fdgdl%2fSPI_SLE66C24PE_0105.pdf%3ffolderId%3ddb3a304412b407950112b416848b20bf%26fileId%3ddb3a304412b407950112b41684c420c0&location=Products.Chip_Card___Security_ICs.Chip_Card_Controllers.SLE_66_family__Enhanced_High_Performance_Controller.SLE_66C24PE.DOCUMENTS.SPI_SLE66C24PE_0105.pdf) mit Information zum Chip, in dem nicht einmal die Pinbelegung beschrieben ist, hat ein Benutzer des Forums noch dieses [PDF](http://bettyhacks.com/forum/index.php?action=dlattach;topic=39.0;attach=22) gepostet.

Anschlussbelegung:

              Masse 1 o       8 Power
             nReset 2   SLE   7 Takt
               Data 3 66C24PE 6 nicht verbunden
    nicht verbunden 4         5 nicht verbunden

Der Chip ist wie folgt mit der CPU verbunden:

- CPU Pin 132 (P2.17) steuert den nReset pin. Wird der CPU-Pin auf LO gesetzt ist der Reset aktiv.

<!-- -->

- CPU Pin 78 (P0.10) steuert ueber einen externen Inverter den Power Pin. Wird der CPU-Pin auf LO gesetzt wird der Chip mit Spannung versorgt.

<!-- -->

- CPU Pin 40 (XCLK) ist ueber einen externen Frequenzteiler mit dem Takteingang des Chips verbunden. Im Betrieb wird ueber den CPU-Pin der 7,5 MHz Peripherietakt ausgegeben. Durch den Frequenzteiler wird der Takt halbiert. Der Smartcard-Chip wird dadurch mit mit 3,75 MHz getaktet.

<!-- -->

- CPU Pin 75 (TXD1) und CPU Pin 76 (RXD1) sind mit dem Daten Pin verbunden. Die Datenrate ist 1/64 der Taktfrequenz, also 58593,75 Bit/s und somit nahe an der von einem PC unsterstuetzen Baudrate von 57600 Bit/s (nur ca. 1,7% Abweichung). Neben der Baudrate ist die Parität auf Even sowie 2 Stopbits einzustellen.

Zum Experimentieren kann man den Chip ausloeten und z.B. mit dem Mastermouse-Interface verbinden. Die andere Seite des Interfaces wird an die serielle PC Schnittstelle angeschlossen. Jetzt kann man mit einen Programm wie z.B. WinExplorer Kommandos an den Chip schicken und die Antworten auswerten. Dadurch laesst sich das Uebertragungsformat herausfinden und man kann eine Kommandoliste aufstellen.

# ATR

Nachdem beim Chip ein Reset ausgefuehrt wurde, wird wie bei Smartcards ueblich, ein ATR ausgegeben. Jedoch ist dieser bei der Betty properitaer.

    Betty-ATR:
    03 02 01

- Das erste Byte enthaelt die Anzahl der ATR Bytes incl. des Laengenbytes selbst.
- Das zweite Byte ist das Lifecycle Byte: 1=Virgin, 2=Personalisiert
- Das letzte Byte ist eine XOR Pruefsumme ueber alle vorherigen Bytes.

Bei allen Infineon-Chips gibts eine von Hersteller undokumentierte Funktion den Chip dazu zu bringen statt die Applikation zu starten den Hersteller-ATR auszugeben.

Die Datenleitung muss dazu beim Starten auf LO gehalten und z.B. nach einer Sekunde wieder freigegeben werden.

    Hersteller-ATR:
    33 66 00 04 9C FF xx xx xx xx xx xx 55 0A 07 22 5A

- Die sechs Byte mit xx enthalten eine eine vom Hersteller vergebene Seriennummer. Betty verwendet die gleiche Nummer (im Batteriefach der Fernbedienung).
- Die fuenfte Stelle gibt den Chiptyp an: 9C = SLE66C24PE

# Protokoll

Der Kommandoblock hat folgenden Aufbau:

|  |  |  |
|----|----|----|
| Laengenbyte | Kommandobyte | Optionale Datenbytes |
| Enthaelt die Anzahl der zum Chip gesendeten Bytes incl. des Laengenbytes selbst. | Gibt an welche Aktion der Chip durchfuehren soll. | Bei manchen Kommandos nicht vorhanden. |

  
Der Antwortblock ist wie folgt aufgebaut:

|  |  |  |  |
|----|----|----|----|
| Laengenbyte | Statusbyte | Optionale Datenbytes | Pruefsummenbyte |
| Enthaelt die Anzahl der Antwortbytes incl. des Laengenbytes selbst. | An diesem Byte kann man erkennen ob das Kommando feherfrei ausgefuehrt wurde oder fehlgeschalgen ist. | Bei manchen Kommandos nicht vorhanden. | XOR Pruefsumme ueber alle vorherigen Bytes dieses Antwortblocks |

  
Die Statuswerte in der Antwort haben folgende Bedeutung (Zahlen im Hex. Format):

|  |  |
|----|----|
| Status | Beschreibung |
| 15 | Das Kommando wurde erfolgreich ausgefuehrt |
| 16 | Das Kommandobyte ist zwar gueltig, jedoch nicht die uebergebenen Daten |
| 17 | Das Kommandobyte ist ungueltig |
| 18 | ? |
| 19 | ? |

  
Durch das Ausprobieren aller 256 Moeglichkeiten fuer das Kommandobyte und weglassen aller Kommandos bei denen Status 17 zurueckgegeben wurde ist folgende Liste entstanden.

  
Folgende Kommandos werden unterstuetzt (Zahlen im Hex. Format):

<table data-border="1">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th>Kommando</th>
<th>In der Firmware
<p>verwendet?</p></th>
<th>Bedeutung</th>
</tr>
&#10;<tr>
<td>3F</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>41</td>
<td>Ja</td>
<td>SC_ID auslesen</td>
</tr>
<tr>
<td>42</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>43</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>44</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>45</td>
<td>Ja</td>
<td>SC_MEM auslesen</td>
</tr>
<tr>
<td>46</td>
<td>Ja</td>
<td>SC_MEM beschreiben</td>
</tr>
<tr>
<td>47</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>48</td>
<td>Ja</td>
<td>12 dez. Byte lange Zufallszahl ausgeben</td>
</tr>
<tr>
<td>49</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>4A</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>4B</td>
<td>Nein</td>
<td>?</td>
</tr>
<tr>
<td>4D</td>
<td>Ja</td>
<td>?</td>
</tr>
<tr>
<td>4F</td>
<td>Ja</td>
<td>?</td>
</tr>
<tr>
<td>50</td>
<td>Ja</td>
<td>SC_Sec_MEM auslesen</td>
</tr>
<tr>
<td>51</td>
<td>Ja</td>
<td>?</td>
</tr>
</tbody>
</table>

  

### Kommando 3F

- wird in der Firmware nicht verwendet

### Kommando 41 (SC_ID auslesen)

- wird in der Firmware bei Adresse 80035BA4 verwendet
- keine Kommando-Daten
- Daten im Antwortblock: Kommandobyte-Echo, 6 Byte lange ID (identisch mit der ID im Batteriefach), 00, 8 \* unbekannte Bytes

### Kommando 42

- wird in der Firmware nicht verwendet

### Kommando 43

- wird in der Firmware nicht verwendet

### Kommando 44

- wird in der Firmware nicht verwendet

### Kommando 45 (SC_MEM auslesen)

- wird in der Firmware bei Adresse 80035890 verwendet
- Kommando-Daten: Registernummer (DWORD), Unbekannt1 (DWORD)
- Daten im Antwortblock: Kommandobyte-Echo, 3 \* 00, Unbekannt1-Echo (DWORD), Registernummer-Echo (DWORD), Registerinhalt (DWORD), 5 \* unbekannte Bytes
- Wertebereich fuer Registernummer: 0 .. E2h

### Kommando 46 (SC_MEM beschreiben)

- wird in der Firmware bei Adresse 8003596C verwendet
- Kommando-Daten: Registernummer (DWORD), Registerinhalt (DWORD)
- keine Daten im Antwortblock
- Wertebereich fuer Registernummer: 0 .. E2h

### Kommando 47

- wird in der Firmware nicht verwendet

### Kommando 48 (12 Byte lange Zufallszahl ausgeben)

- wird in der Firmware bei Adresse 800357C8 verwendet
- keine Kommando-Daten
- Daten im Antwortblock: Kommandobyte-Echo, 3 \* 00, 12 dez. \* Zufallsbytes

### Kommando 49

- wird in der Firmware nicht verwendet

### Kommando 4A

- wird in der Firmware nicht verwendet

### Kommando 4B

- wird in der Firmware nicht verwendet

### Kommando 4D

- wird in der Firmware bei Adresse 80035AFC verwendet
- Kommando-Daten: 0 bis 3Eh Bytes moeglich (die Firmware benutzt 4 Byte)
- Daten im Antwortblock: 4 \* 8 Byte Bloecke (manchmal ist Block 2 und 3 identisch)

### Kommando 4F

- wird in der Firmware bei Adresse 80035568 verwendet
- Kommando-Daten: Unbekannt1 (DWORD), Unbekannt2 (DWORD)
- Daten im Antwortblock: Kommandobyte-Echo, 3 \* 00, Unbekannt2-Echo (DWORD), 16 dez. \* unbekannte Bytes
- Wertebereich fuer Unbekannt1: 0 .. Bh

### Kommando 50 (SC_Sec_MEM auslesen)

- wird in der Firmware bei Adresse 80035A10 verwendet
- Kommando-Daten: Registernummer (DWORD), Unbekannt1 (DWORD)
- Daten im Antwortblock: Kommandobyte-Echo, 3 \* 00, Registernummer-Echo (DWORD), Registerinhalt (DWORD), 5 \* unbekannte Bytes
- Wertebereich fuer Registernummer: 0 .. 95h

### Kommando 51

- wird in der Firmware bei Adresse 80035610 verwendet
- Kommando-Daten: Unbekannt1 (DWORD)
- Daten im Antwortblock: Kommandobyte-Echo, 3 \* 00, Unbekannt1-Echo (DWORD), 8 \* 00, 8 \* unbekannte Bytes.

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

