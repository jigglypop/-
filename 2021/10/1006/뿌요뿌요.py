import sys
from pprint import pprint
sys.stdin = open("./text/11559.txt")
board = [list(input()) for _ in range(12)]
board = list(map(list, list(zip(*board[::-1]))))
Y, X = 6, 12
puyos = "RGBPY"

def clean(board):
    _board = []
    for b in board:
        temp = "".join(b).replace(".", "")
        temp += "." * (12 - len(temp))
        _board.append(list(temp))
    return _board

def dfs(sy, sx, puyo, board):
    visited = [[False] * 12 for _ in range(6)]
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    S = [(sy, sx)]
    visited[sy][sx] = True
    count = 1
    visited_point = [(sy, sx)]
    while S:
        y, x = S.pop()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 6 and 0 <= nx < 12:
                if not visited[ny][nx] and board[ny][nx] == puyo:
                    visited[ny][nx] = True
                    count += 1
                    visited_point.append((ny, nx))
                    S.append((ny, nx))
    if count >= 4:
        for y, x in visited_point:
            board[y][x] = '.'
        return [board, visited_point]
    else:
        return [board, []]
counts = 0
while True:
    result = []
    for y in range(Y):
        for x in range(X):
            if board[y][x] in puyos:
                board, count = dfs(y, x, board[y][x], board)
                result += count
    if len(result) == 0:
        break
    else:
        board = clean(board)
        counts += 1
print(counts)
