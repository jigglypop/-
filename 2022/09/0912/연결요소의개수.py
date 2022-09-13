from pprint import pprint
import sys
sys.stdin = open('./text/11724.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

V, E = Split()
tree = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = Split()
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (V + 1)
count = 0

def dfs(u):
    for v in tree[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v)

for u in range(1, V + 1):
    if not visited[u]:
        dfs(u)
        count += 1
print(count)
