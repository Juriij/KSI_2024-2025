
segment code
..start MOV BX, data	
    	MOV DS, BX
    	MOV BX, stack
    	MOV SS, BX
    	MOV SP, bottom



	MOV AX, 38
	MOV BX, 28
	PUSH AX
	PUSH BX

	CALL minus
	HLT






; result in AX register	
minus:       
      	POP AX     ; return address
	POP BX     ; second_num
	POP CX     ; first_num

	JMP aux_minus

	
aux_minus:
	CMP BX, 0
	JZ end_minus 	
	
	DEC CX
	DEC BX
	
	JMP aux_minus
		


end_minus:
	PUSH AX
	MOV AX, CX
	
	RET











segment data
firstLine  db 18, ?      ; value
	   resb 18       

secondLine db 18, ?      ; instruction
	   resb 18       

thirdLine  db 18, ?      ; value 
	   resb 18     


firstNum   dw ?
secondIns  db 6
thirdNum   dw ?





segment stack
    	resb 16
bottom: db ?