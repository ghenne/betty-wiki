# Diskussion:TAE Adapter

ach so, entschuldigung, die information hatte ich nicht. was macht dann der msp? kommt man irgendwie ans datenblatt heran?

- ja, das datenblatt bekommt man wenn man phillips bzw. nxp beschwatzt. hilfreich ist es auch wenn man eine firmenadresse an der hand hat. hier die antwort auf eine anfrage die ich mal gemacht habe:

<!-- -->

    Thank you for contacting NXP Semiconductors.
    Unfortunately, I do not have the PCD80703HL datasheet.  Please contact your local NXP Sales Office and they should be able to help you.
    A list of sales offices can be found at:
    http://www.nxp.com/profile/sales/europe/#Germany

- der msp sitzt zwischen dem pcd und dem funkchip, und uebernimmt wohl die kommunikation zwischen betty und pcd. und ja, sieht nach verschwendung aus, der pcd sollte genug resourcen haben das mit zu uebernehmen. naja, in der theorie zumindest ;)

<!-- -->

- ein paar auzuege bzgl. der funktionalitaet des pcd chips:

<!-- -->

    The PCD80715/16/18HL
    PCD8013/14/15/16/18HL is a baseband controller with embedded Audio Flash for digital cordless base station terminals
    of various radio standards for cordless telephones. The devices combine the functions of its predecessor, the PCD8012,
    with the ability of a digital answering machine with (optional, device type dependant, integrated 4MBit Audio Flash, and
    64kBit parameter E2PROM, see Table 1), wireless data transmission, full duplex handsfree operation, voice recognition
    and limited modem functions.
    The PCD80715/16/18HL
    PCD8013/14/15/16/18HL comprises a R.E.A.L. DSP, an ARM7TDMI microprocessor, SRAM’s (static RAM) for both the
    DSP and the micro controller, the DSP and micro controller program memories memory, a 4 channel hardware ADPCM,
    interface circuits, two Audio CODEC’s, auxiliary A/D and D/A conversion, the baseband RF modem, the Data Flash for
    speech and pattern storage and a parameter E2PROM (type dependant see Table 1). This results in a one-chip
    implementation of the complete baseband of a featured cordless terminal.
    This device offers a power management to reduce the power of those blocks which are not actively processing. By means
    of configuration registers, the internal core clock frequencies can be programmed in order to adapt the speed together
    with the supply voltage according to the processing load.

    4.2.2 HARDWARE FEATURES
    The PCD80715/16/18HL
    PCD8013/14/15/16/18HL offers the following hardware features. Note that the availability of some features depends on
    the chosen package and device type (see Chapter 4.4, 5).
    · Embedded 32-bit microprocessor (SC)
    – ARM7TDMI RISC controller featuring extremely low mW/MHz,
    – 69 MHz core clock speed guaranteed over full specification range,
    – Non-volatile program memory:
    - 704 kbytes on-chip Program Flash (P-Flash)
    - or up to 704 kbytes of on-chip Program ROM depending on type. (see Table1 for memory size).
    – Additional non-volatile firmware memory:
    up to 128 kbytes on-chip ROM memory depending on type (see Table 1).
    – Embedded volatile memory:
    up to 32 kbytes SRAM depending on type (see Table 1).
    – 16 FIQ and 32 IRQ interrupt sources (maskable).
    – 32 different wake up sources
    · Embedded digital signal processor (DSP) subsystem (on PCD80(7)15/16/18H(L) types only, see Table 1)
    – 16-bit fixed point double Harvard architecture: R.E.A.L. core RD16023,
    – Very large instruction code structure for parallel data processing,
    – 96 MHz clock speed guaranteed at 1.80 V supply voltage,
    – 82 MHz clock speed guaranteed over full specification range,
    – Embedded non-volatile memories: 56 kbytes on-chip program memory and 12 kbytes data memory,
    – Embedded volatile memory: 4kbytes of program SRAM and 22 kbytes of data SRAM,
    – 16 maskable and one non-maskable interrupts,
    – 128 application specific instructions (ASIs), all of them located in an SRAM as a software programmable look-up
    table.
    · Embedded flexible burst mode processor
    – Fully flexible slot/frame formatting under software control, adjustable during runtime,
    – Ciphering, scrambling, CRC checking/generation, protected B-fields,
    – Serial interface (for synthesizer programming or other functionality),
    – Programmable timing and polarity of radio control signals,
    – Phase error measurement and phase error correction in hardware,
    – Operation in a PABX environment by synchronisation to an external master clock (SYNCPORT or IOM).
    · Embedded ADPCM
    – 4 channel ADPCM encoding and decoding according G.711 and G.726.
    · Embedded Data Flash (type dependent option, see Table 1)
    – 4 MBit integrated Data Flash for Answering and Data storage applications,
    – For bandwidth intensive applications such as voice recognition, up to 35MBit/s download speed is supported
    – SC independent direct access to DSP registers via DMA interface (DFAC),
    – Fast program and erase times.
    · Embedded parameter E2PROM (type dependent option, see table 1)
    – 64 kBit integrated E2PROM for parameter storage,
    – Independent erase and program operation from Data and Program Flash.
    · Analog processing unit
    Analog master
    – On-chip power-on reset,
    – On-chip interrupt-based power-down warning logic,
    – On-chip reference voltage and electret microphone supply,
    – On-chip low battery detector,
    – Three on-chip voltage regulator control circuits,
    – On-chip DC/DC converter control logic.
    Voice codecs
    – Up to two (depending on type, see Table 1) high performance Bit-Stream D/A and A/D converters for dynamic
    earpiece and dynamic or electret microphone or line interface (switchable),
    – Switchable sensitivity of the audio input for microphone or line interface,
    – Second input pair for voice codec 2 with on-chip multiplexer (depending on type, see Table 1)
    Analog input/output
    – Six-channel time-multiplexed 8-bit A/D converter,
    – Four analog inputs,
    – Highly accurate battery voltage measurement,
    – 7-bit, tunable current source to simplify battery-temperature measurement,
    – On-chip 8-bit D/A converter for various purposes,
    RF interface
    – GFSK pulse shaper with free programmable filter coefficients,
    – RSSI measurement with a programmable time-constant of the input filter,
    – On-chip hardware for fast antenna-diversity,
    – On-chip comparator for the use as data-slicer with slicer filter.
    Miscellaneous
    – Low-power crystal oscillator with programmable on-chip capacitors for frequency adjustment with large pulling
    range,
    – Hardware toll ticket receiver
    · Microprocessor interfaces:
    – General purpose I/O-pins (partly dedicated to KBS, IIC, UART, IOM/PCM, SPI, PWM, RF_SIG and EMI):
    - Total 34 in (L)QFP100 package
    - Total 19 in (L)QFP64 package
    – Keyboard scanner (KBS) interface (up to a 45 keys triangle matrix),
    – IIC interface (up to 400 kbaud),
    – UART with hardware handshake (data and IrDA support),
    – IOM/PCM interface,
    – SPI interface,
    – Buzzer interface to shift out generated bit pattern,
    – Two 32-bit system timers,
    – 46-bit wide memory interface with three predecoded chip select signals, a read and write signal, a 16-bit wide data
    bus and an up to 25-bit wide address bus (available in LFBGA package only).
    · Voltage range:
    – digital parts 1.35V.. 1.85V (please see restrictions in section “Electrical Specification”),
    – analog, Data Flash and E2PROM parts 2.25V ... 2.75V,
    – digital I/O pins 3.0V ... 3.6V.
    · Operating temperature range: -250C ... +70 0C (Data Flash endurance guaranteed downto 0 0C only)
    · Packages: LQFP100, LQFP64, for details see Table 1.
    · Special Debug packages available (see 18 “Hardware and Software Debugging Concept”)

    4.2.3 FIRMWARE FEATURES
    The PCD80715/16/18HL
    PCD8013/14/15/16/18HL offers the following firmware features:
    · DSP Firmware
    – Digital telephone answering machine.
    – Two way recording.
    – Line echo canceller.
    – Network echo suppressor.
    – DTMF detection.
    – Calling line identification presentation (CLIP).
    – Conference call.
    – Automatic volume control.
    – Full duplex and half duplex handsfree.
    – ADPCM codec.
    – Sidetone.
    – Speaker dependent and independent voice recognition.
    · Microprocessor firmware
    – BMP driver (DECT/ISM)

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

