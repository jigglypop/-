from collections import deque
from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/2178.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

Y, X = Split()
board = [list(input().strip()) for _ in range(Y)]
visited = [[0] * X for _ in range(Y)]
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
Q = deque([(0, 0)])
visited[0][0] = 1
while Q:
    y, x = Q.popleft()
    for dy, dx in di:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if not visited[ny][nx] and board[ny][nx] == '1':
                visited[ny][nx] = visited[y][x] + 1
                Q.append([ny, nx])
pprint(visited[Y - 1][X - 1])