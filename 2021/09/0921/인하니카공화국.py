from pprint import pprint
import sys
sys.stdin = open("./12784.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

def dfs(cur):
    visited[cur] = 1 
    count = 0
    for i in tree[cur]:
        if not visited[i[0]]:
            count += min(i[1],  dfs(i[0]))
    if count == 0:
        return INF
    else:
        return count

for _ in range(int(input())):
    n,m = map(int, input().split())
    tree=[[] for _ in range(n+1)]
    visited = [0] *(n+1)
    for _ in range(m):
        a, b, c = map(int,input().split())
        tree[a].append([b, c])
        tree[b].append([a, c])
    if n == 1:
        print(0)
    else:
        print(dfs(1))