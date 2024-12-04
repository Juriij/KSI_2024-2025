# Implementuj funkci, která vygeneruje list listů j násobků n čísel.
# Kde hodnota na každé pozici, je výsledkem násobku její pozice v listech.
#
# Příklad (3, 3):
# [
#  [1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9],
# ]

def multiplication_table(n: int, j: int) -> list[list[int]]:
    return [ [ num*multiplier for multiplier in range(1, j+1) ] for num in range(1, n+1)]

assert multiplication_table(3, 3) == [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
], "Test case 1 failed"

assert multiplication_table(2, 2) == [
    [1, 2],
    [2, 4],
], "Test case 2 failed"

assert multiplication_table(3, 4) == [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
], "Test case 3 failed"

