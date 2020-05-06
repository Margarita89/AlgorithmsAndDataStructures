# Flip Bit to Win: You have an integer and you can flip exactly one bit from a O to a 1.
# Write code to find the length of the longest sequence of 1 s you could create.
# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8


def flipBitToWin(num):
    # if all bits are 1's
    if (~num) == 0:
        return num.bit_length()

    print(bin(num)[2:])
    prev_len = 0
    cur_len = 0
    max_len = 0

    while num:
        # if the last bit in num is 1
        if (num & 1) == 1:
            cur_len += 1
        # if the last bit in num is 0
        else:
            # if the next bit is again 1
            if (num >> 1 & 1) == 1:
                prev_len = cur_len
            # if the next bit is still 0
            else:
                prev_len = 0
            cur_len = 0
        # right shift (remove last bit)
        num >>= 1
        # update max_len
        max_len = max(max_len, prev_len + cur_len + 1)
    return max_len


if __name__ == "__main__":
    num = 1775
    print(flipBitToWin(num))
