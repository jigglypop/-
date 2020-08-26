from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                result += profit
        return result


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
