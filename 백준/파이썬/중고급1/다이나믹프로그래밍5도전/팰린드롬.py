import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1243.txt', 'r')
N = int(input())
L = int(input())
words = [input() for _ in range(N)]
print(words)
