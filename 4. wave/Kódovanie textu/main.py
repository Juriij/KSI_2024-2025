from typing import List


def convert_to_binary(num: int) -> str:
    binary = ""
    while True:
        remainder = num % 2
        binary += str(remainder)

        if num // 2 == 0:
            break 

        num = num // 2

    return binary[::-1]


# Urob Túto funkciu
def encode_karlik(code_point: int) -> List[int]:
    bytes = []
    binary_code = convert_to_binary(code_point)

    b = len(binary_code) // 7

    amount_remaining_bits = len(binary_code) - b*7


    if amount_remaining_bits <= (8 - b+2):  # no need for extra byte
        for i in range(b+1):
            byte = ""

            if i == 0:
                byte = "0" + binary_code[:(8-(b+2))]
                length_byte = len(byte)
                binary_code = binary_code[(8-(b+2)):]

                print(f'this is first preprocessed byte: {byte}')

                for j in range(8 - length_byte):
                    byte = "1" + byte

                print(f'this is first byte: {byte}')


            else:
                byte += "0"
                byte += binary_code[:7]
                binary_code = binary_code[7:]


            decimal = int(byte, base=2)
            bytes.append(decimal)


    else:  # we need extra byte
        for i in range(b+2):
            byte = ""

            if i == 0:
                byte = "0" + binary_code[:(8-(b+2))]
                length_byte = len(byte)
                binary_code = binary_code[(8-(b+2)):]

                # print(f'this is first preprocessed byte: {byte}')
                
                for j in range(8 - length_byte):
                    byte = "1" + byte

                # print(f'this is first byte: {byte}')

            else:
                byte += "0"
                byte += binary_code[:7]
                binary_code = binary_code[7:]


            decimal = int(byte, base=2)
            bytes.append(decimal)


    return bytes



    





print(encode_karlik(95))  # [192, 95]
print(" ".join(bin(b)[2:].rjust(8, "0") for b in encode_karlik(95)))  # 11000000 01011111
# print(encode_karlik(33))  # [161]
# print(" ".join(bin(b)[2:].rjust(8, "0") for b in encode_karlik(33)))  # 10100001
# print(encode_karlik(256))  # [194, 0]
# print(" ".join(bin(b)[2:].rjust(8, "0") for b in encode_karlik(256)))  # 11000010 00000000
