segment data
firstLine  db 32, ?      ; value
	   resb 32       

secondLine db 32, ?      ; instruction
	   resb 32       

thirdLine  db 32, ?      ; value 
	   resb 32    


firstNum   dw ?
secondIns  db 6
thirdNum   dw ?



temp_space dw ?




counter db ?



SyntaxErrorMessage DB 'Invalid Input: Syntax', '$'
OverflowErrorMessage DB 'Invalid Input: Overflow', '$' 


segment stack
    	resb 16
bottom: db ?





segment code
..start MOV BX, data	
    	MOV DS, BX
    	MOV BX, stack
    	MOV SS, BX
    	MOV SP, bottom


        MOV AH, 0x0a    
        MOV DX, firstLine  
        INT 21h 
	
	MOV counter, 2
	CALL convert_ascii_num1    ; result in [firstNum]





!!!! case: negative input !!!!!
!!!! Edge case: empty input ->>> cover it when loading the input!!!!	

!!!! don't forget to init counter before the CALL!!!!
convert_ascii_num1:    

	CMP [firstLine+1], 0
	JZ return



######## algorithm   ##############
	MOV AX, [firstLine+counter]
	MOV temp_space, AX

        ; checking if the ASCII character is digit
	CMP temp_space, word 48
	JB invalid_syntax

	CMP temp_space, word 57
	JA invalid_syntax

	
	PUSH temp_space
	PUSH 48
	CALL minus
	
	MOV temp_space, AX   	; binary digit moved to temp_space
	

	
	MOV AX, [firstLine+1]
	DEC AX
	PUSH AX
	MOV AX, 10
	PUSH AX
	CALL times
	
	CMP AX, 0
	CALL set_AX_1 


	PUSH temp_space   ; binary digit
	PUSH AX           ; 10 on power of 
	CALL times        ; number in AX 


	MOV BX, firstNum
	PUSH BX 
	PUSH AX
	CALL plus
	
	MOV firstNum, AX
	

######## algorithm   ##############


	DEC [firstLine+1]
	INC counter
	JMP convert_ascii_num1

	





!!!! don't forget RET  don't forget to init counter before the CALL!!!!
convert_ascii_num3:    ; at the end MOV thirdNum, AX
  	



set_AX_1:
	MOV AX, 1
	RET
	
	
return:
	RET










invalid_syntax:
	; display
	MOV DX, SyntaxErrorMessage  
	MOV AH, 09h                  
	INT 21h                      

	; exit
	MOV AH, 4Ch                
	MOV AL, 1                  
	INT 21h                    









; result in AX register
times:                               ; arguments: (first_num, second_num, ret_address)
      	POP AX      ; return address
	POP CX      ; second_num (counter)
	POP DX      ; base_num

	MOV BX, 0   ; result
	MOV DI, 0   ; flag for detecting negative numbers: 0-all_positive,          1-negative


	; add different handiling 1.one num is negative 2.both nums are negative 

	CMP DX, 0
	JS first_negative

	CMP CX, 0
	JS second_negative


	INC CX
	JMP aux_times




first_negative:
	CMP CX, 0
	JS both_negative

	NEG DX
	MOV DI, 1   	; confirmed negative num

	INC CX
	JMP aux_times
	



second_negative:
	NEG CX
	MOV DI, 1   	; confirmed negative num

	INC CX
	JMP aux_times	



both_negative:
	NEG DX
	NEG CX

	INC CX
	JMP aux_times



aux_times:
	DEC CX
	MOV SI, DX  ; inter

	CMP CX, 0
	JZ end_operation_times

	JMP times_loop



times_loop:
	CMP SI, 0
	JZ aux_times

	INC BX
	DEC SI

	JMP times_loop

	



negate_result:
	DEC DI
	NEG BX

	JMP end_operation_times
	


end_operation_times:
	CMP DI, 1
	JZ negate_result

	PUSH AX
	MOV AX, BX

	RET
	





; result in AX register	
plus:                            ; arguments: (first_num, second_num, ret_address)
      	POP AX     ; return address
	POP BX     ; second_num
	POP CX     ; first_num

 
	CMP BX, 0
	JS neg_and_aux_minus


	JMP aux_plus


aux_plus:
	CMP BX, 0
	JZ end_operation	
	
	INC CX
	DEC BX
	
	JMP aux_plus



neg_and_aux_minus:
	NEG BX
	JMP aux_minus	








; result in AX register	
minus:                              ; arguments: (first_num, second_num, ret_address)
      	POP AX    ; return address
	POP BX    ; second_num
	POP CX    ; first_num
	
 
	CMP BX, 0
	JS neg_and_aux_plus


	JMP aux_minus

	
aux_minus:
	CMP BX, 0
	JZ end_operation	
	
	DEC CX
	DEC BX
	
	JMP aux_minus
		


neg_and_aux_plus:
	NEG BX
	JMP aux_plus





end_operation:
	PUSH AX
	MOV AX, CX
	
	RET