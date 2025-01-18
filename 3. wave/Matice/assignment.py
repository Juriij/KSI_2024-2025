class Matrix:
    def __init__(self, array: list[list[int | float]]) -> None:
        """ Vytvoreni matice """
        pass

    @staticmethod
    def zero_matrix(height: int, width: int) -> 'Matrix':
        """ Staticka metoda na vytvoreni nulove matice """
        pass

    @staticmethod
    def identity_matrix(side: int) -> 'Matrix':
        """ Staticka metoda na vytvoreni jednotkove matice """
        pass

    def __str__(self) -> str:
        """ Pretizeni operatoru __str__ na prevod matice na string """
        pass

    def __getitem__(self, tup: tuple[int, int]) -> int | float:
        """ Pretizeni getitemu na vypsani prvku matice """
        pass

    def __setitem__(self, tup: tuple[int, int], new_value: int | float) -> None:
        """ Pretizeni setitemu na nastaveni prvku matice """
        pass

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
