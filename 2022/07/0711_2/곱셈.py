import sys
sys.stdin = open("./text/1629.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

A, B, C = Split()
def _pow(a, b):
    if b == 1:
        return a % C
    else:
        m = _pow(a, b // 2)
        if b % 2 == 0:
            return m * m % C
        else:
            return m * m * a % C

print(_pow(A, B))