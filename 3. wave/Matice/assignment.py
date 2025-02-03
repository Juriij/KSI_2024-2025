class Matrix:
    def __init__(self, array: list[list[int | float]]) -> None:
        """ Vytvoreni matice """
        standard_length = len(array[0])
        for row in array:
            if len(row) == standard_length:
                continue

            raise Exception(
                "Matrix Error: {number of elements per row is inconsistent}"
            )

        self.matrix = array
        self.len_rows = len(array)
        self.len_columns = len(array[0])

    @staticmethod
    def zero_matrix(height: int, width: int) -> 'Matrix':
        """ Staticka metoda na vytvoreni nulove matice """
        if height < 1 or width < 1:
            raise Exception(
                "Matrix Error: "
                "{cannot initialize matrix of the given height and width}"
            )

        return Matrix([[0 for _ in range(width)] for _ in range(height)])

    @staticmethod
    def identity_matrix(side: int) -> 'Matrix':
        """ Staticka metoda na vytvoreni jednotkove matice """
        if side < 1:
            raise Exception(
                "Matrix Error: {cannot initialize matrix of the given length}"
            )

        return Matrix([
            [1 if i == j else 0 for j in range(side)]
            for i in range(side)
        ])

    def __str__(self) -> str:
        """ Pretizeni operatoru __str__ na prevod matice na string """
        text = ''
        for row in self.matrix:
            for elem in row:
                text = text + str(elem) + " "
            text = text[:-1]
            text += '\n'

        return text

    def __getitem__(self, tup: tuple[int, int]) -> int | float:
        """ Pretizeni getitemu na vypsani prvku matice """
        row, column = tup[0]-1, tup[1]-1

        if row > self.len_rows or column > self.len_columns:
            raise Exception("Matrix Error: {index out of range}")

        if row < 0 or column < 0:
            raise Exception("Matrix Error: {index out of range}")

        return self.matrix[row][column]

    def __setitem__(
        self, tup: tuple[int, int], new_value: int | float
    ) -> None:
        """ Pretizeni setitemu na nastaveni prvku matice """
        row, column = tup[0]-1, tup[1]-1

        if row > self.len_rows or column > self.len_columns:
            raise Exception("Matrix Error: {index out of range}")

        if row < 0 or column < 0:
            raise Exception("Matrix Error: {index out of range}")

        self.matrix[row][column] = new_value

    def transposition(self) -> 'Matrix':
        """ Vrati novou matici, ktera je transpozici puvodni matice """
        return Matrix([
            [self.matrix[j][i] for j in range(self.len_rows)]
            for i in range(self.len_columns)
        ])

    def get_info(self) -> tuple[tuple[int, int], bool, bool, bool, bool, bool]:
        """ Vypsani informaci o matici """
        if self.len_rows == 1 and self.len_columns == 1:
            return ((1, 1), True, True, True, True, True)

        dimensions = (self.len_rows, self.len_columns)
        square_matrix = self.len_rows == self.len_columns
        symmetric_matrix = (
            square_matrix
            and all(
                self.matrix[i][j] == self.matrix[j][i]
                for i in range(self.len_rows)
                for j in range(self.len_columns)
            )
        )

        antisymmetric_matrix = (
            square_matrix
            and all(
                self.matrix[i][j] == -self.matrix[j][i]
                for i in range(self.len_rows)
                for j in range(self.len_columns)
            )
        )

        row_echelon_form = (
            self.matrix[0][0] != 0
            and all(
                self.matrix[i][:i] == [0 for _ in range(i)]
                for i in range(1, self.len_rows)
            )
        )

        diagonal_matrix = (
            square_matrix
            and all(
                self.matrix[i][j] != 0 if i == j else self.matrix[i][j] == 0
                for i in range(self.len_rows)
                for j in range(self.len_columns)
            )
        )

        return (
            dimensions,
            square_matrix,
            symmetric_matrix,
            antisymmetric_matrix,
            row_echelon_form,
            diagonal_matrix
        )

    def __eq__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru ==; tzn jestli se dve matice rovnaji """
        if isinstance(other_matrix, Matrix):
            if (other_matrix.len_rows == self.len_rows) and \
               (other_matrix.len_columns == self.len_columns):
                return all(
                    self.matrix[i][j] == other_matrix.matrix[i][j]
                    for i in range(self.len_rows)
                    for j in range(self.len_columns)
                )
            return False

        return False

    def __ne__(self, other_matrix: object) -> bool:
        """ Pretizeni operatoru !=; tzn jestli jsou dve matice rozdilne """
        if not isinstance(other_matrix, Matrix):
            return True

        if (other_matrix.len_rows != self.len_rows) or \
           (other_matrix.len_columns != self.len_columns):
            return True

        return any(
            self.matrix[i][j] != other_matrix.matrix[i][j]
            for i in range(self.len_rows)
            for j in range(self.len_columns)
        )

    def __add__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru + na scitani matic """
        if isinstance(other_matrix, Matrix):
            if (other_matrix.len_rows == self.len_rows) and \
               (other_matrix.len_columns == self.len_columns):
                return Matrix(
                    [
                        [
                            self.matrix[i][j] + other_matrix.matrix[i][j]
                            for j in range(self.len_columns)
                        ]
                        for i in range(self.len_rows)
                    ]
                )

            raise Exception("Matrix Error: {matrices aren't of the same size}")

        raise Exception("Matrix Error: {given argument is not a Matrix}")

    def __sub__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru - na odecitani matic """
        if isinstance(other_matrix, Matrix):
            if (other_matrix.len_rows == self.len_rows) and \
               (other_matrix.len_columns == self.len_columns):
                return Matrix(
                    [
                        [
                            self.matrix[i][j] - other_matrix.matrix[i][j]
                            for j in range(self.len_columns)
                        ]
                        for i in range(self.len_rows)
                    ]
                )

            raise Exception("Matrix Error: {matrices aren't of the same size}")

        raise Exception("Matrix Error: {given argument is not a Matrix}")

    def __rmul__(self, constant: int | float) -> 'Matrix':
        """ Pretizeni operatoru * na nasobeni matice konstantou """
        if isinstance(constant, int) or isinstance(constant, float):
            return Matrix(
                [
                    [
                        self.matrix[i][j] * constant
                        for j in range(self.len_columns)
                    ]
                    for i in range(self.len_rows)
                ]
            )

        raise Exception("Matrix Error: {constant must be an integer or float}")

    def __mul__(self, other_matrix: 'Matrix') -> 'Matrix':
        """ Pretizeni operatoru * na nasobeni matic """
        if isinstance(other_matrix, Matrix):
            if self.len_columns == other_matrix.len_rows:
                return Matrix(
                    [
                        [
                            sum(
                                [
                                    self.matrix[i][g]*other_matrix.matrix[g][j]
                                    for g in range(self.len_columns)
                                ]
                            )
                            for j in range(other_matrix.len_columns)
                        ]
                        for i in range(self.len_rows)
                    ]
                )

            raise Exception(
                "Matrix Error:"
                "{matrices aren't of compatible size for this operation}")

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
            return (
                (matrix.matrix[0][0] * matrix.matrix[1][1]) -
                (matrix.matrix[0][1] * matrix.matrix[1][0])
            )

        result = 0

        for j in range(matrix.len_columns):  # creates one new matrix
            new_matrix = self.det_slice(matrix, j)  # returns reduced matrix
            minor = (-1)**(1 + (j + 1)) * matrix.matrix[0][j]
            minor *= self.det_auxilary(new_matrix)

            result += minor

        return result

    def determinant(self) -> int | float:
        """ Vrati determinant matice """
        if self.len_rows == self.len_columns:
            if self.len_rows == 1:
                return self.matrix[0][0]

            return self.det_auxilary(self)

        raise Exception("Matrix Error: {matrix is not of a square shape}")

    def swap_rows(self, matrix, original_row_index, suitable_row_index):
        original_row = matrix.matrix[original_row_index]
        suitable_row = matrix.matrix[suitable_row_index]

        matrix.matrix[original_row_index] = suitable_row
        matrix.matrix[suitable_row_index] = original_row

        return matrix

    def find_non_zero(self, current_column, matrix_a, matrix_b):
        for i in range(current_column+1, matrix_a.len_rows):

            if matrix_a.matrix[i][current_column] != 0:
                # make a swap for both matrices (matrix_a, matrix_b)
                # and return the new matrices

                matrix_a = self.swap_rows(matrix_a, current_column, i)
                matrix_b = self.swap_rows(matrix_b, current_column, i)

                return matrix_a, matrix_b

        raise Exception("Matrix Error: {matrix doesn't have an inverse}")

    def inverse(self) -> 'Matrix':
        """ Vrati inverzni matici """
        if self.len_rows == self.len_columns:
            matrix_a = Matrix(self.matrix)
            matrix_b = self.identity_matrix(matrix_a.len_rows)

            for i in range(matrix_a.len_rows):
                if matrix_a.matrix[i][i] == 0:
                    matrix_a, matrix_b = self.find_non_zero(
                        i, matrix_a, matrix_b
                    )

                # dividing the entire row by the pivot element
                pivot = matrix_a.matrix[i][i]
                for j in range(matrix_a.len_columns):
                    matrix_a.matrix[i][j] /= pivot
                    matrix_b.matrix[i][j] /= pivot

                # subtracting multiples of the current row "i" from other rows
                # to get zeroes above and below the pivot of the current row

                for z in range(matrix_a.len_rows):
                    if z == i:
                        continue

                    if matrix_a.matrix[z][i] == 0:
                        continue

                    multiply_by = matrix_a.matrix[z][i]

                    # perform the operation of subtracting
                    # current row from the other one

                    performed_a = Matrix([matrix_a.matrix[z]]) - (
                        multiply_by * Matrix([matrix_a.matrix[i]])
                    )

                    matrix_a.matrix[z] = performed_a.matrix[0]

                    performed_b = Matrix([matrix_b.matrix[z]]) - (
                        multiply_by * Matrix([matrix_b.matrix[i]])
                    )

                    matrix_b.matrix[z] = performed_b.matrix[0]

            return matrix_b

        raise Exception("Matrix Error: {matrix is not of a square shape}")


class Matrix3D:
    def __init__(self, array: list[list[list[int]]]) -> None:
        """ Vytvoreni matice 3D"""

        standard_depth = len(array[0])
        standard_length = len(array[0][0])

        for depth in array:
            if len(depth) == standard_depth:
                for row in depth:
                    if len(row) == standard_length:
                        continue

                    raise Exception(
                        "Matrix Error: "
                        "{matrix doesn't have a consistent shape}")

            else:
                raise Exception(
                    "Matrix Error: "
                    "{matrix doesn't have a consistent shape}")

        self.matrix = array
        self.len_depth = len(array)
        self.len_rows = len(array[0])
        self.len_columns = len(array[0][0])

        def __eq__(self, other_matrix: object) -> bool:
            """ Pretizeni operatoru ==; tzn jestli se dve 3D matice rovnaji """
            if isinstance(other_matrix, Matrix3D):
                if (
                    other_matrix.len_depth == self.len_depth and
                    other_matrix.len_rows == self.len_rows and
                    other_matrix.len_columns == self.len_columns
                ):
                    return all(
                        self.matrix[z][i][j] == other_matrix.matrix[z][i][j]
                        for z in range(self.len_depth)
                        for i in range(self.len_rows)
                        for j in range(self.len_columns)
                    )
                return False

            return False

        def __ne__(self, other_matrix: object) -> bool:
            """ Pretizeni operatoru !=; tzn
            jestli jsou dve 3D matice rozdilne """

            if not isinstance(other_matrix, Matrix3D):
                return True

            if not (
                other_matrix.len_depth == self.len_depth and
                other_matrix.len_rows == self.len_rows and
                other_matrix.len_columns == self.len_columns
            ):
                return True

            return any(
                self.matrix[z][i][j] != other_matrix.matrix[z][i][j]
                for z in range(self.len_depth)
                for i in range(self.len_rows)
                for j in range(self.len_columns)
            )

    def determinant_3d(self) -> int:
        """ Vrati determinant 3D matice """
        if self.len_rows == self.len_columns == self.len_depth:
            if self.len_rows == 1:
                return self.matrix[0][0][0]

            return self.det_auxilary(self)

        raise Exception("Matrix Error: {matrix is not of a square shape}")

    def det_auxilary(self, matrix):
        if (matrix.len_rows == 2 and matrix.len_columns == 2 and
                matrix.len_depth == 2):
            return (
                (matrix.matrix[0][0][0] * matrix.matrix[1][1][1]) -
                (matrix.matrix[1][0][1] * matrix.matrix[0][1][0]) +
                (matrix.matrix[0][1][1] * matrix.matrix[1][0][0]) -
                (matrix.matrix[0][0][1] * matrix.matrix[1][1][0])
            )

        result = 0

        for i in range(matrix.len_rows):
            for j in range(matrix.len_columns):
                new_matrix = self.det_slice(matrix, i, j)

                sign = (-1) ** ((i + 1) + (j + 1) + 1)
                value = matrix.matrix[0][i][j]
                minor = sign * value * self.det_auxilary(new_matrix)

                result += minor

        return result

    def det_slice(self, matrix, anchor_i, anchor_j):
        all_layers = []
        for z in range(1, matrix.len_depth):
            layer = []

            for i in range(matrix.len_rows):
                if i == anchor_i:
                    continue

                row = []

                for j in range(matrix.len_columns):
                    if j == anchor_j:
                        continue

                    row.append(matrix.matrix[z][i][j])

                layer.append(row)

            all_layers.append(layer)

        return Matrix3D(all_layers)
