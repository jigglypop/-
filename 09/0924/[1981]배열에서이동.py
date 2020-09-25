import sys
from collections import deque
from heapq import heappush, heappop
sys.stdin = open('1981.txt', 'r')
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
di = ((1, 0), (-1, 0), (0, 1), (0, -1))
heap = []
heappush(heap, (0, board[0][0], board[0][0], 0, 0))
visited = [[[0] * 201 for _ in range(n+1)] for _ in range(n+1)]
while heap:
    count, _max, _min, y, x = heappop(heap)
    if y == n-1 and x == n-1:
        print(count)
        exit(0)
    if visited[y][x][_min]:
        continue
    visited[y][x][_min] = 1
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            Max = max(_max, board[ny][nx])
            Min = min(_min, board[ny][nx])
            if not visited[ny][nx][Min]:
                heappush(heap, (Max-Min, Max, Min, ny, nx))
