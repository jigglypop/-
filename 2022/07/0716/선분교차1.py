
import sys
sys.stdin = open('./text/17386.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()

ax, ay, bx, by = Split()
cx, cy, dx, dy = Split()
A, B, C, D = [ax, ay], [bx, by], [cx, cy], [dx, dy]
def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])
if ccw(A, B, C) * ccw(A, B ,D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0:
    print(1)
else:
    print(0)