import sys
from math import *
sys.stdin = open('./text/11758.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]
p1, q1 = Split()
p2, q2 = Split()
p3, q3 = Split()
ccw = (p2 - p3) * (q1 - q2) - (q2 - q3) * (p1 - p2)
if ccw > 0:print(-1)
elif ccw < 0:print(1)
else:print(0)