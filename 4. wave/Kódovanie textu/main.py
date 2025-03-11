from typing import List
   
# Urob Túto funkciu
def encode_karlik(code_point: int) -> List[int]:
    bytes = []

    binary_code = bin(code_point)[2:]
    binary_length = len(binary_code)

    amnt_data_bytes = binary_length // 7

    
    amnt_remaining_bits = binary_length - (amnt_data_bytes * 7)

    byte_head_length = amnt_data_bytes + 1 + 1
    

    for _ in range(amnt_data_bytes):
        byte = "0" + binary_code[-7:]
        binary_code = binary_code[:-7]

        bytes.append(byte)


    # head-first byte
    byte = ""
    for _ in range(byte_head_length-1):
        byte += "1"
    byte += "0"


    for _ in range(8 - (byte_head_length + amnt_remaining_bits)):
        byte += "0"

    byte += binary_code
    bytes.append(byte)


    for i in range(len(bytes)):
        bytes[i] = int(bytes[i], 2)

    return bytes[::-1]
