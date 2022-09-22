from copy import copy, deepcopy
import sys
sys.stdin = open('./text/5585.txt', 'r')
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
M = str(1000 - N)
result = 0
M = M[::-1]
for i in range(len(M)):
    temp = int(M[i]) * (10 ** i)
    half = 5 * (10 ** i)
    result += temp // half + (temp % half) // (10 ** i)
print(result)