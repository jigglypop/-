from collections import deque
import sys
sys.stdin = open("17071.txt", "r")

n, k = map(int, input().split())
board = [[-1]*500001 for i in range(2)]
board[0][n] = 0


def BFS(k):
    Q = deque([n])
    count = 0
    while Q:
        if board[count % 2][k] >= 0:
            print(count)
            return
        count += 1
        for i in range(len(Q)):
            cur = Q.popleft()
            if cur-1 >= 0:
                if board[count % 2][cur-1] < 0:
                    Q.append(cur-1)
                    board[count % 2][cur-1] = count
            if cur+1 < 500001:
                if board[count % 2][cur+1] < 0:
                    Q.append(cur+1)
                    board[count % 2][cur+1] = count
            if cur*2 < 500001:
                if board[count % 2][cur*2] < 0:
                    board[count % 2][cur*2] = count
                    Q.append(cur*2)
        k += count
        if k > 500000:
            print(-1)
            return


BFS(k)
