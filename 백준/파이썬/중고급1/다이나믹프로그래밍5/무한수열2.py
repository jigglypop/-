import sys
from math import ceil

sys.stdin = open('1354.txt', 'r')

DP = {}
N, P, Q, X, Y = map(int, input().split())


def go(x):
    if x <= 0:
        return 1
    if x in DP:
        return DP[x]
    DP[x] = go(x // P - X) + go(x // Q - Y)
    return DP[x]


print(go(N))
