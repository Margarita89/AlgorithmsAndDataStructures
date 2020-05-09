# Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator (or / operator).
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations


def recursive_multiply(a, b):
    print('a, b:', a, b)
    if a == 0:
        return 0
    if a == 1:
        return b
    half_a = a >> 1
    half = recursive_multiply(half_a, b)
    if a % 2 == 0:
        return half + half
    return half + half + b


def min_multiply(a, b):
    if a > b:
        a, b = b, a
    return recursive_multiply(a, b)


if __name__ == "__main__":
    a = 7
    b = 6
    print(a, 'multiply', b, 'is', min_multiply(a, b))
