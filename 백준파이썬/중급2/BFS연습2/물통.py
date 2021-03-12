import sys
from pprint import pprint
from collections import deque
sys.stdin = open("2251.txt", "r")
input = sys.stdin.readline
a, b, c = map(int, input().split())
check, limit = set(), [a, b, c]
result = [0 for _ in range(c+1)]
orders = ((0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2))
Q = deque([[0, 0, c]])
check.add((0, 0, c))
while Q:
    now = Q.popleft()
    if now[0] == 0:
        result[now[2]] = 1
    for u, v in orders:
        _now = now[::]
        if now[u] + now[v] > limit[v]:
            _now[u] = now[u] + now[v] - limit[v]
            _now[v] = limit[v]
        else:
            _now[u] = 0
            _now[v] = now[u] + now[v]
        if tuple(_now) not in check:
            check.add(tuple(_now))
            Q.append(_now)

for i in range(c+1):
    if result[i] == 1:
        print(i, end=' ')
