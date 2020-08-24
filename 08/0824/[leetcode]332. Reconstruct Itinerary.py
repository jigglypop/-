from typing import *
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        way = []

        def DFS(start):
            while graph[start]:
                DFS(graph[start].pop())
            way.append(start)
        DFS("JFK")
        return way[::-1]


solution = Solution()
print(solution.findItinerary(
    [["MUC", "LHR"],  ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
