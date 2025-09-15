def count_inversion(nums, i=0, count=0):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1

    return count


def count_inversion_using_ms(nums, start, end, count=0):

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
                count += len(right_part) - j - 1
                j += 1

        res.extend(left_part[i:])
        res.extend(right_part[j:])

        return res

    return helper(nums)


nums = [6, 3, 5, 2, 7]
print(count_inversion_using_ms(nums, 0, len(nums)))
