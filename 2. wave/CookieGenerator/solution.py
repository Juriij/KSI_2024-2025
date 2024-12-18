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









def multiples(base_num):
    multiplicant = 1
    
    while True:
        yield base_num * multiplicant
        multiplicant += 1

    

def generator_of_generators() -> Generator[Generator[int, None, None], None, None]:
    n = 1
    while True:
        yield multiples(n)
        n += 1
    








def primes_generator() -> Generator[int, None, None]:
    limit = 10_000  
    base_primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  
    
    for i in range(2, limit + 1):
        if sieve[i]:
            base_primes.append(i)
            for multiple in range(i * i, limit + 1, i):
                sieve[multiple] = False
    

    for prime in base_primes:
        yield prime


    segment_start = limit + 1
    segment_size = 100_000 

    while True:
        segment_end = segment_start + segment_size - 1
        segment = [True] * (segment_size)


        for prime in base_primes:
            start = max(prime * prime, (segment_start + prime - 1) // prime * prime)
            for multiple in range(start, segment_end + 1, prime):
                segment[multiple - segment_start] = False


        for i in range(segment_size):
            if segment[i]:
                yield segment_start + i


        segment_start += segment_size
