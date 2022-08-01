from collections import deque
import sys
sys.stdin = open('./text/1420.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(str, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

Y, X = Split()
board = [list(Str()) for _ in range(Y)]    
graph = [[] for _ in range(2 * Y * X)]
di = ((-1, 0), (1, 0), (0, -1), (0, 1))
for y in range(Y):
    for x in range(X):
        if board[y][x] == "#":
            continue
        if board[y][x] == "K":
            S = (y * X + x) * 2 + 1
        if board[y][x] == "H":
            E = (y * X + x) * 2
        for dy, dx in di:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if board[ny][nx] != "#":
                    graph[(y * X+ x) * 2 + 1].append([((ny) * X + nx) * 2, 1])
                    graph[((ny) * X + nx) * 2].append([(y * X + x)* 2 + 1, 0])
                
for i in range(Y * X):
    graph[i * 2].append([i * 2 + 1, 1])
    graph[i * 2 + 1].append([i * 2, 0])

def BFS():
    Q = deque([S])
    prev = [-1] * (2 * Y * X)
    while Q:
        u = Q.popleft()
        if u == E:
            break
        for v, b in graph[u]:
            if b > 0 and prev[v] < 0:
                prev[v] = u
                Q.append(v)
    return prev
        
result = 0
while True:
    prev = BFS()
    if prev[E] == -1:
        break
    if prev[E] == S:
        result = -1
        break
    u = E
    while u != S:
        for i in range(len(graph[u])):
            if graph[u][i][0] == prev[u]:
                graph[u][i][1] += 1
                break
        for i in range(len(graph[prev[u]])):
            if graph[prev[u]][i][0] == u:
                graph[prev[u]][i][1] -= 1
                break
        u = prev[u]
    result += 1
print(result)