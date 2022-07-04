import sys
sys.stdin = open("./text/1976.txt", "r")
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
board = [list(map(int, input().strip().split())) for _ in range(N)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return  parent[x]

def union(x, y):
    parent[max(find(x), find(y))] = min(find(x), find(y))
    
parent = [i for i in range(N + 1)]
for a in range(N):
    for b in range(N):
        if board[a][b] == 1:
            A, B = sorted([a + 1, b + 1])
            union(A, B)

nums = list(map(int, input().strip().split()))
i = parent[nums[0]]
result = "YES"
for num in nums:
    if i != parent[num]:
        result = "NO"
        break
print(result)
        
