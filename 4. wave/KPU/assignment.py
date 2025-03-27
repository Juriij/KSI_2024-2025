from enum import Enum


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
            
        self.min_number = min_number
        self.max_number = max_number

        if len(self.memory) > self.max_number:
            raise Exception("Error: Memory is longer than the maximum value allowed")
        
        if 0 > self.max_number:
            raise Exception("Error: Maximum value cannot be lower than zero")
        
        self.operations = operations
        






    def run_program(self, code: list[Instruction]) -> tuple[Status, list[int], int]:
        # TODO
        pass

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