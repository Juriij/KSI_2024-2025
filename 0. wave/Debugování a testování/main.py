import string

translation_dict = dict([('a', '.-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'), ('e', '.'), ('f', '..-.'), ('g', '--.'), ('h', '....'), ('i', '..'), ('j', '.---'), ('k', '-.-'), ('l', '.-..'), ('m', '--'), ('n', '-.'), ('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'), ('s', '...'), ('t', '-') ,('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'), ('y', '-.--'), ('z', '--..'), (' ', ''), ('/', '-..-.'), ('-', '-....-'), ('.', '.-.-.-'), (',', '--..--'), (' ', ''), ("1", ".----"), ("2", "..---"), ("3", "...--"), ("4", "....-"), ("5", "....."), ("6", "-...."), ("7", "--..."), ("8", "---.."), ("9", "----."), ("0", "-----")])

alphabet = {}
morse = {}

for key, value in translation_dict.items():
    alphabet[key] = value
    morse[value] = key

def encode(plaintext: str) -> str:
    plaintext = plaintext.lower()
    morse_text = ""
    for char in plaintext:
        morse_text += alphabet[char] + "/"
    morse_text += "//"
    return morse_text

def decode(morse_text: str) -> str:
    morse_array = morse_text.split("/")
    plain_text = ""
    for i in morse_array:
        plain_text += morse[i]
    plain_text = plain_text[:-3]
    return plain_text
