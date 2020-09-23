import sys
sys.stdin = open('11650.txt', 'r')

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points = sorted(points, key=lambda x: (x[0], x[1]))
for point in points:
    print(*point)
