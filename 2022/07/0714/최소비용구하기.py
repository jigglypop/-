
from heapq import heappop, heappush
import sys
sys.stdin = open('./text/1916.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
INF = sys.maxsize
N = Int()
M = Int()
board = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = Split()
    board[a].append((c, b))
dp = [INF] * (N + 1)
S, E = Split()
Q = [(0, S)]
dp[S] = 0
while Q:
    w, u = heappop(Q)
    if dp[u] < w:continue
    for dw, v in board[u]:
        if dp[v] > w + dw:
            dp[v] = w + dw
            heappush(Q, (w + dw, v))
print(dp[E])