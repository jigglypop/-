import sys
sys.stdin = open("4811.txt", "r")
DP = [[-1] * 31 for _ in range(31)]


def go(F, H):
    if DP[F][H] != -1:
        return DP[F][H]
    if F == 0:
        return 1
    if H == 0:
        DP[F][H] = go(F-1, H+1)
        return DP[F][H]
    DP[F][H] = go(F-1, H+1) + go(F, H-1)
    return DP[F][H]


while True:
    N = int(input())
    if N == 0:
        break
    print(go(N, 0))
