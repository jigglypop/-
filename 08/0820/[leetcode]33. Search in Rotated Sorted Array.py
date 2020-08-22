from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))

        if nums[pivot] == target:
            return pivot
        else:
            if nums[0] > target:
                left, right = pivot + 1, len(nums)-1
            elif pivot == 0:
                left, right = pivot + 1, len(nums)-1
            else:
                left, right = 0, pivot-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


solution = Solution()
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 5))
# print(solution.search([1], 0))
print(solution.search([1, 3], 3))
