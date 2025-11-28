def binary_search(arr: list[int], target: int):

    def helper(start, end):
        if start > end:
            return -1

        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return helper(start, mid - 1)
        else:
            return helper(mid + 1, end)

    return helper(0, len(arr) - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 76))
