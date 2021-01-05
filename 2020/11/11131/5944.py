import sys
from heapq import heappop, heappush
sys.stdin = open('5944.txt', 'r')

input = sys.stdin.readline
INF = sys.maxsize

m, n, s, e, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
