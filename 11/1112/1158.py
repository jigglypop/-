import sys
from collections import deque
sys.stdin = open('1158.txt', 'r')

input = sys.stdin.readline
N, K = map(int, input().split())
Q = deque()
for i in range(1, N+1):
    Q.append(i)
print('<', end="")
while Q:
    Q.rotate(-K)
    if len(Q) == 1:
        print(Q.pop(), end="")
    else:
        print(Q.pop(), end=", ")
print('>')
