import sys
from pprint import pprint
sys.stdin = open('2447.txt', 'r')


def Print(stars):
    for star in stars:
        print(''.join(star))


N = int(input())
stars = [['*']*N for _ in range(N)]


def solve(y, x, n):
    if n == 1:
        return

    n //= 3
    for r in range(y+n, y+2*n):
        for c in range(x+n, x+2*n):
            stars[r][c] = ' '
    solve(y, x, n)
    solve(y+n, x, n)
    solve(y, x+n, n)
    solve(y+2*n, x, n)
    solve(y, x+2*n, n)
    solve(y+n, x+2*n, n)
    solve(y+2*n, x+n, n)
    solve(y+2*n, x+2*n, n)


solve(0, 0, N)
Print(stars)
