import sys
from math import *
sys.stdin = open("./text/3679.txt", "r")
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])


def convex_hull(point):
    U = []
    L = []
    point.sort()
    for p in point:
        while len(U) >= 2 and ccw(U[-2], U[-1], p) <= 0:
            U.pop()
        while len(L) >= 2 and ccw(L[-2], L[-1], p) >= 0:
            L.pop()
        U.append(p)
        L.append(p)
    return U, L

for _ in range(int(input())):
    A = list(map(int, input().strip().split()))[1:]
    point = []
    for i in range(0, len(A), 2):
        point.append([A[i], A[i+1], i // 2])
    print(point)
    print(convex_hull(point))