# Vytvoř set comprehension, který z textu získá unikátní samohlásky
# (Pro lidi co nikdy neslyšeli, že 'y' je samohláska - tak jako já. Tak je...)
# Takze pro "Karlik je COOL", vratí:
# {
#   a, e, i, o
# }

def unique_vowels(s: str)-> set[str]:
    return {letter.lower() for letter in s  if letter.lower() in {"a", "i", "u", "e", "o", "y"}}


assert unique_vowels("Karlik je COOL") == {'a', 'e', 'i', 'o'}, "Test case 1 failed"

assert unique_vowels("hello world") == {'e', 'o'}, "Test case 2 failed"

assert unique_vowels("AEIOUaeiou") == {'a', 'e', 'i', 'o', 'u'}, "Test case 3 failed"

assert unique_vowels("bcdfghjklmnpqrstvwxyz") == {'y'}, "Test case 4 failed"

