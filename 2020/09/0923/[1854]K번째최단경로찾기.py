import sys
from heapq import heappop, heappush
sys.stdin = open('1854.txt', 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))

path = [[] for _ in range(n)]
heap = []
heappush(path[0], 0)
heappush(heap, (0, 0))

while heap:
    cur_d, now = heappop(heap)
    for i in range(len(graph[now])):
        nxt, nxt_d = graph[now][i]
        nxt_d += cur_d
        if len(path[nxt]) < k:
            heappush(path[nxt], -nxt_d)
            heappush(heap, (nxt_d, nxt))
        elif len(path[nxt]) >= k and path[nxt][0] < -nxt_d:
            heappop(path[nxt])
            heappush(path[nxt], -nxt_d)
            heappush(heap, (nxt_d, nxt))
for p in path:
    print(-p[0] if len(p) == k else -1)
