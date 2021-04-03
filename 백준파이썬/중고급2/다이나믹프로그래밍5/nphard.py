import sys
from pprint import pprint
sys.setrecursionlimit(10**5)
sys.stdin = open('9520.txt', 'r')
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[-1] * N for _ in range(N)]


def go(left, right, now):
    if now == N:
        return 0
    if DP[left][right] != -1:
        return DP[left][right]
    DP[left][right] = min(go(now, right, now+1) + A[left]
                          [now], go(left, now, now+1)+A[right][now])
    return DP[left][right]


print(go(0, 0, 0))
