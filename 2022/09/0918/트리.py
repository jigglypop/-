from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/1991.txt', 'r')
input = sys.stdin.readline
def Split():return map(ord, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
tree = [[] for _ in range(N + 1)]
for _ in range(N):
    a, b, c = Split()
    tree[a - 64].append(b - 64)
    tree[a - 64].append(c - 64)

def order(u, flag):
    if u == -18:
        return
    l, r = tree[u]
    if flag == 0:print(chr(u + 64), end="")
    order(l, flag)
    if flag == 1:print(chr(u + 64), end="")
    order(r, flag)
    if flag == 2:print(chr(u + 64), end="")

order(1, 0)
print()
order(1, 1)
print()
order(1, 2)