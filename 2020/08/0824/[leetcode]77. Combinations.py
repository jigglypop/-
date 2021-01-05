from typing import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [i+1 for i in range(n)]

        def comb(nums, k):
            for i in range(len(nums)):
                if k == 1:
                    yield [nums[i]]
                else:
                    for next in comb(nums[i+1:], k-1):
                        yield [nums[i]] + next
        for i in comb(nums, k):
            result.append(i)
        return result


solution = Solution()
print(solution.combine(4, 2))
