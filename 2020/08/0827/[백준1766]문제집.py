import sys
import heapq
sys.stdin = open('2252.txt', 'rt')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    check[b] += 1

heap = []
for i in range(1, N+1):
    if check[i] == 0:
        heapq.heappush(heap, i)
while heap:
    u = heapq.heappop(heap)
    for v in graph[u]:
        check[v] -= 1
        if check[v] == 0:
            heapq.heappush(heap, v)
    print(u, end=" ")
