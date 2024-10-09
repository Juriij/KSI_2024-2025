def decrypt(key, cyphertext):
    plain_text = ""
    for i in range(len(cyphertext)):
        for j in cyphertext:
            if j[0] == i:
                for letter in j[1]:
                    plain_text += key[letter]
                    
                plain_text += " "
                break
    
    plain_text = plain_text[:-1]
    plain_text += "."

    return plain_text



# Testy:
key = {"a": "c", "b": "d","c": "e","d": "g", "e": "f", "f": "i", "g": "l", "h": "q", "i": "u", "j": "w", "k": "v", "l": "k", "m": "t", "n": "z", "o": "h", "p": "j", "q": "a", "r": "m", "s": "x", "t": "o", "u": "b", "v": "n", "w": "r", "x": "s", "y": "p", "z": "y"}

print(decrypt(key, [(1, "xkcmc"), (0, "qotp")]))  # "ahoj svete."
print(decrypt(key, [(0, "lqwgfl")]))  # "karlik."
print(decrypt(key, []))  # .
print(decrypt(key, [(0, 'rincrc'), (1, 'xytgi'), (2, 'mqpvc'), (3, 'ltrivfltkqm')]))  # "muzeme spolu tajne komunikovat."
print(decrypt(key, [(2, 'nbq'), (4, 'vcywcltvqmcgvq'), (0, 'xfewq'), (1, 'xc'), (3, 'uzm')]))  # "sifra se zda byt neprekonatelna."
