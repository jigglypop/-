from pprint import pprint
import sys
sys.stdin = open('./text/1012.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

for _ in range(Int()):
    X, Y, K = Split()
    board = [[0] * X for _ in range(Y)]
    for _ in range(K):
        x, y = Split()
        board[y][x] = 1
    
    
    def dfs(sy, sx):
        di = ((-1, 0), (1, 0), (0, 1), (0, -1))
        S = [(sy, sx)]
        board[sy][sx] = 0
        while S:
            y, x = S.pop()
            for dy, dx in di:
                ny, nx = y + dy, x + dx
                if 0 <= ny < Y and 0 <= nx < X and board[ny][nx] == 1:
                    board[ny][nx] = 0
                    S.append((ny, nx))
    count = 0
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 1:
                dfs(y, x)
                count += 1
    print(count)