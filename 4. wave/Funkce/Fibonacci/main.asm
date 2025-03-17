segment code
..start MOV BX, stack
        MOV SS, BX
        MOV SP, top

        POP DX         ; first_value
        POP CX         ; second_value
        POP AX         ; n_value

        PUSH CX        ; F_0
        PUSH DX        ; F_1

        JMP fibonacci
        JMP end_program


fibonacci:
    CMP AX, 0
    JZ end_program_0

    CMP AX, 1
    JZ end_program
    DEC AX

    ADD CX, DX
    PUSH CX

    POP DX
    POP CX
    PUSH CX
    PUSH DX

    JMP fibonacci

end_program:
    HLT

end_program_0:
    POP CX
    HLT


segment stack
        resb 65530
top:    dw 8        ; F_1
        dw 4        ; F_0
        dw 5        ; n
