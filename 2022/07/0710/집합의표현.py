import sys
sys.stdin = open("./text/1717.txt", 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = Split()
parent = [i for i in range(N + 1)]

for _ in range(M):
    a, b, c = Split()
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
