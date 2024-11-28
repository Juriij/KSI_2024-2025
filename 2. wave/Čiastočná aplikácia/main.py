from functools import partial


max_zero = partial(max, default=0)  # TODO
round_two = partial(round, ndigits=2)  # TODO

# TESTY
assert max_zero([5, 2, 3]) == 5
assert max_zero([]) ==  0
assert round_two(12.3456) == 12.35
assert round_two(365) == 365
