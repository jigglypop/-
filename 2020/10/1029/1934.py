import sys
sys.stdin = open("1934.txt", "r")
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(g * (a // g) * (b // g))
