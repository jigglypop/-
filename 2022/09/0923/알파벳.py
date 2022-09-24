from copy import copy, deepcopy
from pprint import pprint
import sys
sys.stdin = open('./text/1987.txt', 'r')
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
board = [list(Str()) for _ in range(Y)]
Max = 0
Set = set()

def dfs(y, x, value):
    global Max
    Max = max(Max, value)
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if board[ny][nx] not in Set:
                Set.add(board[ny][nx])
                dfs(ny, nx, value + 1)
                Set.remove(board[ny][nx])

Set.add(board[0][0])
dfs(0, 0, 1)
print(Max)
