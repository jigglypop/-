from typing import *
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # result = []
        # num_counter = Counter(nums)
        # heap = []
        # for key, value in num_counter.items():
        #     heapq.heappush(heap, (-value, key))
        # for _ in range(k):
        #     v, k = heapq.heappop(heap)
        #     result.append(k)
        # return result
        return list(zip(*Counter(nums).most_common(k)))[0]


solution = Solution()
print(solution.topKFrequent([1, 2], 2))
