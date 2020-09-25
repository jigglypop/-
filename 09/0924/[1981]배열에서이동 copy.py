import sys
from collections import deque
from pprint import pprint
sys.stdin = open('1981.txt', 'r')
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
nums = set()
for b in board:
    nums |= set(b)
nums = sorted(list(nums), reverse=True)


def BFS(start):
    visited = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    Q = deque([(0, 0)])
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    visited[0][0] = [board[0][0], board[0][0]]
    while Q:
        y, x = Q.popleft()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == [0, 0]:
                    Max = max(visited[y][x][0], board[y][x])
                    Min = min(visited[y][x][1], board[y][x])
                    if Max <= start:
                        visited[ny][nx] = [Max, Min]
                        Q.append((ny, nx))
    return visited[n-1][n-1][0] - visited[n-1][n-1][1]


start, end = nums[-1], nums[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    gap = BFS(mid)
    if gap != 0:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
