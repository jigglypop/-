import sys
sys.stdin = open('./text/10254.txt', 'r')
input = sys.stdin.readline
def Split():return map(str, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

for _ in range(Int()):
    points = [List() for _ in range(Int())]

    def ccw(A, B, C):
        return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

    def convel_hull(points):
        points.sort()
        L = []
        for point in points:
            while len(L) >= 2 and ccw(L[-2], L[-1], point) < 0:
                L.pop()
            L.append(point)
        U = []
        for point in reversed(points):
            while len(U) >= 2 and ccw(U[-2], U[-1], point) < 0:
                U.pop()
            U.append(point)
        return L[0] + U[0]

    res = convel_hull(points)
    print(*res)
