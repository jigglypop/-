import sys
sys.stdin = open("2609.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
n, m = N, M
while n > 0:
    m, n = n, m % n
g = m
l = g * (M // g) * (N // g)
print(str(g) + "\n" + str(l))
