from typing import *


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1) & set(nums2))

# 투포인터
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return list(result)


solution = Solution()
print(solution.intersection([1, 2, 2, 1], [2, 2]))
print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
