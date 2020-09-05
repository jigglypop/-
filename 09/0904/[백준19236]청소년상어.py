import sys
from copy import deepcopy

input = sys.stdin.readline
sys.stdin = open("19236.txt", "r")
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
board = []
fishes = {}
for j in range(4):
    tmp = list(map(int, input().split()))
    array = [tmp[2*i] for i in range(4)]
    fishes.update({tmp[2*i]: (i, j, tmp[2*i+1]) for i in range(4)})
    board.append(array)
ans = 0


def is_in(x, y):
    return True if 0 <= x < 4 and 0 <= y < 4 else False


def predict_move(x0, y0, direction, fox):
    x, y = x0 + dx[direction], y0 + dy[direction]
    if is_in(x, y) and (x, y) != fox:
        return x, y, direction
    else:
        direction += -7 if direction == 8 else 1
        return predict_move(x0, y0, direction, fox)


def back(fox, cnt, bd, fish):
    # eat
    global ans
    x0, y0 = fox
    board = deepcopy(bd)
    fishes = deepcopy(fish)
    _, _, direction = fishes.pop(board[y0][x0])
    cnt, board[y0][x0] = cnt+board[y0][x0], 0
    if cnt > ans:
        ans = cnt
    # move
    for i in range(1, 17):
        try:
            x0, y0, d0 = fishes.pop(i)
            x, y, d = predict_move(x0, y0, d0, fox)
            if board[y][x]:
                _, _, d2 = fishes.pop(board[y][x])
                fishes.update({board[y][x]: (x0, y0, d2)})
            fishes.update({board[y0][x0]: (x, y, d)})
            board[y][x], board[y0][x0] = board[y0][x0], board[y][x]
        except KeyError:
            pass
    for k in range(1, 4):
        x, y = fox[0] + k * dx[direction], fox[1] + k * dy[direction]
        if not is_in(x, y):
            break
        if board[y][x]:
            back((x, y), cnt, board, fishes)


back((0, 0), 0, board, fishes)
print(ans)
