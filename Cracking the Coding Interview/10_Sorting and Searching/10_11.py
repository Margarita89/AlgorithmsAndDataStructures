# Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
# to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers.
# For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys.
# Given an array of integers, sort the array into an alternating sequence of peaks and valleys.


# partition around pivot
def partition(arr, start, end):
    pivot = arr[start]
    j = 0
    for i in range(start + 1, end + 1):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[start], arr[j] = arr[j], arr[start]
    return j + 1


# quick sort
def quick_sort(arr, start, end):
    if start < end:
        ind = partition(arr, start, end)
        quick_sort(arr, start, ind - 1)
        quick_sort(arr, ind + 1, end)


def peaks_and_valleys(arr):
    quick_sort(arr, 0, len(arr) - 1)
    print('Sorted Array : ', arr)
    half = len(arr) // 2
    # swap every couple
    for i in range(0, half, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == "__main__":
    arr = [5, 3, 1, 2, 3]
    print('Initial array:', arr)
    print('Array with peaks and valleys', peaks_and_valleys(arr))
