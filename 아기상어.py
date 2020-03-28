import sys
from collections import deque
sys.stdin = open('아기상어.txt','r')

T = 1
dir_x = [0,-1,1,0]
dir_y = [-1,0,0,1]
def bfs():
    global shark,mapping,catch,size,time, finish
    que =[shark.copy()]
    time_tmp = 0
    cancatch = []
    check = 0
    while que != []:
        length = len(que)
        time_tmp += 1
        for j in range(length):
            y,x = que.pop(0)
            for i in range(4):
                ny = y + dir_y[i]
                nx = x + dir_x[i]
                if ny < 0 or nx < 0 or ny >= N or nx >= N or mapping[ny][nx] > size or visit[ny][nx] == 1:
                    continue
                if mapping[ny][nx] < size and mapping[ny][nx]>0:
                    cancatch.append([ny,nx])
                    check = 1
                visit[ny][nx] = 1
                que.append([ny, nx])

        if check == 1:
            cancatch.sort()
            catch_y,catch_x = cancatch.pop(0)
            time += time_tmp
            mapping[catch_y][catch_x] = 0
            shark = [catch_y, catch_x]
            catch += 1
            if size == catch:
                size += 1
                catch = 0
            return

    finish = True
for _ in range(1,T+1):
    time = 0
    size = 2
    mapping =[]
    N = int(input())
    finish = False
    catch = 0
    for i in range(N):
        map_=list(map(int,input().split()))
        mapping.append(map_)
        for j in range(N):
            if map_[j] == 9:
                mapping[i][j] = 0
                shark = [i,j]
    while finish == False:
        visit = [[0] * N for ppp in range(N)]
        bfs()
    print(time)
