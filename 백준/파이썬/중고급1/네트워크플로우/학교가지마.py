import sys
from pprint import pprint
sys.stdin = open('1420.txt')
Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
pprint(board)
