from heapq import *
import sys
sys.stdin = open("./text/11438.txt", "r")
input = sys.stdin.readline().strip()
V, E = [*sorted(map(int, input.split()))]
print(V, E)