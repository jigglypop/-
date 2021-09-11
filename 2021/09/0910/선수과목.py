from collections import deque
import sys
sys.stdin = open('./14567.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
check = [0 for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    check[b] += 1

Q = deque([i for i in range(1, len(check)) if check[i] == 0])
result = []
count = [1 for _ in range(N + 1)]
while Q:
    u = Q.popleft()
    for v in graph[u]:
        check[v] -= 1
        if check[v] == 0:
            count[v] = count[u] + 1
            Q.append(v)
    result.append(u)
print(*count[1:], end=" ")