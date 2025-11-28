def two_pointer(arr: list[int], target: int) -> tuple[int, int]:

    i, j = 0, len(arr) - 1

    while i < j:
        curr_sum = arr[i] + arr[j]

        if curr_sum == target:
            return arr[i], arr[j]
        elif curr_sum > target:
            j -= 1
        else:
            i += 1
    return -1, -1

arr = [20, 40, 50, 75, 120, 145, 200]
print(two_pointer(arr, 60))