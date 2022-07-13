import sys
from math import *
sys.stdin = open('./text/4195.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(str, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

def find(x):
    if parent[x] == x: 
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x
        count[x] += count[y]
    print(count[x])

for _ in range(Int()):
    num = Int()
    parent, count = {}, {}
    for i in range(num):
        a, b = Split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        union(a, b)