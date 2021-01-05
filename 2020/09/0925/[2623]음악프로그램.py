import sys
from collections import deque
sys.stdin = open('2623.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    temp = list(map(int, input().split()))
    for i in range(temp[0], 1, -1):
        a, b = temp[i], temp[i-1]
        graph[b].append(a)
        indegree[a] += 1
Q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)
print(indegree)
print(graph)
result = []
while Q:
    u = Q.popleft()
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            Q.append(v)
    result.append(u)
if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)
