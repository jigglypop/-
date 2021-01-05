import sys
from collections import deque
sys.stdin = open('14395.txt', 'r')

input = sys.stdin.readline
s, t = map(int, input().split())
Q = deque()
check = set()
Q.append((s, ''))
check.add(s)
MAX = 10e9

if s == t:
    print(0)
else:
    res = -1
    while Q:
        c_v, c_s = Q.popleft()
        if c_v == t:
            res = c_s
            print(res)
            exit(0)
        n_v = c_v * c_v
        if 0 <= n_v <= MAX and n_v not in check:
            Q.append((n_v, c_s+'*'))
            check.add(n_v)
        n_v = c_v + c_v
        if 0 <= n_v <= MAX and n_v not in check:
            Q.append((n_v, c_s+'+'))
            check.add(n_v)
        n_v = 1
        if n_v not in check:
            Q.append((n_v, c_s+'/'))
            check.add(n_v)
    print(res)
