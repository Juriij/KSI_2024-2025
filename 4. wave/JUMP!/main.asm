segment code
..start MOV BX, data
        MOV DS, BX

        MOV AL, [nums]
        CMP AL, [1]
        

        HLT

segment data
nums    db 64
        db 66
        db 64
        db 9
        db 0
