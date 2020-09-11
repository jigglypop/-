from collections import deque
import sys
sys.stdin = open("17071.txt", "r")

M = 500000
board = [[-1]*(M+1) for _ in range(2)]
N, K = map(int, input().split())
board[0][N] = 0
Q = deque([(N, 0)])
while Q:
    x, r = Q.popleft()
    k = (r+1) % 2
    if 0 <= x-1 and board[k][x-1] < 0:
        board[k][x-1] = board[r][x]+1
        Q.append((x-1, k))
    if x+1 <= M and board[k][x+1] < 0:
        board[k][x+1] = board[r][x]+1
        Q.append((x+1, k))
    if x*2 <= M and board[k][x*2] < 0:
        board[k][x*2] = board[r][x]+1
        Q.append((x*2, k))
T = 0
S = False
while K+T <= M:
    K += T
    r = T % 2
    if board[r][K] <= T:
        S = True
        break
    T += 1
print(T if S else -1)
