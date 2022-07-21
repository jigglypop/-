from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/7576.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

X, Y = Split()
board = [List() for _ in range(Y)]
Q = deque()
for y in range(Y):
    for x in range(X):
        if board[y][x] == 1:
            Q.append((y, x))
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
Max = 0
while Q:
    y, x = Q.popleft()
    for dy, dx in di:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                Max = max(Max, board[ny][nx])
                Q.append((ny, nx))

def solve():
    Max = 0
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 0:
                return -1
            Max = max(Max, board[y][x])
    return Max - 1

print(solve())