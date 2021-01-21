import sys
sys.stdin = open("2609.txt", "r")
input = sys.stdin.readline


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


N, M = map(int, input().split())
g = gcd(N, M)
print(g)
print(N * M//g)
