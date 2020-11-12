import sys
sys.stdin = open("2609.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


g = gcd(N, M)
l = g * (M // g) * (N // g)
print(str(g) + "\n" + str(l))
