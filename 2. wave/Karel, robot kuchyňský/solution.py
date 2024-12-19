from typing import Callable

Bowl = list[str]
Action = Callable[[Bowl], Bowl] | \
         Callable[[Bowl, Bowl], Bowl] | \
         Callable[[Bowl, Bowl, Bowl], Bowl]


def add(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    return bowl_a + bowl_b




def boil(bowl_a: Bowl) -> Bowl:
    return [ "°" + ingredience + "°"  for ingredience in bowl_a]





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
    pass


















def bake(bowl_a: Bowl, bowl_b: Bowl, bowl_c: Bowl) -> Bowl:
    pass



def remove(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    pass


def compress(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    pass


def sieve(bowl_a: Bowl, bowl_b: Bowl) -> Bowl:
    pass


def cook(recipe: list[Bowl, Action]) -> Bowl:
    pass