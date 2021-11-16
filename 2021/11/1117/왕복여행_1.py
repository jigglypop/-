import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/2311.txt", "r")
INF= sys.maxsize
N, M = map(int,input().split())
graph = [[]for i in range(N+2)]
cost = [[0] * (N+2) for i in range(N+2)]
C = [[0] * (N + 2) for i in range(N + 2)]
s, e = 0, N + 1
for i in range(M):
    a,b,w=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    cost[a][b] = w
    cost[b][a] = w
    C[a][b] = 1
    C[b][a] = 1

C[s][1]=2
C[N][e]=2
graph[s].append(1)
graph[N].append(e)
def spfa():
    global result
    inQ=[0]*(N+2)
    b=[-1]*(N+2)
    d=[INF]*(N+2)
    Q= deque([s])
    d[s]=0
    inQ[s]=1
    while not Q.empty():
        i=Q.get()
        inQ[i]=0
        for j in graph[i]:
            if C[i][j] == 2 and d[j] > d[i] - cost[i][j]:
                d[j] = d[i] - cost[i][j]
                b[j] = i
                if not inQ[j]:
                    Q.append(j)
                    inQ[j]=1
            if C[i][j] == 1 and d[j] > d[i] + cost[i][j]:
                d[j]=d[i]+cost[i][j]
                b[j]=i
                if not inQ[j]:
                    Q.put(j)
                    inQ[j]=1
    if b[e]==-1:
        return 0
    j=e
    while j!=s:
        i=b[j]
        if C[i][j]==2:result-=cost[i][j]
        else:result+=cost[i][j]
        C[i][j]-=1
        C[j][i]+=1
        j=i
    return 1
result=0
while spfa():
    continue
print(result)