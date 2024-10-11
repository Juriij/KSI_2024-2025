class Calculator:
    def __init__(self):
        # TODO: inicializuj atribut
        self.intermediate = 0
    
    # TODO: definuj metody
    def read_intermediate(self):
        return self.intermediate

    def read_result(self):
        result = self.intermediate
        self.intermediate = 0

        return result
    

    def add(self, n: int):
        if isinstance(n, int):
            self.intermediate += n
        else:
            print("invalid input")


    def subtract(self, n: int):
        if isinstance(n, int):
            self.intermediate -= n
        else:
            print("invalid input")


    def multiply(self, n: int):
        if isinstance(n, int):
            self.intermediate = self.intermediate * n
        else:
            print("invalid input")
            

    def divide(self, n: int):
        if isinstance(n, int) and n != 0:
            self.intermediate = self.intermediate // n
        else:
            print("invalid input")
