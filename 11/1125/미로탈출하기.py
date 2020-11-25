import sys
sys.setrecursionlimit(10**9)


def Print(maze):
    for m in maze:
        print(m)
    print()


sys.stdin = open('17090.txt', 'r')
Y, X = map(int, input().split())
maze = [['.'] * (X+2)] + [['.'] + list(input())+['.']
                          for _ in range(Y)] + [['.'] * (X+2)]
visited = [[-1] * (X+2) for _ in range(Y+2)]
# U : 위 D : 아래 R : 오른쪽 L : 왼쪽
# 아래로 내려갔는데 U
# 위로 올라갔는데 D
# 왼쪽으로 갔는데 R
# 오른쪽으로 갔는데 L
start = []
for x in range(1, X+1):
    if maze[1][x] == 'U':
        visited[0][x] = 1
        start.append((0, x))
    if maze[Y][x] == 'D':
        visited[Y+1][x] = 1
        start.append((Y+1, x))
for y in range(1, Y+1):
    if maze[y][1] == 'L':
        visited[y][0] = 1
        start.append((y, 0))
    if maze[y][X] == 'R':
        visited[y][X+1] = 1
        start.append((y, X+1))


def go(y, x):
    # U : 위 D : 아래 R : 오른쪽 L : 왼쪽
    # 아래로 내려갔는데 U
    # 위로 올라갔는데 D
    # 왼쪽으로 갔는데 R
    # 오른쪽으로 갔는데 L
    di = ((1, 0), (-1, 0), (0, -1), (0, 1))
    direct = 'UDRL'
    for i in range(4):
        ny = y + di[i][0]
        nx = x + di[i][1]
        if 0 <= ny < Y+2 and 0 <= nx < X+2:
            if maze[ny][nx] == direct[i]:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = 1
                    go(ny, nx)


for y, x in start:
    go(y, x)
    # if maze[y][x] == 'U':
    # elif maze[y][x] == 'R':
    # elif maze[y][x] == 'D':
    # elif maze[y][x] == 'L':
result = 0
for y in range(1, Y+1):
    for x in range(1, X+1):
        if visited[y][x] == 1:
            result += 1
print(result)
