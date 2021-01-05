import sys
from collections import deque, defaultdict
from copy import deepcopy
sys.stdin = open('16946.txt', 'r')

Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
result_board = deepcopy(board)


def DFS(sy, sx, i):
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    S = deque([(sy, sx)])
    board[sy][sx] = str(i)
    result = set()
    result.add((sy, sx))
    while S:
        y, x = S.pop()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if board[ny][nx] == '0':
                    board[ny][nx] = str(i)
                    S.append((ny, nx))
                    result.add((ny, nx))
    return len(result)


results = defaultdict(int)
i = 2
one = []
for y in range(Y):
    for x in range(X):
        if board[y][x] == '0':
            results[str(i)] = DFS(y, x, i)
            i += 1
        if board[y][x] == '1':
            one.append((y, x))
for y, x in one:
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    dist_set = set()
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            i = board[ny][nx]
            dist_set.add(i)
    count = 1
    for dist in list(dist_set):
        count += results[dist]
    result_board[y][x] = str(count % 10)
for result in result_board:
    print(''.join(result))
