
def generate_substrings(s: str):
    n = 0
    while True:
        substrings = set()
        for i in range(len(s)-n+1):  
            substrings.add(s[i: i+n])  

        if not substrings:  
            break

        yield substrings
        n += 1


# Testy:
iterator = generate_substrings("tuč")
print(next(iterator))  # {""}
print(next(iterator))  # {"t", "u", "č"}
print(next(iterator))  # {"tu", "uč"}
print(next(iterator))  # {"tuč"}
print(next(iterator))