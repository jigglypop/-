import sys
sys.stdin = open('./text/1708.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(200000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
N = Int()
points = [list(Split()) for _ in range(N)]
def ccw(A, B, C):return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
U = []
L = []
points.sort()
for point in points:
    while len(U) >= 2 and ccw(U[-2], U[-1], point) <= 0:U.pop()
    while len(L) >= 2 and ccw(L[-2], L[-1], point) >= 0:L.pop()
    U.append(point)
    L.append(point)
print(len(U) + len(L) - 2)