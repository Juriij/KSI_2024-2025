segment code
..start MOV BX, stack
        MOV SS, BX
        MOV SP, top

        CALL fibonacci
        JMP end_program


fibonacci:
    

end_program:
    HLT

segment stack
        resb 65530
top:    dw 1        ; F_1
        dw 0        ; F_0
        dw 3        ; n
