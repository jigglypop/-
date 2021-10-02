import sys
from copy import deepcopy
from collections import deque
from pprint import pprint

def P(board):
    for b in board:
        print(b)

sys.stdin = open("./text/3055.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(Y)]
Q = deque()
Wboard = [[-1] * X for _ in range(Y)]
Sboard = [[-1] * X for _ in range(Y)]
start = []
end = []
for y in range(Y):
    for x in range(X):
        if arr[y][x] == 'D':
            end = [y, x]
        elif arr[y][x] == 'S':
            start = [y, x]
            Sboard[y][x] = 0
            arr[y][x] = '.'
        elif arr[y][x] == '*':
            Q.append([y, x])
            Wboard[y][x] = 0

di = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while Q:
    y, x = Q.popleft()
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X and arr[ny][nx] == '.' and Wboard[ny][nx] == -1:
            Wboard[ny][nx] = Wboard[y][x] + 1
            Q.append([ny, nx])

Q.append(start)
while Q:
    y, x = Q.popleft()
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X and arr[ny][nx] in '.D' and Sboard[ny][nx] == -1:
            if Sboard[y][x] + 1 < Wboard[ny][nx] or Wboard[ny][nx] == -1:
                Sboard[ny][nx] = Sboard[y][x] + 1
                Q.append([ny, nx])

if Sboard[end[0]][end[1]] == -1:
    print('KAKTUS')
else:
    print(Sboard[end[0]][end[1]])