# Betty init

here is a part of the disassembly of the original firmware.  
it should show you how to init the chip, memory banks, and  
also initializes the lc-display.  
the functions are stripped down, so that only the code needed  
to show the init sequence remains.  
  
  
first function is a pause loop, pause time is given in register R0.  
values shown are for R0=64  
  

    CS0:80000BF4 pause                                   ; CODE XREF: sub_80000C98+40�p
    CS0:80000BF4                                         ; initLCD+24�p ...
    CS0:80000BF4                 LDR     R2, =T0IR
    CS0:80000BF8                 MOV     R3, #0
    CS0:80000BFC                 STR     R3, [R2,#0x10]
    CS0:80000C00                 ADD     R0, R0, R0,LSL#2       -> (64*4)+64 = 320
    CS0:80000C04                 ADD     R3, R3, #2
    CS0:80000C08                 STR     R3, [R2,#4]
    CS0:80000C0C                 ADD     R0, R0, R0,LSL#2       -> (320*4)+320 = 1600
    CS0:80000C10                 SUB     R3, R3, #1
    CS0:80000C14                 RSB     R0, R0, R0,LSL#4       -> (1600*16)-1600 = 24000
    CS0:80000C18                 STR     R3, [R2,#4]
    CS0:80000C1C                 MOV     R0, R0,LSL R3      -> 24000*2 = 48000
    CS0:80000C20
    CS0:80000C20 loc_80000C20                            ; CODE XREF: pause+38�j
    CS0:80000C20                 LDR     R2, =T0IR
    CS0:80000C24                 LDR     R3, [R2,#8]
    CS0:80000C28                 CMP     R3, R0
    CS0:80000C2C                 BCC     loc_80000C20
    CS0:80000C30                 MOV     R3, #2
    CS0:80000C34                 STR     R3, [R2,#4]
    CS0:80000C38 ; End of function pause

  
  
this is a part of the main startup routine. the pll is set up here,  
and the two flash-memory banks are configured.  
  

    CS0:80000054 STARTUP                                 ; CODE XREF: CS0:RESET_VEC j
    CS0:80000054                                         ; DATA XREF: CS0:off_80000028 o
    CS0:80000054                 LDR     R0, =PLL_CONTROL       =0x10000420
    CS0:80000058                 MOV     R1, #0xAA ; '¬'
    CS0:8000005C                 MOV     R2, #0x55 ; 'U'
    CS0:80000060                 LDR     R4, =dword_800029AC    =0x42, =30mhz @ 10mhz input
    CS0:80000064                 LDR     R3, [R4]
    CS0:80000068                 STR     R3, [R0,#4]        PLLCFG = 0100.0010<br>
    CS0:8000006C                 MOV     R3, #1
    CS0:80000070                 STR     R3, [R0]           PLLCON, PLLE=1,PLLC=0
    CS0:80000074                 STR     R1, [R0,#0xC]      PLLFEED
    CS0:80000078                 STR     R2, [R0,#0xC]      PLLFEED
    CS0:8000007C
    CS0:8000007C loc_8000007C                            ; CODE XREF: CS0:80000084 j
    CS0:8000007C                 LDR     R3, [R0,#8]        PLLSTAT
    CS0:80000080                 ANDS    R3, R3, #0x400
    CS0:80000084                 BEQ     loc_8000007C
    CS0:80000088                 MOV     R3, #3
    CS0:8000008C                 STR     R3, [R0]           PLLCON, PLLE=1, PLLC=1
    CS0:80000090                 STR     R1, [R0,#0xC]      PLLFEED
    CS0:80000094                 STR     R2, [R0,#0xC]      PLLFEED
    CS0:80000098                 LDR     R0, =PINSEL2
    CS0:8000009C                 LDR     R1, =dword_800029A4    =0xD6041D4
    CS0:800000A0                 LDR     R2, [R1]
    CS0:800000A4                 STR     R2, [R0]           PINSEL2 = 0xD6041D4
    CS0:800000A8                 LDR     R1, =dword_800029A8    =0x10000420
    CS0:800000AC                 LDR     R2, [R1]
    CS0:800000B0                 LDR     R0, =BCFG0
    CS0:800000B4                 STR     R2, [R0]
    CS0:800000B8                 LDR     R0, =BCFG2         BCFG2=BCF0=0x10000420
    CS0:800000BC                 STR     R2, [R0]

  
  
this snippet initializes bank#1, where the lc-display is connected to.  
0x81000000 is the command interface, 0x81000001 is for data  
  

    CS0:80000C98 sub_80000C98                            ; CODE XREF: sub_80000294+4C p<br>
    CS0:80000CAC                 LDR     R2, =0xC42
    CS0:80000CB0                 LDR     R3, =BCFG1
    CS0:80000CB4                 STR     R2, [R3]

  
  
here the lc-display gets initialized and cleared.  
values shown with -\> are what is written to the command interface of the lcd.  

    CS0:80000F84 initLCD                                 ; DATA XREF: CS0:80002A08?o
    CS0:80000F8C                 MOVL    R3, 0xFFFFFFE1
    CS0:80000F90                 MOV     R4, #0x81000000
    CS0:80000F94                 STRB    R3, [R4]           ->   E1
    CS0:80000F98                 ADD     R3, R3, #1         
    CS0:80000FA0                 MOV     R0, #0x64 ; 'd'
    CS0:80000FA4                 STRB    R3, [R4]           ->   E2
    CS0:80000FA8                 BL      pause
    CS0:80000FAC                 MOVL    R3, 0xFFFFFFAB
    CS0:80000FB0                 STRB    R3, [R4]           ->   AB
    CS0:80000FB4                 ADD     R3, R3, #0x7C
    CS0:80000FB8                 STRB    R3, [R4]           ->   27
    CS0:80000FBC                 MOVL    R2, 0xFFFFFF81
    CS0:80000FC0                 ADD     R3, R3, #0x18
    CS0:80000FC4                 STRB    R2, [R4]           ->   81
    CS0:80000FC8                 STRB    R3, [R4]           ->   3F
    CS0:80000FCC                 ADD     R3, R3, #0x26
    CS0:80000FD0                 STRB    R3, [R4]           ->   65
    CS0:80000FD4                 SUB     R3, R3, #5
    CS0:80000FD8                 STRB    R3, [R4]           ->   60
    CS0:80000FDC                 SUB     R3, R3, #0x44
    CS0:80000FE0                 STRB    R3, [R4]           ->   1C
    CS0:80000FE4                 ADD     R3, R3, #0x45
    CS0:80000FE8                 STRB    R3, [R4]           ->   61
    CS0:80000FEC                 SUB     R3, R3, #0x57
    CS0:80000FF0                 STRB    R3, [R4]           ->   0A
    CS0:80000FF4                 ADD     R3, R3, #0x58
    CS0:80000FF8                 STRB    R3, [R4]           ->   62
    CS0:80000FFC                 ADD     R3, R3, #0x13
    CS0:80001000                 STRB    R3, [R4]           ->   75
    CS0:80001004                 SUB     R3, R3, #0x12
    CS0:80001008                 STRB    R3, [R4]           ->   63
    CS0:8000100C                 SUB     R3, R3, #0xD3
    CS0:80001010                 STRB    R2, [R4]           ->   81
    CS0:80001014                 STRB    R3, [R4]           ->   90
    CS0:80001018                 SUB     R3, R3, #8
    CS0:8000101C                 STRB    R3, [R4]           ->   88
    CS0:80001020                 MOV     R5, #0
    CS0:80001024                 ADD     R3, R3, #1
    CS0:80001028                 STRB    R5, [R4]           ->   00
    CS0:8000102C                 STRB    R3, [R4]           ->   89
    CS0:80001030                 ADD     R3, R3, #1
    CS0:80001034                 STRB    R5, [R4]           ->   00
    CS0:80001038                 MOV     R1, #0x33 ; '3'
    CS0:8000103C                 STRB    R3, [R4]           ->   8A
    CS0:80001040                 ADD     R3, R3, #1
    CS0:80001044                 STRB    R1, [R4]           ->   33
    CS0:80001048                 STRB    R3, [R4]           ->   8B
    CS0:8000104C                 ADD     R3, R3, #1
    CS0:80001050                 STRB    R1, [R4]           ->   33
    CS0:80001054                 MOV     R12, #0x66 ; 'f'
    CS0:80001058                 STRB    R3, [R4]           ->   8C
    CS0:8000105C                 ADD     R3, R3, #1
    CS0:80001060                 STRB    R12, [R4]          ->   66
    CS0:80001064                 STRB    R3, [R4]           ->   8D
    CS0:80001068                 ADD     R3, R3, #1
    CS0:8000106C                 STRB    R12, [R4]          ->   66
    CS0:80001070                 MOVL    LR, 0xFFFFFF99
    CS0:80001074                 STRB    R3, [R4]           ->   8E
    CS0:80001078                 ADD     R3, R3, #1
    CS0:8000107C                 STRB    LR, [R4]           ->   99
    CS0:80001080                 MOV     R0, R5
    CS0:80001084                 STRB    R3, [R4]           ->   8F
    CS0:80001088                 STRB    LR, [R4]           ->   99

    CS0:80000F58                 CMP     R0, #0
    CS0:80000F5C                 MOV     R1, #0x81000000
    CS0:80000F60                 MOVLNE  R3, 0xFFFFFFA1
    CS0:80000F64                 MOVLEQ  R3, 0xFFFFFFA0
    CS0:80000F68                 STRNEB  R3, [R1]   ->   0FFFFFFA1
    CS0:80000F6C                 STREQB  R3, [R1]           ->   A0
    CS0:80000F70                 ADDNE   R3, R3, #0x1F
    CS0:80000F74                 ADDEQ   R3, R3, #0x28
    CS0:80000F78                 STRNEB  R3, [R1]   ->   0FFFFFFC0
    CS0:80000F7C                 STREQB  R3, [R1]           ->   C8

    CS0:80001090                 MOV     R3, #0x2E ; '.'
    CS0:80001094                 STRB    R3, [R4]           ->   2E
    CS0:80001098                 MOV     R0, #0x7D0
    CS0:8000109C                 BL      pause
    CS0:800010A0                 MOV     R3, #0x2F ; '/'
    CS0:800010A4                 STRB    R3, [R4]           ->   2F
    CS0:800010A8                 SUB     R3, R3, #0x8B
    CS0:800010AC                 STRB    R3, [R4]           ->   A4
    CS0:800010B0                 ADD     R3, R3, #2
    CS0:800010B4                 STRB    R3, [R4]           ->   A6
    CS0:800010B8

  
  
this loop clears the lcd screen. it has 128x160 pixels, adressed byte-wise  
(one byte = 8 pixels).  
  

    CS0:800010B8 initLCD_loop1                           ; CODE XREF: initLCD+180?j
    CS0:800010B8                 MOV     R1, #0x81000000 ; clear screen
    CS0:800010BC                 MOVL    R3, 0xFFFFFFB0
    CS0:800010C0                 MOV     R2, R5,LSR#3
    CS0:800010C4                 STRB    R3, [R1]           ->   B0
    CS0:800010C8                 AND     R2, R2, #0x1F
    CS0:800010CC                 ADD     R3, R3, #0x60
    CS0:800010D0                 STRB    R2, [R1]           ->   y-coord?
    CS0:800010D4                 STRB    R3, [R1]           ->   10
    CS0:800010D8                 SUB     R3, R3, #0x10
    CS0:800010DC                 STRB    R3, [R1]           ->   x-coord?
    CS0:800010E0                 MOV     R2, #0x7F ; '?'
    CS0:800010E4
    CS0:800010E4 lcdINIT_loop2                           ; CODE XREF: initLCD+174?j
    CS0:800010E4                 LDR     R3, =byte_81000001
    CS0:800010E8                 MOV     R0, #0
    CS0:800010EC                 SUBS    R2, R2, #1
    CS0:800010F0                 STRB    R0, [R3]           ->   data 00
    CS0:800010F4                 STRB    R0, [R3]           ->   data 00
    CS0:800010F8                 BPL     lcdINIT_loop2
    CS0:800010FC                 ADD     R5, R5, #8
    CS0:80001100                 CMP     R5, #0x9F ; 'ƒ'
    CS0:80001104                 BLE     initLCD_loop1
    CS0:80001108                 MOVL    R2, 0xFFFFFFAF
    CS0:8000110C                 SUB     R3, R3, #1
    CS0:80001110                 STRB    R2, [R3]           ->   AF
    CS0:80001114 ; End of function initLCD

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

