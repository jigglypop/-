import sys
from math import ceil

sys.stdin = open('1351.txt', 'r')

DP = {}
N, P, Q = map(int, input().split())


def go(x):
    if x == 0:
        return 1
    if x in DP:
        return DP[x]
    DP[x] = go(x // P) + go(x // Q)
    return DP[x]


print(go(N))
