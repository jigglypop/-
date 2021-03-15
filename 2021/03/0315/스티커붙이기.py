import sys
sys.stdin = open("18808.txt", "r")
input = sys.stdin.readline


def rotate(board):
    Y = len(board)
    X = len(board[0])
    copy = [[0] * Y for _ in range(X)]
    for y in range(Y):
        for x in range(X):
            copy[x][Y-y-1] = board[y][x]
    return copy


def isDraw(sy, sx, board):
    Y = len(board)
    X = len(board[0])
    for y in range(Y):
        for x in range(X):
            if maps[sy+y][sx+x] == 1 and board[y][x] == 1:
                return False
    return True


def draw(sy, sx, board):
    Y = len(board)
    X = len(board[0])
    count = 0
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 1:
                maps[sy+y][sx+x] = 1
                count += 1
    return count


def go(piece):
    result = 0
    for _ in range(4):
        py, px = len(piece), len(piece[0])
        point = []
        for sy in range(Y-py+1):
            for sx in range(X-px+1):
                if isDraw(sy, sx, piece):
                    result += draw(sy, sx, piece)
                    return result
        piece = rotate(piece)
    return result


Y, X, K = map(int, input().split())
maps = [[0] * X for _ in range(Y)]
count = 0
for _ in range(K):
    y, x = map(int, input().split())
    piece = [list(map(int, input().split())) for _ in range(y)]
    count += go(piece)
print(count)
