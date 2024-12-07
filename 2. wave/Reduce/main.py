from bst import BST
from functools import reduce


def prod(array: list[int]) -> int:
    """
    Returns product of all items in array.
    """
    return reduce(lambda acc, x: acc * x, array, 1)


def odd_sum(array: list[int]) -> int:
    """
    Counts sum of all odd numbers in array.
    """
    return reduce(lambda acc, x: acc + x if (x % 2 != 0) else acc, array, 0)


def str_join(array: list[str]) -> str:
    """
    Joins all strings in array.
    """
    return reduce(lambda acc, x: acc + x, array, "")



def helper_max_absolute(acc, x):
    if acc < abs(x):
        return abs(x)
    
    else:
        return acc


def max_absolute_value(array: list[int]) -> int:
    """
    Returns maximal absolute value of array.
    If array is empty throws an exception.
    """
    if array == []:
        raise Exception
    
    return reduce(helper_max_absolute, array, 0)



def bst(array: list[int]) -> BST:
    """
    Add all items in array to binary search tree.
    You can create tree object by writing: tree = BST().
    You add item to tree by call: tree.add(item).
    """
    return reduce(lambda acc, item: acc.add(item), array, BST())


# tests
print(max_absolute_value([0,0,0]))