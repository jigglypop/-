import sys
from pprint import pprint
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("./text/1135.txt", 'r')
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]
for a, b in enumerate(list(map(int, input().split()))):
    if b != -1:
        tree[b].append(a)

dp = [0 for i in range(N + 1)]
def dfs(u):
    temp = []
    for v in tree[u]:
        dfs(v) 
        temp.append(dp[v]) 
    if temp:
        temp.sort(reverse=True) 
        nexts = [temp[i] + i + 1 for i in range(len(temp))] 
        dp[u] = max(nexts)

dfs(0)
print(dp[0])
