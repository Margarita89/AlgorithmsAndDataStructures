# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.


def sorted_merge(arr_a, arr_b):
    # counters for global arr_a, elements in arr_a and elements in arr_b
    i, j, k = len(arr_a) - 1, len(arr_a) - len(arr_b) - 1, len(arr_b) - 1

    while j >= 0 and k >= 0:
        if arr_a[j] > arr_b[k]:
            arr_a[i] = arr_a[j]
            j -= 1
        else:
            arr_a[i] = arr_b[k]
            k -= 1
        i -= 1
    while k >= 0:
        arr_a[i] = arr_b[k]
        i -= 1
        k -= 1
    return arr_a


if __name__ == "__main__":
    size_a = 10
    size_b = 4
    arr_a = [0] * size_a
    arr_b = [0] * size_b

    for i in range(size_a - size_b):
        arr_a[i] = i * 15
    print(arr_a)
    for i in range(size_b):
        arr_b[i] = 10 + i * 10
    print(arr_b)
    print(sorted_merge(arr_a, arr_b))
