from typing import *
import bisect


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         index = bisect.bisect_left(nums, target)
#         if index < len(nums) and nums[index] == target:
#             return index
#         else:
#             return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))
print(solution.search([-1, 0, 3, 5, 9, 12], 2))
