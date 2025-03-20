segment code
..start MOV BX, hodnota
        MOV DS, BX

        MOV BX, stack
        MOV SS, BX
        MOV SP, bottom

        MOV AX, 1
        MOV CX, word [val]

        CMP CX, 1
        JS end_program

        INC CX

factorial:
    CMP CX, 1
    JZ call_return

    DEC CX
    PUSH CX

    CALL factorial

    JMP multiply
    


multiply:
    POP CX

    CMP word [val], CX
    JZ final_calc

    MUL CX

    JMP call_return



final_calc:
    MUL CX

    JMP end_program
    


end_program: 
    MOV [val], AX
    HLT


call_return:
    RET



segment stack       
        resb 65530   
bottom: db ?        



segment hodnota
val     dw 3
