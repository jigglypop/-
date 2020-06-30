import sys
from copy import deepcopy
from collections import deque

sys.stdin = open("토마토.txt",'r')

def BFS():
    di = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    Q = deque()
    for h in range(H):
        for y in range(Y):
            for x in range(X):
                if board[h][y][x] == 1:
                    Q.append((h,y,x))
                    visit[h][y][x] = 1
                if board[h][y][x] == -1:
                    visit[h][y][x] = -1
    while Q:
        h,y,x = Q.popleft()
        for dh, dy, dx in di:
            nh = h + dh
            ny = y + dy
            nx = x + dx
            if 0 <=nh < H and 0<= ny < Y and 0<= nx < X:
                if visit[nh][ny][nx] == 0 and board[nh][ny][nx] != -1:
                    visit[nh][ny][nx] = visit[h][y][x] + 1
                    Q.append((nh,ny,nx))


X,Y,H = map(int,input().split())
board = [[list(map(int,input().split())) for _ in range(Y)] for _ in range(H)]
visit = [[[0] * X for _ in range(Y)] for _ in range(H)]
BFS()
Max = 0
flag = 999999999999999
for h in range(H):
    for y in range(Y):
        for x in range(X):
            if visit[h][y][x] == 0:
                flag = -1
            Max = max(Max,visit[h][y][x])
            
print(min(Max-1,flag))