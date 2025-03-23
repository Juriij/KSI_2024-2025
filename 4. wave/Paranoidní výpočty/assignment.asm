segment code
..start MOV BX, data	
    	MOV DS, BX
    	MOV BX, stack
    	MOV SS, BX
    	MOV SP, bottom



	MOV AX, 38
	PUSH AX

	MOV BX, 28
	PUSH BX

	CALL minus
	HLT





; result in AX register	
plus:
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
minus:       
      	POP AX     ; return address
	POP BX     ; second_num
	POP CX     ; first_num
	
 
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