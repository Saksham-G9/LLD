class Solution:
    def trap(self, height: list[int]) -> int:
        left_max = right_max = float("-inf")
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                if left_max - height[l] > 0:
                    ans += left_max - height[l]
                l += 1
            else:
                if right_max - height[r]:
                    ans += right_max - height[r]
                r -= 1

        return ans


sol = Solution()
height = [4, 2, 0, 3, 2, 5]
print(sol.trap(height))
