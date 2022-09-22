from copy import copy, deepcopy
import sys
from unittest import result
sys.stdin = open('./text/2805.txt', 'r')
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

N, M = Split()
trees = List()
lo, hi = 1, max(trees)
while lo <= hi:
    mid = (lo + hi) // 2
    cut = 0 
    for tree in trees:
        if tree >= mid:
            cut += tree - mid
    if cut >= M:
        lo = mid + 1
    else:
        hi = mid - 1
print(lo)