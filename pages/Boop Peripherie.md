# Boop Peripherie

# Boop-Peripherienutzung

Hier soll eine Übersicht über die unterschiedlichen von Boop genutzten Hardware-Ressourcen (IRQs, Timer etc.) erfolgen.

## Interrupts

Der [LPC2220](LPC2220%20-%2032bit%20arm7tdmi-s%20cpu.md "LPC2220 - 32bit arm7tdmi-s cpu") hat drei Interrupt-Klassen:

- 1x **FIQ** (Fast IRQ)
- 16x **VIC** (Vector IRQs)
- 32x normale IRQs

Die folgenden IRQs sind vergeben:

|         |               |                                                     |
|---------|---------------|-----------------------------------------------------|
| Nummer  | Quelle        | Aufgabe                                             |
| **FIQ** | PWM + TIMER1  | PWM: Sound und LCD-Backlight; TIMER1: IR-Modulation |
| VIC 2   | EINT0: CC1100 | RF-Chip                                             |
| VIC 3   | EINT2: RTC    | Echtzeituhr                                         |
| VIC 4   | I2C           | I2C Übertragung                                     |
| VIC 14  | ADC           | Analog/Digital-Wandler, Batteriespannung            |

Es gibt ferner vier externe Interrupt-Leitungen EINT\[0..3\], die auch zum Aufwecken aus dem Power-Down verwendet werden können:

|         |                                      |
|---------|--------------------------------------|
| Leitung | Belegung                             |
| EINT0   | CC1100, RF-Chip                      |
| EINT1   | BootLoader Enable - Pin am ext. Port |
| EINT2   | RTC, Echtzeituhr                     |
| EINT3   | Betty-Tastatur                       |

  

## Timer

- Der LPC2220 hat zwei identische 32 bit Timer: TIMER0 und TIMER1
  - User manual Chapter 14: Timer/Counter TIMER0 and TIMER1, p. 208.
  - 4 capture channels, 4 match registers

|        |                                    |
|--------|------------------------------------|
| Timer  | Aufgabe                            |
| TIMER0 | Callback-Funktionen, 5ms-Auflösung |
| TIMER1 | IR-Modulation, Auflösung=???       |

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

