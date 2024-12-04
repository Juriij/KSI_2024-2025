# Implementuj funkci, která vratí slovník obsahující počet každého znaku
# ze zadaného textu.
#
# Pro: "Karlik je COOL"
# Vratí:
# {
#   K: 1,
#   a: 1,
#   r: 1,
#   l: 1,
#   i: 1
#   k: 1
#   " ": 2
#   j: 1
#   e: 1
#   C: 1
#   O: 2
#   L: 1
# }


def char_count(s: str) -> dict[str, int]:
    return { letter:s.count(letter) for letter in s}


assert char_count("Karlik je COOL") == {
    'K': 1,
    'a': 1,
    'r': 1,
    'l': 1,
    'i': 1,
    'k': 1,
    ' ': 2,
    'j': 1,
    'e': 1,
    'C': 1,
    'O': 2,
    'L': 1,
}, "Test case 1 failed"

assert char_count("hello world") == {
    'h': 1,
    'e': 1,
    'l': 3,
    'o': 2,
    ' ': 1,
    'w': 1,
    'r': 1,
    'd': 1,
}, "Test case 2 failed"

assert char_count("") == {}, "Test case 3 failed"

