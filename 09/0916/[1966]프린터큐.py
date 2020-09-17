import sys
from collections import deque
sys.stdin = open('1966.txt', 'r')


tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    printer = sorted(Q)
    results = []
    print(Q)
    print(N, M)
