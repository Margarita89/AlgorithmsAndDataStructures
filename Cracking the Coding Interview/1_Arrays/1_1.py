# Is Unique: Implement an algorithm to determine if a string has all unique characters.

# uses set to check for repeating characters
# O(n) time and O(n) space
def isUnique(s):
    set_of_chars = set()
    for ch in s:
        if ch not in set_of_chars:
            set_of_chars.add(ch)
        else:
            return False
    return True

s = input()
if len(s) < 2:
    print(True)
else:
    print(isUnique(s))

