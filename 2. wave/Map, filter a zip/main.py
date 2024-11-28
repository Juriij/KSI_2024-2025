from typing import Iterator
from math import floor


def process_purchase(
    prices: list[float],
    items: list[str],
    tax: int,
    food_filter: str | None = None,
) -> Iterator[tuple[str, int]]:
    
    connected_list = list(zip(items, prices))

    if food_filter != None:
        connected_list = list(filter(lambda x: x[0] != food_filter, connected_list))

    
    taxed_list = map(lambda x: (x[0], floor(x[1] + (x[1]*tax)/100)), connected_list)

    return taxed_list
    



# Základní testy:
assert list(process_purchase([15, 24, 67], ["water", "eggs", "ham"], 21)) == [
    ("water", 18),
    ("eggs", 29),
    ("ham", 81),
]
assert list(
    process_purchase([15, 24, 67], ["water", "eggs", "ham"], 21, "water")
) == [("eggs", 29), ("ham", 81)]
