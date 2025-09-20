from typing import List
from collections import Counter, defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for el, count in counts.items():
            if count > len(nums) / 2:
                return el


sol = Solution()
nums = [3, 2, 3]
print(sol.majorityElement(nums))
