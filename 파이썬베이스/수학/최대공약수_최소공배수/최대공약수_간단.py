import sys
sys.stdin = open("2609.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

n, m = N, M
# m을 n으로 나눈 나머지가 0이 될 때까지 나눔
while n > 0:
    m, n = n, m % n

g = m
l = g * (M // g) * (N // g)
print(str(g) + "\n" + str(l))
