from copy import copy, deepcopy
from heapq import heappop, heappush
from pprint import pprint
from re import S
import sys
sys.stdin = open('./text/1504.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [deepcopy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [deepcopy(v) for _ in range(Args[0])]
    return A([deepcopy(v) for _ in range(Args.pop())], Args)

N, E = Split()
graph = A([], N + 1)
INF = sys.maxsize

for _ in range(E):
    a, b, c = Split()
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(s):
    Q = [(s, 0)]
    di = [INF] * (N + 1)
    di[s] = 0
    while Q:
        u, c = heappop(Q)
        if di[u] < c:continue
        for v, cost in graph[u]:
            if di[v] > di[u] + cost:
                di[v] = di[u] + cost
                heappush(Q, (v, di[v]))
    return di  

a, b = Split()
S = dijkstra(1)
E = dijkstra(N)
_A = dijkstra(a)
_B = dijkstra(b)
result = min(S[a] + _A[b] + E[b], S[b] + _B[a] + E[a])
print(-1 if result >= INF else result)