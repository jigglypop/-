from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/1753.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

INF = sys.maxsize
V, E = Split()
K = Int()
board = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = Split()
    board[u].append((w, v))

dist = [INF] * (V + 1)
Q = []
heappush(Q, (0, K))
dist[K] = 0
while Q:
    w, u = heappop(Q)
    for dw, v in board[u]:
        if dist[v] > w + dw:
            dist[v] = w + dw
            heappush(Q, (w + dw, v))

for d in dist[1:]:
    print("INF") if d == INF else print(d)
