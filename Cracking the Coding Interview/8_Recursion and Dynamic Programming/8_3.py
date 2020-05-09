# Magic Index: A magic index in an array A[ 1..n-1] is defined to be an index such that A[i] = i
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# Comment: talk about logic of returns

def magic_index(arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return magic_index(arr, mid+1, end)
    else:
        return magic_index(arr, start, mid-1)


if __name__ == "__main__":
    arr = [-20, -10, 0, 1, 4, 7, 18]
    print(magic_index(arr, 0, len(arr)-1))
