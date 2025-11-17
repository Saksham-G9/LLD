def maxi_mini(arr) -> tuple[int, int]:
    def helper(start, end):
        if start == end:
            return arr[start], arr[start]

        mid = (start + end) // 2

        left_max, left_min = helper(start, mid)
        right_max, right_min = helper(mid + 1, end)

        return max(left_max, right_max), min(left_min, right_min)

    return helper(0, len(arr) - 1)


arr = [70, 20, 80, 60, 35]

print(maxi_mini(arr))
