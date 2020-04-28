def DFS(v):
    # 시작점을 방문하고, 스택에 push

    # 빈스택이 아닐동안 반복
    # v의 방문하지 않은 인접정점 w에 찾아서
    # w를 방문하고, v를 스택에 push
    # v를 w로 설정
    # 인접정점이 없다면, 스택에서 pop()해서 v로 설정한다.
    S = []
    S.append(v)
    visit[v] = True
    print(v, end=" ")
    while S:
        for w in G[v]:
            if not visit[w]:
                S.append(w)
                v = w
                visit[w] = True
                print(v, end=" ")
                break
        else:
            v = S.pop()
# ----------------------------------------------
# import sys

# sys.stdin = open("DFS_input.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
DFS(1)