from copy import copy, deepcopy
from collections import deque
import sys
sys.stdin = open('./text/2164.txt', 'r')
input = sys.stdin.readline
def Int():return int(input().strip())
N = Int()
Q = deque([i for i in range(1, N+1)])
while len(Q) > 1:
    Q.popleft()
    move_num = Q.popleft()
    Q.append(move_num)
print(Q[0])
