# Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000.
# The array may have duplicate entries and you do not know what N is.
# With only 4 kilobytes of memory available, how would you print all duplicate elements in the array?

import random


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print('Sorted array:', arr)
    return arr


def find_dup(arr):
    arr_sort = bubble_sort(arr)
    print('Duplicates: ', end='')
    equal = None
    for i in range(len(arr_sort) - 1):
        if arr_sort[i] == arr_sort[i + 1]:
            # print previous equal
            if equal and equal != arr_sort[i]:
                print(equal, end=' ')
            equal = arr_sort[i]
    # print last equal
    if equal:
        print(equal, end=' ')


if __name__ == "__main__":
    arr = []
    N = 60
    for i in range(N):
        arr.append(random.randint(0, N))
    print('Initial array: ',arr)
    find_dup(arr)
