import sys
sys.stdin = open("9370.txt", "r")
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    for _ in range(m):
        a, b, d = map(int, input().split())
        print(a, b, d)
    for _ in range(t):
        x = int(input())
        print(x)