from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/1199.txt', 'r')
input = sys.stdin.readline
def List():return list(map(int, input().split()))
def Int():return int(input())

N = Int()
visited = [List() for _ in range(N)]
graph = []
for y in range(N):
    Q = deque()
    for x in range(N):
        if visited[y][x] == 1:
            Q.append(x)
    graph.append(Q)

def solve():
    if sum(sum(i) % 2 for i in visited):
        print(-1)
        return
    S, result = [0], []
    while S:
        u = S[-1]
        if graph[u]:
            v = graph[u].pop()
            if visited[u][v]:
                visited[u][v] -= 1
                visited[v][u] -= 1
                S.append(v)
            if visited[u][v]:
                graph[u].appendleft(v)
        else:
            result.append(S.pop())
    print(*[i + 1 for i in result])

solve()