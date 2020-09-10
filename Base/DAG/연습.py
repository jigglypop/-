from collections import deque
sys.stdin = open('위상정렬.txt', 'r')

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    check[B] += 1

Q = deque()
result = []
for i in range(1, N+1):
    if check[i] == 0:
        Q.append(i)

while Q:
    u = Q.popleft()
    for v in graph[u]:
        check[v] -= 1
        if check[v] == 0:
            Q.append(v)
    print(u, end=" ")
