import sys
sys.stdin = open('11651.txt', 'r')

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points = sorted(points, key=lambda x: (x[1], x[0]))
for point in points:
    print(*point)
