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
        self.PC = -1
        self.SP = len(self.memory) - 1
        self.flag_register = {"Overflow": False, "Sign": False, "Zero": False, "Parity": False}

        self.state = Status.OK









    def run_program(self, code: list[Instruction]) -> tuple[Status, list[int], int]:
        self.len_code = len(code)
        while True:
            # status is not OK
            if self.state != Status.OK:
                return self.end_program()
            
            # incrementing PC
            self.PC += 1
            self.PC = self.PC % (self.max_number+1)
            
            # PC register points to invalid instruction index
            if not (0 <= self.PC <= self.len_code-1):
                self.state = Status.MEMORY_ERROR
                return self.end_program()
            
            # loading current instruction
            self.instruction = code[self.PC]




            output = self.validate_instruction()
            if output is not None:
                return output
            
            output = self.validate_operands()
            if output is not None:
                return output
            

            # perform instruction 
            self.operation = getattr(self, self.instruction.op.name.lower(), None)

            # reset flag register if arithmetic operation is due to execution 
            if self.instruction.op.name in {"ADD", "SUB", "INC", "DEC", "CMP"}:
                self.flag_register = {"Overflow": False, "Sign": False, "Zero": False, "Parity": False}
    
            self.operation()



    def end_program(self):
        return (self.state, self.memory, self.PC)




    def calc_overflow(self, result):
        if result > self.max_number:
            return abs((result % self.max_number) - 1) + self.min_number 

        # result is lower than self.min_number
        else:
            return self.max_number - abs((result % self.min_number) + 1)



    def even_parity(self, result):
        if result < 0:
            magnitude = abs(result)
            count_ones = bin(magnitude).count('1') + 1
        else:
            count_ones = bin(result).count('1')
        
        return count_ones % 2 == 0



    def add(self):
        for register in self.registers:
            if self.instruction.operands[0] in register:
                register_one_value = int(register[self.instruction.operands[0]])
            
            elif self.instruction.operands[1] in register:
                register_two_value = int(register[self.instruction.operands[1]])


        # checking if overflow occured
        if not(self.min_number <= (register_one_value + register_two_value) <= self.max_number):
            self.flag_register["Overflow"] = True
            new_value = self.calc_overflow(register_one_value + register_two_value)

        else:
            new_value = register_one_value + register_two_value


        if new_value < 0:
            self.flag_register["Sign"] = True

        elif new_value == 0:
            self.flag_register["Zero"] = True

        self.flag_register["Parity"] = self.even_parity(new_value)


        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = new_value
                break




    def sub(self):
        for register in self.registers:
            if self.instruction.operands[0] in register:
                register_one_value = int(register[self.instruction.operands[0]])
            
            elif self.instruction.operands[1] in register:
                register_two_value = int(register[self.instruction.operands[1]])

        # checking if overflow occured
        if not(self.min_number <= (register_one_value - register_two_value) <= self.max_number):
            self.flag_register["Overflow"] = True
            new_value = self.calc_overflow(register_one_value - register_two_value)

        else:
            new_value = register_one_value - register_two_value


        if new_value < 0:
            self.flag_register["Sign"] = True

        elif new_value == 0:
            self.flag_register["Zero"] = True

        self.flag_register["Parity"] = self.even_parity(new_value)


        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = new_value
                break
                
        



    def inc(self):
        for register in self.registers:
            if self.instruction.operands[0] in register:
                register_one_value = int(register[self.instruction.operands[0]])
                break

        # checking if overflow occured
        if not(self.min_number <= (register_one_value + 1) <= self.max_number):
            self.flag_register["Overflow"] = True
            new_value = self.calc_overflow(register_one_value + 1)

        else:
            new_value = register_one_value + 1


        if new_value < 0:
            self.flag_register["Sign"] = True

        elif new_value == 0:
            self.flag_register["Zero"] = True

        self.flag_register["Parity"] = self.even_parity(new_value)

        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = new_value
                break





    def dec(self):
        for register in self.registers:
            if self.instruction.operands[0] in register:
                register_one_value = int(register[self.instruction.operands[0]])
                break

        # checking if overflow occured
        if not(self.min_number <= (register_one_value - 1) <= self.max_number):
            self.flag_register["Overflow"] = True
            new_value = self.calc_overflow(register_one_value - 1)

        else:
            new_value = register_one_value - 1


        if new_value < 0:
            self.flag_register["Sign"] = True

        elif new_value == 0:
            self.flag_register["Zero"] = True

        self.flag_register["Parity"] = self.even_parity(new_value)


        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = new_value
                break







    def cmp(self):
        for register in self.registers:
            if self.instruction.operands[0] in register:
                register_one_value = int(register[self.instruction.operands[0]])
                break
            
            elif self.instruction.operands[1] in register:
                register_two_value = int(register[self.instruction.operands[1]])
                break

        # checking if overflow occured
        if not(self.min_number <= (register_one_value - register_two_value) <= self.max_number):
            self.flag_register["Overflow"] = True
            new_value = self.calc_overflow(register_one_value - register_two_value)

        else:
            new_value = register_one_value - register_two_value


        if new_value < 0:
            self.flag_register["Sign"] = True

        elif new_value == 0:
            self.flag_register["Zero"] = True

        self.flag_register["Parity"] = self.even_parity(new_value)



    def read(self):
        # address
        if self.instruction.operands[1].isdecimal():
            address = int(self.instruction.operands[1])

        # register
        else:
            for register in self.registers:
                if self.instruction.operands[1] in register:
                    address = int(register[self.instruction.operands[1]])
                    break

        

        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = self.memory[address]
                break
       



    def write(self):
        # address
        if self.instruction.operands[0].isdecimal():
            address = int(self.instruction.operands[0])

        # register
        else:
            for register in self.registers:
                if self.instruction.operands[0] in register:
                    address = int(register[self.instruction.operands[0]])
                    break

        

        for register in self.registers:
            if self.instruction.operands[1] in register:
                new_value = register[self.instruction.operands[1]]
                break

        self.memory[address] = new_value



    def mov(self):
        for register in self.registers:
            if self.instruction.operands[1] in register:
                moving_value = register[self.instruction.operands[1]]
                break

        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = moving_value
                break



    def set(self):
        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = int(self.instruction.operands[1])
                break




    def push(self):
        if not(-1 <= self.SP-1 <= len(self.memory)-1):
            self.state = Status.MEMORY_ERROR
            return



        for register in self.registers:
            if self.instruction.operands[0] in register:
                push_value = register[self.instruction.operands[0]]
                break

        self.memory[self.SP] = push_value
        self.SP -= 1






    def pop(self):
        if self.SP+1 > len(self.memory)-1:
            self.state = Status.MEMORY_ERROR
            return 
        
        self.SP += 1


        popped_value = self.memory[self.SP]


        for register in self.registers:
            if self.instruction.operands[0] in register:
                register[self.instruction.operands[0]] = popped_value
                break




    def call(self):
        if not(-1 <= self.SP-1 <= len(self.memory)-1):
            self.state = Status.MEMORY_ERROR
            return
        
        self.memory[self.SP] = self.PC
        self.SP -= 1
        
        instruction_index = int(self.instruction.operands[0])

        self.PC = instruction_index - 1



    def ret(self):
        if self.SP+1 > len(self.memory)-1:
            self.state = Status.MEMORY_ERROR
            return 
        
        self.SP += 1

        ret_address = self.memory[self.SP]
        self.PC = ret_address




    def nop(self):
        pass

    def hlt(self):
        self.state = Status.HALTED








    def reset(self) -> None:
        # TODO
        pass






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


    def validate_amount_params(self):
        if self.instruction.op.name in {"ADD", "SUB", "CMP", "READ", "WRITE", "MOV", "SET"}:
            if not len(self.instruction.operands) == 2:
                return False
            
        elif self.instruction.op.name in {"INC", "DEC", "PUSH", "POP", "CALL", "INPUT", "OUTPUT", "JMP", "JZ", "JNZ", "JO", "JNO", "JS", "JNS", "JP", "JNP"}:
            if not len(self.instruction.operands) == 1:
                return False
            
        # RET, HLT, NOP
        else:
            if not len(self.instruction.operands) == 0:
                return False

        return True


    def validate_operands(self):
        # checking validity of the operands
        register_found = False
 

        if not(self.validate_amount_params()):
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







if __name__ == "__main__":
    cpu = KPU(20, {"A", "B"}, 0, 255)

    program = [
    Instruction(Operation.CALL, ['300']),
    Instruction(Operation.HLT, []),
]
    
print(cpu.run_program(program))
print(cpu.registers)