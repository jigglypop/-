from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/2630.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
board = [List() for _ in range(N)]
zero = 0
one = 0

def devide(sy, sx, N):
    global zero, one
    if N == 1:
        if board[sy][sx] == 0:
            zero += 1
        else:
            one += 1
        return 
    flag = board[sy][sx]
    for y in range(sy, sy + N):
        for x in range(sx, sx + N):
            if flag != board[y][x]:
                n = int(N // 2)
                devide(sy, sx, n)
                devide(sy + n, sx, n)
                devide(sy, sx + n, n)
                devide(sy + n, sx + n, n)
                return
    if flag == 0:
        zero += 1
    else:
        one += 1
    return        

devide(0, 0, N)
print(zero)
print(one)