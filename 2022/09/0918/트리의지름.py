from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/2263.txt', 'r')
input = sys.stdin.readline
def Split():return map(ord, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
tree = [[] for _ in range(N + 1)]
inOrder = List()
postOrder = List()
inIndex = [0] * (N + 1)
for i in range(N):
    inIndex[inOrder[i]] = i 

def go(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postOrder[post_end]
    print(root, end=" ")
    i = inIndex[root]
    go(in_start, i - 1, post_start, post_start + i - in_start - 1)
    go(i + 1, in_end, post_start + i - in_start, post_end - 1)

go(0, N - 1, 0, N - 1)