segment code
..start MOV BX, data	
    	MOV DS, BX
    	MOV BX, stack
    	MOV SS, BX
    	MOV SP, bottom

	
        



	
	HLT

	




segment data
firstLine  db 18, ?      ; value
	   resb 18       

secondLine db 18, ?      ; instruction
	   resb 18       

thirdLine  db 18, ?      ; value 
	   resb 18     





segment stack
    	resb 16
bottom: db ?