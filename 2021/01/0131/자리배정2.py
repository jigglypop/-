import sys
sys.stdin = open("10157.txt", 'r')


def go(X, Y, n):
    if n > X * Y:
        return 0,
    if n <= Y:
        return 1, n
    x, y = go(Y, X - 1, n - Y)
    return 1 + y, Y - x + 1


X, Y = map(int, input().split())
n = int(input())
print(*go(X, Y, n))
