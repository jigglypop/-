from pprint import pprint
import sys
sys.stdin = open('./text/1931.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def List():return list(map(int, input().strip().split()))

board = [List() for _ in range(Int())]
board.sort(key = lambda x: (x[1], x[0]))
result = [board[0]]
for b in board[1:]:
    if b[0] > result[-1][1]:
        result.append(b)
pprint(len(result))