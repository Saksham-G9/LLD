def merge_sort(nums: list[int]):

    def helper(nums: list[int]):
        if len(nums) == 1:
            return nums[:]

        mid = len(nums) // 2

        left_part = helper(nums[:mid])
        right_part = helper(nums[mid:])

        i, j = 0, 0
        res = []
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                res.append(left_part[i])
                i += 1
            else:
                res.append(right_part[j])
                j += 1

        res.extend(left_part[i:])
        res.extend(right_part[j:])

        return res

    return helper(nums)

    


nums = [12, 31, 35, 8, 32, 17]
print(merge_sort(nums))
