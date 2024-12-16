#!/usr/bin/python3

from typing import Generator, List, Any
from types import GeneratorType


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
        





def password_generator(length: int) -> Generator[str, None, None]:
    # same numbers
    for i in range(10):
        yield str(i) * length

    # ascending order
    for i in range(length-1, 10):
        numbers = range(i - (length - 1), i + 1)

        result = ''.join(str(num) for num in numbers)
        yield result


    # descending order
















def generator_of_generators() -> Generator[Generator[int, None, None], None, None]:
    pass


def primes_generator() -> Generator[int, None, None]:
    pass
