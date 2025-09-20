from typing import List
from collections import Counter, defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for el, count in counts.items():
            if count > len(nums) / 2:
                return el

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        arr = [-1] * (len(grid) ** 2)
        missing_number = repeated_number = -1
        curr_sum = 0
        flag = False
        for row in grid:
            for col in row:
                if arr[col - 1] != -1:
                    repeated_number = col
                else:
                    arr[col - 1] = 1
                    curr_sum += col

        temp = 0
        for i in range(1, (len(grid) ** 2) + 1):
            temp += i

        missing_number = temp - curr_sum

        return repeated_number, missing_number

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p = len(nums1) - 1

        i, j = m - 1, n - 1

        while i >= 0 and j >= 0:

            if nums2[j] >= nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1

            p -= 1

        if i < 0:
            for k in range(j + 1):
                nums1[k] = nums2[k]

        return nums1


sol = Solution()
nums1 = [2, 0, 0]
m = 1
nums2 = [1, 1]
n = 2
print(sol.merge(nums1, m, nums2, n))
