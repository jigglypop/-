import sys
from collections import deque
sys.stdin = open('1966.txt', 'r')


tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    result = []
    index = deque(range(N))
    count = 1
    while Q:
        if Q[0] == max(Q):
            if index[0] == M:
                break
            else:
                index.popleft()
                Q.popleft()
                count += 1
        else:
            idx = index.popleft()
            index.append(idx)
            q = Q.popleft()
            Q.append(q)
    print(count)
