import sys
sys.stdin = open("./text/11758.txt", "r")
input = sys.stdin.readline
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
ccw = (x2 - x3) * (y1 - y2) - (y2 - y3) * (x1 - x2)
if ccw > 0:
    print(-1)
elif ccw < 0:
    print(1)
else:
    print(0)