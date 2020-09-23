import sys
from pprint import pprint
sys.stdin = open('2580.txt', 'r')


def set_bit(i, j, n):
    m = 1 << n
    row[i] |= m
    col[j] |= m
    sqr[i//3*3 + j//3] |= m


def clear_bit(i, j, n):
    m = ~(1 << n)
    row[i] &= m
    col[j] &= m
    sqr[i//3*3 + j//3] &= m


def is_set(i, j, n):
    return (1 << n) & row[i] & col[j] & sqr[i//3*3 + j//3]


def sudoku(ep):
    if ep >= len(empty):
        for b in brd:
            print(*b)
        sys.exit(0)

    x, y = empty[ep]
    for n in range(1, 10):
        if is_set(x, y, n):
            brd[x][y] = n
            clear_bit(x, y, n)
            sudoku(ep + 1)
            set_bit(x, y, n)


b = 0b1111111111
row, col, sqr = [b] * 9, [b] * 9, [b] * 9
brd, empty = [], []
for i in range(9):
    brd.append([int(x) for x in input().split()])
    for j in range(9):
        if brd[i][j]:
            clear_bit(i, j, brd[i][j])
        else:
            empty.append((i, j))

sudoku(0)
