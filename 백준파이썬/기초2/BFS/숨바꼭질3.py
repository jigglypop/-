from collections import deque
import sys
sys.stdin = open('13549.txt', 'r')
input = sys.stdin.readline


N, K = map(int, input().split())
Max = 10**5
visited = [-1] * (Max + 1)
visited[N] = 0
Q = deque()
Q.append(N)
while Q:
    x = Q.popleft()
    for nx in (x-1, x+1):
        if 0 <= nx <= Max and visited[nx] == -1:
            Q.append(nx)
            visited[nx] = visited[x] + 1
    if 0 <= 2 * x <= Max and visited[2 * x] == -1:
        Q.append(2*x)
        visited[2*x] = visited[x]
print(visited[K])
