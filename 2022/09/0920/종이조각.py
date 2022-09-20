from copy import copy, deepcopy
from pprint import pprint
import sys
sys.stdin = open('./text/14391.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def L(v, Args):
    if isinstance(Args, int):
        return [deepcopy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [deepcopy(v) for _ in range(Args[0])]
    return L([deepcopy(v) for _ in range(Args.pop())], Args)


Y, X = Split()
A = [list(Str()) for _ in range(Y)]
MAX = 0
for i in range(1 << (Y * X)):
    vA = L(' ', [Y, X])
    vB = L(' ', [Y, X])
    for y in range(Y):
        for x in range(X):
            j = y * X + x
            if i & (1 << j):
                vA[y][x] = A[y][x]
            else:
                vB[y][x] = A[y][x]
    _vB = L(' ', [X, Y])
    for y in range(Y):
        for x in range(X):
            _vB[x][y] = vB[y][x]

    S = 0
    for y in range(Y):
        temp = ''.join(vA[y]).split(" ")
        S += sum(map(int, filter(lambda x: x != '', temp)))
    for x in range(X):
        temp = ''.join(_vB[x]).split(" ")
        S += sum(map(int, filter(lambda x: x != '', temp)))
    MAX = max(MAX, S)
print(MAX)

