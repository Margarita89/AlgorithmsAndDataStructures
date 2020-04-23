# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

from collections import defaultdict

# created dict for a string = {ch1 : counter ch1, ch2 : counter ch2}
def updateDict(s):
    dicty = defaultdict(int)
    for ch in s:
        dicty[ch] += 1
    return dicty


# checks if s1 and s2 are permutations
def permutationCheck(s1, s2):
    # if strings have unequal length - they cannot be a permutation
    if len(s1) != len(s2):
        return False

    # put s1 into dict = {ch1 : counter ch1, ch2 : counter ch2}
    dict1 = updateDict(s1)

    # runs through 2nd string to check if there are chars in dict1
    for ch in s2:
        if ch not in dict1:
            return False
        else:
            dict1[ch] -= 1

    #check if all values in dict1 are zeros
    for key in dict1:
        if dict1[key] != 0:
            return False
    return True


if __name__ == "__main__":

    #s1 = 'asdf'
    #s2 = 'adfs'

    s1 = input()
    s2 = input()

    arr_s1 = [ch for ch in s1]
    arr_s2 = [ch for ch in s2]
    print(permutationCheck(arr_s1, arr_s2))

