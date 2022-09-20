from copy import copy, deepcopy
import sys
sys.stdin = open('./text/1201.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [deepcopy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [deepcopy(v) for _ in range(Args[0])]
    return A([deepcopy(v) for _ in range(Args.pop())], Args)

N, M, K = Split()
if N < M + K - 1 or N > M * K:
    print(-1)
else:
    nums = [i for i in range(1, N + 1)]
    group = [K] + [1] * (M - 1)
    N -= K + (1 * (M - 1))
    i = 1
    while N > 0 and i < len(group):
        group[i] += min(K - 1, N)
        N -= (K - 1)
        i += 1
    j = 0
    for g in group:
        k = j + g
        print(*nums[j:k][::-1], end=" ")
        j = k