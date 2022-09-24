from copy import copy, deepcopy
from heapq import heappop, heappush
import sys
sys.stdin = open('./text/5972.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def L(v, Args):
    if isinstance(Args, int):
        return [deepcopy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [deepcopy(v) for _ in range(Args[0])]
    return L([deepcopy(v) for _ in range(Args.pop())], Args)

N, M = Split()
graph = L([], N + 1)
INF = sys.maxsize
for _ in range(M):
    a, b, c = Split()
    graph[a].append((c, b))
    graph[b].append((c, a))

dist = [INF] * (N + 1)
dist[1] = 0
Q = [(0, 1)]
while Q:
    w, u = heappop(Q)
    if dist[u] > w:continue
    for cost, v in graph[u]:
        if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost
            heappush(Q, (dist[v], v))
print(dist[N])