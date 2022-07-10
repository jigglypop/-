from itertools import product
import sys
sys.stdin = open("./text/15656.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M = Split()
board = list(Split())
board.sort()
for num in list(product(board, repeat = M)):
    print(*num)