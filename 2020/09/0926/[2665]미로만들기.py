import sys
from pprint import pprint
from heapq import heappush, heappop
sys.stdin = open('2665.txt', 'r')
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
board = [list(input()) for _ in range(n)]
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
visited = [[INF] * n for _ in range(n)]
heap = [(0, 0, 0)]
visited[0][0] = 0
while heap:
    time, y, x = heappop(heap)
    if y == n-1 and x == n-1:
        break
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            if visited[ny][nx] < time:
                continue
            if board[ny][nx] == '0':
                w = 1
            else:
                w = 0
            alt = time + w
            if visited[ny][nx] > alt:
                visited[ny][nx] = alt
                heappush(heap, (alt, ny, nx))
print(visited[n-1][n-1])
