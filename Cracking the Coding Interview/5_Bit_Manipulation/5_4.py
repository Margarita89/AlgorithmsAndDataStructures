# Next Number: Given a positive integer, print the next smallest
# and the next largest number that have the same number of 1 bits in their binary representation.


def nextNumber(num):
    if num == 0:
        return "No Answer"
    # find position of first 1 from left - it exists
    return largestNumber(num), smallestNumber(num)


def largestNumber(num):
    mask = num
    first_one_ind = 0
    while mask:
        if mask & 1 == 1:
            break
        mask >>= 1
        first_one_ind += 1

    # find position of first 0 from left after first 1
    first_zero_ind = first_one_ind
    while mask:
        if mask & 1 == 0:
            break
        mask >>= 1
        first_zero_ind += 1

    # check if position for 0 was found
    if mask:
        # insert 1 at position first_zero_ind
        next_large = num | (1 << first_zero_ind)
        # remove 1
        next_large &= ~(1 << first_one_ind)
    else:
        # insert 1 in front
        next_large = num | 1 << num.bit_length()
        # remove 1 (previous first 1)
        next_large &= ~(1 << (num.bit_length()-1))
    return next_large


def smallestNumber(num):
    mask = num
    first_zero_ind = 0
    while mask:
        if mask & 1 == 0:
            break
        mask >>= 1
        first_zero_ind += 1
    if not mask:
        return "No Answer"

    # find position of first 1 from left after first 0
    first_one_ind = first_zero_ind
    while mask:
        if mask & 1 == 1:
            break
        mask >>= 1
        first_one_ind += 1

    # insert 1 at position first_zero_ind
    next_small = num | (1 << first_zero_ind)
    # remove 1
    next_small &= ~(1 << first_one_ind)

    return next_small


if __name__ == "__main__":
    num = 13
    print('Binary representation of', num, 'is:', bin(num)[2:])
    num1, num2 = nextNumber(num)
    if str(num1).isdigit():
        print('Next largest number from', num, 'is:', bin(num1)[2:])
    else:
        print('No Answer')
    if str(num2).isdigit():
        print('Next smallest number from', num, 'is:', bin(num2)[2:])
    else:
        print('No Answer')
