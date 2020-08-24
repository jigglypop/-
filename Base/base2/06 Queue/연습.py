import sys
from collections import deque

def BFS(s):     # s = 시작점
    # 큐를 생성
    # 시작점을 방문하고 큐에 삽입
    # 빈큐가 아닐동안
        # 큐에서 하나 꺼내온다. v
        # v의 방문하지 않은 인접정점을 모두 찾아서
            # 차례로 방문하고 큐에 삽입
    Q = deque()
    visit = [False] * (V + 1)
    visit[s] = 1
    Q.append(s)
    while Q:
        v = Q.popleft()
        print(v)
        for w in G[v]:
            if not visit[w]:
                visit[w] = True;print(w)
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)

sys.stdin = open('BFS_input.txt','r')
V,E = map(int,input().split())
G = [[] for _ in range(V+1)]
D = [0] * (V+1)
P = [0] * (V+1)

for _ in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
BFS(1)
print(D)
print(P)

