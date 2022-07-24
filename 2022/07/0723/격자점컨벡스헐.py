import math
from pprint import pprint
import sys
sys.stdin = open('./text/2699.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def ccw(A, B, C):
    return (B[0] + A[0]) * (C[1] + A[1])  - (C[0] + A[0]) * (B[1] + A[1])

def convel_hull(points):
    U = []
    L = []
    for p in points:
        while len(U) > 1 and ccw(U[-2], U[-1], p) <= 0:
            U.pop()
        while len(L) > 1 and ccw(L[-2], L[-1], p) >= 0:
            L.pop()
        U.append(p)
        L.append(p)
    T = U + L[::-1][1:-1]
    T = T[::-1]
    return T

for _ in range(Int()):
    M = Int()
    nums = []
    point = []
    for _ in range(math.ceil(M / 5)):
        nums += List()
    for i in range(0, len(nums), 2):
        point.append([nums[i], nums[i + 1]])
    point.sort()
    T = convel_hull(point)
    start = sorted(T, key = lambda x: (x[1], -x[0]))[-1]
    i = 0
    while True:
        if T[i][0] == start[0] and T[i][1] == start[1]:
            break
        i += 1
        
    results = T[i:] + T[:i]
    print(len(results))
    for result in results:
        print(*result)