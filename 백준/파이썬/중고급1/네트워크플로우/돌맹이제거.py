import sys
from pprint import pprint
sys.stdin = open('1867.txt')

n, k = map(int, input().split())
N = 2 * n + k
graph = [[] for _ in range(N+1)]
parent = [-1 for _ in range(N+1)]
for i in range(k):
    y, x = map(int, input().split())
    x += n
    z = i + 2 * n + 1
    graph[y].append(z)
    graph[x].append(z)
print(graph)
