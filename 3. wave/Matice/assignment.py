class Matrix:
    def __init__(self, array: list[list[int | float]]) -> None:
        """ Vytvoreni matice """
        standard_length = len(array[0])
        for row in array:
            if len(row) == standard_length:               
                continue

            raise Exception("Matrix Error: {number of elements per row is inconsistent}")

        self.matrix = array
        self.len_rows = len(array)
        self.len_columns = len(array[0])


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
        
        if row > self.len_rows or column > self.len_columns:
            raise Exception("Matrix Error: {index out of range}")
        
        if row < 0 or column < 0:
            raise Exception("Matrix Error: {index out of range}")

        return self.matrix[row][column]

    def __setitem__(self, tup: tuple[int, int], new_value: int | float) -> None:
        """ Pretizeni setitemu na nastaveni prvku matice """
        row, column = tup[0]-1, tup[1]-1 
        
        if row > self.len_rows or column > self.len_columns:
            raise Exception("Matrix Error: {index out of range}")

        if row < 0 or column < 0:
            raise Exception("Matrix Error: {index out of range}")

        self.matrix[row][column] = new_value

    def transposition(self) -> 'Matrix':
        """ Vrati novou matici, ktera je transpozici puvodni matice """
        return Matrix([[self.matrix[j][i] for j in range(self.len_rows)] for i in range(self.len_columns)])


    def get_info(self) -> tuple[tuple[int, int], bool, bool, bool, bool, bool]:
        """ Vypsani informaci o matici """
        dimensions = (self.len_rows, self.len_columns)
        square_matrix = self.len_rows == self.len_columns
        symmetric_matrix = (square_matrix) and all(self.matrix[i][j] == self.matrix[j][i]
                                                    for i in range(self.len_rows) 
                                                    for j in range(self.len_columns))   

        antisymmetric_matrix = (square_matrix) and all(self.matrix[i][j] == -self.matrix[j][i]
                                                    for i in range(self.len_rows) 
                                                    for j in range(self.len_columns))  

        row_echelon_form = (self.matrix[0][0] != 0) and all(self.matrix[i][:i] == [0 for _ in range(i)]
                                                            for i in range(1, self.len_rows))

        diagonal_matrix = (square_matrix) and all(self.matrix[i][j] != 0 if i == j 
                                                    else self.matrix[i][j] == 0
                                                    for i in range(self.len_rows)
                                                    for j in range(self.len_columns))


        return f'({dimensions}, {square_matrix}, {symmetric_matrix}, {antisymmetric_matrix}, {row_echelon_form}, {diagonal_matrix})'


    def __eq__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru ==; tzn jestli se dve matice rovnaji """
        if isinstance(other_matrix, Matrix):
            if (other_matrix.len_rows == self.len_rows) and (other_matrix.len_columns == self.len_columns):
                return all(self.matrix[i][j] == other_matrix.matrix[i][j]
                            for i in range(self.len_rows)
                            for j in range(self.len_columns))

            else:
                return False

        else:
            return False


    def __ne__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru !=; tzn jestli jsou dve matice rozdilne """
        if not isinstance(other_matrix, Matrix):
            return True
        
        else:
            if not ((other_matrix.len_rows == self.len_rows) and (other_matrix.len_columns == self.len_columns)):
                return True

            else:
                return any(self.matrix[i][j] != other_matrix.matrix[i][j]
                            for i in range(self.len_rows)
                            for j in range(self.len_columns))



    def __add__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru + na scitani matic """
        if isinstance(other_matrix, Matrix):
            if (other_matrix.len_rows == self.len_rows) and (other_matrix.len_columns == self.len_columns):
                return Matrix([[self.matrix[i][j] + other_matrix.matrix[i][j] for j in range(self.len_columns)] for i in range(self.len_rows)])

            raise Exception("Matrix Error: {matrices aren't of the same size}")

        raise Exception("Matrix Error: {given argument is not a Matrix}")


    def __sub__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru - na odecitani matic """
        if isinstance(other_matrix, Matrix):
            if (other_matrix.len_rows == self.len_rows) and (other_matrix.len_columns == self.len_columns):
                return Matrix([[self.matrix[i][j] - other_matrix.matrix[i][j] for j in range(self.len_columns)] for i in range(self.len_rows)])

            raise Exception("Matrix Error: {matrices aren't of the same size}")

        raise Exception("Matrix Error: {given argument is not a Matrix}")


    def __rmul__(self, constant: int | float) -> 'Matrix':
        """ Pretizeni operatoru * na nasobeni matice konstantou """
        if isinstance(constant, int) or isinstance(constant, float):
            return Matrix([[self.matrix[i][j] * constant for j in range(self.len_columns)] for i in range(self.len_rows)])
        
        raise Exception("Matrix Error: {constant must be an integer or float}")




    def __mul__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru * na nasobeni matic """
        if isinstance(other_matrix, Matrix):
            if self.len_columns == other_matrix.len_rows:
                return Matrix([[sum([self.matrix[i][g] * other_matrix.matrix[g][j] for g in range(self.len_columns)]) for j in range(other_matrix.len_columns)] for i in range(self.len_rows)])

            raise Exception("Matrix Error: {matrices aren't of compatible size for this operation}")

        raise Exception("Matrix Error: {given argument is not a Matrix}")


    def det_slice(self, matrix, start_point):
        all_rows = []
        for i in range(1, matrix.len_rows):
            new_row = []

            for j in range(matrix.len_columns):
                if j == start_point:
                    continue
                new_row.append(matrix.matrix[i][j])

            all_rows.append(new_row)

        return Matrix(all_rows)



    def det_auxilary(self, matrix):
        if matrix.len_rows == 2 and matrix.len_columns == 2:
            return (matrix.matrix[0][0] * matrix.matrix[1][1]) - (matrix.matrix[0][1] * matrix.matrix[1][0])
        
        result = 0

        for j in range(matrix.len_columns):              # creates one new matrix
            new_matrix = self.det_slice(matrix, j)       # returns reduced matrix
            minor = (-1)**(1+(j+1)) * matrix.matrix[0][j] * self.det_auxilary(new_matrix)

            result += minor

        return result


    def determinant(self) -> int | float:
        """ Vrati determinant matice """
        if self.len_rows == self.len_columns:
            if self.len_rows == 1:
                return self.matrix[0][0]
                
            return self.det_auxilary(self)

        raise Exception("Matrix Error: {matrix is not of a square shape}")





    def find_non_zero(self, current_column, matrix_a, matrix_b):
        for i in range(matrix_a.len_rows):
            if current_column == i:
                continue

            elif matrix_a.matrix[i][current_column] != 0:
                if matrix_a.matrix[current_column][i] != 0:
                    # TODO
                    # make a swap for both matrices (matrix_a, matrix_b) and end the function
                    pass

 


        raise Exception("Matrix Error: {matrix doesn't have an inverse}")



    def inverse(self) -> 'Matrix':
        """ Vrati inverzni matici """
        if self.len_rows == self.len_columns:
            matrix_a = Matrix(self.matrix)
            matrix_b = self.identity_matrix(matrix_a.len_rows)

            for i in range(matrix_a.len_rows):
                if matrix_a.matrix[i][i] == 0:
                    matrix_a, matrix_b = self.find_non_zero(i, matrix_a, matrix_b)



        raise Exception("Matrix Error: {matrix is not of a square shape}")
















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
