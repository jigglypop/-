from pprint import pprint
import sys
sys.stdin = open("./text/2268.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M = Split()
board = [0] * (N + 1)
fenwick = [0] * (N + 1)

def update(fenwick, i, x):
    while i < len(fenwick):
        fenwick[i] += x
        i += (i & -i)

def sum(fenwick, i):
    s = 0
    while i > 0:
        s += fenwick[i]
        i -= (i & -i)
    return s

for _ in range(M):
    a, b, c = Split()
    if a == 1:
        update(fenwick, b, c - board[b])
        board[b] = c
    else:
        if b >= c:
            X = b
            Y = c
        else:
            X = c
            Y = b
        print(sum(fenwick, X) - sum(fenwick, Y-1))