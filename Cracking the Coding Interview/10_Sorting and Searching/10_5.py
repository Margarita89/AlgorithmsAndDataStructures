# Sparse Search: Given a sorted array of strings that is interspersed with empty strings,
# write a method to find the location of a given string.


def sparse_search(arr, s):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == s:
            return mid
        # if arr[mid] is not empty - then common binary search
        if arr[mid] != '':
            if arr[mid] > s:
                end = mid - 1
            else:
                start = mid + 1
        # if arr[mid] is empty - find nearest non-empty indexes and compare
        else:
            mid_left = mid_right = mid
            # find nearest non-empty string on the left
            while arr[mid_left] == '' and mid_left >= start:
                mid_left -= 1
                if arr[mid_left] == s:
                    return mid_left
            # find nearest non-empty string on the right
            while arr[mid_right] == '' and mid_right <= end:
                mid_right += 1
                if arr[mid_right] == s:
                    return mid_right
            # check if s on the right
            if arr[mid_right] != '' and arr[mid_right] < s:
                start = mid_right + 1
            # check if s on the left
            elif arr[mid_left] != '' and arr[mid_left] > s:
                end = mid_left - 1
            else:
                return -1
    return -1


if __name__ == "__main__":
    arr = ['at', '', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
    s = 'ball'
    ans = sparse_search(arr, s)
    if ans == -1:
        print('Element was not found')
    else:
        print('Index : ', ans)
