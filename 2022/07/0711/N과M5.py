from itertools import permutations
import sys
sys.stdin = open("./text/15654.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M = Split()
board = list(Split())
board.sort()
for num in list(permutations(board, M)):
    print(*num)