# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown number of times,
# write code to find an element in the array. You may assume that the array was originally sorted in increasing order.
# EXAMPLE
# Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)


def search_rotated_array(arr, val):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        # check if left half is sorted and if val is in left half
        if arr[mid] > arr[start]:
            if arr[mid] > val > arr[start]:
                end = mid - 1
            # if not in sorted half
            else:
                start = mid + 1
        # check if right half is sorted and if val is in right half
        else:
            if arr[mid] < val < arr[end]:
                start = mid + 1
            # if not in sorted half
            else:
                end = mid - 1
    # if val is not found
    return -1


if __name__ == "__main__":
    input_arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    elem = 5
    print('Input array:', input_arr)
    print('Element', elem, 'has index', search_rotated_array(input_arr, elem))
