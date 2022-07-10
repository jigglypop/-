from pprint import pprint
import sys
sys.stdin = open('./text/9576.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

for _ in range(Int()):
    N, M = Split()
    board = [[] for _ in range(N + 1)]
    parent = [-1 for _ in range(N + 1)]
    