from heapq import heappop, heappush
from pprint import pprint
import sys
from math import *
sys.stdin = open('./text/1976.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

N = Int()
M = Int()
graph = [[] for _ in range(N + 1)]
board = [list(Split()) for _ in range(N)]

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return  parent[x]

def union(x, y):
    parent[max(find(x), find(y))] = min(find(x), find(y))
    
parent = [i for i in range(N + 1)]
for a in range(N):
    for b in range(N):
        if board[a][b] == 1:
            A, B = sorted([a + 1, b + 1])
            union(A, B)

nums = list(Split())
i = parent[nums[0]]
result = "YES"
for num in nums:
    if i != parent[num]:
        result = "NO"
        break
print(result)