import sys
from pprint import pprint
from copy import deepcopy
sys.stdin = open("20058.txt", "r")
input = sys.stdin.readline
N, Q = map(int, input().split())
n = 2 ** 3
maps = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
