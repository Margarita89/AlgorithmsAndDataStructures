# Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.


def group_anagrams(arr):

    res = []
    # create hashmap to check strings
    dicty = {}
    for ind, s in enumerate(arr):
        str_sorted = ''.join(sorted(s))
        if str_sorted not in dicty:
            dicty[str_sorted] = [ind]
        else:
            dicty[str_sorted].append(ind)

    for key in dicty:
        for i in range(len(dicty[key])):
            res.append(arr[dicty[key][i]])
    return res


if __name__ == "__main__":
    arr_str = ['cat', 'trol', 'act', 'fat', 'rolt', 'tac', 'man']
    print('Array of strings: ', arr_str)
    print("Sorted array so that all the anagrams are next to each other:")
    print(group_anagrams(arr_str))

