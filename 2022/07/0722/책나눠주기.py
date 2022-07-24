from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/9576.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

for _ in range(Int()):
    N, M = Split()
    pred = [-1 for _ in range(N + 1)]
    books = [False] * (N + 1)
    board = [List() for _ in range(M)]
    board.sort(key = lambda x: x[1])
    result = 0
    for a, b in board:
        for i in range(a, b + 1):
            if not books[i]:
                result += 1
                books[i] = True
                break
    print(result)