# String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, sl and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# (e.g.,"waterbottle" is a rotation of"erbottlewat").

def StringRotation(a, b):
    s = a + a
    return isSubstring(s, b)

s1 = input()
s2 = input()
if len(s1) != len(s2):
    print(False)
else:
    StringRotation(s1, s2)
