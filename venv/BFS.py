from collections import deque
def Print(M):
    for m in M:
        print(m)
    print()


def BFS(start,N):
    Q = deque([start])
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    while Q:
        y,x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny <= N and 0<= nx <= N:
                if M[ny][nx] != 0:continue
                M[ny][nx] = M[y][x] + 1
                Q.append([ny,nx])

# Q를 쓴다
M = [[0,0,0],
     [0,1,0],
     [0,0,0]]
start = (1,1)
BFS(start,2)
Print(M)
