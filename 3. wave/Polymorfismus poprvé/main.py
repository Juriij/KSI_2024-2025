def advanced_mul(k: int, v: int | list[int]) -> int | list[int]:
    if isinstance(v, int):
        return k * v
    
    elif isinstance(v, list):
        return [elem * k for elem in v]
        

# Testy:
assert advanced_mul(2, 3) == 6
assert advanced_mul(4, 5) == 20
assert advanced_mul(2, [1, 5, 15]) == [2, 10, 30]
assert advanced_mul(3, [2, 4, 8]) == [6, 12, 24]
