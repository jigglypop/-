from pprint import pprint
import sys
sys.stdin = open("./text/1199.txt")
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
N = Int()
dp = [list(Split()) for _ in range(N)]
graph = {}
for i in range(N):
    graph[i] = []
    sums = 0
    for j in range(N):
        for k in range(dp[i][j]):
            sums += 1
            graph[i].append(j)
    if sums % 2 == 1:
        print(-1)
        sys.exit()

S = [0]
while S:
    u = S.pop()
    for v in graph[u]:
        if dp[u][v]:
            dp[u][v]-=1
            dp[v][u]-=1
            S.append(v)
    print(u + 1,end=" ")
