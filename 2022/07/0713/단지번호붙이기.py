from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/2667.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [copy(n) for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

N = Int()
board = [list(Split()) for _ in range(N)]

def bfs(sy, sx):
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    Q = deque([(sy, sx)])
    board[sy][sx] = 0
    result = 1
    while Q:
        y, x = Q.popleft()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    result += 1
                    Q.append((ny, nx))
    return result

count = 0
results = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            results.append(bfs(y, x))
            count += 1
print(count)
for result in sorted(results):
    print(result)