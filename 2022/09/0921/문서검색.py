from copy import copy, deepcopy
import re
import sys
sys.stdin = open('./text/1543.txt', 'r')
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

words = Str()
p = Str()
print(len(re.findall(p, words)))