#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []

        def _bactrack(s: str, i: int, partitions: list[str]):
            if len(s) == 0:
                ans.append(partitions[:])
                return

            for i in range(len(s)):
                str_part = s[0 : i + 1]
                if str_part == str_part[::-1]:
                    partitions.append(str_part)
                    _bactrack(s[i + 1 :], i + 1, partitions)
                    partitions.pop()

        _bactrack(s, 0, [])

        return ans

# @lc code=end
