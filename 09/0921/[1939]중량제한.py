import sys
sys.stdin = open('1939.txt', 'r')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
Max = 0
Min = sys.maxsize
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    Max = max(c, Max)
    Min = min(c, Min)
start, end = map(int, input().split())


def DFS(s, visited, limit):
    S = [s]
    visited[s] = True
    while S:
        u = S.pop()
        if u == end:
            return True
        for v, c in graph[u]:
            if not visited[v] and c >= limit:
                visited[v] = True
                S.append(v)
    return False


result = 0
while Min <= Max:
    mid = (Min + Max) // 2
    if DFS(start, [False] * (N+1), mid):
        result = mid
        Min = mid + 1
    else:
        Max = mid - 1
print(result)
