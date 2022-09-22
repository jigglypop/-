from bisect import bisect_left, bisect_right
from copy import copy, deepcopy
import sys
sys.stdin = open('./text/10816.txt', 'r')
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
nums = List()
nums.sort()
M = Int()
for m in List():
    print(bisect_right(nums, m) - bisect_left(nums, m), end = " ")
