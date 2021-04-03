import sys
from pprint import pprint
sys.stdin = open('1348.txt', 'r')
Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
pprint(board)
