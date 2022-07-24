import sys
from heapq import heappop, heappush
sys.stdin = open('./text/1298.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(float, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, M, K = Split()
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = Split()
    graph[a - 1].append((b - 1, c))
path = [[] for _ in range(N)]
Q = []
heappush(path[0], 0)
heappush(Q, (0, 0))
while Q:
    d, u = heappop(Q)
    for i in range(len(graph[u])):
        v, nd = graph[u][i]
        nd += d
        if len(path[v]) < K:
            heappush(path[v], -nd)
            heappush(Q, (nd, v))
        elif len(path[v]) >= K and path[v][0] < -nd:  
            heappop(path[v])
            heappush(path[v], -nd)
            heappush(Q, (nd, v))

for p in path:
    print(-p[0] if len(p) == K else -1)