import sys
import math
sys.stdin = open("./text/1849.txt", "r")
input = sys.stdin.readline

def init(n, s, e):
    if s == e:
        tree[n] = 1
        return 1
    m=(s + e)//2
    tree[n] = init(n * 2, s, m) + init(n * 2 + 1, m + 1, e)
    return tree[n]

def query(n,s,e,val):
    tree[n] -= 1
    if s == e: return s
    m = (s + e) // 2
    if tree[n * 2] >= val:
        return query(n * 2, s, m, val)
    return query(n * 2 + 1, m+1, e, val- tree[n*2])

N = int(input())
tree = [0] * (4 * N)
results = [0 for i in range(N+1)]

init(1,1,N)

for i in range(1, N + 1):
    results[query(1, 1, N, int(input().rstrip())+1)] = i

for result in results[1:]:
    print(result)