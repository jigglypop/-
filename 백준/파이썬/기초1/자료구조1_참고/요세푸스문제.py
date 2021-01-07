import sys
from pprint import pprint
from collections import deque
sys.stdin = open('1158.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
Q = deque([i + 1 for i in range(N)])
print('<', end="")
while Q:
    Q.rotate(-K)
    print(Q.pop(), end="") if len(Q) == 1 else print(Q.pop(), end=", ")
print('>')
