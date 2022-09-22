from copy import copy, deepcopy
import sys
sys.stdin = open('./text/2512.txt', 'r')
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

N = Int()
costs = List()
M = Int()
lo, hi = -1, max(costs) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    cut = 0
    for cost in costs:
        cut += min(cost, mid)
    if cut <= M:
        lo = mid
    else:
        hi = mid
print(lo)
