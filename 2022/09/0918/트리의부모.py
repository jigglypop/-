from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('./text/11725.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [copy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [copy(v) for _ in range(Args[0])]
    return A([copy(v) for _ in range(Args.pop())], Args)


N = Int()
tree = A([], N + 1)
parent = [0] * (N + 1)
for _ in range(N - 1):
    u, v = Split()
    tree[u].append(v)
    tree[v].append(u)

def dfs(u):
    for v in tree[u]:
        if not parent[v]:
            parent[v] = u
            dfs(v)
    
dfs(1)
print(*parent[2:], sep="\n")