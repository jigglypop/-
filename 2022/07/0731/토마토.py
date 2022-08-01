from collections import deque
import sys
sys.stdin = open('./text/7569.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def BFS():
    di = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
    Q = deque()
    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if board[z][y][x] == 1:
                    Q.append((z,y,x))
                    visit[z][y][x] = 1
                if board[z][y][x] == -1:
                    visit[z][y][x] = -1
    while Q:
        z, y, x = Q.popleft()
        for dz, dy, dx in di:
            nz = z + dz
            ny = y + dy
            nx = x + dx
            if 0 <=nz < Z and 0 <= ny < Y and 0 <= nx < X:
                if visit[nz][ny][nx] == 0 and board[nz][ny][nx] != -1:
                    visit[nz][ny][nx] = visit[z][y][x] + 1
                    Q.append((nz,ny,nx))

X, Y, Z = Split()
board = [[List() for _ in range(Y)] for _ in range(Z)]
visit = [[[0] * X for _ in range(Y)] for _ in range(Z)]
BFS()
Max = 0
flag = sys.maxsize
for z in range(Z):
    for y in range(Y):
        for x in range(X):
            if visit[z][y][x] == 0:
                flag = -1
            Max = max(Max,visit[z][y][x])
            
print(min(Max-1, flag))