import sys
from collections import deque
sys.stdin = open('1948.txt', 'r')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
start = [[] for _ in range(N+1)]
end = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
dist = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    start[a].append((b, c))
    end[b].append((a, c))
    indegree[b] += 1
s, e = map(int, input().split())
Q = deque([s])
while Q:
    u = Q.popleft()
    for v, w in start[u]:
        if dist[v] < dist[u] + w:
            dist[v] = dist[u] + w
        indegree[v] -= 1
        if indegree[v] == 0:
            Q.append(v)
count = 0
Q.append(e)
while Q:
    u = Q.popleft()
    for v, w in end[u]:
        if dist[u] - w == dist[v]:
            count += 1
            if indegree[v] == 0:
                Q.append(v)
                indegree[v] = 1
print(dist[e])
print(count)
