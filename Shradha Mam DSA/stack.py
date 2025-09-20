from collections import deque


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# stockSpanner = StockSpanner()
# print(stockSpanner.next(100))  # return 1
# print(stockSpanner.next(80))  # return 1
# print(stockSpanner.next(60))  # return 1
# print(stockSpanner.next(70))  # return 2
# print(stockSpanner.next(60))  # return 1
# print(stockSpanner.next(75))  # return 1
# print(stockSpanner.next(85))  # return 1
# print(
#     stockSpanner.next(75)
# )  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# print(stockSpanner.next(85))  # return 6


class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mins.append(val)
        elif self.stack and val < self.mins[-1]:
            self.stack.append((val))
            self.mins.append(val)
        else:
            self.stack.append((val))
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        mapping = {"}": "{", "]": "[", ")": "("}
        i, j = 0, len(s) - 1

        while i < j:
            if mapping.get(s[j]) and mapping.get(s[j]) == s[i]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def nextGreaterElement(self, arr: list[int]):

        stack = []
        res = []

        for el in arr[::-1]:

            # if not stack:
            #     res.append(-1)
            #     continue
            while stack and stack[-1] < el:
                stack.pop()

            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(el)
        return res[::-1]

    def previous_smaller_element(self, arr: list[int]):

        stack = []
        ans = []

        for el in arr:

            while stack and stack[-1] > el:
                stack.pop()

            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])

            stack.append(el)

        return ans

    def largestRectangleArea(self, heights: list[int]) -> int:

        i, j = 0, len(heights) - 1
        res = float("-inf")

        while i <= j:
            if heights[i] == heights[j]:
                temp_res = heights[i]
                i += 1
                res = max(temp_res, res)
            elif heights[i] < heights[j]:
                temp_res = heights[i] * (j - i)
                res = max(temp_res, res)
                i += 1
            else:
                temp_res = heights[j] * (j - i)
                res = max(temp_res, res)
                j -= 1

        return res

    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        res = [-1] * len(nums)

        stack = []
        i = len(nums) - 1
        # Right Greater
        for el in nums[::-1]:
            while stack and stack[-1] < el:
                stack.pop()

            if not stack:
                res[i] = -1
                stack.append(el)

            else:
                res[i] = stack[-1]
                stack.append(el)
            i -= 1

        # Handling circular loop
        i = len(nums) - 1
        # Right Greater
        for el in nums[::-1]:
            while stack and stack[-1] <= el:
                stack.pop()

            if not stack:
                res[i] = -1
                stack.append(el)

            else:
                res[i] = stack[-1]
                stack.append(el)
            i -= 1

        return res

    def trap(self, height: list[int]) -> int:

        i = 1
        res = 0
        while i < len(height) - 1:
            left_max = right_max = float("-inf")
            # Left Max
            for j in range(0, i):
                left_max = max(left_max, height[j])
            # Right Max
            for j in range(i, len(height)):
                right_max = max(right_max, height[j])

            if min(left_max, right_max) - height[i] > 0:
                res += min(left_max, right_max) - height[i]

            i += 1
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()

res = sol.trap(height)
print(res)
