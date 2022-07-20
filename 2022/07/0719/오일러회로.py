from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/1199.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

n = Int()
v = [List() for _ in [0] * n]
a = [deque(i[0]for i in enumerate(j) if i[1]) for j in v]

def solve():
    if sum(sum(i) % 2 for i in v):
        print(-1)
        return
    s, t = [0], []
    while s:
        c = s[-1]
        if a[c]:
            x = a[c].pop()
            if v[c][x]:
                v[c][x] -= 1
                v[x][c] -= 1
                s.append(x)
            if v[c][x]:
                a[c].appendleft(x)
        else:
            t.append(s.pop())
    print(*[i + 1 for i in t])

solve()