import sys
from pprint import pprint
sys.stdin = open("2638.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]


def cheeze():
    di = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = [[0] * X for _ in range(Y)]
    S = [(0, 0)]
    while S:
        y, x = S.pop()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if board[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = -1
                    S.append((ny, nx))
                elif board[ny][nx] == 1:
                    visited[ny][nx] += 1
    count = 0
    for y in range(Y):
        for x in range(X):
            if visited[y][x] >= 2:
                board[y][x] = 0
                count += 1
    return count


count = sum(map(sum, board))
n = 0
while count > 0:
    count -= cheeze()
    n += 1
    pprint(board)
print(n)
