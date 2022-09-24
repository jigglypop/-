from copy import copy, deepcopy
from pprint import pprint
import sys
sys.stdin = open('./text/11403.txt', 'r')
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

N = Int()
board = [List() for _ in range(N)]
for z in range(N):
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1 or (board[y][z] == 1 and board[z][x] == 1):
                board[y][x] = 1

for b in board:
    print(*b, end= " ")
    print()
