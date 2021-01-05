import sys
import pprint
from collections import deque
sys.stdin = open('미세먼지안녕.txt','r')

def Print(M):
    for m in M:
        print(m)
    print()

def Turn():
    def Dust(sy, sx):
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dust = M[sy][sx]
        spread = dust // 5
        for dy, dx in dir:
            ny = sy + dy
            nx = sx + dx
            if 0 <= ny < Y and 0 <= nx < X and M[ny][nx] != -1:
                Spread[ny][nx] += spread
                dust -= spread
        original[sy][sx] += dust
    visit = [[0 for _ in range(X)] for _ in range(Y)]
    original = [[0 for _ in range(X)] for _ in range(Y)]
    Spread = [[0 for _ in range(X)] for _ in range(Y)]
    for y in range(Y):
        for x in range(X):
            if M[y][x] > 0:
                Dust(y, x)

    for y in range(Y):
        for x in range(X):
            visit[y][x] = original[y][x] + Spread[y][x]
    return visit

def AirUp(resultB,air):
    visit = [[0 for _ in range(X)] for _ in range(Y)]
    Up = []
    sy,sx = air[0]
    sx += 1
    Up.append((sy,sx))
    visit[sy][sx] = 1
    while sx != X-1 :
        if sy == air[0][0] and sx == air[0][1]: break
        sx += 1
        Up.append((sy,sx))
        visit[sy][sx] = 1
    while sy != 0 :
        if sy == air[0][0] and sx == air[0][1]: break
        sy -= 1
        Up.append((sy,sx))
        visit[sy][sx] = 1
    while sx != 0 :
        if sy == air[0][0] and sx == air[0][1]: break
        sx -= 1
        Up.append((sy,sx))
        visit[sy][sx] = 1
    while sy != air[0][0] :
        if sy == air[0][0] and sx == air[0][1]: break
        sy += 1
        Up.append((sy,sx))
        visit[sy][sx] = 1
    while sx != air[0][1]:
        if sy == air[0][0] and sx == air[0][1]:break
        sx += 1
        Up.append((sy,sx))
        visit[sy][sx] = 1
    result = [[0 for _ in range(X)] for _ in range(Y)]
    for i in range(len(Up)-1):
        sy,sx = Up[i]
        ny,nx = Up[i+1]
        result[ny][nx] = resultB[sy][sx]
    for i in range(len(Up) - 1):
        y, x = Up[i]
        resultB[y][x] = result[y][x]
    return resultA


def AirDown(resultA,air):
    visit = [[0 for _ in range(X)] for _ in range(Y)]

    Down = []
    sy,sx = air[1]
    sx += 1
    Down.append((sy,sx))
    visit[sy][sx] = 1
    while sx != X-1 :
        if sy == air[1][0] and sx == air[1][1]: break
        sx += 1
        Down.append((sy,sx))
        visit[sy][sx] = 1

    while sy != Y-1 :
        if sy == air[0][0] and sx == air[0][1]: break
        sy += 1
        Down.append((sy,sx))
        visit[sy][sx] = 1

    while sx != 0 :
        if sy == air[0][0] and sx == air[0][1]: break
        sx -= 1
        Down.append((sy,sx))
        visit[sy][sx] = 1

    while sy != air[0][0]+1 :
        if sy == air[0][0] and sx == air[0][1]: break
        sy -= 1
        Down.append((sy,sx))
        visit[sy][sx] = 1

    while sx != air[0][1]:
        if sy == air[0][0] and sx == air[0][1]:break
        sx += 1
        Down.append((sy,sx))
        visit[sy][sx] = 1

    result = [[0 for _ in range(X)] for _ in range(Y)]
    for i in range(len(Down)-1):
        sy,sx = Down[i]
        ny,nx = Down[i+1]
        result[ny][nx] = resultA[sy][sx]
    for i in range(len(Down) - 1):
        y, x = Down[i]
        resultA[y][x] = result[y][x]
    return resultA



Y,X,T = map(int,input().split())
M = [list(map(int,input().split())) for _ in range(Y)]
air = []
for y in range(Y):
    for x in range(X):
        if M[y][x] == -1:air.append((y,x))
i = 0
r = []
while i < T:
    i += 1
    resultA = Turn()
    resultB = AirDown(resultA,air)
    resultC =  AirUp(resultB, air)
    M = resultC
    sy1,sx1 = air[0]
    sy2,sx2 = air[1]
    Sum = 0
    for m in M:
        Sum += sum(m)
    r.append(Sum)
    M[sy1][sx1] = -1
    M[sy2][sx2] = -1
print(r[-1])


