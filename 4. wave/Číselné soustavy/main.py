# Tuto funkci implementuj.
def get_parity(x: int) -> bool:
    binone_count = 0

    while True:
        binone_count += x % 2

        if x // 2 == 0:
            break

        x = x // 2


    return False if binone_count % 2 == 0 else True




# Testy:
assert get_parity(0b10) == True
assert get_parity(0b11) == False
assert get_parity(0b1011) == True
assert get_parity(0b10101010) == False
