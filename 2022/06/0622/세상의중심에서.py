import sys
import math
sys.stdin = open("./text/2389.txt", "r")
input = sys.stdin.readline
n = int(input())
point = [[float(i) for i in input().split()] for _ in range(n)]


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex(point):
    point.sort(key=lambda x:(x[0],x[1]))
    if len(point) <=2 :return point
    L = []
    U = []
    for p in point:
        while len(L) >= 2 and ccw(L[-2], L[-1], p) <= 0:
            L.pop()
        L.append(p)
    for P in reversed(point):
        while len(U) >= 2 and ccw(U[-2], U[-1], P) <= 0:
            U.pop()
        U.append(P)
    return L[:-1] + U[:-1]

if n > 1:
    important = convex(point)
    X = 0
    Y = 0
    for i in range(n):
        X += point[i][0]
        Y += point[i][1]
    x = X / n
    y = Y / n
    ratio = 0.1
    for _ in range(30000):
        maxIn = 0
        maxVal = (x - important[0][0])**2 + (y - important[0][1])
        for i in range(len(important)):
            if (tmp:= (x - important[i][0])**2 + (y - important[i][1])**2) > maxVal:
                maxVal = tmp
                maxIn = i
        x += (important[maxIn][0] - x)*ratio
        y += (important[maxIn][1] - y)*ratio
        ratio *= 0.999
    print(f'{x} {y} {math.sqrt((x - important[maxIn][0])**2 + (y - important[maxIn][1])**2)}')
else:
    print(f'{point[0][0]} {point[0][1]} 0')
