import sys
sys.stdin = open('1934.txt', 'r')
input = sys.stdin.readline


def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)


for _ in range(int(input())):
    A, B = map(int, input().split())
    g = gcd(A, B)
    print(g * (A // g) * (B // g))
