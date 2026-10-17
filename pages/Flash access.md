# Flash access

### Information

Dies sind die Routinen der Original-Firmware, mit der ein Sektor im Flash gelöscht wird und Sektoren im Flash beschrieben werden.

## Sektor im Flash löschen

### Registerbelegung

    Register    Inhalt
    R0          Adresse des zu löschenden Sektors

### Code

    CS0:80001BBC eraseFlashSector                        ; DATA XREF: CS0:off_80000878 o
    CS0:80001BBC                 LDR     R2, =0xAAA
    CS0:80001BC0                 BIC     R3, R0, #0xFF0
    CS0:80001BC4                 BIC     R3, R3, #0xF
    CS0:80001BC8                 LDR     R1, =0x554
    CS0:80001BCC                 MOV     R12, #0xAA ; '¬'
    CS0:80001BD0                 STRH    R12, [R3,R2]
    CS0:80001BD4                 MOV     R12, #0x55 ; 'U'
    CS0:80001BD8                 STRH    R12, [R3,R1]
    CS0:80001BDC                 MOV     R12, #0x80 ; 'Ç'
    CS0:80001BE0                 STRH    R12, [R3,R2]
    CS0:80001BE4                 MOV     R12, #0xAA ; '¬'
    CS0:80001BE8                 STRH    R12, [R3,R2]
    CS0:80001BEC                 MOV     R2, #0x55 ; 'U'
    CS0:80001BF0                 STRH    R2, [R3,R1]
    CS0:80001BF4                 MOV     R3, #0x30 ; '0'
    CS0:80001BF8                 STRH    R3, [R0]
    CS0:80001BFC                 LDRH    R2, [R0]
    CS0:80001C00                 LDRH    R3, [R0]
    CS0:80001C04                 AND     R2, R2, #0x44
    CS0:80001C08                 AND     R3, R3, #0x44
    CS0:80001C0C                 CMP     R2, R3
    CS0:80001C10                 LDREQ   R3, =0x2040004
    CS0:80001C14                 BEQ     loc_80001C88
    CS0:80001C18
    CS0:80001C18 loc_80001C18                            ; CODE XREF: eraseFlashSector+6C j
    CS0:80001C18                 LDRH    R3, [R0]
    CS0:80001C1C                 MOV     R3, R3,LSR#3
    CS0:80001C20                 EOR     R3, R3, #1
    CS0:80001C24                 ANDS    R3, R3, #1
    CS0:80001C28                 BNE     loc_80001C18
    CS0:80001C2C                 MOV     R1, R3
    CS0:80001C30
    CS0:80001C30 loc_80001C30                            ; CODE XREF: eraseFlashSector+C4 j
    CS0:80001C30                 LDRH    R2, [R0]
    CS0:80001C34                 LDRH    R3, [R0]
    CS0:80001C38                 AND     R2, R2, #0x44
    CS0:80001C3C                 AND     R3, R3, #0x44
    CS0:80001C40                 CMP     R2, R3
    CS0:80001C44                 BEQ     loc_80001C84
    CS0:80001C48                 LDRH    R3, [R0]
    CS0:80001C4C                 TST     R3, #0x20
    CS0:80001C50                 BEQ     loc_80001C7C
    CS0:80001C54                 LDRH    R2, [R0]
    CS0:80001C58                 LDRH    R3, [R0]
    CS0:80001C5C                 AND     R2, R2, #0x44
    CS0:80001C60                 AND     R3, R3, #0x44
    CS0:80001C64                 CMP     R2, R3
    CS0:80001C68                 MOVNE   R12, #0xF0 ; '­'
    CS0:80001C6C                 LDRNE   R3, =0x2040004
    CS0:80001C70                 STRNEH  R12, [R0]
    CS0:80001C74                 BNE     loc_80001C88
    CS0:80001C78                 B       loc_80001C84
    CS0:80001C7C ; ---------------------------------------------------------------------------
    CS0:80001C7C
    CS0:80001C7C loc_80001C7C                            ; CODE XREF: eraseFlashSector+94 j
    CS0:80001C7C                 CMP     R1, #0
    CS0:80001C80                 BEQ     loc_80001C30
    CS0:80001C84
    CS0:80001C84 loc_80001C84                            ; CODE XREF: eraseFlashSector+88 j
    CS0:80001C84                                         ; eraseFlashSector+BC j
    CS0:80001C84                 MOV     R3, #0
    CS0:80001C88
    CS0:80001C88 loc_80001C88                            ; CODE XREF: eraseFlashSector+58 j
    CS0:80001C88                                         ; eraseFlashSector+B8 j
    CS0:80001C88                 MOV     R0, R3
    CS0:80001C8C                 RET
    CS0:80001C8C ; End of function eraseFlashSector

## Sektoren beschreiben

### Registerbelegung

    Register    Inhalt
    R0          Adresse des zu löschenden Sektors
    R1          Adresse der Quelldaten
    R2          Anzahl der zu schreibenden Bytes/Wörter

### Code

    CS0:80001C9C programFlash                            ; DATA XREF: CS0:off_8000087C o
    CS0:80001C9C                                         ; CS0:off_800009A0 o
    CS0:80001C9C                 STMFD   SP!, {R4,R5,LR}
    CS0:80001CA0                 MOV     R12, R1
    CS0:80001CA4                 SUBS    LR, R2, #0
    CS0:80001CA8                 MOV     R5, #0
    CS0:80001CAC
    CS0:80001CAC loc_80001CAC                            ; CODE XREF: programFlash+8C j
    CS0:80001CAC                 BLE     loc_80001D2C
    CS0:80001CB0                 LDR     R3, =0xAAA
    CS0:80001CB4                 BIC     R2, R0, #0xFF0
    CS0:80001CB8                 BIC     R2, R2, #0xF
    CS0:80001CBC                 MOV     R1, #0xAA ; '¬'
    CS0:80001CC0                 STRH    R1, [R2,R3]
    CS0:80001CC4                 LDR     R1, =0x554
    CS0:80001CC8                 MOV     R4, #0x55 ; 'U'
    CS0:80001CCC                 STRH    R4, [R2,R1]
    CS0:80001CD0                 MOV     R1, #0xA0 ; 'á'
    CS0:80001CD4                 STRH    R1, [R2,R3]
    CS0:80001CD8                 LDRH    R1, [R12]
    CS0:80001CDC                 MOV     R4, #0
    CS0:80001CE0                 STRH    R1, [R0]
    CS0:80001CE4                 AND     R1, R1, #0x80
    CS0:80001CE8
    CS0:80001CE8 loc_80001CE8                            ; CODE XREF: programFlash+78 j
    CS0:80001CE8                 LDRH    R2, [R0]
    CS0:80001CEC                 AND     R3, R2, #0x80
    CS0:80001CF0                 CMP     R3, R1
    CS0:80001CF4                 MOV     R2, R2,LSL#16
    CS0:80001CF8                 BEQ     loc_80001D18
    CS0:80001CFC                 TST     R2, #0x200000
    CS0:80001D00                 LDRNE   R5, =0x2040005
    CS0:80001D04                 MOVNE   R3, #0xF0 ; '­'
    CS0:80001D08                 STRNEH  R3, [R0]
    CS0:80001D0C                 BNE     loc_80001D18
    CS0:80001D10                 CMP     R4, #0
    CS0:80001D14                 BEQ     loc_80001CE8
    CS0:80001D18
    CS0:80001D18 loc_80001D18                            ; CODE XREF: programFlash+5C j
    CS0:80001D18                                         ; programFlash+70 j
    CS0:80001D18                 SUB     LR, LR, #1
    CS0:80001D1C                 CMP     LR, #0
    CS0:80001D20                 ADD     R0, R0, #2
    CS0:80001D24                 ADD     R12, R12, #2
    CS0:80001D28                 B       loc_80001CAC
    CS0:80001D2C ; ---------------------------------------------------------------------------
    CS0:80001D2C
    CS0:80001D2C loc_80001D2C                            ; CODE XREF: programFlash:loc_80001CAC j
    CS0:80001D2C                 MOV     R0, R5
    CS0:80001D30                 LDMFD   SP!, {R4,R5,PC}
    CS0:80001D30 ; End of function programFlash

<!-- forum-links:start -->
## Forumsdiskussionen: BFS_LoadFile und Flash1

BFS_LoadFile, Flash1 und eine Kontrasteinstellung im Settingsmenü.

### BFS_LoadFile / Flash1 und Kontrasteinstellung

- [BFS_LoadFile, Flash1](../forum/topics/0231-bfs-loadfile-flash1.md) — BFS_LoadFile, Flash1 und eine Kontrasteinstellung im Settingsmenü.
<!-- forum-links:end -->

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

