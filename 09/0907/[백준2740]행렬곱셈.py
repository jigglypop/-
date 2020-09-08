import sys
from pprint import pprint
sys.stdin = open("2740.txt", "r")
input = sys.stdin.readline


y1, x1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(y1)]
y2, x2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(y2)]
result = [[0]*x2 for _ in range(y1)]
for y in range(y1):
    for x in range(x2):
        for k in range(y2):
            result[y][x] += A[y][k]*B[k][x]
for a in result:
    print(*a)
