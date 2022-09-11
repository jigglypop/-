from pprint import pprint
import sys
sys.stdin = open('./text/10026.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
A = [list(input().strip()) for _ in range(N)]
B = [[''] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if A[y][x] == 'R' or A[y][x] == 'G':
            B[y][x] = 'S'
        else:
            B[y][x] = A[y][x]

di = ((-1, 0), (1, 0), (0, 1), (0, -1))

def dfs(sy, sx, flag, board):
    S = [(sy, sx)]
    board[sy][sx] = ''
    while S:
        y, x = S.pop()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == flag:
                    board[ny][nx] = ''
                    S.append((ny, nx))
    return board
    
A_count = 0
B_count = 0
for y in range(N):
    for x in range(N):
        if A[y][x] != '':
            A = dfs(y, x, A[y][x], A)
            A_count += 1
        if B[y][x] != '':
            B = dfs(y, x, B[y][x], B)       
            B_count += 1
print(A_count, B_count)
