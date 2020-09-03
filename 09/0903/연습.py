from collections import deque
import sys
sys.stdin = open("9328.txt", "r")
di = ((1, 0), (1, 0), (0, 1), (0, -1))
T = int(input())
for _ in range(T):
    Y, X = map(int, input().split())
    board = ['*.' + input() + ".*" for _ in range(Y)]
    Y, X = Y+4, X+4
    board = ['*'*X, '*'+'.'*(X-2)+'*'] + board + ['*'+'.'*(X-2)+'*', '*'*X]
    key = set(input())
    result = 0
    check = [[False] * X for _ in range(Y)]
    Q = deque()
    door = [deque() for _ in range(26)]
    Q.append((1, 1))
    check[1][1] = True
    while Q:
        y, x = Q.popleft()
        for dy, dx in di:
            ny, nx = y + dy, x+dx
            if check[ny][nx]:
                continue
            w = board[ny][nx]
            if w == '*':
                continue
            check[ny][nx] = True
            if w == ".":
                Q.append((ny, nx))
            elif w == "$":
                Q.append((ny, nx))
                result += 1
            elif w.isupper():
                if w.lower() in key:
                    Q.append((ny, nx))
                else:
                    door[ord(w)-ord('A')].append((ny, nx))
            elif w.islower():
                Q.append((ny, nx))
                if not w in key:
                    key.add(w)
                    Q.extend(door[ord(w)-ord('a')])
    print(result)
