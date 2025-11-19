arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]


def merge_sort(arr):
    '''
    k -> size of arr
    TC -> O(K log N)
    SC -> O(1)
    '''
    def helper(start, end):
        if start >= end:
            return arr[start]

        mid = start + (end - start) // 2

        left_part = helper(start, mid)
        right_part = helper(mid + 1, end)

        res = []
        res.extend(left_part)
        res.extend(right_part)

        res.sort()

        return res

    return helper(0, len(arr) - 1)


print(merge_sort(arrays))
