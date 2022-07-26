from collections import deque
import sys
sys.setrecursionlimit(500000)
sys.stdin = open('./text/1865.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
INF = sys.maxsize
for _ in range(Int()):
    N, M, W = Split()
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = Split()
        graph[a].append((b, c))
        graph[b].append((a, c))
    for _ in range(W):
        a, b, c = Split()
        graph[a].append((b, -c))

    dp = [INF] * (N + 1)
    dp[1] = 0
    result = "NO"
    for i in range(N):
        for u in range(1, N + 1):
            for v, w in graph[u]:
                if dp[v] > dp[u] + w:
                    dp[v] = dp[u] + w
                    if i == N - 1:
                        result = "YES"
                        break

    print(result)
