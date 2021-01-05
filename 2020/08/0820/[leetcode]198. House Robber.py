from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        DP = [0] * len(nums)
        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            DP[i] = max(DP[i-2] + nums[i], DP[i-1])
        return DP[-1]


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))
