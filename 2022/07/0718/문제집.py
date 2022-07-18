from heapq import heappop, heappush
import sys
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
sys.stdin = open('./text/1766.txt', 'r')
N, M = Split()
graph = [[] for _ in range(N + 1)]
check = [0] * (N + 1)
for _ in range(M):
    a, b = Split()
    graph[a].append(b)
    check[b] += 1
heap = []
for i in range(1, len(check)):
    if check[i] == 0:
        heappush(heap, i)
while heap:
    u = heappop(heap)
    for v in graph[u]:
        check[v] -= 1
        if check[v] == 0:
            heappush(heap, v)
    print(u, end=' ')