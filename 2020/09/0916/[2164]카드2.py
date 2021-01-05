import sys
from collections import deque
sys.stdin = open('2164.txt', 'r')

Q = deque(range(1, int(input())+1))
while len(Q) > 1:
    dummy = Q.popleft()
    num = Q.popleft()
    Q.append(num)
print(Q.popleft())
