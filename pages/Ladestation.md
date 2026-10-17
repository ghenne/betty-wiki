# Ladestation

[<img src="../images/4/47/Cradle_aussen_vorne.jpg" width="250" height="221" alt="Cradle aussen vorne" />](Datei_Cradle%20aussen%20vorne.jpg.md)

[<img src="../images/1/15/Cradle_innen_oben.jpg" width="250" height="191" alt="Cradle innen oben" />](Datei_Cradle%20innen%20oben.jpg.md)

[<img src="../images/8/8e/Cradle_innen_unten.jpg" width="250" height="253" alt="Cradle innen unten" />](Datei_Cradle%20innen%20unten.jpg.md)

Das Netzteil des [SCART_Adapter_Hardware#Netzteil](SCART%20Adapter%20Hardware.md "SCART Adapter Hardware") ist aus ähnlichen Komponenten aufgebaut.

## Funktion

Steht die Betty in der Ladestation, werden die beiden NI-MH Akkus (700-1000mAh) der Betty geladen.

**getaktetes Schaltnetzteil:**

- FSD200 - 7-beiniger(!) PWM Schaltregler \[[Datenblatt](http://www.datasheetcatalog.com/datasheets_pdf/F/S/D/2/FSD200.shtml)\]
- EL817 - ein einfacher Optokoppler
- AZ431 - (=TL431) Präzisions-Shunt-Regler auf der Sekundärseite des Netzteils \[[Datenblatt](http://www.alldatasheet.com/datasheet-pdf/pdf/137188/BCDSEMI/AZ431-A.html)\]
- Ausgangsspannung 4.2 V (vor Laderegler abgreifen)

**Ladeschaltung:**

- 9202 - PWM Laderegler (10 pins, SMD. Keine Daten zu finden.)

## Modifikationen

[Umbau auf LiIon Akku](Umbau%20auf%20LiIon%20Akku.md "Umbau auf LiIon Akku")

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

