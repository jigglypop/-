from typing import *


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     num_map = {}
    #     for i, num in enumerate(nums):
    #         num_map[num] = i
    #     for i, num in enumerate(nums):
    #         if target-num in num_map and i != num_map[target-num]:
    #             return nums.index(num), num_map[target-num]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9,))
