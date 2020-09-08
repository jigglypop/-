import sys
from pprint import pprint
sys.stdin = open("1780.txt", "r")

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = 0
result0 = 0
result1 = 0


def cut(x, y, n):
    global result, result0, result1
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        cut(x+n//3*a, y+n//3*b, n//3)
                return

    if check == -1:
        result += 1
    elif check == 0:
        result0 += 1
    elif check == 1:
        result1 += 1


cut(0, 0, N)
print(result)
print(result0)
print(result1)
