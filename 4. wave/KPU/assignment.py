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



    def run_program(self, code: list[Instruction]) -> tuple[Status, list[int], int]:
        # status is not OK
        if self.state != Status.OK:
            return self.end_program()
        
        # PC register points to invalid instruction index
        if not (0 <= self.PC <= len(code)):
            self.state = Status.MEMORY_ERROR
            return self.end_program()
        
        # loading current instruction
        instruction = code[self.PC]

        # incrementing PC and overflow handling
        self.PC += 1
        self.PC = self.PC % len(code)


        # checking validity of the instruction
        if self.operations is None:
            if not (instruction.op in Operation.__members__):
                self.state = Status.BAD_INSTRUCTION
                return self.end_program()

        else:
            if not (instruction.op in self.operations):
                self.state = Status.BAD_INSTRUCTION
                return self.end_program()
            

        # checking validity of the operands
        method = getattr(self, instruction.op.name.lower())
        sig = inspect.signature(method)

        if (len(sig.parameters) - 1) != len(instruction.operands):
            self.state = Status.BAD_OPERAND
            return self.end_program()
        

        if instruction.op.name in set("ADD", "SUB", "INC", "DEC", "CMP", "MOV", "PUSH", "POP", "INPUT", "OUTPUT"):
            for register in instruction.operands:
                if register not in self.register_record:
                    self.state = Status.BAD_OPERAND
                    return self.end_program()
         
        # if instruction.op.name in set("CALL", "JMP", "JZ", "JNZ", "JO", "JNO", "JS", "JNS", "JP", "JNP"):
        #     if not(instruction.operands[0].isdecimal()) or not(self.min_number <= int(instruction.operands[0]) <= self.max_number):
        #         self.state = Status.BAD_OPERAND
        #         return self.end_program()
        
                

        # elif instruction.op.name == "READ":
        #     if instruction.operands[0] not in self.register_record:
        #         self.state = Status.BAD_OPERAND
        #         return self.end_program()
            
        #     if (instruction.operands[1] not in self.register_record): 
        #         if instruction.operands[1][0] == "-":
        #             if not(instruction.operands[1][1:].isdecimal()):
        #                 self.state = Status.BAD_OPERAND
        #                 return self.end_program()

        #         else:
        #             if not(instruction.operands[1].isdecimal()):
        #                 self.state = Status.BAD_OPERAND
        #                 return self.end_program()



        # elif instruction.op.name == "WRITE":

        


        elif instruction.op.name == "SET":
            if instruction.operands[0] not in self.register_record:
                self.state = Status.BAD_OPERAND
                return self.end_program()
            
            if instruction.operands[1][0] == "-":
                if not(instruction.operands[1][1:].isdecimal()):
                        self.state = Status.BAD_OPERAND
                        return self.end_program()

            else:
                if not(instruction.operands[1].isdecimal()):
                    self.state = Status.BAD_OPERAND
                    return self.end_program()
                

            if not(self.min_number <= int(instruction.operands[1]) <= self.max_number):
                self.state = Status.BAD_OPERAND
                return self.end_program()
        

        

        






    def end_program(self):
        return tuple(self.state, self.memory, self.PC)



    def reset(self) -> None:
        # TODO
        pass

    # TODO
    # Add your own functions














if __name__ == "__main__":
    cpu = KPU(15, {"AX", "BX"}, 0, 255)
    program = [
        Instruction(Operation.INPUT, ["AX"]),
        Instruction(Operation.SET, ["BX", "10"]),
        Instruction(Operation.OUTPUT, ["AX"]),
        Instruction(Operation.WRITE, ["BX", "BX"]),
        Instruction(Operation.PUSH, ["BX"]),
        Instruction(Operation.INC, ["AX"]),
        Instruction(Operation.DEC, ["BX"]),
        Instruction(Operation.JNZ, ["2"]),
        Instruction(Operation.HLT, []),
    ]
    # This program should read one chararcter from input
    # and print it and 9 following chars in ASCII.
    print(cpu.run_program(program))

    # Expected status: HALTED
    # Expected memory: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Expected PC: 9