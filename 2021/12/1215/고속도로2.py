import sys
sys.stdin = open("./text/10254.txt", "r")

input = sys.stdin.readline
def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])

def cccw(p1, p2, p3, p4):
    _p3 = p4[:]
    _p3[0] -= (p3[0] - p2[0])
    _p3[1] -= (p3[1] - p2[1])
    return ccw(p1, p2, _p3)
    
def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
     
for _ in range(int(input())):
    n = int(input())
    dots = [list(map(int, input().split())) for _ in range(n)]
    dots.sort()
    U = []
    L = []
    for p in dots:
        while len(U) > 1 and ccw(U[-2], U[-1], p) <= 0:
            U.pop()
        while len(L) > 1 and ccw(L[-2], L[-1], p) >= 0:
            L.pop()
        U.append(p)
        L.append(p)
    P = U[:-1] + L[::-1][:-1]
    N = len(P)
    Max = 0
    j = 1
    result = [P[0], P[1]]
    for i in range(N):
        while j + 1 != i and cccw(P[i], P[(i + 1) % N], P[j % N], P[(j + 1) % N]) > 0:
            if dist(P[i], P[j % N]) > Max:
                result = [P[i], P[j % N]]
                Max = dist(*result)
            j += 1
        if dist(P[i], P[j % N]) > Max:
            result = [P[i], P[j % N]]
            Max = dist(*result)
    print(*result[0], *result[1])

