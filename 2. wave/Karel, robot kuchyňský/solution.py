from typing import Callable
from collections import Counter
import inspect

Bowl = list[str]
Action = Callable[[Bowl], Bowl] | \
         Callable[[Bowl, Bowl], Bowl] | \
         Callable[[Bowl, Bowl, Bowl], Bowl]


def add(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    return bowl_a + bowl_b


def boil(bowl_a: Bowl) -> Bowl:
    return ["°"+ingredience+"°" for ingredience in bowl_a]


def mix(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    result = []
    bowl_a_longer = False
    bowl_b_longer = False

    if len(bowl_a) <= len(bowl_b):
        iterate = len(bowl_a)
        bowl_b_longer = True

    else:
        iterate = len(bowl_b)
        bowl_a_longer = True

    for i in range(iterate):
        result.append(bowl_a[i])
        result.append(bowl_b[i])

    if bowl_a_longer:
        result = result + bowl_a[iterate:]

    elif bowl_b_longer:
        result = result + bowl_b[iterate:]

    return result


def cut(bowl_a: Bowl) -> Bowl:
    new_bowl = []
    for ingredience in bowl_a:
        if ingredience == "":
            new_bowl.append("")
        else:
            for i in range(0, len(ingredience), 2):
                new_bowl.append(ingredience[i:i+2])

    return new_bowl


def remove(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    bowl_a_counts = Counter(bowl_a)

    new_list = []

    for ingredient in bowl_b:
        if bowl_a_counts[ingredient] > 0:
            bowl_a_counts[ingredient] -= 1

        else:
            new_list.append(ingredient)

    return new_list


def sieve(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    result = []
    bowl_a_longer = False
    bowl_b_longer = False

    if len(bowl_a) <= len(bowl_b):
        iterate = len(bowl_a)
        bowl_b_longer = True

    else:
        iterate = len(bowl_b)
        bowl_a_longer = True

    for i in range(iterate):
        if len(bowl_a[i]) == len(bowl_b[i]):
            result.append(bowl_a[i])
            result.append(bowl_b[i])

        elif len(bowl_a[i]) > len(bowl_b[i]):
            result.append(bowl_b[i])

        else:
            result.append(bowl_a[i])

    if bowl_a_longer:
        result = result + bowl_a[iterate:]

    elif bowl_b_longer:
        result = result + bowl_b[iterate:]

    return result


def compress(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    new_list = []

    bowl_b = "".join(bowl_b)
    b_index = 0
    len_bowl_b = len(bowl_b)

    if len_bowl_b == 0:
        return bowl_a

    for ingredient in bowl_a:
        new_ingredient = ""

        for char in ingredient:
            new_char = char + bowl_b[b_index]
            new_ingredient += new_char

            b_index += 1
            if len_bowl_b / b_index == 1:
                b_index = 0

        new_list.append(new_ingredient)

    return new_list


def bake(bowl_a: Bowl, bowl_b: Bowl, bowl_c: Bowl) -> Bowl:
    longest_bowl = []
    new_bowl_a = []

    if len(bowl_a) == 0:
        return bowl_b + bowl_c

    if len(bowl_b) >= len(bowl_c):
        longest_bowl = bowl_b

    else:
        longest_bowl = bowl_c

    if len(longest_bowl) <= len(bowl_a):
        new_bowl_a = bowl_a[:len(longest_bowl)]

    else:
        remainder = len(longest_bowl) % len(bowl_a)

        for _ in range(len(longest_bowl) // len(bowl_a)):
            new_bowl_a.extend(bowl_a)

        new_bowl_a.extend(bowl_a[:remainder])

    return new_bowl_a + bowl_b + bowl_c


def cook(recipe: list[Bowl, Action]) -> Bowl:
    processing = True
    i = 0
    previous_recipe = recipe

    while processing:
        # success
        if len(recipe) == 1 and isinstance(recipe[0], list):
            return recipe[0]

        if i == len(recipe):
            # not success
            if recipe == previous_recipe:
                return []

            previous_recipe = recipe
            i = 0

        # main
        if callable(recipe[i]):
            func = recipe[i]
            sig = inspect.signature(func)
            params = sig.parameters

            segment = recipe[i+1:i+1+len(params)]

            enum = 0
            suitable = True
            for enum, arg in enumerate(segment):
                if isinstance(arg, list):
                    continue

                suitable = False
                break

            if suitable and len(params) == len(segment):
                new_bowl = func(*segment)
                recipe = recipe[:i] + [new_bowl] + recipe[i+1+len(params):]

            else:
                i += enum

        i += 1
