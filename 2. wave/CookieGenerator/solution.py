#!/usr/bin/python3

from typing import Generator, List, Any
from types import GeneratorType
from itertools import product


def generator_connector(generators_list: List[Generator[Any, None, None]]) -> Generator[Any, None, None]:
    for generator in generators_list:
        if not isinstance(generator, GeneratorType):
            continue

        for value in generator:
            yield value






def fibonacci_generator() -> Generator[int, None, None]:
    x1 = 0
    x2 = 1

    yield x2

    while True:
        result = x1 + x2
        yield result

        x1 = x2
        x2 = result
        







def is_ascending(combo):
    for i in range(1, len(combo)):
        if combo[i] - 1 == combo[i-1]:
            continue

        return False
    
    return True



def is_descending(combo):
    for i in range(1, len(combo)):
        if combo[i] + 1 == combo[i-1]:
            continue

        return False
    
    return True


def password_generator(length: int) -> Generator[str, None, None]:
    # same numbers
    for i in range(10):
        yield str(i) * length


    if not length == 1:
        # ascending order
        for i in range(length-1, 10):
            numbers = range(i - (length - 1), i + 1)

            result = ''.join(str(num) for num in numbers)
            yield result


        # descending order
        for i in range(length-1, 10):
            numbers = range(i, i-length, -1)

            result = ''.join(str(num) for num in numbers)
            yield result


        # the rest
        for combo in product(range(10), repeat=length):
            if len(set(combo)) == 1:
                continue

            elif is_ascending(combo) or is_descending(combo):
                continue

            result = ''.join(str(x) for x in combo)

            yield result

    
    







def generator_of_generators() -> Generator[Generator[int, None, None], None, None]:
    pass


def primes_generator() -> Generator[int, None, None]:
    pass
