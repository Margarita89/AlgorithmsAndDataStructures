# Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation.
# If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR:"


def binaryToString(num):
    if num > 1 or num < 0:
        return "ERROR"
    ans = "0" + "."
    while num > 0:
        if len(ans) >= 32:  # check condition on 32 characters
            print(ans)
            return "ERROR"
        num *= 2    # *2 to check if the next digit is 1:
        if num >= 1:
            ans += "1"
            num -= 1    # remove 1 from num to allow next multiplications
        else:
            ans += "0"
    return ans


if __name__ == "__main__":
    num = 0.625
    print(binaryToString(num))
    num = 0.72
    print(binaryToString(num))


