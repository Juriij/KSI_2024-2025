class Matrix:
    def __init__(self, array: list[list[int | float]]) -> None:
        """ Vytvoreni matice """
        standard_length = len(array[0])
        for row in array:
            if len(row) == standard_length:               
                continue

            raise Exception("Matrix Error: {number of elements per row is inconsistent}")

        self.matrix = array
        self.rows = len(array)
        self.columns = len(array[0])


    @staticmethod
    def zero_matrix(height: int, width: int) -> 'Matrix':
        """ Staticka metoda na vytvoreni nulove matice """
        if height < 1 or width < 1:
            raise Exception("Matrix Error: {cannot initialize matrix of the given height and width}")

        return Matrix([[0 for _ in range(width)] for _ in range(height)])

    @staticmethod
    def identity_matrix(side: int) -> 'Matrix':
        """ Staticka metoda na vytvoreni jednotkove matice """
        if side < 1:
            raise Exception("Matrix Error: {cannot initialize matrix of the given length}")

        return Matrix([[1 if i == j else 0 for j in range(side)] for i in range(side)])

    def __str__(self) -> str:
        """ Pretizeni operatoru __str__ na prevod matice na string """
        text = ''
        for row in self.matrix:
            for elem in row:
                text = text + str(elem) + " "
            text = text[:-1]
            text = text + "\n"

        return text

    def __getitem__(self, tup: tuple[int, int]) -> int | float:
        """ Pretizeni getitemu na vypsani prvku matice """
        row, column = tup[0]-1, tup[1]-1 
        
        if row > self.rows or column > self.columns:
            raise Exception("Matrix Error: {index out of range}")
        
        if row < 0 or column < 0:
            raise Exception("Matrix Error: {index out of range}")

        return self.matrix[row][column]

    def __setitem__(self, tup: tuple[int, int], new_value: int | float) -> None:
        """ Pretizeni setitemu na nastaveni prvku matice """
        row, column = tup[0]-1, tup[1]-1 
        
        if row > self.rows or column > self.columns:
            raise Exception("Matrix Error: {index out of range}")

        if row < 0 or column < 0:
            raise Exception("Matrix Error: {index out of range}")

        self.matrix[row][column] = new_value

    def transposition(self) -> 'Matrix':
        """ Vrati novou matici, ktera je transpozici puvodni matice """
        pass

    def get_info(self) -> tuple[tuple[int, int], bool, bool, bool, bool, bool]:
        """ Vypsani informaci o matici """
        pass

    def __eq__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru ==; tzn jestli se dve matice rovnaji """
        pass

    def __ne__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru !=; tzn jestli jsou dve matice rozdilne """
        pass

    def __add__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru + na scitani matic """
        pass

    def __sub__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru - na odecitani matic """
        pass

    def __mul__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru * na nasobeni matic """
        pass

    def __rmul__(self, constant: int | float) -> 'Matrix':
        """ Pretizeni operatoru * na nasobeni matice konstantou """
        pass

    def determinant(self) -> int | float:
        """ Vrati determinant matice """
        pass

    def inverse(self) -> 'Matrix':
        """ Vrati inverzni matici """
        pass









class Matrix3D:
    def __init__(self, array: list[list[list[int]]]) -> None:
        """ Vytvoreni matice 3D"""
        pass

    def __eq__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru ==; tzn jestli se dve 3D matice rovnaji """
        pass

    def __ne__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru !=; tzn jestli jsou dve 3D matice rozdilne """
        pass

    def determinant_3d(self) -> int:
        """ Vrati determinant 3D matice """
        pass
