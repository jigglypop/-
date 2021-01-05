import sys
from collections import deque
sys.stdin = open('11866.txt', 'r')

N, M = map(int, input().split())
Q = deque([i for i in range(1, N+1)])
result = []
while Q:
    for _ in range(M-1):
        Q.rotate(-1)
    result.append(str(Q.popleft()))
print('<', end="")
print(', '.join(result),  end="")
print('>')
