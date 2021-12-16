import sys
from math import ceil
sys.stdin = open("./text/2699.txt", "r")
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

for _ in range(int(input())):
    N = int(input())
    nums = []
    point = []
    for _ in range(ceil(N / 5)):
        nums += list(map(int, input().split()))
    for i in range(0, len(nums), 2):
        point.append([nums[i], nums[i + 1]])
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
    T = T[::-1]
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

