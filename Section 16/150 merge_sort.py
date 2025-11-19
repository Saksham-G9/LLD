from typing import List


def merge_sort(arr: List[int]) -> None:
    """
    Sorts the input list of integers in place using the merge sort algorithm.
    Modifies the original list.
    """

    def helper(start, end):
        if start >= end:
            return

        mid = start + (end - start) // 2
        helper(start, mid)
        helper(mid + 1, end)

        # Merge the two sorted halves in place
        temp = []
        i, j = start, mid + 1

        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        # Copy remaining elements
        temp.extend(arr[i : mid + 1])
        temp.extend(arr[j : end + 1])

        # Copy sorted temp back to arr
        arr[start : end + 1] = temp

    if arr:
        helper(0, len(arr) - 1)


arr = [10, 30, 20, 40, 5, 60]

print(merge_sort(arr))
