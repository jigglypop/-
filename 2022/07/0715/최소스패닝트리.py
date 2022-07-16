
import sys
sys.stdin = open('./text/1197.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

N, M = Split()
edges = []
for _ in range(M):
    a, b, c = Split()
    edges.append((c, a, b))
edges.sort()
result = 0
parent = [i for i in range(N + 1)]
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c
print(result)