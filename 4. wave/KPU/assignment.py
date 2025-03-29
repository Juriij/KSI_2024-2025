from enum import Enum
import inspect


class Operation(Enum):
    ADD = 1
    SUB = 2
    INC = 3
    DEC = 4
    CMP = 5

    MOV = 11
    READ = 12
    WRITE = 13
    SET = 14

    PUSH = 21
    POP = 22

    HLT = 31
    NOP = 32

    CALL = 41
    RET = 42

    JMP = 51
    JZ = 52
    JNZ = 53
    JO = 54
    JNO = 55
    JS = 56
    JNS = 57
    JP = 58
    JNP = 59

    INPUT = 61
    OUTPUT = 62


class Status(Enum):
    OK = 1
    HALTED = 2
    BAD_OPERAND = 3
    MEMORY_ERROR = 4
    BAD_INSTRUCTION = 5


class Instruction:
    def __init__(self, op: Operation, operands: list[str]):
        self.op = op
        self.operands = operands






class KPU:
    def __init__(self, memory_size: int, registers: set[str], min_number: int, max_number: int, operations: set[Operation] | None = None):
        if memory_size < 0:
            raise Exception("Error: Wrong memory size")
        self.memory = [0 for _ in range(memory_size)]

        for register in registers:
            if register.isnumeric():
                raise Exception("Error: Register name cannot be numeric")
            
        self.register_record = registers
        self.registers = list({register:0} for register in registers)
            
        self.min_number = min_number
        self.max_number = max_number

        if len(self.memory) > self.max_number:
            raise Exception("Error: Memory is longer than the maximum value allowed")
        
        if 0 > self.max_number:
            raise Exception("Error: Maximum value cannot be lower than zero")
        
        self.operations = operations

        # init of special registers
        self.PC = 0
        self.SP = len(self.memory) - 1
        self.flag_register = {"Overflow": False, "Sign": False, "Zero": False, "Parity": False}

        self.state = Status.OK




    def validate_instruction(self):
        # checking validity of the instruction
        if self.operations is None:
            if not isinstance(self.instruction.op, Operation):
                self.state = Status.BAD_INSTRUCTION
                return self.end_program()

        else:
            if not (self.instruction.op in self.operations):
                self.state = Status.BAD_INSTRUCTION
                return self.end_program()
            
        return None



    def validate_operands(self):
        # checking validity of the operands
        register_found = False
 
        method = getattr(self, self.instruction.op.name.lower())
        sig = inspect.signature(method)

        if (len(sig.parameters) - 1) != len(self.instruction.operands):
            self.state = Status.BAD_OPERAND
            return self.end_program()

        if self.instruction.op.name in {"ADD", "SUB", "INC", "DEC", "CMP", "MOV", "PUSH", "POP", "INPUT", "OUTPUT"}:
            for register in self.instruction.operands:
                if register not in self.register_record:
                    self.state = Status.BAD_OPERAND
                    return self.end_program()
         
        elif self.instruction.op.name in {"CALL", "JMP", "JZ", "JNZ", "JO", "JNO", "JS", "JNS", "JP", "JNP"}:
            if not(self.instruction.operands[0].isdecimal()) or not(self.min_number <= int(self.instruction.operands[0]) <= self.max_number):
                self.state = Status.BAD_OPERAND
                return self.end_program()
        



        elif self.instruction.op.name == "READ":
            if self.instruction.operands[0] not in self.register_record:
                self.state = Status.BAD_OPERAND
                return self.end_program()
            
            # second operand is register
            if (self.instruction.operands[1] in self.register_record):
                for register in self.registers:
                    if self.instruction.operands[1] in register:
                        register_found = True
                        if not(0 <= register[self.instruction.operands[1]] <= len(self.memory)):
                            self.state = Status.MEMORY_ERROR
                            return self.end_program()      

            if not register_found:
                # second operand is address or rubbish      
                if self.instruction.operands[1][0] == "-" or not(self.instruction.operands[1].isdecimal()):
                    if self.instruction.operands[1][1:].isdecimal():
                        self.state = Status.MEMORY_ERROR
                        return self.end_program() 

                    else:
                        self.state = Status.BAD_OPERAND
                        return self.end_program()      

                if self.instruction.operands[1].isdecimal():
                    if int(self.instruction.operands[1]) >= len(self.memory):
                        self.state = Status.MEMORY_ERROR
                        return self.end_program()                     




        elif self.instruction.op.name == "WRITE":
            if self.instruction.operands[1] not in self.register_record:
                self.state = Status.BAD_OPERAND
                return self.end_program()         


            # second operand is register
            if (self.instruction.operands[0] in self.register_record):
                for register in self.registers:
                    if self.instruction.operands[0] in register:
                        register_found = True
                        if not(0 <= register[self.instruction.operands[0]] <= len(self.memory)):
                            self.state = Status.MEMORY_ERROR
                            return self.end_program()      
            
            if not register_found:
                # second operand is address or rubbish      
                if self.instruction.operands[0][0] == "-" or not(self.instruction.operands[0].isdecimal()):
                    if self.instruction.operands[0][1:].isdecimal():
                        self.state = Status.MEMORY_ERROR
                        return self.end_program() 

                    else:
                        self.state = Status.BAD_OPERAND
                        return self.end_program()      

                if self.instruction.operands[0].isdecimal():
                    if int(self.instruction.operands[0]) >= len(self.memory):
                        self.state = Status.MEMORY_ERROR
                        return self.end_program()     
                
        

        elif self.instruction.op.name == "SET":
            if self.instruction.operands[0] not in self.register_record:
                self.state = Status.BAD_OPERAND
                return self.end_program()
            
            if self.instruction.operands[1][0] == "-":
                if not(self.instruction.operands[1][1:].isdecimal()):
                        self.state = Status.BAD_OPERAND
                        return self.end_program()

            else:
                if not(self.instruction.operands[1].isdecimal()):
                    self.state = Status.BAD_OPERAND
                    return self.end_program()
                

            if not(self.min_number <= int(self.instruction.operands[1]) <= self.max_number):
                self.state = Status.BAD_OPERAND
                return self.end_program()
            

        return None




    def run_program(self, code: list[Instruction]) -> tuple[Status, list[int], int]:
        while True:
            # status is not OK
            if self.state != Status.OK:
                return self.end_program()
            
            # PC register points to invalid instruction index
            if not (0 <= self.PC <= len(code)):
                self.state = Status.MEMORY_ERROR
                return self.end_program()
            
            # loading current instruction
            self.instruction = code[self.PC]

            # incrementing PC and overflow handling
            self.PC += 1
            self.PC = self.PC % len(code)


            output = self.validate_instruction()
            if output is not None:
                return output
            
            output = self.validate_operands()
            if output is not None:
                return output
            


            # !!!!! HERE CODE: perform instruction !!!!!!!!

            # !!!!! HERE CODE: perform instruction !!!!!!!!






    def end_program(self):
        return (self.state, self.memory, self.PC)



    def reset(self) -> None:
        # TODO
        pass

    # TODO
    # Add your own functions














if __name__ == "__main__":
    cpu = KPU(15, {"AX", "BX"}, -50, 255)
    program = [
        Instruction(Operation.SET, ["AX", "50"]),
        Instruction(Operation.SET, ["BX", "50"]),
        Instruction(Operation.WRITE, ["AX", "BX"]),
        Instruction(Operation.HLT, []),
    ]
    print(cpu.run_program(program))