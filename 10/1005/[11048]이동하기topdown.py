import sys
sys.stdin = open('11048.txt', 'r')
sys.setrecursionlimit(1000*1000)
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[0] * (M+1)] + [[0] + list(map(int, input().split()))
                     for _ in range(N)]
DP = [[-1] * (M+1) for _ in range(N+1)]


def go(y, x):
    if y > N or x > M:
        return 0
    if DP[y][x] >= 0:
        return DP[y][x]
    DP[y][x] = max(go(y+1, x), go(y, x+1)) + A[y][x]
    return DP[y][x]


print(go(1, 1))
