segment code
..start MOV BX, data
        MOV DS, BX

        MOV AL, [nums]
        MOV DI, 1

loop:
    MOV DL, [nums+DI]
    CMP DL, 0
    JZ end_program

    CMP AL, DL
    JZ no_change
    JL decrease
    JG increment


increment:
    INC DL
    JMP update_memory


decrease:
    DEC DL
    JMP update_memory


no_change:
    JMP update_memory


update_memory:
    MOV [nums+DI], DL 
    ADD DI, 1
    JMP loop



end_program:
    HLT


segment data
nums    db 64
        db 66
        db 64
        db 9
        db 0
