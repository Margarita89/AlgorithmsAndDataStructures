# Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on)

def pairwiseSwap(num):
    if num.bit_length() <= 1:
        return num

    print(bin(num)[2:])

    even_bits = num & 0xAAAAAAAA    # 0xAAAAAAAA has 1 on even and 0 on odd bit places
    odd_bits = num & 0x55555555     # 0x55555555 has 0 on even and 1 on odd bit places

    # shift right the even_bits
    even_bits >>= 1

    # shift left the odd_bits
    odd_bits <<= 1

    return even_bits | odd_bits


if __name__ == "__main__":
    num = 178
    print(bin(pairwiseSwap(num))[2:])
