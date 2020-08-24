from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1
        for i in range(0, len(nums)):
            result.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            result[i] = result[i] * p
            p = p * nums[i]
        return result


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
