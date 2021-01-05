import sys
from pprint import pprint
from collections import deque
sys.stdin = open('5069.txt', 'r')


def Print(board):
    for b in board:
        print(b)


input = sys.stdin.readline
N, M = map(int, input().split())
