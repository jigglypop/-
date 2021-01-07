from collections import deque
import sys
sys.stdin = open('13913.txt', 'r')
input = sys.stdin.readline


N, K = map(int, input().split())
Max = 10**5
visited = [-1] * (Max + 1)
before = [-1] * (Max + 1)
visited[N] = 0
Q = deque()
Q.append(N)
while Q:
    x = Q.popleft()
    for nx in (x-1, x+1, 2*x):
        if 0 <= nx <= Max and visited[nx] == -1:
            Q.append(nx)
            visited[nx] = visited[x] + 1
            before[nx] = x
S = [K]
check = [False] * (Max + 1)
check[K] = True
result = []
while S:
    u = S.pop()
    result.append(u)
    if u == N:
        break
    v = before[u]
    if not check[v]:
        S.append(v)
        check[v] = True
print(visited[K])
print(*result[::-1])
