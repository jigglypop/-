from typing import *
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(price-min_price, profit)
        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
