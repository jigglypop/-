import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('10942.txt', 'r')
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
DP = [[-1] * N for _ in range(N)]


def go(i, j):
    if i == j:
        return 1
    elif i == j + 1:
        if A[i] == A[j]:
            return 1
        else:
            return 0
    if DP[i][j] != -1:
        return DP[i][j]
    if A[i] != A[j]:
        DP[i][j] = 0
    else:
        DP[i][j] = go(i+1, j-1)
    return DP[i][j]


for _ in range(int(input())):
    S, E = map(int, input().split())
    print(go(S-1, E-1))
