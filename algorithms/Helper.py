def calculate_number_from_bits(bits: list):
    number = 0
    for i, bit in enumerate(bits[::-1]):
        number += bit * (2 ** i)
    return number