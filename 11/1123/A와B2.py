import sys
sys.stdin = open('12919.txt', 'r')
S = list(input())
T = list(input())
print(1) if S == T else print(0)
