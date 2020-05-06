# Conversion: Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2

def Conversion(a, b):
    print('a:', bin(a)[2:])
    print('b:',bin(b)[2:])
    convert_count = 0
    # swap to make a longer or equal to b
    if a.bit_length() < b.bit_length():
        a, b = b, a

    while b:
        if b & 1 != a & 1:
            convert_count += 1
        b >>= 1
        a >>= 1

    if a:
        convert_count += a.bit_length()

    return convert_count


if __name__ == "__main__":
    a = 29
    b = 15
    print('Number of conversions:', Conversion(a, b))
