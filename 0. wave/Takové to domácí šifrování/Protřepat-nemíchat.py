def encode(n: int, plain_text: str) -> str:     # vraci ciphertext typu String
    ciphertext = ""
    if plain_text != "":
        for i in range(0, len(plain_text), n):
            sliced = plain_text[i-n:i]
            ciphertext += sliced[::-1]
            last_i = i

        sliced = plain_text[last_i:]
        ciphertext += sliced[::-1]

    return ciphertext


def decode(n: int, cipher_text: str) -> str:    # vraci plaintext typu String
    plain_text = encode(n, cipher_text)

    return plain_text
