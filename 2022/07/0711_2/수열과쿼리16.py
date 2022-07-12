from pprint import pprint
import sys
sys.stdin = open("./text/14428.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N = Int()
board = [0] * N + list(Split())
for i in reversed(range(1, N)):
    board[i] = min(board[2 * i], board[2 * i ^ 1])

def update(i, x):
    board[i] = x
    while i > 1:
        board[i // 2] = min(board[i], board[i ^ 1])
        i //= 2

def query(l, r):
    result = sys.maxsize
    while l <= r:
        if l % 2 == 1:
            result = min(result, board[l])
            l += 1
        if r % 2 == 0:
            result = min(result, board[r])
            r -= 1
        l >>= 1
        r >>= 1
    return result           

D = N - 1
for _ in range(Int()):
    a, b, c = Split()
    if a == 1: update(b + D, c)
    else: print(query(b + D, c + D))