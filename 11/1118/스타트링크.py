import sys
from collections import deque
sys.stdin = open('5014.txt', 'r')

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())

check = [False] * (F+1)
visited = [0] * (F+1)
Q = deque([S])
check[S] = True
while Q:
    u = Q.popleft()
    for w in [U, -D]:
        v = u + w
        if 1 <= v <= F:
            if check[v] == False:
                check[v] = True
                visited[v] = visited[u] + 1
                Q.append(v)
if check[G]:
    print(visited[G])
else:
    print("use the stairs")
