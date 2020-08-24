from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def DFS(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                DFS(i+1, path+[nums[i]])

        DFS(0, [])
        return result


solution = Solution()
print(solution.subsets([1, 2, 3]))
