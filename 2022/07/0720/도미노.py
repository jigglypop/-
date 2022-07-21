import sys
sys.setrecursionlimit(10 ** 4)
sys.stdin = open('./text/4196.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

for _ in range(Int()):
    N, M = Split()
    board = [[] for _ in range(N + 1)]
    rboard = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = Split()
        board[a].append(b)
        rboard[b].append(a)

    def dfs(u, Board, S):
        visited[u] = True
        for v in Board[u]:
            if not visited[v]:
                dfs(v, Board, S)
        S.append(u)

    S = []
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, board, S)

    visited = [False] * (N + 1)
    results = []
    while S:
        scc = []
        i = S.pop()
        if not visited[i]:
            dfs(i, rboard, scc)
            results.append(sorted(scc))
    print(len(results))


