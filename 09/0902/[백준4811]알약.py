from sys import *
stdin = open("4811.txt", "r")
input = stdin.readline


def DP(one, half):
    if one < 0 or half < 0:
        return 0
    if one == 0 and half == 0:
        return 1
    if memo[one][half] != -1:
        return memo[one][half]
    memo[one][half] = DP(one-1, half+1)+DP(one, half-1)
    return memo[one][half]


memo = [[-1] * 31 for i in range(31)]
while 1:
    a = int(input())
    if a == 0:
        break
    print(DP(a, 0))
