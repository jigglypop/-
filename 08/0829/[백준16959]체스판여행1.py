import sys
from pprint import pprint
from collections import deque
sys.stdin = open("16959.txt", "r")

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
check = [[0, 0] for _ in range(N**2+1)]
move = (((-2, 1), (-2, -1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2)),
        ((-1, -1), (1, 1), (-1, 1), (1, -1)), ((0, -1), (0, 1), (1, 0), (-1, 0)))


def go(start, end, di):
    y, x = start
    ey, ex = end
    dy, dx = di
    while True:
        if y == ey and x == ex:
            return True
        if 0 <= y < N and 0 <= x < N:
            y += dy
            x += dx
        else:
            return False


for y in range(N):
    for x in range(N):
        check[board[y][x]][0] = y
        check[board[y][x]][1] = x
result = 0
Q = deque([[0, 1, 0], [1, 1, 0], [2, 1, 0]])
while Q:
    unit, start, count = Q.popleft()
    print(start)
    if start == N:
        result = count
        break
    # 유닛이 가능한지 검사
    flag = False
    if unit == 0:
        for di in move[0]:
            y, x = di[0] + check[start][0], di[1] + check[start][1]
            if 0 <= y < N and 0 <= x < N and y == check[start + 1][0] and x == check[start+1][0]:
                Q.append([0, start+1, count+1])
                flag = True
        if not flag:
            Q.append((1, start, count+1))
            Q.append((2, start, count+1))
    elif unit == 1:
        for di in move[1]:
            flag = go(check[start], check[start+1], di)
        if flag:
            Q.append((1, start+1, count+1))
        else:
            Q.append((0, start, count+1))
            Q.append((2, start, count+1))
    else:
        for di in move[2]:
            flag = go(check[start], check[start+1], di)
        if flag:
            Q.append((2, start+1, count+1))
        else:
            Q.append((0, start, count+1))
            Q.append((1, start, count+1))
