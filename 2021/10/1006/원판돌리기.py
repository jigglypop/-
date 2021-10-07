import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/17822.txt")
n,m,t = map(int,input().split()) 
board = [deque(int(x) for x in input().split()) for _ in range(n)]
info = [[int(x) for x in input().split()] for _ in range(t)] 

for tc in range(t):
    x,d,k = info[tc]
    result = 0
    for i in range(n):
        result += sum(board[i])
        if (i+1)%x == 0:
            if d == 0:
                board[i].rotate(k)
            else:
                board[i].rotate(-k)
    if result != 0:
        have_to_remove = []
        for i in range(n):
            for j in range(m-1):
                if board[i][j] != 0 and board[i][j+1] != 0 and board[i][j] == board[i][j+1]:
                    have_to_remove.append((i,j))
                    have_to_remove.append((i,j+1))

            if board[i][0] != 0 and board[i][-1]!=0 and board[i][0] == board[i][-1]:
                have_to_remove.append((i,0))
                have_to_remove.append((i,m-1))


        for j in range(m):
            for i in range(n-1):
                if board[i][j] != 0 and board[i+1][j] != 0 and board[i][j] == board[i+1][j]:
                    have_to_remove.append((i,j))
                    have_to_remove.append((i+1,j))

        have_to_remove = list(set(have_to_remove))

        for i in range(len(have_to_remove)):
            x,y = have_to_remove[i]
            board[x][y] = 0

        if len(have_to_remove) == 0:
            avg_sum = 0
            zero_cnt = 0
            for i in range(n):
                avg_sum += sum(board[i])
                zero_cnt += board[i].count(0)
            avg = avg_sum / (n*m-zero_cnt)

            for i in range(n):
                for j in range(m):
                    if board[i][j] != 0 and  board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] !=0 and board[i][j] < avg:
                        board[i][j] += 1
    else:
        break
ans = 0
for i in range(n):
    ans += sum(board[i])

print(ans)