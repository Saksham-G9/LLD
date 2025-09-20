from typing import List
from collections import Counter
import math


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
        return i + 1, nums

    def rotate(self, nums: list[int], k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        return nums

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix = suffix = 1

        for i in range(1, len(nums)):
            prefix = prefix * nums[i - 1]
            res[i] = prefix

        for i in range(len(nums) - 2, -1, -1):
            suffix = suffix * nums[i + 1]
            res[i] = suffix

        return res

    def maxSubArray(self, nums):

        res = float("-inf")

        for i in range(len(nums)):
            curr_sum = 0

            for j in range(i, len(nums)):
                curr_sum += nums[j]
                res = max(res, curr_sum)
        return res

    def maxSubArray2(self, nums):

        res = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum += num
            res = max(curr_sum, res)
            curr_sum = 0 if curr_sum < 0 else curr_sum

        return res

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = []

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return -1

    def majorityElement(self, nums):

        counts = Counter(nums)

        print(counts)

    def maxProfit(self, prices):

        ans = i = 0

        for j in range(1, len(prices)):
            if prices[j] < prices[i]:
                i = j
            else:
                ans = max(prices[j] - prices[i], ans)
        return ans

    def maxArea(self, height):

        i, j = 0, len(height) - 1
        ans = 0

        while i < j:
            area = min(height[j], height[i]) * (j - i)

            ans = max(ans, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return ans

    def sort012(self, nums):
        nums_count = Counter(nums)

        i = 0

        for _ in range(nums_count.get(0)):
            nums[i] = 0
            i += 1

        for _ in range(nums_count.get(1)):
            nums[i] = 1
            i += 1

        for _ in range(nums_count.get(2)):
            nums[i] = 2
            i += 1

        return nums

    def dutch_flag(self, nums):
        i, j, k = 0, 0, len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        return nums

    def merge(nums1, m, nums2, n):
        n1_len = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[n1_len] = nums1[i]
                i -= 1
            else:
                nums1[n1_len] = nums2[j]
                j -= 1
            n1_len -= 1

        while j >= 0:
            nums1[n1_len] = nums2[j]
            j -= 1
            n1_len -= 1

    def isPalindrome(self, s: str):
        i, j = 0, len(s) - 1

        while i < j:

            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].casefold() != s[j].casefold():
                return False

            i += 1
            j -= 1

        return True

    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)

        for ch in s:
            stack.append(ch)
            if len(stack) >= m and "".join(stack[-m:]) == part:
                del stack[-m:]

        return "".join(stack)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        s1_freq = Counter(s1)
        window = Counter(s2[:len_s1])

        if window == s1_freq:
            return True

        for i in range(len_s1, len_s2):
            window[s2[i]] += 1
            window[s2[i - len_s1]] -= 1
            if window[s2[i - len_s1]] == 0:
                del window[s2[i - len_s1]]

            if window == s1_freq:
                return True

        return False

    def reverseWords(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

    def compress(self, chars):
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = [True] * n
        ans = 0
        for i in range(2, n):
            if counts[i]:
                ans += 1
                for j in range(i * 2, n, i):
                    counts[j] = False
        return ans

    def digits_in_number(self, num: int):
        count = 0
        sum = 0
        while num:
            sum += num % 10
            num = num // 10
            count += 1

        return count, sum

    def is_armstrong(self, num: int):
        sum_of_cubes = 0
        temp = num
        while temp:
            sum_of_cubes += (temp % 10) ** 3
            temp = temp // 10

        return sum_of_cubes == num

    def hcf(self, num1: int, num2: int):
        if num1 == num2:
            return num1

        res = 1
        for i in range(1, min(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                res = i

        return res

    def two_sum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for i, el in enumerate(nums):
            val = target - el
            if val in seen:
                return [i, seen.get(val)]
            else:
                seen[el] = i
        return [-1, -1]

    def findMissingAndRepeatedValues(self, grid):

        arr = [0] * (len(grid) ** 2)

        new_arr_sum = 0

        repeated_num = -1

        for num_list in grid:
            for el in num_list:
                val = el - 1
                if arr[val] != 0:
                    repeated_num = el
                else:
                    arr[val] = 1
                    new_arr_sum += el

        missing_num = -1

        for i, val in enumerate(arr):
            if val == 0:
                missing_num = i + 1

        return [repeated_num, missing_num]

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        fast, slow = 0, 0

        while True:

            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        fast = 0

        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast

    def three_sum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        unique_triplets = []

        for i, num in enumerate(nums):
            target = -num
            a, b = i + 1, len(nums) - 1

            while a < b:
                if nums[a] + nums[b] == target:
                    triplets = [nums[i], nums[a], nums[b]]
                    unique_triplets.append(triplets)
                    a += 1
                elif nums[a] + nums[b] > target:
                    b -= 1
                else:
                    a += 1
        return unique_triplets

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1
        return count

    def fact_n(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * self.fact_n(n - 1)

    def sum_n(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n + self.sum_n(n - 1)

    def fib_n(self, n, n1=0, n2=1, count=0):

        if count == n:
            return n1
        count += 1
        return self.fib_n(n, n2, n1 + n2, count)

    def array_sorted(self, nums: list[int]):
        if len(nums) <= 1:
            return True

        def helper(i=0):
            if i == len(nums) - 2:
                return nums[i] <= nums[i + 1]
            if nums[i] > nums[i + 1]:
                return False
            else:
                return helper(i + 1)

        return helper()

    def binary_search(self, nums: int, k: int) -> bool:

        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == k

        def helper(start=0, end=len(nums) - 1):
            if start > end:
                return False

            mid = (start + end) // 2
            if nums[mid] == k:
                return True
            if nums[mid] > k:
                return helper(start, mid - 1)

            return helper(mid + 1, end)

        return helper()

    def print_all_subsets(self, nums: list[int]):
        def helper(subs: list[int], res: list[list[int]], i: int = 0):
            if i == len(nums):
                res.append(subs[:])
                return

            subs.append(nums[i])
            helper(subs, res, i + 1)

            subs.pop()
            helper(subs, res, i + 1)

        res = []
        helper(subs=[], res=res)
        print(res)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(i: int, subset: list[int], res: list[int]):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            helper(i + 1, subset, res)
            subset.pop()
            idx = i + 1
            while idx < len(nums) and nums[idx] == nums[i]:
                idx += 1
            helper(idx, subset, res)

        res = []
        helper(0, [], res)
        print(res)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(i: int, combination: list[int], res: list[list[int]], target):
            if i == len(candidates) or target < 0:
                return
            if target == 0:
                res.append(combination[:])
                return

            combination.append(candidates[i])

            helper(i, combination, res, target - candidates[i])

            combination.pop()
            idx = i + 1
            while idx < len(candidates) and candidates[i] == candidates[idx]:
                idx += 1
            helper(idx, combination, res, target)

        res = []
        helper(0, [], res, target)

        print(res)

    def permute(self, nums: List[int]) -> List[List[int]]:

        nums_len = len(nums)
        ans = []

        def _backtrack(i: int):
            if i == nums_len:
                ans.append(nums[:])
                return

            for idx in range(i, nums_len):
                nums[idx], nums[i] = nums[i], nums[idx]  # swap
                _backtrack(i + 1)
                nums[idx], nums[i] = nums[i], nums[idx]  # undo swap

        _backtrack(0)
        return ans

    def permutation_str(self, val: str):

        char_list = list(val)

        def _backtracking(idx):
            if idx == len(char_list):
                print("".join(char_list), end=" ")
                return

            for i in range(idx, len(char_list)):
                char_list[i], char_list[idx] = char_list[idx], char_list[i]
                _backtracking(idx + 1)
                char_list[i], char_list[idx] = char_list[idx], char_list[i]

        return _backtracking(0)

    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []

        def _isSafe(board, row, col):
            # Check column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper-left diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # Check upper-right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == "Q":
                    return False

            return True

        def _backtrack(board: list[list[int]], row: int):
            if row == len(board):
                ans.append(["".join(row) for row in board])
                return

            for j in range(len(board)):
                if _isSafe(board, row, j):
                    board[row][j] = "Q"
                    _backtrack(board, row + 1)
                    board[row][j] = "."

        _backtrack(board, 0)
        return ans

    def solveSudoku(self, board: List[List[str]]) -> None:

        def isSafe(board: List[List[str]], row: int, col: int, val: int) -> bool:
            val = str(val)
            # check row
            for j in range(9):
                if board[row][j] == val:
                    return False

            # check col
            for i in range(9):
                if board[i][col] == val:
                    return False

            # check grid
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] == val:
                        return False
            return True

        def _backtrack(row, col):
            if row == 9:
                return True

            next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

            if board[row][col] != ".":
                return _backtrack(next_row, next_col)

            for num in range(1, 10):
                if isSafe(board, row, col, num):
                    board[row][col] = str(num)
                    if _backtrack(next_row, next_col):
                        return True
                    board[row][col] = "."

            return False

        _backtrack(0, 0)

    def rat_in_a_maze(self, maze: list[list[int]], n):
        ans = []

        def helper(row, col, path=""):
            # Base case: reached destination
            if row == col == n - 1:
                ans.append(path)
                return

            up, bottom, left, right = row - 1, row + 1, col - 1, col + 1

            # Mark visited
            maze[row][col] = 0

            # Explore all 4 directions
            if row - 1 >= 0 and maze[row - 1][col] == 1:
                helper(row - 1, col, path + "U")
            if row + 1 < n and maze[row + 1][col] == 1:
                helper(row + 1, col, path + "D")
            if col - 1 >= 0 and maze[row][col - 1] == 1:
                helper(row, col - 1, path + "L")
            if col + 1 < n and maze[row][col + 1] == 1:
                helper(row, col + 1, path + "R")

            # Backtrack (unmark visited)
            maze[row][col] = 1

        if maze[0][0] == 1:  # Only start if entry is open
            helper(0, 0)

        return ans

    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        start, end = 0, (len(grid) * len(grid)) - 1
        row, col = 0, 0
        for i in range(start, end):
            target = grid[row][col] + 1

            # 1st dir
            if (
                row - 2 >= 0
                and col + 1 < len(grid)
                and grid[row - 2][col + 1] == target
            ):
                row = row - 2
                col = col + 1

            # 2nd dir
            elif (
                row - 1 >= 0
                and col + 2 < len(grid)
                and grid[row - 1][col + 2] == target
            ):
                row = row - 1
                col = col + 2

            # 3rd dir
            elif (
                row + 1 < len(grid)
                and col + 2 < len(grid)
                and grid[row + 1][col + 2] == target
            ):
                row = row + 1
                col = col + 2

            # 4th dir
            elif (
                row + 2 < len(grid)
                and col + 1 < len(grid)
                and grid[row + 2][col + 1] == target
            ):
                row = row + 2
                col = col + 1

            # 5th dir
            elif (
                row + 2 < len(grid)
                and col - 1 >= 0
                and grid[row + 2][col - 1] == target
            ):
                row = row + 2
                col = col - 1

            # 6th dir
            elif (
                row + 1 < len(grid)
                and col - 2 >= 0
                and grid[row + 1][col - 2] == target
            ):
                row = row + 1
                col = col - 2

            # 7th dir
            elif row - 1 >= 0 and col - 2 >= 0 and grid[row - 1][col - 2] == target:
                row = row - 1
                col = col - 2

            # 8th dir
            elif row - 2 >= 0 and col - 1 >= 0 and grid[row - 2][col - 1] == target:
                row = row - 2
                col = col - 1

            else: 
                return False

        return True


sol = Solution()
grid = [
    [0, 11, 16, 5, 20],
    [17, 4, 19, 10, 15],
    [12, 1, 8, 21, 6],
    [3, 18, 23, 14, 9],
    [24, 13, 2, 7, 22],
]
print(sol.checkValidGrid(grid))
