import sys
from collections import defaultdict, deque
from pprint import pprint
sys.stdin = open("17142.txt", "r")
input = sys.stdin.readline


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

Q = deque()
for y in range(n):
    for x in range(n):
        if board[y][x] == 2:
            Q.append((y, x))


def BFS(Q):
    di = ((1, 0), (-1, 0), (0, 1), (0, -1))
    print(Q)
    return


BFS(Q)
