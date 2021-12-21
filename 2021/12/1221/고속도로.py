import sys
sys.stdin = open("./text/10254.txt", "r")
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

for _ in range(int(input())):
    N = int(input())
    point = [list(map(int, input().split())) for _ in range(N)]
    point.sort()
    U = []
    L = []
    for p in point:
        while len(U) > 1 and ccw(U[-2], U[-1], p) <= 0:
            U.pop()
        while len(L) > 1 and ccw(L[-2], L[-1], p) >= 0:
            L.pop()
        U.append(p)
        L.append(p)
    T = U + L[::-1][1:-1]
    print(T)
    s, e = 0, len(U) - 1
    Max = -1
    while e < len(T) :
        A, B = T[s], T[e]
        W = dist(A, B)
        if W >= Max:
            result = A + B
            Max = W
        s += 1
        e += 1
    print(*result)
