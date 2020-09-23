import sys
sys.stdin = open('11780.txt', 'r')
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = 10**9
graph = [[INF] * (N+1) for _ in range(N+1)]
path = [[-1] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c
        path[a][b] = e
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k]
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=" ")
    print()


def go(x, y):
    if path[x][y] == -1:
        print(0)
        return
    q = []
    q.append(x)
    while x != y:
        x = path[x][y]
        q.append(x)
    print(len(q), end=" ")
    while q:
        print(q.pop(0), end=" ")
    print()
    return


for y in range(1, N+1):
    for x in range(1, N+1):
        if y == x or graph[y][x] == 0:
            print(0)
        else:
            go(y, x)
