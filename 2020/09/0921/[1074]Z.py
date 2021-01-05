import sys
from pprint import pprint
sys.setrecursionlimit(10**5)
sys.stdin = open('1074.txt', 'r')
N, X, Y = map(int, input().split())
idx = 0


def solve(x, y, n):
    global idx
    if not (x <= X < x+n and y <= Y < y+n):
        idx += n*n
        return
    if(n == 1):
        if (x, y) == (X, Y):
            print(idx)
            exit()
        idx += 1
        return
    n //= 2
    solve(x, y, n)
    solve(x, y+n, n)
    solve(x+n, y, n)
    solve(x+n, y+n, n)


solve(0, 0, 1 << N)
