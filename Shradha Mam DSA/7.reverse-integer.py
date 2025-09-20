#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, num: int) -> int:
        num_str = str(num)

        if num < 0:

            reversed_str = "-" + num_str[1:][::-1]
        else:

            reversed_str = num_str[::-1]

        return int(reversed_str)


# @lc code=end
