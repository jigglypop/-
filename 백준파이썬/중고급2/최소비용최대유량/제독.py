import sys
sys.stdin = open("3640.txt", "r")
input = sys.stdin.readline
V, E = map(int, input().split())
print(V, E)
