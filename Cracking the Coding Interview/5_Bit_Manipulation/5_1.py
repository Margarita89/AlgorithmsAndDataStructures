# Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j.
# Write a method to insert M into N such that M starts at bit j and ends at bit i.
# You can assume that the bits j through i have enough space to fit all of M.
# That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
# You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.


def Insertion(n, m, i, j):
    # should return 111 and (j+1)0's
    mask_beg = -1 << j + 1

    # should return 111 (j-i+1)0's 111
    mask_end = (2 ** i) - 1     # or mask_end = 1 << (i+1) - 1

    mask = mask_beg | mask_end
    n &= mask

    # shift m by i bits
    m <<= i

    # add n to m
    n |= m
    return n


def main():
    n = 1024
    m = 19
    i = 2
    j = 6
    print('n : ', bin(n)[2:])
    print('m : ', bin(m)[2:])
    n_ans = Insertion(n, m, i, j)
    print(bin(n_ans)[2:])

if __name__ == "__main__":
    main()
