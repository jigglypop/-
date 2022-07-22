from pprint import pprint
import sys
from math import ceil, log2

sys.setrecursionlimit(10**5)
sys.stdin = open('./text/2820.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def update(i, x):
	while i <= count:
		tree[i] += x
		i += (i & -i)

def query(i):
	res = 0
	while i:
		res += tree[i]
		i -= (i & -i)
	return res

count = 0
def dfs(u):
	global count
	count += 1
	tin[u] = count
	for v in graph[u]:
		dfs(v)
	tout[u] = count

N, M = Split()
graph = [[] for _ in range(N + 1)]
cost = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    if i == 1: 
        cost[i] = Int()
    else:
        cost[i], parent = Split()
        graph[parent].append(i)

tin = [0 for _ in range(N + 1)]
tout = [0 for _ in range(N + 1)]
dfs(1)
tree = [0 for _ in range(count + 1)]

for _ in range(M):
    temp = list(input().split())
    if temp[0] == 'p':
        update(tin[int(temp[1])] + 1, int(temp[2]))
        update(tout[int(temp[1]) ]+ 1, -int(temp[2]))
    else:
        print(cost[int(temp[1])] + query(tin[int(temp[1])]))