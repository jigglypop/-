import sys
from pprint import pprint
sys.stdin = open("2799.txt", "r")


y, x = map(int, input().split())
Y, X = 5 * y, 5 * x
board = [list(input()) for _ in range(Y)]
lists = [0, 0, 0, 0, 0]


def Print(sy, sx):
    board_map = {
        '######....#....#....#....': 0,
        '######****#....#....#....': 1,
        '######****#****#....#....': 2,
        '######****#****#****#....': 3,
        '######****#****#****#****': 4
    }
    words = ''
    for y in range(sy, sy + 5):
        for x in range(sx, sx + 5):
            words += board[y][x]
    lists[board_map[words]] += 1


for y in range(0, Y, 5):
    for x in range(0, X, 5):
        Print(y, x)
print(' '.join(list(map(str, lists))))
