def partition(nums, start, end):
    pivot = nums[end]  # choose last element as pivot
    idx = start - 1

    for j in range(start, end):
        if nums[j] < pivot:
            idx += 1
            nums[idx], nums[j] = nums[j], nums[idx]

    # place pivot in correct position
    idx += 1
    nums[idx], nums[end] = nums[end], nums[idx]
    return idx


def quick_sort(nums: list[int], start: int, end: int):
    if start < end:
        pivotIdx = partition(nums, start, end)
        quick_sort(nums, start, pivotIdx - 1)
        quick_sort(nums, pivotIdx + 1, end)


nums = [12, 31, 35, 8, 32, 17]
quick_sort(nums, 0, len(nums) - 1)
print(nums)  # ✅ [8, 12, 17, 31, 32, 35]
