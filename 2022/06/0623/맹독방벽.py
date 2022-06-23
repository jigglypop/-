import sys
from math import *
sys.stdin = open("./text/7420.txt", "r")
input = sys.stdin.readline

N, L = map(int, input().strip().split())

def ccw(a, b, c): 
    return ((b - a).conjugate() * (c - b)).imag

L = [complex(*map(int, input().split())) for _ in range(N)]
L = sorted(L, key=lambda c: (c.real, c.imag))
P = []
Q = []
for p in L:
    while len(P) >= 2 and ccw(P[-2], P[-1], p) >= 0:
        P.pop()
    while len(Q) >= 2 and ccw(Q[-2], Q[-1], p) <= 0:
        Q.pop()
    P.append(p)
    Q.append(p)
print(len(P)+len(Q)-2)
print(P)
print(Q)