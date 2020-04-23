# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# perform string compression
def stringCompression(s):
    counter = 1
    res = ''
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            counter += 1
        else:
            res = res + s[i] + str(counter)
            counter = 1
    # the last char was not added, add it now
    res = res + s[-1] + str(counter)
    return res


if __name__ == "__main__":
    s = 'aabcccccaaba'
    #s = input()
    if len(s) <= 1:
        print(s)
    else:
        #arr_s = [ch for ch in s]
        print(stringCompression(s))
        #print(*arr, sep='')
