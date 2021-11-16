import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/11405.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
C = [[0] * (N + 2) for _ in range(N + 2)]
F = [[0] * (N + 2) for _ in range(N + 2)]
cost = [[0] * (N + 2) for _ in range(N + 2)]
