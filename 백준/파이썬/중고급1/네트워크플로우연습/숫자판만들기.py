import sys
from pprint import pprint
from collections import deque
sys.stdin = open('2365.txt', 'r')
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
Sum = sum(board[0])


def flow(limit):
    S = 0
    T = 2 * N + 1
    C = [[-1] * (2 * N + 2) for _ in range(2 * N + 2)]
    F = [[-1] * (2 * N + 2) for _ in range(2 * N + 2)]
    graph = [[] for _ in range(2 * N + 2)]
    for i in range(1, N+1):
        C[0][i] = board[0][i - 1]
        graph[0].append(i)
        graph[i].append(0)
    for i in range(N+1, 2 * N+1):
        C[i][2 * N + 1] = board[1][i - N - 1]
        graph[i].append(2 * N + 1)
        graph[2 * N + 1].append(i)
    for y in range(N+1, 2 * N + 1):
        for x in range(1, N+1):
            C[x][y] = limit
            graph[x].append(y)
            graph[y].append(x)

    while True:
        Q = deque([S])
        parent = [-1 for _ in range(2 * N + 2)]
        while Q and parent[T] == -1:
            u = Q.popleft()
            for v in graph[u]:
                if parent[v] == -1 and C[u][v] > F[u][v]:
                    parent[v] = u
                    Q.append(v)
        if parent[v] == -1:
            break
        x = T
        while x != S:
            F[parent[x]][x] += 1
            F[x][parent[x]] -= 1
            x = parent[x]
    result = 0
    for i in range(N + 1, 2 * N + 1):
        result += F[i][T]
    if result == Sum:
        return True
    else:
        return False


lo, hi = 0, Sum
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if not flow(mid):
        lo = mid
    else:
        hi = mid

print(hi)
