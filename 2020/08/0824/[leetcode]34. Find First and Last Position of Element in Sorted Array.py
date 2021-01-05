from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def DFS(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                DFS(next_elements)
                prev_elements.pop()
        DFS(nums)
        return results


solution = Solution()
print(solution.permute([1, 2, 3]))
