import sys
sys.stdin = open('2609.txt', 'r')
input = sys.stdin.readline
A, B = map(int, input().split())


def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)


g = gcd(A, B)
print(g)
print(g * (A // g) * (B // g))
