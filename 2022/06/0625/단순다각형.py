from pprint import pprint
import sys
sys.stdin = open("./text/3679.txt", "r")
input = sys.stdin.readline
N = int(input())

def ccw(A, B, C):
    A = complex(A[0], A[1])
    B = complex(B[0], B[1])
    C = complex(C[0], C[1])    
    return  ((B - A).conjugate() * (C - B)).imag

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

for _ in range(N):
    temp = list(map(int, input().strip().split()))[1:]
    point = []
    j = 0
    for i in range(0, len(temp), 2):
        point.append([temp[i], temp[i + 1], j])
        j += 1
    print(convex_hull(point))
