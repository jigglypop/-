from typing import *
import heapq
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        dist = collections.defaultdict(int)
        Q = [(0, src, K)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        return -1


solution = Solution()
print(solution.findCheapestPrice(
    3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
