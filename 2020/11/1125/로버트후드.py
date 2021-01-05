import sys
sys.stdin = open('9240.txt', 'r')

N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]
point.sort()


def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])


def length(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


U = []
L = []
for p in point:
    while len(U) >= 2 and ccw(U[-2], U[-1], p) <= 0:
        U.pop()
    while len(L) >= 2 and ccw(L[-2], L[-1], p) >= 0:
        L.pop()
    U.append(p)
    L.append(p)
result = []
for i in range(len(U)-1):
    result.append(length(U[i], U[i+1]))
for i in range(len(L)-1):
    result.append(length(L[i], L[i+1]))
print(max(result))
