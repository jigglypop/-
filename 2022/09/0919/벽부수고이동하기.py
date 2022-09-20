from collections import deque
from copy import copy, deepcopy
from pprint import pprint
import sys
sys.stdin = open('./text/2206.txt', 'r')
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

Y, X = Split()
visited = A(0, [2, Y, X])
board = [list(map(int, list(Str()))) for _ in range(Y)]
Q = deque([(0, 0, 0)])
visited[0][0][0] = 1
di = [(0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]
diz = [(1, -1, 0), (1, 1, 0), (1, 0, 1), (1, 0, -1)]
while Q:
    z, y, x = Q.popleft()
    for dz, dy, dx in di:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if visited[nz][ny][nx] == 0 and board[ny][nx] == 0:
                visited[nz][ny][nx] = visited[z][y][x] + 1
                Q.append((nz, ny, nx))
    if z == 1:continue
    for dz, dy, dx in diz:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if visited[nz][ny][nx] == 0 and board[ny][nx] == 1:
                visited[nz][ny][nx] = visited[z][y][x] + 1
                Q.append((nz, ny, nx))

INF = sys.maxsize
Min = INF
if visited[1][Y - 1][X - 1] != 0:
    Min = min(Min, visited[1][Y - 1][X - 1])
if visited[0][Y - 1][X - 1] != 0:
    Min = min(Min, visited[0][Y - 1][X - 1])
print(-1 if Min == INF else Min)