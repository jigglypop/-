from collections import deque
import sys
sys.stdin = open("1525.txt", "r")

di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
board = [list(map(int, input().split())) for _ in range(3)]
start = 0
for y in range(3):
    for x in range(3):
        if board[y][x] == 0:
            board[y][x] = 9
        start = start * 10 + board[y][x]
Q = deque()
dist = dict()
dist[start] = 0
Q.append(start)
while Q:
    now_num = Q.popleft()
    now = str(now_num)
    z = now.find('9')
    x = z//3
    y = z % 3
    for dy, dx in di:
        ny, nx = y+dy, x+dx
        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = list(now)
            temp[x*3+y], temp[nx*3+ny] = temp[nx*3+ny], temp[x*3+y]
            num = int(''.join(temp))
            if num not in dist:
                dist[num] = dist[now_num] + 1
                Q.append(num)
if 123456789 in dist:
    print(dist[123456789])
else:
    print(-1)
