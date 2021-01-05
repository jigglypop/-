import sys
from collections import deque
sys.stdin = open('1516.txt', 'r')
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
cost = [0] * (N+1)
result = [0] * (N+1)
for i in range(N):
    i += 1
    temp = list(map(int, input().split()))
    cost[i] = temp[0]
    for t in temp[1:-1]:
        graph[t].append(i)
        indegree[i] += 1
Q = deque()
for i in range(1, N+1):
    result[i] = cost[i]
    if indegree[i] == 0:
        Q.append(i)
while Q:
    u = Q.popleft()
    for v in graph[u]:
        indegree[v] -= 1
        result[v] = max(result[v], result[u] + cost[v])
        if indegree[v] == 0:
            Q.append(v)
for r in result[1:]:
    print(r)
