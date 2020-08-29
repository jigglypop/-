import sys
from collections import deque
sys.stdin = open("12851.txt", "r")

N, K = map(int, input().split())
Q = deque([(N, 0)])
result = 0
count = 0
while Q:
    x, time = Q.popleft()
    if result != 0 and time > result:
        break
    if x == K:
        result = time
        count += 1
    else:
        Q.append((x+1, time+1))
        Q.append((x-1, time+1))
        Q.append((2*x, time+1))
print(result)
print(count)
