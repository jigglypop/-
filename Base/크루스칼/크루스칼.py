import sys
sys.stdin = open("크루스칼.txt", 'r')

V, E = map(int, input().split())
# parent 만들기
parent = [i for i in range(V+1)]

# 비용순으로 정렬된 간선 만들기
edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
result = 0

# 유니온 파인드


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

# 크루스칼


for edge in edges:
    cost, a, b = edge
    # 루트 노드가 같지 않으면 집합에 포함(사이클이 발생하지 않는 경우)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
print(result)
