# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


# calculates number of letters in string and writes into dict
def UpdateDic(s):
    dicty = {}
    for i, ch in enumerate(s):
        if ch not in dicty:
            if ch != ' ':
                dicty[ch] = 1
        else:
            if ch != ' ':
                dicty[ch] += 1
    return dicty


# check if the string s is palindrome or not
def checkPalindromePermutations(s):
    dict = UpdateDic(s)
    counter_odd = 0

    for key in dict:
        # check how many letters are in string odd number of times (should be no more than 1)
        if dict[key] % 2 != 0:
            counter_odd += 1
            if counter_odd > 1:
                return False
    return True


if __name__ == "__main__":
    #s = input()
    s = "Tact Coa"
    # use s.lower() to return only lower cases
    arr_s = [ch for ch in s.lower()]
    print(checkPalindromePermutations(arr_s))

